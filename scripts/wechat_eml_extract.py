#!/usr/bin/env python3
"""Extract readable text from exported WeChat `.eml` files."""

from __future__ import annotations

import argparse
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
from pathlib import Path
import re
from typing import Iterable


WECHAT_EMOJI_MAP: dict[str, str] = {
    "[呲牙]": "😁",
    "[苦涩]": "🥹",
    "[握手]": "🤝",
    "[偷笑]": "🤭",
    "[让我看看]": "👀",
    "[玫瑰]": "🌹",
    "[转圈]": "💫",
    "[爱心]": "❤️",
    "[强]": "👍",
    "[微笑]": "😊",
    "[抱拳]": "🙏",
    "[加油]": "💪",
    "[吃瓜]": "🍉",
    "[社会社会]": "😎",
    "[庆祝]": "🎉",
    "[跳跳]": "🎉",
    "[666]": "💯",
    "[勾引]": "😉",
    "[奸笑]": "😏",
    "[得意]": "😎",
    "[月亮]": "🌙",
    "[烟花]": "🎆",
    "[图片]": "🖼️",
}


class HTMLTextExtractor(HTMLParser):
    """Convert basic HTML email bodies into readable plain text."""

    BLOCK_TAGS = {"p", "div", "br", "li", "tr", "table", "section"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if data:
            self.parts.append(data)

    def get_text(self) -> str:
        return "".join(self.parts)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract normalized text from WeChat .eml files.")
    parser.add_argument("--input-dir", required=True, help="Directory containing .eml files.")
    parser.add_argument("--output-dir", required=True, help="Directory for normalized markdown output.")
    return parser


def decode_text_parts(message) -> tuple[str, str]:
    plain_parts: list[str] = []
    html_parts: list[str] = []

    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = part.get_content_disposition()
            if content_disposition == "attachment":
                continue
            if content_type == "text/plain":
                plain_parts.append(part.get_content())
            elif content_type == "text/html":
                html_parts.append(part.get_content())
    else:
        content_type = message.get_content_type()
        if content_type == "text/plain":
            plain_parts.append(message.get_content())
        elif content_type == "text/html":
            html_parts.append(message.get_content())

    plain_text = "\n".join(part for part in plain_parts if part).strip()
    html_text = "\n".join(part for part in html_parts if part).strip()
    return plain_text, html_text


def html_to_text(html: str) -> str:
    parser = HTMLTextExtractor()
    parser.feed(html)
    return parser.get_text()


def normalize_whitespace(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def replace_wechat_emoji_placeholders(text: str) -> str:
    for placeholder, emoji in WECHAT_EMOJI_MAP.items():
        text = text.replace(placeholder, emoji)
    return text


def strip_mail_wrapper(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    marker_patterns = (
        "在微信上的聊天记录如下",
        "聊天记录如下",
        "请查收",
    )

    cut_index = -1
    for idx, line in enumerate(lines):
        if any(marker in line for marker in marker_patterns):
            cut_index = idx
            break

    if cut_index >= 0:
        lines = lines[cut_index + 1 :]

    while lines and not lines[0].strip():
        lines.pop(0)

    return "\n".join(lines).strip()


def choose_best_body(plain_text: str, html_text: str) -> str:
    if plain_text and len(plain_text) >= len(html_text):
        return plain_text
    if html_text:
        return html_to_text(html_text)
    return plain_text or ""


def iter_eml_files(input_dir: Path) -> Iterable[Path]:
    return sorted(path for path in input_dir.iterdir() if path.is_file() and path.suffix.lower() == ".eml")


def write_normalized_markdown(source: Path, output_dir: Path) -> Path:
    with source.open("rb") as handle:
        message = BytesParser(policy=policy.default).parse(handle)

    plain_text, html_text = decode_text_parts(message)
    body = choose_best_body(plain_text, html_text)
    body = strip_mail_wrapper(body)
    body = replace_wechat_emoji_placeholders(body)
    body = normalize_whitespace(body)

    subject = str(message.get("Subject", "")).strip()
    sent_at = str(message.get("Date", "")).strip()
    from_addr = str(message.get("From", "")).strip()
    to_addr = str(message.get("To", "")).strip()

    output = output_dir / f"{source.stem}.md"
    output.write_text(
        "\n".join(
            [
                f"# Source File: {source.name}",
                f"# Subject: {subject}",
                f"# Date: {sent_at}",
                f"# From: {from_addr}",
                f"# To: {to_addr}",
                "",
                body,
                "",
            ]
        ),
        encoding="utf-8",
    )
    return output


def main() -> int:
    args = build_parser().parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    if not input_dir.exists():
        raise SystemExit(f"Input directory does not exist: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    eml_files = list(iter_eml_files(input_dir))
    if not eml_files:
        raise SystemExit(f"No .eml files found in: {input_dir}")

    for source in eml_files:
        output = write_normalized_markdown(source, output_dir)
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
