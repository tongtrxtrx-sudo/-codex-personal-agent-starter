---
name: ppt-brief-extractor
description: Use when messy project or reporting notes need to become a structured presentation brief before outlining slides.
---

# Goal
Convert scattered reporting input into a structured presentation brief for slide planning.

# Use When
- the team knows the topic but the presentation logic is still loose
- raw notes mix goals, metrics, budget, audience, and timeline
- a PPT outline needs a stable input structure

# Do Not Use When
- a clear presentation brief already exists
- the task is final slide wording only
- key business numbers are missing and cannot be guessed

# Input Requirements
- raw project notes
- audience and meeting purpose when known
- must-include facts and metrics

# Output Requirements
Return fields such as:
- `presentation_goal`
- `audience`
- `core_message`
- `success_metrics`
- `budget`
- `channels`
- `timeline`
- `must_include`

# Execution Rules
1. Separate facts from assumptions.
2. Keep numbers unchanged.
3. Use `null` for unknowns.
4. Optimize for a future outline, not for slide prose.
5. Surface missing decision-making inputs early.

# Success Criteria
- the brief supports a coherent slide outline
- key facts are preserved
- missing information is explicit

# Risk Boundaries
- never fabricate metrics, budget, or deadlines
- do not bury unresolved assumptions in polished language
