# Corpus Update Log

## 2026-09-14 — batch 4c

Wiki `/Accounting/Processes` again — the flat folder that also held 4a and 4b. **19 new concepts**,
all `status: draft`: 9 to [/people/](/people/), 8 to [/finance/](/finance/), 1 to
[/operations/fleet/](/operations/fleet/), and 1 to a **new [/sales/](/sales/) domain**. With the new
`sales/index.md`, the bundle goes from **147 to 167** markdown files across 13 directories.

Scope was compensation and payroll, procurement, the five documents left needing a routing decision,
and the four month-end journal-entry documents batch 4a appears to have missed.

**OKF spec check:** the raw `SPEC.md`, fetched with a cache-busting query string, declared
**v0.2**. That is the fourth check and the second to agree with the pin; the 2026-07-29 entry
recorded a v0.1 reading. Pin unchanged. OQ-001 stays open.

### Compensation and payroll → `/people/`

* **Creation**: [Calculating salesperson commissions](/people/sales-commission-calculation.md) — the
  Commission Worksheet, prior-period initials, commission profiles, and the chargeback exclusions.
* **Creation**: [Biweekly payroll checklist](/people/payroll-checklist.md) — Monday timecards, then
  the unsigned-agreement, collect-or-do-not-service and production reports.
* **Creation**: [Payroll journal recording](/people/payroll-journal-recording.md) — the Gusto journal
  to QuickBooks entry, GL coding by role and branch, advances, child support, commission split.
* **Creation**: [Processing missed pay](/people/missed-pay-processing.md) — PrismHR net pay
  calculator, then the paired retro-pay and advance entries.
