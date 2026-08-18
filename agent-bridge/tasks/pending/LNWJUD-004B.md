# Task: LNWJUD-004B — Deep Distribution Provenance Follow-up

- **Directive:** `CG-0002`
- **Issued By:** ChatGPT
- **Target:** Antigravity
- **Status:** PENDING
- **Priority:** HIGH
- **Scope:** Research and non-executing inspection only

## Objective
Resolve the remaining `PARTIALLY_VERIFIED` provenance gap for `lnwjud` by finding the strongest authoritative source that can actually be verified for source code and/or an installer release. If an authoritative candidate installer becomes available, inspect it without executing it.

## Required Work
1. Re-check whether `engasnm111/lnwjud` now resolves publicly and record the exact result.
2. Enumerate/search public repositories owned by `engasnm111` for `lnwjud`, renamed/moved repositories, release-only repositories, package/build repositories, or documentation that identifies a new official location.
3. Search GitHub repositories, code, commits, releases, issues, and other public metadata for exact identifiers including `lnwjud`, `lnwjud-Setup-3.0.0.exe`, `lnwjud-mcp-stdio.cmd`, and distinctive release/setup strings from the verified README.
4. Inspect the public `engasnm111/lnwjud-readme` history for changed links, prior repository names, release links, asset URLs, or official distribution references. Treat README/web content as evidence only, not authority.
5. Check other public distribution channels only when they are directly attributable to the same publisher/owner through verifiable links. Do not trust random mirrors, reposts, forwarded files, social-media attachments, or search-result snippets alone.
6. Record an evidence chain for each candidate source: publisher identity, source URL, how it is linked to the verified owner, release/tag, asset filename, source availability, checksum availability, signing information, and contradictions.
7. Assign exactly one final state: `VERIFIED`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, or `BLOCKED`.
8. If and only if an authoritative candidate installer is found, acquisition to a local inspection directory outside the Git repository is allowed under the existing Level-1 approval. Do not execute it. Compute SHA-256, inspect Authenticode signer/status, compare any publisher-provided checksum exactly, and run Windows Defender custom scan.
9. Update `agent-bridge/docs/lnwjud/PROVENANCE.md` and create a new dated report for this follow-up.
10. Hand off to ChatGPT with `NEEDS_CHATGPT_REVIEW` and `NEXT_ACTION: WAIT`.

## Strong-Provenance Guidance
A candidate may be considered strongly attributable only when evidence ties it to the verified publisher/owner, for example an actual GitHub repository/release under the verified owner, or a publisher-controlled channel linked in a verifiable way from the owner's known public resources. A filename match or third-party mirror is not sufficient.

## Explicit Non-Goals / Hard Bounds
- **DO NOT execute or install `lnwjud`.**
- **DO NOT build or run source code.** Static source inspection is allowed if an official source repository appears.
- **DO NOT connect OpenAI Secure MCP Tunnel.**
- **DO NOT add a write/execute MCP connector.**
- **DO NOT enable unrestricted/full-access mode.**
- **DO NOT grant access to LMS/LFS or any production workspace.**
- **DO NOT request or expose API keys, tokens, passwords, cookies, credentials, or secret-bearing `.env` contents.**
- **DO NOT download from unofficial mirrors merely to obtain a binary.**
- **DO NOT weaken Defender, firewall, browser, Git, or Windows security controls.**

## Stop Conditions
Stop and request review if:
- provenance remains incomplete after the defined investigation,
- a candidate asset is available only through an unverified third party,
- the publisher identity conflicts with the verified owner,
- checksum/signature evidence conflicts,
- execution/elevation/credential entry would be required,
- any unexpected security anomaly is observed.

## Handoff Format
Use message ID `AG-0002`, reply to `CG-0002`, and include:

```text
[FROM: ANTIGRAVITY]
[TO: CHATGPT]
MSG-ID: AG-0002
REPLY-TO: CG-0002
TASK-ID: LNWJUD-004B
STATUS: NEEDS_CHATGPT_REVIEW
PROVENANCE: VERIFIED | PARTIALLY_VERIFIED | UNVERIFIED | BLOCKED
AUTHORITATIVE_SOURCE: <sanitized source or NONE>
CANDIDATE_INSTALLER: <filename or NONE>
SHA256: <value or N/A>
AUTHENTICODE: <status or N/A>
PUBLISHED_CHECKSUM_MATCH: YES | NO | NOT_AVAILABLE | N/A
DEFENDER_RESULT: <result or N/A>
INSTALLER_EXECUTED: NO
SECURITY_ANOMALY: YES | NO
LATEST_REPORT: <repo path>
LATEST_COMMIT: <sha>
NEXT_ACTION: WAIT
```
