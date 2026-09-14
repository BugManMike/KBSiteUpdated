---
type: Runbook
title: Workspace account offboarding and backup
description: Locking a departing user out, taking a Google Takeout backup of their data, waiting out the export, deleting the account, and archiving the result.
tags: [google-workspace, offboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
  - id: 15epSEASIxvf5IUAmR7FfYWn1LyAH-wLJvnzaPQLddSs
    resource: https://docs.google.com/document/d/15epSEASIxvf5IUAmR7FfYWn1LyAH-wLJvnzaPQLddSs/edit
    title: Backup and retain user's Google Workspace data
status: draft
---

> **To lock someone out immediately**, search for them in the Workspace admin console and
> click **Suspend**. That locks them out of company Gmail and other Google accounts at once.
> It does **not** lock them out of a company laptop using GCPW — see
> [Windows local account administration](/it/devices/windows-local-account-administration.md).

**Never delete an account without prior authorisation.** Managers may need access to the
departing person's files, and depending on the position may want the account kept open.

# 1. Reset the password

This locks the user out of email and documents.

1. Open `admin.google.com` with Workspace admin permissions.
2. Search the user's email and open their profile.
3. **If the account is already suspended you will need to reactivate it** to proceed.
4. **Reset Password** on the left:
   - **Create password**.
   - Enter a unique temporary password you will not forget.
   - **Uncheck** *Ask user to change their password*.
   - **Reset**.
5. Click their profile photo and remove it. Skip if there is none.
6. **Change Organizational Unit** → **Offboarding Accounts** → **Continue** → **Change**.

# 2. Begin the backup

1. **Security** tab at the top.
2. Scroll to the **Login challenge** panel, open it, and **Turn off for 10 Minutes**.
3. Scroll up to **2-step verification**, open it, click **Get Backup Verification Codes**,
   and copy one.
4. Open **Incognito Mode** in Chrome.
5. Go to `takeout.google.com`.
6. Sign in with the user's email and the temporary password.
7. When prompted for a code, choose **Try Another Way** → enter one of your backup codes.
8. Enter the code you copied.
9. On the data-selection screen, scroll to **Drive** and **uncheck it**. Drive files come
   across separately when the account is deleted.
10. Scroll to the bottom → **Next step**.
11. Destination: **Add to Drive**.
12. File size: **10 GB**. Leave other settings as they are.
13. **Create export**.
    - If a second 2FA screen appears, go back to the Workspace profile, disable the Login
      Challenge again, and repeat.
14. Close the Incognito window.

> **Backup-code digit count contradicts itself in the source.** Step 3 says to copy one of
> the "seven digit" codes; step 7 says to select "Enter one of your **8-digit** codes". Google's
> backup codes are 8 digits. Recorded both as found — IT to correct the source.

# 3. Prepare the account for deletion

The export takes anywhere from a few hours to several days depending on how much data there
is and how old the account is. **Older accounts take longer.**

1. Open `admin.google.com` and find the profile again.
2. **User details** tab → scroll to the **User information** panel.
3. Scroll to **Account Notes** and click the pencil icon.
4. Enter a note recording when the backup started, including your own name so a later reader
   knows who ran it: `Backup start on X/XX/XX @ HH:MM - Your Name`.
5. **Save**.
6. **Change Organization Unit** → **Offboarding Accounts** → **Backup started** →
   **Continue** → **Change**.

> Set a calendar reminder. **Roughly one week is the target wait** before deleting.

# 4. Delete the account

1. **Confirm with managers that deletion is approved.**
2. Open `admin.google.com`, find the account.
3. **Delete User**.
   - A screen offers to archive. **Ignore it** and click **Continue to delete**.
   - Ensure **Transfer** is selected.
   - Search for and select **your own** email address in the *Search for a user* field.
   - **Uncheck** **Calendar** and **Looker Studio**. **Keep** Drive and Docs checked.
   - **Delete User** and confirm.

> **A wrongly deleted account can usually be restored within 15 days.** `admin.google.com` →
> Users → **More Options** → **Recently Deleted Users**. After 15 days it is permanently gone.

# 5. Move the backup to the archive

The transferred files now sit in your own My Drive.

1. Open `drive.google.com` → **My Drive**.
2. Find the folder named after the deleted user's email address.
3. Move it to **Archived Natran.com User Accounts** —
   `drive.google.com/drive/u/0/folders/1V-I9VZLd2JfWBfe6hmQ5GqzVGa41gvH0`. This folder is in
   the Human Resources shared drive. If you cannot open it, ask HR managers or a system admin.

# The abbreviated version is not equivalent

> The source states this procedure twice. A short summary version elsewhere in the same
> document omits the password reset, the profile-photo removal, the Login Challenge and
> backup-code steps, and the Incognito sign-in — and it describes the Takeout destination as
> selecting "Google Drive as the source when backup should be stored" rather than
> **Add to Drive**. Follow the full procedure above. IT to delete or reconcile the summary.

# A third version, from the wiki

A separate wiki document, *"Backup and retain user's Google Workspace data"* (2024-09), covers the
same procedure and **disagrees on the two timings that decide when it is safe to delete an
account**:

| | IT single-source-of-truth | Wiki document |
|---|---|---|
| How long the export takes | "a few hours to several days" | "24 to 72 hours", elsewhere "up to 48 hours" |
| How long to wait before deleting | "roughly one week is the target" | "After 72 hours it will be safe to delete" |
| Restore window after deletion | **15 days** | **20 days** |

> **The restore window is the one to get right.** Google's admin console retains a deleted
> Workspace account for **20 days**, so the wiki figure appears correct and the 15-day figure in
> the other source is conservative — harmless if it makes you act sooner, misleading if someone
> concludes on day 17 that recovery is impossible. IT to correct.

**Two useful details appear only in the wiki version:**

- In Takeout, select **Export Once** from the *Frequency* section. The IT source omits this, and
  the default is a recurring export.
- At the delete step, check **"Include files that are not shared with anyone"** alongside Drive
  and Docs. Without it, a departing user's unshared files are not transferred — which is most of
  what you were trying to preserve.

**It also orders the first two steps the other way round**, moving the account to the Offboarding
Accounts OU *before* resetting the password. Either order works.

> The wiki version adds that when the backup finishes, Google emails the user — which forwards to
> you — so you know when deletion is safe. That only works if forwarding is already in place; see
> [email forwarding](/it/google-workspace/email-forwarding.md).

# Related

- [Email forwarding](/it/google-workspace/email-forwarding.md) — for high-profile accounts kept live
- [Shared contacts administration](/it/google-workspace/shared-contacts.md) — licence and label removal
- [Windows local account administration](/it/devices/windows-local-account-administration.md)
- [Microsoft 365 provisioning](/it/google-workspace/microsoft-365-provisioning.md) — deletion may need manual cleanup
- [CTM offboarding](/it/telephony/ctm-offboarding.md)
- [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md)
