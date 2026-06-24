---
name: headroom-context-compression
description: Use when compressing, checkpointing, summarizing, or reducing token usage for long logs, audit reports, runtime state, conversation context, tool outputs, or Hermes/Codex reports using Headroom from chopratejas/headroom.
---

# Headroom Context Compression

Use this skill to reduce token cost before sending long context to an LLM.

## Runtime paths

Codex runtime:

`/Users/nattawit/.codex/venvs/headroom/bin/python`

Codex resource:

`/Users/nattawit/.codex/resources/headroom`

Helper script:

`/Users/nattawit/.codex/skills/headroom-context-compression/scripts/compress_context.py`

## When to use

Use Headroom before LLM calls for:

- Hermes audit reports and `runtime_truth_latest.json`
- `journalctl` logs, cron inventory, skill audit output
- long context/checkpoint text before continuation
- repeated tool outputs where exact raw detail is not needed
- conversation-history review where you need to compress many sessions into a timeline without losing the evidence trail

See `references/session-review-playbook.md` for the browse/read/scroll workflow when reconstructing prior sessions.

Do not use it for:

- short user messages
- secrets, OAuth callback URLs, tokens, passwords
- legal/grade-critical text where exact wording must be preserved unless the raw source is also retained

## Commands

Generic context compression:

```bash
/Users/nattawit/.codex/venvs/headroom/bin/python \
  /Users/nattawit/.codex/skills/headroom-context-compression/scripts/compress_context.py input.txt \
  --mode generic --target-ratio 0.30 --metrics-only
```

Log compression:

```bash
/Users/nattawit/.codex/venvs/headroom/bin/python \
  /Users/nattawit/.codex/skills/headroom-context-compression/scripts/compress_context.py hermes.log \
  --mode log --json
```

## Reporting contract

When this skill is used in Hermes/Codex reports, include:

- `compression: headroom`
- `mode: generic|log`
- `tokens_before`
- `tokens_after`
- `compression_ratio`
- whether raw source was retained

## Policy

Keep raw source files on disk. Headroom output is a working context, not the only record.
