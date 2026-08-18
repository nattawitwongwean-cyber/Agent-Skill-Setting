# Automatic Agent Bridge Watcher Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a manual-start automatic watcher to Nareerat Agent Gateway so new authorized ChatGPT directives in `Agent-Skill-Setting` can be detected, claimed exactly once, and launch Antigravity non-interactively without the human manually telling Antigravity to check GitHub.

**Architecture:** Extend the existing Gateway packages rather than creating a standalone PowerShell automation layer. The watcher validates a machine-readable control manifest from the trusted private control checkout, uses SQLite-backed atomic claims plus a single-instance lock, synchronizes only with safe Git operations, and launches a capability-detected Antigravity CLI runner. The watcher never grants new authority and fails closed on dirty Git state, unsupported CLI mode, approval-gated profiles, or ambiguous recovery.

**Tech Stack:** Windows 10 x64, Node.js 24, pnpm 10.15.0 via Corepack, TypeScript, `node:sqlite`, `execa`, Vitest, existing Nareerat Gateway runtime/dashboard, GitHub private control repository, Antigravity CLI `agy` capability detection.

**Spec:** `docs/superpowers/specs/2026-08-18-agent-bridge-watcher-design.md`

## Global Constraints

- Product repository: `nattawitwongwean-cyber/Nareerat-Agent-Gateway`.
- Control repository: `nattawitwongwean-cyber/Agent-Skill-Setting`.
- CG-0004 implementation must begin only from an explicitly accepted V0.1 baseline commit; do not silently build on an unreviewed PR head.
- Use branch `agent/cg-0004-watcher` from the accepted baseline commit.
- Keep Windows Task Scheduler, Start with Windows, Windows Service mode, Administrator/elevation, registry/service/firewall changes, SYSTEM profile execution, UNRESTRICTED profile execution, Secure MCP Tunnel setup and production LMS/LFS access out of CG-0004.
- The watcher may be started manually from the Gateway runtime/dashboard or a development CLI entry point only.
- Poll only the explicitly configured local checkout of `nattawitwongwean-cyber/Agent-Skill-Setting`.
- Issue comments are notification/conversation data and never executable authority.
- Automatic execution requires a valid `agent-bridge/control/CURRENT_DIRECTIVE.json` plus matching authorized task references.
- Git synchronization uses `git pull --ff-only`; never force-reset, force-clean or force-push to repair conflicts.
- Default poll interval is 30 seconds; manual configuration range is 10–300 seconds.
- Automatic watcher launch accepts only SAFE or DEVELOP requested profiles.
- Only one watcher instance may own the configured control checkout.
- Only one Antigravity control-plane directive may be RUNNING at a time.
- `agy` flags must be capability-detected from the locally installed `agy --help`; do not assume unsupported flags.
- Never use Antigravity permission-bypass flags.
- Antigravity output is evidence/data, not automatic proof of task completion.
- Watcher/runtime logs must redact secret-like values and must remain local runtime data.
- No credentials, tokens, cookies, private keys, auth/session databases or secret-bearing `.env` values may be committed.
- `No evidence -> no COMPLETED`.
- Finish with a separate draft PR and `AG-0004` handoff; do not merge automatically.

---

## Repository / File Map

Expected product-repo changes:

```text
Nareerat-Agent-Gateway/
├── apps/desktop/src/
│   ├── main.ts
│   ├── preload.ts
│   └── renderer/
│       ├── app.ts
│       └── watcher-view.ts
├── packages/agent-bridge/src/
│   ├── control-manifest.ts
│   ├── control-repo.ts
│   ├── watcher-lock.ts
│   ├── watcher-store.ts
│   ├── watcher-service.ts
│   ├── watcher-types.ts
│   └── index.ts
├── packages/delegation/src/
│   ├── antigravity-runner.ts
│   └── index.ts
├── packages/persistence/src/
│   └── schema.ts
├── tests/integration/
│   └── watcher-e2e.test.ts
└── docs/
    └── WATCHER-VERIFICATION.md
```

Expected control-repo additions once CG-0004 is activated:

```text
Agent-Skill-Setting/
└── agent-bridge/control/
    └── CURRENT_DIRECTIVE.json
```

