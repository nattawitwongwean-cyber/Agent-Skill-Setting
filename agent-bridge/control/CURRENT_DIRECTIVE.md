# Current Directive

- **Directive:** CG-HERMES-0001
- **Source:** ChatGPT continuation of the active @Hermes Full Owner Gateway workstream + explicit current human instruction to continue
- **Target:** Antigravity orchestrator on the Mac development host
- **Scope:** Finish Plan 01 Task 6, run the complete Plan 01 end gate, recheck real Hermes read-only state, and only if Plan 01 is fully green implement/review Plan 02 Task 1
- **Date Received:** 2026-08-20
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/HERMES-FOG-P01T6-P02T1.md`
- **Recovery Checkpoint:** `docs/handoffs/2026-08-20-hermes-full-owner-gateway-plan01-task6-checkpoint.md`
- **Machine Status:** `docs/handoffs/2026-08-20-hermes-full-owner-gateway-status.json`
- **Round 3 Recovery Patch:** `docs/handoffs/2026-08-20-hermes-plan01-task6-round3.patch`

## Purpose

Resume the exact local Mac @Hermes workstream without reconstructing it from stale remote source. Preserve all reviewed Task 6 work, obtain a fresh independent cumulative review, integrate the approved fixes into `feature/hermes-full-owner-gateway`, run the full Plan 01 end gate with fresh evidence, verify protected Hermes/LMS/Docker services read-only, and conditionally begin only Plan 02 Task 1 after Plan 01 is fully green.

The prior `CG-0003R2` is already recorded as processed/completed and is superseded as the current active directive by this new Hermes workstream directive. This directive does not reopen NAG-V01-R2 and does not authorize source main merges or production mutations.

## Required Start Sequence

1. Safely synchronize `Agent-Skill-Setting`.
2. Read `agent-bridge/PROTOCOL.md`.
3. Read this directive and `agent-bridge/tasks/pending/HERMES-FOG-P01T6-P02T1.md` fully.
4. Read all three recovery files referenced above.
5. Check `agent-bridge/state/PROCESSED_MESSAGES.md`; accept `CG-HERMES-0001` exactly once.
6. Open the existing local project/worktrees at the paths in the task. Do not clone/replace the source from the stale GitHub gateway remote.
7. Inspect Git status/history/worktrees before every mutation.
8. Execute Phase A through Phase F exactly as specified in the primary task.
9. Start Phase G (Plan 02 Task 1) only if every Plan 01 requirement is green.
10. Produce fresh verification evidence and hand off as `AG-HERMES-0001`.

## Mandatory Gate

```text
PLAN01_TASK6_FINAL_REVIEW=APPROVED_REQUIRED
PLAN01_END_GATE_ALL_GREEN=REQUIRED_BEFORE_PLAN02
MCP_SCHEMA_COUNT=57
PROTECTED_HERMES_SERVICES_READ_ONLY_RECHECK=REQUIRED
PRODUCTION_HERMES_MUTATION=FORBIDDEN
PRODUCTION_LMS_MUTATION=FORBIDDEN
PRODUCTION_DOCKER_MUTATION=FORBIDDEN
PRODUCTION_HERMES_MCP_INSTALL=FORBIDDEN
SOURCE_REMOTE_PUSH=NOT_AUTHORIZED
SOURCE_MAIN_MERGE=FORBIDDEN
PLAN02_TASK2_PLUS=NOT_AUTHORIZED
SECRETS_EXPOSED=NO
```

## Active Safety Bounds

```text
DO_NOT_RESET_HARD_REAL_WORKSPACE: YES
DO_NOT_GIT_CLEAN_FDX_REAL_WORKSPACE: YES
DO_NOT_FORCE_PUSH: YES
DO_NOT_PUSH_SOURCE_FEATURE_REMOTE: YES
DO_NOT_MERGE_SOURCE_MAIN: YES
DO_NOT_INSTALL_RESTART_STOP_PRODUCTION_SERVICES: YES
DO_NOT_CHANGE_HERMES_AGENT_PRODUCTION_CONFIG: YES
DO_NOT_CHANGE_LMS_PRODUCTION: YES
DO_NOT_CHANGE_DOCKER_PRODUCTION: YES
DO_NOT_READ_PRINT_COMMIT_SECRETS: YES
READ_ONLY_SSH_HERMES_CHECKS: APPROVED
LOCAL_FEATURE_COMMITS: APPROVED
LOCAL_TEST_EXECUTION: APPROVED
FRESH_CODEX_REVIEWER: APPROVED
AGENT_SKILL_SETTING_REPORT_COMMITS: APPROVED
PLAN02_TASK1_LOCAL_IMPLEMENTATION_AFTER_GREEN_GATE: APPROVED
```

If the local Git history materially differs from the recovery checkpoint, if a reviewed commit cannot be recovered exactly, if an end-gate check fails without a safe local fix, or if any step would require privileged/production mutation, stop and report `BLOCKED` rather than guessing.

## Required End State

```text
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED | NEEDS_HUMAN_PRESENCE
REPLY-TO: CG-HERMES-0001
MSG-ID: AG-HERMES-0001
TASK-ID: HERMES-FOG-P01T6-P02T1
PLAN01_FINAL_ROUND3_COMMIT: <sha|UNAVAILABLE>
PLAN01_FINAL_REVIEW: APPROVED|CHANGES_REQUESTED|NOT_RUN
PLAN01_FEATURE_HEAD: <sha>
PLAN01_END_GATE: PASS|FAIL|NOT_RUN
MCP_SCHEMA_COUNT: <number|UNKNOWN>
HERMES_GATEWAY_SERVICE: <state>
LMS_PRODUCTION_SERVICE: <state>
DOCKER_SERVICE: <state>
PRODUCTION_HERMES_MCP_INSTALLED: YES|NO|UNKNOWN
PRODUCTION_HERMES_CHANGED: NO|YES
PLAN01_STATUS: COMPLETE|BLOCKED
PLAN02_TASK1_STARTED: YES|NO
PLAN02_TASK1_COMMIT: <sha|NOT_CREATED>
PLAN02_TASK1_REVIEW: APPROVED|CHANGES_REQUESTED|NOT_RUN
PLAN02_TASK1_VERIFICATION: PASS|FAIL|NOT_RUN
SECRETS_EXPOSED: NO|YES
NEXT_ACTION: WAIT
```

Push only the sanitized coordination report/state/processed-ledger updates to `Agent-Skill-Setting`, then WAIT for ChatGPT review. Do not continue to Plan 02 Task 2.