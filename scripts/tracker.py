"""Simple tracker appender

Usage examples (PowerShell):
  python .\scripts\tracker.py --actor Alice --action "Created tracker" --description "Initial tracker file and script" --status done --related TRACKER.md

The script appends a new entry to TRACKER.md with a sequential ID and ISO timestamp.
"""
import argparse
from datetime import datetime, timezone
from pathlib import Path

TRACKER_PATH = Path(__file__).resolve().parents[1] / 'TRACKER.md'


def next_id(content: str) -> str:
    # Find existing IDs in the file and return next zero-padded ID
    import re
    ids = re.findall(r"^ID:\s*(\d+)", content, flags=re.MULTILINE)
    if not ids:
        return '0001'
    max_id = max(int(i) for i in ids)
    return f"{max_id+1:04d}"


def make_entry(entry_id: str, actor: str, action: str, description: str, status: str, related: str, tags: str) -> str:
    ts = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = ["---",
             f"ID: {entry_id}",
             f"Date: {ts}",
             f"Actor: {actor}",
             f"Action: {action}",
             f"Status: {status}",
             f"Related: {related}",
             f"Tags: {tags}",
             "",
             "Description:",
             description.strip(),
             "---",
             ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Append an entry to TRACKER.md')
    parser.add_argument('--actor', required=True, help='Actor name')
    parser.add_argument('--action', required=True, help='Short action description')
    parser.add_argument('--description', default='', help='Longer description')
    parser.add_argument('--status', default='done', choices=['planned','in-progress','done','blocked'], help='Status')
    parser.add_argument('--related', default='', help='Related files or IDs')
    parser.add_argument('--tags', default='', help='Comma-separated tags')
    args = parser.parse_args()

    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    if TRACKER_PATH.exists():
        content = TRACKER_PATH.read_text(encoding='utf-8')
    else:
        content = ''

    entry_id = next_id(content)
    entry = make_entry(entry_id, args.actor, args.action, args.description, args.status, args.related, args.tags)

    with TRACKER_PATH.open('a', encoding='utf-8') as f:
        f.write(entry)

    print(f"Appended entry ID {entry_id} to {TRACKER_PATH}")


if __name__ == '__main__':
    main()
