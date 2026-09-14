---
type: Runbook
title: Shared contacts administration
description: Granting and removing Shared Contacts licences, and adding or removing contacts from the shared labels that sync to users.
tags: [shared-contacts, google-workspace, contacts]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Shared Contacts (`sharedcontacts.com/app`) distributes a shared directory to users via
labels. Two separate things are managed here: **who has a licence**, and **which contacts sit
on which label**.

# Grant a user a licence

1. Open `sharedcontacts.com/app`.
2. Top-right corner: click the **Manage users & licenses** icon. Hover to see its name.
3. On the left, next to **Users**, click the person-with-a-plus button.
4. Enter the user's email address → **Add Users**. This adds them and assigns a licence if one
   is available.

# Remove a user's licence

1. Open `sharedcontacts.com/app`.
2. Top-right: **Manage users & licenses**.
3. Find the user.
4. Hover their name and select **Remove license** on the far right.
5. Confirm.

**Removing the licence is not the whole job.** If the departing user was themselves assigned
to any labels, those assignments must also be removed so they stop appearing for other users.

# Add a Natran contact

1. Open the company directory at `contacts.google.com/directory`.
2. Locate the contact.
3. **+Label**.
4. Select the shared label. Multiple labels are possible, but **most contacts should be in
   just one**.
5. Open `sharedcontacts.com/app`.
6. Click the label you added and confirm the contact is there.
7. **Sync Contact** in the upper-right corner.

# Add a third-party contact

For contacts without a `natran.com` address:

1. **All Contacts** on the left.
2. At the top, click the person-with-a-plus button.
3. **Add a new contact**.
4. Fill in name, email, phone number and so on.
5. **Create**.

Then add it to a label:

1. Select the label on the left.
2. Click the person-with-a-plus button at the top.
3. **Add existing contacts**.
4. Search the contact and confirm its checkbox is checked.
5. **Add Contacts**.

The contact now syncs to everyone the label is shared with.

# Remove a contact from a label

1. Open `sharedcontacts.com/app`.
2. Click the label on the left.
3. Find the contact's name.
4. Hover it and select **Remove contact from Label** on the far right.
5. Confirm.

Repeat for every other label the contact was assigned to.

# Related

- [Workspace account offboarding](/it/google-workspace/account-offboarding.md)
