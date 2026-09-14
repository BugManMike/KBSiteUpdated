---
type: Reference
title: CallTrackingMetrics account
description: The Natran CTM tenant — account identifier, access paths, and the API quirks that affect anything reading from it.
tags: [ctm, telephony]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt and live reads of the CTM API
  at: 2026-07-26T00:00:00Z
---

CallTrackingMetrics (CTM) is the phone system for Natran Green Pest Control. It
handles inbound call routing, agent queues, SMS and web chat, voicemail, and the
automation triggers that fire on call and chat events.

# Account

| Field | Value |
|---|---|
| Organization | Natran Green Pest Control |
| Account ID | `448519` |
| Console | `app.calltrackingmetrics.com` |
| API base | `https://api.calltrackingmetrics.com/api/v1/accounts/448519` |

The console hostname is `app.calltrackingmetrics.com`.

# Scale, as of 2026-07-26

| Entity | Count |
|---|---|
| Users | 44 |
| Tracking numbers | 154 |
| Queues | 77 |

The queue count is far larger than the twenty queues that appear in the
[team to queue mapping](/it/telephony/ctm-team-queue-mapping.md). What the remainder are has not
been established — the connector cannot enumerate them, for the reason below.

# Access

Two paths exist and they are not interchangeable.

**The web console** is the only way to change anything. Agent creation, number
assignment, queue membership, routing weights, voicemail and triggers are all
console-only operations.

**The CTM connector** (the `ctm_*` tools) is **read-only**. It is useful for
verifying that a console change actually persisted, and for pulling facts without
loading pages, but it cannot substitute for the console on any write.

# The connector cannot enumerate

This is the most important thing to know about reading from CTM, and it is not
documented anywhere in the tooling. **The list endpoints return an unstable
ten-item sample. There is no way to page through a full result set.**

- **`page` is ignored.** A request for `page: 3` returns a response whose own body
  says `"page": 1`. Verified against `ctm_queues_list` and `ctm_users_list`.
- **`per_page` is ignored.** Page size is fixed at ten.
- **Filter parameters are ignored.** `filter` and `number` are accepted without
  error and have no effect.
- **The ten items returned vary between identical calls.** Two `ctm_queues_list`
  calls with the same arguments returned overlapping but different queues. There is
  no stable sort, so repeated calls surface different slices by chance rather than
  by design.
- **`total_entries` and `total_pages` are accurate.** They describe a result set the
  connector will not hand over.

The practical consequence: the connector answers "how many are there" and "what does
this record look like, if it happens to come back," and nothing else. **It cannot be
used to look up a specific user, number or queue by name.** Any procedure that
depends on finding a particular record — such as confirming a newly created agent —
has to run in the console instead.

# Field notes

- **`outbound_number` is not the direct tracking number.** It reports the outbound
  caller ID. For an agent with their own number it shows that number with
  `is_default: true`; for an agent without one it shows the shared account default.
  See [tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md).

# What the connector cannot see at all

Queue weighting factors, queue opt-in state, voicemail greeting text and voice, the
voicemail notification subject and recipient, the Retry Busy Agents setting, and
trigger definitions. None of these appear in any response. They are console-only.

# Related

- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md) — the end-to-end setup process
- [Team to queue mapping](/it/telephony/ctm-team-queue-mapping.md)
- [Queue routing weights](/it/telephony/ctm-queue-routing-weights.md)
