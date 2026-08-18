# lnwjud Distribution Provenance Report

- **Investigation Date:** 2026-08-18 (Updated via Directive `CG-0002` / Task `LNWJUD-004B`)
- **Auditor:** Antigravity (Local Windows Agent)
- **Provenance State:** `PARTIALLY_VERIFIED`

---

## 1. Summary Assessment

Deep follow-up investigation confirmed that author `engasnm111` (Adisorn) created the public documentation repository `https://github.com/engasnm111/lnwjud-readme`. However, exhaustive enumeration across GitHub (repos, gists, forks, code search, commit search), WinGet, npm, and public metadata confirms that the distribution repository (`https://github.com/engasnm111/lnwjud`), release tags, installer binaries (`lnwjud-Setup-3.0.0.exe`), and cryptographic checksums remain **unreleased / not publicly accessible**.

In strict accordance with security bounds, no unofficial mirrors or unverified third-party binaries were downloaded or executed.

---

## 2. Deep Investigation Evidence Chain

### A. Author Account & Repository Inventory (`engasnm111`)
- **GitHub User:** `engasnm111` (User ID: 58149374)
- **Public Repositories:**
  1. `engasnm111/lnwjud-readme` (Public, created 2026-08-17T05:50:35Z) — Documentation, logo, screenshots.
  2. `engasnm111/lnwdeck` (Public, created 2026-08-15) — AI quota/token tracker for Windows.
  3. `engasnm111/resume` (Public, created 2026-07-15) — Personal CV.
- **Gists:** None (`[]`).
- **Target Repo `engasnm111/lnwjud`:** Re-tested; GitHub API returned `GraphQL: Could not resolve to a Repository with the name 'engasnm111/lnwjud'`.

### B. Documentation Repository Git History & Commits
- **Commits in `engasnm111/lnwjud-readme`:**
  - `9e9e52a` (2026-08-17T05:51:17Z, ABCz): `Readme 555` — Initial full README text.
  - `00ce9ee` (2026-08-17T05:51:53Z, ABCz): `Logooo` — Logo addition.
  - `8e96215` (2026-08-17T05:52:15Z, ABCz): `Update README.md` — Logo path update.
  - `e796417` (2026-08-17T06:08:23Z, Adisorn): `Add(): Screennnnnnnnnnzzzz` — Added screenshots.
  - `ca49d09` (2026-08-17T06:12:40Z, Adisorn): `Update(): Rename` — Renamed screenshot files.
- **Observations:** No binary releases, commit patches containing source packages, or alternate download mirrors exist in the repository history.

### C. Forks Analysis
- **Forks:**
  - `pithiwat/lnwjud-readme` (Created 2026-08-17T10:16:20Z) — No releases.
  - `manorann/lnwjud-readme` (Created 2026-08-17T08:03:11Z) — No releases.

### D. Global Code & Metadata Search
- Searched GitHub code globally for distinctive lnwjud identifiers:
  - `lnwjud-mcp-stdio.cmd` -> Matches only `engasnm111/lnwjud-readme`
  - `start-lnwjud-tunnel.ps1` -> Matches only `engasnm111/lnwjud-readme`
  - `LNWJUD_DATA_PATH` -> Matches only `engasnm111/lnwjud-readme`
  - `LNWJUD_UNRESTRICTED` -> Matches only `engasnm111/lnwjud-readme`
- Searched package registries:
  - WinGet: No package matching `lnwjud`.
  - npm: No package matching `lnwjud`.

### E. Installer Asset Status
- **Claimed Asset:** `lnwjud-Setup-3.0.0.exe`
- **Current Availability:** NOT_AVAILABLE on authoritative GitHub release channel.
- **Published SHA-256:** NOT_AVAILABLE.
- **Authenticode Signer:** NOT_AVAILABLE.
- **Downloaded File:** NONE (0 bytes).
- **Execution Status:** NOT_EXECUTED.

---

## 3. Discrepancy Matrix

| Entity / Asset | Documentation Claim | Observed Evidence | Verdict |
|---|---|---|---|
| Author Identity | Adisorn (`engasnm111`) | Confirmed via GitHub account & commit metadata | VERIFIED |
| Architecture / Spec | Detailed MCP gateway spec | Confirmed in `engasnm111/lnwjud-readme` | VERIFIED |
| Source Repository | `github.com/engasnm111/lnwjud` | Unresolved / Private / 404 on GitHub | UNRESOLVED |
| Release Binary | `lnwjud-Setup-3.0.0.exe` | No public release asset published | UNAVAILABLE |
| Cryptographic Checksum | Expected on Release | None published | UNAVAILABLE |

---

## 4. Final Provenance State

```text
PROVENANCE_STATE: PARTIALLY_VERIFIED
REASON: Publisher identity and architectural specification are confirmed under engasnm111, but the underlying source code repository and compiled binary release remain unreleased/inaccessible on GitHub.
ACTION: Stopped before installer acquisition/execution. No unverified third-party mirrors used.
```
