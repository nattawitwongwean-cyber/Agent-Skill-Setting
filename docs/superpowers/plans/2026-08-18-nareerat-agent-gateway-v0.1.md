# Nareerat Agent Gateway V0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a private Windows-first Nareerat Agent Gateway V0.1 that lets ChatGPT Web Pro read/query the local gateway through MCP while write/execute directives arrive through Agent Bridge and are executed primarily by native local tools, with Codex CLI and Antigravity as optional delegates.

**Architecture:** `Agent-Skill-Setting` remains the control plane. A separate private repository, `nattawitwongwean-cyber/Nareerat-Agent-Gateway`, contains product source. The execution core is transport-independent: policy, persistence, task queue, context, tool registry, native tools and delegates are shared by local stdio MCP, loopback HTTP MCP and Agent Bridge. V0.1 uses a dedicated test workspace only and stops before Secure MCP Tunnel configuration or any production LMS/LFS registration.

**Tech Stack:** Windows 10 x64, Node.js 24, pnpm 10.15.0 via Corepack, TypeScript, official MCP TypeScript SDK v2 packages (`@modelcontextprotocol/server`, `@modelcontextprotocol/node`), Zod, built-in Node `node:sqlite`, Electron, React, Vitest, ripgrep, Git, execa, chokidar.

**Spec:** `docs/superpowers/specs/2026-08-18-nareerat-agent-gateway-design.md`

## Global Constraints

- Source repository must be private: `nattawitwongwean-cyber/Nareerat-Agent-Gateway`.
- Control repository remains `nattawitwongwean-cyber/Agent-Skill-Setting`.
- Use Node.js 24 and invoke pnpm through `corepack pnpm@10.15.0`.
- Default permission profile is `DEVELOP` and is restricted to registered workspace roots.
- V0.1 development uses only an isolated generated test workspace; do not register or modify `Nattawit-LMS`, LMS/LFS production code, student data, or other production repositories.
- Do not configure OpenAI Secure MCP Tunnel during CG-0003.
- Do not enable Start with Windows, Windows Service mode, SYSTEM, or UNRESTRICTED profile during CG-0003.
- Do not disable Defender/firewall, modify partitions, export credentials, or use destructive Git reset/clean on real repositories.
- Do not commit secrets, tokens, cookies, private keys, auth/session databases, or secret-bearing `.env` values.
- Native tools are the default executor. Codex and Antigravity are optional delegates.
- Delegate output is never trusted as completion evidence; native diff/build/test/read-back verification is required.
- `No evidence -> no COMPLETED`.
- The Pro-facing remote MCP catalog must not disguise write or execute behavior as read/fetch tools.
- Every task below ends with a testable deliverable and a structured commit on branch `agent/cg-0003-v0.1`.
- Do not merge the implementation branch to `main` during CG-0003; open a draft PR and stop for ChatGPT review.

---

## Repository / File Map

Create the product repository with this shape:

```text
Nareerat-Agent-Gateway/
├── package.json
├── pnpm-workspace.yaml
├── tsconfig.base.json
├── vitest.workspace.ts
├── .gitignore
├── README.md
├── apps/
│   └── desktop/
│       ├── package.json
│       ├── src/main.ts
│       ├── src/preload.ts
│       └── src/renderer/
├── packages/
│   ├── core/
│   ├── policy/
│   ├── persistence/
│   ├── tools/
│   ├── executor/
│   ├── context/
│   ├── agent-bridge/
│   ├── mcp/
│   └── delegation/
├── tests/
│   ├── fixtures/
│   └── integration/
├── docs/
└── scripts/
```

Responsibilities:

- `packages/core`: shared IDs, states, errors, configuration types and runtime composition.
- `packages/policy`: workspace boundaries, profiles, hard blocks, approval decisions.
- `packages/persistence`: SQLite schema/repositories and recovery state using `node:sqlite`.
- `packages/tools`: Tool Registry plus native workspace/files/search/git/process/build/test packs.
- `packages/executor`: task queue, workers, locks, step runner, verification rules.
- `packages/context`: workspace index, ranking, paging, context snapshots, dedup telemetry.
- `packages/agent-bridge`: machine-readable directive reader and idempotency.
- `packages/mcp`: Pro-safe read/fetch catalog, local full catalog, stdio and loopback HTTP adapters.
- `packages/delegation`: Codex and Antigravity adapters.
- `apps/desktop`: Electron tray/dashboard shell only; renderer never directly accesses filesystem, shell or SQLite. Electron main composes the shared Gateway runtime and exposes a narrow preload API.

