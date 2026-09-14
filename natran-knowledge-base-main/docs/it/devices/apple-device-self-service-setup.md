---
type: Runbook
title: Apple device self-service setup
description: The setup an employee performs themselves on a new company iPhone or iPad — device wizard, Google account and 2FA, voicemail, and the eight apps they must configure.
tags: [jamf, devices, onboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 17Q7MX0ihwVewV6fnItCndhOgYfXD6eXE96sd5NTUbfg
    resource: https://docs.google.com/document/d/17Q7MX0ihwVewV6fnItCndhOgYfXD6eXE96sd5NTUbfg/edit
    title: iPhone & iPad self-service setup
status: draft
---

**This document is written for the employee, not the administrator.** It is what you send
someone after [assigning them a device](/it/devices/apple-device-assignment.md).

Company Apple devices are controlled by a mobile management system. Because Google is the
primary information system, **many typical iPhone services are disabled**.

**For help:** call or text `281-377-8227`, or email `admin@natran.com`. A Google Chat to
`admin@natran.com` gets the fastest response.

# Step 1 — Device setup

Select language and region, then join wifi if available (cellular works but is slower).

At the **Quick Start** screen choose **Set Up Manually**, then:

1. Apps & Data → **Don't Transfer Apps & Data**
2. **Next** on the Remote Management screen, if asked
3. Allow the device to set up eSIM, if prompted
4. Set up **Face ID**
5. Enter a **passcode** — *Passcode options* allows a simple 4-digit code
6. **Continue** on *Keep Your iPhone Up to Date*
7. **Enable Location Services** — required
8. Proceed through the remaining screens with settings of your choice

Allow a few minutes for the device to configure and install apps.

# Step 2 — Sign into your Google Workspace account

Skip if you have already activated your company email.

You should have received a temporary password. **Passwords are confidential. No one at the
company will ever ask for your password.**

1. Visit `myaccount.google.com` on the device.
2. Enter your temporary password. Contact the system admin if you do not have it.
3. Create your permanent password on the *Create a strong password* screen. This password works
   across all your Google services.
4. On the **2-Step Verification** screen, enter your iPhone's telephone number → **Next**.
5. Enter the code you receive → **Next**.
6. **Turn On** to activate 2-Step Verification.

You can change your password and 2FA settings any time at `myaccount.google.com` → **Security**.
See [2-Step Verification](/it/google-workspace/two-step-verification.md).

# Step 3 — iPhone voicemail

Skip for an iPad.

1. Open the phone dialer app.
2. Tap the **Voicemail** icon in the corner.
3. **Setup** — if there is no Setup button, tap **Greeting** and skip to step 6.
4. Enter a voicemail passcode → **Done**, then re-enter to confirm.
5. On the Greeting screen select **Custom**.
6. **Record** and speak your greeting.
7. **Play** to listen back.
8. **Save**.

> **The source says you set up voicemail twice** — "once on your iPhone's native phone dialer
> and again on your Ringcentral app (instructions below under app setups)". **There are no
> RingCentral instructions in the app list below.** Either the RingCentral app was removed from
> the standard build and this sentence was left behind, or a step is missing. See
> [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md). IT to resolve.

# Step 4 — Set up your apps

These install automatically during setup. **If any are missing, contact the system admin.
Every one matters — do not skip any.**

| App | What it is for | Setup |
|---|---|---|
| **Mail** | Company email, native app | On *Mail Privacy Protection* select **Don't Protect**. At the bottom of the Inbox you will see *Account Error: Natran* → **Details** → **Settings** → **Re-enter Password** → **Continue** → enter your company email and password. |
| **Gmail** | Company email | **Sign in** → select **Google** → **Continue** → company email and password → **Save Password** → **Allow** notifications. |
| **Fieldroutes** | Operations and routing | Check your email for an invite to set your password. **OK** for Bluetooth → Company name is `natrangreen`, entered exactly → your username and password → **Allow** notifications → **Allow While Using App** for location. |
| **Gusto Wallet** | Timeclock — clock in and out, request time off, download paystubs | Open and sign in. |
| **Chat** | Internal communication between departments | **Get Started** → toggle your Google account on → **Done** → **Allow** notifications. |
| **Podium** | Requesting customer reviews for Google, Facebook and similar | Check your email for an invite to set your password. Enter email and password → **Allow** notifications → **Save Password**. |
| **Google Photos** | Archives and backs up photos taken on the device | **Allow access to all photos** → **Allow** notifications → **Back up** and **Confirm**. |
| **Meet** | Company virtual meetings; also available inside Gmail | **Continue** → **OK** for camera, microphone and notifications → toggle your Google account on → **Done**. |

> **Gusto Wallet is the timeclock here.** Elsewhere in the wiki, attendance events are logged in
> **uAttend**, a different timeclock system. One of the two is legacy. Flagged for the HR batch,
> since attendance policy rather than IT owns the answer.

# Screenshots

This was a screenshot-heavy walkthrough and the images did not survive conversion. Steps
referring to an unnamed icon — the lock-screen info icon in Step 3, and the voicemail icon —
are thinner here than in the original. The source also ends with an empty five-row table,
suggesting more apps were planned.

# Related

- [Apple device assignment](/it/devices/apple-device-assignment.md)
- [2-Step Verification](/it/google-workspace/two-step-verification.md)
- [Fieldroutes user setup](/it/fieldroutes-user-setup.md)
- [Podium user setup](/it/podium-user-setup.md)
