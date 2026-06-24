# Agent Skill Setting

Backup and restore files for Codex agent, plugin, and skill configuration.

This repository intentionally stores safe, reusable configuration only. It does
not store auth tokens, sessions, logs, sqlite state, browser profiles, generated
images, or other machine-local runtime data.

## Layout

- `codex/files/` - portable Codex instruction files.
- `codex/skills-local/` - local skill folders that contain real `SKILL.md`
  files.
- `codex/manifests/` - generated inventory for skills, symlinks, plugins, and
  feature flags.
- `scripts/generate-codex-snapshot.py` - regenerate the snapshot from the
  current machine.
- `scripts/restore-codex-settings.sh` - restore the portable files into
  `~/.codex`.

## Restore

From this repository root:

```bash
bash scripts/restore-codex-settings.sh
```

The restore script backs up existing files before writing replacements.
