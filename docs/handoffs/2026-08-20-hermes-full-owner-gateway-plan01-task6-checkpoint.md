# @Hermes Full Owner Gateway — Plan 01 Task 6 Recovery Checkpoint

Timestamp: 2026-08-20 21:25+07:00

## Scope

Durable checkpoint for the local Mac implementation workspace:

- Project path: `/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway`
- Feature worktree: `/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway/.worktrees/hermes-full-owner-gateway`
- Feature branch: `feature/hermes-full-owner-gateway`
- Plan: `docs/superpowers/plans/2026-08-20-hermes-full-owner-gateway-01-linux-core.md`
- SDD ledger: `.superpowers/sdd/2026-08-20-hermes-full-owner-gateway-01-linux-core/progress.md`

This checkpoint exists because the ChatGPT Mac connector disappeared from the active session after Plan 01 Task 6 fix round 3 verification had started. Do not reconstruct the local feature from the stale remote `Nareerat-Agent-Gateway` main branch.

## Git state at last verified access

Feature branch accepted Task 6 initial commit:

```text
2a152c3 test: verify hermes linux core over mcp
```

Task 6 review-fix commits live on isolated local worker branches and were not yet cherry-picked into the feature branch:

```text
7b174a7 test: harden hermes linux acceptance
492e1f7 test: ensure hermes acceptance kills stuck gateway
```

A third review-fix was implemented in worker `w-20260820210909-9bcab979` based on `492e1f7`, but the session lost Mac access before its final commit/result could be retrieved.

## Round 3 change scope

Only:

```text
test/hermes/linux-jsonrpc-acceptance.mjs
```

Round 3 addressed the two remaining cumulative review findings plus cleanup safety:

1. Reject JSON arrays as malformed JSON-RPC output (`Array.isArray(message)`).
2. Treat child exit evidence as `closed || child.exitCode !== null || child.signalCode !== null` rather than using `child.killed`.
3. Shutdown sequence remains `SIGTERM -> bounded wait -> SIGKILL -> bounded wait`.
4. If exit is still not observed after SIGKILL, throw `Hermes gateway shutdown timed out waiting for child exit after SIGKILL` rather than silently returning.
5. Wrap `gateway.shutdown()` in nested `try/finally` so temporary HOME cleanup runs even when shutdown throws.

## Fresh verification observed for round 3 before connector loss

```text
npm ci                                      PASS
npm run build                               PASS
npm run test:hermes                         33/33 PASS
node test/hermes/linux-jsonrpc-acceptance.mjs PASS
```

Acceptance output:

```text
initialize=PASS
tools/list=57
gateway_info=Hermes/linux
workspace/file read=PASS
owner_exec harmless command=NOT_ENABLED
owner_exec privilege escalation=POLICY_DENIED
git disposable status=NOT_ENABLED (sandbox unavailable)
high-risk admin/lms write tools=NOT_ENABLED
```

`npm test` inside isolated worker worktrees consistently fails for an unrelated sandbox boundary:

```text
EPERM: operation not permitted, open '/Users/nattawit/Library/Application Support/MacDevGateway/audit.log'
```

Controller/feature worktree `npm test` had previously passed with Mac lifecycle `6/6`; it must be rerun after integrating the final Task 6 fixes.

## Real Hermes read-only evidence already obtained

Temporary artifact smoke on host `hermes-Latitude-E6420` used `/tmp` only. Node runtime was `v22.23.2`.

```text
initialize=PASS
tools/list=57
gateway_info=Hermes/linux
```

Protected services remained:

```text
hermes-gateway.service=active
nattawit-lms-production-nginx.service=active
docker.service=active
```

No `hermes-mcp-*` user units were installed.

## Resume sequence — do not skip

1. Restore Mac connector/access to the local project.
2. Inspect worker `w-20260820210909-9bcab979` status/result and its branch/worktree.
3. Verify only `test/hermes/linux-jsonrpc-acceptance.mjs` changed relative to `492e1f7`.
4. Commit the round 3 fix if not already committed.
5. Run a final scoped/cumulative review from `2a152c3` through the round 3 commit. No open load-bearing findings are allowed before integration.
6. Cherry-pick `7b174a7`, `492e1f7`, and the accepted round 3 commit into `feature/hermes-full-owner-gateway` in order, unless the round 3 branch already contains the prior two commits and can be fast-forwarded/cherry-picked safely.
7. From the feature worktree run the complete Plan 01 end gate:

```bash
git status --porcelain
git diff --check
npm run build
npm test
npm run test:workers
npm run test:hermes
node test/hermes/linux-jsonrpc-acceptance.mjs
```

8. Re-run read-only Hermes service checks:

```bash
ssh hermes 'systemctl --user is-active hermes-gateway.service; systemctl --user is-active nattawit-lms-production-nginx.service; systemctl --user is-active docker.service; systemctl --user list-unit-files --no-pager | grep "^hermes-mcp-" || true'
```

9. Only if every Plan 01 end-gate requirement is green, record Plan 01 complete in the SDD ledger and begin Plan 02 Task 1 (`Parameterize worker runtime/state/worktree roots without changing Mac defaults`).
10. Do not install/restart any production Hermes MCP service in Plan 01/02.

## Required Plan 01 end-state evidence

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

## Current status

```text
STATUS=VERIFIED_PARTIAL
PLAN_01_TASK_6=FIX_ROUND_3_VERIFIED_LOCALLY_NOT_YET_FINAL_REVIEWED_OR_INTEGRATED
PLAN_02=NOT_STARTED
PRODUCTION_HERMES_CHANGED=NO
NEXT_ACTION=RECOVER_MAC_CONNECTOR_AND_RESUME_SEQUENCE_ABOVE
```
