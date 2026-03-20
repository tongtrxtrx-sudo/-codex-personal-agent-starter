# WeChat Style Samples

## Goal

This folder stores exported `.eml` samples from WeChat chat history so they can be normalized and adapted into the repository's copy workflow.

## Directory Layout

- `raw-email/kindergarten-group/`
  - Group-chat samples from kindergarten parent groups
- `raw-email/parent-1on1/`
  - Important one-on-one parent conversations
- `normalized/`
  - Cleaned text extracted from `.eml` files
- `profile/`
  - Style summaries, phrase libraries, and workflow adaptation notes

## What To Export

Prefer exporting high-signal messages, not everything.

Recommended:

- 10 to 30 `.eml` files for kindergarten group announcements
- 10 to 30 `.eml` files for important one-on-one parent chats

Good samples usually contain:

- your real tone
- repeated sentence patterns
- reminders and notices
- soft emotional language
- teacher-parent communication style

## File Naming

Use readable names so batch processing is easier.

Recommended patterns:

- `2026-03-21-kindergarten-group-01.eml`
- `2026-03-21-kindergarten-group-02.eml`
- `2026-03-21-parent-1on1-01.eml`
- `2026-03-21-parent-1on1-02.eml`

## Notes

- `.eml` is the preferred source format.
- Try to keep one conversation export per file.
- If a message thread is especially important, keep it intact rather than editing it manually.
- Do not put private files anywhere outside this folder if you want them processed for style extraction later.

## Next Step

After you drop the `.eml` files here, the next processing flow will be:

1. extract message text from raw email
2. normalize timestamps, speakers, and content
3. group by scene and tone
4. build a reusable style profile
5. adapt the copy workflow rules
