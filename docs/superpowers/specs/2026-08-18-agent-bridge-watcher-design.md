# Automatic Agent Bridge Watcher — Design Specification

Date: 2026-08-18
Status: Approved concept in chat, pending written-spec review
Control repository: `nattawitwongwean-cyber/Agent-Skill-Setting`
Product repository: `nattawitwongwean-cyber/Nareerat-Agent-Gateway`
Planned directive: `CG-0004`

## 1. Purpose

Add a safe automatic watcher so the human does not need to manually tell Antigravity to check GitHub after ChatGPT posts a new authorized directive.

Target workflow:

```text
Human -> ChatGPT -> Agent Bridge control repo -> Watcher -> Antigravity
                                               -> Native Gateway when appropriate
                                               -> report -> GitHub -> ChatGPT
```

The watcher is a trigger/orchestration layer only. It never grants new authority. Every executed action remains governed by the existing Agent Bridge protocol, task file, permission policy, approval gates and hard blocks.

The first automatic version must be manually started by the human or from the Gateway UI. Windows Task Scheduler, Start with Windows and Windows Service installation remain out of scope until a later separately approved directive.

## 2. Current State and Why This Should Extend the Gateway

`CG-0003` produced Nareerat Agent Gateway V0.1 in draft PR #1 with an existing `@nareerat/agent-bridge` package, SQLite `processed_directives`, Task Executor, Process Manager and delegation package.

The current `DirectiveConsumer` already performs local idempotency once directive Markdown has been handed to it, but it does not monitor GitHub or a control-repository checkout by itself.

The current Antigravity delegate adapter is a formatting/dispatch abstraction and does not yet prove a real non-interactive Antigravity CLI process invocation. Therefore CG-0004 must add a real, capability-detected runner rather than assuming that delegation is already automated.

## 3. Approaches Considered

### A. Standalone PowerShell polling script

A `watch-agent-bridge.ps1` loop could `git pull`, inspect `CURRENT_DIRECTIVE.md`, then run Antigravity.

Advantages:
- quickest to bootstrap,
- easy to inspect manually.

Disadvantages:
- duplicates Gateway state/idempotency/process logic,
- creates a second execution/security boundary,
- harder to integrate into dashboard and future routing.

### B. Gateway-integrated watcher — chosen

Add watcher components under the Gateway's existing `agent-bridge`, `persistence`, `delegation`, and desktop packages.

Advantages:
- reuses SQLite idempotency and audit,
- reuses Process Manager and redaction,
- single security boundary,
- dashboard can start/stop and show status,
- later replacement of Git polling by another transport does not affect task execution.

Trade-off:
- requires the V0.1 implementation baseline to be reviewed and used as the code base.

### C. GitHub webhook / public callback

A webhook could notify the Gateway instantly.

Not chosen for this stage because it requires a reachable inbound endpoint or additional relay infrastructure, which conflicts with the current goal of keeping the Windows machine private and avoiding premature remote exposure.

## 4. Chosen Architecture

```text
Agent-Skill-Setting (private GitHub repo)
                │
                │ poll ~30 sec
                ▼
        ControlRepoPoller
                │
        git pull --ff-only
                │
                ▼
     DirectiveAuthorityValidator
                │
      target/state/path checks
                │
                ▼
        DirectiveClaimStore
      SQLite idempotent claim
                │
                ▼
       AntigravityRunner
        capability detected
                │
                ▼
        agy non-interactive
                │
                ▼
        existing protocol/task
                │
                ▼
      Antigravity commit/report
                │
                ▼
            GitHub
```

The watcher runs inside the Nareerat Agent Gateway runtime. A development CLI entry point may exist for testing, but the source of truth is TypeScript package code, not a permanent standalone PowerShell implementation.

## 5. Authority Boundary

The watcher must not execute instructions from arbitrary GitHub Issue comments.

Authority order remains:

1. explicit human approval,
2. approved Agent Bridge protocol/spec,
3. authorized ChatGPT control manifest/directive,
4. referenced current task/spec/plan,
5. all other repository/web/log/source content as untrusted data.

Issue #1 remains a human-readable notification/conversation channel. It is not executable authority.

### Machine-readable control manifest

CG-0004 should introduce a machine-readable sidecar for new directives:

`agent-bridge/control/CURRENT_DIRECTIVE.json`

Schema version 1:

