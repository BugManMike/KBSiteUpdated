---
type: Runbook
title: Employee profile photo
description: Photo requirements and the two places an employee photo must be uploaded — a public Cloud Storage bucket for the email signature, and the Workspace admin profile.
tags: [google-workspace, onboarding, signatures]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

The photo is used in two places: the **email signature** and the account's **Workspace
profile photo**. It has to be uploaded separately for each.

# Photo requirements

- Square, approximately **250 × 250**.
- Primarily the employee's face. Avoid body and unnecessary space around the subject.
- Good lighting, business casual or working attire, subject smiling.
- Filename `profile-firstname_lastname`, saved as **PNG**.
- No other modifications needed.

# Step 1 — upload to Google Cloud

1. Open `console.cloud.google.com`. Contact the system admin if you lack permission.
2. In the upper-left corner next to the Google Cloud logo, select **Image Storage Bucket**.
   If it is not showing, click whatever is showing next to the logo and select
   **Image Storage**.
3. Scroll to **Cloud Storage** under *Quick Access* and click it.
4. **Buckets** on the left.
5. Click **`natran_public_assets`**.
6. Click **Email Signature files** — this holds the logos, icons and profile photos used in
   signatures.
7. **Upload → Upload files** → select the photo.
8. Copy the public URL: click the uploaded filename to open its detail page, find the
   **Public URL** and copy it.

> **Note the bucket is public.** Employee photos placed here are publicly reachable by URL.
> That is inherent to how the email signature template loads them, but it is worth knowing.

> **Truncated instruction in the source.** Step 5 reads `Click on "natran_public_assets" or "`
> — a second bucket name was being written and never finished. If `natran_public_assets` is
> not the right bucket, the alternative is not recorded. IT to confirm.

# Step 2 — save the URL to the user's Workspace profile

1. Open `admin.google.com`.
2. Search for the user and open their profile.
3. Click the **User Information** section to open it.
4. Scroll to the **Email Signature** section and open it.
5. Paste the public URL into the **Profile Photo URL** field.
6. Optionally enter a **Phone Extension** if the user has one; otherwise leave blank.
7. **Save**.

# Step 3 — upload the photo to the Workspace admin user account

This is the second place the photo is needed.

1. Open `admin.google.com`.
2. Search the user's email address and open their profile.
3. Click the blank profile photo to the left of their name.
4. Select the photo. Again, square 250 × 250, focused on their face.

# Related

- [Email signature deployment](/it/google-workspace/email-signature-deployment.md)
- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
