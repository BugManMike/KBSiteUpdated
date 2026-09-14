# Handoff — Google Drive wiki ingestion

Working state for the ingestion of the `Natran Wiki` Google Drive folder into the OKF bundle in
`docs/`. Update this file at the end of each work session.

**Last updated:** 2026-09-14, after batch 4c
**Branch:** ⚠️ **unverified — confirm before writing anything.** The 2026-07-28 entry recorded
`wiki-ingestion` as pushed to `origin` but **not merged**, with `main` unchanged at `eb223ab`.
Batch 4c was written against a working copy taken from a `main` archive that already contained
batches 1–4b, which means either the branch was merged and this file was never updated, or the
archive was of the branch. **Check what is actually on `main` and correct this line.** If the
branch is still unmerged, ~167 files of work sit on one branch with no mirror and no branch
protection — both still open in `PROJECT-TODO.md`.

---

## Where things stand

**Done:** batches 1, 2, 3, 4a, 4b, 4c, plus the `content/` → `docs/` merge.
**Bundle:** 167 markdown files, 13 directories, verification clean — 0 broken links, every
`index.md` current, `mkdocs build --strict` clean as a second check.
**Rendered site:** `mkdocs.yml`, `hooks/okf.py` and `.github/workflows/docs.yml` were added
2026-09-14 — a MkDocs Material site over `docs/` that translates the bundle-relative links at build
time without touching a source file. Hosting is **not** yet decided; the deploy job is commented
out. See `docs-site-setup.md`. This is the OQ-005 blocker.

| Batch | Scope | State |
|---|---|---|
| 1 | `IT single-source-of-truth` Google Doc (outside the wiki tree) | done — `b80fcda` |
| 2 | Wiki `/Technology`, `/HR/Onboarding`, `/HR/Onboarding/Device Setup`, `/HR/Offboarding` | done — `177c16d` |
| 3 | Wiki `/Human Resources` (rest) | done — `873ffd8` |
| — | Merge `content/` into `docs/`, retire the company KB contract | done — `9f84571` |
| 4a | Wiki `/Accounting` — close, receivables, collections, `Roles/B&P Agent` | done |
| 4b | Accounting payables, tax, vendor billing, credit/write-offs — 29 concepts | done |
| 4c | Compensation, procurement, the routing-decision documents, and the 4a leftovers — 19 concepts | done — 2026-09-14 |
| **5** | **Customer Care and Dispatch** | **next** |
| 6 | Sales and Marketing | pending |
| 7 | Operations and Shared Services | pending |
| 8 | WIP, root files, and the consolidated unconvertible report | pending |

Roughly **100 convertible documents remain.**

## The contract

Read `CLAUDE.md` before writing anything. Key points that bite:

- **Verify the OKF spec still declares v0.2** before each session — fetch the raw URL with a
  cache-busting query string. It moved from 0.1 to 0.2 during this work.
- **One concept per file.** Never append to an existing doc.
- **Everything is `status: draft`** until a human domain owner confirms it.
- **Reuse the `type` and `tags` vocabularies** in `CLAUDE.md`; propose additions rather than coining
  them, and record every new value in `CLAUDE.md` **and** the batch's `log.md` entry.
- **File by owning domain, not source folder.** The wiki's folders are often wrong — compensation in
  the accounting folder goes to `people/`, vehicle procurement goes to `operations/fleet/`.
- **Flag source defects in-file with a blockquote; never silently fix them.** Name the conflict and who
  needs to resolve it.
- **Never copy secrets or personal data into the repo** — describe and redact so the defect can be
  fixed without propagating it.
- **A domain directory is created by the batch that fills it.** Never scaffold an empty one.

## Working method that has held up

1. Enumerate the source folder with the Drive MCP tools (`parentId = '<id>'`).
2. Read every real content document. Open `wiki.page` files individually — most are navigation shells
   but one was genuine content.
