#!/usr/bin/env python3
"""Append a quick-capture entry to inbox/capture.md.

Usage:
    echo "明天把下载目录规则整理一下" | python .agents/skills/quick-capture/scripts/append_capture.py --type todo --tags codex,agent
"""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a capture entry.")
    parser.add_argument("--type", default="note", help="Entry type, e.g. idea/todo/note/link/decision")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--source", default="manual", help="Source of the entry")
    parser.add_argument("--text", default=None, help="Raw text. If omitted, stdin is used.")
    parser.add_argument("--file", default="inbox/capture.md", help="Target markdown file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw = args.text if args.text is not None else sys.stdin.read().strip()
    if not raw:
        print("No input text provided.", file=sys.stderr)
        return 1

    target = Path(args.file)
    target.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    tags = ", ".join([t.strip() for t in args.tags.split(",") if t.strip()]) or "-"
    entry = (
        f"## [{now}] {args.type}\n"
        f"- 来源：{args.source}\n"
        f"- 标签：{tags}\n"
        f"- 原始内容：{raw}\n"
        f"- 行动建议：\n\n"
    )
    with target.open("a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Appended capture entry to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
