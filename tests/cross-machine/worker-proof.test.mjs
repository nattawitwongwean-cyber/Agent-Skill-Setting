import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES_DIR = path.join(__dirname, "fixtures");

test("cross-machine baseline proof specification is valid", () => {
  const specPath = path.join(FIXTURES_DIR, "proof-spec.json");
  assert.ok(fs.existsSync(specPath), "proof-spec.json must exist");
  const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
  assert.equal(spec.protocol, "cross-machine-dev-proof-v1");
  assert.equal(spec.status, "awaiting_linux_dev");
});
