# Current Directive

- **Directive:** `CG-HERMES-APP-0001`
- **Source:** Explicit human instruction to complete @Hermes as a real ChatGPT Personal app, plus latest Control Room route correction
- **Active Executor Route:** Hermes Agents / Ada on the Hermes machine
- **Mac Route:** PAUSED / PRESERVED — do not use the owner's Mac for Personal app creation for this task
- **Scope:** Complete the @Hermes delivery end-to-end: verified secure Hermes MCP runtime/tunnel + Personal ChatGPT app registration + live `@Hermes` acceptance
- **Date Received:** 2026-08-21
- **Directive State:** WORKING
- **Primary Task:** `agent-bridge/tasks/pending/HERMES-CHATGPT-APP-0001.md`
- **Prior Hermes Source Head:** `bf489e8de3f14301107dab1dcee9eb8d75b893c8`

## Purpose

The prior `CG-HERMES-0001` backend/source scope is not sufficient for the user's product-level goal. Completion requires a real Personal ChatGPT app named `Hermes` to be visible, selectable as `@Hermes`, and to perform a live safe MCP call against the Hermes Linux gateway.

Backend-only evidence is not completion.

## Active Route Override

The latest Control Room correction supersedes earlier Mac-side UI execution instructions for this task:

1. Stop and preserve the Mac-side UI/CLI route.
2. Do not ask the owner to keep the Mac powered on.
3. Ada/Hermes must perform ChatGPT Personal app configuration from the Ada/Hermes machine.
4. Preserve and reuse the already-working Hermes user-scope MCP release and secure tunnel; do not tear down or duplicate working backend components.
5. `CG-HERMES-APP-0001` has already been accepted exactly once and remains `WORKING`; do not duplicate acceptance.

Continuation order: Control Room Issue #1 comment `5363993406` (`CG-HERMES-APP-0001-ADA1`).

## Required Execution

1. Verify the existing Hermes user-scope MCP release and secure ChatGPT-reachable tunnel without exposing secrets.
2. Recheck `hermes-gateway.service`, LMS production nginx, and Docker read-only before and after; do not restart/stop/reconfigure them.
3. From the normal authenticated ChatGPT UI on Ada/Hermes, use the current custom-app/Developer Mode flow to create or refresh a Personal app named exactly `Hermes` using the verified secure MCP endpoint.
4. Run `Scan Tools` and require exactly 57 tools.
5. Verify `Hermes` is visible in Apps/Plugins and `@Hermes` is selectable.
6. Run a safe live MCP call and require fresh evidence: `initialize=PASS`, `tools/list=57`, `gateway_info=Hermes/linux`.
7. Post final compatibility handoff as `CDX-HERMES-APP-0001` with all required acceptance fields.

## Mandatory Acceptance Gate

```text
CHATGPT_PERSONAL_APP_NAME=Hermes
CHATGPT_PERSONAL_APP_VISIBLE=YES
CHATGPT_AT_HERMES_SELECTABLE=YES
CHATGPT_AT_HERMES_LIVE_MCP_CALL=PASS
HERMES_MCP_INITIALIZE=PASS
HERMES_MCP_TOOLS_LIST=57
HERMES_GATEWAY_IDENTITY=Hermes/linux
PROTECTED_EXISTING_SERVICES_CHANGED=NO
SECRETS_EXPOSED=NO
```

Do not mark complete before every UI/live gate above is evidenced.

## Safety Bounds

```text
UNRESTRICTED_MODE=FORBIDDEN
SANDBOX_BYPASS=FORBIDDEN
SECRETS_READ_PRINT_COMMIT=FORBIDDEN
PUBLIC_UNAUTHENTICATED_REMOTE_CONTROL=FORBIDDEN
BULK_DESTRUCTIVE_DELETE=FORBIDDEN
GIT_RESET_HARD_REAL_WORKSPACE=FORBIDDEN
GIT_CLEAN_FDX_REAL_WORKSPACE=FORBIDDEN
GIT_FORCE_PUSH=FORBIDDEN
SOURCE_MAIN_MERGE=NOT_AUTHORIZED
HERMES_EXISTING_GATEWAY_RESTART_STOP_RECONFIGURE=FORBIDDEN
LMS_PRODUCTION_RESTART_STOP_RECONFIGURE=FORBIDDEN
DOCKER_PRODUCTION_RESTART_STOP_RECONFIGURE=FORBIDDEN
ROOT_OR_SYSTEM_WIDE_SECURITY_WEAKENING=FORBIDDEN_WITHOUT_EXACT_NEW_APPROVAL
```

If the Ada/Hermes ChatGPT UI presents an unavoidable fresh account login/consent confirmation that cannot be completed via the normal authenticated session, preserve working runtime/tunnel state and report that single exact blocker as `NEEDS_HUMAN_PRESENCE`.

## Required End State

On success, post `CDX-HERMES-APP-0001`, archive the task, update state/ledger, set `NEEDS_CHATGPT_REVIEW`, and `NEXT_ACTION: WAIT`.
