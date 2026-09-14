---
type: Reference
title: Endpoint Central configuration catalogue
description: The standing ManageEngine configurations applied to company Windows devices, the device groups they target, and how often each reapplies.
tags: [manage-engine, devices, security]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Configurations live in Endpoint Central under **Configurations → All Configurations**. They
are assigned to device groups and reapply on the agent refresh cycle.

# Standing configurations

| Configuration | What it does | Groups | Frequency |
|---|---|---|---|
| On-Demand: Manually Activate Windows Default Administrator Account | Activates the hidden Windows administrator account so admin-level changes can be made manually when no active Windows account has admin rights. | n/a | Once (on demand) |
| On-Demand: Manually Deactivate Windows Default Administrator Account | Deactivates the administrator account. | n/a | Once (on demand) |
| Automatically Disable Windows Default Administrator Account | Deactivates the administrator account whenever the agent checks in. A security measure, because the account requires no password. | All Windows OS Workstations (not server) — includes all Windows devices | Every refresh cycle; approximately every 2 hours or on reboot |
| Deploy Teramind Agent Virus Exclusions | Exempts Teramind from Windows Defender so it is not flagged as a virus. Applied to all devices whether or not the Teramind agent is installed. | All Windows OS Workstations (not server) | Every refresh cycle |
| Deploy Teramind Agent | Installs the Teramind Agent. | *(blank in source)* | *(blank in source)* |
| Disable Windows 11 Widgets | Disables Widgets on the Windows taskbar. | All Windows OS Workstations (not server) | n/a |

> **Source defect.** The *Deploy Teramind Agent* row has empty Groups and Frequency cells.
> The Teramind deployment procedure states the target is Domain → `WORKGROUP` and the policy
> is *Deploy any time at the earliest* — see
> [Teramind agent deployment](/it/devices/teramind-agent-deployment.md). The table has not
> been updated to match. IT to confirm which is authoritative.

# Device groups

**Dynamic groups**

| Group | Membership |
|---|---|
| All Windows OS Workstations (not server) | Automatically includes all Windows devices. Configurations meant for every device belong here — for example BitLocker encryption enforcement. |
| Leadership | Top-level leadership devices. |
| Shared Service Group | All inside sales and customer service. Carries Teramind. |

**Department custom groups**

| Group | Description | Printer |
|---|---|---|
| Leadership | | By request |
| Accounting Group | | |
| Houston Operations | | |
| Human Resources | | |
| Marketing | | |
| Shared Services | | |

> **Source defect.** The department group table's Description and Printer columns are
> almost entirely empty, and a separate "Master Group" list in the same source contains
> literal placeholder entries `2` and `3` alongside real ones (BitLocker, Windows Security
> Exemptions for Teramind). The department groups above are recorded as found; treat the
> blank cells as unwritten rather than as "no printer" or "no description".

# Policies

- **BitLocker encryption is turned on for all computers** and the recovery key is retained
  in Endpoint Central.
- **Patch deployment** installs 7 days after release, force-installs after 30 days if not
  yet patched, prompts the user to install, and prompts the user to reboot.

> **Source defect.** The patching schedule appears only in a scratch issue list in the
> source, not in the policies section, and sits among unresolved questions. It reads as
> settled ("Patching deployment has been setup") but has not been promoted into the
> documented policy set. IT to confirm.

# Related

- [Windows default administrator account](/it/devices/windows-default-administrator-account.md)
- [Teramind agent deployment](/it/devices/teramind-agent-deployment.md)
- [Device enrollment](/it/devices/endpoint-central-device-enrollment.md)
