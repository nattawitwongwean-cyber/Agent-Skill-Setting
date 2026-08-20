# Current Directive

- **Directive:** `CG-CODEX-0001`
- **Source:** Explicit human instruction via ChatGPT
- **Target:** Codex on the Mac development host
- **Scope:** Establish Codex as the primary executor for routine Mac computer-management and development work, with minimal operator interruption and strict Agent Bridge safety bounds
- **Date Received:** 2026-08-21
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/CODEX-MAC-OWNER-0001.md`

## Purpose

Codex is the preferred primary executor for subsequent computer/project work. For routine reversible local actions, Codex should inspect, act, verify, and finish the authorized task without asking for confirmation at every intermediate step.

This is an executor/operating-model directive, not unlimited permission. It does not authorize bypassing sandbox/security controls, exposing secrets, destructive machine actions, protected production mutation, or privilege-boundary changes without an action-specific approval.

The completed `CG-HERMES-0001` workstream remains closed. This directive does not reopen it and does not authorize Hermes Plan 02 Task 2+ by itself.

## Required Start Sequence

1. Read `agent-bridge/PROTOCOL.md`, this directive, `agent-bridge/state/STATUS.md`, and `agent-bridge/state/PROCESSED_MESSAGES.md`.
2. Read `agent-bridge/tasks/pending/CODEX-MAC-OWNER-0001.md` fully.
3. Accept `CG-CODEX-0001` exactly once.
4. Verify the Mac host and available Codex/native tooling using read-only checks.
5. Set Codex as primary executor in bridge state.
6. Post acknowledgement as `CDX-MAC-0001` to Control Room Issue #1.
7. If no concrete task is active, remain `READY` with `NEXT_ACTION: WAIT_FOR_TASK`; do not invent source/product changes.

## Active Bounds

```text
PRIMARY_EXECUTOR=CODEX
ROUTINE_REVERSIBLE_LOCAL_ACTIONS=AUTO
MINIMIZE_OPERATOR_QUESTIONS=YES
VERIFY_AFTER_MUTATION=REQUIRED
PRESERVE_PREEXISTING_USER_WORK=REQUIRED
SECRETS_EXPOSED=NO
UNRESTRICTED_MODE=FORBIDDEN
SANDBOX_BYPASS=FORBIDDEN
BULK_DESTRUCTIVE_DELETE=FORBIDDEN
DISK_OR_PARTITION_DESTRUCTIVE_ACTION=FORBIDDEN
GIT_RESET_HARD_REAL_WORKSPACE=FORBIDDEN
GIT_CLEAN_FDX_REAL_WORKSPACE=FORBIDDEN
GIT_FORCE_PUSH=FORBIDDEN
SYSTEM_ELEVATION=ACTION_SPECIFIC_APPROVAL_REQUIRED
SYSTEM_SERVICE_FIREWALL_REGISTRY_SECURITY_CHANGE=ACTION_SPECIFIC_APPROVAL_REQUIRED
PERSISTENT_MACHINE_WIDE_CHANGE=ACTION_SPECIFIC_APPROVAL_REQUIRED
NEW_UNVERIFIED_BINARY_EXECUTION=FORBIDDEN
PROTECTED_PRODUCTION_MUTATION=SEPARATE_EXPLICIT_DIRECTIVE_REQUIRED
```

## Required Acknowledgement

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
