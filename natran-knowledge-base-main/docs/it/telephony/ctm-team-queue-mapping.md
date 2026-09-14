---
type: Reference
title: CTM team to queue mapping
description: Which call queues each CTM team belongs to, and the rules governing queue variants and backup assignments.
tags: [ctm, telephony, routing]
generated:
  by: Claude (Opus 5), from working sessions with Michael Arndt
  at: 2026-07-26T00:00:00Z
---

An agent's team determines which queues they belong to. This mapping is applied when
an agent is onboarded; whether a team change triggers a re-application has not been
established.

# Mapping

| Team | Queues |
|---|---|
| Human Resources | Human Resources |
| Customer Care | Customer Care · Customer Care (Ring back only) · Customer Care - After Hours · Weekly Meeting - Customer Care |
| Operational Support | Operational Support · Weekly Meeting - Operational Support |
| Inside Sales | Inside Sales · Inside Sales (Ring back only) · Weekly Meeting - Inside Sales |
| Recruiting | Recruiting |
| Billing | Billing · Billing - After Hours |
| Marketing | Marketing |
| Dispatch | Dispatch |
| Developers | *none* |
| Accounting | *none* |
| Austin Operations | *none* |
| Houston Operations | *none* |

# Rules

**Queue variants belong to their team.** The "(Ring back only)", "- After Hours" and
"Weekly Meeting -" forms are not separate or optional. An agent joining Customer Care
joins all four Customer Care queues and they all carry the team's own-team weight —
see [queue routing weights](/it/telephony/ctm-queue-routing-weights.md).

**Four teams have no queues at all.** Developers, Accounting, Austin Operations and
Houston Operations. Their members are still CTM users with voicemail and direct
transfers; they simply are not in the general call rotation.

**Customer Care - After Hours is effectively empty.** The CTM API reported
`total_agents: 0` on 2026-07-26. That looks like an oversight rather than a decision,
and it is not a reason to leave a new Customer Care agent out of it — the queue only
starts working again once someone is in it.

**Sales Support has no team mapped to it.** The queue exists and can be used as a
backup, but nobody joins it by virtue of their team.

# Backup queues

A backup is a queue belonging to a *different* team, assigned so that agent can absorb
overflow. Backups are requested per-agent, not derived from the team.

**Billing takes no backup agents.** The Billing queues already overflow to Customer
Care, so adding backups there is redundant. A request for a Billing backup should be
declined and explained rather than quietly fulfilled.

**Backup scope is ambiguous and must be resolved explicitly.** "Back up Inside Sales"
could mean the main queue or all three Inside Sales queues. Whoever configures it
names every queue in writing and gets confirmation before applying it.

# Related

- [Queue routing weights](/it/telephony/ctm-queue-routing-weights.md) — what weight each queue gets
- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
