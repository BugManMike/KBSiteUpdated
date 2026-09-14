---
type: Runbook
title: Price increase process
description: The annual and off-schedule subscription price increases — forecasting before and after, flagging accounts, running the increase year by year back to 2011, and notifying customers.
tags: [fieldroutes, pricing, sales]
generated:
  by: Claude (Opus 5)
  at: 2026-09-14T20:17:52Z
sources:
  - id: 1JFewLYTgZSGw6e0edMZzBztLIZS0c6XaWt1Z4S0Pmcg
    resource: https://docs.google.com/document/d/1JFewLYTgZSGw6e0edMZzBztLIZS0c6XaWt1Z4S0Pmcg/edit
    title: Price increase process
status: draft
---

Eligible subscription prices are raised annually, with a second path for off-schedule increases
agreed case by case. **New steps for the off-schedule path were added to the source in August 2024.**

> **Read the rate conflict below before running this.** The source states three different increase
> rates in three places, and they are not reconcilable from the document.

# Step 1. Forecast before

1. In the **price increase** Drive folder, create a subfolder named `YYYY MMM` (e.g. `2024 Jun`).
2. Open the **PRICE INCREASE TEMPLATE** spreadsheet, **make a copy**, rename it
   `YYYY MMM price increase`, and move it into the folder from step 1.
3. In Fieldroutes: **Reporting → Forecast Report**.
4. Extend **Forecast To** date **365 days** ahead.
5. Select **Houston Branch** and **Austin Branch**.
6. Under **Customers**, select **Include Potential Customers** and **Exclude Pending Cancels**.
7. Upload the CSV to the **uploadBEFOREforecast** tab of your copied sheet.
8. Check the **Overview** tab — the before pricing should populate the yellow fields.

# Step 2. Create the scheduled-increase flag

**Admin → Preferences → Customer Preferences → Generic Flags.**

Create a customer flag named **`Price increased YYYY MMM %%`**, substituting the rate, year and month
the increase takes effect — e.g. `Price increased 3.5% 2024 Feb`.

# Step 3. Work out the eligibility date range

**The eligibility date is next month, last year.** Running this in July 2024 makes the first range
August 2023.

> **Then repeat for every year back to 2011.** Fieldroutes reporting requires the range to be run one
> year at a time: August 2023, then August 2022, then August 2021, and so on.

# Step 4. Prepare the report

1. Open the saved report **`PRICE INCREASE TEMPLATE SEE WIKI`**.
2. Open the **Service Appointment** filter.
3. Set **Scheduled For** to the first and last day of the eligibility month from step 3.
4. **Run Report** — the results are the subscriptions eligible for increase.
5. **Save** under Saved Reports to keep the change.

The template already carries these parameters; they are listed for information only.

| Section | Parameter | Value |
|---|---|---|
| Customer Account | Office | Houston Office, Austin Office |
| | Account Status | Active Customers |
| | Exclude Flags | `Exclude customer from all price increases`, `Price increase YYYY MMM %%` |
| Subscription | Active Subscription | Yes |
| | Exclude Flags | `Exclude subscription from all price increases` |
| Service Appointment | Scheduled For | the eligibility range from step 3 |
| | Initial Service | Only Initials |
| | Status | Completed |

**Old exclusion flags should be removed after 12 months** so the account becomes eligible again. The
flagging exists because some services are increased off-schedule, and the flag is what stops them
being increased twice inside a year.

# Step 5. Run the increase

1. Run the step-4 report.
2. **Check the initial dates are the ones you selected.**
3. **Set Show Entries to 10,000.** The price increase tool only acts on subscriptions shown on the
   **first page** of the report.
4. **Actions → Update Subscription Price.**
5. Confirm **Apply to Service Types** is selected and the action is set to **Increase**.
6. Set both **Subscription Base Price** and **Subscription Add Ons** to **% of Recurring Price**.
7. Enter the rate as a bare number (the field rejects the `%` symbol).
8. **Proceed to Verification.** Check the before and after prices.
9. **Confirm Change.**
10. Repeat for each year back to **2011**. Some years will return no eligible subscriptions; **that
    does not mean you are finished** — keep going to 2011.

