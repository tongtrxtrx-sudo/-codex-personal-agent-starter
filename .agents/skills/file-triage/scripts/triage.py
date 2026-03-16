#!/usr/bin/env python3
"""Dry-run or apply a simple file triage plan."""
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import shutil
import sys


CATEGORY_MAP = {
    "images": {"png", "jpg", "jpeg", "webp", "gif", "svg"},
    "video": {"mp4", "mov", "mkv", "avi", "webm"},
    "audio": {"mp3", "wav", "m4a", "flac"},
    "docs": {"pdf", "doc", "docx", "txt", "md", "ppt", "pptx"},
    "sheets": {"xls", "xlsx", "csv"},
    "archives": {"zip", "rar", "7z", "tar", "gz"},
    "code": {"py", "js", "ts", "json", "yaml", "yml", "sh", "html", "css"},
}


def categorize(path: Path) -> str:
    ext = path.suffix.lower().lstrip(".")
    for category, exts in CATEGORY_MAP.items():
        if ext in exts:
            return category
    return "misc"


def unique_destination(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    i = 1
    while True:
        candidate = parent / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def plan_moves(target_dir: Path, sorted_dirname: str = "_sorted") -> list[tuple[Path, Path]]:
    plans: list[tuple[Path, Path]] = []
    for child in sorted(target_dir.iterdir()):
        if not child.is_file():
            continue
        category = categorize(child)
        dest_dir = target_dir / sorted_dirname / category
        dest = unique_destination(dest_dir / child.name)
        plans.append((child, dest))
    return plans


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dry-run or apply file triage.")
    parser.add_argument("target", help="Directory to organize")
    parser.add_argument("--apply", action="store_true", help="Actually move files")
    parser.add_argument("--sorted-dirname", default="_sorted", help="Destination root directory name")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_dir = Path(args.target).expanduser().resolve()
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Target directory not found: {target_dir}", file=sys.stderr)
        return 1

    plans = plan_moves(target_dir, sorted_dirname=args.sorted_dirname)
    if not plans:
        print("No files to organize.")
        return 0

    counts = defaultdict(int)
    print("Planned moves:")
    for src, dst in plans:
        counts[dst.parent.name] += 1
        print(f"- {src.name} -> {dst}")

    print()
    print("Summary:")
    for category in sorted(counts):
        print(f"- {category}: {counts[category]} file(s)")

    if not args.apply:
        print()
        print("Dry-run only. Re-run with --apply to execute.")
        return 0

    for src, dst in plans:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))

    print()
    print("Applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