3. Write concepts, routing by owning domain.
4. Update every affected `index.md`.
5. Add a `log.md` entry naming creations, filing corrections, conflicts, and what was **not**
   converted and why.
6. Run the verification script (below), then commit. **Never push.**

**Verification script:** `scripts/check-bundle.py`
Checks frontmatter completeness, `type` against the vocabulary, bundle-relative link resolution, and
`index.md` presence. Run it from the repo root.

The seven `missing status:` warnings it reports are **expected** — those are the original CTM docs,
which are stable, and OKF treats absent as stable.

**Full source inventory** (72 folders, ~438 files, classified):
`...\b102d2c5-9ab9-49c5-9a6d-d7ec610cd287\scratchpad\wiki-inventory.md`

## Decisions already made — do not relitigate

| Decision | Where |
|---|---|
| Existing seven `ctm-*` docs stay canonical; only new material from the IT doc was converted | OQ-005 context, `log.md` batch 1 |
| Eight root domains: `it/ operations/ people/ finance/ customer-care/ sales/ marketing/ services/` | `CLAUDE.md` |
| `type` gained `Script` and `Template` | OQ-007 |
| `content/` merged into `docs/`; company KB contract retired; per-document gating dropped | OQ-009 |
| Employee Handbook and Employee Agreement mapped, not shredded — signed instruments | `people/employee-handbook-map.md` |

## Open questions blocking or shaping later batches

1. **`fieldroutes` vs `pestroutes`** as the CRM tag value — OQ-008. **Wanted before batch 5**, which
   is now the batch immediately next. Still unanswered. Batch 4b added 11 docs and 4c added **6
   more**, so the reversal cost is now **~24 files** rather than one. Note that 4c's sources call it
   *Pestroutes* throughout, including one that writes "Fieldroutes (Formerly known as Pestroutes)" —
   the rename is real and the wiki has not caught up.
2. **When a procedure spans two systems, which gets the system tag?** — OQ-010. **Decided
   provisionally during 4b** (the entry point wins) and applied to 11 docs, but settled mid-ingestion
   rather than agreed in advance. **Wants ratification or reversal before more of the corpus depends
   on it.**
3. **Nothing validates the `tags` vocabulary** — OQ-011. `check-bundle.py` enforces `type` and ignores
   `tags` entirely, which is how the recorded vocabulary drifted behind actual usage and how a typo
   (`vim`) survived as a value. Cheapest to fix before batch 5.
4. **The two CTM conflicts** — the new-user role (Call Agent vs Call Manager vs by-position) and the
   voicemail greeting pronouns. Flagged in-file in `it/telephony/`.
5. **Should the Handbook and Agreement be shredded** into concepts after all?
6. **Who confirms `draft → stable`** per domain. **Still the largest single question, and it grew**:
   **146 of the bundle's 153 concepts are `status: draft`** — everything except the seven original
   CTM documents — including every finance and people document, and nobody has been named to review
   any of them. Batches 4a, 4b and 4c each surfaced
   control gaps a domain owner would resolve in minutes; without one, the in-file flags just
   accumulate and the whole corpus stays provisional. The rendered site added 2026-09-14 puts a
   **"Draft — not yet confirmed"** banner on every one of those pages, which makes the problem
   visible to readers but does not solve it.
7. **Which sales commission spreadsheet is live** — the *Commission Worksheet* (2024 document) or
   the *Natran sales commission report* (two 2023 documents). New in 4c. The older pair holds the
   only step-by-step for importing the Fieldroutes reports, so this cannot be settled by simply
   retiring them.
8. **The price increase rate.** The source states 3%, 5% and 3.5% in different places, and the
   customer-notification obligation turns on whether the increase exceeds 5%. New in 4c and the most
   consequential single unanswered number in the corpus — see
   [price increase process](docs/sales/price-increase-process.md).

## Corpus-wide questions the batches keep re-raising

Not blockers, but each has now been hit by more than one batch, and each needs one person to answer
rather than another in-file flag.

