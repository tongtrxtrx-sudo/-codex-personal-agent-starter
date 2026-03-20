---
name: brief-extractor
description: Use when messy campaign or content requirements need to be turned into a structured brief before copy generation or review.
---

# Goal
Turn raw business input into a stable structured brief for downstream copy work.

# Use When
- the request mixes dates, prices, audience, channels, selling points, and tone in free text
- downstream copy needs reusable structured fields
- the team wants one source of truth across multiple channels

# Do Not Use When
- the user already gave a complete structured brief
- the task is final copy editing only
- facts are missing and the user expects invention

# Input Requirements
- raw request, notes, or chat transcript
- must-keep facts such as dates, prices, contacts, audience, and tone
- unclear or missing items must stay empty or `null`

# Output Requirements
Return a fixed structure with fields such as:
- `campaign_name`
- `date_range`
- `deadline`
- `audience`
- `core_selling_points`
- `tone`
- `must_include`
- `forbidden`
- `channels`

# Execution Rules
1. Preserve dates, prices, and contacts verbatim.
2. Do not invent missing facts.
3. Use `null` or empty lists for unknowns.
4. Prefer structured output over prose.
5. Surface contradictions before handing off downstream.

# Success Criteria
- key facts are preserved
- the brief is reusable by downstream skills
- missing facts are visible instead of guessed

# Suggested Template
Use [brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brief-extractor/assets/brief-template.json) as the default structure when the input is still messy.

# Risk Boundaries
- never fabricate offers, prices, dates, or contacts
- escalate contradictory or policy-sensitive inputs to a human
