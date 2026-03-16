# File Triage Rules

## Categories
- images: png, jpg, jpeg, webp, gif, svg
- video: mp4, mov, mkv, avi, webm
- audio: mp3, wav, m4a, flac
- docs: pdf, doc, docx, txt, md, ppt, pptx
- sheets: xls, xlsx, csv
- archives: zip, rar, 7z, tar, gz
- code: py, js, ts, json, yaml, yml, sh, html, css
- misc: everything else

## Default Strategy
- target layout: `<target>/_sorted/<category>/`
- no recursion by default
- never delete anything except the original file being moved
- add a numeric suffix when a destination name already exists
- always preview with dry-run first

## Cases That Need Human Confirmation
- the destination already contains many files with the same names
- the move crosses disks or volumes
- empty-directory cleanup is requested
- the desired organization is project-based instead of type-based
