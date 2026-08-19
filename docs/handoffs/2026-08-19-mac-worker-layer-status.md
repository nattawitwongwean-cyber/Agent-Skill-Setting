# Mac Worker Layer & @Dev Durable Continuation Handoff Status

**Date**: 2026-08-19
**Primary Coordination Repository**: `https://github.com/nattawitwongwean-cyber/Agent-Skill-Setting.git`
**Mac Project Path**: `/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway`
**Mac Feature Branch**: `feature/mac-worker-orchestration` (Commit `33bab07`)
**Cross-Machine Proof Branch**: `cross-machine/proof-2026-08-19` (Linux Commit `96d2aa4`)
**Status Flags**:
- `DEV_CROSS_MACHINE_PROOF=PASS`
- `GIT_DURABLE_HANDOFF=PASS`

---

## 1. System Diagnosis: "This conversation does not support developer MCPs"

- **Origin**: ChatGPT Platform/Session Capability Gate (OpenAI Platform level).
- **Evidence**:
  - Mac Gateway LaunchAgent (`gui/501/com.local.mcp.owner-gateway`) is `state: running` (PID 20429, PPID 1 `launchd`).
  - Probes `http://127.0.0.1:8080/healthz` (`200 live`) and `/readyz` (`200 ready`) succeed.
  - Tunnel client maintains active connection to OpenAI Control Plane (`tunnel_6a8544639b788191a4843710862dad74`).
  - ChatGPT rejected tool calls before sending requests through the tunnel because the specific chat conversation context was not initialized in Developer Mode.
- **Locally Fixable**: No (client/platform gate).
- **Remediation**: Open a fresh chat session on ChatGPT with Developer Mode enabled, or continue operations via the durable Git-based handoff path.

---

## 2. Real @Dev Cross-Machine Proof Evidence

| Step | Machine | Action | Evidence / Result |
|---|---|---|---|
| 1. Baseline Task | Mac | Created branch `cross-machine/proof-2026-08-19` with test spec `proof-spec.json` | Commit `1e13643` pushed to GitHub |
| 2. Linux Execution | `@Dev` (hermes Linux) | Cloned isolated worktree, created fixture `linux-dev-proof.json`, updated tests | Commit `96d2aa4`, `node --test` passed 2/2 |
| 3. Cross-Machine Fetch | Mac | Fetched commit `96d2aa4` from Linux worktree via SSH/Git | Merged `96d2aa4` cleanly |
| 4. Mac Verification | Mac | Ran `node --test tests/cross-machine/worker-proof.test.mjs` independently | `tests 2, pass 2, fail 0` |
| 5. GitHub Push | Mac | Pushed verified proof branch to `nattawitwongwean-cyber/Agent-Skill-Setting.git` | `1e13643..96d2aa4` |

### Sanitized Linux Proof Fixture (`tests/cross-machine/fixtures/linux-dev-proof.json`):
```json
{
  "protocol": "cross-machine-dev-proof-v1",
  "hostname": "hermes-Latitude-E6420",
  "platform": "linux",
  "status": "DEV_LINUX_VERIFIED",
  "kernel": "6.8.0-138-generic",
  "timestamp": "2026-08-19T20:52:30+07:00",
  "testedWith": "node test runner",
  "verifiedBy": "Linux Dev Gateway (@Dev)"
}
```

---

## 3. Worker Layer Tasks Progress (Tasks 1–12)

| Task | Description | Status | Commits / Artifacts |
|---|---|---|---|
| Task 1 | Safe Git Bootstrap & Baseline | `COMPLETE` | `247dbbb` |
| Task 2 | Worker Types, Security & Sanitization | `COMPLETE` | `aa687c3` (`security.ts`, `types.ts`, `security.test.mjs`) |
| Task 3 | Process Registry & Safe Isolated Cancellation | `COMPLETE` | `bf256dd` (`process-registry.ts`, `process-registry.test.mjs`) |
| Task 4 | Worktree Isolation | `COMPLETE` | `cda3188` (`worktree.ts`, `worktree.test.mjs`) |
| Task 5 | Codex Worker Adapter | `COMPLETE` | `78b36b8` (`codex-adapter.ts`, `codex-adapter.test.mjs`) |
| Task 6 | Antigravity Worker Adapter | `COMPLETE` | `37636fa` (`antigravity-adapter.ts`, `antigravity-adapter.test.mjs`) |
| Task 7 | Non-Secret Persistence & Restart Reconciliation | `COMPLETE` | `e29370a` (`persistence.ts`, `persistence.test.mjs`) |
| Task 8 | Worker Manager & Batch Concurrency | `COMPLETE` | `b0ddcf6` (`manager.ts`, `manager.test.mjs`) |
| Task 9 | MCP Worker Tools Catalog (33 tools) | `COMPLETE` | `4db861b` (`mcp-worker-tools.test.mjs`, `src/index.ts`) |
| Task 10 | Real Worker Acceptance Test Suite | `COMPLETE` | `7f138e0` (`external-worker-acceptance.mjs`) |
| Task 11 | Batch / Cancel / Worktree Isolation Acceptance | `COMPLETE` | `7f138e0` |
| Task 12 | LaunchAgent & Real-Topology Lifecycle Integration | `COMPLETE` | Live LaunchAgent verified with 33 tools |

---

## 4. Test Summary

- `npm run typecheck`: `PASS` (0 errors)
- `npm run build`: `PASS` (0 errors)
- `npm test`: `PASS` (Desktop probe: 222ms, 6/6 Lifecycle regression tests)
- `npm run test:workers`: `PASS` (26/26 Unit & Subsystem tests)
- `npm run test:workers:external`: `PASS` (5/5 Acceptance scenarios)
- Cross-Machine Proof (`worker-proof.test.mjs`): `PASS` (Executed and verified on both Linux and Mac)
