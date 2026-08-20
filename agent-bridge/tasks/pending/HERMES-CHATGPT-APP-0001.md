# Task: HERMES-CHATGPT-APP-0001 — Make @Hermes a Real ChatGPT Personal App

- **Directive:** `CG-HERMES-APP-0001`
- **Issued By:** ChatGPT from explicit human instruction to continue until Hermes is actually available in ChatGPT
- **Target:** Codex on the Mac development host
- **Status:** PENDING
- **Priority:** CRITICAL
- **Program:** `@Hermes Full Owner Gateway`
- **Date Received:** 2026-08-21
- **Source Feature Branch:** `feature/hermes-full-owner-gateway`
- **Known Source Feature Head:** `bf489e8de3f14301107dab1dcee9eb8d75b893c8`
- **Prior Completed Task:** `agent-bridge/tasks/completed/HERMES-FOG-P01T6-P02T1.md`

## Human Intent / Definition of Done

The previous Hermes directive is not considered sufficient for the user's current goal because ChatGPT still does not show a Personal plugin/app named `Hermes`.

This task is complete only when all of the following are freshly verified:

```text
CHATGPT_PERSONAL_APP_NAME=Hermes
CHATGPT_PLUGINS_PERSONAL_CREATED_BY_ME_VISIBLE=YES
CHATGPT_AT_HERMES_SELECTABLE=YES
CHATGPT_AT_HERMES_LIVE_MCP_CALL=PASS
HERMES_MCP_INITIALIZE=PASS
HERMES_MCP_TOOLS_LIST=57
HERMES_GATEWAY_IDENTITY=Hermes/linux
```

A backend-only implementation, local acceptance test, source commit, or control-plane record is NOT completion.

## Authority / New Scope

The operator explicitly said to continue after being shown that the `Hermes` ChatGPT plugin/app is missing. This is a new concrete directive that authorizes the minimum necessary work to turn the already-built Hermes backend into a real Personal ChatGPT app.

This task authorizes:

- continuing the local Hermes feature implementation only as required to expose a standards-compliant remote MCP endpoint to ChatGPT;
- deploying/enabling a new **user-scope Hermes MCP runtime/service** on the Hermes host if required;
- creating/configuring the minimum-scope **secure MCP transport/tunnel** required for ChatGPT to reach that Hermes MCP endpoint;
- registering/creating a **Personal ChatGPT app named `Hermes`** using the existing authenticated ChatGPT session on the Mac;
- refreshing/reconnecting the app after descriptor changes;
- performing safe live verification through ChatGPT;
- preserving the existing protected `hermes-gateway.service`, LMS production nginx, and Docker services without restart/stop/reconfiguration unless a later exact approval explicitly says otherwise.

No credential/token may be printed, copied into GitHub/chat, or committed. Existing authenticated sessions/credential stores may be used only through their normal application/tool interface without extracting secret material.

## Required Docs-First Rule

Before implementation/registration, use current official OpenAI Apps SDK documentation as authority, including current guidance for:

- Apps SDK MCP server requirements;
- ChatGPT Developer Mode / Personal app creation;
- remote HTTPS MCP connectivity;
- app refresh/reconnect after MCP metadata changes.

Prefer current OpenAI product wording (`app`) even if the UI still labels the page `Plugins`.

## Phase A — Bootstrap and Executor Role

1. Sync/read `agent-bridge/PROTOCOL.md`, `CURRENT_DIRECTIVE.md`, `STATUS.md`, `PROCESSED_MESSAGES.md`, this task, and the prior Hermes final report.
2. Codex is the primary executor. If `CG-CODEX-0001` is still unprocessed, record/load its standing executor bounds before this task; do not let that administrative role acknowledgement block this concrete task.
3. Accept `CG-HERMES-APP-0001` exactly once.
4. Verify the Mac host and the existing local Hermes source/worktree read-only before mutation.
5. Preserve unrelated dirty user work; never reset/clean destructively.

## Phase B — Inspect the Existing Working `Mac` Personal App Pattern

Use the existing ChatGPT Personal app `Mac` as a read-only reference for the shortest known-good local setup.

Inspect only non-secret configuration needed to determine:

- how the existing `Mac` app is registered;
- what remote MCP URL/transport shape ChatGPT accepts in this account;
- whether a secure tunnel/private-MCP mechanism already exists and can be reused safely;
- whether the Mac app was created through ChatGPT Developer Mode / Personal app UI.

Do not export cookies/tokens/browser credentials. Do not expose any secret URL query tokens in reports.

## Phase C — Prepare a Reachable Hermes MCP Endpoint

Source of truth remains the local Mac repository/worktree from the prior Hermes task, not a stale source remote.

1. Inspect the current feature branch/worktree and Plan 02+ docs only as needed for this deliverable.
2. Implement the smallest additional source/runtime changes required for a production-safe remote MCP endpoint.
3. Maintain the verified 57-tool schema and existing fail-closed policy behavior.
4. Run fresh build/tests and a direct MCP acceptance check before deployment.
5. If runtime deployment is needed, install only a new user-scope Hermes MCP runtime/service owned by the Hermes user. Do not modify the existing Hermes Agent gateway, LMS production, or Docker service configuration.
6. Verify protected services before and after.

## Phase D — Secure ChatGPT Connectivity

ChatGPT must reach the Hermes MCP endpoint over a supported secure transport.

Preferred order:

