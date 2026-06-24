---
name: rtk-shell-guard
description: >
  Use when running shell, terminal, ssh, systemctl, journalctl, git, or any command where token-efficient output matters.
---

# RTK Shell Guard

Always run shell commands through `rtk` unless a command explicitly cannot be proxied. Prefer concise commands and bounded output.

## Rules

- Prefix commands with `rtk`.
- Use `rg` for text search and `rg --files` for file search when available.
- Limit log output with `tail`, `sed -n`, or exact filters.
- Do not run destructive commands unless the user explicitly approved them.
- Summarize important output for the user because they do not see raw terminal output.
