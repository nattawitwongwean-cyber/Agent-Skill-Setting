#!/usr/bin/env python3
"""Create a compact Codex context pack for a repository."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

BEGIN = "<!-- context-bootstrap:start -->"
END = "<!-- context-bootstrap:end -->"

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".turbo",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
}

MANIFESTS = [
    "package.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
    "pyproject.toml",
    "requirements.txt",
    "poetry.lock",
    "uv.lock",
    "go.mod",
    "Cargo.toml",
    "Gemfile",
    "composer.json",
    "Makefile",
    "Dockerfile",
    "docker-compose.yml",
    "compose.yml",
]

DOC_PATTERNS = [
    "README.md",
    "README",
    "CONTRIBUTING.md",
    "docs",
    ".github",
]


@dataclass
class WriteResult:
    path: Path
    action: str


def rel(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def git_root(start: Path) -> Path:
    try:
        proc = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return start.resolve()
    if proc.returncode == 0 and proc.stdout.strip():
        return Path(proc.stdout.strip()).resolve()
    return start.resolve()


def read_text(path: Path, limit: int = 20_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def package_runner(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "bun.lock").exists() or (root / "bun.lockb").exists():
        return "bun"
    return "npm run"


def detect_package_commands(root: Path) -> list[tuple[str, str, str]]:
    package_json = root / "package.json"
    if not package_json.exists():
        return []
    try:
        data = json.loads(read_text(package_json))
    except json.JSONDecodeError:
        return []

    scripts = data.get("scripts", {})
    if not isinstance(scripts, dict):
        return []

    runner = package_runner(root)
    preferred = [
        ("install", "Install dependencies"),
        ("dev", "Run development server"),
        ("build", "Build"),
        ("test", "Test"),
        ("lint", "Lint"),
        ("typecheck", "Typecheck"),
        ("format", "Format"),
        ("start", "Start"),
    ]

    commands: list[tuple[str, str, str]] = []
    for script, purpose in preferred:
        if script not in scripts:
            continue
        if runner in {"pnpm", "yarn"}:
            command = f"{runner} {script}"
        elif runner == "bun":
            command = f"bun run {script}"
        else:
            command = f"npm run {script}"
        commands.append((purpose, command, "package.json"))
    return commands


def detect_make_targets(root: Path) -> list[tuple[str, str, str]]:
    makefile = root / "Makefile"
    if not makefile.exists():
        return []
    text = read_text(makefile)
    targets = set(re.findall(r"^([A-Za-z0-9_.-]+):(?:\s|$)", text, re.MULTILINE))
    commands: list[tuple[str, str, str]] = []
    for target, purpose in [
        ("setup", "Setup"),
        ("install", "Install dependencies"),
        ("dev", "Run development server"),
        ("build", "Build"),
        ("test", "Test"),
        ("lint", "Lint"),
        ("format", "Format"),
    ]:
        if target in targets:
            commands.append((purpose, f"make {target}", "Makefile"))
    return commands


def detect_commands(root: Path) -> list[tuple[str, str, str]]:
    commands = []
    commands.extend(detect_package_commands(root))
    commands.extend(detect_make_targets(root))

    if (root / "pyproject.toml").exists() or (root / "pytest.ini").exists():
        commands.append(("Test", "python3 -m pytest", "Python project files"))
    if (root / "go.mod").exists():
        commands.append(("Test", "go test ./...", "go.mod"))
    if (root / "Cargo.toml").exists():
        commands.append(("Test", "cargo test", "Cargo.toml"))

    deduped: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for item in commands:
        if item[1] in seen:
            continue
        seen.add(item[1])
        deduped.append(item)
    return deduped


def detect_manifests(root: Path) -> list[str]:
    found = []
    for name in MANIFESTS:
        if (root / name).exists():
            found.append(name)
    return found


def detect_docs(root: Path) -> list[str]:
    found = []
    for name in DOC_PATTERNS:
        path = root / name
        if path.exists():
            found.append(name)
    return found


def top_level_entries(root: Path) -> list[str]:
    entries = []
    try:
        children = sorted(root.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except OSError:
        return entries
    for child in children:
        if child.name in SKIP_DIRS:
            continue
        if child.name.startswith(".") and child.name not in {".github"}:
            continue
        suffix = "/" if child.is_dir() else ""
        entries.append(f"{child.name}{suffix}")
        if len(entries) >= 30:
            entries.append("...")
            break
    return entries


def render_table(rows: list[tuple[str, str, str]]) -> str:
    if not rows:
        return "| Purpose | Command | Source | Status |\n| --- | --- | --- | --- |\n| Unknown | Unknown | Not detected | Unverified |"
    lines = ["| Purpose | Command | Source | Status |", "| --- | --- | --- | --- |"]
    for purpose, command, source in rows:
        lines.append(f"| {purpose} | `{command}` | {source} | Unverified |")
    return "\n".join(lines)


def render_context(root: Path) -> str:
    manifests = detect_manifests(root)
    docs = detect_docs(root)
    entries = top_level_entries(root)
    commands = detect_commands(root)

    return f"""# Project Context