---

### Task 1: Create the private repository and verified TypeScript workspace

**Files:**
- Create: repository root files listed above.
- Create: `packages/core/src/version.ts`
- Test: `packages/core/src/version.test.ts`

**Interfaces:**
- Produces workspace scripts `build`, `test`, `typecheck` and package import prefix `@nareerat/*`.
- Produces `GATEWAY_VERSION = "0.1.0"`.

- [ ] **Step 1: Verify the repo does not already exist, then create it privately**

Run:

```powershell
gh repo view nattawitwongwean-cyber/Nareerat-Agent-Gateway
```

Expected before creation: repository-not-found. If it already exists, inspect it and do not overwrite it.

If absent:

```powershell
gh repo create nattawitwongwean-cyber/Nareerat-Agent-Gateway --private --description "Windows-first local MCP and native agent gateway" --clone
Set-Location .\Nareerat-Agent-Gateway
git checkout -b agent/cg-0003-v0.1
```

- [ ] **Step 2: Create workspace manifests**

Root `package.json` must contain at least:

```json
{
  "name": "nareerat-agent-gateway",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "packageManager": "pnpm@10.15.0",
  "engines": { "node": ">=24 <25" },
  "scripts": {
    "build": "tsc -b",
    "typecheck": "tsc -b --pretty false",
    "test": "vitest run",
    "test:watch": "vitest",
    "dev:desktop": "pnpm --filter @nareerat/desktop dev"
  }
}
```

`pnpm-workspace.yaml`:

```yaml
packages:
  - apps/*
  - packages/*
```

Install the baseline toolchain and runtime dependencies:

```powershell
corepack pnpm@10.15.0 add -Dw typescript vitest @types/node
corepack pnpm@10.15.0 add -w zod execa chokidar
```

- [ ] **Step 3: Write the first failing test**

`packages/core/src/version.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { GATEWAY_VERSION } from "./version.js";

describe("gateway version", () => {
  it("starts at 0.1.0", () => {
    expect(GATEWAY_VERSION).toBe("0.1.0");
  });
});
```

Run:

```powershell
corepack pnpm@10.15.0 test
```

Expected: FAIL because `version.ts` does not exist.

- [ ] **Step 4: Implement the minimal module**

`packages/core/src/version.ts`:

```ts
export const GATEWAY_VERSION = "0.1.0" as const;
```

Create project references/tsconfig files so `pnpm build` compiles all packages.

- [ ] **Step 5: Verify toolchain**

Run:

```powershell
corepack pnpm@10.15.0 test
corepack pnpm@10.15.0 typecheck
corepack pnpm@10.15.0 build
```

Expected: all exit 0.

- [ ] **Step 6: Commit**

```powershell
git add .
git diff --cached --check
git commit -m "chore: bootstrap gateway workspace"
git push -u origin agent/cg-0003-v0.1
```

---

### Task 2: Implement workspace canonicalization and permission profiles

**Files:**
- Create: `packages/core/src/types.ts`
- Create: `packages/policy/src/workspace-path.ts`
- Create: `packages/policy/src/policy-engine.ts`
- Test: `packages/policy/src/workspace-path.test.ts`
- Test: `packages/policy/src/policy-engine.test.ts`

**Interfaces:**

```ts
export type PermissionProfile = "SAFE" | "DEVELOP" | "SYSTEM" | "UNRESTRICTED";
export type RiskLevel = "READ" | "WRITE" | "EXECUTE" | "SYSTEM" | "DESTRUCTIVE";
export interface WorkspaceRecord { id: string; root: string; profile: PermissionProfile; }
export function resolveWorkspacePath(workspace: WorkspaceRecord, candidate: string): Promise<string>;
export class PolicyEngine { decide(request: PolicyRequest): Promise<PolicyDecision>; }
```

- [ ] **Step 1: Write path traversal tests**

Cover normal child paths, `..` escape, absolute outside path and a symlink/junction escape created inside a temporary workspace.

Core assertion:

```ts
await expect(resolveWorkspacePath(ws, "../outside.txt")).rejects.toThrow(/workspace boundary/i);
```

