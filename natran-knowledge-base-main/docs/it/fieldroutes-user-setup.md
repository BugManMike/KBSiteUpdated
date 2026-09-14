---
type: Runbook
title: Fieldroutes user setup
description: Creating a Fieldroutes user with the right user type, assigning their access control profile and commission profile, and linking their user ID to Podium.
tags: [fieldroutes, onboarding, crm]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:03:15Z
sources:
  - id: 13aQLZu8t8bscRkupKgVIT3Tysj6v4JWkoWfp6OHu4Gw
    resource: https://docs.google.com/document/d/13aQLZu8t8bscRkupKgVIT3Tysj6v4JWkoWfp6OHu4Gw/edit
    title: Add a user to Pestroutes
status: draft
---

Four steps, the last optional. See
[Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md) for the naming question —
this source calls the system PestRoutes throughout.

> **Check which office you are in.** The office you are logged into shows in the **lower right
> corner** (Houston Branch, Austin Branch, and so on). Click it to switch. Creating a user in the
> wrong office is easy and this is the only indicator.

# 1. Add the account

1. Log into `natrangreen.pestroutes.com`.
2. **Admin** in the upper right.
3. Click the button to add a new user.
4. Enter the user's details:
   - **work** telephone and email addresses
   - username should be easy to remember, e.g. `firstlastname`
   - select the **User Type**:

| User Type | For |
|---|---|
| Office Staff | Inside sales, customer service |
| Sales Rep | Residential and commercial outside sales |
| Technician | Any operational member — technicians, service managers, and so on |

The user is emailed a password recovery email and uses it to set their password.

> The source says they "can use this to setup their email", which is a slip — it sets their
> Fieldroutes password, not their email.

# 2. Assign access control permissions

1. From the user list, click the user's name to open their card.
2. **Access Control**.
3. Select from the Access Control Profiles dropdown.

> **Which profile to pick is documented in a separate wiki document** —
> *"Which Access Control profile should I use in Pestroutes?"* — which sits in the HR folder and
> is covered in a later ingestion batch. Until then, this step has no guidance attached to it.

# 3. Assign a commission profile

**Technicians and customer care agents get a commission profile. Inside sales and outside sales
reps currently do not.**

1. Open the user's card from the employee list.
2. **Commission Rates**.
3. Open the **Custom Profile** dropdown and select:

| Role | Profile |
|---|---|
| Hourly Technician | **Hourly tech Uphelps only** |
| Production Technician | **Tech Production ## Percent** — refer to their employee agreement for the rate |
| Customer Care | **Customer care referral bonus** |

> **The production technician rate comes from the individual's employee agreement**, so this step
> needs HR input rather than being an IT decision. Also note "Uphelps" is transcribed as found and
> may be a typo for a vendor or product name.

> That inside and outside sales reps have **no** commission profile in Fieldroutes does not mean
> they are uncommissioned — sales commission is calculated separately. See the accounting batch.

# 4. Link the user ID to Podium — technicians and service managers only

The Fieldroutes **user ID** sits next to the employee's name on their card. It is roughly five
digits, e.g. `10755`.

Take that ID to [Podium user setup](/it/podium-user-setup.md) Step 2.

# Related

- [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md)
- [Podium user setup](/it/podium-user-setup.md)
- [Apple device self-service setup](/it/devices/apple-device-self-service-setup.md) — the user's side of the Fieldroutes app
