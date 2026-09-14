---
type: Runbook
title: Apple device assignment
description: Assigning an iPhone or iPad to an employee in Jamf Now — naming, blueprint, user assignment, and the notes and inventory records that go with it.
tags: [jamf, devices, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1-ELuT1r_4h9ASE8cWg_boPfnpsTHCrhZL0ypQnNUr80
    resource: https://docs.google.com/document/d/1-ELuT1r_4h9ASE8cWg_boPfnpsTHCrhZL0ypQnNUr80/edit
    title: Assigning iPhone and iPads devices in JAMF
status: draft
---

Apple devices are managed in **Jamf Now** (`login.jamfnow.com`). A **blueprint** is a
collection of settings assigned by branch and role; assigning one is what installs the apps.

# 1. Update the device inventory sheet

In the
[Device Inventory Sheet](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/edit#gid=1095740877),
note when the device is being checked out, who it is assigned to, and any notable conditions.
Retain the sheet on the device inventory clipboard.

# 2. Power on the device

If the device is new or recently erased, run the initial setup first — see
[Apple device self-service setup](/it/devices/apple-device-self-service-setup.md) Step 1 — then
come back here.

# 3. Assign in Jamf Now

1. Sign into `login.jamfnow.com`.
2. **Devices** → search by serial number. With the device in hand you can find the serial:
   - tap the info icon in the lower-right of the lock screen, which shows serial, IMEI and more; or
   - if the device is already set up, open Settings and search "serial number".
3. Select the device to open its dashboard — device name, settings, and three tabs
   (Dashboard, Details, Notes).
4. **⋯** in the upper corner → **Edit Name**. Use a name like `John Smith iPhone`.
   **Check the box to apply this name to the device.**
5. **Assign Blueprint** in the Blueprint box — pick the blueprint matching their branch and
   role.
6. **Assign device** → enter the user's name and **company email address** → **Assign Device**.
7. **Notes** tab → add a note recording who it went to, your name and the date. For example:
   *"Device assigned to John Smith. - Mike 3/21/22"*.

Once the device syncs with Jamf Now all the apps install automatically. The user finishes up
with [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md).

# "Unenrolled. Details may be out of date"

Expected, not an error. The device enrols itself when it is turned on and the user completes
the self-service setup.

# Related

- [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md)
- [Apple device erase](/it/devices/apple-device-erase.md)
- [AT&T SIM activation](/it/devices/att-sim-activation.md)
- [Device QR code labels](/it/devices/device-qr-code-labels.md)
