# Task: NAG-V01-R2 — Final V0.1 Baseline Corrections + Official Antigravity CLI Enablement

- **Directive:** `CG-0003R2`
- **Issued By:** ChatGPT after source review of AG-0003R
- **Target:** Antigravity
- **Status:** PENDING
- **Priority:** HIGH
- **Source Repo:** `nattawitwongwean-cyber/Nareerat-Agent-Gateway`
- **Source Branch:** `agent/cg-0003-v0.1`
- **Draft PR:** `#1`
- **Review Reference:** Agent-Skill-Setting Issue `#3`

## Objective

Resolve the final two V0.1 baseline blockers found by ChatGPT source review, then install/enable the official Google Antigravity CLI (`agy`) on the Windows machine under the newly granted user-scope authorization so the future Automatic Agent Bridge Watcher can actually launch Antigravity.

Do not start CG-0004. This task only produces an accepted-candidate V0.1 source commit and verified `agy` capability evidence for ChatGPT review.

## Blocking Correction A — Electron ESM Runtime / Real Tray Smoke

Current source uses ESM (`type: module`, `module: NodeNext`) but `apps/desktop/src/main.ts` still uses `__dirname`, and renderer loading currently depends on source assets without a verified build/copy path.

Required outcome:

1. Make Electron paths ESM-safe using `import.meta.url` + `fileURLToPath()`/`path.dirname()` or an equivalent proven approach.
2. Ensure the renderer assets actually exist in the built/runtime location used by `BrowserWindow.loadFile()`.
3. Ensure the renderer loads JavaScript that Electron can execute after build; do not point packaged/runtime HTML at an uncompiled `.ts` source file unless a verified runtime transpilation pipeline exists.
4. Add a deterministic build/copy step for renderer HTML/CSS/JS assets if needed.
5. Run a real Electron smoke test on Windows that launches the Electron process non-elevated, reaches `app.whenReady()`, creates the tray/window, verifies the dashboard file loads, then exits normally.
6. Capture concise evidence without screenshots containing secrets.

The existing Node/Vitest core test alone is not sufficient evidence for `ELECTRON_TRAY_SMOKE: PASS`.

## Blocking Correction B — Capability-Detected Antigravity Invocation

Current adapter detects any of `--headless`, `-p`, or `--prompt` but always executes `--headless`. Replace this with an explicit detected invocation strategy.

Required behavior:

- Inspect the installed CLI's actual `--help` output at runtime.
- Select only flags that are present in that exact installed help output.
- Prefer the documented one-shot/non-interactive print mode when available (for example `-p`/`--print` or the exact equivalent shown by installed help).
- Use `--cwd` only if the installed CLI help confirms it.
- Use `--output-format json` or `stream-json` only if supported by the installed CLI help.
- Never use permission-bypass flags.
- Invoke with argv + `shell: false`.
- If no safe non-interactive mode exists, return `UNAVAILABLE` and do not fake success.
- Add tests proving the adapter chooses the detected strategy rather than a hard-coded flag.

## Newly Approved Level-2 Action — Official Google Antigravity CLI (`agy`) Installation / Enablement

The human explicitly approved installing/enabling the Antigravity CLI on this Windows machine.

Authorized actions:

1. Check whether an official `agy` executable already exists in the installed Antigravity user installation but is simply absent from PATH.
2. Consult the current official Google Antigravity documentation/source only to identify the supported Windows CLI installation or enablement method.
3. If a separate installer/package is required, acquire it only from an official Google/Antigravity source documented by Google.
4. Record source URL/domain, file metadata, SHA-256, Authenticode signer/status when applicable, and run a Windows Defender custom scan before executing any downloaded installer.
5. Execute the verified official Antigravity CLI installer/package **only if it can be installed non-elevated/user-scope**.
6. If `agy` already exists locally, prefer enabling that official binary instead of downloading a duplicate.
7. A persistent **user-level PATH** update for the official `agy` directory is approved if required. Verify by opening a fresh non-elevated shell and running `agy --version` and `agy --help`.
8. If installation/enablement requires Administrator privileges, machine-wide PATH, service creation, firewall changes, security weakening, or credentials copied into scripts/logs: STOP and report `NEEDS_HUMAN_PRESENCE` or `NEEDS_APPROVAL` as appropriate.
9. If first-run authentication is required, prepare the CLI and ask the human to complete browser/login interaction directly. Do not capture or commit credentials/tokens.

## Safety Bounds

