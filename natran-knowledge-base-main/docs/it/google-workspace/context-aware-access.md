---
type: Policy
title: Context-Aware Access
description: The two access levels restricting Google Workspace to company-owned or admin-approved password-protected devices, what they require of a device, and how new policies are rolled out.
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

Google Workspace uses Context-Aware Access (CAA) to restrict the core applications — Gmail,
Drive, Calendar and so on. The primary policy ensures **only company-owned or explicitly
admin-approved devices** can reach company data. A secondary policy checks the device is
**secured with a password or passcode**.

# Access levels

| Name | Description |
|---|---|
| Compare-Owned and Approved User-Owned Devices | Blocks access to company data on any device not listed in company inventory or approved as a user-owned device. |
| Password required | Blocks access to company data if the device is not password protected. |

> **"Compare-Owned" is a typo for "Company-Owned"** in the source. Recorded as found because
> the string may be the literal access-level name in the admin console — in which case
> renaming it there would break references. IT to confirm.

# What the user experiences

- Company-owned devices, and approved password-protected personal devices, get a seamless
  Google experience.
- A device without a password, or any other unauthorised device, is **blocked**. A message
  appears in the browser explaining why access was denied and telling the user to contact the
  system administrator.

# Prerequisites for a device to pass

Both of these must be true:

1. **Endpoint Verification** — the user must reach Workspace through Google Chrome with the
   Endpoint Verification extension installed. The extension deploys automatically on sign-in.
2. **Native Helper app** — on Windows and Mac, the Endpoint Verification Native Helper
   (`EndpointVerification.msi`) must also be installed system-wide.

**Why the Native Helper is not optional:** the Chrome extension alone cannot read physical
hardware data. The Native Helper reads the physical BIOS serial number and passes it to
Workspace so it can be matched against the company-owned inventory. The MSI is deployed to
company-owned devices through ManageEngine Endpoint Central.

# The core access-level rule

An **Advanced Mode** access level groups conditions with `OR` logic.

- **Rule name:** Company-Owned OR Approved Devices
- **CEL expression:**
  `device.is_corp_owned_device == true || device.is_admin_approved_device == true`

# Rollout discipline

When applying a new CAA policy or adding an application to the restriction list:

- **Always use Monitor Mode first.** Apply the policy domain-wide in Monitor mode for
  **7–14 days**. This simulates the block and records it in the audit logs without disrupting
  the business.
- **Then Active Mode.** Once the logs have been audited and exceptions handled, switch to
  Active to enforce the hard block.
- **Turn on custom user messages.** Ensure Remediation messages are toggled **ON** so users
  receive Google's automated tips — for example "Install the Chrome extension" — and can
  unblock themselves before raising a ticket.

# Where policies are applied

- **Globally:** Security → Context-Aware Access → General Settings.
  - *Access levels for all Google-owned apps* applies policies to Google apps.
  - *Access levels for OAuth apps* applies policies to third-party apps using Google OAuth.
- **By app and Organizational Unit:** Security → Context-Aware Access → *Assign access levels
  to apps* in the Assign access level section.
  - App-level policies also let you **warn** users their device is out of compliance — a
    feature not available when policies are applied globally.

# Related

- [CAA device approval and troubleshooting](/it/google-workspace/caa-device-approval.md)
- [Device enrollment](/it/devices/endpoint-central-device-enrollment.md) — company-owned registration
- [Chrome managed browser enrollment](/it/devices/chrome-managed-browser-enrollment.md)
- [Admin account separation](/it/google-workspace/admin-account-separation.md)
