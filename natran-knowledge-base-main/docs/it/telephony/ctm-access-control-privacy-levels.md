---
type: Reference
title: CTM access control and privacy levels
description: The privacy policy levels governing what each CTM role can see in the activity log, and the access-control tags that implement them.
tags: [ctm, telephony, access-control]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T02:27:00Z
sources:
  - id: 1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc
    resource: https://docs.google.com/document/d/1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc/edit
    title: IT single-source-of-truth
status: draft
---

Access controls govern two things:

- what agents can and cannot see in their activity log
- which wrap-up screens are displayed to users

**The mechanism is tags.** Access controls use tags to determine which activity is displayed.

> **The tag and level tables below contradict each other in several places.** They are
> transcribed as found and the contradictions are marked. **Do not configure anything from this
> file until IT resolves them** — an access-control mistake here means someone sees recruiting or
> HR call activity they should not.

# Privacy policy levels

| Level | Strictness | Roles | Applied to | Description |
|---|---|---|---|---|
| Level 10 | Maximum | Call Agents | Technicians | Agents can only see their own call log activity. These agents have the role **Call Agent**. |
| Level 7 | Moderate | Call Managers | Recruiting | Sensitive areas such as recruiting and human resources, whose activity should only be visible to themselves. Human Resources has visibility into recruiting; recruiting does not have visibility into HR. Role **Call Manager**, to see activity within their groups. |
| Level 5 | Moderate | Call Managers | Human Resources | Agents can see activity from other teams depending on access control setup. Role must be **Call Manager**. Human Resources can see recruiting activity. |
| Level 1 | Relaxed | Call Managers | Inside Sales, Customer Care, Dispatch, Sales Support | Fewer restrictions — these teams can see activity across each other. Role must be **Call Manager**. |
| n/a | none | Administrators | n/a | Administrators see all areas of CTM **provided they have not been added to any teams**. Even so they remain bound by access-control restrictions. An administrator who needs to make and take calls should have a separate user account for that. |

The administrator rule mirrors the Workspace policy — see
[admin account separation](/it/google-workspace/admin-account-separation.md).

# Access control tags

These tags control who can and cannot see activity in the CTM activity panel. In all cases,
administrators not assigned to a team see everything.

| Tag | Level claimed in source | Audience | Applies to |
|---|---|---|---|
| `TA10` | Level 10 | Austin team managers. Call Agents within the Austin team see only their own activity. | Inbound calls, outbound calls, inbound SMS/chats, outbound SMS |
| `TH10` | **Level 1** | Houston team agents and managers. Call Agents within the Houston team see only their own activity. | Inbound calls, outbound calls, inbound SMS/chats, outbound SMS |
| `HR7` | **Level 10** | HR agents, HR team manager | Inbound calls, outbound calls, inbound SMS/chats, outbound SMS |
| `R5` | Level 5 | Recruiting, recruiting team managers, HR team manager | Inbound calls, outbound calls, inbound SMS/chats, outbound SMS |
| `SS1` | Level 1 | Inside sales, customer care, dispatch, sales support. All activity from managers and agents in those teams. | Inbound calls, outbound calls, inbound SMS/chats, outbound SMS |

## The contradictions, spelled out

The tag names follow a pattern — letters for the group, digits for the privacy level. On that
reading, three rows are wrong:

1. **`TH10` is labelled "Level 1 privacy policy."** Its name says 10 and its described behaviour
   is Level 10 behaviour ("see only their own activity"). Its Austin counterpart `TA10` is
   labelled Level 10. **The label is almost certainly a typo for Level 10.**
2. **`HR7` is labelled "Level 10 privacy policy."** Its name says 7. But the level table assigns
   **Level 7 to Recruiting** and **Level 5 to Human Resources** — so a tag named `HR7` matches
   neither its own label nor the level table's HR assignment.
3. **`R5` is Recruiting at Level 5**, but the level table puts Recruiting at Level 7 and Human
   Resources at Level 5. **The HR and Recruiting levels appear swapped between the two tables.**

Also unreconciled: the level table says **Level 10 applies to Technicians**, while the tags
implementing Level 10 (`TA10`, `TH10`) are Austin and Houston **team** tags, not technician tags.

# Triggers

The tagging is driven by four triggers:

- Tag all activity with `ac:shared-service` tag — *the primary trigger, tagging all inbound
  calls with the L1 tag*
- Tag all activity with `ac:shared-service` (outbound activity)
- Remove `ac:shared-service` from agent calls (inbound activity)
- Remove shared-service tag from flows

> **Two tag vocabularies coexist and are never connected.** The triggers use
> `ac:shared-service`; the tables above use `SS1`, `TA10` and so on. Whether `ac:shared-service`
> *is* `SS1` under another name, or a separate mechanism, is not stated. The source's detail
> table for the primary trigger contains only **Lorem ipsum placeholder rows** — the trigger
> configuration was never written down.

# Related

- [CTM team to queue mapping](/it/telephony/ctm-team-queue-mapping.md)
- [CTM chat tag lifecycle](/it/telephony/ctm-chat-tag-lifecycle.md)
- [Agent onboarding](/it/telephony/ctm-agent-onboarding.md)
