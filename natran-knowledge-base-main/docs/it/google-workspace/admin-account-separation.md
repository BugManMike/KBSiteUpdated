---
type: Policy
title: Admin privileges require a separate account
description: No daily-driver Google Workspace account may hold admin privileges; elevated access is granted through a second, dedicated account.
tags: [google-workspace, security, access-control]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

**No daily driver account should be allowed to have admin privileges.**

The risk is that a compromised device, or a device left unattended, becomes a route into
sensitive areas of the business.

Where a user genuinely needs administrator privileges, those are granted on a **secondary
account**. So `johnsmith@natran.com` would have a second account
`johnsmithadmin@natran.com`, and the admin work happens there.

# The same principle applies in CTM

CallTrackingMetrics carries an equivalent rule: an administrator who also needs to make and
take calls should hold a **separate user account** for that purpose, because an admin added
to a team stops being able to see everything. See
[CTM access control and privacy levels](/it/telephony/ctm-access-control-privacy-levels.md).

# Related

- [Workspace account provisioning](/it/google-workspace/account-provisioning.md)
- [Context-Aware Access](/it/google-workspace/context-aware-access.md)
