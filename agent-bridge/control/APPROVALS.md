# Approvals Ledger

## Historical / Existing Level-1 Authorizations
- Machine prerequisite audit: APPROVED
- Ripgrep package (`BurntSushi.ripgrep.MSVC`) installation if missing: APPROVED
- Agent Bridge file creation and maintenance: APPROVED
- Git commit and push for sanitized Agent Bridge paths: APPROVED
- GitHub Issue #1 Control Room handoff posting: APPROVED

## CG-0003 — Nareerat Agent Gateway V0.1 Level-1 Authorizations

The human approved the Nareerat Agent Gateway architecture and written design specification before this directive.

The following actions are approved for `CG-0003` / `NAG-V01`:

- Create private repo `nattawitwongwean-cyber/Nareerat-Agent-Gateway` if it does not already exist.
- Create/push a minimal baseline `main` commit and implementation branch `agent/cg-0003-v0.1`.
- Create and edit Gateway source, tests, docs, configs and fixture files inside that source repo.
- Create disposable/generated test workspaces for integration tests.
- Install project-local dependencies explicitly required by the approved implementation plan using `corepack pnpm@10.15.0`.
- Run non-elevated Node, TypeScript, Vitest, Git, ripgrep and project build/test/typecheck commands inside the Gateway repo or disposable fixtures.
- Launch the new Electron desktop runtime interactively for a local smoke test and exit normally.
- Inspect installed delegate versions/help (`codex`, `agy`) without reading credential stores or changing authentication/configuration.
- Run optional Codex/Antigravity delegate smoke tests only in disposable fixture workspaces, subject to policy and fail-closed behavior.
- Create/push normal Git commits to the implementation branch.
- Open a draft PR to `main` after verification.
- Report results through Agent Bridge and Issue #1.

## CG-0003R — V0.1 Review Corrections

`CG-0003R` / `NAG-V01-R1` is a corrective continuation of the already approved V0.1 scope, not a new product phase.

The existing CG-0003 Level-1 authorizations apply to these review corrections, including:

- replacing the handwritten MCP layer with the supported MCP TypeScript SDK,
- installing project-local MCP SDK packages required for that correction,
- installing project-local Electron/React dependencies already required by the approved V0.1 plan,
- implementing the approved Electron tray/window/preload behavior,
- capability-detecting and safely invoking the installed `agy` CLI in disposable fixture workspaces when supported,
- adding a machine-local runtime authentication boundary for loopback API access without committing secrets,
- removing generated `*.tsbuildinfo` artifacts from Git tracking,
- rerunning non-elevated tests, typecheck, build and approved local smoke tests,
- pushing corrections to `agent/cg-0003-v0.1` and updating draft PR #1.

No new Level-2 permission is granted by CG-0003R.

## CG-0003 / CG-0003R Actions Not Approved

- Production LMS/LFS/student workspace access or mutation: NOT APPROVED
- Registering `Nattawit-LMS` or any production repo for DEVELOP writes: NOT APPROVED
- OpenAI Secure MCP Tunnel creation/configuration: NOT APPROVED
- OpenAI tunnel/API credential entry or capture: NOT APPROVED
- Start with Windows / startup persistence: NOT APPROVED
- Windows Service creation: NOT APPROVED
- SYSTEM profile execution: NOT APPROVED
- UNRESTRICTED profile execution: NOT APPROVED
- Elevated / Administrator execution: NOT APPROVED
- Registry / Windows service / Scheduled Task / firewall mutation: NOT APPROVED
- Defender disabling/exclusion changes: NOT APPROVED
- Force push: NOT APPROVED
- Merge of the V0.1 draft PR: NOT APPROVED
- Antigravity permission-bypass flags such as `--dangerously-skip-permissions`: NOT APPROVED

## Standing Hard Blocks

- Disk format or partition mutation.
- Credential/password/cookie/private-key export.
- Secret-bearing `.env` content committed or copied into reports.
- Public remote-control exposure outside an approved secure transport.
- Destructive Git reset/clean on real repositories.
- Unapproved shutdown/reboot.
