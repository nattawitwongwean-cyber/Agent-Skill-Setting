---
name: github-workflows
description: >
  Use for GitHub-first workflows: repo status, issues, branches, PRs, backup, and handoff to Codex.
---

# GitHub Workflows

Use GitHub as source of truth for repo work.

## Rules

- Inspect repo/branch/status before recommending changes.
- Prefer issue/branch/PR flow for development history.
- Do not deploy or merge unless user explicitly approves.
- If GitHub is only for backup, keep workflow simple: commit, push, PR/merge only when requested.
