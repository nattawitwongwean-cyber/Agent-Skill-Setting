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

## CG-0003 Actions Not Approved

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
