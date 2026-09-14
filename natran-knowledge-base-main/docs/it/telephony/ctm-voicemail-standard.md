---
type: Policy
title: CTM voicemail and missed call alerts
description: The three per-user alert settings every agent gets — the missed call notification, the voicemail mailbox and greeting, and the voicemail notification email.
tags: [ctm, telephony, voicemail, notifications]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt
  at: 2026-07-26T00:00:00Z
---

**Every CTM user gets a voicemail box** — whether or not they have a direct number, and
whether or not their team has queues. An agent without a number still takes transfers,
and a transferred call needs somewhere to land.

The setup is built fresh for each new user, including when the tracking number is
recycled from someone who left.

There are three parts, on three different screens. All three are required.

# Missed call alert

**Phone & Devices** tab → **"Call notifications"** section → enable **"Email Notify on
Missed Calls"** → Save Changes for that section.

This is the missed *call* setting and it applies to everyone. It sits next to the
Direct tracking number field, which makes it easy to read as part of the number setup
and skip for an agent who has no number. It is not — an agent who misses a queue call
or a transfer needs the same alert as anyone else.

# Greeting

The greeting is a **plain text field read aloud by text-to-speech**. Nothing is
recorded or uploaded. The field ships pre-filled with "Please leave a message after the
beep" and is replaced entirely with:

> You have reached the voicemail for **[First Last]** with Natran Green Pest Control.
> They're currently away from their desk or assisting another customer. Please leave a
> detailed message with your name and number and they'll return your call promptly.

**The pronouns are fixed.** The script uses *they / their / they'll* deliberately and is
not adjusted to match the agent. Same wording on every mailbox in the account.

> **Conflict with the IT single-source-of-truth doc (unresolved).** That document
> (`1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc`) prints the script with a gendered
> placeholder — *"I'm sorry but \[he/she] is away from their desk"* — and instructs the
> administrator to *"change the name and pronouns to suit the user"*. That is the direct
> opposite of the rule above, and its wording differs too ("I'm sorry but" versus
> "They're currently away from their desk or assisting another customer"). This doc is
> left as canonical. Michael to settle which script is in use, since every new mailbox
> built from either source diverges from the other.
>
> The two sources **agree** on every mailbox setting in the table below — Standard-F
> female, Email on, Transcribe on, Multi-Lingual English and Spanish, 20 seconds to ring —
> and on the missed-call alert above. Only the greeting text is in dispute.

# Mailbox settings

| Setting | Value | Note |
|---|---|---|
| Greeting language | English | default; unchanged |
| Greeting voice | Standard-F female | |
| Email | On | defaults to Off |
| Transcribe | On | defaults to Off |
| Lang | Multi-Lingual - English and Spanish - $0.020 / min | transcription language, not greeting language |
| Seconds to Ring Before Voicemail | 20 | unless specified otherwise |

Greeting language and transcription language are two different controls that sit near
each other and are routinely confused. Only the transcription one changes.

A new user's mailbox shows a red *"VoiceMail Box is not active. Click save to activate"*
warning until the section is saved for the first time.

# Notification email

CTM creates one notification record per user automatically, named
`VoiceMail Notification for [First Last]`, and gives it a generic subject. It is found
under **Reports → Notification**, in the Report Settings group — a different screen from
everything above.

| Field | Value |
|---|---|
| Email Recipients | the agent's own email address |
| Subject | `New voicemail from {{caller_number_format}} {{name}}  Activity ID: {{id}}` |

The two spaces before "Activity ID:" match the existing records and are intentional.

**This alert goes to the agent personally.** It is not the shared `voicemails@natran.com`
address, which handles missed calls and missed chats. Different alert, different
recipient — see [missed chat notification](/it/telephony/ctm-missed-chat-notification.md).

If the notification record does not exist yet, the mailbox has probably not been saved.

# Related

- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
- [Tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md)
