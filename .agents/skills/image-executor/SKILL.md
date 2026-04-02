---
name: image-executor
description: Use when a visual direction has already been chosen and the task is to generate, edit, or iterate actual images with OpenAI image APIs while preserving generation settings and outputs.
---

# Image Executor

## Goal
Turn an approved visual direction into actual generated image outputs with reproducible settings and saved metadata.

## Use When
- a team has already chosen one visual direction
- the next step is real image generation or editing, not more direction exploration
- output settings, revised prompts, and generated files must be preserved for later review

## Do Not Use When
- the brief is still vague
- no direction has been approved yet
- the task requires final human graphic design production

## Input Requirements
- approved visual brief
- selected direction with prompt and negative prompt
- output constraints such as size, quality, format, and transparency when known
- reference images or masks when editing is required

## Output Requirements
Return:
- generation config
- execution mode used
- saved output file paths or artifact references
- revised prompt when available
- notes for the next review round

## Execution Rules
1. Do not run generation until one direction is explicitly chosen by a human.
2. Use the Image API for one-shot generation or one-shot editing.
3. Use the Responses API with the image generation tool for conversational multi-turn image iteration.
4. Default to `gpt-image-1.5`; only drop to `gpt-image-1-mini` when faster, cheaper exploration is acceptable.
5. Persist generation settings, including model, size, quality, format, background, action, and reference inputs.
6. Record `revised_prompt` when the API returns it.
7. Keep generation separate from result approval.

## Success Criteria
- generated outputs can be traced back to an approved direction
- settings are explicit enough to rerun
- downstream review can compare result, prompt, and brief without guesswork

## Suggested Template
Use [generation-config-template.json](D:/work/myclaw/codex-personal-agent-starter/.agents/skills/image-executor/assets/generation-config-template.json) to keep execution records stable.

## Risk Boundaries
- do not treat the first generated image as final by default
- do not override explicit brand constraints for novelty
- do not skip human review after generation
