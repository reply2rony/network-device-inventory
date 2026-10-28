# Network Device Inventory

A simple starter template for keeping a small-office network device
inventory: one row per device, kept in a plain CSV file, plus a small
starter script that summarises it.

## What it is
- `inventory-template.csv` — one row per device (type, location,
  status, and a few identification fields). Sample data only; replace
  it with your own inventory.
- `docs/inventory-guide.md` — how to fill in each column, what each
  status means, and a short monthly review routine.
- `scripts/inventory-summary.py` — reads the inventory CSV and prints
  a summary: how many devices of each type, how many in each status,
  and which rows need attention (for example, a device marked
  "Retired" that is still listed as in use, or a row with a missing
  field).
- `docs/diagram.png` — a generated Sample / Demo diagram of the
  inventory flow. It is an illustration, not a screenshot of a real
  system, and it does not show any real company system or data.

## How to use it (no code)
1. Copy `inventory-template.csv` and delete the sample rows.
2. Add one row per device, following `docs/inventory-guide.md`.
3. Once a month, work through the review routine in the guide and
   update any row whose status or location has changed.

## How to use it (with Python)
1. Install Python 3 — no extra packages needed.
2. In a terminal, go to this folder and run:
   `python scripts/inventory-summary.py`
3. Read the summary it prints. It does not change your CSV and it
   does not touch any network device.

## Sample data note
All device names, locations, serial numbers, and IP addresses in the
sample file are made up, including the private-range addresses used
as examples. Never put real employee data, real system names, real
serial numbers, or real credentials in a public repository.

## Note on skills
Python is labelled "Learning" in the author's profile. This script is
an intentionally short, commented starter learning template for IT
support work, and the CSV and guide versions work without it. No CCTV
content is used as experience here, and no performance numbers are
claimed.
