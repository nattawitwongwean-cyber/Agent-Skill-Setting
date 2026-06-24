#!/usr/bin/env python3
"""Compress context/log text with Headroom and emit text or metrics JSON."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("HEADROOM_TELEMETRY", "off")
os.environ.setdefault("HEADROOM_STATELESS", "true")


def read_input(path: str | None) -> str:
    if path and path != "-":
        return Path(path).read_text(encoding="utf-8", errors="replace")
    return sys.stdin.read()


def compress_generic(text: str, target_ratio: float, model: str) -> dict:
    from headroom import compress

    messages = [{"role": "user", "content": text}]
    res = compress(
        messages,
        model=model,
        compress_user_messages=True,
        protect_recent=0,
        target_ratio=target_ratio,
    )
    output = res.messages[0].get("content", "") if res.messages else ""
    return {
        "mode": "generic",
        "ok": True,
        "tokens_before": getattr(res, "tokens_before", None),
        "tokens_after": getattr(res, "tokens_after", None),
        "tokens_saved": getattr(res, "tokens_saved", None),
        "compression_ratio": getattr(res, "compression_ratio", None),
        "transforms_applied": getattr(res, "transforms_applied", []),
        "output": output,
    }


def compress_log(text: str) -> dict:
    from headroom.transforms import LogCompressor

    res = LogCompressor().compress(text)
    output = getattr(res, "compressed", "")
    before = getattr(res, "original_tokens", None)
    after = getattr(res, "compressed_tokens", None)
    if before is None or after is None:
        before = estimate_tokens(text)
        after = estimate_tokens(output)
    return {
        "mode": "log",
        "ok": True,
        "tokens_before": before,
        "tokens_after": after,
        "tokens_saved": before - after,
        "compression_ratio": getattr(res, "compression_ratio", None),
        "transforms_applied": ["LogCompressor"],
        "output": output,
    }


def estimate_tokens(text: str) -> int:
    try:
        import tiktoken

        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return max(1, len(text) // 4)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compress text/log context with Headroom")
    parser.add_argument("input", nargs="?", help="Input file, or stdin if omitted/-")
    parser.add_argument("--mode", choices=["generic", "log"], default="generic")
    parser.add_argument("--target-ratio", type=float, default=0.30)
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--json", action="store_true", help="Print full JSON including output")
    parser.add_argument("--metrics-only", action="store_true", help="Print JSON metrics without compressed output")
    parser.add_argument("--output", help="Write compressed text to file")
    args = parser.parse_args()

    text = read_input(args.input)
    if not text.strip():
        result = {"mode": args.mode, "ok": False, "error": "empty_input", "output": ""}
    else:
        try:
            result = compress_log(text) if args.mode == "log" else compress_generic(text, args.target_ratio, args.model)
        except Exception as exc:
            result = {"mode": args.mode, "ok": False, "error": type(exc).__name__, "detail": str(exc), "output": text}

    output = result.get("output", "")
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")

    if args.metrics_only:
        metrics = {k: v for k, v in result.items() if k != "output"}
        print(json.dumps(metrics, ensure_ascii=False, indent=2))
    elif args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(output)
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
