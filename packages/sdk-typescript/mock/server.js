import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

const fixtures = JSON.parse(await readFile(new URL("../fixtures/mock-data.json", import.meta.url), "utf8"));
const routes = new Map([
  ["/v1/identity/me", fixtures.identity],
  ["/v1/official-alerts", { items: fixtures.alerts, page: { page_size: fixtures.alerts.length, has_more: false, next_cursor: null } }],
  [`/v1/official-alerts/${fixtures.alerts[0].alert_id}`, fixtures.alerts[0]],
  [`/v1/localities/${fixtures.locality.locality.locality_id}`, fixtures.locality],
  ["/v1/shelters", { items: fixtures.shelters, page: { page_size: fixtures.shelters.length, has_more: false, next_cursor: null } }],
]);

export function createMockServer() {
  return createServer((request, response) => {
    const pathname = new URL(request.url ?? "/", "http://mock.invalid").pathname;
    const body = request.method === "GET" ? routes.get(pathname) : undefined;
    response.setHeader("content-type", body ? "application/json; charset=utf-8" : "application/problem+json; charset=utf-8");
    response.setHeader("x-correlation-id", "correlation.synthetic.001");
    if (!body) {
      response.writeHead(request.method === "GET" ? 404 : 405);
      response.end(JSON.stringify({ type: "about:blank", title: "Not found", status: request.method === "GET" ? 404 : 405, code: request.method === "GET" ? "NOT_FOUND" : "METHOD_NOT_ALLOWED", correlation_id: "correlation.synthetic.001" }));
      return;
    }
    response.writeHead(200);
    response.end(JSON.stringify(body));
  });
}

if (process.argv[1] && fileURLToPath(import.meta.url) === fileURLToPath(new URL(`file:///${process.argv[1].replaceAll("\\", "/")}`))) {
  const port = Number(process.env.PORT ?? 4010);
  createMockServer().listen(port, "127.0.0.1", () => console.log(`SafeZone synthetic mock listening on http://127.0.0.1:${port}`));
}
