---
name: context-bootstrap
description: Use when starting work in an unfamiliar repository, preparing Codex for a project, refreshing AGENTS.md or repo context, reducing repeated exploration, or creating compact context maps, handoff notes, command references, architecture notes, or AI onboarding files.
metadata:
  short-description: Create compact repo context for Codex
---

# Context Bootstrap

Create a compact, durable context layer so future Codex sessions can understand a repository quickly without rereading everything.

## When To Use

Use this skill when:

- A project is new, large, poorly documented, or repeatedly re-explored.
- The user asks to set up Codex, context, `AGENTS.md`, AI docs, onboarding, handoff, repo memory, or project instructions.
- You need a concise map of commands, architecture, important paths, current state, and unknowns.

Do not use it for one-off edits where reading the touched files is faster than creating repo context.

## Workflow

1. Inspect existing context first: `AGENTS.md`, `README*`, package manifests, docs, issue trackers, and recent handoff notes.
2. Run the helper in dry-run mode from the repo root:

```bash
rtk python3 ~/.codex/skills/context-bootstrap/scripts/bootstrap_context.py "$PWD" --dry-run
```

3. If the plan looks safe, run it without `--dry-run`. The helper only overwrites generated managed blocks by default.
4. Review the generated files and refine facts manually. Mark unverified assumptions as `Unknown` instead of guessing.
5. For complex repos, read `references/context-pack.md` before customizing the structure.

## Default Outputs

- `AGENTS.md`: Adds a managed project-context block without replacing existing instructions.
- `docs/ai/CONTEXT.md`: Stable project map, commands, important files, and open questions.
- `docs/ai/HANDOFF.md`: Small handoff template for current goal, next steps, and risks.

## Guardrails

- Preserve user-written content. If a file exists without context-bootstrap markers, ask before replacing or use `--overwrite` only with clear intent.
- Keep context compact: facts future Codex needs in the first two minutes, not full documentation.
- Do not include secrets, tokens, private endpoints, or large copied logs.
- Commands should be copied from manifests or existing docs when possible. If not tested, label them unverified.
- Prefer links to detailed docs over duplicating long explanations.

## Useful Companion Skills

- `zoom-out`: build a higher-level architecture understanding before writing context.
- `handoff`: compact current session state into reusable notes.
- `grill-with-docs`: turn existing docs into sharper requirements or assumptions.
- `to-prd` and `to-issues`: convert product context into plans and trackable work.
