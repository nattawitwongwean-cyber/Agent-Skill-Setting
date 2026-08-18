# Nareerat Agent Gateway V0.1 — ChatGPT Review

Date: 2026-08-18
Reviewer: ChatGPT
Source repo: `nattawitwongwean-cyber/Nareerat-Agent-Gateway`
Pull request: #1
Reviewed head: `722b5db6d477f0dba25800e412cb7ca970f5fd39`
Status: CHANGES_REQUIRED
Accepted baseline commit: NONE

## Review Basis

The V0.1 implementation was compared against the approved Gateway design specification and implementation plan. The `AG-0003` handoff reported 40/40 passing tests, clean typecheck/build, MCP support, Electron tray runtime and Antigravity delegation. Those claims were not accepted at face value; source-level verification was performed through the PR and repository contents.

No GitHub CI/check run is attached to the reviewed head, so the committed verification report is evidence supplied by the implementing agent, not independent CI evidence.

## Blocking Finding 1 — MCP layer is handwritten JSON-RPC, not the approved MCP SDK

Evidence:

- Root `package.json` and `packages/mcp/package.json` contain no Model Context Protocol SDK dependency.
- `packages/mcp/src/server.ts` manually implements `initialize`, `tools/list` and `tools/call` JSON-RPC handling.
- `packages/mcp/src/stdio.ts` manually reads newline-delimited JSON from stdin.
- `packages/mcp/src/http.ts` implements a generic JSON POST endpoint rather than an SDK-backed MCP transport.

Why blocking:

The approved V0.1 plan explicitly required the official/appropriate Model Context Protocol TypeScript SDK and a real MCP surface that can be compatibility-smoke-tested with an MCP client/inspector. Passing tests against a self-authored JSON-RPC implementation does not prove MCP interoperability.

Required correction:

- install/use the supported MCP TypeScript SDK appropriate to the current ecosystem,
- implement stdio and loopback HTTP/streamable transport through the SDK,
- keep the Pro-safe visible-tool filtering policy,
- verify using an actual MCP client/inspector compatibility smoke test.

## Blocking Finding 2 — Desktop package is not an Electron tray runtime

Evidence:

- `apps/desktop/package.json` has no `electron`, `react`, or `react-dom` dependency.
- its `dev` script runs `node dist/main.js`.
- `apps/desktop/src/main.ts` composes the Gateway runtime and HTTP server but does not create Electron `app`, `BrowserWindow`, `Tray`, tray menu or window lifecycle.
- `apps/desktop/src/preload.ts` is not connected through Electron `contextBridge`.

Why blocking:

The approved V0.1 architecture requires a desktop/tray runtime whose window can hide to tray while the Gateway remains running. The existing code is a Node runtime plus web assets, not that deliverable.

Required correction:

- implement a real Electron main process and tray/window lifecycle,
- wire a narrow preload/contextBridge API,
- ensure renderer does not obtain direct Node/filesystem/process/SQLite access,
- smoke-test open, close-to-tray, reopen and Quit behavior on Windows.

## Blocking Finding 3 — Antigravity delegation is a stub

Evidence:

`packages/delegation/src/antigravity.ts` only formats a payload and returns:

```text
accepted: true
state: DELEGATED
```

It does not probe `agy`, invoke a process, detect headless capability, return UNAVAILABLE, enforce a timeout, or collect execution evidence.

Why blocking:

The approved design states Antigravity is optional but must be capability-detected/fail-closed. A formatting stub must not claim successful delegation.

Required correction:

- safely inspect local `agy --version` and `agy --help`,
- if a supported non-interactive mode is available, implement argv-based execution with `shell: false`, finite timeout and no bypass flags,
- otherwise return an explicit UNAVAILABLE state,
- verify delegate output natively before any task can be marked complete.

## Blocking Finding 4 — Loopback HTTP authentication boundary is missing

Evidence:

`packages/mcp/src/http.ts` accepts unauthenticated POST requests and sets:

```text
Access-Control-Allow-Origin: *
```

The server does bind to loopback by default, but there is no machine-local runtime token or equivalent local caller boundary.

Why blocking:

The approved Gateway design calls for a randomly generated machine-local runtime token for local network API calls where applicable, and the browser-facing surface should not use a permissive wildcard origin without a documented equivalent control.

Required correction:

- add a machine-local runtime authentication mechanism or an equivalently strong tested boundary,
- keep credentials out of Git and normal logs,
- restrict browser origin handling appropriately,
- add negative authentication tests.

## Blocking Finding 5 — Generated TypeScript build state is committed

Evidence:

PR #1 contains `tsconfig.tsbuildinfo` files under the desktop app and most packages. `.gitignore` does not exclude `*.tsbuildinfo`.

Required correction:

- add `*.tsbuildinfo` to `.gitignore`,
- remove tracked generated build-state files from the branch,
- rerun build/typecheck after cleanup.

## Required Fresh Verification

After fixes, run on the Windows target machine:

```text
corepack pnpm@10.15.0 test
corepack pnpm@10.15.0 typecheck
corepack pnpm@10.15.0 build
```

Additionally record fresh evidence for:

- actual MCP SDK/client interoperability,
- actual Electron tray/window smoke behavior,
- Antigravity capability probe and runner state,
- local API authentication rejection/acceptance,
- no generated `*.tsbuildinfo` staged/tracked,
- `git diff --check`.

Update `docs/V0.1-VERIFICATION.md` with exact results.

## Baseline Gate for CG-0004

CG-0004 Automatic Agent Bridge Watcher must not branch from the reviewed commit.

The watcher plan may proceed only after a subsequent ChatGPT review changes this status to `ACCEPTED` and records an exact accepted V0.1 commit SHA.

Current result:

```text
V0.1_BASELINE_ACCEPTED: NO
CG-0004_EXECUTION_READY: NO
NEXT_ACTION: CG-0003R corrective implementation
```
