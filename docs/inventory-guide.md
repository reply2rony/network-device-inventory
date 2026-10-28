# Network Device Inventory — guide

A starter guide for a small-office network device inventory. Keep it
simple: if a column does not apply to a device, leave it blank rather
than inventing a value.

## Columns in `inventory-template.csv`

| Column | What to put in it |
| ------ | ----------------- |
| `device_id` | Your own short ID, for example `SW-01`. Keep it unique. |
| `device_type` | Router, Switch, Access Point, Printer, or Firewall — or another plain type name. |
| `location` | The room or site where the device sits, in your own words. |
| `status` | `In use`, `Spare`, `Under repair`, or `Retired`. |
| `ip_address` | The device's address on your own network, if it has one. |
| `serial_number` | Only if you need it for warranty or support calls. |
| `notes` | Anything useful: who looks after it, or what it connects to. |

## Statuses, in plain words

- **In use** — installed and serving users right now.
- **Spare** — working, kept aside for a swap-in.
- **Under repair** — sent away or waiting for a fix; do not count it
  as available until it is back and tested.
- **Retired** — removed from service. Keep the row for history, but
  never list a retired device as if it were still in use.

## Monthly review routine

1. Walk the rooms and check that every "In use" device is really
   where the inventory says it is.
2. Update the status of anything that moved, broke, or was replaced.
3. Mark anything removed from service as "Retired" instead of
   deleting the row — the history is useful later.
4. Run `python scripts/inventory-summary.py` and follow up every
   row it flags as needing attention.
5. Store the updated CSV with your other IT documents, and never
   publish the real version in a public place.

## What this template is not

- It is not a network scanner and it does not discover devices.
- It is not a monitoring tool and it does not check whether a
  device is online.
- It does not store passwords, and it must never be used to store
  any credential.
