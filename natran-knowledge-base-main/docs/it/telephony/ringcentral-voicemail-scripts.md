---
type: Script
title: RingCentral voicemail greeting scripts
description: The three greetings office personnel record for RingCentral — working hours, away, and after hours.
tags: [ringcentral, telephony, voicemail]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1BV7-XdVHMkuR3WSLVza87pjR4x4Sqy1PFQ0TSxowsqg
    resource: https://docs.google.com/document/d/1BV7-XdVHMkuR3WSLVza87pjR4x4Sqy1PFQ0TSxowsqg/edit
    title: Voicemail Greeting Script for Office Personnel
status: draft
---

> **This is very likely a legacy system.** These are **RingCentral** greetings, recorded in the
> user's own voice. The current telephony system is CallTrackingMetrics, where the greeting is
> **text read aloud by text-to-speech** and worded in the third person — see
> [CTM voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md). Whether
> RingCentral is retired is unconfirmed. See
> [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md) for the full
> question.

For how to record these, see
[RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md).

# 1. Working hours

> Hello, you have reached the desk of **[your name]** with Natran Green Pest Control. I'm sorry
> but I am either away from my desk or assisting another customer. Please leave a detailed
> message with your name and telephone number and I'll return your call as soon as possible.
> Thanks and have a wonderful day.

# 2. Away message

> Hello, you have reached the desk of **[your name]** with Natran Green Pest Control. I'm sorry
> but I'm out of the office today. If you need immediate assistance please hang up and call our
> main line at **(281) 324-8779**. Otherwise please leave a detailed message with your name and
> telephone number and I will return your call when I'm back in the office. Thanks and have a
> wonderful day.

# 3. After hours

> Hello, you have reached the desk of **[your name]** with Natran Green Pest Control. My normal
> hours are **#AM to #PM Monday through Friday**. Please leave a detailed message with your name
> and telephone number and I'll return your call when I'm back in the office. Thanks and have a
> wonderful day.

# Notes on the wording

**These are first person.** The speaker is the agent — *I am away from my desk*, *I'll return
your call*. The CTM greeting is third person about the agent, spoken by a synthetic voice. The
phrase *"away from my desk or assisting another customer"* survives into the CTM script as
"They're currently away from their desk or assisting another customer", so the CTM wording is
descended from script 1 above.

**Script 3 leaves the hours as literal placeholders** — `#AM to #PM` — with no guidance on what
each department's hours are. The agent has to know them.

**Script 2 hard-codes the main line as (281) 324-8779.** That number appears nowhere else in the
corpus so far and has not been verified as current.

# Related

- [RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md)
- [CTM voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md) — the current standard
