# HERMES-HRP-TRANSFER-0001 — Transfer Reliability Pack Development Inputs to Hermes

## Objective

Stage and verify every development input required for the approved Hermes Reliability Pack on a dedicated Hermes user-owned development workspace, without mutating protected production services or deleting the authoritative Mac source.

## Authority

Explicit human instruction: transfer all files that need development to Hermes.

Transfer manifest:

`agent-bridge/transfers/HERMES-HRP-0001/TRANSFER_MANIFEST.json`

Transfer handoff:

`agent-bridge/transfers/HERMES-HRP-0001/README.md`

Approved umbrella design:

`docs/superpowers/specs/2026-08-21-hermes-reliability-pack-design.md`

## Phase 1 — Pull Control/Design Inputs

On Hermes, update the existing safe checkout of `nattawitwongwean-cyber/Agent-Skill-Setting` using non-destructive Git operations. Do not reset/clean away local work.

Verify all `controlRepository.requiredFiles` from the transfer manifest are present.

## Phase 2 — Establish Dedicated Hermes Development Destination

Choose a user-owned development path separate from the running release/service directories. Record the exact path in the handoff.

Do not develop inside the protected production runtime directory.

## Phase 3 — Copy Full Authoritative Source Baseline

Source:

```text
/Users/nattawit/Documents/Codex/2026-08-19/files-pasted-by-the-user-master/work/mac-owner-gateway/.worktrees/hermes-full-owner-gateway
feature/hermes-full-owner-gateway
bf489e8de3f14301107dab1dcee9eb8d75b893c8
```

When an already-authorized authenticated Mac↔Hermes transfer route is available, copy all Git-tracked project source/test/script/package/doc files needed to build and test the repository.

Rules:

- COPY, do not move/delete the Mac source.
- Do not transfer `.env`, credentials, browser/session data, private keys, tokens, tunnel secrets, caches, `node_modules`, coverage or temporary output.
- Do not copy Mac-specific `.git/worktrees` administrative metadata into the Hermes development tree.
- Prefer a clean Git repository/worktree representation on Hermes preserving commit history and `bf489e8` provenance when the existing route supports it.
- Do not reconstruct missing source from the production release.

If the Mac source route is unavailable, set `SOURCE_TREE_TRANSFER=BLOCKED_MAC_CONTROL_ROUTE`, keep all GitHub-delivered files staged on Hermes, and wait. Do not report complete.

## Phase 4 — Verify File Transfer

Fresh verification must capture:

```text
HERMES_DEV_PATH=<path>
SOURCE_BRANCH=feature/hermes-full-owner-gateway
SOURCE_HEAD=bf489e8de3f14301107dab1dcee9eb8d75b893c8
TRACKED_FILE_COUNT_SOURCE=<integer>
TRACKED_FILE_COUNT_DESTINATION=<integer>
FILESET_VERIFICATION=PASS
CONTROL_INPUTS_PRESENT=YES
SECRETS_TRANSFERRED=NO
PROTECTED_EXISTING_SERVICES_CHANGED=NO
```

Use a sanitized tracked-file manifest/hash comparison. Never print file contents that may contain secrets.

## Phase 5 — Preserve Production

Read-only confirm:

```text
hermes-gateway.service=active
nattawit-lms-production-nginx.service=active
docker.service=active
```

No restart, stop, enable/disable, reconfiguration or replacement is authorized by this transfer task.

## Completion

Reply in Control Room as:

```text
[FROM: HERMES AGENTS]
[TO: CHATGPT]
MSG-ID: HERMES-HRP-TRANSFER-0001
TASK-ID: HERMES-HRP-TRANSFER-0001
STATUS: NEEDS_CHATGPT_REVIEW
HERMES_DEV_PATH: ...
SOURCE_HEAD: ...
TRACKED_FILE_COUNT_SOURCE: ...
TRACKED_FILE_COUNT_DESTINATION: ...
FILESET_VERIFICATION: PASS
CONTROL_INPUTS_PRESENT: YES
SECRETS_TRANSFERRED: NO
PROTECTED_EXISTING_SERVICES_CHANGED: NO
NEXT_ACTION: WAIT
```

Do not begin Reliability Pack source modification until the transfer verification is complete and the implementation plan for the corresponding track is available/approved.
