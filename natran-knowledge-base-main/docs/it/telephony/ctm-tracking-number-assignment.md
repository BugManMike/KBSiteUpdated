---
type: Reference
title: CTM tracking number assignment
description: What a direct tracking number does for an agent, how agents without one still receive calls, and the save bug that makes assignment unreliable.
tags: [ctm, telephony, routing]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt
  at: 2026-07-26T00:00:00Z
---

CTM calls every number in the account a **tracking number**. A number assigned to a
specific person is their direct number — a DID.

# One field, two names

The field labelled **"Default Number"** on the user's Phone & Devices tab and the thing
referred to as the **"Direct Tracking Number"** are the same field. Both names are in
active use.

# What assignment does

Assigning a number to an agent means, on the number's own edit page:

- **Call Routing** set to *Dial Agent*, then the agent
- **Default Route** set to *Individual Voicemail*
- **Text Routing** set to *Agent*, then the agent

Call and text routing are separate controls. Setting one does not set the other, and an
agent whose text routing is unset will not receive SMS sent to their own number.

# Agents without a number

Not having a number is a normal configuration, common for field staff. Those agents:

- receive calls from **their queues**
- receive calls **transferred to them** by a colleague
- do **not** receive direct inbound calls from outside

They still get a voicemail box and a missed-call alert, because a transferred call can
land in either. See the [voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md). Assigning a
number purely to make a record look complete is the wrong instinct.

# Numbers are recycled, not retired

Every number in the account is already routing somewhere — usually to a marketing
source, a voice menu, or the previous holder. Reassignment overwrites that routing, so
the prior target is worth recording before the change and reporting after it. Number
labels often carry the history, e.g. *"(832) 706-0459 Inventory (was Kate Hartman)"*.

A recycled number does **not** carry over the previous holder's voicemail. That is built
fresh every time.

# The clearing bug

After editing a number and navigating back to the user's record, the Default Number
field sometimes comes back **blank**. No error is shown. Re-select and re-save.

This is the single most common way an agent ends up with no working number, because
nothing surfaces the failure until someone calls them.

# Verifying it stuck

`ctm_users_list` reports `outbound_number` per user. For an agent who was assigned a
number, it should show that number with `is_default: true`; a shared marketing number
such as "Google Ads Website - Austin" means the assignment did not save.

For an agent with **no** number, that same shared value is the correct end state. The
check inverts, so it should be skipped rather than read as a failure.

# Related

- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
- [Missed chat notification](/it/telephony/ctm-missed-chat-notification.md) — keyed to the number
- [CTM account](/it/telephony/ctm-account.md)
