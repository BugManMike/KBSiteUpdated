---
type: Runbook
title: CTM agent offboarding
description: Rerouting a departing agent's direct number to a smart router and queue, updating the number tracker spreadsheet, and removing their CTM account.
tags: [ctm, telephony, routing, offboarding]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Offboarding is two jobs in this order: **reroute the number, then remove the account.** Doing
it the other way round strands inbound calls and texts to a number nobody owns.

This is the inverse of [agent onboarding](/it/telephony/ctm-agent-onboarding.md). Agents without
a direct number skip straight to *Deactivate the account*.

# 1. Reroute the direct number

1. Open `app.calltrackingmetrics.com` with an admin account.
2. **Numbers → Tracking Numbers**.
3. Search for and locate the user's telephone number.
4. **Edit**.
5. Update the **Description** field to:
   `Routing to [department] (Formerly [First Last Name] employee direct number)`
6. **Call Routing** section:
   - Change *"How would you like to route your calls?"* to **Smart Route Calls**.
   - Select the smart router for their department — e.g. an outgoing Inside Sales agent routes
     to **Smart Routing - Inside Sales**.
   - **Save Changes.**
7. **Text Routing** section:
   - Change *"How would you like to route your texts?"* to **Queue**.
   - Select the department queue — e.g. the **Inside Sales** queue.
   - **Save Changes.**
8. **Call the number** to confirm it routes correctly.

Note that call routing goes to a **smart router** and text routing goes to a **queue** — two
different destination types for the same number. That asymmetry is deliberate, and matches the
separation of call and text routing described in
[tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md).

> Call and Text Routing have **separate Save Changes buttons**, consistent with the rest of the
> CTM console. Saving one does not save the other.

# 2. Update the number tracker spreadsheet

*Natran Call Tracking Metrics & AT&T Phone Number Trackers* —
`docs.google.com/spreadsheets/d/1ZkfvuyXFkDKsqPhtXB2yfpN3-Ct40aaKpSSfH-42rLg`

This is the same spreadsheet the onboarding runbook updates, and the same three tabs.

**`Numbers_CTM` tab** — find the number and change only these fields:

| Field | New value |
|---|---|
| Status | `Unassigned` |
| Assigned | delete the name, leave blank |
| Description | `Unassigned. Was formerly [First Last Name]'s direct number. Call routing to [department]` |
| Route Type | Smart Router or Queue, depending on setup |
| Route Name | the route calls now forward to |

**`Users` tab** — set the user to **Inactive**.

**`Activity Log` tab** — add a row:

- Date of change
- The telephone number you updated
- Who made the change in CTM — normally yourself
- Description of the change, e.g. *Routing CTM calls to [department]*

# 3. Deactivate the account

1. Click the **Settings** icon in the lower-left corner of CTM.
2. **Manage Users**.
3. Search for and locate the user's account.
4. Click the **delete (trash) icon** at the end of the row.
5. On the next page click **Remove User**.

> **This deletes rather than suspends.** The source describes no way to disable a CTM user
> while retaining the record, and no note about what happens to their historical call activity.
> If activity history matters for reporting, confirm before removing.

# What this does not cover

The onboarding runbook lists a **Keeping.com** hand-off for agents with a number, with no
written procedure. Nothing in the source describes undoing it. Assume a Keeping step is
outstanding at offboarding and check manually.

# Related

- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
- [Tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md)
- [Missed chat notification](/it/telephony/ctm-missed-chat-notification.md) — keyed to the number being rerouted
- [Workspace account offboarding](/it/google-workspace/account-offboarding.md)
