#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
stamp="$(date +%Y%m%d-%H%M%S)"
backup_dir="$codex_home/backup-agent-skill-setting-$stamp"

mkdir -p "$codex_home" "$backup_dir"

backup_if_exists() {
  local path="$1"
  if [ -e "$path" ] || [ -L "$path" ]; then
    mv "$path" "$backup_dir/"
  fi
}

for file in AGENTS.md RTK.md SKILL_AUTOUSE.md SKILL_SELECTION_TH.md SKILL_SELECTION_TH.json; do
  if [ -e "$repo_root/codex/files/$file" ]; then
    backup_if_exists "$codex_home/$file"
    cp "$repo_root/codex/files/$file" "$codex_home/$file"
  fi
done

if [ -d "$repo_root/codex/skills-local" ] || [ -d "$repo_root/codex/skills-symlink-real" ]; then
  backup_if_exists "$codex_home/skills"
  mkdir -p "$codex_home/skills"
fi

if [ -d "$repo_root/codex/skills-local" ]; then
  cp -R "$repo_root/codex/skills-local/." "$codex_home/skills/"
fi

if [ -d "$repo_root/codex/skills-symlink-real" ]; then
  cp -R "$repo_root/codex/skills-symlink-real/." "$codex_home/skills/"
fi

echo "Restored portable Codex settings to $codex_home"
echo "Previous files were moved to $backup_dir"
echo "Skills were restored as real directories."
