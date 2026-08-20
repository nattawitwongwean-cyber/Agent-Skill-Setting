# Task: HERMES-FOG-P01T6-P02T1 — Finish Plan 01 Task 6, Gate Plan 01, Then Start Plan 02 Task 1

- **Directive:** `CG-HERMES-0001`
- **Issued By:** ChatGPT with explicit human instruction to continue the active @Hermes workstream
- **Target:** Antigravity orchestrator on the Mac development host
- **Status:** COMPLETED_WAITING_REVIEW
- **Priority:** HIGH
- **Program:** `@Hermes Full Owner Gateway`
- **Source Repo:** local Mac repository only; do not reconstruct from the stale GitHub gateway remote
- **Feature Branch:** `feature/hermes-full-owner-gateway`
- **Plan 01:** `docs/superpowers/plans/2026-08-20-hermes-full-owner-gateway-01-linux-core.md`
- **Plan 02:** `docs/superpowers/plans/2026-08-20-hermes-full-owner-gateway-02-provider-runtime.md`
- **Recovery Checkpoint:** `docs/handoffs/2026-08-20-hermes-full-owner-gateway-plan01-task6-checkpoint.md`
- **Machine Status:** `docs/handoffs/2026-08-20-hermes-full-owner-gateway-status.json`
- **Round 3 Recovery Patch:** `docs/handoffs/2026-08-20-hermes-plan01-task6-round3.patch`
- **Completed At:** `2026-08-20T22:09:00+07:00`
- **Handoff:** `AG-HERMES-0001`
- **Final Source Feature Head:** `bf489e8de3f14301107dab1dcee9eb8d75b893c8`
- **Final Report:** `agent-bridge/reports/2026-08-20/HERMES-FOG-P01T6-P02T1.md`

## Objective

Resume the exact local @Hermes workstream from the latest verified checkpoint. Finish Plan 01 Task 6 without losing the already-reviewed fixes, run the complete Plan 01 end gate with fresh evidence, preserve protected Hermes/LMS/Docker production state, and only if Plan 01 is fully green begin Plan 02 Task 1 (portable worker runtime layout).

Do not report completion from historical evidence alone. Fresh evidence is required.

## Completion Record

The objective was completed within the directive's authorized scope.

```text
PLAN01_FINAL_ROUND3_COMMIT=151ca8b
PLAN01_FINAL_REVIEW=APPROVED
PLAN01_FEATURE_HEAD=93d9909
PLAN01_GIT_STATUS_CLEAN=YES
PLAN01_DIFF_CHECK=PASS
PLAN01_BUILD=PASS
PLAN01_NPM_TEST=PASS — Mac lifecycle 6/6
PLAN01_WORKER_TESTS=PASS — 70/70
PLAN01_HERMES_TESTS=PASS — 33/33
PLAN01_JSONRPC_ACCEPTANCE=PASS
MCP_SCHEMA_COUNT=57
HERMES_GATEWAY_SERVICE=active
LMS_PRODUCTION_SERVICE=active
DOCKER_SERVICE=active
PRODUCTION_HERMES_MCP_INSTALLED=NO
PRODUCTION_HERMES_CHANGED=NO
PLAN01_STATUS=COMPLETE
PLAN02_TASK1_STARTED=YES
PLAN02_TASK1_COMMIT=bf489e8
PLAN02_TASK1_REVIEW=APPROVED
PLAN02_TASK1_BUILD=PASS
PLAN02_TASK1_TEST=PASS — runtime-layout 4/4
PLAN02_TASK1_WORKER_TESTS=PASS — 74/74
PLAN02_TASK1_NPM_TEST=PASS — Mac lifecycle 6/6
PLAN02_TASK2_PLUS=NOT_AUTHORIZED / NOT_STARTED
SOURCE_REMOTE_PUSH=NO
SOURCE_MAIN_MERGE=NO
SECRETS_EXPOSED=NO
SECURITY_ANOMALY=NO
NEXT_ACTION=WAIT
```

Full evidence and rulings are preserved in the final report referenced above.

## Source-of-Truth Order

1. Existing local Mac repository and its Git history/worktrees.
2. Existing local SDD ledger and plan/spec files in that repository.
3. The recovery checkpoint/status/round-3 patch in `Agent-Skill-Setting`.
4. Historical handoffs.
5. The stale GitHub `Nareerat-Agent-Gateway` source remote is **not** authoritative for this Hermes feature.

Never replace the local repository with the stale remote and never reset away uncommitted work.

