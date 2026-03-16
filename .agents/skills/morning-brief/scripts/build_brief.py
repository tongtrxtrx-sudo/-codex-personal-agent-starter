#!/usr/bin/env python3
"""Build a simple morning brief from local markdown files."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import sys


CHECKBOX_RE = re.compile(r"^\s*-\s*\[\s\]\s+(.*)$")


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def collect_tasks(path: Path) -> list[str]:
    if not path.exists():
        return []
    tasks: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = CHECKBOX_RE.match(line)
        if m:
            tasks.append(m.group(1).strip())
    return tasks


def last_capture_lines(path: Path, limit: int = 8) -> list[str]:
    if not path.exists():
        return []
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip().startswith("- 原始内容：")]
    return [ln.replace("- 原始内容：", "", 1).strip() for ln in lines[-limit:]]


def main() -> int:
    configure_stdio()

    focus_file = Path("memory/current_focus.md")
    capture_file = Path("inbox/capture.md")

    priorities = collect_tasks(focus_file)[:3]
    recent_captures = last_capture_lines(capture_file, limit=5)

    print(f"# 今日晨报（{date.today().isoformat()}）")
    print()
    print("## 今日最重要的 3 件事")
    if priorities:
        for i, item in enumerate(priorities, start=1):
            print(f"{i}. {item}")
    else:
        print("1. （尚未在 memory/current_focus.md 中填写）")

    print()
    print("## 最近值得留意")
    if recent_captures:
        for item in recent_captures:
            print(f"- {item}")
    else:
        print("- （capture 里暂无新内容）")

    print()
    print("## 建议起手动作")
    if priorities:
        print(f"- 先做：{priorities[0]}")
    else:
        print("- 先补全 current_focus.md，再开始今天的工作。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
