"""
MkDocs hook that renders the OKF v0.2 bundle without modifying it.

The bundle's contract (see CLAUDE.md) says links between docs are
bundle-relative — `/it/telephony/ctm-account.md`, not a relative path.
That is correct for the bundle and wrong for a static site, where such a
link resolves against the web server root rather than the bundle root.
There are ~750 of them.

Rather than rewrite 147 source files and break the contract, this hook
translates the links at build time, in memory. The repo stays exactly as
the contract describes it; the site still works, including when served
from a subpath such as GitHub Pages.

It also renders the frontmatter the bundle already carries:

  * `title`   -> the page's H1, since concept files carry their title in
                 frontmatter rather than as a heading in the body
  * `type`    -> a pill (Runbook, Reference, Policy, Script, Template)
  * `tags`    -> pills, and the Material tags index
  * `status`  -> a banner on anything still `draft`, i.e. not yet
                 confirmed by a domain owner. Absent means stable, per OKF.

Nothing here writes to disk.
"""

import posixpath
import re

# ]( /path/to/file.md#anchor )  — the bundle-relative form
BUNDLE_FILE_LINK = re.compile(r"\]\(/([^)\s#]+\.md)(#[^)\s]*)?\)")

# ]( /path/to/dir/ )  — bundle-relative directory link
BUNDLE_DIR_LINK = re.compile(r"\]\(/([^)\s#]*/)\)")

# ]( dir/ )  — a directory link already written relative, as the index.md
# files use. Left alone, MkDocs resolves it against the *page* URL, which
# is wrong for any page not itself at a directory root (log.md, notably).
REL_DIR_LINK = re.compile(r"\]\((?!/|[a-z]+:)([^)\s#]*/)\)")

# Reserved filenames are exempt from frontmatter (CLAUDE.md) and already
# carry their own H1.
RESERVED = ("index.md", "log.md")

TYPE_TITLES = {
    "Runbook": "A procedure someone executes, in order, to get a result.",
    "Reference": "Lookup material. Read, not performed.",
    "Policy": "A rule that constrains a choice, and the reasoning behind it.",
    "Script": "Language delivered verbatim to a customer.",
    "Template": "A fill-in artifact the reader copies and completes.",
}

DRAFT_BANNER = (
    '!!! warning "Draft — not yet confirmed"\n'
    "    No domain owner has reviewed this document. Treat it as a faithful\n"
    "    transcription of its source, not as approved practice.\n"
)


def _rewrite_links(markdown: str, src_uri: str) -> str:
    """Turn bundle-relative links into links relative to this page."""
    src_dir = posixpath.dirname(src_uri)

    def file_repl(match: re.Match) -> str:
        target, anchor = match.group(1), match.group(2) or ""
        return f"]({posixpath.relpath(target, src_dir or '.')}{anchor})"

    def dir_repl(match: re.Match) -> str:
        target = match.group(1)
        rel = posixpath.relpath(target, src_dir or ".")
        # Point at the directory's index.md rather than the bare directory.
        # MkDocs only computes a correct URL for links it can resolve to a
        # real file; a bare `dir/` is left alone and then resolves against
        # the page URL instead of the bundle root.
        return f"]({rel}/index.md)"

    markdown = BUNDLE_FILE_LINK.sub(file_repl, markdown)
    markdown = BUNDLE_DIR_LINK.sub(dir_repl, markdown)
    return REL_DIR_LINK.sub(lambda m: f"]({m.group(1)}index.md)", markdown)


def _header(meta: dict) -> str:
    """Build the title, pills and draft banner from OKF frontmatter."""
    parts = []

    title = meta.get("title")
    if title:
        parts.append(f"# {title}\n")

    pills = []
    doc_type = meta.get("type")
    if doc_type:
        hint = TYPE_TITLES.get(doc_type, "")
        pills.append(
            f'<span class="okf-pill okf-type" title="{hint}">{doc_type}</span>'
        )

    # Tags are deliberately NOT rendered here — Material's tags plugin
    # already renders them above the title, and those chips link through
    # to the tag index. Duplicating them would just be noise.

    if pills:
        parts.append(f'<div class="okf-meta">{"".join(pills)}</div>\n')

    # OKF: absent status means stable.
    if str(meta.get("status", "")).lower() == "draft":
        parts.append(DRAFT_BANNER)

    return "\n".join(parts) + "\n" if parts else ""


def on_page_markdown(markdown, page, config, files, **kwargs):
    src_uri = page.file.src_uri
    markdown = _rewrite_links(markdown, src_uri)

    if posixpath.basename(src_uri) in RESERVED:
        return markdown

    return _header(page.meta or {}) + markdown
