---
type: Runbook
title: Apple device erase and unassign
description: Wiping a returned iPhone or iPad — retaining anything needed first, resetting the blueprint, renaming and unassigning, erasing, and updating inventory.
tags: [jamf, devices, offboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1wR0Ei-vdA57vnWJKnORMJBKMB6Ze5RurUx1rHNjtYms
    resource: https://docs.google.com/document/d/1wR0Ei-vdA57vnWJKnORMJBKMB6Ze5RurUx1rHNjtYms/edit
    title: Erase and unassign iPhone, iPad and iOS devices
status: draft
---

Six steps, and **Step 4 cannot be undone**. Do Steps 1 to 3 first.

# 1. Retain anything needed

Most documents are backed up in the cloud, but review the device before erasing. **Speak with
management first** about anything that may need manual backup.

To get into the device, remove its passcode:

1. Sign into `login.jamfnow.com`.
2. Find the device by device name, employee name or serial number.
3. Click the device name to open its profile.
4. **More Options** (three dots, upper right).
5. **Unlock Device** — this temporarily removes the passcode.

# 2. Set the blueprint to Default

Each device carries a blueprint matching the employee's role. Deactivating means resetting it.

1. Open the device profile in Jamf Now.
2. **Assign Blueprint**.
3. Select **Default** → **Assign Blueprint**.

Most apps will disappear from the device. That is expected.

# 3. Note, unassign and rename

**Note the changes.** Notes tab → record when the device was wiped, any known defects or
issues, and your own name.

**Unassign.** **More Options** → **Unassign Device** → confirm with the red **Unassign**
button.

**Rename.** **More Options** → **Edit Name** → change it to
`Unassigned. Device erased 1/15/22`, using the actual erase date.

# 4. Erase — cannot be undone

1. Make sure the device is **turned on**.
2. **More Options** → **Erase Device**.
3. Red **Erase** button to confirm.
4. Confirm it completed. It may take a few minutes; you will know it is done when the new
   device setup screen appears.

# 5. Update the inventory spreadsheet

In the
[Device Inventory spreadsheet](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/):

- Device name → `Unassigned. Device erased MM/DD/YY`
- Status → **Inventoried**
- Notes → when it was returned and who the previous user was

> The notes matter more than they look: they are what tells you the device's history when it is
> reissued to a technician taking over a route.

# 6. Power down and return

1. Power the device off.
2. Make sure it is **fully charged**.
3. Update and complete the
   [Device Inventory History Sheet](https://docs.google.com/document/d/1IQ0t9Ue7p23tjPS4YFnAvAOQgzacnswpD7K3Hv3M4Ok/).
4. Return it to inventory.

> **Two inventory records, one device.** Step 5 updates a spreadsheet and Step 6 updates a
> separate "Device Inventory History Sheet", which is a Google **Doc**, not a sheet, despite the
> name. Whether both are still maintained is unclear. Separately,
> [Windows device user removal](/it/devices/windows-device-user-removal.md) has **HR** updating
> the inventory spreadsheet rather than IT. IT and HR to agree on who owns which record.

# Related

- [Apple device assignment](/it/devices/apple-device-assignment.md)
- [Chromebook assignment](/it/devices/chromebook-assignment.md)