# Step 6. Flag the accounts

Add the step-2 flag to the report's **Exclude Customer Flag** field, then re-run each year's date
range, using **Actions → Add/Remove Flags** to apply the flag. Continue back to 2011.

# Step 7. Forecast after

Repeat step 1's forecast report, uploading the CSV to the **uploadAFTERforecast** tab.

# Step 8. Create the off-schedule flag

**Admin → Customer Preferences → Generic Flags.** Create a second flag named
**`Price Increased YYYY MMM Off-Schedule Increase`**.

# Step 9. Off-schedule increases

1. Run the saved **`EOM: Price evaluation`** report.
2. Upload it to the **price evaluation worksheet**.
3. **Review the flagged accounts and agree the increases with management.**
4. Increase prices manually on the subscription, **and increase production values to match** — see
   [technician production pay](/people/technician-production-pay.md).
5. Flag the accounts manually.

# Step 10. Clear the evaluation flag

Run the same report, open each customer's **Info** tab, and remove the **Price Evaluation** flag from
the Generic Flag field.

# Step 11. Notify the customer

Send a custom email from the **Price Adjustment Notice Template**, editing the body to name the
service type and the customer's new price.

# Step 12. Schedule the increase 30 days out

**Set a task due in 30 days to apply the price.** The contract requires **30 days' advance notice
whenever a price is increased above 5%.**

# Conflicts in the source

> **Three different increase rates.** The summary box says prices rise **"every year on January 31st
> by 3%"**; step 1 says **"After a year, pricing should be increased by 5%"**; step 5 instructs
> entering **5**. The worked flag example in step 2 uses **3.5%**. **Nobody can run this correctly
> from the document as written.** The rate is the single most consequential value in the procedure
> and it needs one authoritative answer.

> **The notification threshold contradicts itself against the rate.** The summary says customers need
> not be notified **unless the increase is more than 5%**; step 12 says the contract requires 30
> days' notice **whenever a price is increased above 5%**. If the standard increase is 5%, every
> annual run sits exactly on the boundary — and if it is above 5%, steps 11 and 12 are mandatory on
> every account rather than the exception they read as. **This is a contractual obligation being
> decided by an ambiguity.**

> **Annual or monthly?** The summary describes a single annual run on January 31st. The footnote in
> step 4 says *"subsequent price increases were done monthly on eligible subscriptions"*. The
> off-schedule path in steps 8–10 implies a rolling monthly evaluation. The cadence is not stated
> anywhere consistently.

> **The off-schedule flag has two different names.** Step 8 creates
> `Price Increased YYYY MMM Off-Schedule Increase`; step 9 tells you to apply
> `Price Increased YYYY MMM Custom Increase`. One of them is wrong, and a mismatched flag means the
> exclusion in step 4 will not catch the account next year — so it gets increased twice.

> **Step 4's footnote is time-expired.** It says the `Price increase 2024 Feb 3.5%` flag can be
> removed from the saved report **"starting in February 2025"**, and that the instructions can then
> be updated. That date has long passed and neither appears to have happened.

> **Step 5.3 is a trap with no guard.** If Show Entries is left at its default, the tool silently
> increases only the first page of results and reports success. Nothing in the procedure verifies
> afterwards how many subscriptions were actually changed — the step-7 forecast would show a smaller
> increase than expected, but the document never says to compare it against anything.

**Screenshot and video loss.** The source embeds a Loom walkthrough. The Drive read returns text
only.

# Related

- [Setting sales expectations in the budget](/finance/sales-expectation-budgeting.md)
- [Technician production pay](/people/technician-production-pay.md)
- [Approved coupon codes](/finance/coupon-codes.md)
- [11-month customer retention credit](/finance/retention-credit-11-month.md)
