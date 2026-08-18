# Task: NAG-V01 — Build Nareerat Agent Gateway V0.1

- **Directive:** `CG-0003`
- **Issued By:** ChatGPT
- **Target:** Antigravity
- **Status:** PENDING
- **Priority:** HIGH
- **Execution Style:** Task-by-task TDD with frequent commits

## Authoritative Documents

Read fully before implementation:

1. `docs/superpowers/specs/2026-08-18-nareerat-agent-gateway-design.md`
2. `docs/superpowers/plans/2026-08-18-nareerat-agent-gateway-v0.1.md`
3. `agent-bridge/PROTOCOL.md`
4. `agent-bridge/control/APPROVALS.md`

## Objective

Create private repository `nattawitwongwean-cyber/Nareerat-Agent-Gateway` and implement the approved V0.1 core gateway on the Windows machine. Native local tools are the primary executor. Codex CLI and Antigravity are optional delegates only.

## Bootstrap Override / Correction

The new source repository must have a real `main` baseline before the implementation branch is created so a draft PR can be opened later.

If the source repository does not exist:

```powershell
gh repo create nattawitwongwean-cyber/Nareerat-Agent-Gateway --private --description "Windows-first local MCP and native agent gateway" --clone
Set-Location .\Nareerat-Agent-Gateway
"# Nareerat Agent Gateway" | Set-Content -Encoding utf8 README.md
@("node_modules/","dist/","coverage/","*.log","data/",".env",".env.*") | Set-Content -Encoding utf8 .gitignore
git add README.md .gitignore
git commit -m "chore: initialize private gateway repository"
git push -u origin HEAD:main
git checkout -b agent/cg-0003-v0.1
```

If the repo already exists, inspect it first and do not overwrite existing work. Synchronize safely and create/use `agent/cg-0003-v0.1` only when that will not destroy existing changes.

After this baseline correction, follow Tasks 1–14 in the implementation plan, treating any conflicting branch-creation sentence in Task 1 as superseded by this task file.

## Explicitly Authorized for CG-0003

- Create the private source repository above if absent.
- Create/push baseline `main` and implementation branch `agent/cg-0003-v0.1`.
- Create/modify files only inside the new source repo, generated temporary fixture workspaces, and approved Agent Bridge reporting paths.
- Install project-local npm/pnpm dependencies explicitly required by the implementation plan using `corepack pnpm@10.15.0`.
- Run non-elevated Node/TypeScript/Vitest/Git/ripgrep commands needed by the plan.
- Run non-elevated build/test/typecheck processes in the new repo or generated fixture workspace.
- Launch the V0.1 Electron desktop app interactively for one local smoke test, then quit normally.
- Inspect `codex --version`, `codex exec --help`, `agy --version`, and `agy --help` without changing authentication/configuration.
- Run optional delegate smoke tests only in generated fixture workspaces and only under the plan's fail-closed rules.
- Create a draft pull request from `agent/cg-0003-v0.1` to `main` after verification.
- Commit/push sanitized reports to Agent Bridge and comment in Control Room Issue #1.

## Not Authorized / Hard Bounds

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

Do not use Antigravity permission-bypass flags such as `--dangerously-skip-permissions` for delegation automation.

## Safety Workspace Rule

All write/shell/build/test integration work must use the new Gateway repository or a generated disposable fixture workspace. Do not point V0.1 at `Nattawit-LMS`, student submissions, school systems, real `.env` files, or other production/user-data repositories.

## Progress / Checkpoints

Commit after every implementation-plan task. If a task cannot pass its required verification, do not claim it complete. Record the exact failure and continue only if the next task does not depend on the failed capability; otherwise stop as `BLOCKED`.

If any requested action becomes Level-2/system/elevated or requires credentials, stop that action and request approval instead of bypassing the gate.

## Required End State

Open a **draft** PR only after the implementation plan's full V0.1 verification step has been executed. Do not merge it.

Report as:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-0003
REPLY-TO: CG-0003
TASK-ID: NAG-V01
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED
SOURCE_REPO: nattawitwongwean-cyber/Nareerat-Agent-Gateway
BRANCH: agent/cg-0003-v0.1
PR: <draft PR reference or NONE>
TESTS: <exact result>
TYPECHECK: <PASS|FAIL|NOT_RUN>
BUILD: <PASS|FAIL|NOT_RUN>
NATIVE_VERTICAL_SLICE: <PASS|FAIL|NOT_RUN>
PRO_SAFE_MCP_CATALOG: <PASS|FAIL|NOT_RUN>
CODEX_DELEGATE: <AVAILABLE|UNAVAILABLE|PASS|FAIL|NOT_RUN>
ANTIGRAVITY_DELEGATE: <AVAILABLE|UNAVAILABLE|PASS|FAIL|NOT_RUN>
SECURITY_ANOMALY: <YES|NO>
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
LATEST_REPORT: <repo path>
LATEST_SOURCE_COMMIT: <sha or NONE>
NEXT_ACTION: WAIT
```

Then set Agent Bridge state to `NEEDS_CHATGPT_REVIEW` or `BLOCKED` and wait. Do not begin V0.2.