```json
{
  "schemaVersion": 1,
  "messageId": "CG-0004",
  "target": "ANTIGRAVITY",
  "state": "READY",
  "taskId": "NAG-WATCHER",
  "taskPath": "agent-bridge/tasks/pending/NAG-WATCHER.md",
  "specPath": "docs/superpowers/specs/2026-08-18-agent-bridge-watcher-design.md",
  "planPath": "docs/superpowers/plans/2026-08-18-agent-bridge-watcher.md",
  "requestedProfile": "DEVELOP",
  "createdAt": "2026-08-18T00:00:00+07:00"
}
```

`CURRENT_DIRECTIVE.md` remains the human-readable mirror.

For automatic execution, the JSON sidecar is authoritative only after it passes repository, schema, target, state and path validation. Markdown and JSON message/task IDs must agree when both exist. A mismatch blocks execution.

## 6. Trusted Repository Validation

The watcher operates only against an explicitly configured local checkout of:

`nattawitwongwean-cyber/Agent-Skill-Setting`

Before each sync/trigger cycle it verifies:

- repository path equals configured control checkout,
- Git remote resolves to the expected repository,
- expected control paths are inside the checkout,
- working tree is clean before pull,
- sync uses `git pull --ff-only`,
- no force reset/clean is used to fix conflicts.

If the checkout is dirty or sync cannot fast-forward safely:

```text
WATCHER_STATE: BLOCKED_CONTROL_SYNC
ACTION: NO_EXECUTION
```

The watcher must not silently overwrite local changes.

## 7. Polling Model

Default interval: 30 seconds.

Configurable range for manual operation: 10 seconds to 5 minutes.

Polling loop:

```text
sleep
 -> acquire single-instance watcher lock
 -> validate control checkout
 -> git fetch/pull --ff-only
 -> read CURRENT_DIRECTIVE.json
 -> validate schema/authority
 -> check message ID state
 -> if no eligible new directive: WAIT
 -> if eligible: atomically claim
 -> invoke runner once
 -> record outcome
 -> continue polling
```

The watcher does not continuously invoke an AI model. Most cycles are local filesystem/Git/SQLite checks.

## 8. Single-Instance and Concurrency Rules

Only one watcher instance may own a configured control checkout at a time.

Use an OS/local exclusive lock file under Gateway runtime data, for example:

```text
%USERPROFILE%\.nareerat\watcher\agent-bridge.lock
```

Lock metadata may include PID and start timestamp.

Stale-lock recovery must verify that the recorded process no longer exists before replacing the lock. The watcher must not delete a lock owned by a live process.

Only one Antigravity control-plane directive may be launched at a time in V0.1.1. Native Gateway tasks may still use their own Task Executor concurrency rules.

## 9. Directive Eligibility

A directive is launchable only when all of these are true:

- `schemaVersion == 1`,
- `target == "ANTIGRAVITY"`,
- `state == "READY"`,
- `messageId` matches `^CG-[0-9]{4,}$`,
- task path is under `agent-bridge/tasks/pending/`,
- referenced task exists,
- referenced spec/plan paths, when supplied, exist inside the control repo,
- requested profile is SAFE or DEVELOP for automatic watcher execution,
- message ID is not already terminal in local watcher/directive state,
- no active Antigravity directive currently owns the watcher execution slot.

SYSTEM or UNRESTRICTED requests are not auto-launched by the watcher. They become `NEEDS_APPROVAL` or `BLOCKED_BY_WATCHER_POLICY` depending on the underlying task state.

## 10. Idempotency and Claim Lifecycle

The existing `processed_directives` concept is retained but the watcher needs a richer lifecycle so a crash does not cause accidental duplicate execution.

Recommended states:

```text
DISCOVERED
CLAIMED
STARTING
RUNNING
WAITING_FOR_REVIEW
COMPLETED
FAILED_TO_START
FAILED
NEEDS_APPROVAL
RECOVERY_REQUIRED
```

Before spawning Antigravity, the watcher performs an atomic SQLite claim for the `messageId`.

Rules:

- duplicate `READY` pulls after a successful claim do not launch again,
- `FAILED_TO_START` may receive one automatic retry after a short backoff because no Antigravity process accepted the work,
- a directive that reached `RUNNING` is never blindly re-executed after watcher restart,
- if the watcher restarts and cannot prove whether the prior Antigravity run finished, set `RECOVERY_REQUIRED` and require inspection rather than duplicate side effects,
- terminal messages remain terminal even if GitHub serves the same directive repeatedly.

