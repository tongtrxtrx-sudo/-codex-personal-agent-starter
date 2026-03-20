#!/usr/bin/env python3
"""Build deterministic workflow packets for the copy workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


SCENES: dict[str, dict[str, Any]] = {
    "activity_promo": {
        "aliases": ["活动", "推广", "招生活动", "春游", "体验日", "促销", "报名"],
        "minimal_questions": [
            "time",
            "deadline",
            "price",
            "audience",
            "contact_or_signup",
        ],
        "default_purpose": "promote_convert",
    },
    "internal_notice": {
        "aliases": ["通知", "放假", "返岗", "值班", "公告"],
        "minimal_questions": [
            "time_arrangement",
            "back_to_work_time",
            "contact",
            "required_action",
        ],
        "default_purpose": "notify_sync",
    },
    "training_notice": {
        "aliases": ["培训", "内训", "课程通知"],
        "minimal_questions": [
            "topic",
            "time",
            "location",
            "audience",
            "contact",
        ],
        "default_purpose": "notify_sync",
    },
    "service_reminder": {
        "aliases": ["提醒", "预约", "会员", "服务", "体测"],
        "minimal_questions": [
            "service_name",
            "deadline",
            "audience",
            "price_or_free",
            "booking_entry",
        ],
        "default_purpose": "notify_sync",
    },
    "meeting_notice": {
        "aliases": ["会议通知", "开会", "参会"],
        "minimal_questions": [
            "topic",
            "time",
            "location_or_link",
            "audience",
            "contact_or_prep",
        ],
        "default_purpose": "notify_sync",
    },
    "weekly_report": {
        "aliases": ["周报", "汇报", "工作汇报", "项目推进"],
        "minimal_questions": [
            "time_range",
            "completed_work",
            "current_risks",
            "next_steps",
            "audience",
        ],
        "default_purpose": "notify_sync",
    },
    "meeting_followup": {
        "aliases": ["会议纪要", "会后同步", "follow-up", "followup"],
        "minimal_questions": [
            "meeting_topic",
            "key_decisions",
            "action_items",
            "owners",
            "deadlines",
        ],
        "default_purpose": "notify_sync",
    },
    "hiring": {
        "aliases": ["招聘", "岗位", "投递", "jd"],
        "minimal_questions": [
            "role",
            "location",
            "responsibilities",
            "apply_channel",
            "platform",
        ],
        "default_purpose": "promote_convert",
    },
    "client_followup": {
        "aliases": ["客户", "跟进", "服务通知", "客服"],
        "minimal_questions": [
            "topic",
            "time_node",
            "target_user",
            "required_action",
            "contact",
        ],
        "default_purpose": "notify_sync",
    },
    "social_post": {
        "aliases": ["小红书", "朋友圈", "微博", "知乎", "发帖", "内容帖"],
        "minimal_questions": [
            "topic",
            "audience",
            "core_message",
            "style",
            "platform",
        ],
        "default_purpose": "share_express",
    },
    "video_packaging": {
        "aliases": ["B站", "抖音", "快手", "视频号", "简介", "配文", "标题"],
        "minimal_questions": [
            "topic",
            "platform",
            "core_hook",
            "tone",
            "cta_level",
        ],
        "default_purpose": "record_package",
    },
}

PLATFORMS: dict[str, dict[str, Any]] = {
    "xiaohongshu": {"aliases": ["小红书"]},
    "moments": {"aliases": ["朋友圈"]},
    "weibo": {"aliases": ["微博"]},
    "douyin": {"aliases": ["抖音"]},
    "zhihu": {"aliases": ["知乎"]},
    "bilibili": {"aliases": ["b站", "B站", "哔哩哔哩"]},
    "wechat_article": {"aliases": ["公众号", "微信公众号"]},
    "video_channel": {"aliases": ["视频号"]},
    "kuaishou": {"aliases": ["快手"]},
    "wechat_work": {"aliases": ["企业微信"]},
    "email": {"aliases": ["邮件", "邮箱"]},
    "sms": {"aliases": ["短信"]},
    "group_notice": {"aliases": ["家长群", "群通知", "社群"]},
}

PURPOSES: dict[str, list[str]] = {
    "notify_sync": ["通知", "同步", "提醒", "安排"],
    "promote_convert": ["推广", "报名", "预约", "转化", "获客"],
    "share_express": ["分享", "表达", "经验", "记录生活"],
    "interact_spread": ["互动", "传播", "评论", "讨论"],
    "record_package": ["包装", "简介", "封面", "记录"],
}

DISPLAY_MODES = {"default", "expanded"}
OUTPUT_FORMATS = {"markdown", "json"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Copy workflow runner.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("template", help="Print request template.")

    classify = sub.add_parser("classify", help="Infer scene/platform/purpose.")
    add_common_input_args(classify)
    add_optional_classification_args(classify)

    prompt = sub.add_parser("prompt", help="Build an agent prompt packet.")
    add_common_input_args(prompt)
    add_optional_classification_args(prompt)
    prompt.add_argument("--display-mode", default="default", choices=sorted(DISPLAY_MODES))
    prompt.add_argument("--output-format", default="markdown", choices=sorted(OUTPUT_FORMATS))

    validate_request = sub.add_parser("validate-request", help="Validate a request file.")
    validate_request.add_argument("--file", required=True)

    validate_response = sub.add_parser("validate-response", help="Validate a response file.")
    validate_response.add_argument("--file", required=True)

    return parser


def add_common_input_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--raw", help="Raw input string.")
    parser.add_argument("--input-file", help="Path to a raw input file.")


def add_optional_classification_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--scene", choices=sorted(SCENES.keys()))
    parser.add_argument("--platform", dest="platforms", action="append", choices=sorted(PLATFORMS.keys()))
    parser.add_argument("--purpose", choices=sorted(PURPOSES.keys()))


def read_raw_text(args: argparse.Namespace) -> str:
    if args.raw:
        return args.raw.strip()
    if args.input_file:
        return Path(args.input_file).read_text(encoding="utf-8-sig").strip()
    raise SystemExit("Provide --raw or --input-file.")


def load_json_file(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def normalize_text(text: str) -> str:
    return text.lower().replace(" ", "")


def infer_scene(raw_text: str, explicit_scene: str | None) -> str:
    if explicit_scene:
        return explicit_scene
    normalized = normalize_text(raw_text)
    best_scene = "social_post"
    best_score = -1
    for scene, meta in SCENES.items():
        score = sum(1 for alias in meta["aliases"] if alias.lower() in normalized)
        if score > best_score:
            best_scene = scene
            best_score = score
    return best_scene


def infer_platforms(raw_text: str, explicit_platforms: list[str] | None) -> list[str]:
    if explicit_platforms:
        return explicit_platforms
    normalized = normalize_text(raw_text)
    detected: list[str] = []
    for platform, meta in PLATFORMS.items():
        if any(alias.lower() in normalized for alias in meta["aliases"]):
            detected.append(platform)
    return detected


def infer_purpose(raw_text: str, scene: str, explicit_purpose: str | None) -> str:
    if explicit_purpose:
        return explicit_purpose
    normalized = normalize_text(raw_text)
    for purpose, aliases in PURPOSES.items():
        if any(alias.lower() in normalized for alias in aliases):
            return purpose
    return SCENES[scene]["default_purpose"]


def missing_fields(scene: str, platforms: list[str]) -> list[str]:
    missing = list(SCENES[scene]["minimal_questions"])
    if platforms and "platform" in missing:
        missing.remove("platform")
    return missing


def request_template() -> dict[str, Any]:
    return {
        "raw_input": "Write your raw request here.",
        "scene": None,
        "platforms": [],
        "purpose": None,
        "display_mode": "default",
        "output_format": "markdown",
    }


def validate_request_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload.get("raw_input"), str) or not payload["raw_input"].strip():
        errors.append("raw_input must be a non-empty string.")
    scene = payload.get("scene")
    if scene is not None and scene not in SCENES:
        errors.append("scene is invalid.")
    platforms = payload.get("platforms", [])
    if not isinstance(platforms, list) or any(platform not in PLATFORMS for platform in platforms):
        errors.append("platforms must be a list of known platform keys.")
    purpose = payload.get("purpose")
    if purpose is not None and purpose not in PURPOSES:
        errors.append("purpose is invalid.")
    if payload.get("display_mode", "default") not in DISPLAY_MODES:
        errors.append("display_mode must be default or expanded.")
    if payload.get("output_format", "markdown") not in OUTPUT_FORMATS:
        errors.append("output_format must be markdown or json.")
    return errors


def validate_response_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = [
        "scene",
        "platforms",
        "purpose",
        "display_mode",
        "missing_fields",
        "final_recommended_copy",
        "backup_versions",
        "human_check_items",
    ]
    for key in required:
        if key not in payload:
            errors.append(f"missing key: {key}")
    if payload.get("display_mode") not in DISPLAY_MODES:
        errors.append("display_mode must be default or expanded.")
    if not isinstance(payload.get("platforms", []), list):
        errors.append("platforms must be a list.")
    if not isinstance(payload.get("missing_fields", []), list):
        errors.append("missing_fields must be a list.")
    if not isinstance(payload.get("human_check_items", []), list):
        errors.append("human_check_items must be a list.")
    return errors


def build_prompt_packet(raw_text: str, scene: str, platforms: list[str], purpose: str, display_mode: str) -> str:
    platform_list = ", ".join(platforms) if platforms else "not specified"
    intake = ", ".join(missing_fields(scene, platforms))
    if display_mode == "default":
        output_contract = (
            "Return only: final recommended copy, backup versions, and human-check items."
        )
    else:
        output_contract = (
            "Return: structured brief, draft copy, review result, and human-check items."
        )
    return f"""Use the copy-workflow at:
