# Current Directive

- **Directive:** CG-0003R2
- **Source:** ChatGPT source review + explicit human approval
- **Target:** Antigravity
- **Scope:** Final V0.1 baseline corrections and official Antigravity CLI enablement
- **Date Received:** 2026-08-18
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/NAG-V01-R2.md`
- **Design Spec:** `docs/superpowers/specs/2026-08-18-nareerat-agent-gateway-design.md`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-18-nareerat-agent-gateway-v0.1.md`
- **Review Reference:** Agent-Skill-Setting Issue `#3`

## Purpose

Resolve the final two source-level blockers that remain after AG-0003R, then install/enable the official Google Antigravity CLI (`agy`) under the newly approved user-scope authorization so the future Automatic Agent Bridge Watcher can launch Antigravity safely.

This is still corrective V0.1 work. Do not start CG-0004 yet.

## Required Start Sequence

1. Safely synchronize `Agent-Skill-Setting`.
2. Read `agent-bridge/PROTOCOL.md`.
3. Read the latest `agent-bridge/control/APPROVALS.md` including CG-0003R2 authorization.
4. Read the Gateway Design Spec and V0.1 Implementation Plan.
5. Read Agent-Skill-Setting Issue #3 review findings.
6. Read `agent-bridge/tasks/pending/NAG-V01-R2.md` fully.
7. Check `PROCESSED_MESSAGES.md`; accept `CG-0003R2` exactly once.
8. Open existing Gateway repo/branch `agent/cg-0003-v0.1`; do not replace the repo and do not merge PR #1.
9. Correct the two blockers and perform the approved official `agy` install/enable sequence.
10. Produce fresh verification evidence and hand off as AG-0003R2.

## Blocking Corrections

```text
ELECTRON_ESM_RUNTIME_AND_REAL_TRAY_SMOKE: REQUIRED
ANTIGRAVITY_CAPABILITY_DETECTED_INVOCATION: REQUIRED
OFFICIAL_AGY_INSTALL_OR_ENABLE: APPROVED_AND_REQUIRED_WHEN_NEEDED
```

## Active Bounds

```text
NATIVE_FIRST: YES
SOURCE_REPO_PRIVATE: YES
TEST_FIXTURES_ONLY_FOR_WORKSPACE_WRITES: YES
DO_NOT_TOUCH_PRODUCTION_LMS_LFS: YES
DO_NOT_REGISTER_PRODUCTION_WORKSPACE: YES
DO_NOT_CONFIGURE_SECURE_MCP_TUNNEL: YES
DO_NOT_CREATE_OPENAI_TUNNEL_OR_KEYS: YES
DO_NOT_ENABLE_START_WITH_WINDOWS: YES
DO_NOT_CREATE_WINDOWS_SERVICE: YES
DO_NOT_CREATE_SCHEDULED_TASK: YES
DO_NOT_USE_SYSTEM_PROFILE: YES
DO_NOT_USE_UNRESTRICTED_PROFILE: YES
DO_NOT_RUN_AS_ADMINISTRATOR: YES
DO_NOT_MODIFY_MACHINE_WIDE_PATH: YES
USER_SCOPE_PATH_FOR_OFFICIAL_AGY: APPROVED
OFFICIAL_GOOGLE_AGY_USER_SCOPE_INSTALL: APPROVED
DO_NOT_MODIFY_REGISTRY_SERVICE_FIREWALL: YES
DO_NOT_DISABLE_DEFENDER: YES
DO_NOT_FORCE_PUSH: YES
DO_NOT_MERGE_DRAFT_PR: YES
DO_NOT_USE_PERMISSION_BYPASS_FLAGS: YES
DO_NOT_EXPOSE_SECRETS: YES
DO_NOT_START_CG_0004: YES
```

## Installation Safety Rules

- Prefer an already-installed official Antigravity `agy` binary if it exists but is missing from PATH.
- If download/install is necessary, use only a current official Google/Antigravity source documented by Google.
- Before executing a downloaded installer/package, record source provenance, SHA-256, Authenticode status/signer when applicable, and Windows Defender custom-scan result.
- Installation must be non-elevated/user-scope. If Admin elevation or machine-wide PATH is required, stop and request approval instead.
- User-level PATH for the verified official `agy` directory is explicitly approved.
- If authentication/login is required, ask for human presence and never capture credentials/tokens.

## Required End State

After corrections and fresh verification:

```text
STATUS: NEEDS_CHATGPT_REVIEW | NEEDS_HUMAN_PRESENCE | BLOCKED
REPLY-TO: CG-0003R2
MSG-ID: AG-0003R2
TASK-ID: NAG-V01-R2
PR: #1
LATEST_SOURCE_COMMIT: <sha>
TESTS: <exact result>
TYPECHECK: PASS|FAIL|NOT_RUN
BUILD: PASS|FAIL|NOT_RUN
ELECTRON_ESM_PATHS: PASS|FAIL|NOT_RUN
ELECTRON_RENDERER_ASSETS: PASS|FAIL|NOT_RUN
ELECTRON_REAL_TRAY_SMOKE: PASS|FAIL|NOT_RUN
AGY_OFFICIAL_SOURCE_VERIFIED: PASS|FAIL|NOT_NEEDED
AGY_INSTALL_OR_ENABLE: PASS|FAIL|NEEDS_HUMAN_PRESENCE|NOT_RUN
AGY_VERSION: <version|UNAVAILABLE>
AGY_NONINTERACTIVE_MODE: <mode|UNAVAILABLE>
ANTIGRAVITY_ADAPTER_STRATEGY_TEST: PASS|FAIL|NOT_RUN
MCP_SDK_COMPATIBILITY: PASS|FAIL|NOT_RUN
LOCAL_API_AUTH: PASS|FAIL|NOT_RUN
TSBUILDINFO_TRACKED: YES|NO
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
NEXT_ACTION: WAIT
```

Push fixes to `agent/cg-0003-v0.1`, update draft PR #1/report, and wait for ChatGPT review. Do not start CG-0004.
