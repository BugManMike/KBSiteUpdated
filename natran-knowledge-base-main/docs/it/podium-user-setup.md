---
type: Runbook
title: Podium user setup
description: Inviting a technician to Podium and mapping their Fieldroutes user ID so review requests are attributed to the right person.
tags: [podium, onboarding, marketing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1Tk8u1ulMgQZUc0_KH4KB6mcjVsDeSWCp9CDGrr_ZVTs
    resource: https://docs.google.com/document/d/1Tk8u1ulMgQZUc0_KH4KB6mcjVsDeSWCp9CDGrr_ZVTs/edit
    title: Add to Podium
status: draft
---

Podium solicits customer reviews and surveys. A technician can send a review request manually; if
no review is captured, **Podium automatically sends a request the next day** asking the customer
to rate the service on a 1–10 scale.

**Reviews are published publicly** on Google, Facebook and similar. **Survey feedback is internal
only.** That distinction matters when deciding what to send a customer.

Two steps, and the second requires the first to be complete.

# Step 1 — Invite the user

The Podium app installs automatically on their company device when they receive it.

1. Log into `podium.com`.
2. Gear icon in the upper-right corner.
3. **Add your team**.
4. **Invite User** → enter the user's email address.
5. Select **Team Members** for any technician role. Other roles are assigned per the user's role
   in the company — consult the system admin if unsure.
6. Select the appropriate **location**.
7. **Send Invitations**.

# Step 2 — Map the Fieldroutes user ID

Without this, review requests are not attributed to the technician who did the work.

**The user must already exist in Fieldroutes** — see
[Fieldroutes user setup](/it/fieldroutes-user-setup.md).

**Find their Fieldroutes ID:**

1. Log into `natrangreen.pestroutes.com`.
2. **Confirm you are in the correct office** — shown in the lower-right corner. Click to switch.
3. **Admin** in the upper right → click the user.
4. Copy the user ID next to their name. Roughly five digits, e.g. `10755`.

**Enter it in Podium:**

1. Sign into `podium.com`.
2. **More** in the upper left → **Settings**.
3. **Users** → **All Users**.
4. The button in the upper-right corner → **Map Integration User IDs**.
5. Select **Pestroutes SSI** from the integration dropdown → **Continue**.
6. Enter each user's Fieldroutes ID next to their name. **Each user has a unique ID.**
7. **Save**.

> The integration is named **"Pestroutes SSI"** in Podium's own dropdown. That is a vendor-side
> label, so it will keep saying PestRoutes regardless of what this bundle settles on — relevant to
> the naming question in
> [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md).

> Step 4 of both halves refers to an unnamed button shown only in a screenshot, which did not
> survive conversion.

# Related

- [Fieldroutes user setup](/it/fieldroutes-user-setup.md)
- [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md)