```text
DO_NOT_TOUCH_PRODUCTION_LMS_LFS: YES
DO_NOT_REGISTER_PRODUCTION_WORKSPACE: YES
DO_NOT_CONFIGURE_SECURE_MCP_TUNNEL: YES
DO_NOT_CREATE_OPENAI_TUNNEL_OR_KEYS: YES
DO_NOT_ENABLE_START_WITH_WINDOWS: YES
DO_NOT_CREATE_WINDOWS_SERVICE: YES
DO_NOT_CREATE_SCHEDULED_TASK: YES
DO_NOT_USE_SYSTEM_PROFILE: YES
DO_NOT_USE_UNRESTRICTED_PROFILE: YES
DO_NOT_RUN_AS_ADMINISTRATOR: YES
DO_NOT_MODIFY_MACHINE_WIDE_PATH: YES
USER_SCOPE_PATH_FOR_OFFICIAL_AGY: APPROVED
DO_NOT_MODIFY_REGISTRY_SERVICE_FIREWALL: YES
DO_NOT_DISABLE_DEFENDER: YES
DO_NOT_FORCE_PUSH: YES
DO_NOT_MERGE_DRAFT_PR: YES
DO_NOT_USE_PERMISSION_BYPASS_FLAGS: YES
DO_NOT_EXPOSE_SECRETS: YES
DO_NOT_START_CG_0004: YES
```

## Required Verification

After the fixes/install attempt, run fresh evidence on the updated source branch:

```powershell
corepack pnpm@10.15.0 test
corepack pnpm@10.15.0 typecheck
corepack pnpm@10.15.0 build
git diff --check
```

Also verify:

```text
ELECTRON_ESM_PATHS: PASS|FAIL
ELECTRON_RENDERER_ASSETS: PASS|FAIL
ELECTRON_REAL_TRAY_SMOKE: PASS|FAIL|NEEDS_HUMAN_PRESENCE
AGY_OFFICIAL_SOURCE_VERIFIED: PASS|FAIL|NOT_NEEDED
AGY_INSTALL_OR_ENABLE: PASS|FAIL|NEEDS_HUMAN_PRESENCE
AGY_VERSION: <sanitized version or UNAVAILABLE>
AGY_NONINTERACTIVE_MODE: <detected exact safe flag/mode or UNAVAILABLE>
ANTIGRAVITY_ADAPTER_STRATEGY_TEST: PASS|FAIL
MCP_SDK_COMPATIBILITY: PASS|FAIL
LOCAL_API_AUTH: PASS|FAIL
TSBUILDINFO_TRACKED: YES|NO
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
```

For any downloaded executable/package, include only sanitized security metadata (source, SHA-256, signature/Defender result); never commit the binary to Agent-Skill-Setting.

## Git Rules

- Work on existing `agent/cg-0003-v0.1` and draft PR #1.
- Inspect status before changes.
- Stage only intended source/test/config/docs paths.
- Do not force push.
- Do not merge PR #1.
- Commit corrections with a structured message and push normally.

## Required Handoff

When complete or blocked, report:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-0003R2
REPLY-TO: CG-0003R2
TASK-ID: NAG-V01-R2
STATUS: NEEDS_CHATGPT_REVIEW | NEEDS_HUMAN_PRESENCE | BLOCKED
PR: #1
LATEST_SOURCE_COMMIT: <sha>
TESTS: <exact result>
TYPECHECK: PASS|FAIL|NOT_RUN
BUILD: PASS|FAIL|NOT_RUN
ELECTRON_ESM_PATHS: PASS|FAIL|NOT_RUN
ELECTRON_RENDERER_ASSETS: PASS|FAIL|NOT_RUN
ELECTRON_REAL_TRAY_SMOKE: PASS|FAIL|NOT_RUN
AGY_OFFICIAL_SOURCE_VERIFIED: PASS|FAIL|NOT_NEEDED
AGY_INSTALL_OR_ENABLE: PASS|FAIL|NEEDS_HUMAN_PRESENCE|NOT_RUN
AGY_VERSION: <version|UNAVAILABLE>
AGY_NONINTERACTIVE_MODE: <mode|UNAVAILABLE>
ANTIGRAVITY_ADAPTER_STRATEGY_TEST: PASS|FAIL|NOT_RUN
MCP_SDK_COMPATIBILITY: PASS|FAIL|NOT_RUN
LOCAL_API_AUTH: PASS|FAIL|NOT_RUN
TSBUILDINFO_TRACKED: YES|NO
SECURITY_ANOMALY: YES|NO
PRODUCTION_WORKSPACE_TOUCHED: NO
SECURE_MCP_TUNNEL_CONFIGURED: NO
NEXT_ACTION: WAIT
```

Then WAIT. Do not start CG-0004 until ChatGPT explicitly marks an exact Gateway V0.1 commit `ACCEPTED`.
