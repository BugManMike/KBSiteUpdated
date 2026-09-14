# Decisions & Open Questions

Working register for decisions and pending discussion items about this knowledge
base — how it's built, not what it contains.

**This file sits deliberately outside the OKF bundle.** OKF §3.1 reserves exactly
two filenames (`index.md`, `log.md`) and states that all other `.md` files *are*
concept documents — so anything inside `docs/` would need a `type` and would
travel with the bundle as if it were company knowledge. §3 permits a bundle to be
"a subdirectory within a larger repository," which puts the repo root outside the
spec's jurisdiction. `CLAUDE.md` already lives here on the same basis.

Two consequences of being out of scope: no frontmatter is required, and `Status`
below is a plain field — there's no collision with OKF's spec-owned `status`
lifecycle (`draft`/`stable`/`deprecated`), which only governs documents inside
the bundle.

Naming follows the Architecture Decision Record convention (Nygard, 2011) rather
than anything OKF specifies, because OKF specifies nothing here. Resolved items
keep their context and consequences so the reasoning survives; changes to the
corpus itself get recorded in the bundle's `log.md`.

---

# Open

## OQ-012 — How do OKF rules scope per project, and how does finished project work reach this bundle?

- **Status**: open — **agreed in principle 2026-08-11, nothing built**
- **Raised**: 2026-08-11
- **Blocks**: nothing; the cost is drift that compounds with every new project repo

Two problems with one cause. The global `~/.claude/CLAUDE.md` carries an OKF section that
is in context on *every* project regardless of relevance, yet is too thin to author a
conformant doc and too generic to fit any particular repo. It omits `resource`, the
`sources` and `verified` families, `stale_after`, the actor convention, and the derived
trust tiers.

**The drift is already measurable.** `generated.by` exists in four incompatible forms:

| Where | Value |
|---|---|
| This bundle (147 docs) | `Claude (Opus 5)` |
| `aps-knowledge-base` | `claude-opus-5` |
| `zoho-me-deploy-teramind` | `Claude (claude-opus-4-8)` |
| OKF's own convention | `<producer>/<version>`, `human:<id>`, `process:<id>` |

That project also uses lowercase ad-hoc types — `readme`, `changelog`, `troubleshooting` —
matching neither this bundle's five-value vocabulary nor APS's.

The second problem: there is no path by which knowledge produced during a project reaches
this bundle. It stays in the project repo until someone remembers.

**Agreed in principle, per Michael:**

| Question | Choice |
|---|---|
| Which bundle is master | This repo |
| Where detailed OKF rules live | A global Claude skill, loaded only when authoring OKF docs, plus a per-repo `docs/meta/` for that repo's closed vocabulary |
| What lands here from a finished project | **Distilled concepts** — not full copies, not pointers |
| How it gets remembered | A guarded `Stop` hook, not a CLAUDE.md reminder |

**Why distilled.** Two findings decided it. First, 21 files under `docs/` already match
teramind/endpoint-central — including [the Teramind agent deployment
runbook](docs/it/devices/teramind-agent-deployment.md) — so publishing that project is
mostly an *update* against existing concepts. A full copy would create a second,
conflicting Teramind runbook. Second, `zoho-me-deploy-teramind` has no git remote and sits
under `localonly/`, so a pointer `resource:` would resolve on exactly one machine.
Separately, `readme` and `changelog` are repo artifacts, not company knowledge, and should
never enter the bundle at all.

**Why a hook rather than an instruction.** `CLAUDE.md` is context, not a trigger — nothing
executes it, which is the same weakness that produced the four actor forms above. Of the
available events, `SessionEnd` cannot inject context and fires after the user has left;
`Stop` can inject but fires every turn, so it needs a guard (OKF docs changed, tree clean,
commits ahead of a per-repo published marker) or it becomes noise.

**Two corrections to the original sketch, found on reading this repo:**

- It proposed porting the validator from `aps-data-warehouse`. Unnecessary — this repo
  already has `scripts/check-bundle.py`. Extend that instead.
- A machine-readable `docs/meta/` vocabulary is precisely what **OQ-011** says is missing
  when it notes that `CLAUDE.md`'s prose table "is not" a machine-readable place. The two
  items share a fix and should be resolved together.