- [ ] **Step 2: Run only policy tests and confirm red state**

```powershell
corepack pnpm@10.15.0 vitest run packages/policy
```

Expected: FAIL due to missing implementations.

- [ ] **Step 3: Implement canonical path enforcement**

Implementation must resolve the workspace root and target with `realpath` when existing, normalize Windows case/separators, and reject any resolved path not equal to root or under `root + path.sep`.

- [ ] **Step 4: Write permission tests**

Required cases:

```ts
expect((await engine.decide(readInWorkspace)).state).toBe("ALLOW");
expect((await engine.decide(writeInWorkspaceDevelop)).state).toBe("ALLOW");
expect((await engine.decide(writeInWorkspaceSafe)).state).toBe("DENY");
expect((await engine.decide(systemMutationDevelop)).state).toBe("NEEDS_APPROVAL");
expect((await engine.decide(formatDisk)).state).toBe("HARD_BLOCK");
```

Hard-block command normalization must catch at least direct Windows disk-format/partition-destructive commands, Defender/firewall disable commands and unapproved shutdown/reboot requests.

- [ ] **Step 5: Implement `PolicyEngine` and verify**

Run:

```powershell
corepack pnpm@10.15.0 vitest run packages/policy
```

Expected: all policy tests pass.

- [ ] **Step 6: Commit**

```powershell
git add packages/core packages/policy
git commit -m "feat(policy): enforce workspace and profile boundaries"
git push
```

---

### Task 3: Add SQLite persistence and recovery repositories

**Files:**
- Create: `packages/persistence/src/database.ts`
- Create: `packages/persistence/src/schema.ts`
- Create: `packages/persistence/src/task-repository.ts`
- Create: `packages/persistence/src/audit-repository.ts`
- Test: `packages/persistence/src/persistence.test.ts`

**Interfaces:**

```ts
export function openGatewayDatabase(path: string): GatewayDatabase;
export class TaskRepository {
  create(input: CreateTaskInput): TaskRecord;
  get(id: string): TaskRecord | undefined;
  updateState(id: string, state: TaskState): TaskRecord;
  listRecoverable(): TaskRecord[];
}
export class AuditRepository { append(event: AuditEvent): void; recent(limit: number): AuditEvent[]; }
```

- [ ] **Step 1: Write failing persistence tests**

Use a temporary SQLite file. Verify a task survives close/reopen and `RUNNING` tasks appear in `listRecoverable()`.

- [ ] **Step 2: Run tests and verify failure**

```powershell
corepack pnpm@10.15.0 vitest run packages/persistence
```

- [ ] **Step 3: Implement database wrapper with Node built-in SQLite**

Use:

```ts
import { DatabaseSync } from "node:sqlite";
```

Open with extensions disabled. Enable foreign keys and WAL using SQL pragmas. V0.1 must not load SQLite extensions.

Create tables named exactly:

```text
workspaces
tasks
task_steps
tool_calls
processes
approvals
audit_events
delegations
context_snapshots
workspace_index_state
processed_directives
```

Store timestamps as ISO-8601 UTC strings.

- [ ] **Step 4: Implement task/audit repositories and recovery query**

`listRecoverable()` returns tasks in `PLANNING`, `RUNNING` or `VERIFYING` at startup.

- [ ] **Step 5: Verify persistence**

```powershell
corepack pnpm@10.15.0 vitest run packages/persistence
```

Expected: PASS.

- [ ] **Step 6: Commit**

```powershell
git add packages/persistence
git commit -m "feat(persistence): add durable gateway state"
git push
```

---

### Task 4: Build the Tool Registry and discovery meta-tools

**Files:**
- Create: `packages/tools/src/registry.ts`
- Create: `packages/tools/src/types.ts`
- Create: `packages/tools/src/discovery.ts`
- Test: `packages/tools/src/registry.test.ts`

**Interfaces:**

```ts
export interface ToolDefinition<I = unknown, O = unknown> {
  name: string;
  category: string;
  description: string;
  riskLevel: RiskLevel;
  minimumProfile: PermissionProfile;
  timeoutMs: number;
  parallelSafe: boolean;
  workspaceLock: boolean;
  inputSchema: z.ZodType<I>;
  handler: (input: I, ctx: ToolContext) => Promise<O>;
}
export class ToolRegistry {
  register(def: ToolDefinition): void;
  get(name: string): ToolDefinition | undefined;
  search(query: string): ToolSummary[];
  describe(name: string): ToolDescription;
  capabilities(): CapabilitySummary;
}
```

