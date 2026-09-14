---
type: Runbook
title: Windows device user removal and return
description: Removing a departing user's local account from a Windows device by hand, returning the device to storage, and the HR notification that closes the loop.
tags: [devices, offboarding, inventory]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1MHWumYCVg5AYgpBrVC4Fnd42-DmD34BOo0JDImP_jec
    resource: https://docs.google.com/document/d/1MHWumYCVg5AYgpBrVC4Fnd42-DmD34BOo0JDImP_jec/edit
    title: Onboarding and offboarding users from Windows devices
status: draft
---

> **This is the manual method and it probably should not be used.**
> [Windows local account administration](/it/devices/windows-local-account-administration.md)
> does the same job through ManageEngine Endpoint Central, remotely, with a **Safe Delete**
> option that retains the user's data before removing the account. This procedure requires
> physical access to the device and **deletes the account and data together with no backup
> step**. The Endpoint Central method is from a 2026 source; this one is from 2024. Recorded
> because the device-return and HR-notification steps at the end appear nowhere else. IT to
> confirm which removal method is current.

# Remove the user

1. Sign into the computer's **Admin** account.
2. Open the Windows **Settings** app — search "Settings" and select the gear icon.
3. Search Settings for **Other Users**.
4. Select the user to remove.
5. **Remove**.
6. **Delete account and data**.

# Return the device

7. Put the device back into the designated storage area.
8. **Notify Human Resources** that the account has been removed and the device returned to
   inventory, so they can update the
   [Device Inventory sheet](https://docs.google.com/spreadsheets/u/0/d/1-nOodSJ30lYS2N4BT_U2tdYkpW7wpEybkSdrBRsKoyE/edit)
   and remove the user.

> **Note who owns the inventory sheet.** HR updates it here, but
> [Apple device erase](/it/devices/apple-device-erase.md) has the IT administrator updating the
> same spreadsheet directly. Two devices types, two different owners of the same record. IT and
> HR to agree.

# The Windows sign-in side

The same source document covers adding a user to a Windows device. That material is fuller in
[Windows PC setup](/it/devices/windows-pc-setup.md) Steps 5–7 and is not repeated here, with
one exception worth recording because it appears nowhere else.

**RC Phone Desktop (RingCentral)** was installed on Windows devices and configured as follows —
have the user sign in with the Google icon, then the **⛭** settings:

- **Notifications & Sounds → Notifications:** *Automatically launch on startup* on.
- **Notifications & Sounds → Notifications:** *Display missed events in taskbar* and
  *Display incoming calls in notification center* both on.
- **Notifications & Sounds → Headsets:** Headset support on. Download and install
  **Plantronics Hub** from the link there, then return to RC Phone and confirm it reads
  *Found* next to Plantronics Hub. The app may need restarting for it to register.
- **Contacts:** *View Google Contacts* on → **Sign In** → select the user's Google account →
  approve all permissions until it reads Authenticated. This syncs Google contacts into RC
  Phone.

> **RingCentral appears to be the previous phone system.** The newer [Windows PC
> setup](/it/devices/windows-pc-setup.md) installs Call Tracking Metrics instead, and the IT
> single-source-of-truth names CTM as "our telephony system" with no mention of RingCentral.
> See [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md), where the
> same question is flagged. If RingCentral is retired, these settings are dead and this section
> should be deleted rather than carried forward.

# Related

- [Windows local account administration](/it/devices/windows-local-account-administration.md)
- [Windows PC setup](/it/devices/windows-pc-setup.md)
