---
type: Runbook
title: Door access
description: Issuing and deactivating UniFi Access key fobs for office and sales staff, and granting another admin the permissions to do it.
tags: [unifi, door-access, network]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
  - id: 1Isyaa3Q2KQJNIcnwM-6k8YthbWezhPiNLCMqwlFB064
    resource: https://docs.google.com/document/d/1Isyaa3Q2KQJNIcnwM-6k8YthbWezhPiNLCMqwlFB064/edit
    title: Door Access setup
status: draft
---

Front door access runs on UniFi Access, on the Dream Machine Pro. Beyond issuing credentials,
admin permissions can be granted so a user receives doorbell notifications and can unlock the
door remotely.

> **Before you can set up door access for others** you need a UI.com account. Register at
> `account.ui.com/register`, then contact the system administrator to have your account added
> to the network server for door access.

# Who gets what — unresolved

**Two sources disagree on whether PIN codes may be issued at all.**

The **IT single-source-of-truth** (2026-07) states:

> Only office and sales staff should be issued security fobs. Technicians will enter through the
> back door. **DO NOT issue pin codes.**

The **wiki Door Access setup** document (2026-05) instead offers **three credential types** and
recommends a face photo, with a PIN code as one of the three options. It says nothing about
restricting fobs to office and sales staff.

> **This resolves a puzzle from the earlier ingestion, and replaces it with a real question.**
> The IT document's introduction promises instructions for "how to create pin codes" while its
> body forbids them — because that introduction is **copied verbatim from the wiki document**,
> where PIN codes genuinely are documented. The IT author kept the intro, replaced the procedure
> with an NFC-only one, and added the prohibition. Both documents also carry the same swapped
> iOS/Android app links, confirming the lineage.
>
> So the contradiction is not sloppiness — it is a **policy change captured halfway**. What is
> unknown is whether the change was made deliberately and the wiki was never updated, or whether
> the prohibition is one person's view. Because PIN codes are the one credential that can be
> shared or observed, **IT should confirm the rule before anyone issues a credential**.

Both procedures are recorded below. They also differ in the group assigned: **Door Access -
Natran** in the wiki version, **Unlock Access** in the IT version.

# Issue credentials — wiki version

1. Open `unifi.ui.com` and sign in.
2. Select **Dream Machine Pro 12460** — click directly on the name to enter.
3. Click the **Access** icon at the top of the page. Hover over the icons to find it. This opens
   the Door Access settings.
4. Find **Active Users** and click the **(+)** button next to the name — it reads
   **Create New Person** on hover.
5. Enter first and last name. **Leave the email field blank.**
6. **Select Groups** → **Door Access - Natran** → **Save**.
7. Add credentials — **at least one is required**:

   **NFC card**
   1. Find a physical keyfob or other NFC card.
   2. Click the **(+)** icon next to *NFC card*.
   3. Select the reader to scan with.
   4. Tap the card to the reader.
   5. Confirm once the reader recognises it.

   **Face photo** *(recommended)*
   1. Take a photo of the employee's face on your smartphone.
   2. Click the **(+)** icon next to *Face Photo*.
   3. Upload and crop it so it focuses on the face.
   4. **Upload**.

   **PIN code** — *see the unresolved question above before using this*
   1. Click the **(+)** icon next to *PIN Code*.
   2. Enter a 4-digit code, or generate a random one.
   3. **Add**.

8. **Create** at the bottom.

# Issue a key fob — IT single-source-of-truth version

1. Sign in at `unifi.ui.com` → select **Dream Machine Pro** → **Access**.
2. **Users** in the left panel.
3. **Create New User** (upper right) → enter first and last name.
4. **Select Groups** in the Groups section → select **Unlock Access** → **Save**.
5. Select **Add NFC card**.
6. Select **Main Door - Entry**, then **Entry**.
7. The access device near the door blinks to show it is in pairing mode. Hold the security
   badge against it to register. It beeps on success.
8. Your screen shows the device registered and assigned a number.
9. Click **Assign**.

# Deactivate a user

The two sources give different navigation paths for this as well. The wiki version is more
specific and includes a filter step the other omits:

**Wiki version**

1. Log in at `unifi.ui.com`.
2. Select **Dream Machine Pro 12460**.
3. Select **Active Accounts** on the left.
4. **If the Admin Permission checkbox at the top is checked, uncheck it to show all users.**
   Otherwise you will only see administrators and may conclude the person is not there.
5. Locate the person and click their name.
6. Click the **gear icon** to open their settings panel.
7. Scroll to **Deactivate** and click it.
8. **Deactivate** to confirm.

**IT single-source-of-truth version**

1. Sign in at `unifi.ui.com` → **Users** on the left.
2. Select the user.
3. Click the **Active** dropdown → **Deactivate**.
4. *(Optional)* To delete permanently, select **Deactivated** from the dropdown and choose
   **Delete**.

> Both sources head this section **"Deactivate Door Pin Code"** while the steps deactivate a
> *person*, not a credential. **Neither document says how to remove a single PIN code, fob or
> face photo while leaving the person active** — which is what you would need if a fob were lost.

# Grant another user admin access

Requires admin credentials.

1. Sign in at `unifi.ui.com` → **Users** on the left.
2. Select the user to give admin access to.
3. **Role** → **Limited Admin** → **Add email**.
4. **Application Permission** → **UniFi Access** → **Administrator**. Select **None** for all
   other apps.
5. **Groups** → **Add Group** → check **Unlock Access** → **Add**.
6. **Add** at the bottom to finish.

The user receives an emailed invite to set up an account.

# The Door Access app

Once a user has accepted the invite and set up an account, they can install the UniFi Access
app on their smartphone. There is also an [instructional video](https://youtu.be/jfnI-VkgRVg).

> **The two app store links in the source are swapped** — the link labelled "iOS version"
> points to Google Play, and the one labelled "Android version" points to the Apple App Store.
> Deliberately not reproduced here so nobody follows the wrong one. Search for **UniFi Access**
> in the correct store for the user's phone.

# Related

- [Zoho software repository](/it/network/zoho-software-repository.md) — the other UniFi-attached device
- [Printer fixed IP assignment](/it/printers/fixed-ip-assignment.md) — same UniFi controller
