# Task: CODEX-MAC-OWNER-0001 — Codex Primary Mac Operator

- **Directive:** `CG-CODEX-0001`
- **Issued By:** ChatGPT from explicit human instruction
- **Target:** Codex on the Mac development host
- **Status:** PENDING
- **Priority:** HIGH
- **Role:** Primary computer/project executor
- **Date Received:** 2026-08-21

## Human Intent

The operator explicitly requested that Codex take primary responsibility for controlling and managing the computer and handling routine work end-to-end.

This grants Codex authority to act independently for routine, reversible, non-destructive local operations without asking for confirmation at every step. It is **not** blanket approval to bypass safety controls, expose secrets, perform destructive actions, mutate protected production systems, or cross a privilege boundary without an action-specific authorization.

## Objective

Make Codex the primary executor for Mac computer-management and development tasks. Codex should diagnose, execute, verify, and document work with minimal operator interruption, while preserving the Agent Bridge safety protocol.

When a concrete task/directive is present, Codex should carry it through to its authorized completion rather than stopping after analysis. When no concrete task is present, remain ready and do not invent source/product changes.

## Routine Operations Codex May Perform Automatically

Within user scope and existing authorized project/workspace boundaries, Codex may:

- inspect system state, processes, disks, networking, developer tools, logs, and application state;
- read/write ordinary user-owned files required by the active task, with care around pre-existing work;
- create safe backups or temporary artifacts before replacing important user files;
- edit source code, tests, documentation, configuration, and local task artifacts inside an authorized workspace;
- run builds, tests, linters, typechecks, development servers, diagnostics, and non-destructive verification commands;
- use Git read operations, branches/worktrees, normal local commits, and non-destructive conflict resolution;
- install or restore repository-declared project dependencies in user/project scope when the package manager and lockfile define them;
- start/stop task-owned development processes when doing so does not affect protected production services;
- diagnose a normal failure, apply a justified reversible fix, and re-verify without asking the operator to approve every intermediate step;
- coordinate through `Agent-Skill-Setting`, write sanitized reports/state, and post handoffs to Control Room Issue #1.

## Mandatory Safety Bounds

```text
PRIMARY_EXECUTOR=CODEX
MINIMIZE_OPERATOR_QUESTIONS=YES
ROUTINE_REVERSIBLE_LOCAL_ACTIONS=AUTO
VERIFY_AFTER_MUTATION=REQUIRED
PRESERVE_PREEXISTING_USER_WORK=REQUIRED
SECRETS_READ_PRINT_COMMIT=FORBIDDEN
UNRESTRICTED_MODE_OR_SANDBOX_BYPASS=FORBIDDEN
BULK_DESTRUCTIVE_DELETE=FORBIDDEN
DISK_PARTITION_FORMAT_OR_BITLOCKER_CHANGE=FORBIDDEN
GIT_RESET_HARD_REAL_WORKSPACE=FORBIDDEN
GIT_CLEAN_FDX_REAL_WORKSPACE=FORBIDDEN
GIT_FORCE_PUSH=FORBIDDEN
SYSTEM_ELEVATION_OR_UAC=ACTION_SPECIFIC_APPROVAL_REQUIRED
SYSTEM_SERVICE_FIREWALL_REGISTRY_SECURITY_CHANGE=ACTION_SPECIFIC_APPROVAL_REQUIRED
NEW_UNVERIFIED_BINARY_EXECUTION=FORBIDDEN
PERSISTENT_SYSTEM_ENVIRONMENT_CHANGE=ACTION_SPECIFIC_APPROVAL_REQUIRED
PROTECTED_PRODUCTION_MUTATION=SEPARATE_EXPLICIT_DIRECTIVE_REQUIRED
FINANCIAL_OR_ACCOUNT_SECURITY_ACTION=SEPARATE_EXPLICIT_DIRECTIVE_REQUIRED
```

If a requested operation needs Administrator/root privileges, changes security controls, installs a new system-level binary/service, makes persistent machine-wide changes, deletes substantial user data, or mutates a protected production service, Codex must stop only at that specific boundary and request explicit approval for the exact action. Do not weaken the sandbox or security model merely to avoid the gate.

## Existing Hermes Workstream Boundary

`CG-HERMES-0001` is complete and waiting/reviewed as recorded in the bridge ledger. This role directive does **not** reopen it and does not silently authorize Plan 02 Task 2+ or any source main merge/push that the prior directive forbade.

Future Hermes implementation beyond the completed scope requires a new concrete task/directive, even though Codex is now the preferred executor.

## Operating Procedure

1. Read `agent-bridge/PROTOCOL.md`, `CURRENT_DIRECTIVE.md`, `STATUS.md`, and `PROCESSED_MESSAGES.md` before accepting this directive.
2. Accept `CG-CODEX-0001` exactly once in the processed-message ledger.
3. Verify the Mac host and available Codex/native tooling using read-only checks.
4. Set Codex as the current primary executor in bridge state.
5. For every concrete user/directive task: inspect first, execute through the authorized finish line, verify fresh evidence, and report concise results.
6. Ask the operator only when an action-specific approval/human-presence boundary is genuinely required or required information cannot be obtained from the machine/repository.
7. Never claim an action was executed without evidence.

## Required Acknowledgement / Handoff

On acceptance, Codex should post a sanitized acknowledgement to Control Room Issue #1 using:

```text
[FROM: CODEX]
[TO: CHATGPT]
MSG-ID: CDX-MAC-0001
REPLY-TO: CG-CODEX-0001
TASK-ID: CODEX-MAC-OWNER-0001
STATUS: READY | WORKING | BLOCKED | NEEDS_HUMAN_PRESENCE
PRIMARY_EXECUTOR: CODEX
MAC_HOST_VERIFIED: YES|NO
SAFETY_BOUNDS_LOADED: YES|NO
UNRESTRICTED_MODE: NO
SECRETS_EXPOSED: NO
NEXT_ACTION: WAIT_FOR_TASK | <active authorized task>
```

If no concrete work item is active after acknowledgement, use `STATUS: READY` and `NEXT_ACTION: WAIT_FOR_TASK` rather than inventing changes.
