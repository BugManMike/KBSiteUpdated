---
type: Runbook
title: Printer fixed IP assignment
description: Reserving a static IP for a printer in UniFi and then pinning the same address on the device itself, so ManageEngine can deploy it without manual installs.
tags: [unifi, printers, network]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

**Why a fixed IP:** a printer that always sits at the same address can be deployed through
ManageEngine, so nobody has to install it on each computer by hand.

The address is set **twice** — once reserved on the network, once pinned on the device. That
is deliberate redundancy and prevents address conflicts.

> **When handling IP addresses you may need to reboot networks and devices** before one will
> accept the address you want to make static. This happens when another device currently holds
> the address you are trying to use.

# 1. Reserve the address on the network

1. Open `unifi.ui.com` and sign in with your UniFi Site ID. If you do not have a UniFi ID or
   the right permissions, consult the company system administrator.
2. Select the **Dream Machine Pro 12460** device.
3. On the left, click **UniFi Client Devices**.
4. Locate the printer in the client list. Clicking it opens a settings panel on the right.
5. Click the **Gear** icon to open **device settings**.
6. Give the device an alias in the form
   `Printer - Common name (Make Model #)`, where the common name is the room, department or
   primary user — something that makes it easy to find in the office. **Copy this name down**;
   it is reused later.
7. **Add to Printer group** in the group section.
8. Under IP settings, **check Fixed IP Address**. Use the current address or choose another.
   **Keep printers in sequential IP order.** Check the
   [Device Inventory](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/edit?gid=776411787#gid=776411787&range=A1)
   sheet for addresses already in use.

> If you cannot tell which printer you are working with, its IP address is under **Machine
> Info** on the device's LCD panel. Some models locate this differently.

# 2. Pin the same address on the device

1. Open the device interface at its fixed IP, e.g. `http://192.168.1.200`. You must be on-site
   and on the company network.
2. Click the **Network** tab at the top.
3. Click **Wired**.
4. The page should open on **TCP/IP (Wired)** settings; if not, click it on the left.
5. Enter the fixed IP you reserved above into the IP address field — it looks like
   `192.168.1.###`. Usually the address already present is the one you want to make fixed.
6. Subnet mask **255.255.255.0**, gateway **192.168.1.1**. These are the defaults.
7. **Change the Boot method to static.** That is the most important part.
8. **Submit**.

> **This block exists twice in the source and the two copies have diverged.** An earlier copy,
> under the printer setup walkthrough, gives six steps and omits the **Network** tab click at
> step 2, opening straight at *Wired* → *TCP/IP settings*. It also states "You had previously
> set a fixed IP address on the router", implying the reverse order to the one documented here.
> The eight-step version above is the later and fuller of the two. **IT should delete one copy**
> — as it stands, two procedures for the same task disagree on the click path and the order of
> operations.

# Known printer addresses

The source records these in a scratch issues list rather than in the printer documentation:

| Address | Note |
|---|---|
| 192.168.1.200 | Matthew Ulrich printer |
| 192.168.1.201 | Katy printer |
| 192.168.1.202 | |
| 192.168.1.203 | |
| 192.168.1.204 | |

> **Do not treat this as the inventory.** It is an undated working list, three of the five rows
> are unlabelled, and one printer is identified by a person's name rather than a location or
> asset. The
> [Device Inventory](https://docs.google.com/spreadsheets/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/edit?gid=776411787#gid=776411787&range=A1)
> spreadsheet is the system of record. Recorded here only because the two may disagree.

# Related

- [Brother printer setup](/it/printers/brother-printer-setup.md)
- [ManageEngine printer deployment](/it/printers/manage-engine-deployment.md)