Responsibilities:

- `control-manifest.ts`: schema validation and path/target/profile eligibility.
- `control-repo.ts`: trusted remote verification, dirty-state check, safe ff-only pull and manifest loading.
- `watcher-lock.ts`: local single-instance lock with dead-PID recovery.
- `watcher-store.ts`: atomic lifecycle claims and recovery-safe state in SQLite.
- `watcher-service.ts`: polling/backoff/orchestration; no direct shell construction.
- `antigravity-runner.ts`: capability-detected real `agy` process invocation and structured output handling.
- desktop files: read-only watcher status and explicit Start/Stop/Poll Now controls.

---

### Task 0: Establish the accepted V0.1 baseline before watcher work

**Files:**
- No product source changes.
- Read: Gateway draft PR #1 and Agent Bridge review state.

**Interfaces:**
- Produces an exact accepted baseline commit SHA used to create `agent/cg-0004-watcher`.

- [ ] **Step 1: Read the CG-0003 review result**

The implementation worker must confirm a ChatGPT review record explicitly identifies an accepted Gateway V0.1 commit. Do not infer acceptance from `AG-0003` saying tests passed.

- [ ] **Step 2: Refuse to branch from an unaccepted commit**

If no accepted SHA exists, report:

```text
STATUS: BLOCKED
REASON: V0.1_BASELINE_NOT_ACCEPTED
NEXT_ACTION: WAIT
```

and stop CG-0004 implementation.

- [ ] **Step 3: Create the watcher branch from the accepted SHA**

Run only after acceptance:

```powershell
git fetch origin
git status --short --branch
git checkout --detach <ACCEPTED_V01_SHA>
git checkout -b agent/cg-0004-watcher
git push -u origin agent/cg-0004-watcher
```

Expected: clean branch rooted exactly at the accepted baseline.

---

### Task 1: Add the machine-readable control manifest schema

**Files:**
- Create: `packages/agent-bridge/src/control-manifest.ts`
- Create: `packages/agent-bridge/src/control-manifest.test.ts`
- Modify: `packages/agent-bridge/src/index.ts`

**Interfaces:**

```ts
export type DirectiveTarget = "ANTIGRAVITY" | "NATIVE" | "CODEX" | "HYBRID";
export type DirectiveManifestState = "READY" | "WAITING" | "NEEDS_APPROVAL" | "NEEDS_CHATGPT_REVIEW" | "COMPLETED" | "BLOCKED";

export interface ControlDirectiveManifest {
  schemaVersion: 1;
  messageId: string;
  target: DirectiveTarget;
  state: DirectiveManifestState;
  taskId: string;
  taskPath: string;
  specPath?: string;
  planPath?: string;
  requestedProfile: "SAFE" | "DEVELOP" | "SYSTEM" | "UNRESTRICTED";
  createdAt: string;
}

export function parseControlManifest(jsonText: string): ControlDirectiveManifest;
export function validateControlManifestPaths(manifest: ControlDirectiveManifest): void;
export function isWatcherEligible(manifest: ControlDirectiveManifest): boolean;
```

- [ ] **Step 1: Write failing schema tests**

Tests must cover a valid v1 manifest, malformed JSON, wrong `schemaVersion`, invalid message ID, wrong target, non-READY state, SYSTEM/UNRESTRICTED profile, and task-path traversal.

Core assertions:

```ts
expect(parseControlManifest(validJson).messageId).toBe("CG-0004");
expect(() => parseControlManifest('{"schemaVersion":2}')).toThrow();
expect(() => validateControlManifestPaths({ ...valid, taskPath: "../escape.md" })).toThrow(/control path/i);
expect(isWatcherEligible({ ...valid, requestedProfile: "SYSTEM" })).toBe(false);
```

- [ ] **Step 2: Run the red test**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge/src/control-manifest.test.ts
```

Expected: FAIL because the module does not exist.

- [ ] **Step 3: Implement Zod-backed schema validation**

Require `messageId` to match `^CG-[0-9]{4,}$`. Normalize repository paths to POSIX separators before checking that `taskPath` starts with `agent-bridge/tasks/pending/` and that optional spec/plan paths are relative, non-empty and do not contain `..` segments.

- [ ] **Step 4: Verify green state**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge/src/control-manifest.test.ts
```