* **Creation**: [Calculating a technician's PTO rate](/people/technician-pto-rate.md) — twelve months
  of wages less bonuses, divided by 2080.
* **Creation**: [Lead referral bonus](/people/lead-referral-bonus.md) — the Sales Rep 3 credit and
  the two Fieldroutes commission profiles.
* **Creation**: [Overtime alerts in uAttend](/people/overtime-alerts.md).
* **Creation**: [401(k) participant administration](/people/401k-contributions.md) — add, deactivate,
  terminate, and the per-cycle contribution submission.
* **Creation**: [Virtual assistant sign-up and invoicing](/people/virtual-assistant-onboarding.md) —
  W-8BEN, a US-dollar receiving account, and the invoice route per company.

### The 4a leftovers, now converted → `/finance/`

Confirmed genuinely missing rather than folded into
[month-end bookkeeping review](/finance/month-end-bookkeeping-review.md), which references all four
topics in steps 3, 7 and 8 but carries none of the procedures.

* **Creation**: [Booking monthly depreciation](/finance/depreciation-monthly.md).
* **Creation**: [Journalizing vehicle loan interest](/finance/vehicle-loan-interest.md).
* **Creation**: [Journalizing SBA loan interest](/finance/sba-loan-interest.md).
* **Creation**: [Checking P&L transactions have classes](/finance/pl-class-assignment.md).

### Budgeting and the routing-decision documents

* **Creation**: [Sentricon install budgeting](/finance/sentricon-install-budgeting.md).
* **Creation**: [Setting sales expectations in the budget](/finance/sales-expectation-budgeting.md).
* **Creation**: [Approved coupon codes](/finance/coupon-codes.md).
* **Creation**: [Technician check collection](/finance/technician-check-collection.md).
* **Creation**: [Budgeting for a vehicle purchase](/operations/fleet/vehicle-purchase-budgeting.md).
* **Creation**: [Price increase process](/sales/price-increase-process.md), and the new
  [/sales/](/sales/) index.

### The duplicate resolved

**Three documents describe calculating sales commissions, and they split two-to-one against a
spreadsheet, not a vintage.** *Sales Commission* (June 2023) and *Sales commission proces* *(sic)*
(May 2023) are near-identical to each other and drive the **Natran sales commission report** sheet;
both carry their own "this article is in need of updates" banner. *How to calculate salesperson
commissions* (January 2024) drives a **different** spreadsheet, the **Commission Worksheet**, with
different tabs and a `commissionProfile` rate table the older pair has no equivalent for.

The 2024 document was taken as canonical — newest, and the only one not self-flagged as stale. The
two 2023 documents were **not** converted. **But they are not simply superseded**: they hold the
full step-by-step for importing the Fieldroutes reports, which the 2024 document replaces with a
link to an external Scribe recording. That procedure now exists only against a spreadsheet that may
be retired. Flagged in-file; payroll to confirm which sheet is live.

This is the batch-4a pattern again — apparent duplicates that are different vintages, neither
complete — with the twist that the *newer* one is the thinner one.

### Already converted, not repeated

**`Expense accounting for departments` was converted in batch 4b** as
[employee expense accounts](/finance/employee-expense-accounts.md) — same source ID. It appeared on
the 4c list as needing a routing decision; no action was needed. Listed here so the next batch does
not re-check it.

### Two earlier flags resolved by this batch's sources

* [Employee referral bonus](/people/employee-referral-bonus.md) asked whether the Accounting-folder
  *Referral bonus* document described the same scheme. **It does not** — it is a customer-lead
  referral, now [lead referral bonus](/people/lead-referral-bonus.md). The cross-reference block was
  rewritten to record the answer. The $2,000 figure remains unverified against payroll, because
  nothing in the accounting corpus implements it at all.
* [Waiving fees and applying account credit](/finance/applying-account-credit.md) said no reason was
  recorded for a credit. **Half-answered** by [approved coupon codes](/finance/coupon-codes.md) — a
  reason *is* coded, in a field that procedure already fills in. The approver still is not. Flag
  amended rather than removed.

### Personal and financial data found in sources

**No values were copied into this repo.**

* **`Technician check collection process` names the company's deposit bank account number in plain
  text**, in a page readable by every technician. Redacted here; the source needs it removed.
* **`VA Sign-up and Invoicing process-Finance` routes every new contractor through one employee's
  personal Wise referral link**, which pays that employee. It also instructs the contractor to email
  bank account and routing numbers to two individuals, named personally rather than by role.
* `How to Journalize interest entries for SBA Loan` works through a specific month with the loan's
  payoff balance and monthly payment. Described as a method with the figures marked as one month's
  example.

### Conflicts and defects found

**The price increase process is the worst document the ingestion has converted.**

* **Three different increase rates in one document** — 3% in the summary, 5% in step 1, 5 entered in
  step 5, and 3.5% in the worked flag example. Nobody can run it correctly as written.
* **The notification threshold sits exactly on the rate.** Customers need not be told unless the
  increase exceeds 5%; the contract requires 30 days' notice above 5%; the instruction is to enter
  5. Whether steps 11 and 12 are mandatory on every account turns on an ambiguity.
* **Annual or monthly is unresolved** — the summary says one annual run, a footnote says subsequent
  increases were monthly, the off-schedule path implies a rolling evaluation.
* **The off-schedule flag has two different names**, created in step 8 and applied in step 9. A
  mismatch means the account is not excluded next year and gets increased twice.
* **Step 4's footnote expired in February 2025** and neither the report nor the instructions were
  updated.
* **Step 5.3 is an unguarded trap** — leave Show Entries at the default and the tool silently
  increases only the first page while reporting success.

Elsewhere:

* **`Payroll checklist` has broken step numbering** (Step 1, Step 2, Step 1, Step 3), **is cut off
  mid-sentence** naming the second folder to create, and **ends on a bare heading**, "Monthly sales
  commission and referral bonuses", with no content under it.
* **`Balancing sales department expectations` ends mid-sentence**, numbers two different steps 3, and
  titles one "Sep 2".
* **`Budgeting for vehicle purchase and setup` is labelled a work in progress and stops** at "You
  should see the following notes:". Its opening sentence still contains the placeholder "you will be
  setting X entries".
* **`Budget for Sentricon Installs` skips step 3** and hardcodes a $295 unit cost, last touched in
  2022, with no stated source.
* **401(k) terminations are filed with "Termination Reason: Permanent Layoff" as a constant**, for
  every departure.
* **Depreciation is derived from loan principal movement rather than an asset schedule**, which
  breaks for any vehicle bought outright, paid off, or on a term other than five years — while the
  budget process assumes a `depreciationSchedule` tab that the books never read.
* **`Natran Payroll Recording Process` step 6 asks a bookkeeper to hand-edit formulas in a tab named
  "JE for Upload - Do NOT edit"**, every cycle, with the only check being a balance test that would
  still pass if Houston and Austin were swapped.

### The corpus-wide finding this batch sharpens

**There are four payroll or timekeeping systems, not three.** `PROJECT-TODO.md` records Gusto,
uAttend and PrismHR. This batch adds a **PEO** whose "Detail Deductions by Deduction Code" report is
the authority for 401(k) contribution amounts. So: payroll runs in **Gusto**, time is kept in
**uAttend** (on an **Advantage Pro Services** tenant), wage history for PTO rates comes from
**PrismHR**, and benefit deductions come from a **PEO** report. No document states the relationship
between any two of them.

### Vocabulary added

Recorded in `CLAUDE.md` as well as here.

* **System**: `prismhr`, `principal`, `wise`.
* **Topic**: `budgeting`, `pricing`, `commissions`.

### New domain created

**`/sales/`**, holding [price increase process](/sales/price-increase-process.md). Created rather
than deferred because pricing is explicitly a `sales/` subject under the placement rule in
`CLAUDE.md`, and the directory now has real content rather than scaffolding. Batch 6 fills it out.
[Setting sales expectations in the budget](/finance/sales-expectation-budgeting.md) was filed under
`finance/` instead, with the other budget-model procedures; **that placement is flagged in-file for
reconsideration in batch 6.**

### Deviation from the plan, recorded

`HANDOFF.md` routed **`Budget for Sentricon Installs`** to `operations/fleet/`. It was filed to
`finance/` instead: it is a materials-cost budget entry with no fleet content, and it sits beside the
two existing Sentricon billing concepts. `Budgeting for vehicle purchase and setup` went to
`operations/fleet/` as planned.

`HANDOFF.md` also listed **`Balancing sales department expectations`** under compensation. It is not
compensation — it is sales capacity and quota planning in the budget model. Filed accordingly.

### Not converted

* **`Sales Commission`** and **`Sales commission proces`** — superseded duplicates, see above.
* **`[Scorecards Core Process]`**, **`[Accounts Payable Core Process]`**, **`[Bookkeeping Core
  Process]`**, **`[Financial Modeling Core Process]`** — 1024-byte link stubs pointing into
  `Natran Core Processes`, the document OQ-005 names as its forcing point.
* **`Natran Law Inside Sale 11/21`** and **`Account Receivable Process`** (two documents of that
  title) — outside batch scope; they belong with the receivables cluster already converted in 4a, and
  should be checked against it in a later pass rather than opened here.

## 2026-07-29 — Collect or Do Not Service split into its own concept

**No new source material.** A refactor of existing batch-4b content to satisfy the
one-concept-per-file rule. **1 new concept to [/finance/](/finance/)**, `status: draft`.

* **Creation**: [Holding service on past-due accounts](/finance/holding-service-past-due-accounts.md) —
  the daily *Collect or Do Not Service* loop, lifted verbatim out of
  [accounts receivable daily operations](/finance/accounts-receivable-daily.md): flag the past-due
  appointment off `Audit - Past due appointment`, custom-date the unserviced subscription out of the
  job pool off `Audit - Appointment Collect Flag`, then remove the custom date once the balance
  clears off `Audit - Collection Custom Date`.
* **Update**: `accounts-receivable-daily.md` keeps its `# Hold service on past-due accounts` heading
  as a pointer rather than dropping it, so the daily cadence still reads complete, and its
  `description` no longer claims the material. Both source document IDs were **carried onto the new
  concept as well as left on the parent** — the split does not resolve which of the two same-titled
  Drive docs is the 2026 version, so both remain provenance for both files.

**Both existing source-defect flags travelled with the content**: the unresolved
invoice-age-vs-account-age conflict (15 days past due vs. residential 30 / commercial 45), and the
note that the third sub-process is the one that gets forgotten. Neither was silently fixed.

**One `TODO:` marker added** — the field half of the process is genuinely undocumented. Nothing in
the corpus covers technician training, what the appointment card shows, or what happens when a flagged
account is serviced anyway. Recorded as a TODO pointing at Linear NLDR-100 rather than written from
inference; the meeting record that discusses it (several 2026-05 to 2026-07 L10s and one-on-ones) is
not a source document and was **not** transcribed into the concept.

**No new vocabulary.** `type: Runbook` and `tags: [fieldroutes, receivables]` match the sibling
collections concepts.

**OKF spec check anomaly, third occurrence**: the canonical raw SPEC.md declared **v0.1 — Draft**
again today, contradicting the 2026-07-28 note in `DECISIONS.md` that closed OQ-001 on the grounds
that `main` had reached v0.2. The cache-busting query string was stripped by a redirect, so a stale
render cannot be ruled out. Surfaced before writing; decision was to **stay pinned at v0.2**, per
Michael. The pin in `CLAUDE.md` is unchanged and OQ-001 is reopened.

## 2026-07-28 — n8n notification workflows

**Source: the live n8n instance** (`n8n.srv1090686.hstgr.cloud`), not the wiki — parameters read
directly from the two saved workflow definitions. **3 new concepts, all to
[/it/automation/](/it/automation/)**, a new directory created by this batch. All `status: draft`.

* **Creation**: [Email → Google Chat notification design](/it/automation/email-to-chat-notification-design.md) —
  the shared design: why IMAP on keeping@natran.com rather than the office@natran.com Google Group,
  why an app password rather than OAuth, the `[@.]keeping\.com` sender-exclusion regex, duplicate
  suppression and its re-testing gotcha, phone-link convention, troubleshooting.
* **Creation**: [HubSpot form → Chat notification workflow](/it/automation/hubspot-form-chat-notification.md) —
  subject `New Form Submission`, 3-minute wait, body trimmed at "View at HubSpot", 800-char cap.
* **Creation**: [Tech referral form → Chat notification workflow](/it/automation/tech-referral-chat-notification.md) —
  subject `TECH REFERRAL FORM`, 1-minute wait, full body posted, 3500-char cap.

**New system tag: `n8n`** — recorded in `CLAUDE.md`. The workflows post to Google Chat, but the
entry-point rule puts the system tag where the task starts.

**Secrets redacted per content rules**: the Chat webhook URL (carries `key`+`token`) is written as
`<GOOGLE_CHAT_WEBHOOK_URL>`, the mailbox app password as `<IMAP_APP_PASSWORD>`; the Chat space is
identified by space ID only.

**Source defect flagged in-file**: the HubSpot workflow's message-body From/To extraction lacks the
`headers.*` fallbacks the tech-referral workflow has — drift, not intent; flagged in the HubSpot
runbook rather than silently reconciled.

**OKF spec check anomaly**: the canonical raw SPEC.md, fetched with a cache-busting query string,
declared **v0.1 — Draft** (older than the pinned v0.2, missing the `generated`/`status`/`sources`/
`verified`/`stale_after` families). Surfaced before writing; decision was to **stay pinned at v0.2**.
The pin in `CLAUDE.md` is unchanged.

## 2026-07-28 — batch 4b

**Wiki `/Accounting/Processes`** — payables, tax, vendor billing, and credit and write-offs.
**29 new concepts, all to [/finance/](/finance/).** All `status: draft`.

**30 source documents in, 29 concepts out** — two credit-card documents collapsed into one. Every
source in scope was convertible; **nothing was rejected as unconvertible.** The four documents the
batch-4b plan expected to be link stubs on the basis of their 1024-byte size — franchise tax, W-9/1099,
waiving late fees, sorting Divvy charges — all turned out to hold **real content**. File size is not a
reliable stub signal in this tree.

**Creations — payables** (12): [where vendors send invoices](/finance/invoice-submission-address.md);
[forwarding vendor invoices into Bill.com](/finance/bill-com-invoice-intake.md); [entering a bill from
the Bill.com inbox](/finance/bill-com-bill-entry.md); [processing bill payments in
Bill.com](/finance/bill-com-bill-payments.md); [setting up vendor payment details in
Bill.com](/finance/bill-com-vendor-payment-setup.md); [uploading King Ranch
bills](/finance/king-ranch-bills.md); [paying and recording the Chevron fuel
bill](/finance/chevron-fuel-bill.md); [recording ad spend from prepaid to
expense](/finance/ad-spend-journal-entries.md); [reviewing N94 ad data before
invoicing](/finance/n94-invoice-data-review.md); [attaching Divvy
receipts](/finance/divvy-receipt-attachment.md); [splitting Divvy materials
charges](/finance/divvy-materials-split.md); [health benefit vendors](/finance/health-benefit-vendors.md).

**Creations — tax** (4): [recording sales tax](/finance/sales-tax-recording.md); [filing and paying
sales tax](/finance/sales-tax-filing.md); [franchise tax payment](/finance/franchise-tax-payment.md);
[W-9 collection and 1099 filing](/finance/w9-1099-filing.md).

**Creations — vendor billing** (2): [submitting Sentricon renewals to
Corteva](/finance/sentricon-renewal-billing.md); [submitting Sentricon installations to
Corteva](/finance/sentricon-initial-billing.md).

**Creations — credit, fees and write-offs** (11): [applying late fees and
interest](/finance/late-fees-and-interest.md); [waiving fees and applying account
credit](/finance/applying-account-credit.md); [weekly credit report](/finance/weekly-credit-report.md);
[11-month customer retention credit](/finance/retention-credit-11-month.md); [refunding partial
payments](/finance/partial-payment-refunds.md); [recording bad debt](/finance/bad-debt-recording.md);
[expiring credit card notification](/finance/expiring-credit-card-notification.md); [handling returned
ACH payments](/finance/returned-ach-payments.md); [chargeback dispute and
rebuttal](/finance/chargeback-disputes.md); [Transworld dispute
process](/finance/transworld-disputes.md); [lien notice process](/finance/lien-notices.md).

### The duplicate confirmed

**`Expiring credit card notification` and `The Expired Credit Card Processs` are the same process.**
The batch-4b plan flagged them as probable duplicates and they are — same report path, same purpose.
Written from the **2025** version; the **2022** version is recorded as superseded inside
[expiring credit card notification](/finance/expiring-credit-card-notification.md). The older one gives
a **different customer callback number** and signs off from a **named individual with a job title**
rather than from Customer Care, which is the reason it should not be reused. **The older source should
be deleted or marked superseded at source.**

### Personal and customer data found in sources

* **[Lien notice process](/finance/lien-notices.md) — the worst of it.** The lien notice template is
  stored not as a blank form but as a **sent letter**, carrying a real customer's **service address,
  balance and overdue date**. Replaced with bracketed placeholders; **the source needs cleaning**,
  because anyone working quickly could send the next notice with the previous customer's details in it.
* The **Chevron fuel account number** and the identifier of the **paying bank account** — described by
  role, not copied. Consistent with batch 4a.
* A **Divvy card's last four digits** — referred to here as "the second Divvy Visa account".
* Vendor **bank and routing numbers** in the Bill.com vendor setup — the procedure is recorded, the
  values are not.
* [Reviewing N94 ad data](/finance/n94-invoice-data-review.md) linked a **Microsoft Ads session URL
  carrying account, customer and user identifiers** in its query string. Replaced with the plain
  sign-in URL.
* [W-9 collection and 1099 filing](/finance/w9-1099-filing.md) is noted rather than flagged: the
  process necessarily puts **taxpayer identification numbers** into QuickBooks and signed W-9s into a
  Drive folder. Ordinary practice — but that folder's access scope is now a known question.

### Conflicts and defects found

* **Franchise tax is described as monthly.** Texas franchise tax is **annual**, due 15 May. The
  cadence a bookkeeper would take from this document is wrong, and
  [the accounting schedule](/finance/accounting-schedule-of-events.md) is where they would look.
* **The bad-debt branch filter names "Natran Branch"**, where the whole rest of the corpus uses
  **Houston** and **Austin**. It decides which office's bad debt gets booked.
* **`Trade`, the fake customer, now carries two unrelated month-end adjustments** — the AR
  ending-balance plug flagged in batch 4a and the bad-debt credit memo found here.
* **Two phone numbers in one customer email.** The NSF notice gives 713-900-1994 in the body and
  713-868-5588 ext. 3 in the signature.
* **The NSF email tells the customer auto-pay has been deactivated, but no step deactivates it.** The
  chargeback procedure has an explicit step for this; the ACH one does not.
* **Chevron payment type is "Check" while its reference number is "ACH".** Reconciliation matches on
  payment type.
* **Ad-spend entries are dated inconsistently** — the 1st of the month for Google and Bing, the last
  day for Google Local Services, for the same monthly close.
* **Google Local Services spend debits the same expense account as search spend** (`6025`), so the two
  channels cannot be separated on the P&L.
* **The 11-month retention credit applies its double-credit-prevention flag last**, after the coupon
  and the email; an interrupted run leaves credited accounts unflagged. Its two flags also differ only
  as **`MNT` against `MTH`**.
* **Sentricon renewals default to "Select All"** and require manual exclusion of pending cancels, which
  is the unsafe ordering.
* **Late fees are charged before interest is calculated on the balance**, so the month's $35 fee is
  inside the 1.5% base.
* **Late fees stop at 365 days overdue** with no explanation of what happens above that.
* **The Transworld fallback substitutes a completed service document for a missing signed agreement.**
  A service document proves service, not agreed price or term — the same gap that sinks a chargeback
  rebuttal.
* **The lien notice asserts statutory lien rights** under Texas Property Code §§53.056–53.058 and
  threatens litigation, with **no legal review step anywhere in the process**. Recorded as found;
  flagged for counsel.
* **"TextNet"** for the state payment system, which is **TEXNET**. Left as written — the on-screen label
  is what a new bookkeeper matches against.
* **The sales tax portal is called the "Franchise Tax Payment Portal"** in the sales tax procedure.
* **Weekly credit runs weekly against a month-to-date range**, so each report re-sends everything
  already reported.
* **Approval is the undocumented step in payables.** [Processing bill
  payments](/finance/bill-com-bill-payments.md) filters on **Approved** without anything saying who
  approves, against what limit, or how a bill gets there. The same hole appears on the credit side:
  neither [applying account credit](/finance/applying-account-credit.md) nor
  [weekly credit](/finance/weekly-credit-report.md) records a reason, an approver or a limit for a
  waiver.
* **Two procedures name a person by first name only** and no role — the weekly credit recipient and the
  lien notice signatory. Recorded by inferred role, with the gap flagged in-file.
* **A third health-benefit vendor pair.** [Health benefit
  vendors](/finance/health-benefit-vendors.md) names two; batch 4a found six in the allocation
  procedure and two different ones in HR's benefits calendar. **Still no authoritative list.**

### Titles that do not match their contents

Three sources were filed under what they actually contain, with the original title preserved in-file:

* **`How to waive late fees in Pestroutes`** contains the general coupon/credit mechanism with no
  late-fee-specific step → [waiving fees and applying account
  credit](/finance/applying-account-credit.md).
* **`How to Pay Health Benefit Vendors`** contains **no payment procedure at all** — only two vendor
  descriptions. Filed as a `Reference`. **The health-benefit payables procedure remains undocumented.**
* **`Payment Details Setup in Bill.com Process`** numbers its second section **"Step 21"**.

### Content lost or missing at source

* **[Refunding partial payments](/finance/partial-payment-refunds.md) ends on "Here's an example:" with
  nothing after it.** The account note is the only thing explaining a reversal, a discount and a coupon
  sitting on one account, and it is the part nobody wrote down.
* **[Attaching Divvy receipts](/finance/divvy-receipt-attachment.md)** ends on an empty "Examples"
  heading.
* Screenshot loss again, as in batch 2: the Sentricon, Chevron and Bill.com procedures were written
  against interface screenshots that a text read does not return.
* A **Scribe walkthrough** embedded in the chargeback procedure. Its steps were written out in full
  instead.

### Vocabulary added

Thirteen values, all recorded in `CLAUDE.md` as part of this batch.

**System** (6): `bill-com`, `authorize-net`, `transfirst`, `transworld`, `chevron`, `google-ads`.
**Topic** (7): `payables`, `tax`, `vendor-billing`, `credit`, `refunds`, `disputes`, `write-offs`.

`corteva` was **deliberately not added** — the Sentricon procedures are operated inside Fieldroutes and
Corteva is the counterparty, not a system anyone signs into. Same reasoning kept `king-ranch` out.

**The tagging rule this batch settled:** where a procedure spans two systems, the system tag is **the
entry point** — the one the task starts in. So returned ACH payments is `authorize-net` (the return is
discovered there) while the Sentricon submissions are `fieldroutes` (the Sentricon UI lives inside it).

`CLAUDE.md`'s recorded tag list had also **drifted behind actual usage** — `quickbooks`, `bookkeeping`,
`receivables`, `divvy`, `jazzhr`, `vehicles` and `sales` were all in the corpus but not in the
vocabulary table. Brought current in the same edit.

### Noted, not converted

**Four month-end journal-entry documents in this source folder appear never to have been converted**,
and they belong to the batch-4a close cluster rather than to 4b: `How to Book Depreciation every
month`, `Journalize interest entries for Vehicle payments`, `How to Journalize interest entries for SBA
Loan`, and `How to check all P&L transactions have classes`. **Left for a decision** rather than pulled
into this batch — flagged in `HANDOFF.md`.

`VA Sign-up and Invoicing process-Finance` was also left: it covers the hiring side of the contractors
whose payment setup is in [Bill.com vendor payment
setup](/finance/bill-com-vendor-payment-setup.md), and belongs with VA onboarding.

The ACH/eCheck refund procedure that [refunding partial
payments](/finance/partial-payment-refunds.md) links to sits outside this folder and was not converted,
so only the Fieldroutes side of that process is in the bundle.

## 2026-07-28 — batch 4a

**Wiki `/Accounting`** — the `wiki.page` schedule, the month-end close cluster, receivables and
collections, and `Roles/B&P Agent`. **16 new concepts.** Creates **[/finance/](/finance/)**. All
`status: draft`.

Batch 4 was 82 files, so it is split three ways. **4a is the close-and-receivables cluster**; 4b is
payables, tax and vendor billing; 4c routes compensation to `people/` and procurement to
`operations/fleet/`.

**Creations — [/finance/](/finance/)** (15): accounting schedule of events; month-end bookkeeping
review; accounts receivable close; revenue recording; clearing uncategorized expenses; corporate
class proration; intercompany transactions; health benefit allocation; employee expense accounts;
accounts receivable daily operations; collections calling process; collections call and text
scripts; sending accounts to collections; DSO tracking; A/R and payroll agent duties.

**Creations — [/operations/](/operations/)** (1): [production vs
materials](/operations/production-vs-materials.md) — filed to operations rather than finance because
the 10% material-usage target judges technician performance, not the books.

### An earlier conclusion corrected

**RingCentral is not retired.** [Month-end bookkeeping review](/finance/month-end-bookkeeping-review.md)
step 15 splits the RingCentral charge between Natran and APS **per user, every month**. Batch 2 had
flagged RingCentral as probably superseded by CTM because no migration was recorded anywhere; a live
monthly cost allocation says otherwise. The likely answer is that **both systems run** — CTM for call
handling, RingCentral for extensions or desk phones. Noted in
[RingCentral voicemail setup](/it/telephony/ringcentral-voicemail-setup.md); the question shifts from
"is this dead?" to "what is each system for?"

### The duplicate resolved

The two identically titled `Account Receivable Process` documents flagged in the batch-1 inventory
**are not copies.** The 2026 version adds three daily past-due sub-processes and an equipment-recovery
step; the 2023 version has the TSI submission procedure and a Wednesday/Friday 9 am cadence the newer
one dropped. **Neither is complete.** Split across
[accounts receivable daily operations](/finance/accounts-receivable-daily.md) and
[sending accounts to collections](/finance/sending-accounts-to-collections.md), with the differences
flagged at each point.

### Conflicts found

* **Two collection agencies.** TSI has a full submission procedure; ARM is where the calling process
  says debt goes at day 100. The 2026 AR document names **both** — TSI in its intro, ARM in its body.
  This decides where customer debt is sent.
* **The DSO target contradicts the metric.** The collections process cites Investopedia's standard DSO
  definition then states a target of **3 to 4 days**, which is off by roughly an order of magnitude for
  a business billing monthly. The number is being used to judge performance.
* **Three collections timelines** — a day-90/day-100 table, a "freeze after 90 days" FAQ answer, and a
  "weekly for 8 weeks" instruction, which is 56 days.
* **Six health-benefit vendors here, none of which match the two named in the HR benefits calendar.**
  Between [health benefit allocation](/finance/health-benefit-allocation.md) and [benefits
  enrolment](/people/benefits-enrolment.md) there is no complete list of what the company offers.
* **Outside Sales is marked "not currently active"** in the expense account table — while a full
  [PTO — outside sales](/people/pto-outside-sales.md) policy exists and recruiting templates advertise
  the role with on-target earnings.
* **Past-due service holds use two different measures** — 15 days past due, and residential 30 / commercial
  45 days on the account — without saying how they combine. It decides whether a customer gets serviced.
* **The AR ending-balance adjustment is a plug** posted as an invoice against a fake customer named
  `Trade`, with no tolerance check and nothing asking why the variance exists.
* **The monthly checklist is not in dependency order** — the Corporate proration must run last, and its
  own procedure says so in capitals, but the schedule does not.

### Notes

`BAD DEBIT` is a typo for *BAD DEBT* in both AR documents and was **left as written** — it is the
literal string in existing records, and [DSO tracking](/finance/dso-tracking.md) filters on it.

A named employee's health premium and split percentage appear as a worked example in the source;
**the individual and the amount were not transcribed**, only the mechanism. Chevron and bank account
numbers likewise described rather than copied.

`/Roles/B&P Agent` was converted despite being four systems out of date — it references **ServiceCEO**,
the pre-Pestroutes platform, and is the only document describing that role end to end. Four of its
duties have no current owner anywhere in the corpus.

## 2026-07-28 — company KB merged into the bundle

**`content/` merged into `docs/`. The bundle is now the only documentation tree in the
repo.** Resolves the open item `PROJECT-TODO.md` had carried since the second tree was
created; reasoning in `DECISIONS.md` under OQ-009.

**No concepts were added or changed.** `content/` held eight files and no real content —
four section landing pages and four pages whose entire body read *"TODO: replace this
placeholder with the first real page."* Its four sections already matched domains the
bundle was growing.

* **Update**: Removed `content/`, `taxonomy.yml`, `_templates/` and `CHANGELOG.md`.
  `docs/log.md` — this file — is now the single history for the corpus.
* **Update**: The four section descriptions were folded into
  [/it/](/it/), [/operations/](/operations/) and [/people/](/people/). The fourth,
  `finance`, was **not** scaffolded — a directory is created by the batch that fills it,
  so `finance/` arrives with batch 4 rather than existing as an `index.md` listing
  nothing.
* **Update**: `CLAUDE.md` lost its two-contract preamble and its entire "Company KB"
  section, and gained a **Root domains** table and a **Content rules** section. `README.md`
  rewritten to describe one tree.
* **Update**: **Per-document access control is retired.** `content/people` had been gated
  to `[leadership, hr]` and `content/finance` to `[leadership, finance]`. OKF v0.2 cannot
  express that, and per Michael the gating is dropped rather than carried as
  project-specific frontmatter — access is controlled at the repository level, so every
  concept here is equally restricted. The `leadership` / `hr` / `finance` role vocabulary
  goes with it.
* **Update**: **One rule was promoted rather than lost.** *"Never store secrets or personal
  data — no SSNs, bank/account numbers, home addresses, passwords, or API keys"* previously
  applied to `content/` only. It is now a bundle-wide content rule. Batch 3 found a fuel PIN
  derived from Social Security numbers and shared passwords emailed in plaintext, so the
  rule now covers the tree where that material actually lands.

The status-value collision `CLAUDE.md` used to warn about is gone. Only OKF's
`draft` / `stable` / `deprecated` remain — no more `draft → review → published`.

## 2026-07-28 — batch 3

**Wiki `/Human Resources`** — the root files, `/Safety`, `/Other Resources`, `/HR Forms` and
`/QualityPro Certifications`. **27 new concepts.** All `status: draft`.

Creates two new root domains: **[/people/](/people/)** and **[/operations/](/operations/)**.
`operations/` currently holds only `fleet/`; the rest arrives in batch 7. Renamed from
`field-ops/` per Michael before anything was written.

* **Update**: `type: Template` used for the first time, on the two template libraries. With
  `Script` used in batch 2, both additions from OQ-007 now have real usage.
* **Update**: Tags gained 5 system values (`gusto`, `uattend`, `jamf`, `wex`, `npma`) and 19
  topic values. Recorded in `CLAUDE.md`.

### The security finding

**[HR email templates](/people/hr-email-templates.md) contains four security problems in its
source, and none of their values were copied into this repository.** Described in the file so
they can be fixed:

1. **The fuel PIN is the last four digits of the employee's Social Security number.** The same
   template instructs the employee not to share it.
2. **A shared default password is emailed in plaintext**, reused across Fieldroutes, NPMA and
   TPCA. A second covers KnowledgeVine; a fixed access code covers the respirator questionnaire.
3. **The Houston back door code is emailed in plaintext** to new hires' *personal* addresses, and
   no offboarding template rotates it.
4. **Two templates were saved with a real employee's name, username, password, phone number and
   email still in them.**

Also: the [employee file worksheet](/people/employee-file-worksheet.md) template has **a real
surname left in the Last name field**, and collects SSN and date of birth on paper.

### How the two signed documents were handled

The **Employee Handbook** (~50 policies) and the **New Employee Agreement** are signed
instruments. Shredding either wholesale would create a second copy of a signed legal document
that can drift from the original — OQ-005's problem with legal consequences attached.

**So the extraction was selective**: operational policy came out, legal terms stayed in place, and
both documents are fully mapped. See [employee handbook
map](/people/employee-handbook-map.md) and [employee agreement
map](/people/employee-agreement-map.md), which each say what was taken and what was left.
**This is a judgment call, not a rule from the brief** — say so if you would rather have them
shredded completely.

The Employee Agreement turned out to be the densest compensation source in the wiki. **The
technician production pay formula exists nowhere else** — see [technician production
pay](/people/technician-production-pay.md).

**Creations — [/people/](/people/)** (22): employee handbook map; employee agreement map;
employment classification, hours and pay; technician production pay; employee file worksheet;
attendance and punctuality; requesting time off; logging an attendance event; PTO office hourly;
PTO outside sales; holiday policy; benefits enrolment; employee service discount; employee
referral bonus; injury and incident response; uniform and dress code; mobile device policy; pet
policy; recruiting SMS templates; HR email templates; QualityPro certification registration;
QualityPro Public Health study materials.

**Creations — [/operations/fleet/](/operations/fleet/)** (4): [vehicle use
policy](/operations/fleet/vehicle-use-policy.md); [driver fuel
policy](/operations/fleet/driver-fuel-policy.md); [Wex fuel card
setup](/operations/fleet/wex-fuel-card-setup.md); [equipment and inventory
responsibility](/operations/fleet/equipment-and-inventory-responsibility.md).

**Creations — [/it/](/it/)** (1): [Fieldroutes access control
profiles](/it/fieldroutes-access-control-profiles.md). This closes the dependency batch 2 left
open — [Fieldroutes user setup](/it/fieldroutes-user-setup.md) step 2 had no guidance attached.
Its most useful line: **`Default Technician` is the Austin profile**, which the name does not
suggest.

### Filing corrections

Four Employee Agreement sections were filed to `operations/fleet/` rather than `people/`, because
fleet operations own them even though the employee signs them: vehicle use, driver fuel, equipment
and inventory. The **Wex fuel card** procedure moved out of the wiki's HR folder for the same
reason — the fuel PIN is the control in the driver fuel policy.

### Conflicts found

* **Time-off notice has three different rules** — 2 hours before shift (handbook), one hour before
  shift (both PTO policies), Monday before payroll (Gusto). They answer the same question
  differently and are not reconcilable as a sequence. Set out in [attendance and
  punctuality](/people/attendance-and-punctuality.md).
* **Three timekeeping systems** — Gusto, uAttend, and EOSG/PrismHR — with no statement of which is
  authoritative for what. The handbook adds a fourth reference to an unnamed "employee portal", and
  onboarding tells new hires their paystubs are in EOSG while the device setup says Gusto Wallet.
* **The uAttend tenant belongs to Advantage Pro Services**, not Natran — the URL is
  `v2.trackmytime.com/advantagepro`.
* **Injury drug testing** — the handbook makes a screen mandatory for *every* work-related injury;
  the safety document conditions it on treatment being received.
* **Injury treatment path** — the safety document sends employees to CareNow; the Employee
  Agreement requires a doctor from the insurance network and warns the employee may pay the bill
  otherwise. Whether CareNow is in-network is nowhere stated.
* **The outside sales PTO table has no 2–3 year tier**, its prose grants five flex days while its
  table omits them, and its signature block still says *"Office Employee Time Off Policy"*.
* **Busy season** is March–August in the handbook and office policy, but March–May and
  October–December for outside sales.
* **Holiday pay eligibility excludes technicians** — only exempt salaried staff and full-time
  hourly office staff qualify. Stated plainly, so it appears deliberate, but never called out as
  such.
* **The uniform and dress code policy exists in both signed documents** in near-identical wording.
* **Two legal entity names** — *Natran Green Pest Control, Inc.* on the Employee Agreement,
  *Natran, LLC* on the insurance policy.

### Not converted

The `[HR Core Process]`, `[Leadership Team Core Process]`, `[Corrective Action Form]`, `[Employee
Referral Bonus Form]`, `[Nursing Mother's Accommodation Request]`, `[CareNow Locations Website]`
and `JazzHR webinar training` link stubs; the JazzHR shortcut; and all binaries — the CareNow
location and authorization PDFs, the injury-related HR form PDFs, the Employment Work Status
Change PDF, the EAP information sheet, and the QualityPro and GreenPro study guide PDFs.

**Deferred:** `Natran Brand Promise` (38 KB) pairs with the root `The Natran Brand` document and
is handled together in batch 8. The standalone **Pet Protocol** Google Doc that three departments
link to sits outside the enumerated wiki tree and has not been read — it may or may not match the
handbook section now recorded at [pet policy](/people/pet-policy.md).

## 2026-07-28 — batch 2

**Wiki `/Technology`, `/HR/Onboarding`, `/HR/Onboarding/Device Setup & Onboarding` and
`/HR/Offboarding`.** 20 new concepts, plus material folded into 5 existing ones. All
`status: draft`.

Every document in this batch was written between 2022 and 2025; the IT
single-source-of-truth ingested in batch 1 is 2026-07. **Where they overlap, the older
document usually describes a manual process that the newer one automates through
ManageEngine.** Nothing was discarded on that basis — the age gap is recorded in-file and
the reconciliation is IT's call, not this ingestion's.

* **Update**: `type: Script` used for the first time, on [RingCentral voicemail greeting
  scripts](/it/telephony/ringcentral-voicemail-scripts.md). This is the usage OQ-007 was
  waiting for.
* **Update**: New **system** tags: `jamf`, `ringcentral`, `podium`, `keeping`, `gam`,
  `busylight`, `att`, `google-chat`. New **topic** tags: `inventory`, `support`. Recorded
  in `CLAUDE.md`.

**Creations — [/it/devices/](/it/devices/)** (9): [Windows PC
setup](/it/devices/windows-pc-setup.md); [Windows device user removal and
return](/it/devices/windows-device-user-removal.md); [Apple device
assignment](/it/devices/apple-device-assignment.md); [Apple device self-service
setup](/it/devices/apple-device-self-service-setup.md); [Apple device erase and
unassign](/it/devices/apple-device-erase.md); [Chromebook
assignment](/it/devices/chromebook-assignment.md); [AT&T SIM
activation](/it/devices/att-sim-activation.md); [Device QR code
labels](/it/devices/device-qr-code-labels.md); [Busylight
setup](/it/devices/busylight-setup.md); [Teramind user
monitoring](/it/devices/teramind-user-monitoring.md).

**Creations — [/it/google-workspace/](/it/google-workspace/)** (4): [2-Step
Verification](/it/google-workspace/two-step-verification.md); [GAM setup and
commands](/it/google-workspace/gam-setup-and-commands.md); [Keeping shared inbox
setup](/it/google-workspace/keeping-shared-inbox.md); [Group email
moderation](/it/google-workspace/group-email-moderation.md).

**Creations — [/it/telephony/](/it/telephony/)** (3): [RingCentral voicemail greeting
scripts](/it/telephony/ringcentral-voicemail-scripts.md); [RingCentral voicemail
setup](/it/telephony/ringcentral-voicemail-setup.md); [RingCentral call
monitoring](/it/telephony/ringcentral-call-monitoring.md).

**Creations — [/it/](/it/)** (3): [Fieldroutes user
setup](/it/fieldroutes-user-setup.md); [Podium user setup](/it/podium-user-setup.md);
[Reporting an IT issue](/it/reporting-an-it-issue.md).

**The RingCentral question.** Three documents in this batch describe RingCentral as the phone
system. CTM is documented as current everywhere else, and no migration is recorded anywhere in
the corpus. The evidence both ways is set out in [RingCentral voicemail
setup](/it/telephony/ringcentral-voicemail-setup.md). They are `draft`, not `deprecated` —
marking a whole system retired is a domain owner's call. Stale cross-references to RingCentral
also survive in [Apple device self-service
setup](/it/devices/apple-device-self-service-setup.md) and [Windows device user
removal](/it/devices/windows-device-user-removal.md), flagged in both.

**Material folded into existing concepts** rather than duplicated, each with the second source
added to its frontmatter:

* [Door access](/it/network/door-access-unifi.md) — **this resolves the batch-1 puzzle and
  replaces it with a policy question.** The IT document's introduction promised PIN-code
  instructions while its body forbade them; that introduction turns out to be copied verbatim
  from the wiki document, where PIN codes *are* documented as one of three credential types
  alongside NFC cards and a recommended face photo. Both carry the same swapped iOS/Android
  links, confirming the lineage. So the contradiction is a policy change captured halfway. Both
  procedures are now recorded side by side; they also disagree on the group name (**Door Access -
  Natran** vs **Unlock Access**) and on the deactivation path.
* [Workspace account offboarding](/it/google-workspace/account-offboarding.md) — a third version
  of the same procedure, disagreeing on the two timings that decide when deletion is safe. Most
  consequential: the restore window is **20 days** here against **15** in the IT document.
  Google's actual figure is 20. Two steps appear only in the wiki version — selecting **Export
  Once**, and checking **"Include files that are not shared with anyone"** at deletion, without
  which a departing user's unshared files are not transferred.
* [Workspace account provisioning](/it/google-workspace/account-provisioning.md) — gains the
  organizational unit hierarchy (`Regions → Branch → Role`, or `Corporate`) that the IT document
  refers to but never spells out, plus the Employee Info fields that feed the email signature.
  The two sources conflict on the password step; the wiki version has you **print** the
  credentials.
* [Fieldroutes user deactivation](/it/fieldroutes-user-deactivation.md) — gains the rule that
  matters most: **suspend the Google account first, or the user resets their own Fieldroutes
  password.** The two sources also assign the appointment and task cleanup to different people.
* [Windows default administrator account](/it/devices/windows-default-administrator-account.md) —
  a second source names the configuration differently and ends with Save-plus-reboot rather than
  Deploy Immediately.

**One batch-1 ambiguity resolved.** Backup verification codes are **8 digits**. The IT document
called them seven in one step and eight two steps later; both wiki sources in this batch say
eight, and that matches Google. Recorded in [2-Step
Verification](/it/google-workspace/two-step-verification.md).

**Not converted from this batch:** the `[IT Core Process]`, `[Technician Shirt Order Form]`,
`[Business Card Request Form]` and `[Tech Voicemail Greeting]` link stubs; the
`Technology/Resources` folder (a single JSON asset, linked from [Busylight
setup](/it/devices/busylight-setup.md)); and the `/HR/Onboarding` and `/HR/Offboarding`
`wiki.page` hybrids, whose provisioning-checklist structure is already carried by
[Workspace account provisioning](/it/google-workspace/account-provisioning.md) and
[account offboarding](/it/google-workspace/account-offboarding.md).

**Deferred to the HR batch:** *"Which Access Control profile should I use in Pestroutes?"*, which
[Fieldroutes user setup](/it/fieldroutes-user-setup.md) step 2 depends on and which currently
leaves that step without guidance. Also the **uAttend vs Gusto Wallet** timeclock question — two
different systems appear as *the* timeclock in different documents.

**New defects flagged in-file**, beyond the cross-source conflicts above: a PowerShell command
with a typographic quote that would fail as written; two incompatible GAM installations
(`C:\GAMCONFIG` + GAMADV-XTD3 vs `c:\NATRAN-GAM` + GAM-team/GAM); a Keeping invite step telling
you to check all mailboxes against a provisioning rule saying to keep users out of recruiting and
HR inboxes; a RingCentral away-message procedure that would overwrite the working-hours greeting
if followed literally; an AT&T activation template asking for a Billing Account Number recorded
nowhere; and a self-service setup promising RingCentral voicemail instructions that do not exist.

## 2026-07-28

**Batch 1 of the Google Drive wiki ingestion.** Source: the `IT single-source-of-truth`
Google Doc (`1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc`, ~110 KB, modified
2026-07-27). Note it lives *outside* the `Natran Wiki` shared-drive folder that the rest
of this ingestion draws on. Everything below is `status: draft` pending domain-owner
confirmation.

* **Update**: Added four directories under [/it/](/it/) — `devices/`,
  `google-workspace/`, `network/`, `printers/` — each with an `index.md`. The remaining
  seven root-level domains agreed for this ingestion (`people/`, `finance/`,
  `customer-care/`, `field-ops/`, `sales/`, `marketing/`, `services/`) are deliberately
  **not** scaffolded yet; each is created by the batch that first fills it, so the bundle
  never carries an `index.md` listing nothing.
* **Update**: Extended the `type` vocabulary with `Script` and `Template`, per Michael.
  Neither is used in this batch — both were approved for the customer-care and sales
  batches still to come. Recorded in `CLAUDE.md`.
* **Update**: Extended the `tags` vocabulary. New **system** values: `manage-engine`,
  `google-workspace`, `teramind`, `chrome`, `gcpw`, `unifi`, `brother`, `raspberry-pi`,
  `microsoft-365`, `shared-contacts`, `fieldroutes`, `hubspot`. New **topic** values:
  `devices`, `provisioning`, `deployment`, `security`, `access-control`, `offboarding`,
  `printers`, `scanning`, `network`, `door-access`, `email`, `signatures`, `contacts`,
  `crm`, `marketing`. Recorded in `CLAUDE.md`.

**Creations — [/it/devices/](/it/devices/)** (8): Windows device enrollment; Endpoint
Central configuration catalogue; Windows default administrator account; Windows local
account administration; software deployment packages; Teramind agent deployment; Chrome
managed browser enrollment; GCPW deployment.

**Creations — [/it/google-workspace/](/it/google-workspace/)** (12): admin account
separation; account provisioning; Google Groups; Microsoft 365 provisioning; profile
photo; email signature deployment; email signature template structure; account
offboarding and backup; email forwarding; shared contacts administration; Context-Aware
Access; CAA device approval.

**Creations — [/it/printers/](/it/printers/)** (4): Brother printer setup; fixed IP
assignment; ManageEngine printer deployment; Brother scanner to Drive.

**Creations — [/it/network/](/it/network/)** (2): door access; Zoho software repository
(Raspberry Pi).

**Creations — [/it/](/it/)** (2): [Fieldroutes user
deactivation](/it/fieldroutes-user-deactivation.md); [Hubspot user
provisioning](/it/hubspot-user-provisioning.md).

**Creations — [/it/telephony/](/it/telephony/)** (3): [CTM agent
offboarding](/it/telephony/ctm-offboarding.md), [CTM access control and privacy
levels](/it/telephony/ctm-access-control-privacy-levels.md), [CTM chat tag
lifecycle](/it/telephony/ctm-chat-tag-lifecycle.md).

The source's CTM tab covers the same ground as the seven existing `ctm-*` concepts. Per
Michael, **those seven stay canonical** — they came from working sessions plus live API
reads — and only genuinely new material was converted, as the three files above.

* **Update**: Added unresolved-conflict blockquotes to
  [CTM agent onboarding](/it/telephony/ctm-agent-onboarding.md) (the source states the
  new-user role three different ways: Call Agent, Call Manager, and by-position) and
  [CTM voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md) (the
  source gives a gendered greeting script and instructs administrators to match pronouns
  to the agent, the opposite of the recorded rule). Both name the competing sources and
  are for Michael to settle. No canonical content was changed.

**Filing corrections.** Nothing in this source was filed by its tab. Door access and the
Raspberry Pi moved out of the source's `Network` tab framing into `/it/network/`; the
source's `Call Tracking Metrics` stub sat under its `Microsoft` heading and was discarded
as a to-do; Teramind content lives under the source's Device Management tab while its own
`Teramind` tab is empty.

**Not converted from this source**, with reasons: the `To dos` tab (self-described holding
area), `Tab 13` (untitled — raw notes, open questions, and a group table with literal `2`
and `3` placeholder rows), `Issues` (a numbered scratch list with a Google support case
URL and a ManageEngine pricing note), the CTM `Settings` section (an in-progress trigger
experiment with duplicate step numbering, the author's own inline uncertainty, and an
unfinished test matrix), the `Style guide` tab (formatting boilerplate, not company
knowledge), and the empty `Teramind`, `Queues` and `Teams` tabs.

**Source defects flagged in-file, not fixed.** Around 25 in total, including: a
copy-pasted "set fixed IP on device" block that exists twice and has diverged to six
steps versus eight; backup codes described as seven-digit in one step and eight-digit two
steps later; a GAM command hardcoded to a named employee instead of a placeholder; two
incompatible email-signature schemas with a mapping table documenting only one of them;
iOS and Android app-store links swapped; a door-access section whose introduction promises
pin codes while its rule forbids them; a `Deploy GCPW` configuration that installs the
Chrome package; Lorem ipsum placeholder rows in three CTM tables; and an access-control
tag scheme (`TH10`, `HR7`, `R5`) whose level labels contradict both their own names and
the privacy-level table — the last of these is the one with real exposure, since it
governs who can see recruiting and HR call activity.

**Screenshot loss.** The Drive read returns text only. Noted at the point of loss in
[Brother printer setup](/it/printers/brother-printer-setup.md), [ManageEngine printer
deployment](/it/printers/manage-engine-deployment.md) and [email
forwarding](/it/google-workspace/email-forwarding.md), all of which were written against
interface screenshots.

**Cross-company content.** This Natran IT document carries Advantage Pro Services
material — an APS email-signature template, its GAM command, and its
`admin@advantageproservices.com` template owner. Transcribed as found and flagged in
[email signature template structure](/it/google-workspace/email-signature-template-structure.md);
whether APS material belongs in the Natran bundle is a scoping question for Michael.

## 2026-07-26

* **Initialization**: Created `docs/` and seeded the corpus with its first seven
  concepts, all covering CallTrackingMetrics.
* **Creation**: [CTM account](/it/telephony/ctm-account.md) — account identifier, access paths,
  and the API quirks that affect anything reading from it.
* **Creation**: [CTM agent onboarding](/it/telephony/ctm-agent-onboarding.md) — the end-to-end
  provisioning runbook and its hand-offs.
* **Creation**: [CTM team to queue mapping](/it/telephony/ctm-team-queue-mapping.md).
* **Creation**: [CTM queue routing weights](/it/telephony/ctm-queue-routing-weights.md).
* **Creation**: [CTM tracking number assignment](/it/telephony/ctm-tracking-number-assignment.md).
* **Creation**: [CTM voicemail and missed call alerts](/it/telephony/ctm-voicemail-standard.md).
* **Creation**: [CTM missed chat notification](/it/telephony/ctm-missed-chat-notification.md).
* **Update**: Established the `type` vocabulary (`Runbook`, `Reference`, `Policy`)
  and the system + topic `tags` convention. Recorded in `CLAUDE.md`; reasoning in
  `DECISIONS.md` under OQ-003.
* **Update**: Promoted the flat `docs/` directory to a full bundle — the root
  [index](/index.md) now carries `okf_version: "0.2"`, every directory has an
  `index.md`, and doc links are bundle-relative.
* **Update**: Moved all seven CTM concepts to [/it/telephony/](/it/telephony/)
  under the new placement rule: nothing tool- or function-specific at the bundle
  root. Reasoning in `DECISIONS.md` under OQ-006.

Source for all seven: working sessions with Michael Arndt plus live reads of the
CTM API for account 448519, captured while building the `ctm-new-user-setup` skill.
