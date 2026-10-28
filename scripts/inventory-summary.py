#!/usr/bin/env python3
"""Summarise a network device inventory CSV (starter learning template).

Reads inventory-template.csv next to this script's parent folder and
prints counts by device type and by status, plus rows that need
attention. It never changes the CSV and never touches a network device.

Usage: python scripts/inventory-summary.py
"""

import csv
from collections import Counter
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "inventory-template.csv"

VALID_STATUSES = {"In use", "Spare", "Under repair", "Retired"}


def load_rows(path):
    """Read the inventory CSV and return a list of row dicts."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def find_attention_rows(rows):
    """Return human-readable notes for rows that need attention."""
    notes = []
    seen_ids = set()
    for row in rows:
        device = row.get("device_id", "").strip() or "(no id)"
        if device in seen_ids:
            notes.append(f"{device}: device_id is listed more than once.")
        seen_ids.add(device)
        status = row.get("status", "").strip()
        if status not in VALID_STATUSES:
            notes.append(f"{device}: unknown status '{status}'.")
        if status == "In use" and not row.get("ip_address", "").strip():
            notes.append(f"{device}: marked 'In use' but has no IP address.")
        if not row.get("location", "").strip():
            notes.append(f"{device}: no location recorded.")
    return notes


def main():
    rows = load_rows(CSV_PATH)
    print(f"Devices in inventory: {len(rows)}")
    print("\nBy device type:")
    for device_type, count in sorted(Counter(r["device_type"] for r in rows).items()):
        print(f"  {device_type}: {count}")
    print("\nBy status:")
    for status, count in sorted(Counter(r["status"] for r in rows).items()):
        print(f"  {status}: {count}")
    attention = find_attention_rows(rows)
    print("\nNeeds attention:")
    if attention:
        for note in attention:
            print(f"  - {note}")
    else:
        print("  None — every row has a known status and a location.")


if __name__ == "__main__":
    main()