- [ ] **Step 1: Write tests for duplicate registration, search and describe**

The duplicate-name test must throw instead of silently replacing a tool.

- [ ] **Step 2: Implement the registry with deterministic category/name ordering**

- [ ] **Step 3: Implement `capabilities`, `tool_search`, `tool_describe` as normal registry-backed functions**

- [ ] **Step 4: Verify**

```powershell
corepack pnpm@10.15.0 vitest run packages/tools/src/registry.test.ts
```

- [ ] **Step 5: Commit**

```powershell
git add packages/tools
git commit -m "feat(tools): add registry and on-demand discovery"
git push
```

---

### Task 5: Implement native workspace/file/search/Git tools

**Files:**
- Create: `packages/tools/src/workspace/*`
- Create: `packages/tools/src/files/*`
- Create: `packages/tools/src/search/*`
- Create: `packages/tools/src/git/*`
- Test: `tests/integration/native-read-write.test.ts`

**Interfaces produced:**

```text
workspace_register, workspace_list, workspace_info
file_read, file_read_page, file_list, file_stat, file_write, file_patch, file_copy
search_text, search_files, search_page
git_status, git_diff, git_log, git_show, git_branch
```

- [ ] **Step 1: Create an isolated fixture workspace**

The test creates a temporary Git repo containing `src/login.ts`, `tests/login.test.ts` and a package manifest. Never point integration tests at a user project.

- [ ] **Step 2: Write failing integration tests**

Required assertions:

- read returns content and paging cursor,
- write and patch succeed under DEVELOP,
- patch outside workspace is denied,
- ripgrep search returns matching file/line,
- Git status/diff reflect a native patch.

- [ ] **Step 3: Implement file operations through the Policy Engine**

Every mutation calls `resolveWorkspacePath()` and `PolicyEngine.decide()` before opening the file.

- [ ] **Step 4: Implement search using `rg --json` through a fixed executable invocation**

Do not interpolate the user query into a shell command string. Pass argv array through `execa`.

- [ ] **Step 5: Implement Git inspection using argv arrays**

Git V0.1 tools are inspection-only in the direct native catalog. Mutating Git actions remain task/policy controlled.

- [ ] **Step 6: Verify**

```powershell
corepack pnpm@10.15.0 vitest run tests/integration/native-read-write.test.ts
```

- [ ] **Step 7: Commit**

```powershell
git add packages/tools tests/integration/native-read-write.test.ts
git commit -m "feat(native): add workspace file search and git tools"
git push
```

---

### Task 6: Implement Process Manager plus shell/build/test tools

**Files:**
- Create: `packages/executor/src/process-manager.ts`
- Create: `packages/tools/src/process/*`
- Create: `packages/tools/src/build/*`
- Create: `packages/tools/src/test/*`
- Test: `packages/executor/src/process-manager.test.ts`

**Interfaces:**

```ts
export class ProcessManager {
  start(spec: ProcessSpec): Promise<ProcessRecord>;
  status(id: string): ProcessRecord;
  logsPage(id: string, cursor?: string): LogPage;
  cancel(id: string): Promise<ProcessRecord>;
}
```

Tools: `process_start`, `process_status`, `process_logs_page`, `process_cancel`, `build_run`, `test_run`, `test_summary`.

- [ ] **Step 1: Write tests for exit code, timeout, cancellation and log paging**

Use Node fixture commands that print >200 lines and one command that sleeps beyond a short test timeout.

- [ ] **Step 2: Implement subprocess spawning with `execa`**

Use `shell: false`, explicit argv, controlled cwd and a minimized environment. Store raw logs under a gateway data directory, not the repository.

- [ ] **Step 3: Add secret redaction**

Before audit/log summaries, redact values for argument forms containing names such as `token`, `password`, `secret`, `api-key`, `authorization`.

- [ ] **Step 4: Implement build/test wrappers as task-aware process starts**

They accept explicit command + argv configured for the registered test workspace; they are not an arbitrary command-concatenation API.

- [ ] **Step 5: Verify**

```powershell
corepack pnpm@10.15.0 vitest run packages/executor/src/process-manager.test.ts
```