## Known Local Paths

```text
PROJECT=/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway
FEATURE_WORKTREE=/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway/.worktrees/hermes-full-owner-gateway
ROUND3_WORKTREE=/Users/nattawit/Library/Application Support/MacDevGateway/workers/w-20260820210909-9bcab979/workspace
FEATURE_BRANCH=feature/hermes-full-owner-gateway
```

Last verified feature head before review fixes:

```text
2a152c3 test: verify hermes linux core over mcp
```

Known review-fix commits at checkpoint time:

```text
7b174a7 test: harden hermes linux acceptance
492e1f7 test: ensure hermes acceptance kills stuck gateway
```

Round 3 was based on `492e1f7` and changed only:

```text
test/hermes/linux-jsonrpc-acceptance.mjs
```

## Mandatory Bootstrap

1. Safely synchronize `Agent-Skill-Setting` and read `agent-bridge/PROTOCOL.md`.
2. Read the three recovery files listed above in full.
3. Read local Plan 01, Plan 02, design spec, and `.superpowers/sdd/2026-08-20-hermes-full-owner-gateway-01-linux-core/progress.md` if present.
4. In the local project and feature worktree run read-only Git inspection first:

```bash
git status --short --branch
git log --oneline --decorate -20
git worktree list
```

5. Do not use `git reset --hard`, `git clean -fdx`, force push, or destructive cleanup.

## Phase A — Recover and Finish Task 6 Round 3

1. Inspect `ROUND3_WORKTREE` if it still exists:

```bash
git status --short --branch
git log --oneline --decorate -8
git diff --check
git diff 492e1f7 -- test/hermes/linux-jsonrpc-acceptance.mjs
```

2. Expected round-3 corrections:
   - reject JSON arrays as malformed JSON-RPC messages with `Array.isArray(message)`;
   - child-exit evidence includes `child.signalCode !== null`;
   - shutdown is `SIGTERM -> bounded wait -> SIGKILL -> bounded wait`;
   - if exit is still not observed after SIGKILL, throw rather than silently succeeding;
   - nested `try/finally` guarantees temporary HOME cleanup even if shutdown throws;
   - all prior request-timeout, pending-rejection, malformed-output, notify-error, exact git-status-payload and fail-closed behavior remains intact.

3. If the round-3 worktree contains the expected uncommitted patch, stage only `test/hermes/linux-jsonrpc-acceptance.mjs` and commit it with:

```text
test: fail closed on hermes acceptance shutdown
```

4. If the round-3 worktree is gone or its uncommitted patch is missing, recover only that exact change from `docs/handoffs/2026-08-20-hermes-plan01-task6-round3.patch` onto a branch whose parent is `492e1f7`. Verify the patch before committing. Do not hand-reconstruct unrelated code.

5. Record the resulting round-3 commit SHA.

## Phase B — Fresh Independent Cumulative Review

A fresh reviewer must inspect the cumulative Task 6 acceptance-harness changes from `2a152c3` through the final round-3 commit. Prefer a separate Codex reviewer/process from the Antigravity implementer. The reviewer must be read-only and must not mutate source.

Review scope:

```text
test/hermes/linux-jsonrpc-acceptance.mjs
package.json only if it is part of the original Task 6 range
```

Reviewer must explicitly verify:

```text
JSON_ARRAY_OUTPUT_REJECTED=YES
REQUESTS_BOUNDED=YES
MALFORMED_OUTPUT_REJECTS_PENDING=YES
CHILD_ERROR_EXIT_REJECTS_PENDING=YES
ACTUAL_EXIT_EVIDENCE_INCLUDES_SIGNAL_CODE=YES
SIGTERM_WAIT_SIGKILL_WAIT=YES
NO_SUCCESS_IF_CHILD_SURVIVES_SIGKILL_WAIT=YES
TEMP_HOME_CLEANUP_ON_SHUTDOWN_THROW=YES
NOTIFY_WRITE_FAILURE_FATAL_PATH=YES
GIT_STATUS_PAYLOAD_EXACT_ASSERTION=YES
OWNER_EXEC_FAIL_CLOSED_WHEN_SANDBOX_UNAVAILABLE=YES
NO_SCOPE_EXPANSION=YES
```

If any load-bearing finding remains, fix it in a fresh implementer pass and re-review. Do not integrate until reviewer verdict is `APPROVED`.

## Phase C — Integrate Task 6 Fixes

After approval, integrate into `feature/hermes-full-owner-gateway` in history-preserving order. At minimum the feature must contain the equivalent of:

