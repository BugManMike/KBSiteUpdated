---
type: Runbook
title: CTM missed chat notification
description: How an unclaimed web chat is tagged and emailed to the shared inbox, and how to add a newly assigned number to the trigger.
tags: [ctm, telephony, notifications]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt
  at: 2026-07-26T00:00:00Z
---

When a web chat arrives and nobody claims it before it times out, a CTM trigger tags the
activity and emails a monitored inbox — normally the shared `voicemails@natran.com` —
so someone can follow up by SMS. The trigger is
keyed to the agent's tracking number, so each agent with a number needs their own
workflow block inside it.

This is a *notification*. It is distinct from the **Text Routing** control described in
[tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md), which decides where
texts go in the first place. Both are needed.

# Where it lives

Automation → Triggers → **"Chat - tag missed chat, email notification"**
(Trigger: "End event with all data ready"; Run: All Tracking Numbers).

Filtering the Triggers list on `missed chat` returns three triggers. The **list page
prints every workflow rule inline**, tracking numbers included, so it can be searched
without opening anything — which is the right way to check whether a number is already
covered.

If a number already appears, a block exists for it, usually left by the previous holder.
Leave it alone: no rename, no edit, no duplicate.

The trigger's edit screen renders inside an inline frame and shows "Initializing..." for
15–30 seconds. Page-reading tools cannot see inside that frame; it needs waiting out
rather than reloading.

# Block standard

One block per agent, named `[First Last] DiD`, appended at the bottom of the Workflows
list.

**Rules**

```
If   Type            is any        Chat
And  Tracking Number includes any  [the agent's number]
And  Status          is any        No Answer
```

`includes any` is the standard. The number is easiest to find by its last four digits;
options display with their CTM label.

**Actions, in this order**

1. Remove Tags → `chat-new`
2. Tag Call → `chat-missed`
3. Send Email:
   - To: the notification destination agreed at intake. This is normally
     `voicemails@natran.com` and deviating from it needs a reason, but it is a
     per-agent decision rather than a constant.
   - Subject: `Missed chat from {{caller_number}} {{name}} Activity ID: {{id}}`
   - Body:

     ```
     The following chat was sent but no one claimed it and it timed out.
     Send the contact a new SMS message to continue the conversation.
     Date: {{called_at}}
     Activity ID: {{id}}
     Tracking Number: {{tracking_number}}
     Tags: {{tag_list}}
     From: {{name}}
     Number: {{caller_number}}
     Transcription:
     {{chat_transcription}}
     ```

   - Check **both** "Exclude Activity Details" and "Exclude Standard Footer"

Each block has its own Save Changes button at its bottom-left. Saving there also clears
the floating "You have unsaved changes" bar.

# Verifying

Reload Triggers, filter `missed chat`, and confirm the new
`Tracking Number includes any +1XXXXXXXXXX` rule appears in the trigger's rule summary
on the list page. The connector cannot see trigger definitions, so this is the only
check available.

# Two things that look wrong but aren't

**"And stop processing further workflows"** in the block footer is static text, not a
setting. There is nothing to toggle.

**The existing blocks are inconsistent.** Some send to personal addresses, one uses
`includes all`, one has its actions out of order, one uses Remove Tags where it should
Tag Call. They are not a template and are not being retrofitted; new blocks follow the
standard above.

# Keeping.com

A separate Keeping.com setting is also required for each agent with a number. It is not
the same as this trigger and both are needed. No written procedure exists for it yet.

# Related

- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
- [Voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md) — the other notification, to a different recipient