- [ ] **Step 6: Commit**

```powershell
git add packages/executor packages/tools/src/process packages/tools/src/build packages/tools/src/test
git commit -m "feat(process): add managed shell build and test execution"
git push
```

---

### Task 7: Implement persistent Task Executor, write locks and approval states

**Files:**
- Create: `packages/executor/src/task-executor.ts`
- Create: `packages/executor/src/workspace-lock.ts`
- Create: `packages/executor/src/worker-pool.ts`
- Test: `packages/executor/src/task-executor.test.ts`

**Interfaces:**

```ts
export class TaskExecutor {
  submit(input: SubmitTaskInput): TaskRecord;
  runNext(): Promise<void>;
  cancel(taskId: string): Promise<TaskRecord>;
  recover(): Promise<void>;
}
```

- [ ] **Step 1: Write state-machine tests**

Assert valid flow `QUEUED -> PLANNING -> RUNNING -> VERIFYING -> COMPLETED` and reject invalid transitions such as `COMPLETED -> RUNNING`.

- [ ] **Step 2: Write lock/concurrency tests**

Two write tasks for one workspace: second must reach `WAITING_FOR_WORKSPACE_LOCK`. Read-only task may run concurrently. Default worker count is 3.

- [ ] **Step 3: Write approval test**

A SYSTEM-level action under DEVELOP becomes `NEEDS_APPROVAL`; after an `APPROVED_ONCE` record, the same step resumes once and the approval is consumed.

- [ ] **Step 4: Implement queue/locks/recovery**

At startup, stale `RUNNING` tasks with no live process become `RECOVERY_REQUIRED`; never mark them complete automatically.

- [ ] **Step 5: Implement verification gate**

A write/edit step records read-back/diff evidence. Build/test steps require recorded process exit result. A delegate result alone cannot produce `COMPLETED`.

- [ ] **Step 6: Verify**

```powershell
corepack pnpm@10.15.0 vitest run packages/executor/src/task-executor.test.ts
```

- [ ] **Step 7: Commit**

```powershell
git add packages/executor
git commit -m "feat(executor): add persistent queue locks and approvals"
git push
```

---

### Task 8: Implement Workspace Index and Context Economy Engine

**Files:**
- Create: `packages/context/src/indexer.ts`
- Create: `packages/context/src/ranker.ts`
- Create: `packages/context/src/paging.ts`
- Create: `packages/context/src/snapshots.ts`
- Test: `packages/context/src/context.test.ts`

**Interfaces:**

```ts
export class ContextEngine {
  buildIndex(workspaceId: string): Promise<IndexStats>;
  forTask(request: ContextRequest): Promise<ContextPage>;
  page(contextId: string, cursor: string): Promise<ContextPage>;
  stats(contextId: string): ContextStats;
}
```

- [ ] **Step 1: Write ranking tests with fixed deterministic fixture scores**

The login-error fixture must rank exact error/symbol/path matches above unrelated files.

- [ ] **Step 2: Write paging/dedup tests**

A second overlapping context request must report positive `deduplicatedChars` and deliver less repeated content.

- [ ] **Step 3: Implement deterministic V0.1 ranking**

Use exact text/symbol, path/name, recent Git changes, simple import hints and related-test naming. Do not add remote embeddings in V0.1.

- [ ] **Step 4: Implement watcher invalidation with `chokidar`**

Changed files invalidate only affected index entries and mark older context snapshots stale.

- [ ] **Step 5: Verify**

```powershell
corepack pnpm@10.15.0 vitest run packages/context
```

- [ ] **Step 6: Commit**

```powershell
git add packages/context
git commit -m "feat(context): add indexed ranked paged context"
git push
```

---

### Task 9: Implement machine-readable Agent Bridge directive consumption

**Files in product repo:**
- Create: `packages/agent-bridge/src/directive-schema.ts`
- Create: `packages/agent-bridge/src/consumer.ts`
- Test: `packages/agent-bridge/src/consumer.test.ts`
- Create fixture: `tests/fixtures/control-repo/agent-bridge/gateway/inbox/CG-TEST-001.json`

**Machine-readable directive schema:**

