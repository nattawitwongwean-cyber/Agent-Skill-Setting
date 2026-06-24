#!/usr/bin/env python3
"""Generate a safe Codex skill/config snapshot for this repository."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
from pathlib import Path


CODEX_HOME = Path.home() / ".codex"
REPO_ROOT = Path(__file__).resolve().parents[1]
OUT = REPO_ROOT / "codex"

SAFE_FILES = [
    "AGENTS.md",
    "RTK.md",
    "SKILL_AUTOUSE.md",
    "SKILL_SELECTION_TH.md",
    "SKILL_SELECTION_TH.json",
]

EXCLUDED_SENSITIVE_FILES = [
    "auth.json",
    "history.jsonl",
    "session_index.jsonl",
    "sessions/",
    "log/",
    "logs_*.sqlite*",
    "state_*.sqlite*",
    "memories_*.sqlite*",
    "goals_*.sqlite*",
    "browser/",
    "attachments/",
    "generated_images/",
]

SANITIZE_REPLACEMENTS = {
    "ghp_" + "abc123": "github-token-example-redacted",
}


def read_skill_metadata(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8", errors="replace")[:6000]
    name = re.search(r"^name:\s*(.+)$", text, re.M)
    desc = re.search(r"^description:\s*(.+)$", text, re.M)
    return {
        "name": name.group(1).strip() if name else skill_file.parent.name,
        "description": desc.group(1).strip() if desc else "",
    }


def copy_safe_files() -> None:
    target = OUT / "files"
    target.mkdir(parents=True, exist_ok=True)
    for name in SAFE_FILES:
        src = CODEX_HOME / name
        if src.exists():
            shutil.copy2(src, target / name)


def copy_local_skills() -> tuple[list[dict[str, str]], list[dict[str, str]], list[str]]:
    source = CODEX_HOME / "skills"
    target = OUT / "skills-local"
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    local: list[dict[str, str]] = []
    symlinks: list[dict[str, str]] = []
    missing: list[str] = []

    for item in sorted(source.iterdir(), key=lambda p: p.name.lower()):
        if item.name == ".system":
            continue
        if item.is_symlink():
            symlinks.append({"name": item.name, "target": os.readlink(item)})
            continue
        if not item.is_dir():
            continue
        skill_file = item / "SKILL.md"
        if not skill_file.exists():
            missing.append(item.name)
            continue
        dest = target / item.name
        shutil.copytree(
            item,
            dest,
            ignore=shutil.ignore_patterns(
                ".git",
                ".DS_Store",
                "__pycache__",
                "node_modules",
                ".coverage",
                ".pytest_cache",
            ),
        )
        sanitize_tree(dest)
        meta = read_skill_metadata(skill_file)
        local.append({"folder": item.name, **meta})

    return local, symlinks, missing


def sanitize_tree(path: Path) -> None:
    for file_path in path.rglob("*"):
        if not file_path.is_file():
            continue
        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = text
        for old, new in SANITIZE_REPLACEMENTS.items():
            updated = updated.replace(old, new)
        if updated != text:
            file_path.write_text(updated, encoding="utf-8")


def read_config_inventory() -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    config = CODEX_HOME / "config.toml"
    if not config.exists():
        return [], []
    text = config.read_text(encoding="utf-8", errors="replace")

    plugins = []
    for match in re.finditer(r'^\[plugins\."([^"]+)"\]\s*\nenabled\s*=\s*(true|false)', text, re.M):
        plugins.append({"plugin": match.group(1), "enabled": match.group(2) == "true"})

    features = []
    in_features = False
    for line in text.splitlines():
        if line.strip() == "[features]":
            in_features = True
            continue
        if in_features and line.startswith("["):
            break
        if in_features and "=" in line:
            key, value = [part.strip() for part in line.split("=", 1)]
            features.append({"feature": key, "value": value})

    return plugins, features


def write_manifests(
    local: list[dict[str, str]],
    symlinks: list[dict[str, str]],
    missing: list[str],
    plugins: list[dict[str, object]],
    features: list[dict[str, str]],
) -> None:
    out = OUT / "manifests"
    out.mkdir(parents=True, exist_ok=True)
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat()
    enabled_count = sum(1 for item in plugins if item["enabled"])

    snapshot = {
        "generated_at": generated_at,
        "source_codex_home": str(CODEX_HOME),
        "counts": {
            "local_skill_dirs": len(local),
            "symlink_skills": len(symlinks),
            "missing_skill_md_dirs": len(missing),
            "enabled_plugins": enabled_count,
        },
        "excluded_sensitive_files": EXCLUDED_SENSITIVE_FILES,
    }

    files = {
        "snapshot.json": snapshot,
        "local-skills.json": local,
        "symlink-skills.json": symlinks,
        "missing-skill-md.json": missing,
        "plugins-enabled.json": plugins,
        "features.json": features,
    }
    for name, data in files.items():
        (out / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Codex Skill Snapshot",
        "",
        f"Generated: {generated_at}",
        "",
        "## Counts",
        "",
        f"- Local skill dirs: {len(local)}",
        f"- Symlink skills: {len(symlinks)}",
        f"- Missing SKILL.md dirs: {len(missing)}",
        f"- Enabled plugins: {enabled_count}",
        "",
        "## Local Skills",
        "",
    ]
    for item in local:
        description = item.get("description", "")
        if description:
            lines.append(f"- `{item['folder']}` - {description}")
        else:
            lines.append(f"- `{item['folder']}`")
    lines += ["", "## Symlink Skills", ""]
    for item in symlinks:
        lines.append(f"- `{item['name']}` -> `{item['target']}`")
    lines += ["", "## Missing SKILL.md Directories", ""]
    lines.extend([f"- `{item}`" for item in missing] or ["- None"])
    lines += ["", "## Enabled Plugins", ""]
    for item in plugins:
        if item["enabled"]:
            lines.append(f"- `{item['plugin']}`")
    (out / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    copy_safe_files()
    local, symlinks, missing = copy_local_skills()
    plugins, features = read_config_inventory()
    write_manifests(local, symlinks, missing, plugins, features)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
