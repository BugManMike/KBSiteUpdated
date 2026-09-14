---
type: Runbook
title: CTM agent onboarding
description: End-to-end process for provisioning a new agent in CallTrackingMetrics, from intake through the hand-off items that live outside CTM.
tags: [ctm, telephony, onboarding]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt
  at: 2026-07-26T00:00:00Z
---

Provisioning an agent touches seven areas of CTM plus two systems outside it. The work is
sequential because later steps depend on the user record existing, but the phases are
independently verifiable and several are conditional.

This runbook is the map. The normative values live in the linked concepts and are not
duplicated here.

# Intake

Collected before anything is created:

| Item | Notes |
|---|---|
| Email, first name, last name | |
| Team | Determines queues — see [team to queue mapping](/it/telephony/ctm-team-queue-mapping.md) |
| Branch | Corporate / Austin Branch / Houston Branch / n/a |
| Tracking number | Or an explicit "none" — see [tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md) |
| Notification destination | Defaults to `voicemails@natran.com`; deviations need a reason |
| Backup queues | Other teams' queues, named individually |

**Branch is not team.** An agent in the Houston *branch* is not on the Houston
Operations *team*. The two fields are collected together and read similarly, but only
the team determines which phases run.

The full plan — every queue with its weight, which phases run, which are skipped — is
confirmed before anything is created. It costs one exchange and catches wrong-team and
wrong-number errors while they are still free to fix.

# Phases

| # | Phase | Applies to |
|---|---|---|
| 1 | Create the user | everyone |
| 2 | Assign and configure the tracking number | agents with a number |
| 3 | Notifications and voicemail | **everyone, no exceptions** |
| 4 | Message response | Austin Operations and Houston Operations only |
| 5 | Team and queue assignment | everyone; queue step skipped for no-queue teams |
| 6 | Missed chat trigger | agents with a number |
| 7 | Queue routing rules | Retry Busy Agents for everyone; weights per assigned queue |

**Phase 1.** Settings → Manage Users → New User. Email, first and last name, "Set
default login page to Desk Mode" enabled, Role set to **Call Manager**. The role is
always Call Manager for a new agent; anything else is handled outside this process.
Saving redirects to the user's edit page.

> **Conflict with the IT single-source-of-truth doc (unresolved).** That document
> (`1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc`) states the new-user role three
> different ways: its invite procedure says select **Call Agent**; its Roles note says
> *"the default user role should be Call Manager"*; and its Roles table assigns by
> position — Inside Sales Agent → Call Manager, Customer Care Agent → Agent. This doc's
> **Call Manager** came from working sessions plus live API reads and is left as
> canonical. The role choice is not cosmetic: it determines what the agent can see, per
> [access control and privacy levels](/it/telephony/ctm-access-control-privacy-levels.md).
> Michael to settle.
>
> The same document adds two Phase 1 details not recorded here — generate **MFA backup
> codes** on the new user, and leave **Access Controls** set to *No Restrictions* — and
> calls the desk-mode toggle *"Default login page to Desktop Calling"* rather than
> "Desk Mode". Whether those are additions to this phase or a different reading of it is
> unverified.

**Phase 2.** See [tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md). Skipped
entirely for agents without a number — but note this does not extend to Phase 3.

**Phase 3.** See [voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md). Three parts on three
screens: **"Email Notify on Missed Calls"** in the Call notifications section of Phone
& Devices, the mailbox on the Voicemail tab, and the notification record under
Reports → Notification. This phase runs for every user regardless of number or team,
and should never appear on a list of skipped work.

**Phase 4.** Austin Operations and Houston Operations only. Messaging tab → Message
Responses → Add, titled `On my way`:

> Hello, this is **[First Last]** with Natran Green Pest Control. I am currently en route
> to our scheduled appointment and expect to arrive within the next 30 minutes.

**Phase 5.** Assignments tab → set the team → Save Changes → **Edit Assigned Queues**
→ move the team's queues plus any backups into the right-hand box → Save Changes. The four no-queue teams take the team assignment only.
Access Control Groups follow automatically from the team; Divisions and LeadReactor
priorities are not part of this process.

**Phase 6.** See [missed chat notification](/it/telephony/ctm-missed-chat-notification.md).

**Phase 7.** See [queue routing weights](/it/telephony/ctm-queue-routing-weights.md).

# The user edit page is one page

Profile, Security, Phone & Devices, Voicemail, Messaging, Assignments and Versions are
jump links into a single long page, and **each section has its own Save Changes button**.
Saving one does not save the others. This is the most common way the process fails
silently.

# Verification

**Verification is a console job.** The CTM connector cannot look up a specific user —
its list endpoints ignore `page` and return an unstable ten-item sample, so a newly
created agent may simply never come back. See [CTM account](/it/telephony/ctm-account.md).

Confirm in the console, on the user's own record:

| Setting | Where |
|---|---|
| Role is Call Manager, Desk Mode default on | Profile |
| Default Number still populated | Phone & Devices — re-check; it clears silently |
| Email Notify on Missed Calls enabled | Phone & Devices → Call notifications |
| Voicemail box active, red warning cleared | Voicemail |
| Notification subject and recipient | Reports → Notification |
| Team and queue membership | Assignments |
| Weighting factor on the star column | each queue's Agent Routing Table |
| New workflow block present | Automation → Triggers, filtered on `missed chat` |

If the connector does happen to return the new user, four fields corroborate the
console: `role: call_manager`, `desk_mode_default: true`,
`notifications.email_notify_on_missed_calls: true`, and `outbound_number`. Treat that
as a bonus, not the check.

# Hand-offs outside CTM

Two items complete the onboarding and are not done in CTM:

**The number tracker spreadsheet.** *Natran Call Tracking Metrics & AT&T Phone Number
Trackers* —
`docs.google.com/spreadsheets/d/1ZkfvuyXFkDKsqPhtXB2yfpN3-Ct40aaKpSSfH-42rLg` —
needs three tabs updated: `Numbers_CTM` (the number's inventory row moves to
Assigned), `Users` (new row) and `Activity Log` (new row).

**Keeping.com.** Required for agents with a number, separate from the Phase 6 trigger.
No written procedure exists.

# Close-out

A run reports what changed, what was skipped and why, and anything that would not save —
including the number's previous routing target versus its new one. A report claiming
success while one queue weight failed to persist is worse than no report, because the
gap then goes unnoticed until a customer call is missed.

# Related

- [CTM account](/it/telephony/ctm-account.md)

# Citations

[1] Working sessions with Michael Arndt, 2026-07-26 — process definition, gotchas, and
    the protected weight values.
[2] Live reads of the CTM API for account 448519, 2026-07-26 — user, queue and number
    counts, field names, and the finding that the list endpoints ignore `page` and
    return an unstable sample.