Expected: PASS.

- [ ] **Step 5: Commit**

```powershell
git add packages/agent-bridge/src/control-manifest.ts packages/agent-bridge/src/control-manifest.test.ts packages/agent-bridge/src/index.ts
git diff --cached --check
git commit -m "feat(bridge): validate machine-readable control manifest"
git push
```

---

### Task 2: Implement trusted control-repository synchronization

**Files:**
- Create: `packages/agent-bridge/src/control-repo.ts`
- Create: `packages/agent-bridge/src/control-repo.test.ts`

**Interfaces:**

```ts
export interface ControlRepoConfig {
  checkoutPath: string;
  expectedOwner: "nattawitwongwean-cyber";
  expectedRepo: "Agent-Skill-Setting";
}

export interface ControlSyncResult {
  state: "SYNCED" | "DIRTY" | "REMOTE_MISMATCH" | "SYNC_ERROR";
  manifestText?: string;
  error?: string;
}

export class ControlRepoPoller {
  constructor(config: ControlRepoConfig, deps?: ControlRepoDeps);
  syncAndRead(): Promise<ControlSyncResult>;
}
```

- [ ] **Step 1: Write failing tests using disposable local Git repositories**

Cover:

```text
correct GitHub remote + clean tree -> SYNCED
wrong owner/repo -> REMOTE_MISMATCH
dirty tree -> DIRTY
ff-only pull failure -> SYNC_ERROR
CURRENT_DIRECTIVE.json missing -> SYNC_ERROR
```

Use an injected Git command dependency in unit tests; do not require network access.

- [ ] **Step 2: Implement canonical Git remote validation**

Accept only canonical HTTPS or SSH forms that resolve to the configured owner/repo, for example:

```text
https://github.com/nattawitwongwean-cyber/Agent-Skill-Setting.git
git@github.com:nattawitwongwean-cyber/Agent-Skill-Setting.git
```

Reject remotes containing embedded credentials/userinfo or a different host/repository.

- [ ] **Step 3: Implement safe sync**

Use `execa("git", argv, { shell: false, cwd })` for:

```text
git status --porcelain
git remote get-url origin
git pull --ff-only
```

Never invoke reset, clean or force checkout.

- [ ] **Step 4: Verify**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge/src/control-repo.test.ts
```

Expected: PASS.

- [ ] **Step 5: Commit**

```powershell
git add packages/agent-bridge/src/control-repo.ts packages/agent-bridge/src/control-repo.test.ts
git commit -m "feat(bridge): add trusted ff-only control repo poller"
git push
```

---

### Task 3: Add a single-instance watcher lock

**Files:**
- Create: `packages/agent-bridge/src/watcher-lock.ts`
- Create: `packages/agent-bridge/src/watcher-lock.test.ts`

**Interfaces:**

```ts
export interface WatcherLockRecord { pid: number; startedAt: string; controlRepo: string; }
export class WatcherLock {
  acquire(): Promise<void>;
  release(): Promise<void>;
  isHeld(): Promise<boolean>;
}
```

- [ ] **Step 1: Write failing lock tests**

Test first acquisition, rejection of a second live owner, recovery of a stale dead-PID lock, and refusal to steal a lock when the process probe reports the PID alive.

- [ ] **Step 2: Implement exclusive creation**

Create the lock file using Node filesystem exclusive-create semantics (`flag: "wx"`) under Gateway runtime data. Store only PID, start time and configured control checkout path.

- [ ] **Step 3: Implement injectable process-liveness probe**

Default behavior may use `process.kill(pid, 0)`; treat permission-denied/EPERM as evidence that the process exists. Tests must inject deterministic liveness behavior.

- [ ] **Step 4: Verify and commit**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge/src/watcher-lock.test.ts
git add packages/agent-bridge/src/watcher-lock.ts packages/agent-bridge/src/watcher-lock.test.ts
git commit -m "feat(watcher): enforce a single watcher instance"
git push
```

---

### Task 4: Add atomic watcher claim lifecycle persistence

