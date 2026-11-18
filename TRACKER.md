# Project Activity Tracker

Purpose
- Keep a chronological, human-readable record of what happens from the beginning to the end of the project.
- Serve as both a changelog and lightweight incident/decision log.

How to use
- Add a new entry for meaningful events: design decisions, major code changes, environment changes, tests, errors, deployments, handoffs.
- Use the helper script `scripts/tracker.py` to append entries (recommended) or edit this file by hand.

Entry format
- Each entry is a markdown block with the following fields. Prefer using the helper script to ensure consistent formatting.

Example entry (auto-generated)

---
ID: 0001
Date: 2026-01-04T12:34:56Z
Actor: Alice
Action: Created tracker files
Status: done
Related: scripts/tracker.py, TRACKER.md
Tags: init, docs

Description:
Created a project tracker and helper script to append entries.
---

Guidelines
- ID: sequential zero-padded number (e.g., 0001, 0002).
- Date: ISO 8601 UTC timestamp (the helper script writes this automatically).
- Actor: who made the change (initials or name).
- Action: short verb phrase (e.g., "Added tests", "Fixed bug in loader").
- Status: planned | in-progress | done | blocked
- Related: filenames or issues this entry references.
- Tags: comma-separated short tags for filtering.

Searching & filtering
- Use your editor search to find tags, actors, or filenames.
- If you prefer a machine-readable log later, we can add a JSON/CSV export tool.

Maintenance tips
- Keep entries concise but clear.
- Use the helper script for consistent timestamps and IDs.
- Reserve manual edits for corrections or bulk imports.

Contact
- If you want additional automation (e.g., Git hooks to append entries automatically on commits), ask and I'll add a minimal implementation.
