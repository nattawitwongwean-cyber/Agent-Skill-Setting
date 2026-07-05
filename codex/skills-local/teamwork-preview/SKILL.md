---
name: teamwork-preview
description: Use when an Antigravity-style teamwork-preview workflow is requested in Codex - maps to the Codex-native superpowers:subagent-driven-development workflow.
---

# Teamwork Preview for Codex

This is a Codex compatibility wrapper for Antigravity's `teamwork-preview`
skill.

Use the Codex-native `superpowers:subagent-driven-development` skill for the real workflow.
That skill contains the full Superpowers implementation process, including task
isolation, implementation review, code-quality review, and verification.

When this wrapper is activated:

1. Load `superpowers:subagent-driven-development`.
2. If Codex multiagent tools are available, use them according to the loaded
   skill.
3. If multiagent tools are not available, execute the workflow sequentially
   while preserving the review gates described by
   `superpowers:subagent-driven-development`.
4. Do not use Antigravity-only tools such as `browser_subagent`, `task.md`, or
   `view_file`; use Codex equivalents.