**Files:**
- Modify: `packages/persistence/src/schema.ts`
- Create: `packages/agent-bridge/src/watcher-store.ts`
- Create: `packages/agent-bridge/src/watcher-store.test.ts`

**Interfaces:**

```ts
export type WatcherDirectiveState =
  | "DISCOVERED"
  | "CLAIMED"
  | "STARTING"
  | "RUNNING"
  | "WAITING_FOR_REVIEW"
  | "COMPLETED"
  | "FAILED_TO_START"
  | "FAILED"
  | "NEEDS_APPROVAL"
  | "RECOVERY_REQUIRED";

export class WatcherStore {
  discover(messageId: string, taskId: string): WatcherRecord;
  claim(messageId: string): WatcherRecord;
  transition(messageId: string, state: WatcherDirectiveState, patch?: WatcherPatch): WatcherRecord;
  get(messageId: string): WatcherRecord | undefined;
  recoverAmbiguous(): WatcherRecord[];
}
```

- [ ] **Step 1: Add a dedicated `watcher_directives` table**

Schema fields:

```text
message_id TEXT PRIMARY KEY
task_id TEXT NOT NULL
state TEXT NOT NULL
attempt_count INTEGER NOT NULL DEFAULT 0
pid INTEGER
first_seen_at TEXT NOT NULL
claimed_at TEXT
started_at TEXT
finished_at TEXT
last_error TEXT
```

Do not overload existing `processed_directives`; that ledger remains compatible with the V0.1 consumer/audit path.

- [ ] **Step 2: Write failing idempotency tests**

Required behavior:

```text
same message discovered twice -> one row
first claim -> CLAIMED
second claim -> rejected/already claimed
FAILED_TO_START -> at most one retry
RUNNING on restart with no proven terminal result -> RECOVERY_REQUIRED
COMPLETED/WAITING_FOR_REVIEW -> never auto-relaunch
```

- [ ] **Step 3: Implement atomic claims using a SQLite transaction**

A claim must update only an eligible state and must fail if another process already advanced the row.

- [ ] **Step 4: Verify and commit**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge/src/watcher-store.test.ts
git add packages/persistence/src/schema.ts packages/agent-bridge/src/watcher-store.ts packages/agent-bridge/src/watcher-store.test.ts
git commit -m "feat(watcher): add crash-safe directive claim lifecycle"
git push
```

---

### Task 5: Implement a real fail-closed Antigravity CLI runner

**Files:**
- Create: `packages/delegation/src/antigravity-runner.ts`
- Create: `packages/delegation/src/antigravity-runner.test.ts`
- Modify: `packages/delegation/src/index.ts`

**Interfaces:**

```ts
export interface AntigravityCapabilities {
  available: boolean;
  version?: string;
  supportsPrint: boolean;
  supportsCwd: boolean;
  supportsStreamJson: boolean;
}

export interface AntigravityRunRequest {
  controlRepo: string;
  messageId: string;
  timeoutMs: number;
}

export interface AntigravityRunResult {
  state: "STARTED" | "COMPLETED" | "FAILED" | "UNAVAILABLE" | "TIMED_OUT";
  pid?: number;
  exitCode?: number;
  summary: string;
}

