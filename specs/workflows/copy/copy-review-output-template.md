# Copy Review Output Template

## Goal
Force review output to explain both the recommendation and the rejection logic, not just list problems.

## Required Sections

```md
## Review Summary
- Overall status:
- Main risk:

## Problems
1. ...
2. ...

## Fix Suggestions
1. ...
2. ...

## Recommended Version
- Title / main version:
- Reason:
  - Most complete
  - Most stable
  - Best fit for current scene

## Not Recommended
- Version:
- Reason:
  - Too long
  - Missing critical fact
  - Tone mismatch

## Next Edit Priority
1. What should be fixed first
2. What can wait

## Human Check Items
- ...
- ...
```

## Use When
- There are multiple title versions
- There are multiple body versions
- The user did not specify a preference
- One version is clearly safer or more usable than the others
