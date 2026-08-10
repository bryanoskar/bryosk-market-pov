#!/usr/bin/env python3
"""
Daily archive job for BryOsk Market PoV.

Runs in GitHub Actions on a daily cron schedule. Its job:
  1. Read the current index.html and extract the DATA fields
     (dateLong, riskScore, riskLabel, bottomLine).
  2. Check archive/metadata.json — if that content's own date is already
     archived, no-op.
  3. Otherwise:
       - Copy index.html → archive/YYYY-MM-DD.html (named after the date
         found IN the content, not wall-clock "today")
       - Insert a new entry into archive/metadata.json, keep entries sorted
         newest-first, update lastUpdated.
  4. GitHub Actions commits and pushes any changes.

Deliberately does NOT require the content's date to equal wall-clock
"today" (UTC). The archive cron runs on a fixed schedule (00:10 UTC), but
the daily content-refresh automation runs on a separate, less predictable
schedule that can land before or after that fixed time. Requiring exact
equality created a silent permanent-skip failure mode: once the refresh
landed even once after the archive cron's fixed time, dateLong would
forever read as "yesterday" relative to whenever the cron fires, and the
guard would mismatch every single day after that (this happened for real
on 2026-08-08 and 2026-08-09). Filing each snapshot under its own claimed
date and deduping against archived dates (see the 2026-05-31 incident this
guard was originally added for) gets the same anti-mislabeling protection
without depending on the two schedules staying in lockstep.

Side effects: writes to archive/{today}.html and archive/metadata.json.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = REPO_ROOT / "index.html"
ARCHIVE_DIR = REPO_ROOT / "archive"
METADATA_JSON = ARCHIVE_DIR / "metadata.json"


def find_string(field: str, html: str) -> str | None:
    """Match `field:"value"` (allowing escaped quotes) inside the DATA object."""
    m = re.search(rf'\b{field}\s*:\s*"((?:\\.|[^"\\])*)"', html)
    if not m:
        return None
    # Unescape common JS string escapes
    return m.group(1).replace('\\"', '"').replace("\\\\", "\\")


def find_int(field: str, html: str) -> int:
    m = re.search(rf'\b{field}\s*:\s*(\d+)', html)
    return int(m.group(1)) if m else 0


def strip_tags(text: str) -> str:
    """Strip HTML tags and collapse whitespace."""
    no_tags = re.sub(r"<[^>]+>", "", text or "")
    return re.sub(r"\s+", " ", no_tags).strip()


def parse_date_long(s: str) -> str | None:
    """Convert 'Sunday, 31 May 2026' → '2026-05-31'. Returns None on parse failure."""
    if not s:
        return None
    try:
        dt = datetime.strptime(s, "%A, %d %B %Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return None


def main() -> int:
    if not INDEX_HTML.exists():
        print(f"ERROR: index.html not found at {INDEX_HTML}", file=sys.stderr)
        return 1
    if not METADATA_JSON.exists():
        print(f"ERROR: metadata.json not found at {METADATA_JSON}", file=sys.stderr)
        return 1

    html = INDEX_HTML.read_text(encoding="utf-8")
    date_long = find_string("dateLong", html) or ""
    risk_score = find_int("riskScore", html)
    risk_label = find_string("riskLabel", html) or ""
    bottom_line = find_string("bottomLine", html) or ""

    # Guard: the entry is filed under the date the CONTENT itself claims
    # (dateLong), not wall-clock "today". This is what actually prevents
    # mislabeling (stale content can never be saved under a fresher
    # filename than it claims), without requiring the archive cron and the
    # content-refresh automation to run in the same UTC calendar day.
    in_file_date = parse_date_long(date_long)
    if not in_file_date:
        print(f"ERROR: could not parse dateLong {date_long!r} into a date.", file=sys.stderr)
        return 1

    archive_file = ARCHIVE_DIR / f"{in_file_date}.html"

    meta = json.loads(METADATA_JSON.read_text(encoding="utf-8"))
    entries = meta.setdefault("entries", [])
    existing_dates = {e.get("date") for e in entries}

    if in_file_date in existing_dates:
        print(f"Already archived for {in_file_date}; no-op.")
        return 0

    # Snapshot the page under its own claimed date
    shutil.copy(INDEX_HTML, archive_file)

    excerpt = strip_tags(bottom_line)
    new_entry = {
        "date": in_file_date,
        "dateLong": date_long or in_file_date,
        "riskScore": risk_score,
        "riskLabel": risk_label,
        "bottomLineExcerpt": excerpt[:500],
        "file": f"{in_file_date}.html",
    }

    entries.append(new_entry)
    entries.sort(key=lambda e: e.get("date", ""), reverse=True)
    meta["lastUpdated"] = entries[0]["date"]
    if "since" not in meta and entries:
        meta["since"] = entries[-1].get("date", in_file_date)

    METADATA_JSON.write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Archived {in_file_date}: risk {risk_score}/100 — {date_long}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