export class AntigravityRunner {
  detectCapabilities(): Promise<AntigravityCapabilities>;
  run(request: AntigravityRunRequest): Promise<AntigravityRunResult>;
  cancel(): Promise<void>;
}
```

- [ ] **Step 1: Write mocked capability tests**

Test help output containing `-p`/`--print`, `--cwd`, and `--output-format`; test missing print mode; test missing stream-json support. Missing safe print mode must result in `available: false` for automatic watcher execution.

- [ ] **Step 2: Implement capability detection**

Run:

```text
agy --version
agy --help
```

with `shell: false`, short timeout and no authentication/config mutation.

- [ ] **Step 3: Construct only verified argv**

When the local help confirms support, the preferred invocation is conceptually:

```text
agy -p <compact-bootstrap-prompt> --cwd <control-repo> --output-format stream-json
```

If `--output-format stream-json` is unavailable but safe print mode is available, use plain text output and mark structured progress unsupported. Never invent flags absent from help.

- [ ] **Step 4: Use a compact bootstrap prompt**

The prompt must tell Antigravity to read the authoritative files itself and process only the current validated directive. It must not inline the full task, credentials or repository file contents into argv.

- [ ] **Step 5: Add structured/local log handling**

Parse stream-json line-by-line when supported. Store sanitized local JSONL under Gateway runtime data. Redact token/password/secret/api-key/authorization-like values before durable logging.

- [ ] **Step 6: Verify with fake executable and optional real capability probe**

Unit tests use a fake executable/dependency. A real probe may run `agy --version` and `agy --help`; a real one-shot smoke test is optional and must use an isolated fixture with a harmless read-only marker task.

- [ ] **Step 7: Commit**

```powershell
git add packages/delegation/src/antigravity-runner.ts packages/delegation/src/antigravity-runner.test.ts packages/delegation/src/index.ts
git commit -m "feat(delegation): add capability-detected Antigravity runner"
git push
```

---

### Task 6: Implement WatcherService polling, backoff and launch policy

**Files:**
- Create: `packages/agent-bridge/src/watcher-types.ts`
- Create: `packages/agent-bridge/src/watcher-service.ts`
- Create: `packages/agent-bridge/src/watcher-service.test.ts`
- Modify: `packages/agent-bridge/src/index.ts`

**Interfaces:**

```ts
export interface WatcherStatus {
  state: "STOPPED" | "RUNNING" | "BLOCKED";
  controlRepoState: "UNKNOWN" | "CONNECTED" | "DIRTY" | "SYNC_ERROR" | "REMOTE_MISMATCH";
  pollIntervalMs: number;
  lastPollAt?: string;
  currentDirective?: string;
  antigravity: "UNKNOWN" | "AVAILABLE" | "UNAVAILABLE" | "RUNNING";
  lastResult?: string;
}

export class WatcherService {
  start(): Promise<void>;
  stop(): Promise<void>;
  pollNow(): Promise<void>;
  getStatus(): WatcherStatus;
}
```

- [ ] **Step 1: Write failing orchestration tests**

Required cases:

```text
valid new READY manifest -> one claim + one runner call
same manifest on next poll -> zero additional runner calls
wrong target/non-READY -> ignored
SYSTEM/UNRESTRICTED -> not launched
control repo DIRTY -> BLOCKED, zero runner calls
runner UNAVAILABLE -> watcher remains healthy, directive not launched
FAILED_TO_START -> one delayed retry maximum
RUNNING ambiguity after restart -> RECOVERY_REQUIRED, no relaunch
stop() -> cancels future poll timers cleanly
```

- [ ] **Step 2: Implement polling loop without overlapping polls**

A poll cycle acquires an in-process mutex/flag so timer and manual Poll Now cannot execute the same cycle concurrently.

- [ ] **Step 3: Implement exponential backoff**

Normal interval is configured 30s. Git/network sync errors double delay up to 300s; a successful sync resets to normal interval.

- [ ] **Step 4: Suspend control polling during an active Antigravity directive**

Do not run Git sync against the same checkout while the Antigravity runner owns it. Resume only after the runner exits and the watcher records its local lifecycle state.

- [ ] **Step 5: Map runner outcomes conservatively**

A zero process exit is not sufficient to mark the actual Agent Bridge task COMPLETED. Watcher state should become `WAITING_FOR_REVIEW` when the run exits normally and let committed Agent Bridge state/report provide task evidence.

- [ ] **Step 6: Verify and commit**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge/src/watcher-service.test.ts
git add packages/agent-bridge/src/watcher-types.ts packages/agent-bridge/src/watcher-service.ts packages/agent-bridge/src/watcher-service.test.ts packages/agent-bridge/src/index.ts
git commit -m "feat(watcher): poll validate claim and launch directives"
git push
```

---

### Task 7: Integrate watcher status and manual controls into Gateway runtime

**Files:**
- Modify: `apps/desktop/src/main.ts`
- Modify: `apps/desktop/src/preload.ts`
- Modify: existing renderer app/navigation files
- Create: `apps/desktop/src/renderer/watcher-view.ts`
- Test: `apps/desktop/src/watcher.test.ts`

