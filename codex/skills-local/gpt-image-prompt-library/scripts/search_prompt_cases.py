#!/usr/bin/env python3
"""Search GPT Image prompt cases from the local resource pack."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_ROOT = Path.home() / ".codex" / "resources" / "gpt-image-2-prompts"
CASE_RE = re.compile(r"^### Case\s+(?P<num>\d+):\s+\[(?P<title>[^\]]+)\]\((?P<url>[^)]+)\)", re.M)
PROMPT_RE = re.compile(r"\*\*Prompt:\*\*\s*\n\s*```\s*\n(?P<prompt>.*?)\n```", re.S)


def iter_cases(root: Path):
    cases_dir = root / "cases"
    for path in sorted(cases_dir.glob("*.md")):
        if "_" in path.stem:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = list(CASE_RE.finditer(text))
        for idx, match in enumerate(matches):
            start = match.end()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
            block = text[start:end]
            prompt_match = PROMPT_RE.search(block)
            prompt = prompt_match.group("prompt").strip() if prompt_match else ""
            yield {
                "category": path.stem,
                "case": int(match.group("num")),
                "title": match.group("title"),
                "source_url": match.group("url"),
                "prompt": prompt,
                "file": str(path),
            }


def score(case, terms):
    blob = f"{case['category']} {case['title']} {case['prompt']}".lower()
    return sum(blob.count(term) for term in terms)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="*", help="Search terms, e.g. poster classroom thai")
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--category", help="Filter category: portrait, poster, ui, ecommerce, ad-creative, character, comparison")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).expanduser()
    terms = [q.lower() for q in args.query]
    rows = []
    for case in iter_cases(root):
        if args.category and case["category"] != args.category:
            continue
        s = score(case, terms) if terms else 1
        if s > 0:
            case = dict(case)
            case["score"] = s
            rows.append(case)
    rows.sort(key=lambda c: (c["score"], c["case"]), reverse=True)
    rows = rows[: args.limit]

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        for c in rows:
            preview = " ".join(c["prompt"].split())[:300]
            print(f"[{c['category']} #{c['case']}] {c['title']}")
            print(f"source: {c['source_url']}")
            print(f"prompt: {preview}")
            print()

if __name__ == "__main__":
    main()
