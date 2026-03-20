---
name: image-prompt-generator
description: Use when a structured visual brief needs to produce multiple usable creative directions and image prompts.
---

# Goal
Generate clear visual directions, prompts, and negative prompts from a structured visual brief.

# Use When
- the team needs 2-3 creative directions before design execution
- image generation requires better prompt discipline
- a poster or key visual concept must be explored quickly

# Do Not Use When
- the brief is still missing core audience or tone
- the task is to approve brand compliance only
- final design production requires a human designer's judgment

# Input Requirements
- structured visual brief
- required text overlay
- any brand or format constraints

# Output Requirements
Return for each direction:
- direction name
- short visual description
- main prompt
- negative prompt
- suggested headline or overlay idea

# Execution Rules
1. Produce clearly differentiated directions.
2. Keep prompts specific about subject, scene, style, and composition.
3. Use negative prompts to suppress cheap or off-brand outputs.
4. Keep overlay text concise.
5. Make every direction reviewable without generating images first.

# Success Criteria
- directions are distinct and understandable
- prompts are specific enough for reuse
- the team can choose a direction before spending design effort

# Suggested Template
Use [image-direction-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-prompt-generator/assets/image-direction-template.md) to keep direction outputs stable.
Also consult [image-brief-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-brief-required-fields.md) and [image-direction-quality-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-direction-quality-rules.md).

# Risk Boundaries
- do not promise final design quality from prompt text alone
- do not ignore brand or audience constraints to chase novelty
