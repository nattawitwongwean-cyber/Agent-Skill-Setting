---
name: writing-workflows
description: Use when an Antigravity-style workflow or skill authoring task is requested in Codex - maps to Superpowers superpowers:writing-skills
---

# Writing Workflows for Codex

This is a Codex compatibility wrapper for Antigravity's `writing-workflows`
skill.

Use the Codex-native `superpowers:writing-skills` skill for the real workflow. It covers
creating, refining, and testing reusable agent skills in the Superpowers style.

When this wrapper is activated:

1. Load `superpowers:writing-skills`.
2. Follow its guidance for skill structure, frontmatter, progressive disclosure,
   and validation.
3. For Codex-specific skills, install them under `~/.codex/skills` or the
   workspace's `.agents/skills` only when a project-local skill is intended.
4. Avoid Antigravity-only global workflow paths unless the user explicitly asks
   for Antigravity support.
