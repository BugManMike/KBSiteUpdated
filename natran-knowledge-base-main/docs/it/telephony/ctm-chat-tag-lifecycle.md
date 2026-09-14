---
type: Reference
title: CTM chat tag lifecycle
description: The four triggers that move a web chat through its tag states, and how assignment plus status together indicate whether a chat is new, in progress, closed or missed.
tags: [ctm, telephony, notifications]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

A web chat carries a tag recording where it is in its life. Four triggers move it between
states.

This is the wider machine that
[missed chat notification](/it/telephony/ctm-missed-chat-notification.md) sits inside — that
document covers the one trigger that sends the email, in full per-agent detail. This one covers
all four states.

# Reading a chat's state

Assignment and status together tell you where a chat stands:

| Assigned? | Status | Meaning |
|---|---|---|
| No | In progress | New |
| No | No answer | Missed |
| Yes | In progress | Being managed |
| Yes | Answered | Closed |

# The triggers

| Name | Trigger | What it does |
|---|---|---|
| Chat - tag new/missed chats | Activity is received | Tags new incoming chats with `chat-new`. |
| Chat - tag missed chat | End event with all data ready | When an incoming chat is not claimed by any agent, tags the activity `chat-missed` and sends an email. |
| Chat - update tag when agent assigned | Agent is assigned or a receiving number is connected | Updates the tag from `chat-new` to `chat-inprogress`. |
| Chat - tag when chat ends | End event with all data ready | Updates the tag from `chat-inprogress` to `chat-ended`. |

So the happy path is `chat-new` → `chat-inprogress` → `chat-ended`, and the failure path is
`chat-new` → `chat-missed`.

> **Truncated description.** The first trigger's description ends mid-sentence — "Tags new
> incoming chats with `chat-new` tag. Also will tag" — so it may do something further that was
> never written. Its name says *new/missed* while its stated action only tags new, which
> suggests the missing clause matters.

> **Count mismatch with the existing corpus.** This table lists **four** chat triggers.
> [Missed chat notification](/it/telephony/ctm-missed-chat-notification.md) records that
> filtering the Triggers list on `missed chat` returns **three**. Those are consistent if only
> three of the four have "missed chat" in their names — but it has not been verified against
> the console. Worth one check.

# Abandonment is undecided

The source asks, and does not answer:

- When is a chat considered abandoned — after 5 minutes, and send a notification?
- How would that change the tag?
- Can a chat be force-transferred, or can other users assume control?

**There is no abandonment timeout documented.** The `chat-missed` path fires on the chat's end
event, not on a timer. If a 5-minute rule was intended, it does not exist yet.

> The source's trigger table also carries three **Lorem ipsum placeholder rows** after the four
> real ones. Ignored here.

# Related

- [Missed chat notification](/it/telephony/ctm-missed-chat-notification.md)
- [CTM access control and privacy levels](/it/telephony/ctm-access-control-privacy-levels.md)