**The mechanism above only defends part of the problem.** Getting project knowledge into
this bundle is a pipeline with three failure points — *capture* (the knowledge exists in a
durable file at all), *trigger* (something notices it is time to publish), and *transfer*
(the distill-and-write). A skill and a hook address trigger and transfer. Most loss happens
at capture, and four distinct leaks are currently undefended:

| Leak | Covered by the above? |
|---|---|
| Project wrote OKF docs but never published them | Yes — hook plus publish skill |
| Knowledge produced during a working session, never written to any file | **No** |
| Repos that will never carry OKF docs — `natran-sales-portal` holds 12 KB of architecture in its `CLAUDE.md`, `natran-n8n-automation` documents live business automations | **No** |
| Repos never revisited — `zoho-me-deploy-teramind` has no git remote and sits under `localonly/`; deleting the folder loses everything in it | **No** |

The second leak is the largest and the least visible. The findings that produced *this*
entry — the four actor forms, the 21-file overlap with existing Teramind concepts, the fact
that a `SessionEnd` hook cannot inject context — existed in no file anywhere. They came out
of a working session and survive only because they were written here by hand. A trigger that
fires at the end of a session finds nothing to publish if nothing was captured during it.

The fourth leak needs a different mechanism entirely. A `Stop` hook is **reactive** — it can
only fire in a session someone happens to start in that repo, so it structurally cannot reach
the repos nobody opens again. That needs a **periodic sweep**: something that walks the repo
set, compares each against this bundle, and reports what never landed. Worth noting that this
register's own repo demonstrated the failure mode during the session that raised this item —
three stale git locks from a killed `git maintenance` run on 2026-07-28 had silently blocked
every write for two weeks, leaving the n8n documentation uncommitted and one disk failure from
gone. Nothing surfaced it; a sweep would have.

**A last weakness worth recording:** distillation needs judgment, so it is skippable. If the
nudge arrives at a bad moment it gets dismissed, and if the sweep grows noisy it gets ignored.
A system that accepts only polished concepts will quietly accept nothing, so it should degrade
gracefully — a rough captured note carrying its provenance is worth more than a perfect concept
never written.

So the full shape is four legs, not two: **capture** as a working norm while the knowledge is
still in context, **trigger** at wrap-up, **sweep** for everything the trigger cannot reach, and
**close the loop** via `sources` and `stale_after` so the bundle can answer where a concept came
from and whether it has rotted.

**Not settled, and deliberately left open:**

- Whether to adopt OKF's actor convention here. 147 docs carry `Claude (Opus 5)`; changing
  it means a backfill or a knowingly mixed corpus.
- Whether the spec pin should move to a commit-pinned URL. `aps-data-warehouse` pins commit
  `3fcbb9f` and records that the raw `main` URL served v0.1 — which is the same stale-render
  behaviour **OQ-001** hit, and OQ-001 explicitly left "whether v0.2 exists on a tag, branch,
  or release" uninvestigated.
- Whether APS material belongs here at all. Already carried in `PROJECT-TODO.md`; choosing
  this repo as master sharpens it, because APS is a separate GitHub org with a
  non-overlapping vocabulary (12 coarse tags vs ~90 on two axes).

Nothing has been implemented. No skill, hook, `docs/meta/` directory, or validator change
exists yet.

## OQ-011 — Nothing validates the `tags` vocabulary

- **Status**: open
- **Raised**: 2026-07-28, during batch 4b
- **Blocks**: nothing; it is the mechanism by which the other tag problems went unnoticed

`scripts/check-bundle.py` validates `type` against a hardcoded `VOCAB` set and rejects
anything outside it. **It does not check `tags` at all** — it only confirms the key is
present. Tags are therefore free text, and two consequences have already materialised:

- **The recorded vocabulary drifted behind actual usage.** `quickbooks`, `bookkeeping`,
  `receivables`, `divvy`, `jazzhr`, `vehicles` and `sales` were all in the corpus while
  absent from the `CLAUDE.md` table. Brought current during batch 4b, but nothing stops it
  recurring.
