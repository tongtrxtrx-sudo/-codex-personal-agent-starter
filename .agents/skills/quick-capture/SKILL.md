---
name: quick-capture
description: "Trigger when the user mainly wants to save a thought, TODO, link, meeting note, rough draft, or temporary decision. Do not trigger for deep research, complex planning, code changes, or system operations."
---

# Goal
Capture fragmented input into `inbox/capture.md` with minimal information loss.

# Use When
- the user says things like "note this", "save this", "capture this", or "do not expand yet"
- the input is a fragment such as an idea, link, TODO, meeting note, or speech-to-text dump
- the main goal is preservation, not analysis

# Do Not Use When
- the task requires deep reasoning or solution design
- the task requires code edits, command execution, or filesystem operations
- the user explicitly wants a polished document

# Workflow
1. Classify the input as `idea`, `todo`, `note`, `decision`, or `link`.
2. Preserve the original wording when the meaning is ambiguous.
3. Append to `inbox/capture.md` instead of overwriting existing notes.
4. Keep a stable structure:
   - timestamp
   - type
   - tags
   - raw content
   - optional next action
5. If the user only asked to record something, finish with a short confirmation and stop.

# Suggested Format
See `assets/capture-template.md`.

# Optional Script
Use this only when a more reliable append flow is helpful:
`uv run python .agents/skills/quick-capture/scripts/append_capture.py`

Prefer direct editing for single entries. Use the script when repeated or structured appends are safer.
