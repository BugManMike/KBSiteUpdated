---
type: Runbook
title: Fieldroutes user deactivation
description: Deactivating a Fieldroutes user and reassigning their open tasks, plus the reactivate-and-repeat trick for an urgent lockout.
tags: [fieldroutes, offboarding, crm]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
  - id: 1dJKq3vl0allP24Tctq347KaCzcGgnnK12zql_xtBxyE
    resource: https://docs.google.com/document/d/1dJKq3vl0allP24Tctq347KaCzcGgnnK12zql_xtBxyE/edit
    title: Deactivate Pestroutes Account
status: draft
---

Fieldroutes is the CRM. The Natran tenant is `natrangreen.fieldroutes.com`.

> **Naming: Fieldroutes and PestRoutes are the same system.** The IT documentation calls it
> Fieldroutes; the rest of the company wiki calls it PestRoutes throughout, and procedures
> elsewhere reference "Pestroutes" menus and permission profiles. The product was renamed. This
> bundle needs one tag value for it — flagged for you to settle, since retagging later is worse
> than choosing now.

# Deactivate a user

1. Open `natrangreen.fieldroutes.com`.
2. **Admin** in the upper-right corner.
3. Locate the user.
4. Click their name to open their account.
5. Click **de-activate** in the upper right, under where it says *Active*.
6. **Save**.
7. If prompted to reassign tasks, change all of them to the manager's name. **There is no bulk
   action — you have to do this one at a time.**
8. **Save**, then **Save** again to lock the user's screen.

# Urgent lockout

> If you need to deactivate an account **urgently**, you can skip the task reassignment:
> deactivate the account, skip reassignment, **change the password**, then reactivate. The
> tasks stay associated with the user, and you can now safely deactivate again and reassign
> tasks at your own pace.

The point is that changing the password locks them out immediately, so the slow one-at-a-time
task reassignment does not sit between you and the lockout.

# The wiki version: password first, always

A second source, the wiki's *"Deactivate Pestroutes Account"*, treats the password change as
**step one of the normal procedure** rather than an urgent-case shortcut, and adds a sequencing
rule the other source omits:

> **Suspend the user's Google account first. Otherwise they can reset their Fieldroutes password
> themselves** and undo the lockout.

That is the important line in either version. Fieldroutes password recovery goes to their email,
so locking Fieldroutes without locking email accomplishes nothing. See
[account offboarding](/it/google-workspace/account-offboarding.md).

**You need Fieldroutes admin permission** for any of this.

## Change the password

1. Log into `natrangreen.pestroutes.com`.
2. **Admin** in the upper-right corner.
3. Find the user in the list and **click their name** to open their employee card.
4. **Set** under **Password Reset** and enter a new password.

## Then deactivate

1. **Before deactivating, email the office managers** and ask them to clear any appointments,
   borders and visual groupings, and to reassign pending tasks.
2. From the same user card, click **De-Active** → **Save**.
3. **If you get a warning prompt, send it to the office managers** to address. The system blocks
   deactivation while anything from step 1 is still pending.

> **The two sources assign the cleanup work to different people.** The IT version has *you*
> reassigning tasks inside Fieldroutes, one at a time, when prompted. This version has you emailing
> **office managers** to clear appointments, borders and visual groupings and reassign tasks before
> you start. The second is more thorough — appointments, borders and visual groupings are not
> tasks and would not be caught by the reassignment prompt — but it depends on someone else acting
> first. IT and operations to agree who does what, because as written each version lets the other's
> work fall through.

# Related

- [Workspace account offboarding](/it/google-workspace/account-offboarding.md)
- [CTM offboarding](/it/telephony/ctm-offboarding.md)