1. Reuse a verified existing secure transport pattern already used by the working `Mac` Personal app when appropriate.
2. Otherwise configure the minimum-scope OpenAI-supported secure/private MCP transport required for this one Hermes endpoint.
3. Do not expose an unauthenticated remote-control endpoint publicly.
4. Never print or commit tunnel credentials, bearer tokens, cookies, or private keys.
5. If a browser/login confirmation is required, use the existing authenticated UI and continue automatically when possible; use `NEEDS_HUMAN_PRESENCE` only for an exact manual credential/consent interaction that computer control cannot lawfully complete.

## Phase E — Create the Personal ChatGPT App

Using the ChatGPT UI on the Mac:

1. Ensure Developer Mode / the current equivalent for Personal app creation is enabled as required by current docs.
2. Open the Plugins/Apps management screen.
3. Create a new Personal app named exactly `Hermes` pointing to the verified secure Hermes MCP endpoint.
4. Save/connect it.
5. Refresh the app after final MCP descriptor/metadata changes.
6. Verify `Hermes` appears under **Personal → Created by me** in the same UI where `Dev` and `Mac` currently appear.

Do not claim success from API/backend evidence alone; UI presence is a mandatory gate.

## Phase F — End-to-End @Hermes Acceptance

From ChatGPT itself:

1. Start/select a chat and invoke/select `@Hermes`.
2. Perform a safe read-only live MCP call.
3. Verify fresh evidence:

```text
initialize=PASS
tools/list=57
gateway_info=Hermes/linux
safe read-only tool call=PASS
privilege escalation remains denied
high-risk destructive/admin/LMS writes remain fail-closed unless separately authorized
```

4. Capture only sanitized evidence. Never screenshot or log secrets.
5. Recheck on the Hermes host that protected services remain active.

## Safety Bounds

```text
PRIMARY_EXECUTOR=CODEX
UNRESTRICTED_MODE=FORBIDDEN
SANDBOX_BYPASS=FORBIDDEN
SECRETS_READ_PRINT_COMMIT=FORBIDDEN
PUBLIC_UNAUTHENTICATED_REMOTE_CONTROL=FORBIDDEN
BULK_DESTRUCTIVE_DELETE=FORBIDDEN
GIT_RESET_HARD_REAL_WORKSPACE=FORBIDDEN
GIT_CLEAN_FDX_REAL_WORKSPACE=FORBIDDEN
GIT_FORCE_PUSH=FORBIDDEN
DISK_PARTITION_DESTRUCTIVE_ACTION=FORBIDDEN
HERMES_EXISTING_GATEWAY_RESTART_STOP_RECONFIGURE=FORBIDDEN
LMS_PRODUCTION_RESTART_STOP_RECONFIGURE=FORBIDDEN
DOCKER_PRODUCTION_RESTART_STOP_RECONFIGURE=FORBIDDEN
NEW_HERMES_MCP_USER_SCOPE_SERVICE=AUTHORIZED_IF_REQUIRED
SECURE_MCP_TRANSPORT_FOR_HERMES_APP=AUTHORIZED_IF_REQUIRED
CHATGPT_PERSONAL_APP_REGISTRATION_HERMES=AUTHORIZED
SOURCE_LOCAL_FEATURE_COMMITS=AUTHORIZED
SOURCE_REMOTE_PUSH=NOT_REQUIRED; DO_NOT_PUSH UNLESS TECHNICALLY NECESSARY AND EXPLICITLY JUSTIFIED IN HANDOFF
SOURCE_MAIN_MERGE=NOT_AUTHORIZED
```

If root/system-wide privilege, firewall/security weakening, destructive cleanup, or modification of existing protected production services is truly required, stop only at that exact boundary and report `NEEDS_APPROVAL`/`NEEDS_HUMAN_PRESENCE` with the precise action. Do not weaken controls to avoid the gate.

## Required Handoff

When the UI + live `@Hermes` acceptance is complete, write a sanitized report under `agent-bridge/reports/2026-08-21/`, move this task to `tasks/completed/`, update the processed-message ledger and status, and post to Control Room Issue #1:

```text
[FROM: CODEX]
[TO: CHATGPT]
MSG-ID: CDX-HERMES-APP-0001
REPLY-TO: CG-HERMES-APP-0001
TASK-ID: HERMES-CHATGPT-APP-0001
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED | NEEDS_HUMAN_PRESENCE | NEEDS_APPROVAL
PRIMARY_EXECUTOR: CODEX
CHATGPT_PERSONAL_APP_NAME: Hermes
CHATGPT_PERSONAL_APP_VISIBLE: YES|NO
CHATGPT_AT_HERMES_SELECTABLE: YES|NO
CHATGPT_AT_HERMES_LIVE_MCP_CALL: PASS|FAIL|NOT_RUN
HERMES_MCP_ENDPOINT_REACHABLE: YES|NO
HERMES_MCP_INITIALIZE: PASS|FAIL|NOT_RUN
HERMES_MCP_TOOLS_LIST: <number|UNKNOWN>
HERMES_GATEWAY_IDENTITY: <value|UNKNOWN>
HERMES_GATEWAY_SERVICE: <state>
LMS_PRODUCTION_SERVICE: <state>
DOCKER_SERVICE: <state>
PROTECTED_EXISTING_SERVICES_CHANGED: NO|YES
SECRETS_EXPOSED: NO|YES
NEXT_ACTION: WAIT
```

Do not mark this task complete unless `CHATGPT_PERSONAL_APP_VISIBLE=YES`, `CHATGPT_AT_HERMES_SELECTABLE=YES`, and the live MCP call passes.