---
name: context-compression-checkpoint
description: >
  Use when context is long, work must continue later, or a checkpoint/resume summary is needed.
---

# Context Compression Checkpoint

Use this as the canonical checkpoint skill in Codex. Prefer Headroom as an engine when log/session compression is needed.

## Rules

- Capture objective, current state, files touched, decisions, blockers, next actions, and verification evidence.
- Keep checkpoint short enough to paste into a new session.
- Use `headroom-context-compression` when compressing long logs or session transcripts.
- Do not checkpoint repeatedly when no meaningful work changed.
