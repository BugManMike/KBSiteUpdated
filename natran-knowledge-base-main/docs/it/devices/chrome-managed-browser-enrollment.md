---
type: Runbook
title: Chrome managed browser enrollment
description: How Chrome on company Windows devices is enrolled into cloud management via an Endpoint Central registry configuration, and how to confirm a device is enrolled.
tags: [chrome, devices, deployment]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Managed browsers allow Chrome policies to be applied to company-owned Windows devices.
Enrollment is a registry key written by Endpoint Central.

# Inspect the existing setup

`endpointcentral.manageengine.com` → **Configurations** → **All Configurations** → open
**Managed Browser Enrollment for Google Chrome**.

# How it was configured

1. **Configurations** at the top.
2. **Configuration → Windows** in the sidebar under *Add Configuration*.
3. Hover **Registry** → **Computer Configuration**.
4. Name it **Managed Browser Enrollment for Google Chrome**.
5. Registry Configuration type: **Manually**.
6. Action: **Write Value**.
7. **Header Key:** `HKEY_LOCAL_MACHINE`
8. **Sub-Key:** `SOFTWARE\Policies\Google\Chrome`
9. **Value Name:** `CloudManagementEnrollmentToken`
10. **Value Data:** the enrollment token from
    `admin.google.com/ac/chrome/browsers/` → **Enroll**. Requires Google Workspace admin.

# Confirm enrollment

- On the device, open `chrome://policy/` in Chrome and look for
  `CloudManagementEnrollmentToken`. The value resembles
  `5db2f5fe-3999-4999-8444-e31f292f9`.
- Or check `admin.google.com/ac/chrome/browsers/` for the device. Newly enrolled devices can
  take a few hours to appear.

> **Open item in the source.** The document records an unresolved question about whether all
> users are on managed browsers, with a Google support case opened against it. Treat
> organisation-wide enrollment as unverified.

# Related

- [Software deployment packages](/it/devices/software-deployment-packages.md)
- [Context-Aware Access](/it/google-workspace/context-aware-access.md) — requires the
  Endpoint Verification Chrome extension
