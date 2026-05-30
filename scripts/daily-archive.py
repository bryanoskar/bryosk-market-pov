#!/usr/bin/env python3
"""
Daily archive job for BryOsk Market PoV.

Runs in GitHub Actions on a daily cron schedule. Its job:
  1. Read the current index.html and extract the DATA fields
     (dateLong, riskScore, riskLabel, bottomLine).
  2. Check archive/metadata.json — if today's date is already archived, no-op.
  3. Otherwise:
       - Copy index.html → archive/YYYY-MM-DD.html
       - Prepend a new entry to archive/metadata.json
       - Update lastUpdated.
  4. GitHub Actions commits and pushes any changes.

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

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archive_file = ARCHIVE_DIR / f"{today}.html"

    meta = json.loads(METADATA_JSON.read_text(encoding="utf-8"))
    existing_dates = {e.get("date") for e in meta.get("entries", [])}

    if today in existing_dates:
        print(f"Already archived for {today}; no-op.")
        return 0

    # Snapshot today's main page
    shutil.copy(INDEX_HTML, archive_file)

    excerpt = strip_tags(bottom_line)
    new_entry = {
        "date": today,
        "dateLong": date_long or today,
        "riskScore": risk_score,
        "riskLabel": risk_label,
        "bottomLineExcerpt": excerpt[:500],
        "file": f"{today}.html",
    }

    # Newest first
    meta.setdefault("entries", []).insert(0, new_entry)
    meta["lastUpdated"] = today
    if "since" not in meta and meta["entries"]:
        meta["since"] = meta["entries"][-1].get("date", today)

    METADATA_JSON.write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Archived {today}: risk {risk_score}/100 — {date_long}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
