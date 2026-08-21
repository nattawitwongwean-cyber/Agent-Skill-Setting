# Hermes Reliability Pack Transfer Handoff

Transfer ID: `HERMES-HRP-0001`

## Intent

Move every development input required for the approved Hermes Reliability Pack to a Hermes-owned **development** workspace. This is a copy/sync operation only. It must not remove the authoritative Mac source and must not turn the protected production release directory into a development checkout.

## What Hermes Can Pull Immediately

Pull `main` from `nattawitwongwean-cyber/Agent-Skill-Setting` and read:

- `docs/superpowers/specs/2026-08-21-hermes-reliability-pack-design.md`
- `agent-bridge/reports/2026-08-20/HERMES-FOG-P01T6-P02T1.md`
- `agent-bridge/control/CURRENT_DIRECTIVE.md`
- `agent-bridge/control/APPROVALS.md`
- `agent-bridge/state/STATUS.md`
- `agent-bridge/state/PROCESSED_MESSAGES.md`
- `agent-bridge/tasks/pending/HERMES-CHATGPT-APP-0001.md`
- this transfer directory
- `agent-bridge/tasks/pending/HERMES-HRP-TRANSFER-0001.md`

The machine-readable manifest is `TRANSFER_MANIFEST.json`.

## Source Tree That Must Be Copied to Hermes

Authoritative source remains the Mac worktree:

```text
/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway/.worktrees/hermes-full-owner-gateway
branch: feature/hermes-full-owner-gateway
expected head: bf489e8de3f14301107dab1dcee9eb8d75b893c8
```

Copy **all Git-tracked project files required to build and test the repository**, including source, tests, package metadata, scripts and relevant repository docs. Preserve the Mac copy.

Do not copy:

- `.env` or secret-bearing environment files;
- browser cookies/profiles/auth databases;
- private keys, tokens or tunnel credentials;
- `node_modules`, cache, coverage and temporary output;
- stale build output when it can be rebuilt from source;
- Git worktree administrative metadata tied to the Mac filesystem.

Do not reconstruct source by decompiling or editing the running production release. If the source sync route is unavailable, report that exact transfer blocker and preserve the production runtime.

## Destination Rules

Use a dedicated Hermes user-owned development path, separate from production service directories. The Hermes agent must record the chosen path in its handoff.

The transfer is successful only after Hermes verifies:

```text
SOURCE_HEAD=<expected or explicitly explained divergence>
TRACKED_FILE_COUNT_SOURCE=<n>
TRACKED_FILE_COUNT_DESTINATION=<n>
FILESET_VERIFICATION=PASS
SECRETS_TRANSFERRED=NO
PROTECTED_EXISTING_SERVICES_CHANGED=NO
```

A file-list/hash comparison may exclude `.git` internals and generated artifacts but must cover all transferred tracked source files.

## Production Boundaries

Read-only checks are allowed. Do not restart, stop, reconfigure or replace:

- `hermes-gateway.service`
- `nattawit-lms-production-nginx.service`
- `docker.service`

Preserve the existing secure tunnel and existing ChatGPT Personal app unless a later implementation plan specifically requires a descriptor refresh.

## Development Ownership After Transfer

Hermes becomes the preferred development host for Reliability Pack implementation once the source tree sync is verified. Changes should be made in an isolated development branch/worktree on Hermes, with TDD, independent review, and explicit verification before any rollout.
