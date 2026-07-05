---
name: superpowers-bootstrap
description: Use when an Antigravity-style Superpowers bootstrap is requested in Codex - maps the bootstrap behavior to Codex's superpowers:using-superpowers skill
---

# Superpowers Bootstrap for Codex

This is a Codex compatibility wrapper for the Antigravity `superpowers-bootstrap`
skill.

Use Codex's native `superpowers:using-superpowers` skill for the actual workflow. It is the
Codex-compatible bootstrap that checks available skills before work starts and
loads the relevant Superpowers skill for the task.

When this wrapper is activated:

1. Load `superpowers:using-superpowers`.
2. Follow its skill-selection rules.
3. Prefer the plugin-provided Superpowers skills exposed as `superpowers:*`.
4. Do not use Antigravity-only tools such as `browser_subagent`, `task.md`, or
   `view_file`; use the Codex tool equivalents from the loaded skill.
