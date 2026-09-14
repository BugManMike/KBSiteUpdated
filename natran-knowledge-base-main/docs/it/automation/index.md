# Automation

Workflow automation on the self-hosted n8n instance (`n8n.srv1090686.hstgr.cloud`) —
notification pipelines that move events from email into Google Chat.

* [Email → Google Chat notification design](email-to-chat-notification-design.md) - The shared design behind the n8n workflows that post lead emails into Google Chat — mail source, filtering rationale, duplicate suppression, phone-link convention, and troubleshooting.
* [HubSpot form → Chat notification workflow](hubspot-form-chat-notification.md) - The n8n workflow that posts HubSpot "New Form Submission" emails to office@natran.com into Google Chat — exact node parameters, message formatting, and rebuild steps.
* [Tech referral form → Chat notification workflow](tech-referral-chat-notification.md) - The n8n workflow that posts "TECH REFERRAL FORM" emails into Google Chat — exact node parameters, full-body message formatting, and rebuild steps.
