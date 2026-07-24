import test from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";

const bytes = await readFile(new URL("../fixtures/mock-data.json", import.meta.url));
const fixtures = JSON.parse(bytes);
test("fixture bytes and opaque synthetic IDs are deterministic", () => {
  assert.deepEqual(JSON.parse(bytes), fixtures);
  const ids = [fixtures.identity.actor_id, fixtures.alerts[0].alert_id, fixtures.alerts[0].version_id, fixtures.locality.locality.locality_id, fixtures.shelters[0].shelter_id];
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(ids.every((id) => id.includes("synthetic")));
});
test("fixture responses preserve safety boundaries", () => {
  const alert = fixtures.alerts[0];
  assert.equal(alert.information_kind, "official_alert");
  assert.equal(createHash("sha256").update(alert.content).digest("hex"), alert.content_hash);
  assert.equal(alert.version_number, 2);
  assert.ok(alert.previous_version_id && alert.source.source_uri && alert.source.signature_status);
  const shelter = fixtures.shelters[0];
  assert.equal(shelter.freshness_status, "stale");
  assert.equal(shelter.official_status, "not_official");
  const serialized = bytes.toString().toLowerCase();
  for (const forbidden of ["phone_number", "email_address", "resident_list", "access_token", "evacuation_order", "dispatch_order", "road_closure"]) assert.ok(!serialized.includes(forbidden));
});