```ts
export const GatewayDirectiveSchema = z.object({
  id: z.string().min(1),
  workspaceId: z.string().min(1),
  goal: z.string().min(1),
  executor: z.enum(["NATIVE", "CODEX", "ANTIGRAVITY", "HYBRID", "AUTO"]),
  requestedProfile: z.enum(["SAFE", "DEVELOP", "SYSTEM", "UNRESTRICTED"]).default("DEVELOP"),
  createdAt: z.string().datetime()
});
```

- [ ] **Step 1: Write idempotency tests**

The same directive file pulled twice creates exactly one task; `processed_directives` records its ID.

- [ ] **Step 2: Write trust-boundary tests**

Files outside configured `agent-bridge/gateway/inbox/` must not be parsed as executable directives. Issue-comment text is not executable authority.

- [ ] **Step 3: Implement consumer against a configured local control-repo checkout**

Polling may run `git pull --ff-only` only in its dedicated control checkout and then scan the approved inbox path. On Git conflict/failure, report `BLOCKED_CONTROL_SYNC`; never reset hard.

- [ ] **Step 4: Verify**

```powershell
corepack pnpm@10.15.0 vitest run packages/agent-bridge
```

- [ ] **Step 5: Commit**

```powershell
git add packages/agent-bridge tests/fixtures/control-repo
git commit -m "feat(bridge): consume idempotent gateway directives"
git push
```

---

### Task 10: Add MCP read/fetch surface and local full stdio surface

**Files:**
- Create: `packages/mcp/src/server.ts`
- Create: `packages/mcp/src/catalog.ts`
- Create: `packages/mcp/src/stdio.ts`
- Create: `packages/mcp/src/http.ts`
- Test: `packages/mcp/src/catalog.test.ts`

**Interfaces:**

```ts
export type McpCapabilityMode = "PRO_READ_BRIDGE_WRITE" | "FULL_MCP";
export function visibleTools(mode: McpCapabilityMode, registry: ToolRegistry): ToolDefinition[];
export async function serveStdio(runtime: GatewayRuntime): Promise<void>;
export async function serveLoopbackHttp(runtime: GatewayRuntime, port: number): Promise<void>;
```

- [ ] **Step 1: Install official MCP server packages**

```powershell
corepack pnpm@10.15.0 add -w @modelcontextprotocol/server @modelcontextprotocol/node
```

- [ ] **Step 2: Write catalog filtering tests**

In `PRO_READ_BRIDGE_WRITE`, assert that read/search/context/status/log/report/discovery tools are visible and `file_write`, `file_patch`, `process_start`, `build_run`, `test_run`, delegates and task mutation tools are not directly exposed.

- [ ] **Step 3: Implement MCP adapters without business logic**

MCP handlers call registry/runtime APIs; they must not duplicate filesystem/process implementation.

- [ ] **Step 4: Bind HTTP only to `127.0.0.1`**

Default MCP HTTP port `39401`; configurable override allowed. Do not bind `0.0.0.0` in V0.1.

- [ ] **Step 5: Verify local MCP catalog tests and stdio smoke test**

```powershell
corepack pnpm@10.15.0 vitest run packages/mcp
```

Then launch a local test client/inspector against stdio and confirm `capabilities`, `workspace_list`, `tool_search` work against the fixture runtime.

- [ ] **Step 6: Commit**

```powershell
git add packages/mcp package.json pnpm-lock.yaml
git commit -m "feat(mcp): expose pro-safe and local tool surfaces"
git push
```

---

### Task 11: Add optional Codex and Antigravity delegation adapters

**Files:**
- Create: `packages/delegation/src/types.ts`
- Create: `packages/delegation/src/codex.ts`
- Create: `packages/delegation/src/antigravity.ts`
- Test: `packages/delegation/src/delegation.test.ts`

**Interfaces:**

```ts
export interface DelegateResult { state: "SUCCESS" | "FAILED" | "UNAVAILABLE"; summary: string; processId?: string; }
export interface DelegateAdapter { available(): Promise<boolean>; run(input: DelegateRequest): Promise<DelegateResult>; }
```

- [ ] **Step 1: Inspect installed delegate CLIs without changing auth/config**

Run and capture sanitized outputs in the development report:

```powershell
codex --version
codex exec --help
agy --version
agy --help
```

Do not read credential files.

- [ ] **Step 2: Implement Codex adapter using non-interactive `codex exec`**

