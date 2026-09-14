# natran-knowledge-base

Durable knowledge base for the Natran organization. Everything of substance in this
repo is documentation — there is no application code to build or test.

**One contract: the OKF v0.2 bundle in `docs/`.** All company knowledge lives there.
The repo root holds only meta files that sit deliberately outside the bundle —
`CLAUDE.md`, `DECISIONS.md`, `PROJECT-TODO.md` and `README.md`.

> Until 2026-07-28 this repo carried a second, parallel contract — a "company KB" in
> `content/` with its own frontmatter schema, `draft → review → published` status
> values, and a `visibility`/`allowed_roles` access model. **It was merged into `docs/`
> and retired**; `content/`, `taxonomy.yml`, `_templates/` and `CHANGELOG.md` are gone.
> See OQ-009 in `DECISIONS.md`. Nothing was lost — the `content/` tree contained only
> section scaffolding and explicit placeholder pages.

## Ownership

**Owner:** `admin@natran.com`, accountable for the corpus. Access is controlled at the
repository level; there is no per-document gating.

## Documentation format — OKF v0.2

All documentation in this repo uses the **Open Knowledge Format (OKF)**, pinned at
**v0.2**.

- Spec: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
- Raw (use this to verify the version — the blob URL and intermediate caches have
  served a stale render for hours after a release):
  `https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/SPEC.md?t=<now>`

### Before writing or extending any doc

1. Fetch the raw spec URL **with a cache-busting query string** and confirm it still
   declares v0.2.
2. If it declares a different version, **stop and surface it** before writing
   anything: name the new version, summarize what changed (especially renamed, added,
   or removed required fields), and ask whether to adopt it and revise existing docs,
   or stay pinned. Anything short of a clear yes means stay pinned.
3. Never adopt a newer OKF revision on your own. Upgrading is a deliberate, reviewed
   change — a major bump can rename required fields and invalidate every file. On an
   explicit yes, update the pinned version in this file as part of the same change.

### Frontmatter

Every non-reserved `.md` file carries YAML frontmatter. `type` is the only field OKF
requires, but in this repo always include:

```yaml
---
type: <concept type from the vocabulary below>
title: <human-readable display name>
description: <one sentence>
tags: [<tag>, <tag>]
generated:
  by: <actor — person or model that produced this>
  at: <ISO8601 timestamp>
---
```

Optional OKF field families, used when they apply: `resource` (canonical URI for an
underlying asset), `sources` (provenance), `verified` (trust), `stale_after`
(lifecycle).

`status` is a **spec-owned lifecycle field** with exactly three values: `draft`,
`stable`, `deprecated`. Absent means stable. Never repurpose it — project-specific
state axes get their own key (`review_status`, `rollout_status`, etc.).

### Structure

- **One concept per file.** Distinct new material gets its own file — never appended
  as a section to an existing doc.
- `index.md` and `log.md` are **reserved filenames** and are the only files exempt
  from frontmatter. `index.md` is a directory listing; `log.md` is a chronological
  update history.
- **Current state: full bundle** (promoted 2026-07-26, ahead of the wiki
  migration): one atomic file per concept, an `index.md` per directory, a root
  `index.md` carrying `okf_version: "0.2"`, a `log.md`, and bundle-relative links
  (`/dir/file.md`). Keep every directory's `index.md` current when adding or
  moving docs.
- **Placement rule: nothing tool- or function-specific at the bundle root.** Root
  directories are org-level groupings; tools and functions nest under the owning
  department — telephony lives at `/it/telephony/`, not `/telephony/`. See OQ-006
  in `DECISIONS.md`.

### Vocabularies

Reuse the `type` and `tags` values already present in the corpus. Do not invent new
ones ad hoc — if nothing fits, say so and propose the addition rather than silently
coining a value. As the vocabularies stabilize, record them here.

Established `type` values:

| Type | Use for |
|---|---|
| `Runbook` | A procedure someone executes, in order, to get a result. |
| `Reference` | Lookup material — tables, identifiers, system facts. Read, not performed. |
| `Policy` | A rule that constrains a choice, and the reasoning behind it. |
| `Script` | Language delivered verbatim to a customer — call, SMS or email wording. |
| `Template` | A fill-in artifact the reader copies and completes. |

`Process` and `Playbook` were considered and deliberately left out until a doc needs
them; see OQ-003 in `DECISIONS.md`. `Script` and `Template` were added 2026-07-28 for the
wiki ingestion — see OQ-007.

