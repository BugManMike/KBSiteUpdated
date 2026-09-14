---
type: Runbook
title: Workspace account provisioning
description: Creating a Google Workspace user, the onboarding steps that follow account creation, and how a phone extension is recorded.
tags: [google-workspace, onboarding, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
  - id: 1oB_zUI_LJH-szuBnAVxvGENZDvHffYgORfkIRBZs-98
    resource: https://docs.google.com/document/d/1oB_zUI_LJH-szuBnAVxvGENZDvHffYgORfkIRBZs-98/edit
    title: Create an email address
status: draft
---

Google Workspace is the primary identity system. Everything else — Windows sign-in via GCPW,
Microsoft, Keeping — derives from the Workspace account.

Before starting, note that admin privileges are never added to this account. See
[admin account separation](/it/google-workspace/admin-account-separation.md).

# Create the account

1. Open `admin.google.com`.
2. Search for **"Add a user"**.
3. Fill in first name, last name, username.
   - Username is first and last name combined, e.g. `johnsmith`.
   - Leave secondary email blank.
   - Enter the employee's **work phone number** in the Phone number field. This number
     appears in their email signature.
4. Click **"Manage user's password, organization unit…"** to open further options.
   - Click the pencil icon to edit the Organization Unit and select the correct one.
   - Automatically generate their password.
   - **Add New User** to save.
   - **Preview and Send**, then enter the user's **personal** email address — this sends
     them a link to set their own password.
   - **Done**.

# Organizational unit structure

A second source, the wiki's *"Create an email address"* document, records the OU hierarchy that
the procedure above refers to but never spells out. **Services and security settings are applied
based on the OU**, so this is not cosmetic:

- **Branch staff:** `Regions` → the appropriate **Branch** → the user's **Role**
- **Corporate staff:** `Corporate` → the appropriate role

The same hierarchy is used when assigning devices — see
[Chromebook assignment](/it/devices/chromebook-assignment.md).

> **The two sources conflict on the password step.** The IT single-source-of-truth says to
> **automatically generate** the password and send a setup link to the user's personal email. The
> wiki document says to **create or assign** a password, tick the option to force a change on
> first sign-in, then *"print and save a copy of the user's credentials"* or email it to their
> personal address. **Printing credentials is the weaker practice** and the generated-password
> route avoids it entirely. IT to confirm the generated-password route is current and retire the
> other.

> **Watch the licence warning.** The wiki source notes that if you hit an out-of-licence warning,
> contact the system administrator — you may need to delete unused accounts or buy more licences.
> The same constraint applies to Teramind and Hubspot seats.

# Employee info for the email signature

Also from the wiki source, and not in the IT document. After creating the account:

**User Information → Contact Information** — enter the user's **work telephone number**. This
populates the company directory.

**Employee Info** — enter these two and leave the rest blank, because they feed the email
signature:

| Field | Example |
|---|---|
| **Job Title** | Inside Sales, Branch Manager — should resemble the OU you assigned |
| **Department** | Residential Sales, Customer Care |

These map to `field:organization.title` and `field:organization.department` in the signature
template — see
[email signature template structure](/it/google-workspace/email-signature-template-structure.md).

> The wiki source says the work telephone number "will be said to the company directory", a typo
> for *added*.

# Onboarding checklist

The full onboarding sequence, in order:

1. Create the user account.
   - Generate backup codes for 2FA.
   - Confirm work phone, position and other details are filled in.
2. Set up 2FA.
3. Place in the correct Organization Unit.
4. Add to groups — see [Google Groups](/it/google-workspace/google-groups.md).
5. Add to Keeping.
   - Invite the user to Keeping.
   - **Make sure the user is not exposed to sensitive inboxes** (recruiting, HR).
   - The *push to inbox* setting has to be done by the user themselves.
6. Delegate the inbox to the user's manager and other interested parties.
7. Deploy the email signature — see
   [email signature deployment](/it/google-workspace/email-signature-deployment.md).

> **This checklist appears twice in the source**, once in a summary section and once inside a
> tab literally headed "To do". The two copies are near-identical, except the To-do copy's
> offboarding half is truncated mid-sentence ("Move account to"). The onboarding half matches.
> Recorded here from the complete copy.

> **Not covered anywhere in the source:** the profile-photo step. Photos are required for the
> email signature — see [profile photo](/it/google-workspace/profile-photo.md) — but the photo
> does not appear in this checklist. IT to confirm where it belongs in the sequence.

# Phone extension

Skip unless the user actually has an extension.

If callers reach the user by dialling, say, `456` after calling the office:

1. From the user's Workspace profile, open the **User Information** section.
2. Confirm the phone number is present and set as **Work**.
3. Scroll to the **Email Signature** section.
4. Click the **Phone Extension** field to edit.
5. Enter only the extension digits, e.g. `456`.

> **Do not re-enter the phone number here.** Only the extension digits belong in this field.

# Related

- [Admin account separation](/it/google-workspace/admin-account-separation.md)
- [Profile photo](/it/google-workspace/profile-photo.md)
- [Email signature deployment](/it/google-workspace/email-signature-deployment.md)
- [Microsoft 365 provisioning](/it/google-workspace/microsoft-365-provisioning.md)
- [Account offboarding](/it/google-workspace/account-offboarding.md)
