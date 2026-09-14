---
type: Reference
title: Microsoft 365 provisioning
description: How Workspace users are automatically provisioned into Microsoft Entra, how they sign in, and the deletion case that needs manual cleanup.
tags: [microsoft-365, google-workspace, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Microsoft accounts are **not created by hand**. Users are provisioned automatically from
Google Workspace by a web app.

The app lives at `admin.google.com` → **Apps** → **Web and Mobile Apps** → search for
**Microsoft Office 365**.

- Creating a user in Workspace creates them in **Microsoft Entra**.
- Deleting a user in Workspace deletes them in Microsoft — **usually**. Sometimes it does not,
  and the user must be deleted manually. There is no security exposure when this happens: with
  the primary Workspace account gone the user cannot authenticate or reach any data.

# How users sign in

Users with Workspace accounts reach Microsoft with their Google credentials. They enter their
email, select **Work Account**, and are pushed to a Google sign-in screen to authenticate.

# Admin consoles

| Console | Use |
|---|---|
| `admin.microsoft.com` | Adding software licenses — e.g. purchasing Microsoft Office for a user with a specific need. |
| `entra.microsoft.com` (formerly Azure) | Other admin items. **Largely unused**, since the organisation runs on Google Workspace. |

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
- [Account offboarding](/it/google-workspace/account-offboarding.md)