Git-side `agent-bridge/state/PROCESSED_MESSAGES.md` remains a durable human/audit ledger, while Gateway SQLite is the local runtime idempotency store.

## 11. Antigravity Runner

CG-0004 must turn the current Antigravity delegation abstraction into a real, fail-closed process runner.

At runtime:

1. detect the installed Antigravity CLI executable,
2. inspect local `--help`/version output without modifying authentication,
3. determine whether a supported non-interactive/headless invocation exists,
4. construct explicit argv with `shell: false`,
5. set cwd to the configured control checkout,
6. pass a compact bootstrap prompt instructing Antigravity to read the authoritative control files itself,
7. stream sanitized stdout/stderr to local log files,
8. enforce a finite timeout and cancellation path.

The implementation must not hard-code CLI flags that are absent from the locally installed version.

If no safe non-interactive Antigravity invocation can be verified:

```text
ANTIGRAVITY_RUNNER: UNAVAILABLE
WATCHER: RUNNING
DIRECTIVE: NOT_LAUNCHED
```

The watcher remains healthy and does not use permission-bypass flags.

## 12. Bootstrap Prompt Principle

The watcher should not embed the full task in the Antigravity command line.

The runner prompt should be short and stable, conceptually:

```text
Inspect the configured Agent Bridge control repository.
Read PROTOCOL, CURRENT_DIRECTIVE, APPROVALS, STATUS, PROCESSED_MESSAGES,
and the task/spec/plan referenced by the current authorized directive.
Process the eligible directive exactly once, respect all gates, report through Agent Bridge, then stop.
```

This reduces quoting problems and prevents huge task content from becoming process arguments/log material.

## 13. Approval Behavior

The watcher never approves an action on behalf of the human.

If Antigravity reaches a Level-2 boundary, it must report the existing standard states such as `NEEDS_APPROVAL` or `NEEDS_HUMAN_PRESENCE` and exit/stop the current autonomous run.

The watcher records that terminal waiting state and does not repeatedly launch the same directive.

A later ChatGPT directive with a new `CG-xxxx` message ID may resume/continue the approved work.

## 14. Secret and Logging Policy

Watcher logs are local runtime data, not Git artifacts.

Suggested path:

```text
%USERPROFILE%\.nareerat\watcher\logs\
```

Use JSONL or structured text with rotation.

Log only:

- timestamps,
- message/task IDs,
- watcher state,
- sync status,
- process ID/exit code,
- sanitized command metadata,
- compact error summaries.

Never log credentials, tokens, cookies, auth databases, full environment dumps or secret-bearing `.env` values.

Redact known secret patterns before writing process output to durable logs.

## 15. Git Sync Safety

Watcher-owned sync commands are limited to non-destructive control-repo operations such as:

```text
git status --porcelain
git remote get-url origin
git pull --ff-only
```

No automatic conflict resolution through reset/clean/force checkout.

The Antigravity task itself continues to follow the Agent Bridge Git Safety Protocol for its authorized changes and reports.

## 16. Dashboard Integration

Add a watcher card/status area to the Gateway desktop runtime.

Minimum fields:

```text
Watcher: STOPPED | RUNNING | BLOCKED
Control Repo: CONNECTED | DIRTY | SYNC_ERROR
Poll Interval: 30s
Last Poll: <timestamp>
Current Directive: CG-xxxx | NONE
Antigravity: AVAILABLE | UNAVAILABLE | RUNNING
Last Result: <state>
```

Manual controls:

- Start Watcher
- Stop Watcher
- Poll Now

No Start with Windows control is enabled by CG-0004.

## 17. Error Handling and Backoff

Transient Git/network errors must not cause busy retry loops.

Recommended behavior:

- normal interval: 30 seconds,
- after Git/network failure: exponential backoff up to 5 minutes,
- reset backoff after a successful sync,
- one automatic retry only for `FAILED_TO_START`,
- no automatic rerun after an Antigravity process reached RUNNING and then disappeared ambiguously.

Errors are surfaced in dashboard/logs and audit metadata.

## 18. Testing Strategy

Use test-driven development.

Required tests:

