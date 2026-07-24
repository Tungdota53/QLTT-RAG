import assert from "node:assert/strict";
import test from "node:test";

import { createMockServer } from "../../packages/sdk-typescript/mock/server.js";

test("generated SDK mock serves a synthetic read-only integration response", async (context) => {
  const server = createMockServer();
  await new Promise((resolve, reject) => server.listen(0, "127.0.0.1", resolve).once("error", reject));
  context.after(() => new Promise((resolve) => server.close(resolve)));

  const baseUrl = `http://127.0.0.1:${server.address().port}`;
  const response = await fetch(`${baseUrl}/v1/official-alerts`);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("x-correlation-id"), "correlation.synthetic.001");
  const body = await response.json();
  assert.equal(body.items[0].information_kind, "official_alert");
  assert.match(body.items[0].alert_id, /synthetic/);

  const prohibited = await fetch(`${baseUrl}/v1/community-reports`);
  assert.equal(prohibited.status, 404);
});