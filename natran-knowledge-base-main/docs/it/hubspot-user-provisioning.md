---
type: Runbook
title: Hubspot user provisioning
description: Creating a Hubspot user, adding them to teams, and choosing the right seat type for their role.
tags: [hubspot, onboarding, marketing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Hubspot is the marketing platform.

# Add a user

1. Open `hubspot.com`.
2. Gear icon in the upper right for **Settings**.
3. **Users & Teams** under *Account Management*.
4. **Add users** (orange button) → **Create New**.
5. Enter the new user's email address → **Next**.
6. Select the seat assignment — see the table below.
7. Select **User seat permissions** to set access.
8. **Next**.
9. Confirm details → **Create user**.
10. **Done**.

# Add a user to teams

1. **Teams** tab at the top.
2. Select the teams to add the user to. **If you cannot see your team, check whether it is
   nested inside another team.**
3. Click the team name.
4. Add the user to the team.
5. **Save**.

# Seat types

| Seat | Unlimited | User type | What it gives |
|---|---|---|---|
| View-Only | ✅ | Any | Look at data, reports and dashboards without changing anything. |
| Core | | Managers | The standard "editor" seat: create, edit and delete records — contacts, deals and so on — across the CRM. Also unlocks editing for the purchased Hubs, such as Marketing Hub or CMS. |
| Developer | ✅ | Developers | Dedicated access to Hubspot's developer platform: API keys, private apps, local development and sandboxes. |
| Sales Enterprise | | Inside Sales | Everything in Core, plus advanced sales productivity tools. |
| Service Professional | | *(unresolved)* | Everything in Core, plus advanced support tools. |

> **The Service Professional row has a literal `?` in the user-type column** in the source — it
> was never decided which roles get this seat. IT to fill in. Given customer care is the obvious
> candidate and currently has no listed seat type at all, this is a real gap rather than a
> cosmetic one.

**Unlimited** marks seats that do not consume a paid licence. Core, Sales Enterprise and
Service Professional do, so seat choice has a cost.

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
