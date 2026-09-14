---
type: Runbook
title: Busylight setup
description: What to buy, which Plenom and Jabra software to install, and how to load the preset call-status light priorities.
tags: [busylight, devices, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 10pp7KBzbjSpYPYMXb_N1UUne1y_wHHQB3tSnYkMkrNA
    resource: https://docs.google.com/document/d/10pp7KBzbjSpYPYMXb_N1UUne1y_wHHQB3tSnYkMkrNA/edit
    title: Busylight Setup
status: draft
---

A Busylight is a status light showing whether someone is on a call. It mounts on a shelf or
wall — **not a monitor**.

# Purchasing

| Item | Note |
|---|---|
| Busylight | Mounts on a shelf or a wall, not a monitor |
| Extension cord | Only if mounting the light further than 9 ft away |

Both are ordered from Amazon; the source links specific listings.

# Software

**Plenom** (`plenom.com/downloads/download-software/`) — install:

- Google Calendar
- Kuando In-A-Call
- Kuando Hub
- Jabra GN

**Jabra Direct** (`jabra.com/software-and-services/jabra-direct`) — **only if the user has a
Jabra headset.**

# Load the preset priorities

Priorities decide which colour wins when more than one status applies.

1. **Platform Priorities**
2. **Restore Priorities**
3. Upload
   [the priorities file](https://drive.google.com/file/d/1dWFKABGDDZEmXOfK0Ski0Ua2k3hPcDay/view)
4. Verify the priorities appear correctly
5. Edit **Manual Controls** to allow all options **except "off"**

> **Step 5 is the point of the whole configuration.** Allowing everything except *off* means a
> user can change their light but cannot switch it off — which is what makes the light
> trustworthy to a colleague walking past.

# Creating custom priorities

1. **Platform Priorities**
2. **Priority Assistant**
3. Follow the prompts
4. Test that the light behaves as intended
5. Edit **Manual Controls** to allow all options **except "off"**

> The priorities file is a JSON backup stored in the wiki's `Technology/Resources` folder. It is
> a binary asset, not documentation, so it is not reproduced here — the link above is the only
> copy. If it is ever lost, the custom-priorities route above is the fallback.

> Step 4 of the preset route says to "verify priorities appear like so" and Step 5 references an
> interface screenshot. Both images are lost, so there is no reference for what correct looks
> like.

# Related

- [Windows PC setup](/it/devices/windows-pc-setup.md)
