# CLAUDE.md

Guidance for working **on** this repository in Claude Code. It is not loaded when
someone merely uses the skill; it orients whoever clones the repo to modify it.

## What this repo is

The `identidad-personal` skill and two worked example manuals. The skill's method,
what to ask and what it enforces, lives in `SKILL.md`. Read it first; don't restate
it here.

## Working conventions

- **The examples are compiled, not hand-edited.** Each of the two people ships a
  manual and a one-page card, four published files in all. Edit the sources in
  `ejemplo/compilar/` and rebuild; the steps are in
  `ejemplo/compilar/COMO-REGENERAR.md`. Never edit the large self-contained
  `ejemplo/manual-*.html` or `ejemplo/ficha-*.html` by hand: the fonts are
  embedded as base64 and they are not meant to be touched directly.
- **A card's tokens are a copy of its manual's.** Change a palette and you change
  it in both source files, or the card starts stating values the manual no longer
  holds. Nothing enforces this; it has to be done by hand.
- **The index page numbers are written by hand and drift in silence.** Any content
  edit can move the pagination without anything failing. After editing a manual,
  re-check the index against the rebuilt PDF — `COMO-REGENERAR.md` has the check.
- **`assets/plantilla.html` is the mechanical scaffold, not a design.** It carries
  the proven `@page` print CSS and the document structure. Fill its `{{...}}`
  placeholders and `:root` tokens; don't rebuild the print CSS from scratch.
- **`assets/ficha.html` is the same idea for the one-page card,** and it has
  exactly one mechanic worth protecting: it prints to a single page. After any
  change to it, print it and count the pages (headless Chrome with
  `--print-to-pdf` does the job) before committing. It carries no palette of its
  own by design: a filled card copies the manual's `:root` block unchanged, so
  the two cannot drift.
- **Pagination is native.** The paginated PDF comes from the `@page` margin boxes
  rendered by a Chromium browser (Chrome or Edge) with "Background graphics" on.
  There is no pagination library, and none is needed.
- **Fonts are OFL, subset to woff2 and embedded as base64.** For IBM Plex
  (Valentina's manual) regenerate with `ejemplo/compilar/subset-plex.py`.
- **Enforce mechanics, offer taste.** A new rule is only allowed to be binding
  when breaking it produces something measurably wrong: text that fails
  contrast, a value that goes invisible in one version, a page that will not
  print. Anything that is a matter of the person's own colour, type or graphic
  vocabulary goes in as a decision the skill raises and the person closes, not
  as a rule the skill imposes. The skill is a method, and a method that dictates
  taste stops producing a system of the person's own.
- **Verify color contrast by number (WCAG 2.1), never by eye,** for any new
  palette. The example manuals quote real ratios; keep them true if a color changes.
- **Keep both READMEs in step.** `README.md` (English, GitHub's default) and
  `README.es.md` (Spanish) carry the same content; edit them together.
- **Word/`.docx` is not part of this skill.** It points to
  [`ooxmlkit`](https://github.com/Carlos-Padilla-Bravo/ooxmlkit), a separate
  library in its own repository. Don't absorb it: it needs Windows and Word,
  which is exactly what the HTML deliverable avoids. What the two repos share is
  **Ignacia**: her manual is the worked example over there too, so a change to
  her palette or her families here leaves that example stating values this repo
  no longer holds. It is the same drift as a card against its manual, across
  repositories, and nothing enforces it either.

## Layout

- `SKILL.md` — the skill: method and composition rules.
- `assets/plantilla.html` — the reference scaffold the skill fills in.
- `assets/ficha.html` — the one-page identity card scaffold.
- `ejemplo/` — the two finished manuals and their one-page cards (`.html` + `.pdf`)
  plus the sample images; `ejemplo/compilar/` holds the editable sources and the
  rebuild note.
- `README.md` / `README.es.md`, `LICENSE`.

## Verifying a change

There is no test suite; the deliverable is checked on the rendered PDF. After a
change, rebuild and read the PDF page by page: no blank pages, the index page
numbers match the real pagination, and hyphenation leaves nothing ugly.

## Status

Maintained occasionally, with no promise of support. There is one trigger for a
change: the author's own identity manual evolves and the lesson generalises beyond
his case. Anything specific to one person stays out. Issues are disabled, so this
is not a support channel.

Before porting a rule from a real manual, check it against the two example manuals
in `ejemplo/`. A rule that would declare one of them wrong is either not general or
is worded too strongly.
