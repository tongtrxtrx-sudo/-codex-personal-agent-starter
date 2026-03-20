---
name: copy-generator
description: Use when a structured campaign brief needs to be turned into channel-ready marketing or notification copy for multiple formats.
---

# Goal
Generate first-draft copy from a structured brief without losing key business facts.

# Use When
- a brief already exists and channels are known
- one campaign needs multiple copy variants
- the team wants a reusable draft before manual review

# Do Not Use When
- the source brief is incomplete or contradictory
- legal, policy, or contract language needs final wording
- the task is only to review existing copy

# Input Requirements
- structured brief from `brief-extractor`
- target channels and length expectations
- tone, must-include items, and forbidden expressions

# Output Requirements
Return channel-specific blocks such as:
- poster headlines
- social post copy
- group notice
- SMS or short notification

# Execution Rules
1. Keep prices, dates, deadlines, and contacts unchanged.
2. Match the requested channel and length.
3. Keep tone consistent with the brief.
4. Generate usable drafts, not final approvals.
5. Separate outputs clearly by channel and version.
6. Check channel-required fields and length guardrails before finalizing each channel block.

# Success Criteria
- each channel has a usable draft
- key facts are present in every required output
- the copy sounds consistent and not over-promotional

# Suggested Template
Use [copy-output-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-generator/assets/copy-output-template.md) to keep channel outputs stable.
Also consult [copy-channel-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-required-fields.md), [copy-channel-length-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-length-rules.md), [copy-title-templates.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-title-templates.md), and [copy-version-selection-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-version-selection-rules.md).

# Risk Boundaries
- do not add unsupported claims or guarantees
- do not remove mandatory facts to make copy shorter
