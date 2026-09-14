---
type: Runbook
title: Wex fuel card setup
description: Adding a driver to the Exxon system with a fuel PIN, then inviting them to the Wex mobile app.
tags: [wex, fleet, provisioning]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:19:05Z
sources:
  - id: 1wcC0zJYswKO5FU9wQx6PEuA4dsh31um10YvtLusGRk4
    resource: https://docs.google.com/document/d/1wcC0zJYswKO5FU9wQx6PEuA4dsh31um10YvtLusGRk4/edit
    title: Add user to Wex fuel card system
status: draft
---

The Wex fuel card app lets a driver locate and purchase fuel from their iPhone. Setup is two
systems: **Exxon** creates the driver and their PIN, **Wex** invites them to the app.

Both steps use the **same administrator credentials**.

> This is filed under fleet rather than HR because the fuel PIN is the control in
> [driver fuel policy](/operations/fleet/driver-fuel-policy.md). Its source document sits in the
> wiki's HR folder.

# Step 1 — Create the driver in Exxon

1. Sign in at `exxonmobiluniversalonline.com` with administrator credentials.
2. **Cards** on the left, then **Drivers**.
3. Enter:
   - First and last name
   - Phone number
   - **Company** email address
   - Driver's licence number, state and expiration date
   - **A Driver Prompt ID** — this is the PIN they will use to purchase fuel
4. **Add**.

> **The Driver Prompt ID is the fuel PIN**, and it identifies the employee by name on the weekly
> fuel report. The employee is accountable for every transaction made with it and may not share it.
> The agreement specifies **4 to 6 digits** — this procedure does not restate that constraint, so
> check it when creating one. See [driver fuel policy](/operations/fleet/driver-fuel-policy.md).

> **Who chooses the PIN is not stated**, only that you create one. Since the employee is
> accountable for its use, and the admin creating it necessarily knows it, there is a gap here worth
> closing — the policy tells the employee to report it if anyone else knows their PIN.

# Step 2 — Invite them to the Wex app

1. Sign in at `wmd.wexonline.com/driverdash-invite/#/login` with the same credentials.
2. Find the driver you just created, listed under **Invite Driver**. **Add their phone number if it
   is not already there.**
3. Ensure the checkbox is ticked and click **Invite User**.

The system texts the driver instructions to activate the app.

> **The licence expiration date collected in step 1 is never used again** in this procedure, and
> nothing in the corpus describes re-checking it. Given
> [vehicle use policy](/operations/fleet/vehicle-use-policy.md) requires a valid licence to drive a
> company vehicle, an expiry-tracking process would be the obvious companion to this one. None is
> documented.

# Related

- [Driver fuel policy](/operations/fleet/driver-fuel-policy.md)
- [Vehicle use policy](/operations/fleet/vehicle-use-policy.md)
