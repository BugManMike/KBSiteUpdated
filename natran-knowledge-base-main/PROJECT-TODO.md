# Project TODO

How to use: add items under the right group with `- [ ]`, check them off with `- [x]`
when done, and prune completed items occasionally. Anyone can add.

## Open decisions

- [ ] Decide the canonical publishing surface (wiki, site generator, or raw repo) — see
      OQ-005 in `DECISIONS.md`
- [x] Decide how the company KB (`content/`) and the OKF bundle (`docs/`) relate long-term
      — **merged into `docs/` 2026-07-28**, see OQ-009
- [ ] Settle `fieldroutes` vs `pestroutes` as the CRM tag value — see OQ-008. Wanted
      before the Customer Care batch, which is **next**. Reversal cost is now ~24 files
- [ ] **Decide the price increase rate.** The source states 3%, 5% and 3.5% in different
      places, and whether customers must be notified turns on whether it exceeds 5% — see
      `docs/sales/price-increase-process.md`
- [ ] Confirm which sales commission spreadsheet is live — the 2024 *Commission Worksheet*
      or the 2023 *Natran sales commission report*. The older one holds the only
      step-by-step for importing the reports
- [ ] Resolve the two CTM conflicts flagged in `docs/it/telephony/` — the new-user role
      (Call Agent vs Call Manager vs by-position) and the voicemail greeting pronouns
- [ ] Decide whether the Employee Handbook and Employee Agreement should be shredded into
      concepts, or left mapped as they are now — see the two map documents in
      `docs/people/`
- [ ] Agree who confirms `status: draft → stable` per domain. Almost the whole corpus is
      currently `draft` pending a domain owner's sign-off
- [ ] Scope OKF authoring rules per project, and settle how finished project work reaches
      this bundle — see OQ-012. Agreed in principle 2026-08-11; nothing built. Overlaps
      OQ-011, which wants the same machine-readable vocabulary

## Urgent — security and data, from the batch 4c ingestion

- [ ] Remove the deposit bank account number from the technician check collection wiki page
- [ ] Remove the personal Wise referral link from the VA sign-up document, and stop routing
      contractors' bank details to named individuals by email
- [ ] Get the W-8BEN tax position in the VA sign-up document reviewed by someone qualified
      before another contractor is onboarded from it
- [ ] Stop filing every 401(k) termination as "Permanent Layoff"
- [ ] Confirm the $295 Sentricon unit cost, last touched in 2022, and record its source

See `docs/finance/technician-check-collection.md`, `docs/people/virtual-assistant-onboarding.md`,
`docs/people/401k-contributions.md` and `docs/finance/sentricon-install-budgeting.md` — values
deliberately not copied into this repo.

## Urgent — security, from the batch 3 ingestion

- [ ] Stop deriving the fuel PIN from employees' Social Security numbers
- [ ] Stop emailing shared default passwords in plaintext; they are reused across
      Fieldroutes, NPMA and TPCA
- [ ] Rotate the Houston back door code and stop emailing it to personal addresses; no
      offboarding step currently rotates it
- [ ] Clear the real employee details left in two HR email templates, and the real surname
      left in the New Hire Worksheet template

See `docs/people/hr-email-templates.md` — values deliberately not copied into this repo.

## Content & migration

- [x] Inventory existing docs to migrate — **done**, 72 folders and ~438 files enumerated,
      see the 2026-07-28 entry in `docs/log.md`
- [x] Batch 4c — compensation, procurement, the routing-decision documents and the four
      month-end journal entries left over from 4a — **done 2026-09-14, 19 concepts**
- [ ] Finish the wiki ingestion: batches 5–8 remain — Customer Care and Dispatch, Sales and
      Marketing, Operations and Shared Services, then the root files and the unconvertible
      report. **~100 convertible documents left**
- [ ] Decide what happens to `Natran Core Processes` (432 KB, ~20 inbound link stubs) —
      the forcing point for OQ-005
- [ ] Reconcile the **four** payroll and timekeeping systems: Gusto (payroll), uAttend (time,
      on an Advantage Pro Services tenant), EOSG/PrismHR (wage history for PTO rates), and the
      PEO whose deduction report drives 401(k) contributions. Batch 4c found the fourth; one
      procedure reaches into three of them
- [ ] Decide whether Advantage Pro Services material belongs in the Natran bundle at all —
      it appears in the email signature templates, the GAM setup, and the uAttend procedure

## Features to build

- [x] Frontmatter lint check — **`scripts/check-bundle.py` promoted into the repo 2026-07-28**
- [x] Wire `scripts/check-bundle.py` into CI — **`.github/workflows/docs.yml`, 2026-09-14.**
      It also runs `mkdocs build --strict` as an independent link check
- [x] Simple rendered view of the bundle — **MkDocs Material site built 2026-09-14**, see
      `docs-site-setup.md`. Source files unchanged; a build-time hook translates the
      bundle-relative links
- [ ] **Decide where the site is hosted, and deploy it.** This, not the build, is what
      actually unblocks OQ-005. GitHub Pages on a private repo needs Enterprise Cloud;
      Cloudflare Pages behind Access is the cheaper fit. The deploy job is written but
      commented out
- [x] Search across concepts (title, tags, body) — **comes with the site's search plugin**

## Infra & ops

- [ ] Set up branch protection / review requirement on `main`
- [ ] Automated backup or mirror of the repo
- [ ] Decide backup cadence and retention

## Backlog / ideas

- [ ] Stale-doc report by the `generated.at` date
- [ ] Tag vocabulary cleanup once the ingestion is complete — it grew fast across batches
      1–3 and some values will turn out redundant
- [ ] Resolve the `Process` / `Playbook` type question if a document ever needs them —
      see OQ-003
