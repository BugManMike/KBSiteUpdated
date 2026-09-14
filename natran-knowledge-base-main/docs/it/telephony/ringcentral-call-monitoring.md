---
type: Runbook
title: RingCentral call monitoring
description: Creating and updating a RingCentral call monitoring group so a supervisor can listen in on named agents' calls.
tags: [ringcentral, telephony]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 13FKfqwy4igNHGkNLqch88RhD4sxQtgRkbYs1mVPpIgk
    resource: https://docs.google.com/document/d/13FKfqwy4igNHGkNLqch88RhD4sxQtgRkbYs1mVPpIgk/edit
    title: How to setup call monitoring in Ringcentral
status: draft
---

> **Likely legacy.** RingCentral appears to have been superseded by CallTrackingMetrics — see
> [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md) for the evidence
> either way. Transcribed pending confirmation.

A call monitoring group pairs **one person who monitors** with **the people they may monitor**.

> **You need admin permissions** to create or change a monitoring group. Contact the system admin
> if you do not have them.

Both procedures start the same way: sign into `login.ringcentral.com` and confirm you are in the
**Admin Portal** — it says so in the upper-right corner. Then **Phone System** → **Groups** →
**Call Monitoring**.

# Create a group

1. **+ New Call Monitoring**.
2. Name the group — e.g. *"John's call monitoring group"* → **Next**.
3. Select the person **doing** the monitoring → **Next**.
4. Select the people **to be monitored** → **Save**.

# Update a group

1. Existing groups are listed. Click the one to change.
2. **Group members**.
3. Add the names to monitor → **Save**.

> **Update only covers adding.** The source has no procedure for removing someone from a
> monitoring group, or for deleting a group. Given the group controls who can listen to whose
> calls, removal is the more sensitive direction. IT to document it.

# The CTM equivalent

CallTrackingMetrics handles this differently — visibility is governed by roles, teams and
access-control tags rather than named monitoring groups. See
[CTM access control and privacy levels](/it/telephony/ctm-access-control-privacy-levels.md).
Anyone migrating this configuration should read that first; the models do not map one to one.

# Related

- [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md)
- [CTM access control and privacy levels](/it/telephony/ctm-access-control-privacy-levels.md)
