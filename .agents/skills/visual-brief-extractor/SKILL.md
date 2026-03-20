---
name: visual-brief-extractor
description: Use when raw marketing or campaign requirements need to be translated into structured visual directions before image prompting.
---

# Goal
Translate messy marketing input into a structured visual brief that a prompt generator can use reliably.

# Use When
- a poster, cover, or key visual direction is still vague
- teams disagree on style, scene, or brand tone
- image prompting keeps failing because the brief is too loose

# Do Not Use When
- a complete visual brief already exists
- the task is to review finished visuals only
- the model is expected to invent brand rules with no source

# Input Requirements
- campaign context
- target audience
- desired mood, scene, and brand tone
- must-show and must-avoid elements when available

# Output Requirements
Return a structure with fields such as:
- `subject`
- `audience`
- `scene`
- `style_keywords`
- `brand_tone`
- `primary_colors`
- `must_show_elements`
- `text_overlay`
- `negative_constraints`

# Execution Rules
1. Convert vague wording into explicit visual fields.
2. Leave unsupported items as `null`.
3. Separate positive direction from negative constraints.
4. Keep text overlay factual and short.
5. Surface missing brand inputs early.

# Success Criteria
- downstream prompting has enough detail to start
- visual intent is explicit and reusable
- avoidable ambiguity is reduced

# Suggested Template
Use [visual-brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/visual-brief-extractor/assets/visual-brief-template.json) as the default structure for image workflow inputs.

# Risk Boundaries
- do not invent official brand colors or rules
- do not turn unsupported assumptions into mandatory constraints
