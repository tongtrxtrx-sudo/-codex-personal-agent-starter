---
name: copy-reviewer
description: Use when generated copy needs factual, tonal, and channel-fit review before a human approves external use.
---

# Goal
Review copy for factual completeness, tone consistency, and channel fitness before release.

# Use When
- first-draft copy already exists
- multiple channels must stay aligned
- external-facing copy needs a safer last check

# Do Not Use When
- there is no draft to review
- the task is to invent brand policy from scratch
- legal approval is required from a qualified person

# Input Requirements
- draft copy grouped by channel
- source brief
- known style constraints and forbidden phrases

# Output Requirements
Return:
- issue list
- corrected copy when fixes are obvious
- recommendation reasons
- explicit unresolved items that need human judgment

# Execution Rules
1. Check dates, prices, contacts, and deadlines first.
2. Flag exaggeration, missing facts, and inconsistent tone.
3. Review channel fit, especially headline length and SMS length.
4. Prefer specific corrections over vague comments.
5. Keep unresolved business decisions visible.
6. Review each channel against required-field and length guardrails, not just overall readability.

# Success Criteria
- factual problems are identified quickly
- copy quality improves without losing business intent
- the human reviewer knows exactly what still needs approval

# Suggested Checklist
Use [review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-reviewer/assets/review-checklist.md) for consistent factual and risk review.
Also consult [copy-channel-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-required-fields.md), [copy-channel-length-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-length-rules.md), [copy-title-templates.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-title-templates.md), and [copy-version-selection-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-version-selection-rules.md).
Use [copy-review-output-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-review-output-template.md) when multiple versions need explicit recommendation logic.

# Risk Boundaries
- never silently normalize incorrect facts
- never treat reviewed copy as approved for publication
