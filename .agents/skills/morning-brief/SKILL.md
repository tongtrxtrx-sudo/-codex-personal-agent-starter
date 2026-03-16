---
name: morning-brief
description: "Trigger when the user wants a short daily brief, startup summary, or immediate priority view for today. Do not trigger for deep research, long-form reporting, or real calendar synchronization."
---

# Goal
Generate a short, clear, and immediately actionable morning brief from local project context.

# Preferred Inputs
Read these first:
- `memory/current_focus.md`
- `inbox/capture.md`

Read this only when it materially helps:
- `memory/profile.md`

# Use When
- the user asks for today's brief
- the user asks what to do first today
- the user wants help starting the day
- the user wants a priority summary from current local notes

# Do Not Use When
- the user wants a formal weekly or monthly report
- the user wants online news or live research
- the user wants real calendar data and no calendar tool is available

# Output Shape
Keep the result short. By default, stay within these sections:
1. top 3 priorities for today
2. small actions that fit in the next 30 minutes
3. follow-ups that may not need to happen today
4. risks or blockers
5. one recommended starting action

# Behavior Rules
- Do not invent calendar events.
- If the local context is thin, say that the brief is based only on local files.
- Prefer execution order over motivational language.
- Default to Chinese user-facing output.
- If the user asks for a minimal version, compress it to five lines or fewer.

# Suggested Template
See `assets/brief-template.md`.

# Optional Script
Use this for a fast first draft:
`uv run python .agents/skills/morning-brief/scripts/build_brief.py`

Treat script output as a draft that can be refined against the current context.