D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-workflow.md

Scene: {scene}
Platforms: {platform_list}
Purpose: {purpose}
Display mode: {display_mode}

Raw input:
{raw_text}

If required information is missing, ask only about:
{intake}

Output contract:
{output_contract}

Always run the internal chain:
brief -> draft -> review -> human-check

Respect the request contract:
D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-request.schema.json

Respect the response contract:
D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-output.schema.json
"""


def handle_template() -> int:
    print(json.dumps(request_template(), ensure_ascii=False, indent=2))
    return 0


def handle_classify(args: argparse.Namespace) -> int:
    raw_text = read_raw_text(args)
    scene = infer_scene(raw_text, args.scene)
    platforms = infer_platforms(raw_text, args.platforms)
    purpose = infer_purpose(raw_text, scene, args.purpose)
    result = {
        "scene": scene,
        "platforms": platforms,
        "purpose": purpose,
        "minimal_questions": SCENES[scene]["minimal_questions"],
        "missing_fields": missing_fields(scene, platforms),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def handle_prompt(args: argparse.Namespace) -> int:
    raw_text = read_raw_text(args)
    scene = infer_scene(raw_text, args.scene)
    platforms = infer_platforms(raw_text, args.platforms)
    purpose = infer_purpose(raw_text, scene, args.purpose)
    packet = {
        "scene": scene,
        "platforms": platforms,
        "purpose": purpose,
        "display_mode": args.display_mode,
        "missing_fields": missing_fields(scene, platforms),
        "agent_instruction": build_prompt_packet(raw_text, scene, platforms, purpose, args.display_mode),
    }
    if args.output_format == "json":
        print(json.dumps(packet, ensure_ascii=False, indent=2))
    else:
        print(packet["agent_instruction"])
    return 0


def handle_validate_request(args: argparse.Namespace) -> int:
    payload = load_json_file(args.file)
    errors = validate_request_payload(payload)
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"ok": True}, ensure_ascii=False, indent=2))
    return 0


def handle_validate_response(args: argparse.Namespace) -> int:
    payload = load_json_file(args.file)
    errors = validate_response_payload(payload)
    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"ok": True}, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "template":
        return handle_template()
    if args.command == "classify":
        return handle_classify(args)
    if args.command == "prompt":
        return handle_prompt(args)
    if args.command == "validate-request":
        return handle_validate_request(args)
    if args.command == "validate-response":
        return handle_validate_response(args)
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
