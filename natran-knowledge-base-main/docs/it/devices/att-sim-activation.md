---
type: Runbook
title: AT&T SIM activation
description: The four values AT&T needs to activate the SIM in an Apple-purchased iPhone, and which representatives to send them to.
tags: [att, devices, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 1NZS506QKJvPSOJnHZBIAaXk7qWNpMmC-NJxXkIqhJjA
    resource: https://docs.google.com/document/d/1NZS506QKJvPSOJnHZBIAaXk7qWNpMmC-NJxXkIqhJjA/edit
    title: How to activate an AT&T SIM card
status: draft
---

An iPhone purchased directly from Apple ships with an **inactive** SIM. AT&T has to activate it.

# Who to contact

Email our AT&T business department representatives:

| Representative | Addresses |
|---|---|
| Nashira Boyd | `nashira.boyd@att.com`, also `nb792u@att.com` |
| Lana Pickel | `lana.pickel@att.com`, also `ld9803@att.com` |

# What to send

```
BAN:
AREA CODE:
IMEI:
ICCID/SIM:
```

| Field | What it is |
|---|---|
| **BAN** | Our Billing Account Number |
| **AREA CODE** | Whichever area code is wanted — Austin `512`, Houston `832` or `713` |
| **IMEI** | Usually found by tapping the info icon on the iPhone's lock screen, generally in the corner |
| **ICCID/SIM** | Found the same way as the IMEI, or printed on the SIM card itself |

> **The BAN is not recorded anywhere in the source.** The template asks for it but the value
> appears in no document in the wiki. Whoever runs this needs to already know it, or ask. IT to
> decide whether it belongs in the knowledge base — it is an account identifier rather than a
> credential, but it does identify the billing account to anyone reading.

> **The document is titled "How to activate a Natran SIM card" internally** while its filename
> says AT&T. Same thing.

# Related

- [Apple device assignment](/it/devices/apple-device-assignment.md)
- [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md)