- **A typo survived as a vocabulary value.** `docs/operations/production-vs-materials.md`
  carries the tag `vim`, which is almost certainly a mistyping of something else. It is the
  only use of that value in the corpus. Left alone — it predates batch 4b and is not that
  batch's to fix.

`CLAUDE.md` instructs reusing established values and proposing rather than coining
additions. That instruction is currently enforced by nothing but attention.

Three options:

| Option | Consequence |
|---|---|
| Extend `check-bundle.py` to validate tags against a list | Catches typos and silent coining at the point of writing. Needs the list kept in one machine-readable place, which `CLAUDE.md`'s prose table is not. |
| Have the script *report* unrecognised tags as warnings, not errors | Keeps batch velocity — a new value is surfaced for review rather than blocking. Warnings get ignored once there are enough of them. |
| Leave it to review | Zero tooling cost. This is the status quo, and it produced the drift above. |

The middle option matches how the seven `missing status:` warnings are already handled, so
there is precedent for a warning tier that humans triage.

**Not urgent, but cheapest to do before batch 5**, which lands the bulk of CRM material and
will introduce another wave of tags.

## OQ-010 — When a procedure spans two systems, which gets the system tag?

- **Status**: **decided provisionally during batch 4b — wants ratification**
- **Raised**: 2026-07-28
- **Blocks**: nothing; but 11 docs already depend on the answer

`CLAUDE.md` says a doc "usually carries one system tag and one to three topic tags". Batch
4b was the first batch where that broke down repeatedly: many finance procedures genuinely
span two systems — a payment gateway *and* the CRM, a vendor portal *and* Bill.com, the CRM
*and* QuickBooks.

**The rule applied: the system tag is the task's entry point** — the system the procedure
starts in, or where the triggering fact is discovered.

So [handling returned ACH payments](docs/finance/returned-ach-payments.md) is tagged
`authorize-net`, because the return is discovered in the gateway even though most of the work
happens in the CRM; the Sentricon submissions are tagged `fieldroutes`, because the Sentricon
UI lives inside the CRM even though the counterparty is Corteva.

**Recorded in `CLAUDE.md` and applied across batch 4b.** Flagged here rather than buried
because it was settled mid-ingestion by whoever was writing, not agreed in advance.

Two consequences worth a look:

- **It suppresses counterparty tags.** `corteva` and `king-ranch` were deliberately not
  added, on the grounds that they are counterparties rather than systems anyone signs into.
  That is defensible, but it means "everything we do with Corteva" is not answerable by tag —
  only by full-text search.
- **The alternative — allowing two system tags — was not tried.** `CLAUDE.md` says "usually
  one", not "exactly one", so nothing forbade it. It would make cross-system procedures
  findable from either side at the cost of a fuzzier convention.

If the entry-point rule is wrong, the cost of reversing it is retagging roughly 11 docs, and
it compounds the same way OQ-008 does.

## OQ-008 — Is the CRM tagged `fieldroutes` or `pestroutes`?

- **Status**: open
- **Raised**: 2026-07-28
- **Blocks**: nothing yet; grows more expensive with every batch

The CRM was renamed PestRoutes → FieldRoutes. The `IT single-source-of-truth` doc calls it
**Fieldroutes** and the tenant URL is `natrangreen.fieldroutes.com`. Every other document
in the wiki — dozens of them, across Customer Care, Operations, Accounting and Sales —
calls it **Pestroutes**, and refers to "Pestroutes" menus, reports and Access Control
profiles by that name.

Batch 1 used `fieldroutes` provisionally, on one document. The cost of switching is one
retag today and grows with each batch that files CRM material.

Three options, none obviously right:

| Option | Consequence |
|---|---|
| `fieldroutes` | Matches the vendor's current name and the live URL. Diverges from the words staff actually use and from every source document. |
| `pestroutes` | Matches the corpus and staff vocabulary. Encodes a retired product name that will read as stale to anyone new. |
| `pestroutes` with `fieldroutes` as an alias | Needs a tag-alias concept the bundle does not have, and OKF does not provide one. |

Worth deciding before Batch 5 (Customer Care), which is where the bulk of CRM material
lands.

## OQ-007 — `Script` and `Template` added to the `type` vocabulary

- **Status**: open
- **Raised**: 2026-07-28
- **Blocks**: nothing; recorded for review