Use argv invocation, a finite timeout and `--ephemeral` where supported by the installed help output. Never add flags that are not present in the local installed CLI help. Run within the registered test workspace only.

- [ ] **Step 3: Implement Antigravity adapter as feature-detected and fail-closed**

Use the installed `agy` help output to detect a supported non-interactive print/headless mode. Do not use `--dangerously-skip-permissions`. If structured/reliable headless output cannot be verified on the installed version within a short smoke timeout, `available()` returns false and the gateway continues with native/Codex execution rather than weakening permissions.

- [ ] **Step 4: Write mocked adapter tests plus one opt-in local smoke test**

Mock tests verify timeout/error/redaction. Real smoke tests operate only in the generated fixture workspace and do not modify external files.

- [ ] **Step 5: Verify native evidence after any delegate smoke edit**

If a delegate changes the fixture, verify with native `git diff` and fixture tests; never mark success only from delegate stdout.

- [ ] **Step 6: Commit**

```powershell
git add packages/delegation
git commit -m "feat(delegation): add optional codex and antigravity adapters"
git push
```

---

### Task 12: Add Electron tray runtime and minimal dashboard

**Files:**
- Create: `apps/desktop/package.json`
- Create: `apps/desktop/src/main.ts`
- Create: `apps/desktop/src/preload.ts`
- Create: `apps/desktop/src/renderer/App.tsx`
- Create: `apps/desktop/src/renderer/pages/{Overview,Workspaces,Tasks,Processes,Tools,Approvals,Logs}.tsx`
- Test: `apps/desktop/src/renderer/App.test.tsx`

**Interfaces:**
- Electron main owns/composes the shared Gateway runtime; renderer does not import Node filesystem/process/SQLite modules.
- Closing the window hides to tray; Quit stops runtime.
- Renderer receives sanitized state through preload IPC only.

- [ ] **Step 1: Install Electron/React test dependencies**

```powershell
corepack pnpm@10.15.0 add --filter @nareerat/desktop electron react react-dom
corepack pnpm@10.15.0 add -D --filter @nareerat/desktop @types/react @types/react-dom @testing-library/react jsdom
```

- [ ] **Step 2: Write renderer smoke test**

Assert the seven required navigation labels render and Overview displays Gateway/Profile/Task summary from a mocked preload API.

- [ ] **Step 3: Implement tray lifecycle**

Menu items: Open Dashboard, Gateway Status, Start/Stop Gateway, Quit. `Start with Windows` is not implemented/enabled in CG-0003.

- [ ] **Step 4: Implement basic pages using runtime read APIs**

No renderer page is allowed to bypass preload/runtime interfaces or call shell/filesystem directly.

- [ ] **Step 5: Verify desktop unit tests and launch smoke**

```powershell
corepack pnpm@10.15.0 vitest run apps/desktop
corepack pnpm@10.15.0 build
```

Launch once interactively on Windows, confirm tray icon and dashboard open/close behavior, then quit normally.

- [ ] **Step 6: Commit**

```powershell
git add apps/desktop package.json pnpm-lock.yaml
git commit -m "feat(desktop): add tray runtime and dashboard shell"
git push
```

---

### Task 13: End-to-end V0.1 security/integration verification

**Files:**
- Create: `tests/integration/v0.1-e2e.test.ts`
- Create: `docs/V0.1-VERIFICATION.md`

- [ ] **Step 1: Build an isolated generated workspace**

The fixture must include a tiny TypeScript app with `pnpm test` and `pnpm build`. Register only this fixture under DEVELOP.

- [ ] **Step 2: Verify native task vertical slice**

Submit through the Task Executor:

1. context/search a known bug marker,
2. patch one fixture source file,
3. run fixture tests,
4. run fixture build,
5. read native Git diff,
6. create task report.

Expected: task reaches `COMPLETED` only after test/build/diff evidence exists.

- [ ] **Step 3: Verify path/security negatives**

Attempt fixture workspace escape, SAFE-profile write, SYSTEM mutation and hard-block command. Expected outcomes: boundary error, DENY, NEEDS_APPROVAL, HARD_BLOCK respectively.

- [ ] **Step 4: Verify Agent Bridge idempotency**

Process one fixture directive twice. Expected: exactly one local task and one processed-directive record.

- [ ] **Step 5: Verify restart recovery**

Persist a fake RUNNING task, restart runtime, confirm it becomes `RECOVERY_REQUIRED` if no process exists.

