# Task: NAG-V01-R1 — Correct V0.1 Review Blockers

- **Directive:** `CG-0003R`
- **Issued By:** ChatGPT review of Gateway PR #1
- **Target:** Antigravity
- **Status:** PENDING
- **Priority:** HIGH
- **Source Repo:** `nattawitwongwean-cyber/Nareerat-Agent-Gateway`
- **Working Branch:** `agent/cg-0003-v0.1`
- **Reviewed Head:** `722b5db6d477f0dba25800e412cb7ca970f5fd39`

## Authoritative Inputs

Read fully before changes:

1. `docs/superpowers/specs/2026-08-18-nareerat-agent-gateway-design.md`
2. `docs/superpowers/plans/2026-08-18-nareerat-agent-gateway-v0.1.md`
3. `docs/superpowers/reviews/2026-08-18-nareerat-agent-gateway-v0.1-review.md`
4. PR #1 review comment on `nattawitwongwean-cyber/Nareerat-Agent-Gateway`
5. `agent-bridge/PROTOCOL.md`
6. `agent-bridge/control/APPROVALS.md`

## Objective

Bring the existing V0.1 implementation into compliance with the already approved Gateway design/plan. This is a corrective continuation of CG-0003, not V0.2 and not CG-0004.

## Required Corrections

### 1. Replace handwritten MCP protocol/transport with supported MCP TypeScript SDK

Current blocker:

- `packages/mcp` implements custom JSON-RPC manually and has no MCP SDK dependency.

Required result:

- use the current supported official/appropriate Model Context Protocol TypeScript SDK,
- implement actual stdio and loopback HTTP/streamable MCP transport through SDK APIs,
- retain `PRO_READ_BRIDGE_WRITE` filtering so write/execute tools are not directly exposed in Pro mode,
- add a real MCP compatibility smoke test using a supported MCP client/inspector/test client rather than only calling internal server methods.

Do not hard-code stale package names from the original plan if the official SDK packaging has changed; verify current package/documentation first and record the exact package/version selected.

### 2. Implement actual Electron tray desktop shell

Current blocker:

- desktop package has no Electron dependency and no Electron `app`, `BrowserWindow`, `Tray`, tray menu or `contextBridge` lifecycle.

Required result:

- install project-local Electron/renderer dependencies needed by the approved V0.1 architecture,
- create real Electron main process,
- create BrowserWindow + system Tray,
- closing main window hides to tray instead of stopping the Gateway,
- tray can reopen the dashboard and Quit stops runtime cleanly,
- preload exposes a narrow sanitized API using Electron context isolation/contextBridge,
- renderer never receives direct unrestricted Node/filesystem/process/SQLite access,
- run one interactive Windows smoke test and record exact observations.

### 3. Replace Antigravity delegation stub with capability-detected fail-closed runner

Current blocker:

- `AntigravityDelegateAdapter` currently formats text and always reports DELEGATED without invoking `agy`.

Required result:

- inspect `agy --version` and `agy --help` without changing authentication/configuration,
- detect safe non-interactive/headless/print capabilities from installed help,
- if supported, invoke with explicit argv, `shell: false`, finite timeout, registered fixture workspace only, no permission-bypass flag,
- if unsupported, report `UNAVAILABLE` rather than fake success,
- native verification remains mandatory after any delegate-created fixture change.

### 4. Add local runtime authentication boundary to loopback HTTP

Current blocker:

- unauthenticated POST endpoint and wildcard CORS.

Required result:

- use a randomly generated machine-local runtime token or an equivalently strong tested local caller boundary,
- keep secret material outside Git and redact it from logs,
- reject unauthenticated/invalid requests,
- restrict browser origin handling; do not leave permissive `Access-Control-Allow-Origin: *` for the mutation-capable local API,
- add positive/negative auth tests.

### 5. Remove generated TypeScript build-state artifacts

Required result:

- add `*.tsbuildinfo` to `.gitignore`,
- remove tracked `tsconfig.tsbuildinfo` files from the branch,
- verify build/typecheck regenerate locally without restaging them.

## Fresh Verification Required

Run on the target Windows machine after fixes:

```powershell
corepack pnpm@10.15.0 test
corepack pnpm@10.15.0 typecheck
corepack pnpm@10.15.0 build
git status --short
git diff --check main...HEAD
```

Additionally verify and record:

```text
MCP_SDK_COMPATIBILITY: PASS|FAIL
ELECTRON_TRAY_SMOKE: PASS|FAIL
ANTIGRAVITY_CAPABILITY: AVAILABLE|UNAVAILABLE
ANTIGRAVITY_SAFE_SMOKE: PASS|FAIL|NOT_RUN
LOCAL_API_AUTH: PASS|FAIL
TSBUILDINFO_TRACKED: NO
```

Update `docs/V0.1-VERIFICATION.md` with the fresh evidence and exact test counts.

## Active Safety Bounds

The existing CG-0003 bounds remain in force:

```text
DO_NOT_TOUCH_PRODUCTION_LMS_LFS: YES
DO_NOT_REGISTER_PRODUCTION_WORKSPACE: YES
DO_NOT_CONFIGURE_SECURE_MCP_TUNNEL: YES
DO_NOT_CREATE_OPENAI_TUNNEL_OR_KEYS: YES
DO_NOT_ENABLE_START_WITH_WINDOWS: YES
DO_NOT_CREATE_WINDOWS_SERVICE: YES
DO_NOT_USE_SYSTEM_PROFILE: YES
DO_NOT_USE_UNRESTRICTED_PROFILE: YES
DO_NOT_RUN_AS_ADMINISTRATOR: YES
DO_NOT_MODIFY_REGISTRY_SERVICE_FIREWALL: YES
DO_NOT_DISABLE_DEFENDER: YES
DO_NOT_FORCE_PUSH: YES
DO_NOT_MERGE_DRAFT_PR: YES
DO_NOT_EXPOSE_SECRETS: YES
```

Project-local dependencies required to satisfy the already approved V0.1 plan are authorized. Do not introduce unrelated features.

## Required End State

Push fixes to the existing `agent/cg-0003-v0.1` branch and keep PR #1 draft/unmerged.

Report:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-0003R
REPLY-TO: CG-0003R
TASK-ID: NAG-V01-R1
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED
SOURCE_BRANCH: agent/cg-0003-v0.1
PR: #1
LATEST_SOURCE_COMMIT: <sha>
TESTS: <exact result>
TYPECHECK: <PASS|FAIL|NOT_RUN>
BUILD: <PASS|FAIL|NOT_RUN>
MCP_SDK_COMPATIBILITY: <PASS|FAIL|NOT_RUN>
ELECTRON_TRAY_SMOKE: <PASS|FAIL|NOT_RUN>
ANTIGRAVITY_CAPABILITY: <AVAILABLE|UNAVAILABLE|NOT_RUN>
ANTIGRAVITY_SAFE_SMOKE: <PASS|FAIL|NOT_RUN>
LOCAL_API_AUTH: <PASS|FAIL|NOT_RUN>
TSBUILDINFO_TRACKED: <YES|NO>
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
SECURITY_ANOMALY: <YES|NO>
NEXT_ACTION: WAIT
```

Do not start CG-0004 until ChatGPT explicitly marks a V0.1 commit as accepted baseline.