Added on Michael's approval during the wiki-ingestion scoping, on the same
propose-rather-than-coin basis as OQ-003.

`Script` covers language delivered verbatim to a customer — the Cancellation Script, the
Customer Care Script, the SMS and email follow-up sets. `Runbook` was the alternative and
fits badly: a call script is not a procedure executed in order to get a result, and
labelling it one loses the distinction that matters, which is that the words themselves are
the artifact.

`Template` covers fill-in artifacts the reader copies and completes.

**Neither is used yet.** Batch 1 (the IT document) produced only `Runbook`, `Reference` and
`Policy`. Both new values were approved ahead of the Customer Care and Sales batches, which
is where the material sits. Listed as open rather than resolved because a type approved
before any document uses it is still a guess about future shape — the same reasoning that
held `Process` and `Playbook` back under OQ-003. Resolve once real documents carry them.

## OQ-005 — Which surface is canonical after the wiki migration?

- **Status**: open
- **Raised**: 2026-07-26
- **Blocks**: nothing yet. Forcing point is Phase 3 (see below).

The `Natran Wiki` shared-drive folder (`1gfI4Z18Rmd6UnjTm0Xned1SvdiwQ0GZQ`) holds
roughly 322 files across three levels, fronted by a YouNeedAWiki instance. If its
content migrates into this bundle while the originals stay editable, the two
corpora diverge and neither can be trusted.

**Corrected 2026-07-28 by full enumeration.** The folder holds **72 folders and ~438
files across six levels** (root plus five). The deepest path is
`Sales and Marketing / Sales / Sales Support Rep Documents / Report Guides / Report
Templates`. Of those files only ~242 are real content: ~96 are link stubs (a ~1024-byte
document whose *title* is a markdown link and whose body is empty), ~95 are binaries, and
~5 are navigation shells. The "three levels" estimate above was wrong in a way that
matters — it implied a flat corpus that could be walked in one pass.

**Two findings that bear directly on this question.** First, the divergence risk is no
longer theoretical: the `IT single-source-of-truth` doc (ingested 2026-07-28, Batch 1)
contains a full CallTrackingMetrics section covering the same ground as the seven existing
`ctm-*` concepts, and the two sources already disagree on the new-user role and the
voicemail greeting. Divergence arrived before the migration finished. Second, the doc that
OQ-005 names as the Phase-3 forcing point — `Natran Core Processes`, 432 KB, multi-tab —
is the target of **at least 20 link stubs** scattered across the tree. It is not one
document among many; it is the hub the wiki's navigation depends on. Shredding it breaks
every one of those stubs, which is a second, separate reason the question cannot stay
deferred past Phase 3.

**No divergence is possible today.** The two corpora cover disjoint material: this
repo is CTM-only, and the wiki contains no CTM documentation at all. The risk
begins when `Natran Core Processes` is shredded into concept files while the
Google Doc still holds the same content — Phase 3 of the migration. That is the
deadline for answering, not now.

**The decidable form of this question is about audience, not governance.** A
bookkeeper working a Friday checklist, or a care rep reaching for the cancellation
script mid-call, will not open a git client. If no reader-facing render of this
bundle is ever built, the wiki cannot be frozen, because it serves readers the
repo structurally cannot. So the question to actually answer is: *is anyone going
to build a way for staff to read this outside a git client?*

It is therefore not the binary it first appears. Three options:

| Option | Consequence |
|---|---|
| Repo canonical, wiki frozen | Cleanest lineage. Strands every daily operational reader unless a renderer exists. |
| Wiki canonical, repo derived | The OKF contract becomes decorative — one-concept-per-file cannot be enforced against a Google Doc with tabs. |
| **Canonical per domain** | Divergence stays bounded because the domains don't overlap. Needs no global answer. |

The per-domain split is already drawn by who reads what: telephony, IT, accounting
internals and the vocabularies are read by Michael and can be repo-canonical
immediately; scripts, prep sheets, and care/dispatch SOPs are read by staff daily
and stay wiki-canonical until there is a renderer. A global answer is only needed
if everything must later live in one place.

Deferred 2026-07-26 — Michael unsure, and deferring is safe until Phase 3.

