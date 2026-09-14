---
type: Runbook
title: Software deployment packages
description: How to add a software package to Endpoint Central for deployment, and which software targets which device group.
tags: [manage-engine, devices, deployment]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

# Create a package

1. **Package Deployment** at the top.
2. **Add Package** → select **Windows**.
3. Name the package.
4. Select **MSI** or **EXE**.
5. License Type is **commercial**.
6. Location Installable → **From Local Computer** → select the file.
7. **Add Package**.

Packages are stored on a local network share served by a Raspberry Pi — see
[Zoho software repository](/it/network/zoho-software-repository.md).

# Deployment targets

| Software | Target |
|---|---|
| Teramind | `WORKGROUP` |
| Steam | Custom Group (Natran Shared Services) |

> **Two things to check here.** First, this table has only two rows while the source's
> surrounding sections describe deploying Teramind, Chrome, GCPW and printer packages —
> so it is incomplete rather than exhaustive. Second, **Steam** is listed as deployed to
> Natran Shared Services; it is not obviously a business application, and may be a leftover
> test entry. IT to confirm whether that deployment is intentional.

# Chrome web apps

Chrome web apps are deployed for:

- Google Meet
- Google Calendar
- Gmail
- Chat
- Fieldroutes
- Call Tracking Metrics
- Google Drive
- Linear or Kanbanchi
- Hubspot

> **Unresolved in the source.** "Linear or Kanbanchi" records an undecided choice between two
> tools rather than a deployed state. Separately, the source notes as an open problem that
> Chrome apps can be added but not pinned to the taskbar. Neither is settled documentation.

# Related

- [Teramind agent deployment](/it/devices/teramind-agent-deployment.md)
- [Chrome managed browser enrollment](/it/devices/chrome-managed-browser-enrollment.md)
- [Configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md)
