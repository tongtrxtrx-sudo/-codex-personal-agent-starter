---
name: brand-checker
description: Use when image directions, prompts, or visual headlines need a brand-fit and audience-fit review before adoption.
---

# Goal
Review visual directions for brand alignment, audience fit, and avoidable low-quality signals.

# Use When
- multiple creative directions need ranking
- teams worry about cheap, noisy, or off-brand outputs
- poster headlines and prompt directions need a final filter

# Do Not Use When
- no visual directions exist yet
- formal brand governance requires an official approver
- the task is to generate prompts from scratch

# Input Requirements
- candidate visual directions or prompts
- visual brief
- known brand tone and audience expectations

# Output Requirements
Return:
- recommended direction
- reasons for selection
- risk notes
- suggested revisions

# Execution Rules
1. Evaluate trust, clarity, audience fit, and brand tone first.
2. Flag over-cartoon, over-promotional, cluttered, or cheap-looking directions.
3. Check whether overlay titles are too long or too salesy.
4. Prefer actionable revisions over generic criticism.
5. Keep human approval explicit.

# Success Criteria
- the safest and strongest direction is easy to choose
- revision advice is concrete
- obvious brand mistakes are caught before design execution

# Suggested Checklist
Use [brand-review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brand-checker/assets/brand-review-checklist.md) for consistent review.
Also consult [image-brief-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-brief-required-fields.md) and [image-direction-quality-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-direction-quality-rules.md).

# Risk Boundaries
- never claim a direction is fully approved by the brand owner
- do not override explicit brand rules with personal taste
