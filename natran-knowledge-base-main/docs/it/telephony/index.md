# Telephony

CallTrackingMetrics is the current phone system. RingCentral material is also here and is
probably legacy — see [RingCentral voicemail setup](ringcentral-voicemail-setup.md) for the
evidence either way, which is not yet settled.

## CallTrackingMetrics

* [CallTrackingMetrics account](ctm-account.md) - The Natran CTM tenant — account identifier, access paths, and the API quirks that affect anything reading from it.
* [CTM agent onboarding](ctm-agent-onboarding.md) - End-to-end process for provisioning a new agent in CallTrackingMetrics, from intake through the hand-off items that live outside CTM.
* [CTM agent offboarding](ctm-offboarding.md) - Rerouting a departing agent's direct number to a smart router and queue, updating the number tracker, and removing their account.
* [CTM team to queue mapping](ctm-team-queue-mapping.md) - Which call queues each CTM team belongs to, and the rules governing queue variants and backup assignments.
* [CTM queue routing weights](ctm-queue-routing-weights.md) - The weighting factors, concurrency limit and opt-in state applied to an agent's row in each call queue, and the rows that must never be touched.
* [CTM tracking number assignment](ctm-tracking-number-assignment.md) - What a direct tracking number does for an agent, how agents without one still receive calls, and the save bug that makes assignment unreliable.
* [CTM voicemail and missed call alerts](ctm-voicemail-standard.md) - The three per-user alert settings every agent gets — the missed call notification, the voicemail mailbox and greeting, and the voicemail notification email.
* [CTM missed chat notification](ctm-missed-chat-notification.md) - How an unclaimed web chat is tagged and emailed to the shared inbox, and how to add a newly assigned number to the trigger.
* [CTM chat tag lifecycle](ctm-chat-tag-lifecycle.md) - The four triggers moving a web chat through its tag states, and how assignment plus status indicate where a chat stands.
* [CTM access control and privacy levels](ctm-access-control-privacy-levels.md) - The privacy policy levels governing what each role sees in the activity log, and the access-control tags implementing them.

## RingCentral (status unconfirmed)

* [RingCentral voicemail greeting scripts](ringcentral-voicemail-scripts.md) - The three greetings office personnel record: working hours, away, and after hours.
* [RingCentral voicemail setup](ringcentral-voicemail-setup.md) - Recording those greetings in a RingCentral extension, and why the after-hours one lives on a different screen.
* [RingCentral call monitoring](ringcentral-call-monitoring.md) - Creating and updating a call monitoring group so a supervisor can listen in on named agents' calls.
