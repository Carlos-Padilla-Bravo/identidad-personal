---
name: identidad-personal
description: >-
  Guides a person, through questions, to build their own personal brand
  identity manual (color, type, composition and voice) and delivers it finished
  as a self-contained HTML file that prints to a paginated PDF from the browser.
  It is a method of consultation, not a template: it closes each design decision
  before moving on. Works in English and Spanish; it detects or asks the
  person's language and delivers in it. Trigger when someone asks to build,
  create or design their personal brand identity manual, system or guidelines.
  Spanish triggers: construir / crear / diseñar mi manual, sistema o guía de
  identidad o de marca personal.
---

# Identidad Personal — method

This skill guides a person to build their personal brand identity manual. It does not fill in a template: it asks questions, closes decisions with judgment, and delivers the finished manual at the end. Follow the method below from start to finish.

## Language

Detect the person's language or ask at the start. Interact and deliver the manual in that language. The skill works in English and Spanish.

## Interaction principles

They govern the whole path.

- **Speak to the person, about them, directly.** This is personal branding: say "you", "how you work", "how you sound", not "your brand" as if it were a company.
- **Draw it out with questions, do not offer a menu to fill in.** The value is in the decisions the person makes while guided, not in options picked from a list.
- **Close each decision before moving to the next.** Do not open a stage with the previous one unresolved.
- **Few questions per stage.** Have a conversation, do not interrogate with twenty items at once.
- **Recommend, do not just list.** Explain why one option beats another.
- **Stop to consult on what is costly to reverse.** Color direction, type and the signature are closed by asking first, never silently.
- **If the person does not know, propose a reasonable default and move on.** Do not leave them stuck on a decision.

## Design principles

The skill enforces these in the manual it produces.

- **Close the direction before the detail.** The color direction is agreed before writing a single hex value; the type character, before choosing a family.
- **Ration the signal color.** An accent that marks, not one that decorates. Reference proportion: 90% neutrals, 8% primary, 2% signal. That split is calibrated on an extended piece, the kind the reader scrolls or turns through. In a piece that fits in a single view the primary needs more surface, because the elements carrying it (heading, rule, accent) are all present at once on a small area; up to a quarter is still an accompaniment to the neutrals. The signal's ceiling never moves: it marks one thing per piece, on forty pages or on one screen. State the proportion in the manual as depending on the piece, not as one number.
- **Cap the type styles.** A small number (reference: nine). A new style on a whim breaks the system.
- **Verify contrast with a number**, per WCAG 2.1, not by eye. Do not rely on color alone.
- **Freely licensed type by default,** so it can be embedded and reused at no cost and without permission.
- **The logo is a decision point, not a rule.** Ask whether the mark is a logo or a typographic name signature, and branch. The skill does not design the logo; it only documents one that already exists.

## The path

### Phase A. Foundation: who you are

Draw out, in this order, closing each point before moving on. This replaces any profile file: it is built by asking.

1. **Essence.** What you do, reduced to one sentence that stays true when everything else is stripped away.
2. **Territory.** Which areas or disciplines you work in, and what stays out.
3. **Purpose.** What your work exists for.
4. **Personality.** How you behave, marked with opposing examples: closer or more reserved, more technical or more approachable, more cautious or more categorical. A position is chosen, not "all of them".
5. **Audiences.** Who you speak to, and how the register shifts for each.
6. **Tone.** How you sound writing and speaking. Minimal voice rules.

### Phase B. Visual system: how it looks

With the foundation closed, now expressing it. The visual translates what came before; it does not precede it.

1. **Color.** Direction first: what feeling it conveys, what it avoids. Then the values: a dominant neutral, a primary, a rationed signal color, and the proportion between them. Verify the contrast of every pair that carries text.

   **Build the neutrals, do not default to them.** They are 90% of the surface and get the least attention, which is why they are where a first palette usually fails. Three things to close:

   - **No pure greys, and one consistent hue across the ramp.** Every neutral carries a slight tint, and they all lean the same way. A pure grey next to a saturated primary reads dirty, and neutrals that drift in hue make the system look assembled from parts. Whether that tint matches the primary's family or deliberately opposes it is a choice: cool neutrals under a cool primary read as one material; warm neutrals under a cool primary read as a warm-and-cool pairing. Both work. Neutrals with no direction do not.
   - **Every neutral declares its role.** Background, alternate surface, rule, secondary text, main text. A value with no job is a value someone will misuse.
   - **Only as many steps as there are roles.** A short manual needs four; one with tables, notes and metadata needs closer to seven. Do not build a scale for its own sake.

   **Check the palette against the territory.** The territory closed in Phase A names what stays out. Some hues point straight at a sector: yellow-green at agriculture, teal at sustainability and wellness, a saturated violet-blue at digital products. If a value points at something the person excluded, it contradicts the foundation no matter how well it performs on contrast.