**Interfaces:**

Runtime APIs:

```ts
startWatcher(): Promise<WatcherStatus>;
stopWatcher(): Promise<WatcherStatus>;
pollWatcherNow(): Promise<WatcherStatus>;
getWatcherStatus(): Promise<WatcherStatus>;
```

- [ ] **Step 1: Write failing runtime/UI tests**

Assert the runtime exposes watcher status and that Start/Stop/Poll Now call only the watcher service API. Assert no renderer code directly invokes `git`, `agy`, filesystem mutation or SQLite.

- [ ] **Step 2: Compose WatcherService in the Gateway main/runtime layer**

Watcher starts in `STOPPED` state. Gateway application startup must not automatically start it during CG-0004.

- [ ] **Step 3: Add status fields**

Display:

```text
Watcher
Control Repo
Poll Interval
Last Poll
Current Directive
Antigravity
Last Result
```

- [ ] **Step 4: Add explicit manual controls**

Controls: Start Watcher, Stop Watcher, Poll Now. Do not implement Start with Windows or Scheduled Task creation.

- [ ] **Step 5: Verify and commit**

```powershell
corepack pnpm@10.15.0 vitest run apps/desktop
corepack pnpm@10.15.0 build
git add apps/desktop
git commit -m "feat(desktop): add manual Agent Bridge watcher controls"
git push
```

---

### Task 8: Add end-to-end watcher safety verification

**Files:**
- Create: `tests/integration/watcher-e2e.test.ts`
- Create: `docs/WATCHER-VERIFICATION.md`

- [ ] **Step 1: Create disposable control-repo fixtures**

Build a temporary Git repository containing `agent-bridge/control/CURRENT_DIRECTIVE.json` plus fixture task/spec/plan files. Use a fake runner that records launches; never point E2E tests at the real control repo.

- [ ] **Step 2: Verify exactly-once launch**

Run multiple poll cycles against one valid READY fixture directive. Expected: runner call count remains exactly 1 after the first atomic claim.

- [ ] **Step 3: Verify restart behavior**

Persist a RUNNING watcher record, recreate runtime, and verify it transitions to `RECOVERY_REQUIRED` rather than launching again.

- [ ] **Step 4: Verify trust negatives**

Test wrong remote, dirty checkout, path traversal, wrong target, non-READY state, SYSTEM/UNRESTRICTED request, malformed manifest, fake Issue comment text and missing task file. Expected: no runner launch.

- [ ] **Step 5: Verify lock behavior**

Start one watcher instance; second instance must fail to acquire the control-checkout lock. Release first instance and verify a new instance can acquire it.

- [ ] **Step 6: Verify secret redaction**

Feed fake runner output containing values such as `token=abc123` and `Authorization: Bearer xyz`; durable test logs must contain `<REDACTED>` and not the original values.

- [ ] **Step 7: Optional real Antigravity smoke**

Only if `detectCapabilities()` confirms safe non-interactive print mode. Use a disposable fixture with a read-only marker instruction. Record exact version/help capability and result. If unsupported, record `ANTIGRAVITY_RUNNER: UNAVAILABLE` and do not weaken permissions.

- [ ] **Step 8: Run full verification**

```powershell
corepack pnpm@10.15.0 test
corepack pnpm@10.15.0 typecheck
corepack pnpm@10.15.0 build
git status --short
git diff --check <ACCEPTED_V01_SHA>...HEAD
```

Record exact counts/results in `docs/WATCHER-VERIFICATION.md`.

- [ ] **Step 9: Commit**

```powershell
git add tests/integration/watcher-e2e.test.ts docs/WATCHER-VERIFICATION.md
git commit -m "test: verify automatic Agent Bridge watcher"
git push
```

---

### Task 9: Activate CG-0004 control manifest and perform one real manual-start watcher trial

**Files in control repo:**
- Create/update: `agent-bridge/control/CURRENT_DIRECTIVE.json`
- Maintain matching: `agent-bridge/control/CURRENT_DIRECTIVE.md`
- Create/update CG-0004 task/report paths as directed by ChatGPT.

**Interfaces:**
- JSON and Markdown message/task IDs must match.

