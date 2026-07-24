import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createMockServer } from "../mock/server.js";

const fixtures = JSON.parse(await readFile(new URL("../fixtures/mock-data.json", import.meta.url), "utf8"));
let server;
let baseUrl;
test.before(async () => {
  server = createMockServer();
  await new Promise((resolve, reject) => server.listen(0, "127.0.0.1", resolve).once("error", reject));
  baseUrl = `http://127.0.0.1:${server.address().port}`;
});
test.after(() => new Promise((resolve) => server.close(resolve)));
const cases = [
  ["/v1/identity/me", "actor_id"],
  ["/v1/official-alerts", "items"],
  [`/v1/official-alerts/${fixtures.alerts[0].alert_id}`, "content_hash"],
  [`/v1/localities/${fixtures.locality.locality.locality_id}`, "geometry"],
  ["/v1/shelters", "items"],
];
for (const [path, property] of cases) test(`GET ${path} covers contract response`, async () => {
  const response = await fetch(baseUrl + path);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("x-correlation-id"), "correlation.synthetic.001");
  assert.ok(property in await response.json());
});
test("mock is read-only and does not invent later behavior", async () => {
  assert.equal((await fetch(baseUrl + "/v1/shelters", { method: "POST" })).status, 405);
  assert.equal((await fetch(baseUrl + "/v1/community-reports")).status, 404);
});