```text
2a152c3
7b174a7
492e1f7
<round3-final-sha>
```

Prefer normal `git cherry-pick` of the missing commits. Do not duplicate commits already present. Resolve no conflict by deleting unrelated work. If history differs materially from the checkpoint, stop and report the exact graph rather than guessing.

After integration:

```bash
git status --short --branch
git log --oneline --decorate -12
git diff --check
```

Feature worktree must be clean before the end gate.

## Phase D — Plan 01 End Gate (Fresh)

From the feature worktree run every command:

```bash
git status --porcelain
git diff --check
npm run build
npm test
npm run test:workers
npm run test:hermes
node test/hermes/linux-jsonrpc-acceptance.mjs
```

Record exact exit codes and concise test totals. The known isolated-worker `EPERM` on the MacDevGateway audit log is not acceptable as a feature-worktree end-gate result; `npm test` must be run from the controller/feature worktree where the audit path is permitted.

Required Plan 01 evidence:

```text
HERMES_LINUX_CORE=PASS
HERMES_DIRECT_OWNER_READ=PASS
HERMES_DIRECT_OWNER_MUTATION_DISPOSABLE_ONLY=PASS
MCP_SCHEMA_COUNT=57
PRIVILEGE_ESCALATION_FROM_OWNER_SHELL=DENIED
OWNER_COMMAND_SANDBOX=PASS or OWNER_COMMAND_TOOLS_NOT_ENABLED
GIT_HOOKS_IMPLICIT_EXECUTION=DENIED
PROTECTED_PROCESS_TERMINATION=DENIED
MAC_REGRESSION=PASS
HERMES_AGENT_UNCHANGED=YES
LMS_PRODUCTION_UNCHANGED=YES
ROOTLESS_DOCKER_UNCHANGED=YES
PRODUCTION_HERMES_MCP_INSTALLED=NO
SECRETS_EXPOSED=NO
```

Do not infer any PASS that the current end-gate output cannot support.

## Phase E — Real Hermes Read-Only Recheck

Use the existing SSH route to the Hermes host only for read-only checks. Do not install, restart, stop, enable, disable, or modify production services/configuration.

Verify at least:

```text
hostname identifies the expected Hermes host
hermes-gateway.service remains active
LMS production nginx service remains active
Docker service remains active
no production hermes-mcp-* service/unit has been installed by this program
```

Use the actual unit names present on the host and report them exactly. If the previously observed names differ, inspect read-only and report the real names; do not rename or modify services.

Optional: repeat the temporary `/tmp` read-only JSON-RPC artifact smoke from the final integrated source if it can be done without production mutation. If repeated, verify `initialize=PASS`, `tools/list=57`, and `gateway_info=Hermes/linux`, then delete only the temporary artifact that this task created.

## Phase F — Close Plan 01

Only when Phases A-E are green:

1. Update the local SDD ledger with Task 6 final reviewer verdict, integrated SHAs, end-gate evidence, and real Hermes read-only evidence.
2. Mark Plan 01 complete locally.
3. Do not merge to main and do not push the local source feature branch unless separately authorized. Coordination-report commits to `Agent-Skill-Setting` are allowed by the bridge protocol.

If any Plan 01 requirement is not green, stop here and report `BLOCKED` or `NEEDS_CHATGPT_REVIEW`. Do not start Plan 02.

## Phase G — Conditional Start of Plan 02 Task 1

This phase is authorized **only if Plan 01 is fully green**.

Read Plan 02 in full, then implement Task 1 exactly: parameterize worker runtime/state/worktree roots without changing existing Mac defaults.

Expected new file:

```text
src/workers/runtime-layout.ts
```

Expected modifications:

```text
src/workers/persistence.ts
src/workers/worktree.ts
src/workers/manager.ts
```

Expected test:

```text
test/workers/runtime-layout.test.mjs
```

Required public interface:

```ts
export interface WorkerRuntimeLayout {
  stateRoot: string;
  workerRoot: string;
  worktreeRoot: string;
}
export function defaultMacWorkerRuntimeLayout(env?: NodeJS.ProcessEnv): WorkerRuntimeLayout;
export function hermesWorkerRuntimeLayout(home: string): WorkerRuntimeLayout;
```

Expected layouts:

```text
Mac stateRoot=/Users/demo/Library/Application Support/MacDevGateway/workers/state
Mac workerRoot=/Users/demo/Library/Application Support/MacDevGateway/workers
Hermes stateRoot=/home/hermes/.local/state/hermes-mcp/workers/state
Hermes workerRoot=/home/hermes/.local/state/hermes-mcp/workers/runtime
Hermes worktreeRoot=/home/hermes/.local/share/hermes-mcp/worktrees
```