- [ ] **Step 1: Validate the real control checkout before trial**

Confirm clean tree, expected origin and no secret-bearing changes.

- [ ] **Step 2: Start watcher manually**

Use the Gateway runtime control, not Task Scheduler or Windows startup.

- [ ] **Step 3: Perform one controlled directive trial**

Use only the current authorized CG-0004 test/handoff scope. Confirm watcher discovers and claims the directive once and launches Antigravity only if the safe runner is available.

- [ ] **Step 4: Poll repeatedly after the trial**

Confirm the same CG-0004 message is not launched twice.

- [ ] **Step 5: Stop watcher manually**

Confirm lock release and clean shutdown.

---

### Task 10: Open separate draft PR and hand off AG-0004

**Files:**
- Update `README.md` or watcher docs with manual start/stop instructions and safety defaults.
- Update sanitized Agent Bridge report/state files.

- [ ] **Step 1: Verify the diff and secret safety**

```powershell
git status --short
git diff <ACCEPTED_V01_SHA>...HEAD
git diff --check <ACCEPTED_V01_SHA>...HEAD
```

Confirm no runtime log, token, credential or generated local database is staged.

- [ ] **Step 2: Open a draft watcher PR**

If V0.1 is not yet merged, open the watcher PR against the accepted V0.1 branch so the watcher diff is isolated. If the exact accepted V0.1 commit is already on `main`, target `main`.

Suggested title:

```text
feat: add automatic Agent Bridge watcher
```

Do not merge.

- [ ] **Step 3: Report through Agent Bridge**

Required handoff:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-0004
REPLY-TO: CG-0004
TASK-ID: NAG-WATCHER
STATUS: NEEDS_CHATGPT_REVIEW | BLOCKED
SOURCE_BRANCH: agent/cg-0004-watcher
PR: <draft PR reference or NONE>
TESTS: <exact pass/fail count>
TYPECHECK: <PASS|FAIL|NOT_RUN>
BUILD: <PASS|FAIL|NOT_RUN>
WATCHER_E2E: <PASS|FAIL|NOT_RUN>
EXACTLY_ONCE: <PASS|FAIL|NOT_RUN>
LOCK_TEST: <PASS|FAIL|NOT_RUN>
CONTROL_REPO_VALIDATION: <PASS|FAIL|NOT_RUN>
ANTIGRAVITY_RUNNER: <AVAILABLE|UNAVAILABLE|PASS|FAIL>
REAL_WATCHER_TRIAL: <PASS|FAIL|NOT_RUN>
START_WITH_WINDOWS: NOT_CONFIGURED
WINDOWS_SERVICE: NOT_CONFIGURED
SECURE_MCP_TUNNEL: NOT_CONFIGURED
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURITY_ANOMALY: <YES|NO>
NEXT_ACTION: WAIT
```

- [ ] **Step 4: Stop**

Do not create Task Scheduler/startup persistence, merge PRs, begin V0.2, configure Secure MCP Tunnel or register a production workspace.

---

## Plan Self-Review Checklist

- [x] Builds on the existing Gateway Agent Bridge rather than duplicating it in PowerShell.
- [x] Requires an explicitly accepted V0.1 baseline before implementation begins.
- [x] Introduces a machine-readable control manifest and refuses arbitrary Issue-comment execution.
- [x] Validates trusted Git remote, clean checkout and ff-only synchronization.
- [x] Covers single-instance locking and dead/live PID behavior.
- [x] Covers atomic exactly-once claims, failed-start retry limit and ambiguous crash recovery.
- [x] Real Antigravity invocation is capability-detected from local CLI help and fails closed.
- [x] No permission-bypass flags or machine-wide Antigravity configuration changes are required.
- [x] Polling, backoff and active-run suspension prevent overlapping control-repo sync.
- [x] Dashboard is manual-start only; no startup persistence is introduced.
- [x] E2E tests use disposable Git repos and fake runners by default.
- [x] SYSTEM/UNRESTRICTED and Level-2 work are not automatically launched.
- [x] Logs remain local and secret redaction is tested.
- [x] Separate draft PR and AG-0004 handoff are required; no automatic merge.
- [x] No TODO/TBD placeholders remain.