- **There is still no authoritative list of health benefit vendors.** Three batches, three different
  lists: six vendors in [health benefit allocation](docs/finance/health-benefit-allocation.md), two
  different ones in [benefits enrolment](docs/people/benefits-enrolment.md), and a third pair in
  [health benefit vendors](docs/finance/health-benefit-vendors.md). Whoever owns benefits should
  publish the real list; the docs can then point at it.
- **`Trade`, a fake customer, now carries two unrelated month-end adjustments** — the AR
  ending-balance plug (4a) and the bad-debt credit memo (4b). Anything posted against `Trade` is
  becoming uninterpretable.
- **There are four payroll or timekeeping systems, not three.** Batch 4c added a **PEO** whose
  deduction report is the authority for 401(k) contributions, alongside **Gusto** (payroll),
  **uAttend** (time, on an **Advantage Pro Services** tenant) and **PrismHR** (wage history for PTO
  rates). No document states the relationship between any two of them, and one procedure reaches
  into three of the four. This is the tangle to hand to one person, not another in-file flag.
- **Approval is undocumented on both sides of the ledger.** Bill payment filters on "Approved" with
  no documented approver or limit; fee waivers and credits record no reason, approver or limit. Batch
  4c found the same shape again in **missed pay** (no approver on a manual wage correction) and gave
  it a partial answer on the credit side: [approved coupon codes](docs/finance/coupon-codes.md)
  records a *reason* but still no approver. Same
  gap, found independently in two places.
- **Several procedures name individuals by first name only**, with no role — the weekly credit
  recipient, the lien notice signatory, the N94 contact. Recorded by inferred role where possible.
  Each one stops working when that person changes jobs.

## Small cleanups noticed, not done

Deliberately left alone — each predates the batch that found it, and fixing other batches' work
inside an ingestion commit makes the diffs hard to review.

- **`docs/operations/production-vs-materials.md` carries the tag `vim`** — almost certainly a typo,
  and the only use of that value in the corpus. See OQ-011.
- **The `CLAUDE.md` tag table drifted** behind actual usage before batch 4b brought it current.
  Nothing prevents recurrence; that is what OQ-011 is about.

## Urgent, non-ingestion — from batch 3

Found in the HR email templates source. **Values were deliberately not copied into the repo**; they
are in the source document. See `docs/people/hr-email-templates.md`.

- The **fuel PIN is the last four digits of the employee's Social Security number**.
- A **shared default password is emailed in plaintext**, reused across Fieldroutes, NPMA and TPCA.
- The **Houston back door code is emailed in plaintext to personal addresses**, and no offboarding
  step rotates it.
- **Two templates contain a real employee's name, username and password**; the New Hire Worksheet
  template has a real surname left in it.

## Urgent, non-ingestion — from batch 4b

Also source-side cleanup, not repo work. Each is flagged in-file under `docs/finance/`.

- **The Lien Notice template is a sent letter, not a blank form.** It carries a real customer's
  **service address, balance and overdue date**. Anyone working quickly sends the next notice with the
  previous customer's details still in it. Placeholders were used in
  `docs/finance/lien-notices.md`; the source needs fixing.
- **The lien notice asserts statutory lien rights** under Texas Property Code §§53.056–53.058 and
  threatens litigation, with **no legal review step anywhere in the process**. Those provisions sit in
  the mechanic's and materialman's lien chapter. **Confirm with counsel before sending another one.**
- **Franchise tax is documented as a monthly payment.** Texas franchise tax is annual, due 15 May.
- **`The Expired Credit Card Processs` should be deleted or marked superseded** — it duplicates the 2025
  notification procedure with a different customer callback number and a named individual's signature,
  which will keep going out after they change roles.
- **The "Important file" spreadsheet holds both companies' bank account details** and is referred to in
  the sales tax procedure by nothing more specific than that name.
- **Approval is undocumented on both sides of the ledger** — no approver, limit or reason code for
  paying a bill or for waiving a fee. This is the largest control gap batch 4b found.