{BEGIN}
Generated by `context-bootstrap`. Keep this file compact and update facts when they change.

## Snapshot

- Root: `{root}`
- Manifests: {", ".join(f"`{item}`" for item in manifests) if manifests else "Unknown"}
- Existing docs: {", ".join(f"`{item}`" for item in docs) if docs else "Unknown"}

## Common Commands

Codex should run shell commands through `rtk`; commands below show the underlying project commands.

{render_table(commands)}

## Important Paths

{chr(10).join(f"- `{item}`" for item in entries) if entries else "- Unknown"}

## Working Agreements

- Follow `AGENTS.md` before this file.
- Prefer the smallest relevant context before editing.
- Mark assumptions as `Unknown` until verified.
- Do not store secrets, tokens, credentials, or private production data here.

## Unknowns To Clarify

- Primary product/domain owner.
- Canonical build, test, lint, and deploy commands.
- Critical services, environments, and safety constraints.
{END}
"""


def render_handoff() -> str:
    return f"""# Handoff

{BEGIN}
Update this before pausing substantial work or handing the repo to another Codex session.

## Current Goal

- Unknown

## Current State

- No active handoff yet.

## Changed Files

- Unknown

## Next Actions

- Unknown

## Risks Or Blockers

- Unknown
{END}
"""


def render_agents_block() -> str:
    return f"""{BEGIN}
## Project Context

- Read `docs/ai/CONTEXT.md` before substantial work in this repository.
- Use `docs/ai/HANDOFF.md` to resume paused work or preserve state before stopping.
- Keep generated context compact. Update facts when commands, structure, or constraints change.
- Commands in context files are canonical project commands; Codex should execute shell commands through `rtk`.
{END}"""


def replace_or_append_managed_block(existing: str, block: str) -> str:
    pattern = re.compile(rf"{re.escape(BEGIN)}.*?{re.escape(END)}", re.DOTALL)
    if pattern.search(existing):
        return pattern.sub(block, existing)
    separator = "\n\n" if existing.strip() else ""
    return existing.rstrip() + separator + block + "\n"


def write_managed_file(path: Path, content: str, overwrite: bool, dry_run: bool) -> WriteResult:
    if path.exists():
        existing = read_text(path, limit=2_000_000)
        if BEGIN in existing and END in existing:
            action = "update"
        elif overwrite:
            action = "overwrite"
        else:
            return WriteResult(path, "skip-existing-unmanaged")
    else:
        action = "create"

    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return WriteResult(path, action)


def update_agents(path: Path, dry_run: bool) -> WriteResult:
    block = render_agents_block()
    existing = read_text(path, limit=2_000_000) if path.exists() else ""
    updated = replace_or_append_managed_block(existing, block)
    action = "update" if path.exists() else "create"
    if not dry_run:
        path.write_text(updated, encoding="utf-8")
    return WriteResult(path, action)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or refresh Codex project context files.")
    parser.add_argument("path", nargs="?", default=".", help="Repository path. Defaults to current directory.")
    parser.add_argument("--context-dir", default="docs/ai", help="Context directory relative to repo root.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite unmanaged context files.")
    parser.add_argument("--dry-run", action="store_true", help="Show planned writes without changing files.")
    args = parser.parse_args()

    root = git_root(Path(args.path).expanduser())
    context_dir = root / args.context_dir

    results = [
        update_agents(root / "AGENTS.md", args.dry_run),
        write_managed_file(context_dir / "CONTEXT.md", render_context(root), args.overwrite, args.dry_run),
        write_managed_file(context_dir / "HANDOFF.md", render_handoff(), args.overwrite, args.dry_run),
    ]

    mode = "DRY RUN" if args.dry_run else "DONE"
    print(f"{mode}: context-bootstrap for {root}")
    for result in results:
        print(f"- {result.action}: {rel(root, result.path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
