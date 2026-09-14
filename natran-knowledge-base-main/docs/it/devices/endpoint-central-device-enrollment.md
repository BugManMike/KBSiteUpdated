---
type: Runbook
title: Windows device enrollment
description: The three things installed on a new company Windows device before any other setup happens, and how to find a device's computer name afterwards.
tags: [manage-engine, devices, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

A new company Windows device gets three things, in order. Everything else follows from the
third.

1. Register the device as **"company owned"** in Google Workspace.
2. Install **Google Credential Provider for Windows** (GCPW) — see
   [GCPW deployment](/it/devices/gcpw-deployment.md).
3. Install the **ManageEngine Endpoint Central agent**.

> **Registering as company-owned is not optional bookkeeping.** Context-Aware Access
> blocks company data on any device absent from the company-owned inventory, and the
> serial must match exactly. See
> [Context-Aware Access](/it/google-workspace/context-aware-access.md).

**The rest of the device setup should be performed through ManageEngine.** Once the agent
is installed, the device picks up group-assigned configurations on its own refresh cycle —
roughly every two hours, or on reboot. See
[configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md).

# Finding a device's computer name

Most configurations target a **computer name**, not a user. A device has many usernames but
exactly one computer name.

**From the device:** Windows search → *About your PC* → Device specifications → Device
name. Usually looks like `LAPTOP-XYZ123`.

**From Endpoint Central:** `endpointcentral.manageengine.com` → **Inventory** →
**Computers**. If the user is signed in, their name appears in the *Logged in User* column,
which is how you associate a person with a computer name.

# Related

- [Configuration catalogue](/it/devices/endpoint-central-configuration-catalogue.md)
- [Windows local account administration](/it/devices/windows-local-account-administration.md)
- [Software deployment packages](/it/devices/software-deployment-packages.md)
