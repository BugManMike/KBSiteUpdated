---
type: Runbook
title: Email forwarding for offboarded accounts
description: Keeping a departing high-profile user's email operational by adding a Gmail routing rule, and the extra filter needed when forwarding into Keeping.
tags: [google-workspace, offboarding, email]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

When offboarding a high-profile account you may want their address to keep working and
forward elsewhere.

# Add the routing rule

1. Open `admin.google.com` with Workspace admin permissions.
2. Search for **Gmail** → **Settings for Gmail**.
3. Scroll to the bottom → **Routing** panel.
4. Scroll to **Email forwarding using recipient address map**.
5. **Add Another Rule**.
6. Configure it:
   - Title it descriptively, e.g. *John Smith route to keeping@natran.com*.
   - Messages to affect: **All incoming messages**.
   - **Save**.

> **The recipient address map itself is not described.** The steps stop at "Save" without
> saying where the departing address and its destination are entered — which is the actual
> substance of a recipient address map rule. IT to complete this procedure.

# Forwarding into keeping@natran.com

If the destination is `keeping@natran.com`, additional steps are needed inside that inbox.

1. Sign into the `keeping@natran.com` inbox. Contact the system admin if you lack permission.
2. Search for the address you are forwarding — e.g. `johnsmith@natran.com`.
3. Click the options icon at the end of the search bar.
4. Copy the email into the **to** field.
5. **Create filter**, then:
   - Check **apply the label** and select **Employee Forwarding**.
   - Forward it to: `Office.Natran.65260@incoming.keeping.com`
   - **Create filter**.

> This procedure relied on screenshots that did not survive conversion — steps 3 and 4
> referenced images showing which icon and which field. The written text alone is thin here.

# Related

- [Workspace account offboarding](/it/google-workspace/account-offboarding.md)
