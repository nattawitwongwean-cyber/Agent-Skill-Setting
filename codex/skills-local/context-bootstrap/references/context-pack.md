# Context Pack Reference

Use this reference when the default `context-bootstrap` output needs adjustment for a larger repo, monorepo, or team workflow.

## Layers

| Layer | Purpose | Keep It To |
| --- | --- | --- |
| `AGENTS.md` | Executable instructions Codex must follow | Rules, commands, context entry points |
| `docs/ai/CONTEXT.md` | Stable map of the repository | Architecture, directories, verified commands, unknowns |
| `docs/ai/HANDOFF.md` | Short-lived session state | Current goal, changed files, next actions, blockers |
| `docs/adr/` | Durable decisions | Decisions with tradeoffs and dates, only when useful |

## Good Context

- Helps a fresh Codex session act correctly within two minutes.
- Names canonical commands and whether they were verified.
- Points to source docs instead of copying them.
- Separates stable facts from current work.
- Leaves unknowns explicit.

## Bad Context

- Long summaries of obvious code.
- Secrets, private tokens, or pasted production data.
- Claims about behavior that were not verified.
- Duplicated README content with no new decision value.
- Large generated maps that will go stale immediately.

## Monorepo Pattern

Use one root context file for global rules, then package-specific sections:

```text
docs/ai/CONTEXT.md
packages/api/docs/ai/CONTEXT.md
packages/web/docs/ai/CONTEXT.md
```

Root `AGENTS.md` should say when to read package-level context. Avoid making every task load every package.

## Refresh Checklist

- Project commands still match manifests.
- Main directories and ownership notes are still current.
- Handoff reflects the current goal or is intentionally blank.
- New decisions have ADRs only if they will matter later.
- Old unknowns were resolved or intentionally kept.