**Update 2026-09-14 — the renderer now exists; the question is no longer about whether one is
possible.** A MkDocs Material site over `docs/` was built and verified against the full bundle: all
167 files render, search works, navigation is generated from the folder tree so later batches appear
without config changes, and the ~750 bundle-relative links are translated at build time by
`hooks/okf.py` rather than by editing a single source file. The OKF contract is untouched and
`scripts/check-bundle.py` still passes. See `docs-site-setup.md`.

**What that changes.** The decidable form of this question was *"is anyone going to build a way for
staff to read this outside a git client?"* — and the answer is now yes, pending one decision: **where
it is hosted.** The bundle is internal (account identifiers, access paths, control procedures, named
individuals), and **GitHub Pages on a private repository requires GitHub Enterprise Cloud** — on a
Free, Pro or Team plan, enabling Pages publishes the site publicly regardless of repo visibility. The
deploy job is written but commented out for exactly that reason. Cloudflare Pages behind Access, using
the Google Workspace login staff already have, is the recommended fit.

**What it does not change.** The per-domain split in the table above is still the right answer for
the interim, and `Natran Core Processes` is still the Phase-3 forcing point. **Close this question by
choosing a host and announcing the URL**, not by choosing between repo and wiki in the abstract.

---

## OQ-002 — Where should existing policy content come from?

- **Status**: open
- **Raised**: 2026-07-26
- **Blocks**: all content authoring

Candidate sources, not mutually exclusive:

| Source | What it would give us |
|---|---|
| Interview Michael | Highest fidelity to actual practice; slowest |
| Google Drive | Existing handbooks, SOPs, policy docs to convert |
| Connected systems | HubSpot (sales stages), Front (care tags/SLAs), Gusto (HR/onboarding), CallTrackingMetrics (call routing) |
| Best-practice scaffolding | Fast generic drafts to correct; risks encoding fiction as policy |

Deferred on 2026-07-26 — to be asked again. Nothing substantive can be written
until this is answered; the failure mode of guessing is documentation that reads
as authoritative while being wrong, which is worse than an empty repo.

**Partially answered 2026-07-26 for CTM only.** The seven `ctm-*` docs came from
the first two rows of that table in combination: process definition and gotchas
direct from Michael over several working sessions, cross-checked against live
reads of the CTM API for account 448519 (entity counts, field names, pagination
behaviour). No best-practice scaffolding was used, so nothing in those docs is
generic filler.

That pairing — interview plus live system read — is the pattern worth repeating.
The interview supplies intent and the exceptions that no API exposes; the system
read catches drift and supplies identifiers nobody remembers correctly. Neither
alone would have been sufficient: the API cannot see queue weights or the reason
Billing takes no backups, and the interview would not have caught that CTM's
`filter` parameters are silently ignored.

Still open for every other domain.

---

## OQ-001 — Live OKF spec declares v0.1, not the pinned v0.2

- **Status**: **reopened 2026-07-29** — was resolved 2026-07-26, closed 2026-07-28, and the
  discrepancy has since returned
- **Raised**: 2026-07-26
- **Blocks**: nothing; the pin holds and no document is invalid either way

**Context.** The raw spec at `main` declares `Version 0.1 — Draft`, which is
*behind* the version CLAUDE.md pins, not ahead of it. Fields CLAUDE.md treats as
spec-owned that have no basis in the live v0.1 text:

- `status` (draft/stable/deprecated) — absent from v0.1
- `sources`, `verified`, `stale_after` — absent from v0.1
- `generated: {by, at}` — v0.1 instead recommends a flat `timestamp`

Unchanged between the two: `type` is the only required field, `index.md` and
`log.md` are the reserved filenames, and `okf_version` is declared in the
bundle-root `index.md` frontmatter.

**Consequences.** Docs use the CLAUDE.md house frontmatter, which a strict v0.1
consumer sees as unknown extra keys — harmless, since §9 requires consumers to
tolerate them. Whether v0.2 exists on a tag, branch, or release was **not**
investigated; if the pin ever needs justifying, that's the first place to look.

**Closed 2026-07-28.** The raw spec at `main` was observed to declare `Version 0.2`, with
§12 confirming it, so the discrepancy was recorded as no longer existing.

