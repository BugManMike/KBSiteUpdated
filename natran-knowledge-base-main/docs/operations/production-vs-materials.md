---
type: Runbook
title: Production vs materials
description: The monthly measure of technician effectiveness — entering production values into the VIM inventory system and running the report against a 10% material usage target.
tags: [vim, technicians, inventory]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T03:44:23Z
sources:
  - id: 17Bn2xCcFpTkBtPwpOmxxXk-T5D6ccs-5mthBija3Tcw
    resource: https://docs.google.com/document/d/17Bn2xCcFpTkBtPwpOmxxXk-T5D6ccs-5mthBija3Tcw/edit
    title: Production vs. materials
status: draft
---

**A method for determining the effectiveness of each technician. The target is 10% material usage
compared to production.**

Run monthly, per warehouse. It sits in the accounting folder in the source wiki but the metric is an
operations one — it judges technician performance, not the books.

# 1. Run the production report in Pestroutes

1. **Reporting → Commission** → profile dropdown → **Tech Production**.
2. Date range → **Last Month**.
3. Employee Type → **Technician**.
4. **Advanced Filters → all Offices selected.**
5. **Refresh.**

The page lists each technician with their completed production.

6. **Export to Excel** and save to the End-of-Month folder.

# 2. Enter production values into VIM

1. Sign into `uim2.com`.
2. **Operations** → select the **Warehouse**.
3. **Production.**
4. You get a list of trucks and drivers.
5. **Key the production amounts from step 1 into each driver's truck.**
6. **Submit**, then **Continue**.
7. **Repeat for each warehouse.**

> This is a manual re-key from a spreadsheet into a second system, per technician, every month. It is
> the step where the numbers can silently diverge from Pestroutes.

# 3. Run the report

1. `uim2.com/uim-app/reports`.
2. **Orders → Production.**
3. Select the **Warehouse** from the **Location** dropdown.
4. **Create Report** or **Download**.
5. Save to the same End-of-Month folder as step 1.
6. **Repeat for each warehouse.**

# Reading the result

**The 10% target is the whole point** and the source states it in a single line without saying what
happens either side of it — no threshold for intervention, no owner for the conversation, no record
of where the 10% came from.

> Note the system is called **VIM** in the document title and body but the URL is **uim2.com**, and
> the wiki also holds a *"VIM Users-Full Set Up Guide 2023"* PDF and a *"How to Generate Inventory
> Report on VIM"* procedure. Both spellings are in use. The inventory batch will settle it.

> Material usage depends on what technicians draw from inventory, so this metric is only as good as the
> inventory records behind it. The inventory process is covered in a later batch.

# Related

- [Technician production pay](/people/technician-production-pay.md) — the pay side of the same production figures
- [Employee expense accounts](/finance/employee-expense-accounts.md) — only Standard Techs are on production pay
