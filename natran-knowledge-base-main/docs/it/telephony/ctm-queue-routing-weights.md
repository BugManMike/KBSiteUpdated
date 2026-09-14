---
type: Policy
title: CTM queue routing weights
description: The weighting factors, concurrency limit and opt-in state applied to an agent's row in each call queue, and the rows that must never be touched.
tags: [ctm, telephony, routing]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt
  at: 2026-07-26T00:00:00Z
---

CTM distributes queue calls across agents in proportion to a per-agent, per-queue
**weighting factor**. The factor lives on the agent's row inside each queue's Agent
Routing Table, so a single agent has as many independent weights as they have queues.

# Where these settings live

Routing → **Queues** (`/queues`) → the queue's row → **edit agent routing rules** in
the Agents column. The Agent Routing Table pages at ten agents; use the Search box or
append `#entries_per_page=100` to the URL to bring a specific agent into view.

**Retry Busy Agents** is elsewhere: Settings → Manage Users → the user's row →
**User Queue** in the Agent Queue column → Routing → expand **Agent Selection
Options**.

# Standard values

| Setting | Own-team queue | Backup queue |
|---|---|---|
| Weighting Factor | `10` | `5` |
| Max Concurrent Activities | `2` | `2` |
| Opt In/Out of Queue Calls | leave unchanged | set **On** |

Own-team and backup are defined by the [team to queue mapping](/it/telephony/ctm-team-queue-mapping.md).
The 10:5 ratio means a backup agent takes roughly half the share of a primary, which is
the intent — present in the rotation without displacing the team that owns the queue.

Every new agent also gets **Retry Busy Agents** enabled on their personal User Queue,
independent of team and independent of whether they have a tracking number. Agents on
the four no-queue teams still get this.

# The "Edit All" button silently drops the weight

The Agent Routing Table has an "Edit All" control at the upper right that appears to
set values for every agent at once. **Do not use it.** Max Concurrent Activities saves
correctly, the weighting factor does not — the star column comes back blank on reload
and no error is shown anywhere.

The row-level **Edit** link at the left of each agent's row is the only reliable path.
It opens that agent's own routing page for that queue, where every setting above lives,
so it is one page visit per queue.

Worth spot-checking the first queue configured in any session: reload the Agent Routing
Table and confirm the star column shows the weight. Once it sticks via the row-level
page it stays.

# Protected rows

**Never modify another agent's row.** The values that look like mistakes are deliberate:

| Agent | Weight | Where |
|---|---|---|
| Michael Arndt | 100 | most queues |
| Katelyn Zimmerer | 9 | Inside Sales |
| Larry Newsom | 7 | Customer Care |
| Tamara Ferris | 7 | Operational Support |
| ctmuser | 1 | — |

The **Billing** queue's weights are blank. They are being corrected by hand and should
be left alone.

# Agents cannot be added from this page

If an agent is missing from a queue's routing table entirely, they were never assigned
to the queue. That is fixed on the user's Assignments tab, not here.

# Related

- [Team to queue mapping](/it/telephony/ctm-team-queue-mapping.md)
- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
- [CTM account](/it/telephony/ctm-account.md) — the connector cannot verify any value on this page
