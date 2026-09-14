---
type: Runbook
title: 2-Step Verification
description: Checking whether a user has 2FA enabled, and the two different routes to getting it turned on depending on whether the account is more than two weeks old.
tags: [google-workspace, security, onboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1O5To1iDKll6qxcCgb5BsSGh-gl4_XZQ2q_ZcsMLzSkY
    resource: https://docs.google.com/document/d/1O5To1iDKll6qxcCgb5BsSGh-gl4_XZQ2q_ZcsMLzSkY/edit
    title: 2-Step verification setup
status: draft
---

Two-step verification requires a password plus a second factor, normally an SMS code.

**The two-week mark is what decides the procedure.** Inside two weeks of account creation the
user can set it up unaided. After that they are locked out of doing so and an admin has to issue
backup codes to get them in.

> A user who has not set up 2FA **will be locked out** of a company Windows device — see
> [Windows PC setup](/it/devices/windows-pc-setup.md) Step 5. Check this before handing a device
> over.

# Step 1 — Check the current state

1. Sign into `admin.google.com`.
2. Search the user's name and open their account.
3. **Security** tab.
4. Scroll to **2-Step Verification**.
   - **ON** — done, nothing further needed.
   - **OFF** — continue below.

# Step 2 — Within two weeks of account creation

The user can do this themselves:

1. Have them go to `myaccount.google.com` and sign in with their work account.
2. **Security** → **2-Step Verification** → follow the prompts to set up SMS using their **work
   phone number**.

# Step 3 — After two weeks

The admin issues backup codes so the user can get in far enough to set 2FA up properly.

**Admin, on the user's account page:**

1. **Security** tab → **2-Step Verification** → **Get Backup Verification Codes**.
2. Provide a code to the user.
3. Same tab → **Login challenge** → **Turn off for 10 mins**. This temporarily disables a
   security feature that would otherwise interfere.

**Then the user:**

4. Sign into `myaccount.google.com` using the backup code.
5. **Security** → **2-Step Verification** → follow the setup guide using their work phone's SMS.

> **The 10-minute window is tight** and covers both the sign-in and the 2FA setup. If it lapses,
> turn the Login challenge off again rather than assuming something else failed.

# Step 4 — Confirm

Admin re-checks: open the user's account → **Security** → **2-Step Verification** → confirm it
reads **ON**.

# Backup code length

Google's backup codes are **8 digits**, and both this procedure and
[account offboarding](/it/google-workspace/account-offboarding.md) treat them that way.

> Note for anyone reading the IT single-source-of-truth: that document calls them "seven digit"
> in one step and "8-digit" two steps later. **Eight is correct** — corroborated here and in the
> wiki's own offboarding procedure.

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
- [Account offboarding](/it/google-workspace/account-offboarding.md) — uses backup codes to reach a departing user's account
- [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md) — where a new hire usually does this
