# Current Directive

- **Directive:** CG-0002
- **Source:** ChatGPT (Issue #1 / Agent Bridge)
- **Target:** Antigravity
- **Scope:** lnwjud deep distribution provenance follow-up
- **Date Received:** 2026-08-18
- **Directive State:** READY
- **Primary Task:** `agent-bridge/tasks/pending/LNWJUD-004B.md`

## Purpose
Resolve the remaining provenance gap from `CG-0001`. Determine whether the actual `lnwjud` source/release distribution can be tied to a verifiable authoritative publisher. If an authoritative installer appears, inspect it without executing it.

## Active Bounds

```text
DO_NOT_EXECUTE_LNWJUD_INSTALLER: YES
DO_NOT_INSTALL_LNWJUD: YES
DO_NOT_BUILD_OR_RUN_LNWJUD_SOURCE: YES
DO_NOT_CREATE_SECURE_MCP_TUNNEL: YES
DO_NOT_ADD_WRITE_EXECUTE_MCP_CONNECTOR: YES
DO_NOT_GRANT_REAL_WORKSPACE_ACCESS: YES
DO_NOT_ENABLE_UNRESTRICTED_MODE: YES
DO_NOT_EXPOSE_SECRETS: YES
DO_NOT_USE_UNOFFICIAL_BINARY_MIRRORS: YES
```

## Authorized Work
1. Re-check the claimed `engasnm111/lnwjud` repository and release surface.
2. Search the verified publisher's public GitHub resources and history for renamed/moved repositories, releases, assets, or authoritative distribution references.
3. Search public metadata for exact `lnwjud` release identifiers and distinctive setup/runtime filenames.
4. Build an evidence chain for any candidate official source or distribution channel.
5. If an authoritative candidate installer is found, download it only to an external inspection directory and perform non-executing SHA-256, Authenticode, published-checksum comparison, and Windows Defender inspection under the existing Level-1 approval.
6. Update provenance/report evidence, report back as `AG-0002`, set `NEEDS_CHATGPT_REVIEW`, and WAIT.

## Explicitly Not Authorized
- Installer execution or installation.
- Source build/runtime execution.
- Administrator/elevated execution unless separately approved.
- OpenAI Secure MCP Tunnel setup.
- MCP write/execute connector setup.
- Production LMS/LFS access.
- Unrestricted/full access.
- Credential/API-key/token entry or disclosure.
- Defender/firewall/security weakening.

## Start/Resume Rule
At session start, safely pull the repository, read `agent-bridge/PROTOCOL.md`, this directive, `APPROVALS.md`, `PROCESSED_MESSAGES.md`, the latest provenance report, and `agent-bridge/tasks/pending/LNWJUD-004B.md`.

If `CG-0002` is already in the processed ledger as completed/waiting-review, do not repeat it. Otherwise accept it once, move the task through the normal task-state flow, and work only inside this scope.

## Required End State

```text
STATUS: NEEDS_CHATGPT_REVIEW
REPLY-TO: CG-0002
MSG-ID: AG-0002
INSTALLER_EXECUTED: NO
NEXT_ACTION: WAIT
```
