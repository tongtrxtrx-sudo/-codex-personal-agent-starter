---
name: file-triage
description: "Trigger when the user wants to organize a folder, group files by type, batch rename, or preview a file cleanup plan. Batch move, rename, or delete actions must start with a dry-run and require confirmation before execution."
---

# Goal
Organize a local directory safely and predictably without causing irreversible changes before the user confirms.

# Use When
- the user wants to organize Downloads or another local folder
- the user wants files grouped by type
- the user wants to preview planned moves
- the user wants batch renaming for local files

# Mandatory Safety Rules
- Default to dry-run only.
- Show the plan and wait for confirmation before any batch move, rename, or delete action.
- Do not delete files by default.
- If the rules are unclear, stop and ask instead of guessing.
- If the script is used, do not add `--apply` until the user confirms.

# Recommended Flow
1. Read `references/rules.md`.
2. Confirm the target directory.
3. Run a dry-run and show the plan.
4. Wait for confirmation before applying changes.
5. Summarize the result:
   - how many files moved
   - which files were skipped
   - which naming conflicts required suffixes

# Suggested Script
Dry-run:
`uv run python .agents/skills/file-triage/scripts/triage.py ~/Downloads`

Apply after confirmation:
`uv run python .agents/skills/file-triage/scripts/triage.py ~/Downloads --apply`

# Do Not Use When
- the user only wants to search file contents
- the task is knowledge organization rather than filesystem organization
- the target directory is still unclear
