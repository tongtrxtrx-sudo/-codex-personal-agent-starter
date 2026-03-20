---
name: ppt-workflow
description: Use when the user wants one-step PPT workflow processing from raw notes to presentation brief, outline, slide draft, and human-check items.
---

# Goal
Run the full PPT workflow from raw notes to a presentation-ready structure without making the user call each underlying skill manually.

# Use When
- the user wants PPT workflow in one sentence
- the task is presentation logic and content drafting
- the expected result should include brief, outline, and slide content

# Do Not Use When
- the user explicitly wants only slide beautification
- the task is final executive sign-off wording only
- key facts and metrics are missing and cannot be guessed

# Required Output
Always return these 4 parts in order:
1. `presentation brief`
2. `deck outline`
3. `slide draft`
4. `human-check items`

# Internal Flow
1. Use [ppt-brief-extractor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/ppt-brief-extractor/SKILL.md)
2. Use [deck-outliner](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/deck-outliner/SKILL.md)
3. Use [slide-writer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/slide-writer/SKILL.md)

# Execution Rules
1. Start from raw presentation notes, not polished assumptions.
2. Keep numbers, names, dates, and metrics unchanged.
3. Build logic before writing detailed slide text.
4. Keep speaker notes separate from on-slide text.
5. Leave final business judgment and approval for human confirmation.

# Example Invocation
`显式使用 $ppt-workflow。按 PPT workflow 处理下面需求，输出 presentation brief、目录结构、页面初稿、待确认项。`
