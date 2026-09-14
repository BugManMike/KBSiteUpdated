# Rendered site for the bundle

A static site over `docs/`, built with MkDocs Material. It exists to answer OQ-005: staff who
read this corpus daily — a bookkeeper on a Friday checklist, a care rep mid-call — will not
open a git client, and the wiki cannot be frozen until they have somewhere else to read.

**The bundle is not modified.** No source file changed, the OKF v0.2 contract in `CLAUDE.md`
still describes the repo exactly, and `scripts/check-bundle.py` still passes. Everything the
site needs is done at build time.

## What was added

| File | Purpose |
|---|---|
| `mkdocs.yml` | Site configuration. `strict: true` — a broken link fails the build. |
| `hooks/okf.py` | Build-time adapter between the bundle contract and the web. See below. |
| `docs/assets/okf.css` | Styling for the type and tag pills. |
| `requirements-docs.txt` | Pinned `mkdocs` and `mkdocs-material`. |
| `.github/workflows/docs.yml` | CI: runs `check-bundle.py`, then builds the site. Deploy job included but commented out — read the hosting section first. |

## Run it locally

```bash
pip install -r requirements-docs.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # static output into site/
```

`mkdocs serve` live-reloads, which makes it a decent way to review an ingestion batch before
committing it.

## What the hook does, and why it exists

`CLAUDE.md` specifies that links between docs are **bundle-relative** — `/it/telephony/ctm-account.md`.
That is right for the bundle and wrong for a web server, where a leading `/` means the server
root, not the bundle root. There are **~750 such links** across the corpus, and they would all
break — silently, and worse if the site is ever served from a subpath like `/natran-knowledge-base/`.

The two available fixes were: rewrite 750 links across 147 files and change the contract, or
translate at build time. The hook does the second. It:

1. Rewrites bundle-relative links to page-relative ones in memory, so MkDocs can resolve and
   verify every one of them.
2. Points bare directory links at that directory's `index.md`, so they resolve from any page
   depth rather than against the current page's URL.
3. Renders the frontmatter the bundle already carries — `title` becomes the page's H1 (concept
   files carry their title in frontmatter, not as a body heading), `type` and `tags` become
   pills, and `tags` also feed Material's tag index.
4. Puts a **"Draft — not yet confirmed"** banner on every page with `status: draft`. Per OKF,
   absent means stable, so the seven original CTM docs show no banner.

That last one is deliberate. 124 of the bundle's files are `draft` with no domain owner named.
Making that visible on the page is the cheapest pressure toward getting it resolved — a reader
can see that nobody has vouched for what they are reading.

## Navigation

There is no `nav:` block. MkDocs generates navigation from the folder tree, so **batches 4c
through 8 will appear automatically** with no config edits. Section landing pages are each
directory's existing `index.md`.

Search across title, tags and body — the third item under "Features to build" in
`PROJECT-TODO.md` — comes from the built-in search plugin and needs nothing further.

## Hosting — decide this before enabling the deploy job

**This bundle is internal.** It contains account identifiers, access paths, control procedures
and named individuals. It must not be served publicly.

> **GitHub Pages on a private repository requires GitHub Enterprise Cloud.** On a Free, Pro or
> Team plan, turning on Pages publishes the site **publicly** no matter the repository's
> visibility. Confirm the plan before enabling the deploy job in `.github/workflows/docs.yml`.

Options, cheapest first:

| Option | Access control | Notes |
|---|---|---|
| **CI artifact only** (as shipped) | Repo permissions | Every run uploads `site/`. Zero hosting decisions; reviewers download it. Not a daily-reader surface. |
| **Cloudflare Pages + Access** | Google Workspace SSO | Free tier covers this. Staff sign in with their Natran account. The most direct fit given Workspace is already the identity provider. |
| **GitHub Pages, private** | GitHub org membership | Only on Enterprise Cloud. Simplest if you already have it — uncomment the deploy job. |
| **Internal host** | Network / existing SSO | `mkdocs build` output is plain static files; any internal web server serves them. |

Cloudflare Pages with Access in front is the recommendation: it puts the site behind the
Google Workspace login staff already have, and costs nothing at this size.

Whichever you pick, set `site_url` in `mkdocs.yml` afterwards — the 404 page and the sitemap
need it.

## Once it is live

This is the moment OQ-005 becomes decidable, so close it rather than letting it drift:

1. Set `site_url`, `repo_url` and `edit_uri` in `mkdocs.yml`. `edit_uri` puts an edit link on
   every page, which is what lets a domain owner fix something without asking anyone.
2. Announce the URL to the people who read the wiki daily, pointing at their own section.
3. Put a "moved — now at &lt;url&gt;" banner on the migrated wiki pages. Do not delete them yet.
4. Freeze the migrated parts of the wiki to read-only.
5. Record the decision in `DECISIONS.md` under OQ-005 and close it.
