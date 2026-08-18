# lnwjud Distribution Provenance Report

- **Investigation Date:** 2026-08-18T09:40:00+07:00
- **Auditor:** Antigravity (Local Windows Agent)
- **Provenance State:** `PARTIALLY_VERIFIED`

---

## 1. Summary Assessment

Authoritative documentation exists in a public repository (`engasnm111/lnwjud-readme`), authored by `engasnm111`. However, the claimed distribution repository (`https://github.com/engasnm111/lnwjud`), release tags, installer binaries (`lnwjud-Setup-3.0.0.exe`), and published cryptographic checksums are currently **inaccessible or unpublished** on GitHub.

In accordance with Agent Bridge security rules, no unverified binary was downloaded from unofficial or third-party mirrors.

---

## 2. Investigation Details

### Authoritative Documentation Source
- **Repository Owner:** `engasnm111`
- **Repository Name:** `lnwjud-readme`
- **Repository Visibility:** Public
- **URL:** `https://github.com/engasnm111/lnwjud-readme`
- **Last Updated:** 2026-08-17T17:55:40Z
- **Repository Contents:**
  - `README.md` (50,591 bytes) — Detailed architecture, security bounds, and setup guide.
  - `Screenshot/` — UI captures of Lnwjud desktop and live log hub.
  - `logo-256x256.png` (68,801 bytes) — Brand asset.
- **Releases on `engasnm111/lnwjud-readme`:** None (`[]`).

### Target Source & Binary Repository Check
- **Claimed Source URL:** `https://github.com/engasnm111/lnwjud.git`
- **Claimed Release URL:** `https://github.com/engasnm111/lnwjud/releases/latest`
- **Claimed Asset Filename:** `lnwjud-Setup-3.0.0.exe`
- **GitHub API Verification Result:**
  ```text
  GraphQL: Could not resolve to a Repository with the name 'engasnm111/lnwjud'.
  ```
- **Finding:** The repository `engasnm111/lnwjud` does not resolve publicly (it may be private, uncreated, or restricted).

### Cryptographic & Signature Information
- **Published SHA-256 Checksum:** NOT_AVAILABLE (no release page or checksum file published).
- **Authenticode Signer Identity:** NOT_AVAILABLE (no binary asset available).
- **License Claim:** MIT License (stated in README, but formal `LICENSE` file is inside unresolved source repo).

---

## 3. Discrepancy Matrix

| Item | Claim in README | Observed Reality on GitHub | Impact |
|---|---|---|---|
| Source Code Repo | `github.com/engasnm111/lnwjud` | Repository does not resolve (404/Private) | Cannot build from source |
| Releases | `github.com/engasnm111/lnwjud/releases` | Release surface does not exist | Cannot download pre-built installer |
| Checksums | Expected on Release page | Not published | Cannot cryptographically verify ahead of time |
| Readme Repo | `github.com/engasnm111/lnwjud-readme` | Exists and is public | Architectural specification verified |

---

## 4. Final Provenance State

```text
PROVENANCE_STATE: PARTIALLY_VERIFIED
REASON: Documentation repository confirmed under engasnm111, but binary release and source repository are inaccessible.
ACTION: Stopped before installer download/inspection. No unverified third-party mirrors used.
```
