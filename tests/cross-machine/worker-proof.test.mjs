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
  assert.equal(spec.status, "completed_by_linux_dev");
});

test("linux dev gateway proof artifact is present and verified", () => {
  const linuxProofPath = path.join(FIXTURES_DIR, "linux-dev-proof.json");
  assert.ok(fs.existsSync(linuxProofPath), "linux-dev-proof.json must exist");
  const proof = JSON.parse(fs.readFileSync(linuxProofPath, "utf8"));
  assert.equal(proof.protocol, "cross-machine-dev-proof-v1");
  assert.equal(proof.platform, "linux");
  assert.equal(proof.status, "DEV_LINUX_VERIFIED");
  assert.equal(proof.verifiedBy, "Linux Dev Gateway (@Dev)");
});