**Reopened 2026-07-29**, during the Collect or Do Not Service split. The raw spec declared
`Version 0.1 — Draft` again — no §12, the document ends at §11 plus Appendix A. Decision was
again to **stay pinned at v0.2**, per Michael; `CLAUDE.md` is unchanged.

**This is now the third observation of v0.1 and the second contradiction inside this repo.** The
2026-07-28 closure above and the `n8n notification workflows` entry in `docs/log.md` are dated the
same day and disagree with each other: one records `main` at v0.2, the other records the
cache-busted fetch returning v0.1. Two readings are consistent with the evidence:

| Reading | What follows |
|---|---|
| `main` genuinely oscillates, or v0.2 was reverted | The pin is defensible but describes a version that is not reliably retrievable. `CLAUDE.md`'s "fetch and confirm" step can never pass, so it will keep firing on every batch. |
| One or more fetches saw a stale cache | The check is working as designed and the noise is expected. `CLAUDE.md` already warns caches serve stale renders "for hours after a release". |

**A confounder worth recording:** on 2026-07-29 the cache-busting query string was **stripped by a
redirect** — the request to `…/SPEC.md?t=<now>` was followed to `…/SPEC.md` with no query. So the
cache-buster `CLAUDE.md` mandates may not be doing anything on that host, which would make every
"cache-busted" observation in this register unreliable, including the ones that saw v0.2.

**Cheapest way to settle it**, and the thing deliberately not done three times now: check the
`knowledge-catalog` repo's tags, releases and commit history for `okf/SPEC.md`. That distinguishes the
two readings outright and costs one pass. Until someone does, this item should stay open rather than
being closed a third time on a single observation.

---

# Resolved

## OQ-009 — How do the company KB (`content/`) and the OKF bundle (`docs/`) relate?

- **Status**: resolved
- **Raised**: 2026-07-27 (as an open item in `PROJECT-TODO.md`)
- **Resolved**: 2026-07-28 — **merge into `docs/`; retire the company KB contract**, per
  Michael

**Context.** The repo carried two parallel documentation contracts. `docs/` was an OKF
v0.2 bundle. `content/` was a "company KB" with its own frontmatter schema (`id`,
`section`, `owner`, `version`, embedded `changelog`), its own status values
(`draft → review → published`), and an access model (`visibility: open | gated` plus
`allowed_roles`), governed by `taxonomy.yml`, `_templates/page.md`, `CHANGELOG.md` and
half of `README.md`. `CLAUDE.md` instructed that neither tree's rules be applied to the
other.

`PROJECT-TODO.md` recorded the relationship as an open decision from the day the second
tree was created.

**Why merging was cheap.** `content/` held **eight files and no real content** — four
`_section.md` landing pages and four pages whose entire body was *"TODO: replace this
placeholder with the first real X page."* Its four sections (`operations`, `it`, `people`,
`finance`) already matched the domain names the OKF bundle was growing. `content/it/_section.md`
had itself started deferring to the bundle: *"Detailed CTM/telephony runbooks currently
live in the OKF bundle at `docs/it/telephony/` — link to them from pages here rather than
duplicating."*

So the second tree never diverged from the first, because it never contained anything.

**The one real question was access control.** `content/people` was gated to
`[leadership, hr]` and `content/finance` to `[leadership, finance]`. OKF v0.2 has no
access-control concept, so merging drops per-document gating. Two options were put to
Michael: carry `visibility`/`allowed_roles` as project-specific frontmatter — legitimate,
since the OKF contract already permits project-specific state axes beside the spec-owned
`status` — or drop it.

**Decided: drop it.** Access is controlled at the repository level, so every document in
`docs/` is equally restricted, and per-document gating would have been metadata nothing
enforces. The `leadership` / `hr` / `finance` role vocabulary is retired with it.

**Consequences.**

- Deleted: `content/`, `taxonomy.yml`, `_templates/`, `CHANGELOG.md`.
- `README.md` rewritten to describe the single bundle. `CLAUDE.md`'s two-contract preamble
  and its entire "Company KB" section removed.
