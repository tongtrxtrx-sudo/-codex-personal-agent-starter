---
name: image-workflow
description: Use when the user wants one-step image workflow processing from raw visual needs to visual brief, prompt directions, review notes, and human-check items.
---

# Goal
Run the full image workflow from raw visual needs to review-ready direction output without making the user call each underlying skill manually.

# Use When
- the user wants image workflow in one sentence
- the task is visual direction exploration for posters, covers, or campaign visuals
- the expected result should include visual brief, directions, and review, not just one prompt

# Do Not Use When
- the user explicitly wants only prompt writing or only brand review
- the task is final graphic design execution
- the brand owner must directly approve every visual decision before exploration

# Required Output
Always return these 4 parts in order:
1. `visual brief`
2. `prompt directions`
3. `brand review`
4. `human-check items`

# Internal Flow
1. Use [visual-brief-extractor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/visual-brief-extractor/SKILL.md)
2. Use [image-prompt-generator](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-prompt-generator/SKILL.md)
3. Use [brand-checker](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brand-checker/SKILL.md)

# Execution Rules
1. Start from raw visual requirements.
2. Use [visual-brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/visual-brief-extractor/assets/visual-brief-template.json) for brief structure.
3. Use [image-direction-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-prompt-generator/assets/image-direction-template.md) for direction output.
4. Use [brand-review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brand-checker/assets/brand-review-checklist.md) for review.
5. Enforce [image-brief-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-brief-required-fields.md) and [image-direction-quality-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-direction-quality-rules.md).
6. Keep final direction choice and brand-sensitive decisions for human confirmation.

# Example Invocation
`显式使用 $image-workflow。按图片 workflow 处理下面需求，输出 visual brief、3个视觉方向、brand review、待确认项。`
