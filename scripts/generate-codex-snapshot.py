#!/usr/bin/env python3
"""Generate a safe Codex skill/config snapshot for this repository."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import subprocess
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

MANUAL_SOURCE_REPOSITORIES = [
    {
        "name": "impeccable",
        "url": "https://github.com/pbakaus/impeccable",
        "install_hint": "npx skills add pbakaus/impeccable",
        "notes": "Skill imported via the skills CLI; current Codex copy is stored under codex/skills-local/impeccable.",
    },
    {
        "name": "mattpocock-skills",
        "url": "https://github.com/mattpocock/skills.git",
        "install_hint": "git clone https://github.com/mattpocock/skills.git",
        "notes": "Imported and converted into local Codex skills; see setup-matt-pocock-skills and related local skill folders.",
    },
    {
        "name": "rtk",
        "url": "https://github.com/rtk-ai/rtk",
        "install_hint": "brew install rtk",
        "notes": "Shell guard is configured through RTK.md; command available at /opt/homebrew/bin/rtk on this machine.",
    },
    {
        "name": "cocoindex",
        "url": "https://github.com/cocoindex-io/cocoindex.git",
        "install_hint": "git clone https://github.com/cocoindex-io/cocoindex.git",
        "notes": "Recorded from prior evaluation request; not copied as a Codex skill in this snapshot.",
    },
    {
        "name": "9router",
        "url": "https://github.com/decolua/9router.git",
        "install_hint": "git clone https://github.com/decolua/9router.git",
        "notes": "Recorded from prior routing/Hermes architecture discussion; not copied as a Codex skill in this snapshot.",
    },
]


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


def copy_skill_tree(source: Path, dest: Path) -> None:
    shutil.copytree(
        source,
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


def copy_local_skills() -> tuple[list[dict[str, str]], list[dict[str, str]], list[str]]:
    source = CODEX_HOME / "skills"
    local_target = OUT / "skills-local"
    symlink_target = OUT / "skills-symlink-real"
    for target in (local_target, symlink_target):
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
            resolved = item.resolve()
            copied = False
            if (resolved / "SKILL.md").exists():
                copy_skill_tree(resolved, symlink_target / item.name)
                copied = True
            symlinks.append({
                "name": item.name,
                "target": os.readlink(item),
                "resolved": str(resolved),
                "copied_as_real_files": copied,
            })
            continue
        if not item.is_dir():
            continue
        skill_file = item / "SKILL.md"
        if not skill_file.exists():
            missing.append(item.name)
            continue
        dest = local_target / item.name
        copy_skill_tree(item, dest)
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


def git_remote_url(repo: Path) -> str:
    try:
        output = subprocess.check_output(
            ["git", "-C", str(repo), "remote", "get-url", "origin"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return output.strip()


def current_git_commit(repo: Path) -> str:
    try:
        output = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return output.strip()


def discover_source_repositories() -> list[dict[str, str]]:
    repositories: list[dict[str, str]] = []
    seen_urls: set[str] = set()

    for git_dir in sorted(CODEX_HOME.rglob(".git"), key=lambda p: str(p).lower()):
        if ".tmp" in git_dir.parts:
            continue
        repo = git_dir.parent
        url = git_remote_url(repo)
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)
        repositories.append(
            {
                "name": repo.name,
                "url": url,
                "local_path": str(repo),
                "commit": current_git_commit(repo),
                "source": "discovered-git-remote",
            }
        )

    for item in MANUAL_SOURCE_REPOSITORIES:
        if item["url"] in seen_urls:
            continue
        repositories.append({**item, "source": "manual-install-record"})
        seen_urls.add(item["url"])

    return repositories


def write_manifests(
    local: list[dict[str, str]],
    symlinks: list[dict[str, str]],
    missing: list[str],
    plugins: list[dict[str, object]],
    features: list[dict[str, str]],
    repositories: list[dict[str, str]],
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
            "symlink_skills_copied_as_real_files": sum(1 for item in symlinks if item["copied_as_real_files"]),
            "missing_skill_md_dirs": len(missing),
            "enabled_plugins": enabled_count,
            "source_repositories": len(repositories),
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
        "source-repositories.json": repositories,
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
        f"- Symlink skills copied as real files: {sum(1 for item in symlinks if item['copied_as_real_files'])}",
        f"- Missing SKILL.md dirs: {len(missing)}",
        f"- Enabled plugins: {enabled_count}",
        f"- Source repositories: {len(repositories)}",
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
        status = "copied" if item["copied_as_real_files"] else "not copied"
        lines.append(f"- `{item['name']}` -> `{item['target']}` ({status})")
    lines += ["", "## Missing SKILL.md Directories", ""]
    lines.extend([f"- `{item}`" for item in missing] or ["- None"])
    lines += ["", "## Enabled Plugins", ""]
    for item in plugins:
        if item["enabled"]:
            lines.append(f"- `{item['plugin']}`")
    lines += ["", "## Source Repositories", ""]
    for item in repositories:
        detail = item.get("install_hint") or item.get("local_path") or ""
        suffix = f" - {detail}" if detail else ""
        lines.append(f"- `{item['name']}` - {item['url']}{suffix}")
    (out / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    repo_lines = [
        "# Source Repositories",
        "",
        "Install sources and reference repositories used to build this Codex skill snapshot.",
        "This is an inventory only; secrets, sessions, logs, and runtime state are intentionally excluded.",
        "",
    ]
    for item in repositories:
        repo_lines.extend(
            [
                f"## {item['name']}",
                "",
                f"- URL: {item['url']}",
                f"- Source: {item.get('source', '')}",
            ]
        )
        if item.get("local_path"):
            repo_lines.append(f"- Local path at snapshot time: `{item['local_path']}`")
        if item.get("commit"):
            repo_lines.append(f"- Commit at snapshot time: `{item['commit']}`")
        if item.get("install_hint"):
            repo_lines.append(f"- Install hint: `{item['install_hint']}`")
        if item.get("notes"):
            repo_lines.append(f"- Notes: {item['notes']}")
        repo_lines.append("")
    (out / "SOURCE_REPOSITORIES.md").write_text("\n".join(repo_lines), encoding="utf-8")


def main() -> int:
    copy_safe_files()
    local, symlinks, missing = copy_local_skills()
    plugins, features = read_config_inventory()
    repositories = discover_source_repositories()
    write_manifests(local, symlinks, missing, plugins, features, repositories)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
