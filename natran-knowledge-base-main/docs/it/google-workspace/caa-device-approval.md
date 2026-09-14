---
type: Runbook
title: CAA device approval and troubleshooting
description: What to do when a user hits the red "You don't have access" screen — reading the audit logs, fixing an inventory serial mismatch, or approving a legitimate personal device.
tags: [google-workspace, security, access-control]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

When a user reports a red **"You don't have access"** screen, work through these in order.
For the policies causing the block, see
[Context-Aware Access](/it/google-workspace/context-aware-access.md).

# 1. Check the audit logs

**Reporting → Audit and investigation → Context-Aware Access log events.**

Filter by the user's email to see *why* access was denied — missing Endpoint Verification, an
unregistered device, and so on. Do this first; it tells you which of the next two steps
applies.

# 2. Company-owned device being blocked — check the serial

If the device is company-owned but blocked, its serial number likely does not match the
inventory record.

The physical serial reported by the Native Helper must be an **exact, case-sensitive match**
to the record in **Devices → Mobile & endpoints → Company owned inventory**. When it matches,
Workspace auto-approves the device.

# 3. Legitimate personal device — approve it manually

A remote worker on a legitimate device that is not in inventory lands in the pending queue.

1. **Devices → Mobile & endpoints → Devices.**
2. Filter by **Status: Pending approval**.
3. Locate the user's device, verify it is legitimate, and click **Approve**.

Then have the user click the **Endpoint Verification** extension icon in Chrome and select
**Sync Now** to pull their new approved status immediately, rather than waiting.

# Related

- [Context-Aware Access](/it/google-workspace/context-aware-access.md)
- [Device enrollment](/it/devices/endpoint-central-device-enrollment.md)
