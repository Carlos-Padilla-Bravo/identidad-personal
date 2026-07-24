# CLAUDE.md

Guidance for working **on** this repository in Claude Code. It is not loaded when
someone merely uses the skill; it orients whoever clones the repo to modify it.

## What this repo is

The `identidad-personal` skill and two worked example manuals. The skill's method,
what to ask and what it enforces, lives in `SKILL.md`. Read it first; don't restate
it here.

## Working conventions

- **The example manuals are compiled, not hand-edited.** Edit the sources in
  `ejemplo/compilar/` and rebuild; the steps are in
  `ejemplo/compilar/COMO-REGENERAR.md`. Never edit the large self-contained
  `ejemplo/manual-*.html` by hand: the fonts are embedded as base64 and it is not
  meant to be touched directly.
- **`assets/plantilla.html` is the mechanical scaffold, not a design.** It carries
  the proven `@page` print CSS and the document structure. Fill its `{{...}}`
  placeholders and `:root` tokens; don't rebuild the print CSS from scratch.
- **Pagination is native.** The paginated PDF comes from the `@page` margin boxes
  rendered by a Chromium browser (Chrome or Edge) with "Background graphics" on.
  There is no pagination library, and none is needed.
- **Fonts are OFL, subset to woff2 and embedded as base64.** For IBM Plex
  (Valentina's manual) regenerate with `ejemplo/compilar/subset-plex.py`.
- **Verify color contrast by number (WCAG 2.1), never by eye,** for any new
  palette. The example manuals quote real ratios; keep them true if a color changes.
- **Keep both READMEs in step.** `README.md` (English, GitHub's default) and
  `README.es.md` (Spanish) carry the same content; edit them together.
- **Word/`.docx` is not part of this skill.** It points to `wordkit`, a separate
  library in its own repository.

## Layout

- `SKILL.md` — the skill: method and composition rules.
- `assets/plantilla.html` — the reference scaffold the skill fills in.
- `ejemplo/` — the two finished manuals (`.html` + `.pdf`) and their sample images;
  `ejemplo/compilar/` holds the editable sources and the rebuild note.
- `README.md` / `README.es.md`, `LICENSE`.

## Verifying a change

There is no test suite; the deliverable is checked on the rendered PDF. After a
change, rebuild and read the PDF page by page: no blank pages, the index page
numbers match the real pagination, and hyphenation leaves nothing ugly.

## Status

Archived: published as is, with no maintenance promised.
