---
name: copy-workflow
description: Use when the user wants one-step copy processing from raw requirements to ready-to-use copy output with clear final check items.
---

# Goal
Run the full copy workflow from raw input to review-ready output without making the user call each underlying skill manually.

# Use When
- the user wants copy workflow in one sentence
- the input is raw campaign, notice, promotion, reminder, social post, or common work-scene requirements
- the expected result should include draft copy and review, not just a single final paragraph

# Do Not Use When
- the user explicitly wants to test only one underlying skill
- the task is legal, contract, or policy wording that needs specialist approval
- the user wants direct auto-publish behavior

# Output Modes
## Default Mode
Return only:
1. `final recommended copy`
2. `backup versions`
3. `human-check items`

## Expanded Mode
Only when the user explicitly asks to "show full workflow", "expand the chain", "use debug mode", or "show brief/draft/review", return:
1. `structured brief`
2. `draft copy`
3. `review result`
4. `human-check items`

# Internal Flow
1. Use [brief-extractor](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brief-extractor/SKILL.md)
2. Use [copy-generator](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-generator/SKILL.md)
3. Use [copy-reviewer](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-reviewer/SKILL.md)

# Execution Rules
1. Start from raw input, not assumptions.
2. Use [brief-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/brief-extractor/assets/brief-template.json) for the brief structure.
3. Use [copy-output-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-generator/assets/copy-output-template.md) for draft output shape.
4. Use [review-checklist.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/copy-reviewer/assets/review-checklist.md) for review.
5. Use [copy-review-output-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-review-output-template.md) for recommendation logic in review output.
6. Enforce [copy-channel-required-fields.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-required-fields.md) and [copy-channel-length-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-channel-length-rules.md).
7. Use [copy-title-templates.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-title-templates.md) and [copy-version-selection-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-version-selection-rules.md) when multiple versions are needed.
8. Identify the scene first, using [copy-scene-intake-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-scene-intake-rules.md).
9. If the task targets Xiaohongshu, Moments, Weibo, Douyin, Zhihu, or Bilibili, also enforce [copy-social-platform-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-social-platform-rules.md).
10. If the task is a common work scene, also enforce [copy-work-scene-rules.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-work-scene-rules.md).
11. Do not skip the review step.
12. Internally run the full workflow even when the user sees only default-mode output.
13. Keep unresolved facts and final approval items visible.
14. In default mode, hide intermediate nodes unless the user explicitly asks to expand them.

# Example Invocation
`显式使用 $copy-workflow。按文案 workflow 处理下面需求，默认只输出最终推荐版本、备选版本、待确认项；如果我说“展开链路”，再显示 structured brief、draft copy、review result。`
