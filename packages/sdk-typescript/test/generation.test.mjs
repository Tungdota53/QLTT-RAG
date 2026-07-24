import test from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
test("generated source is synchronized and byte-stable", async () => {
  execFileSync(process.execPath, ["scripts/generate.mjs", "--check"], { cwd: root });
  const before = await readFile(resolve(root, "src/index.ts"));
  execFileSync(process.execPath, ["scripts/generate.mjs"], { cwd: root });
  const after = await readFile(resolve(root, "src/index.ts"));
  assert.deepEqual(after, before);
  assert.match(after.toString(), /^\/\/ @generated/);
});
