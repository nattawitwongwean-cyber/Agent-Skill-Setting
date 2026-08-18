# Machine Inventory

Sanitized safe machine environment and prerequisite audit. No credentials, tokens, or private secrets.

- **Audited Date:** 2026-08-18T09:38:00+07:00
- **Operating System:** Microsoft Windows 10 Pro (64-bit)
- **OS Version / Build:** 10.0.19045 (Build 19045)
- **PowerShell Version:** 7.6.5
- **Available Disk Space (C:):** 43.1 GB free

## Prerequisites & Tools

| Tool / Requirement | Status | Version | Notes |
|---|---|---|---|
| Git | PASS | 2.52.0.windows.1 | Working on `main` branch |
| Node.js | PASS | v24.13.0 | Meets Node 24 requirement |
| Corepack | PASS | 0.34.5 | Available for pinning |
| pnpm (global) | PASS | 10.28.2 | Global CLI present |
| pnpm (pinned) | PASS | 10.15.0 | Tested via `corepack pnpm@10.15.0 --version` |
| Codex CLI | PASS | 0.144.1 | Installed and available |
| WinGet | PASS | v1.29.280 | Windows Package Manager present |
| ripgrep (`rg`) | PASS | 15.2.0 (rev e89fff89ac) | Installed via approved `BurntSushi.ripgrep.MSVC` |
| GitHub CLI (`gh`) | PASS | 2.95.0 | Authenticated to repository |
| Outbound Network | PASS | `api.openai.com:443` (TCP: True) | Basic reachability confirmed |
