---
type: Runbook
title: Chromebook assignment
description: Recording a Chromebook against an employee in the Workspace admin console and moving it into their organizational unit.
tags: [google-workspace, devices, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1w1ecIRITAeCJ28qYn0kMiRi3M4DvdqrY5XzWTPdzyUg
    resource: https://docs.google.com/document/d/1w1ecIRITAeCJ28qYn0kMiRi3M4DvdqrY5XzWTPdzyUg/edit
    title: Assign Chromebooks
status: draft
---

Chromebooks are managed directly in the Google Workspace admin console — not Jamf Now, not
ManageEngine.

# 1. Find and record the device

1. Sign into `admin.google.com`.
2. **Devices** → **Chrome** → **Devices**.
3. Select **Device Inventory** from the organizational units, or **All Devices**.
4. Select the device, or search using **Search or add a filter**.
5. Open the **Custom Fields** section:
   - enter the employee's name in the **User** field
   - update **notes** with something like *"Assigned to John Smith on 5/23/22"*

# 2. Move it to the user's organizational unit

**Move** → select the OU containing the assigned user → **Move**.

For example, a service manager in Houston goes to
**Regions → Houston Branch → Service Managers**. That OU structure is the same one used for
user accounts — see
[Workspace account provisioning](/it/google-workspace/account-provisioning.md).

# Erasing

The source points to a separate "Erase Chromebooks and ChromeOS devices" document. That
document sits in the wiki's `WIP` folder rather than with the other device procedures, and is
covered in a later ingestion batch.

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
- [Apple device assignment](/it/devices/apple-device-assignment.md)