- **One rule was promoted rather than lost.** "Never store secrets or personal data — no
  SSNs, bank/account numbers, home addresses, passwords, or API keys" was scoped to
  `content/` only. It is now a bundle-wide content rule in `CLAUDE.md`. This matters more
  than it looks: batch 3 found a fuel PIN derived from employees' Social Security numbers
  and shared passwords emailed in plaintext, so the rule now covers the tree where that
  material actually lands.
- The four section descriptions were folded into the corresponding `docs/*/index.md` files.
  `finance/` was **not** scaffolded — it is created by the batch that first fills it, per
  the no-empty-directory rule.
- `docs/log.md` is now the single history for the corpus; `CHANGELOG.md` is gone.
- The status-value collision that `CLAUDE.md` warned about no longer exists. Only OKF's
  `draft` / `stable` / `deprecated` remain.

**What this does not resolve.** OQ-005 — which surface is canonical once the wiki
migration completes — is untouched. Collapsing two git trees into one says nothing about
whether the repo or the YouNeedAWiki instance is authoritative for staff readers.

## OQ-006 — Where do tool-specific docs sit in the bundle hierarchy?

- **Status**: resolved
- **Raised**: 2026-07-26
- **Resolved**: 2026-07-26 — **nothing tool- or function-specific at the bundle
  root; telephony nests under `it/`**, per Michael

**Context.** The wiki-migration scoping survey proposed a bundle layout with
`telephony/` as a root-level directory sitting beside `it/`. Michael rejected
that placement: telephony is an IT function, and a root that mixes org-level
groupings with individual tools stops scaling the moment a second tool arrives.

**Consequences.** The seven `ctm-*` concepts move to `/it/telephony/`. The rule
is recorded in `CLAUDE.md`: root directories are org-level groupings; tool- and
function-specific material nests under the owning department. Promotion to a
full bundle happened with this change — earlier than the ~10-doc guideline —
because directory nesting requires the bundle scaffolding anyway.

## OQ-003 — `type` and `tags` vocabularies are undefined

- **Status**: resolved
- **Raised**: 2026-07-26
- **Resolved**: 2026-07-26 — **`Runbook` / `Reference` / `Policy`; tags on a
  system + topic pairing**, per Michael

**Context.** Both vocabularies were empty and CLAUDE.md forbids coining values ad
hoc, which blocked the first real authoring pass. Five `type` candidates had been
floated: `Policy`, `Process`, `Playbook`, `Runbook`, `Reference`.

Three were adopted. `Runbook` covers procedures someone executes, `Reference`
covers lookup material, `Policy` covers rules that constrain a choice. `Process`
and `Playbook` were held back rather than defined speculatively — the CTM corpus
did not need them, and a type defined before a doc requires it is a guess about
future shape.

Tags use two axes applied together: one **system** tag (`ctm`) and one to three
**topic** tags (`telephony`, `routing`, `voicemail`, `notifications`,
`onboarding`). Topic-only was considered and rejected: the system is obvious
from the title today, but stops being obvious the moment a second system enters
the corpus, and retrofitting a tag axis across existing docs is worse than
carrying one slightly redundant tag now.

**Consequences.** Values recorded in CLAUDE.md. The vocabulary is expected to
grow — the bar for a new value is a doc that genuinely does not fit, proposed
rather than coined, same as before.

## OQ-004 — Does meta content belong in the corpus?

- **Status**: resolved
- **Raised**: 2026-07-26
- **Resolved**: 2026-07-26 — **no; keep meta at repo root, outside the bundle**

**Context.** The register was initially written to `docs/open-questions.md` with
a coined `type: Register`, which sat awkwardly beside real company-process
concepts and required defending a vocabulary value that existed only to describe
project bookkeeping.

**Consequences.** The `Register` type is withdrawn before it entered the
vocabulary. `docs/` now contains only genuine company knowledge. The register no
longer travels with the bundle if it's ever distributed — acceptable, since its
audience is us, not consumers of the corpus.

---

# Citations

[1] [OKF SPEC.md at main, retrieved 2026-07-26](https://raw.githubusercontent.com/GoogleCloudPlatform/knowledge-catalog/main/okf/SPEC.md)
[2] [Michael Nygard, "Documenting Architecture Decisions" (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
