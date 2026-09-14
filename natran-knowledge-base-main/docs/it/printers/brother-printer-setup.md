---
type: Runbook
title: Brother printer setup
description: Unboxing and configuring a new Brother MFC printer — network cabling, inventory, web sign-in, auto-updates, and the restriction settings that keep users out of device config.
tags: [brother, printers, devices]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

The organisation uses **Brother MFC series** printers for printing and scanning.

Setting up a printer end-to-end is three documents:

1. This one — physical setup and device configuration.
2. [Fixed IP assignment](/it/printers/fixed-ip-assignment.md) — reserving the address on the
   network and pinning it on the device.
3. [ManageEngine printer deployment](/it/printers/manage-engine-deployment.md) — pushing the
   printer to work devices.

# Unboxing

1. **Connect the device to the network with a standard Cat5 LAN cable. Do not use wifi** —
   wifi printing is unreliable and should be avoided.
2. Add the device to the [Device Inventory](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/edit?gid=776411787#gid=776411787&range=A1)
   spreadsheet under the **Printers** tab.

# Sign into the device

1. Enter the device IP address in a browser, e.g. `http://192.168.1.200`. **Device IPs are
   local only** — you must be on-site on the local network, or have direct VPN access.
2. On the device page click **Open Secure Login** at the top. If warned the connection is not
   private, click **Advanced** then **Proceed to the IP** link.
3. A login field appears at the top. Each Brother printer ships with a default password, found
   on the back of the printer or in the owner's manual.

> The source says "We will update that later" about the default password, and its
> **Update password** section is an empty numbered stub. **There is no documented procedure
> for changing a printer's default password.** Given these devices are reachable over the
> local network, IT should treat this as a gap rather than an omission.

# Turn on auto-updates

Devices receive firmware updates that can install themselves.

1. **Administrator** at the top of the screen.
2. **Firmware Update** on the left — confirm it is enabled. If not, select **Enabled** and
   **Submit**.
3. **Firmware Update Setup** on the left.
4. Set **Update Method** to **Auto Install** and accept the terms and conditions.
5. Update days: **Sunday, Wednesday, Friday** is sufficient. Update range **19:00 to 24:00**.
6. **Submit**.

# Restriction management

**Administrator** tab → **Restriction Management** on the left.

- **User restriction: Off.** This would require users to enter credentials before printing,
  scanning or copying. It is kept off so users have free use of the device.
- **Setting Lock: On.** This stops users changing device settings from the LCD panel. Kept on
  to prevent changes that disconnect the device from the network or otherwise break it.

**Setting Lock Details** — apply this table for consistency across the organisation:

| Setting | Enabled | Disabled |
|---|---|---|
| General Setup | ☑️ | ◻️ |
| Shortcut Settings | ☑️ | ◻️ |
| Fax | ◻️ | ☑️ |
| Printer | ☑️ | ◻️ |
| Network | ◻️ | ☑️ |
| Print Reports | ◻️ | ☑️ |
| Machine Info | ☑️ | ◻️ |
| Initial Setup | ◻️ | ☑️ |
| Service | ◻️ | ☑️ |
| Address Book | ◻️ | ☑️ |

> **Read the column headings carefully.** A ☑️ under *Enabled* means that setting group **is
> locked** — Setting Lock is what is being configured, so "enabled" is the lock, not the
> feature. The source does not spell this out and the table is easy to read backwards.

# Screenshots

This procedure was written against screenshots of the Brother web interface that did not
survive conversion. Field names and menu paths are transcribed, but the visual confirmation
steps are text-only here.

# Related

- [Fixed IP assignment](/it/printers/fixed-ip-assignment.md)
- [ManageEngine printer deployment](/it/printers/manage-engine-deployment.md)
- [Brother scanner to Drive](/it/printers/brother-scanner-to-drive.md)
