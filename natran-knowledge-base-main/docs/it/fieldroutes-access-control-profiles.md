---
type: Reference
title: Fieldroutes access control profiles
description: The access control profiles available in Fieldroutes, which user type each pairs with, and the two technician profiles that are chosen by branch.
tags: [fieldroutes, access-control, crm]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:19:05Z
sources:
  - id: 1C8tEXM8xTJolC4tBo_lqnpWgCUsCqle2UDAcrJ5pnvU
    resource: https://docs.google.com/document/d/1C8tEXM8xTJolC4tBo_lqnpWgCUsCqle2UDAcrJ5pnvU/edit
    title: Which Access Control profile should I use in Pestroutes?
status: draft
---

This is the profile list that [Fieldroutes user setup](/it/fieldroutes-user-setup.md) step 2 depends
on.

| Profile | User type | Description | Notes |
|---|---|---|---|
| Branch Manager | Sales Rep | Access to most all features in Fieldroutes | |
| Billing & Payroll Manager | Office Staff | All billing functions **except deleting invoices**. Some user management controls | |
| Billing & Payroll Assistant | Office Staff | Various billing functions. **Cannot change user settings** | |
| Commercial Sales Manager | Sales Rep | | |
| Customer Care Manager | Office Staff | | |
| Customer Care Representative | Office Staff | | |
| Dispatch & Scheduling Representative | Office Staff | | |
| Field Service Manager_HTX | Technicians | | |
| Inside Sales Manager | Sales Rep | | |
| Inside Sales Representative | Sales Rep | | |
| Marketing Manager | Office Staff | | |
| Outside Sales Rep | Sales Rep | | |
| Super Admin | *(blank)* | | |
| Technician - Houston | Technician | | **Use for Houston techs** |
| Default Technician | Technician | | **Use for Austin techs** |

# The two things this table actually tells you

**Technician profiles are chosen by branch, and the names do not say so.** `Technician - Houston` is
for Houston; **`Default Technician` is for Austin**. Nothing about "Default" suggests Austin, and
picking it for a Houston technician would be a silent mistake. This is the single most useful line in
the document.

**Branch Manager is a Sales Rep user type**, not Office Staff — which matters because the user type is
set at account creation and is a separate field from the profile. See
[Fieldroutes user setup](/it/fieldroutes-user-setup.md) step 1.

# What is missing

> **Twelve of the fifteen rows have an empty Description.** The table lists what exists but not what
> most profiles permit, so choosing between, say, `Customer Care Manager` and
> `Customer Care Representative` requires knowing the answer already or inspecting the profile in
> Fieldroutes.

> **`Field Service Manager_HTX` is Houston-only** — its name carries the branch suffix and there is
> no Austin equivalent listed. Either Austin FSMs use a different profile or the row is missing.

> **`Super Admin` has no user type recorded**, and no description. Given it is presumably the most
> privileged profile, that blank is the one worth filling first.

> The document is titled *"Which Access Control profile should I use in Pestroutes?"* — the naming
> question flagged in [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md) applies
> here too.

# Related

- [Fieldroutes user setup](/it/fieldroutes-user-setup.md)
- [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md)
