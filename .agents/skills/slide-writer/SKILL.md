---
name: slide-writer
description: Use when a slide outline needs concise page content and speaker notes without turning slides into long paragraphs.
---

# Goal
Write concise slide content and speaker notes from a reviewed deck outline.

# Use When
- the page structure is already decided
- teams need usable slide text fast
- a presenter needs short notes for each page

# Do Not Use When
- the slide outline is still unstable
- the task is visual design or formatting only
- the meeting requires final executive approval on every sentence

# Input Requirements
- reviewed deck outline
- any wording constraints
- must-keep metrics, dates, and names

# Output Requirements
Return per slide:
- title
- short on-slide points
- optional chart guidance
- speaker notes

# Execution Rules
1. Keep on-slide text concise.
2. Put supporting explanation into speaker notes.
3. Preserve all fixed numbers and names exactly.
4. Write for presentation, not report prose.
5. Keep slides readable at a glance.

# Success Criteria
- slide text is clear and short
- speaker notes help the presenter explain the page
- the output can be dropped into a deck with minimal rewriting

# Risk Boundaries
- do not turn uncertain assumptions into hard claims
- do not treat generated slides as final leadership-approved material
