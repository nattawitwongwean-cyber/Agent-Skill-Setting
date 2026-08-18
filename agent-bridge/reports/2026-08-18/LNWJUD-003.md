# Task Report: LNWJUD-003

**Task ID:** LNWJUD-003
**Status:** COMPLETED
**Date:** 2026-08-18

## Objective
Audit the Windows host machine for all required development and runtime prerequisites, verify non-destructive connectivity, check pinned pnpm compatibility, and install ripgrep (`rg`) using the approved package identity if missing.

## Starting State
- Windows 10 Pro x64 (Build 19045), C: ~43.1 GB free
- `rg` command missing in initial environment check.

## Actions Performed
1. Queried Windows OS details and drive C: free space via CIM `Win32_OperatingSystem`.
2. Checked versions of `winget`, `git`, `node`, `corepack`, `pnpm`, `codex`, `rg`, and `gh`.
3. Verified pinned pnpm version 10.15.0 via `corepack pnpm@10.15.0 --version`.
4. Executed TCP test connection to `api.openai.com:443`.
5. Inspected `BurntSushi.ripgrep.MSVC` via `winget show`.
6. Installed ripgrep using `winget install --id BurntSushi.ripgrep.MSVC -e --source winget --accept-source-agreements --accept-package-agreements`.
7. Refreshed PATH in process and verified `rg --version`.
8. Recorded machine facts in `agent-bridge/state/MACHINE.md` and state-changing installation in `agent-bridge/journal/2026-08-18.md`.

## Commands Executed
```powershell
Get-CimInstance Win32_OperatingSystem
corepack pnpm@10.15.0 --version
Test-NetConnection api.openai.com -Port 443 | Select-Object ComputerName,RemotePort,TcpTestSucceeded
winget show --id BurntSushi.ripgrep.MSVC -e --source winget
winget install --id BurntSushi.ripgrep.MSVC -e --source winget --accept-source-agreements --accept-package-agreements
rg --version
where.exe rg
```

## Files Changed
- `agent-bridge/state/MACHINE.md`
- `agent-bridge/journal/2026-08-18.md`
- `agent-bridge/tasks/completed/LNWJUD-003.md`
- `agent-bridge/reports/2026-08-18/LNWJUD-003.md`

## Verification
- OS: Windows 10 Pro 64-bit Build 19045 (Pass)
- C: Drive Free: 43.1 GB (Pass)
- Git: 2.52.0 (Pass)
- Node.js: v24.13.0 (Pass)
- Corepack: 0.34.5 (Pass)
- Pinned pnpm (10.15.0): Verified (Pass)
- Codex CLI: 0.144.1 (Pass)
- ripgrep: 15.2.0 installed at `C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\rg.exe` (Pass)
- Network connectivity `api.openai.com:443`: True (Pass)

## Evidence
- `corepack pnpm@10.15.0 --version` -> `10.15.0`
- `rg --version` -> `ripgrep 15.2.0 (rev e89fff89ac)`
- `Test-NetConnection` -> `TcpTestSucceeded: True`

## Errors
None.

## Security Observations
- No credentials or sensitive tokens accessed.
- Outbound check was strictly TCP connectivity; no OpenAI tunnel setup or credential use was performed.
- ripgrep installed under standard user AppData directory via official WinGet source without requiring unapproved elevation.

## Rollback
To uninstall ripgrep: `winget uninstall --id BurntSushi.ripgrep.MSVC`.

## Final Result
All machine prerequisites verified and satisfied. Environment ready for lnwjud provenance investigation.

## Recommended Next Step
Proceed to `LNWJUD-004`: Investigate authoritative distribution source and provenance for lnwjud.
