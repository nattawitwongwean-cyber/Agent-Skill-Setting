# Current Directive

- **Directive:** CG-0003
- **Source:** ChatGPT (Issue #1 / Agent Bridge)
- **Target:** Antigravity
- **Scope:** Build Nareerat Agent Gateway V0.1
- **Date Received:** 2026-08-18
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/NAG-V01.md`
- **Design Spec:** `docs/superpowers/specs/2026-08-18-nareerat-agent-gateway-design.md`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-18-nareerat-agent-gateway-v0.1.md`

## Purpose

Create the private `nattawitwongwean-cyber/Nareerat-Agent-Gateway` source repository and implement the approved V0.1 core gateway using native local tools as the primary executor. Codex CLI and Antigravity are optional delegates only.

## Required Start Sequence

1. Safely synchronize `Agent-Skill-Setting`.
2. Read `agent-bridge/PROTOCOL.md`.
3. Read `agent-bridge/control/APPROVALS.md`.
4. Read the Gateway Design Spec fully.
5. Read the Gateway V0.1 Implementation Plan fully.
6. Read `agent-bridge/tasks/pending/NAG-V01.md`, including its Bootstrap Override.
7. Check `PROCESSED_MESSAGES.md`; accept `CG-0003` exactly once.
8. Implement plan task-by-task with TDD and per-task commits.

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
```

## Authorized Work

Execute the approved V0.1 implementation plan in the new source repo and disposable fixture workspaces only. Project-local dependency installation, source/test creation, normal Git commits, non-elevated build/test/typecheck, local Electron smoke testing, delegate capability detection/safe fixture smoke testing, and draft PR creation are approved as recorded in `APPROVALS.md`.

## Stop / Escalation Rules

- If any plan step requires Administrator/elevation, SYSTEM/UNRESTRICTED profile, credentials, registry/service/firewall mutation, production workspace access, Secure MCP Tunnel setup, startup persistence, or security weakening: stop that action and request approval.
- If a required test fails, diagnose using non-destructive evidence and one justified fix at a time. Do not claim the task complete without verification.
- Do not use delegate permission-bypass flags.
- Do not merge the final PR.

## Required End State

After all safely executable V0.1 plan tasks are complete or a blocking dependency is reached:

```text
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED
REPLY-TO: CG-0003
MSG-ID: AG-0003
TASK-ID: NAG-V01
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
NEXT_ACTION: WAIT
```

Open a draft PR if verification permits, report exact test/typecheck/build results and stop. Do not start V0.2.
