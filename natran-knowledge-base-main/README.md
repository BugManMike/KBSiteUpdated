# Natran Green Pest Control — Knowledge Base

Internal knowledge base stored as plain Markdown with YAML frontmatter, organized in a
git-friendly folder tree: human-readable, diffable, and portable to any platform later
(no lock-in).

Everything of substance is documentation. There is no application code to build or test.

## Layout

```
docs/                the knowledge base — an OKF v0.2 bundle
  index.md           bundle root; carries okf_version
  log.md             chronological history of changes to the corpus
  <domain>/          one directory per org-level domain
    index.md         directory listing
    <concept>.md     one file per concept

CLAUDE.md            the documentation contract — read this before editing docs
DECISIONS.md         register of decisions and open questions about how the base is built
PROJECT-TODO.md      running project checklist
README.md            this file
```

Start reading at [docs/index.md](docs/index.md). For what changed and why, see
[docs/log.md](docs/log.md).

## Format

The bundle uses the **Open Knowledge Format (OKF)**, pinned at **v0.2**.

Every non-reserved `.md` file carries frontmatter with a `type`, `title`, `description`,
`tags`, and a `generated` block. `index.md` and `log.md` are reserved filenames and are
the only files exempt.

**The full contract is in [CLAUDE.md](CLAUDE.md)** — the type and tag vocabularies, the
one-concept-per-file rule, the placement rule for root directories, and the requirement to
verify the pinned spec version before writing. Read it before adding or editing anything.

## Conventions worth knowing up front

- **One concept per file.** New material gets its own file; it is never appended as a
  section to an existing doc.
- **Links between docs are bundle-relative** — `/it/telephony/ctm-account.md`, not a
  relative path or a URL.
- **`status`** is OKF's own lifecycle field: `draft`, `stable`, `deprecated`. Absent means
  stable. Most of the corpus is currently `draft`, pending confirmation by a domain owner.
- **Never store secrets or personal data** — no SSNs, bank or account numbers, home
  addresses, passwords, or API keys.
- **Source defects are flagged in-file, not silently fixed.** Where a source document
  contradicts itself or another document, the doc transcribes both and adds a blockquote
  naming the conflict and who needs to resolve it. Those blockquotes are the working list
  of things needing a human decision.

## Ownership

**Owner:** `admin@natran.com`. Access is controlled at the repository level; there is no
per-document gating.

## History

The corpus began as CallTrackingMetrics documentation and is being extended by ingesting
the `Natran Wiki` Google Drive folder. Progress, per-batch detail, and the conflicts found
along the way are in [docs/log.md](docs/log.md).

A second parallel tree (`content/`, with its own schema and access model) existed briefly
and was merged into `docs/` on 2026-07-28 — see OQ-009 in [DECISIONS.md](DECISIONS.md).