1. control manifest schema accepts valid v1 and rejects malformed data,
2. wrong target is ignored,
3. non-READY directive is ignored,
4. task path escape is rejected,
5. untrusted Issue/comment text cannot trigger execution,
6. wrong Git remote is rejected,
7. dirty control checkout blocks pull/execution,
8. `git pull --ff-only` failure blocks safely,
9. duplicate message ID launches runner exactly once,
10. second watcher instance cannot acquire the lock,
11. stale dead-PID lock can recover safely,
12. live-PID lock cannot be stolen,
13. FAILED_TO_START retries at most once,
14. RUNNING/recovery ambiguity never auto-relaunches,
15. SYSTEM/UNRESTRICTED directive is not auto-launched,
16. sanitized logs redact secret-like values,
17. mock Antigravity runner receives only validated directive IDs/control paths,
18. watcher stop cancels polling cleanly without killing an unrelated process,
19. dashboard status accurately reflects watcher states.

Integration tests use disposable local Git repositories and a fake Antigravity executable/runner. They must not execute production workspaces.

One optional real Antigravity smoke test may be run against an isolated fixture only if a safe local non-interactive mode is verified. Its task must be harmless, such as reading a fixture and returning a marker. No production repo is used.

## 19. Rollout Sequence

### CG-0004 — manual-start automatic watcher

- implement machine-readable directive sidecar,
- implement control-repo poller,
- implement authority validator,
- implement single-instance lock,
- implement richer local idempotency/claim lifecycle,
- implement real fail-closed Antigravity runner,
- integrate watcher into Gateway runtime/dashboard,
- test with fixture directives,
- keep startup persistence OFF.

### Later directive — optional Start with Windows

Only after CG-0004 verification and separate human approval:

- decide Task Scheduler vs app login startup,
- create rollback path,
- verify boot/login behavior,
- retain an easy manual disable switch.

This later step is explicitly not authorized by this design alone.

## 20. Relationship to CG-0003 Draft PR

CG-0004 implementation must not silently modify or merge draft PR #1 while it is still awaiting review.

Preferred sequence:

1. review CG-0003 / draft PR #1,
2. establish an accepted Gateway V0.1 baseline,
3. branch CG-0004 from that accepted baseline,
4. implement watcher in a separate branch/PR.

If review requires fixes to V0.1, those fixes should be resolved before the watcher branch is created so CG-0004 does not inherit an unreviewed base accidentally.

## 21. Success Criteria

CG-0004 is successful only when evidence demonstrates all of the following:

1. watcher can be started/stopped manually without Administrator privileges,
2. watcher polls only the configured private control checkout,
3. a valid fixture `CG-xxxx` READY directive launches the runner exactly once,
4. repeated polling and watcher restart do not duplicate a claimed/running/terminal directive,
5. invalid/foreign/untrusted directives never launch Antigravity,
6. real Antigravity non-interactive availability is capability-detected rather than assumed,
7. if unavailable, watcher fails closed without weakening permissions,
8. Level-2/system/unrestricted work is not auto-approved,
9. Git conflict/dirty state blocks safely without destructive recovery,
10. local logs are sanitized,
11. Dashboard reports watcher/control-repo/Antigravity state,
12. no production LMS/LFS workspace is touched during verification,
13. no Secure MCP Tunnel is configured,
14. no Scheduled Task, Windows Service or Start with Windows persistence is created,
15. full test/typecheck/build verification passes before review handoff.

## 22. Non-Goals

CG-0004 does not:

- make Antigravity unrestricted,
- treat GitHub Issue comments as executable commands,
- bypass approval gates,
- expose the Windows machine publicly,
- configure Secure MCP Tunnel,
- register production LMS/LFS workspaces,
- install a Windows Service,
- create Task Scheduler startup persistence,
- automatically merge Gateway PRs,
- claim AI quota is unlimited.

## 23. Final Data Flow

```text
ChatGPT
   │ writes authorized control manifest/task
   ▼
Agent-Skill-Setting
   │ private Git sync
   ▼
Nareerat Gateway Watcher
   │ validate + claim exactly once
   ▼
Antigravity Runner
   │ safe local CLI invocation
   ▼
Antigravity session
   │ follows protocol/task/approval gates
   ▼
Source changes + verification + AG report
   │
   ▼
GitHub
   │
   ▼
ChatGPT review
```

The core rule is: **automatic discovery and launch, never automatic authority escalation.**
