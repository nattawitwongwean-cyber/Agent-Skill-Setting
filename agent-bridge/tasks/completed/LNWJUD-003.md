# Task: LNWJUD-003 — Safe Machine Prerequisite Audit

- **Task ID:** LNWJUD-003
- **Status:** COMPLETED
- **Started:** 2026-08-18T09:38:00+07:00
- **Completed:** 2026-08-18T09:39:10+07:00

## Objective
Re-measure the Windows host environment, verify versions of Git, Node, Corepack, pnpm, Codex CLI, and ripgrep, verify pinned pnpm availability, test safe outbound connectivity to `api.openai.com:443`, and install ripgrep via the approved WinGet package if absent.

## Verification Evidence
- Windows 10 Pro x64 (Build 19045), Disk C: 43.1 GB free
- PowerShell 7.6.5, Git 2.52.0, Node v24.13.0, Corepack 0.34.5, Codex CLI 0.144.1
- Pinned pnpm test: `corepack pnpm@10.15.0 --version` -> `10.15.0`
- Network reachability: `api.openai.com:443` -> `TcpTestSucceeded: True`
- ripgrep (`rg`): Initially absent. Inspected `BurntSushi.ripgrep.MSVC` on winget, installed via pre-approved winget command, verified `rg --version` -> `ripgrep 15.2.0 (rev e89fff89ac)`.