Established `tags`: two axes, applied together.

- **System** — the tool the knowledge is about: `ctm`, `manage-engine`,
  `google-workspace`, `teramind`, `chrome`, `gcpw`, `unifi`, `brother`, `raspberry-pi`,
  `microsoft-365`, `shared-contacts`, `fieldroutes`, `hubspot`, `jamf`, `ringcentral`,
  `podium`, `keeping`, `gam`, `busylight`, `att`, `google-chat`, `gusto`, `uattend`,
  `jamf`, `wex`, `npma`, `quickbooks`, `divvy`, `jazzhr`, `bill-com`, `authorize-net`,
  `transfirst`, `transworld`, `chevron`, `google-ads`, `n8n`, `prismhr`, `principal`, `wise`
- **Topic** — what it concerns: `telephony`, `routing`, `voicemail`, `notifications`,
  `onboarding`, `offboarding`, `provisioning`, `deployment`, `devices`, `security`,
  `access-control`, `printers`, `scanning`, `network`, `door-access`, `email`,
  `signatures`, `contacts`, `crm`, `marketing`, `inventory`, `support`, `policy`,
  `compensation`, `payroll`, `pto`, `attendance`, `holidays`, `benefits`, `safety`,
  `injury`, `uniform`, `recruiting`, `training`, `certification`, `handbook`,
  `technicians`, `fleet`, `vehicles`, `sales`, `bookkeeping`, `receivables`, `payables`,
  `tax`, `vendor-billing`, `credit`, `refunds`, `disputes`, `write-offs`, `budgeting`, `pricing`,
  `commissions`

**Where a procedure spans two systems, the system tag is the entry point** — the system the
task starts in. Handling returned ACH payments is tagged `authorize-net` because the return
is discovered there; the Sentricon submissions are tagged `fieldroutes` because the Sentricon
UI lives inside it. Settled during the batch 4b ingestion.

The vocabulary grows per ingestion batch. Every new value is recorded here **and** in the
`log.md` entry for the batch that introduced it, so additions stay reviewable rather than
accumulating silently.

**`fieldroutes` vs `pestroutes` is unsettled.** The IT documentation calls the CRM
Fieldroutes; the rest of the wiki calls it PestRoutes. Same product, renamed. `fieldroutes`
is provisional — see OQ-008 in `DECISIONS.md`.

A doc usually carries one system tag and one to three topic tags. The pairing is what
lets "everything about CTM" and "everything about routing" both be answerable as the
corpus grows past a single system.

### Root domains

Root directories are org-level groupings, one per department or function:

| Domain | Covers |
|---|---|
| `it/` | Tools, accounts, telephony, devices, and how to get help with them. |
| `operations/` | How the business runs day to day — service workflows, SOPs, checklists, technicians, scheduling, inventory, fleet. |
| `people/` | Employment policy, compensation, hiring, onboarding, safety, team processes. |
| `finance/` | Budgets, reporting cadence, payroll, vendor and billing processes. |
| `customer-care/` | Customer-facing procedures, scripts, cancellations, subscriptions. |
| `sales/` | Inside and outside sales, pricing, leads. |
| `marketing/` | Sources, campaigns, retention. |
| `services/` | Cross-cutting service definitions and per-service SOPs. |

A domain directory is created by the batch that first fills it — never scaffolded
empty, because an `index.md` listing nothing is worse than no directory.

## Content rules

- **Never store secrets or personal data** — no SSNs, bank or account numbers, home
  addresses, passwords, or API keys. This applies to the whole bundle. When a source
  document contains them, describe the problem and redact the value rather than
  transcribing it, so the defect can be fixed without copying it into git.
- **Never fabricate details.** If a source lacks the substance a `type` requires, do
  not write the doc — report it as unconvertible and say why. Where something is
  genuinely unknown, leave a `TODO:` marker rather than guessing.
- **Flag source defects in-file; never silently fix them.** Transcribe faithfully and
  add a blockquote naming the conflict and who needs to resolve it.

## Conventions

- Links between docs are bundle-relative (`/dir/file.md`).
- Consumers MUST NOT reject a bundle for missing optional fields, unknown types, or
  broken cross-links — so prefer writing the doc over blocking on a perfect link.
- `DECISIONS.md` at the repo root is the register for decisions about *how* the base is
  built. Changes to what it *contains* go in the bundle's `log.md`. Both sit outside
  OKF's jurisdiction — see the note at the top of `DECISIONS.md`.
