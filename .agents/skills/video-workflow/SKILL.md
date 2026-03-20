---
name: video-workflow
description: Use when the user wants one-step video workflow processing from raw campaign needs to topic angles, script, storyboard review, and human-check items.
---

# Goal
Run the full video workflow from raw campaign needs to shootable review-ready output without making the user call each underlying skill manually.

# Use When
- the user wants video workflow in one sentence
- the task is short-form video planning, not direct editing
- the expected result should include angle selection, script, and storyboard review

# Do Not Use When
- the user explicitly wants only a hook list or only a script
- the task is final editing, filming, or publishing automation
- specialist compliance approval is required before drafting

# Required Output
Always return these 4 parts in order:
1. `video angles`
2. `script draft`
3. `storyboard review`
4. `human-check items`

# Internal Flow
1. Use [video-angle-generator](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/video-angle-generator/SKILL.md)
2. Use [script-writer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/script-writer/SKILL.md)
3. Use [storyboard-reviewer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/storyboard-reviewer/SKILL.md)

# Execution Rules
1. Start from raw campaign or content needs.
2. Produce multiple angles before locking one script.
3. Keep dates, prices, contacts, and CTA consistent across script and storyboard.
4. Do not skip the review layer.
5. Keep publish approval and final posting decisions for human confirmation.

# Example Invocation
`显式使用 $video-workflow。按视频 workflow 处理下面需求，输出选题方向、脚本、分镜审校、待确认项。`
