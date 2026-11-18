# TRACKER.md — How to use

Files created
- `TRACKER.md` — the human-readable project activity tracker.
- `scripts/tracker.py` — convenience script to append consistent entries.

Quick usage (PowerShell)

Run the script with required fields:

```powershell
python .\scripts\tracker.py --actor "Your Name" --action "Added tests" --description "Added unit tests for loader" --status done --related loader.py --tags tests,unit
```

Examples
- Add a design decision:
  python .\scripts\tracker.py --actor Bob --action "Decided on DB" --description "Use ChromaDB for local experiments" --status done --tags design,db

- Add a work-in-progress note:
  python .\scripts\tracker.py --actor Alice --action "Working on ingestion" --description "Partial import script ready" --status in-progress --related ingestion.py --tags import

Notes
- The script creates sequential zero-padded IDs (0001, 0002...).
- Timestamps are recorded in UTC ISO 8601.
- If you prefer manual edits, follow the format in `TRACKER.md` exactly.

Next improvements (optional)
- Add a Git commit hook to require a tracker entry when certain files change.
- Add an export command to produce CSV or JSON.
- Add a small UI (local web page) to browse entries.

If you'd like any of those, tell me which one to implement next.