- [ ] **Step 6: Verify Pro-safe MCP catalog**

Assert no direct write/execute tool appears in `PRO_READ_BRIDGE_WRITE` mode.

- [ ] **Step 7: Run full verification**

```powershell
corepack pnpm@10.15.0 test
corepack pnpm@10.15.0 typecheck
corepack pnpm@10.15.0 build
git status --short
git diff main...HEAD --check
```

Record exact pass/fail counts and any disabled optional delegate capability in `docs/V0.1-VERIFICATION.md`.

- [ ] **Step 8: Commit**

```powershell
git add tests docs/V0.1-VERIFICATION.md
git commit -m "test: verify gateway v0.1 vertical slice"
git push
```

---

### Task 14: Open review PR and hand off through Agent Bridge

**Files in product repo:**
- Update: `README.md` with local developer start commands and safety defaults.

**Files in control repo:**
- Create/update Agent Bridge report for `CG-0003`.
- Do not modify the Gateway implementation from the control repo.

- [ ] **Step 1: Confirm no secrets or production workspace paths are staged**

Run:

```powershell
git status --short
git diff main...HEAD
git diff main...HEAD --check
```

Search branch content for obvious key markers without printing values. If a secret is found, stop, remove it safely before PR creation, and report `SECURITY_BLOCKED`; do not copy the secret into logs or reports.

- [ ] **Step 2: Open a draft PR; do not merge**

```powershell
gh pr create --repo nattawitwongwean-cyber/Nareerat-Agent-Gateway --base main --head agent/cg-0003-v0.1 --draft --title "feat: Nareerat Agent Gateway V0.1" --body "Implements the CG-0003 V0.1 core gateway plan. See docs/V0.1-VERIFICATION.md for evidence. No Secure MCP Tunnel or production workspace is configured."
```

- [ ] **Step 3: Report to Agent Bridge**

Handoff must include:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-0003
REPLY-TO: CG-0003
TASK-ID: NAG-V01
STATUS: NEEDS_CHATGPT_REVIEW
SOURCE_REPO: nattawitwongwean-cyber/Nareerat-Agent-Gateway
BRANCH: agent/cg-0003-v0.1
PR: <draft PR number/url>
TESTS: <exact result>
TYPECHECK: <PASS|FAIL>
BUILD: <PASS|FAIL>
NATIVE_VERTICAL_SLICE: <PASS|FAIL>
PRO_SAFE_MCP_CATALOG: <PASS|FAIL>
CODEX_DELEGATE: <AVAILABLE|UNAVAILABLE|PASS|FAIL>
ANTIGRAVITY_DELEGATE: <AVAILABLE|UNAVAILABLE|PASS|FAIL>
SECURITY_ANOMALY: <YES|NO>
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
NEXT_ACTION: WAIT
```

- [ ] **Step 4: Stop**

Do not merge the PR, register a production workspace, configure Secure MCP Tunnel, enable startup/service mode, or begin V0.2. Wait for ChatGPT/human review.

---

## Plan Self-Review Checklist

- [x] Native read/write/search/Git vertical slice is covered.
- [x] Workspace canonicalization/path escape tests precede production-like write behavior.
- [x] SAFE/DEVELOP/SYSTEM/UNRESTRICTED policy model and hard blocks are represented.
- [x] SQLite persistence, recovery, task states, locks and approvals are covered without a native SQLite npm add-on.
- [x] Process timeout/cancel/log paging and secret redaction are covered.
- [x] Context indexing/ranking/paging/dedup/snapshot staleness are covered.
- [x] Tool Registry/discovery metadata are covered.
- [x] Agent Bridge uses machine-readable authorized path plus idempotency.
- [x] Pro mode explicitly filters write/execute MCP tools rather than disguising them.
- [x] Codex and Antigravity remain optional and fail closed.
- [x] Delegate success requires native verification.
- [x] Electron renderer is isolated from Node/filesystem/process/SQLite access behind preload/runtime APIs.
- [x] Full end-to-end verification uses only generated fixture workspaces.
- [x] Secure MCP Tunnel, production LMS/LFS, Windows startup/service and unrestricted mode are explicitly out of CG-0003 scope.
- [x] Final work is delivered as a draft PR and is not auto-merged.
- [x] No TODO/TBD placeholders remain.
