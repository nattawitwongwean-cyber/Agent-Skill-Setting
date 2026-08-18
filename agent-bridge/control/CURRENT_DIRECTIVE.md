# Current Directive

- **Directive:** CG-0003R
- **Source:** ChatGPT review (Issue #1 / PR #1)
- **Target:** Antigravity
- **Scope:** Correct Nareerat Agent Gateway V0.1 review blockers
- **Date Received:** 2026-08-18
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/NAG-V01-R1.md`
- **Design Spec:** `docs/superpowers/specs/2026-08-18-nareerat-agent-gateway-design.md`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-18-nareerat-agent-gateway-v0.1.md`
- **Review Record:** `docs/superpowers/reviews/2026-08-18-nareerat-agent-gateway-v0.1-review.md`

## Purpose

Correct the source-level V0.1 mismatches found during ChatGPT review of draft PR #1 before any Gateway V0.1 commit is accepted as the baseline for the Automatic Agent Bridge Watcher.

This is a corrective continuation of CG-0003. Do not start CG-0004 yet.

## Required Start Sequence

1. Safely synchronize `Agent-Skill-Setting`.
2. Read `agent-bridge/PROTOCOL.md`.
3. Read `agent-bridge/control/APPROVALS.md`.
4. Read the Gateway Design Spec and V0.1 Implementation Plan.
5. Read the ChatGPT V0.1 review record fully.
6. Read `agent-bridge/tasks/pending/NAG-V01-R1.md` fully.
7. Check `PROCESSED_MESSAGES.md`; accept `CG-0003R` exactly once.
8. Open existing Gateway repo/branch `agent/cg-0003-v0.1`; do not create a replacement repo or merge PR #1.
9. Correct only the identified V0.1 blockers and verify them with fresh evidence.

## Blocking Corrections

```text
MCP_SDK_REAL_IMPLEMENTATION: REQUIRED
REAL_ELECTRON_TRAY_RUNTIME: REQUIRED
ANTIGRAVITY_DELEGATE_FAIL_CLOSED_RUNNER: REQUIRED
LOCAL_LOOPBACK_AUTH_BOUNDARY: REQUIRED
REMOVE_TRACKED_TSBUILDINFO: REQUIRED
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
DO_NOT_USE_SYSTEM_PROFILE: YES
DO_NOT_USE_UNRESTRICTED_PROFILE: YES
DO_NOT_RUN_AS_ADMINISTRATOR: YES
DO_NOT_MODIFY_REGISTRY_SERVICE_FIREWALL: YES
DO_NOT_DISABLE_DEFENDER: YES
DO_NOT_FORCE_PUSH: YES
DO_NOT_MERGE_DRAFT_PR: YES
DO_NOT_EXPOSE_SECRETS: YES
DO_NOT_START_CG_0004: YES
```

## Authorized Work

Use the existing CG-0003 Level-1 authorizations as clarified in `APPROVALS.md`. Project-local dependencies necessary to satisfy the already approved V0.1 plan are authorized. Work only on the existing Gateway branch and disposable fixture workspaces.

## Stop / Escalation Rules

- If any correction requires Administrator/elevation, credentials, SYSTEM/UNRESTRICTED, machine-wide Antigravity configuration, registry/service/firewall mutation, production workspace access, Secure MCP Tunnel, startup persistence, or security weakening: stop that action and request approval.
- Do not use Antigravity permission-bypass flags.
- Do not claim success from the previous AG-0003 report; rerun fresh verification after source corrections.
- If safe non-interactive Antigravity CLI support is not available, implement/report `UNAVAILABLE` rather than fake delegation success.
- Do not merge PR #1.

## Required End State

After corrections and fresh verification:

```text
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED
REPLY-TO: CG-0003R
MSG-ID: AG-0003R
TASK-ID: NAG-V01-R1
PR: #1
MCP_SDK_COMPATIBILITY: PASS|FAIL|NOT_RUN
ELECTRON_TRAY_SMOKE: PASS|FAIL|NOT_RUN
ANTIGRAVITY_CAPABILITY: AVAILABLE|UNAVAILABLE|NOT_RUN
LOCAL_API_AUTH: PASS|FAIL|NOT_RUN
TSBUILDINFO_TRACKED: YES|NO
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
NEXT_ACTION: WAIT
```

Push fixes to `agent/cg-0003-v0.1`, update the draft PR/report, hand off, and wait for ChatGPT review. Do not start CG-0004.