## Urgent, non-ingestion — from batch 4c

Source-side cleanup again. **No values were copied into the repo.** Each is flagged in-file.

- **The technician check collection procedure names the company's deposit bank account number in
  plain text**, in a page every technician reads. A deposit account number plus the company name is
  enough to originate a debit. **Remove it from the source.**
- **Every virtual assistant is onboarded through one employee's personal Wise referral link**, which
  pays that employee. The same document tells the contractor to email bank account and routing
  numbers to two individuals, named personally rather than by role.
- **The VA onboarding document states a tax position** — asserting a permanent establishment in the
  Philippines under Article 5 — and hands it to the contractor as the answer to copy into a W-8BEN.
  Nobody qualified has signed off on it, and a wrong entry creates a personal tax liability for the
  contractor. **Same class of exposure as the lien notice found in 4b.**
- **401(k) terminations are filed with "Permanent Layoff" as the reason for every departure**,
  including resignations. That is a benefits record, not a form field to leave on a default.
- **The Sentricon budget hardcodes a $295 unit cost last touched in 2022**, with no stated source and
  no check against what Corteva actually invoices.

## Batch 5 — what is next, concretely

Source folder: wiki `/Customer Care and Dispatch` (`1NPV_OKqPd3G-ZWUKocdcvBrvjLK2MijZ`). It has
subfolders — enumerate before converting; unlike `/Accounting/Processes` it is not flat.

**This is the batch that lands the bulk of the CRM material**, which is why OQ-008 (`fieldroutes`
vs `pestroutes`) was wanted before it. That decision has still not been made. The reversal cost was
~18 files at the end of 4b; batch 4c added `fieldroutes` to **6 more**, so it is now ~24 files.
**Ask before starting.**

Two root domains will be created by this batch: **`customer-care/`** and, if dispatch material does
not fit there, scheduling content under **`operations/`**. Neither should be scaffolded empty.

**Known to be in or near this folder:** the `2026 Shift Calendar and Skillsets` spreadsheet lives
here (`10sF5DSgepBzcJbfh0dKQqcs72tU7YaP-AXxmEbjfz_0`) and is actively edited — treat it as a live
reference rather than a document to transcribe wholesale.

**Expect to meet the material the corpus already points at but does not hold:** cancellation and
subscription scripts, the customer-care side of collections, and the field half of
[holding service on past-due accounts](docs/finance/holding-service-past-due-accounts.md), which
carries a `TODO:` marker precisely because this batch had not run.

### Still unconverted in `/Accounting/Processes`

Left deliberately, with reasons, after 4c:

- **`Sales Commission`** and **`Sales commission proces`** *(sic)* — superseded duplicates of
  [calculating salesperson commissions](docs/people/sales-commission-calculation.md). Do not convert;
  they should be retired at source once payroll confirms which spreadsheet is live.
- **`Account Receivable Process`** — **two documents share this title** (`1mFcV0-7...`, modified
  2026-09-03, and `1gnrmNiWb_...`, 2023). The 2026 one is the most recently edited document in the
  folder. Both belong with the receivables cluster converted in 4a and should be **checked against
  it**, not converted blind. The 4a entry already records an unresolved two-same-titled-docs problem
  in this area.
- **`Natran Law Inside Sale 11/21`** — outside any converted scope; read before deciding.
- The four **`[... Core Process]`** 1024-byte link stubs — pointers into `Natran Core Processes`,
  which is OQ-005's forcing point.

## Reference

- Wiki root folder: `1gfI4Z18Rmd6UnjTm0Xned1SvdiwQ0GZQ`
- `IT single-source-of-truth` doc: `1bWFcupYYDpgr8VdkuegTsAK_x9SEar1UAQZtdFj_mQc`
- `Natran Core Processes` — 432 KB, ~20 inbound link stubs, the forcing point for OQ-005:
  `1eWWlf4kxO5reYoN1RExpNXhQ2WZkZPpZy_ET8UW5e1E`
