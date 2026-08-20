# Current Directive

- **Directive:** `CG-HERMES-APP-0001`
- **Source:** Explicit human instruction after verifying that no `Hermes` Personal ChatGPT app is visible
- **Target:** Codex on the Mac development host
- **Scope:** Complete the @Hermes delivery end-to-end: reachable secure Hermes MCP runtime + Personal ChatGPT app registration + live `@Hermes` acceptance
- **Date Received:** 2026-08-21
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/HERMES-CHATGPT-APP-0001.md`
- **Prior Hermes Source Head:** `bf489e8de3f14301107dab1dcee9eb8d75b893c8`

## Purpose

The prior `CG-HERMES-0001` successfully completed the Hermes backend/source scope, but the user's actual product-level goal is not complete because ChatGPT still does not show a Personal app named `Hermes`. This directive closes that gap.

Completion requires a real Personal ChatGPT app named `Hermes` to appear under **Personal → Created by me**, be selectable as `@Hermes`, and successfully perform a live safe MCP call against the Hermes Linux gateway.

Backend-only evidence is not sufficient.

## Executor

Codex is the primary executor. The earlier `CG-CODEX-0001` role policy remains the standing execution model. If its administrative acknowledgement is still unprocessed, load/record those bounds without delaying this concrete Hermes task.

## Required Start Sequence

1. Read `agent-bridge/PROTOCOL.md`, `control/APPROVALS.md`, this directive, `STATUS.md`, and `PROCESSED_MESSAGES.md`.
2. Read `agent-bridge/tasks/pending/HERMES-CHATGPT-APP-0001.md` in full and the prior Hermes final report.
3. Accept `CG-HERMES-APP-0001` exactly once.
4. Verify the correct Mac host and existing local Hermes feature worktree/source head read-only before mutation.
5. Use current official OpenAI Apps SDK / ChatGPT Personal app documentation before registration work.
6. Execute the task through the UI + live `@Hermes` acceptance gate.

## Human Authorization for This Directive

The operator explicitly instructed ChatGPT to continue after confirming that `Hermes` was missing from the Plugins/Personal UI. Within this directive, the minimum necessary Level-2 work to produce the requested Personal app is authorized:

```text
NEW_HERMES_MCP_USER_SCOPE_SERVICE=APPROVED_IF_REQUIRED
SECURE_MCP_TRANSPORT_FOR_HERMES_APP=APPROVED_IF_REQUIRED
CHATGPT_PERSONAL_APP_REGISTRATION_HERMES=APPROVED
USE_EXISTING_AUTHENTICATED_CHATGPT_SESSION_WITHOUT_SECRET_EXTRACTION=APPROVED
```

This does NOT authorize extracting credentials, weakening security controls, root/system-wide changes, or modifying/restarting the existing protected Hermes gateway, LMS production nginx, or Docker services.

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

Do not mark complete before every required UI/live gate above is evidenced.

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
SOURCE_MAIN_MERGE=NOT_AUTHORIZED
HERMES_EXISTING_GATEWAY_RESTART_STOP_RECONFIGURE=FORBIDDEN
LMS_PRODUCTION_RESTART_STOP_RECONFIGURE=FORBIDDEN
DOCKER_PRODUCTION_RESTART_STOP_RECONFIGURE=FORBIDDEN
```

If an exact root/system-wide/security-weakening action becomes genuinely necessary, stop only at that boundary and report the exact required approval instead of bypassing it.

## Required End State

On success, post `CDX-HERMES-APP-0001`, archive the task, update state/ledger, set `NEEDS_CHATGPT_REVIEW`, and `NEXT_ACTION: WAIT`.