2. **Type.** Character first; then a freely licensed family; hierarchy with a cap on styles; a scale built on a fixed ratio.
3. **Signature or logo.** The Phase B decision. With a logo, document its rules: versions, clear space, minimum size, incorrect uses, placement. Without a logo, build the typographic name signature.
4. **Composition.** Grid, margins, the treatment of tables and figures if the manual uses them, and the page format for printing: numbering, header with the name, footer with version and date, and breaks between sections. On screen the manual is continuous; that format appears when printing to PDF. The rules below are not optional.

**Composition rules the skill enforces:**

- **One column measure.** Paragraphs, tables, figures, notes and captions share exactly the same width, justified left and right. No paragraphs narrower than the tables; that ragged right edge shows through the whole manual and is the first thing that gives away poor formatting.
- **All reading text justified,** body, leads, notes and captions, with hyphenation on (`hyphens: auto` and the correct `lang`). Hyphenation removes the gaps justification leaves.
- **Numbering in the structuring color, not the signal.** Section, subsection and table-of-contents numbers go in the primary. Using the signal to number contradicts rationing it: the signal signals; it does not order, and it stays for table and figure labels.
- **The signal marks. It never orders, and it never decorates.** Two uses are legitimate. A **fixed marker**, applied by a style and always meaning the same thing: the table and figure label, the rule down the side of a note block, the mark on the cover. It may repeat, because the reader learns it once and it separates a block from the body around it. And a **content highlight**, chosen instance by instance: inside any one figure, table or block, exactly one thing carries it, the datum or the example the text is arguing about.

  The test for a fixed marker is whether it separates something the layout has not already separated. A list bullet fails it: the list is already a list, so tinting every bullet adds nothing and spends the signal on decoration. A slot in the fixed colour order of chart series fails it worse, because it turns the signal into the name of a category, and a colour that names a category can no longer mean "look here". In a chart the signal goes on top of the datum, over a series that already carries its own colour.
- **Numbered subsections** (3.1, 3.2…) and **the table of contents unfolds the subsections** indented, each with its page number. Contents with no dot leader: title on the left, number on the right. CSS dotted borders print unevenly.
- **Cover as its own page,** separate from the contents; on screen, with a rule and air, not glued to the contents.
- **Figure title at the foot, table title above.** The "Figure N · …" label always sits at the base of the figure; the "Table N · …" label above the table. Same signal marker on both, different position.
- **A dividing rule below the header and above the footer** on interior pages, not on the cover. Draw it with `border-bottom` and `border-top` on the `@page` margin boxes; include the center boxes with a space as content so the line runs unbroken across the width, and drop them on `@page:first`.

### Phase C. The deliverable

1. **Assemble the manual as a self-contained HTML file:** a single page, everything embedded, no external dependencies. Start from the reference scaffold in [`assets/plantilla.html`](assets/plantilla.html), which carries the proven mechanics (the `@page` print boxes, the document structure, one worked example of each block) with no palette or content. Fill its `{{...}}` placeholders and `:root` tokens with the decisions made, embed the chosen fonts as base64, and include a light and a dark version. Do not rebuild the print CSS from scratch: pagination is native, so no pagination library is needed. Printed from a Chromium browser (Chrome or Edge) with "Background graphics" on, the file comes out paginated, with page numbers, header and footer. On screen it stays continuous.
2. **Close with a token sheet:** colors by role, type scale, families. It is the contract other tools can read.
3. **For an editable `.docx`,** there is [`ooxmlkit`](https://github.com/Carlos-Padilla-Bravo/ooxmlkit), a separate published library that generates Word from the same decisions. It is optional and not part of this skill, and it asks for more: closing the document needs Windows and Microsoft Word. The HTML above already prints the formal paginated PDF on any platform.
4. **Hand over the loose tokens too,** to reuse the identity on other pieces or to turn the manual into a skill that other skills consult.

## Structure of the delivered manual

- **Cover.** Signature or name, subtitle and metadata (version, date, status).
- **Table of contents.**

And the numbered sections:

1. Introduction: what it is, what it solves, how to read it and its scope.
2. Essence
3. Purpose and personality
4. Values and tone
5. Color system and roles
6. Typography
7. Signature or logo
8. Graphic elements and composition
9. Usage recommendations
10. Appendices: technical sheet of the system (tokens) and provenance of the typefaces.

The cover, the contents, the introduction and the appendices are fixed. Of the content sections, drop the ones that do not add to a given case. The structure guides; it does not compel.

## What the skill does not do

- It does not design the logo or any graphic mark. It documents one that already exists.
- It does not invent the person's purpose or positioning. It articulates them from what the person already does.
- It does not do corporate identity. It is one person's brand.
- It does not itself produce the `.docx`; that path belongs to [`ooxmlkit`](https://github.com/Carlos-Padilla-Bravo/ooxmlkit), a separate library.