`WorkerManager` must accept optional `layout?: WorkerRuntimeLayout` while existing callers remain unchanged. Worktree helpers must accept/use layout without breaking dependency-injected tests.

Use test-first implementation where practical. Do not touch Plan 02 Task 2+ in this directive.

Plan 02 Task 1 verification:

```bash
npm run build
node --test test/workers/runtime-layout.test.mjs
npm run test:workers
npm test
git diff --check
```

Have a fresh reviewer inspect Task 1 for Mac-default compatibility, Hermes paths, consistent layout threading, injection compatibility, and scope control before marking it complete.

Expected local commit message after approval:

```text
refactor: make worker runtime layout portable
```

## Safety Bounds

```text
PRODUCTION_HERMES_MUTATION=FORBIDDEN
PRODUCTION_LMS_MUTATION=FORBIDDEN
PRODUCTION_DOCKER_MUTATION=FORBIDDEN
PRODUCTION_SERVICE_RESTART_STOP_INSTALL=FORBIDDEN
SECRETS_READ_PRINT_COMMIT=FORBIDDEN
SOURCE_FORCE_PUSH=FORBIDDEN
SOURCE_MAIN_MERGE=FORBIDDEN
SOURCE_REMOTE_PUSH=NOT_AUTHORIZED
GIT_RESET_HARD_ON_REAL_WORKSPACE=FORBIDDEN
GIT_CLEAN_FDX_ON_REAL_WORKSPACE=FORBIDDEN
ONLY_COORDINATION_REPO_REPORTING_PUSH=ALLOWED
PLAN_02_TASK_2_PLUS=NOT_AUTHORIZED_IN_THIS_DIRECTIVE
```

If a step would require privileged production mutation, credentials, destructive cleanup, or an irreversible action, stop and report instead.

## Required Handoff

When finished, blocked, or ready for ChatGPT review, write a sanitized report under `agent-bridge/reports/2026-08-20/` and update bridge state/processed ledger according to `PROTOCOL.md`.

Use this report schema:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-HERMES-0001
REPLY-TO: CG-HERMES-0001
TASK-ID: HERMES-FOG-P01T6-P02T1
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED | NEEDS_HUMAN_PRESENCE
PLAN01_FINAL_ROUND3_COMMIT: <sha|UNAVAILABLE>
PLAN01_FINAL_REVIEW: APPROVED|CHANGES_REQUESTED|NOT_RUN
PLAN01_FEATURE_HEAD: <sha>
PLAN01_GIT_STATUS_CLEAN: YES|NO
PLAN01_DIFF_CHECK: PASS|FAIL|NOT_RUN
PLAN01_BUILD: PASS|FAIL|NOT_RUN
PLAN01_NPM_TEST: <exact result|NOT_RUN>
PLAN01_WORKER_TESTS: <exact result|NOT_RUN>
PLAN01_HERMES_TESTS: <exact result|NOT_RUN>
PLAN01_JSONRPC_ACCEPTANCE: <exact result|NOT_RUN>
MCP_SCHEMA_COUNT: <number|UNKNOWN>
HERMES_GATEWAY_SERVICE: <exact read-only state>
LMS_PRODUCTION_SERVICE: <exact read-only state>
DOCKER_SERVICE: <exact read-only state>
PRODUCTION_HERMES_MCP_INSTALLED: YES|NO|UNKNOWN
PRODUCTION_HERMES_CHANGED: NO|YES
PLAN01_STATUS: COMPLETE|BLOCKED
PLAN02_TASK1_STARTED: YES|NO
PLAN02_TASK1_COMMIT: <sha|NOT_CREATED>
PLAN02_TASK1_REVIEW: APPROVED|CHANGES_REQUESTED|NOT_RUN
PLAN02_TASK1_BUILD: PASS|FAIL|NOT_RUN
PLAN02_TASK1_TEST: <exact result|NOT_RUN>
PLAN02_TASK1_WORKER_TESTS: <exact result|NOT_RUN>
PLAN02_TASK1_NPM_TEST: <exact result|NOT_RUN>
SECRETS_EXPOSED: NO|YES
SECURITY_ANOMALY: NO|YES
NEXT_ACTION: WAIT
```

Then stop and wait for ChatGPT review. Do not continue to Plan 02 Task 2.
