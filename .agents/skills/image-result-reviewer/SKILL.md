---
name: image-result-reviewer
description: Use when generated images need to be checked against the brief, chosen direction, and brand expectations before final selection or another generation round.
---

# Image Result Reviewer

## Goal
Review actual generated image outputs and decide whether to accept, revise, or regenerate.

## Use When
- images have already been generated
- the team needs a concrete recommendation between accept, revise, or regenerate
- prompt-level review is no longer enough because real outputs now exist

## Do Not Use When
- no images exist yet
- the task is only to choose between abstract prompt directions
- a formal brand approver must make the decision without any pre-review

## Input Requirements
- generated image outputs
- approved visual brief
- selected direction
- generation config when available

## Output Requirements
Return:
- overall recommendation
- strongest output
- mismatch findings
- revision instructions
- human-check items

## Execution Rules
1. Compare the actual image to the approved brief first, not to personal taste.
2. Check subject clarity, scene match, brand fit, audience fit, and information-space usability.
3. Flag cheap-looking rendering, clutter, weak hierarchy, bad text handling, or drift from the chosen direction.
4. Distinguish between small fixes and full reruns.
5. Keep the final approval human.

## Success Criteria
- the next action is obvious: accept, revise, or regenerate
- findings are tied to the brief and direction
- revision advice is specific enough for another generation round

## Suggested Template
Use [image-result-review-template.md](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-result-reviewer/assets/image-result-review-template.md) for stable review output.

## Risk Boundaries
- do not claim the image is brand-approved
- do not confuse prompt quality with actual image quality
- do not hide material mismatches behind vague positivity
