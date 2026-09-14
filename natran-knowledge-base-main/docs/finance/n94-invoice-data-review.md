---
type: Runbook
title: Reviewing N94 ad data before invoicing
description: The month-end check that verifies the marketing agency's reported Google, Google LSA and Bing spend against the platforms before they invoice for it.
tags: [google-ads, vendor-billing, marketing]
generated:
  by: Claude (Opus 5)
  at: 2026-07-28T04:05:00Z
sources:
  - id: 1TpP0BDqDZ1sK8JupuIRUBM5mSJu9EbaCLOYxSkNJaiU
    resource: https://docs.google.com/document/d/1TpP0BDqDZ1sK8JupuIRUBM5mSJu9EbaCLOYxSkNJaiU/edit
    title: Reviewing N94 Data for invoicing| Natran
status: draft
---

**N94** — also called **SIA N Digital** — is the marketing firm that manages Google, Bing and Facebook
ads for both APS and Natran.

**Every first week of the month** N94 emails a Google Sheet of ads/campaign data, which is the basis
for their invoice. **It is the bookkeeper's end-of-month task to verify that data against the ad
platforms before N94 invoices.**

**When a number does not match:** copy the amount from the platform, paste it over the wrong cell in
the Google Sheet, and **mark the cell yellow** to show it was changed. This is the same correction
rule for all three checks below.

# 1. Google Corp

Open the link in N94's email and go to the tab **NGPC - 01/01/24 to 12/01/24** — the dates shift with
the year.

Compare the **previous month's** figure in **column B** against Google:

1. Log in to Google Ads → **Natran CORP Ads**.
2. **Billing** on the left menu.
3. Scroll to the month being worked on and click it.
4. The **Net cost** should match column B.

# 2. Google Local Services

1. Log in to the [Local Services Ads account](https://ads.google.com/intl/en_us/home/local-services-ads/).
2. Select **Natran Green Pest Control (Dripping Springs)** for **Austin**, or **Natran Green Pest
   Control - Woodlands** for **Houston**.
3. Hamburger menu, top left → **Billing**.
4. In **Transactions**, compare the month's amount against **column C** (Google LSA Austin) or
   **column D** (Google LSA Woodlands).

# 3. Bing

1. Log in to [Microsoft Ads](https://ads.microsoft.com/).
2. **Billing** on the left menu.
3. In **Transaction History**, click the month being worked on.
4. Compare the **Spend Amount** against **column E**.

> **The correction rule only works in one direction.** Every mismatch is resolved by overwriting the
> agency's number with the platform's, which is right if the platform is authoritative — but nothing
> asks *why* the agency's figure differed, and nothing is sent back to N94. A systematic
> over-reporting would be silently corrected every month and never raised. The yellow highlight is the
> only trace.

> The Bing step in the source links to a **session-expired Microsoft Ads redirect URL** carrying
> account, customer and user identifiers in its query string. Replaced here with the plain sign-in URL;
> the identifiers were not copied.

> The agency is named **N94** in the title and body and **SIA N Digital** as an alias, with no
> statement of which is the legal entity that invoices. Minor, but it matters when matching the bill.

# Related

- [Recording ad spend from prepaid to expense](/finance/ad-spend-journal-entries.md)
- [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
