---
name: nklmilojevic
description: GitHub profile README set as Belgrade street-name and house-number enamel plates.
colors:
  enamel: "#1b4592"
  ink: "#f5f7fa"
  enamel-shadow: "#0e2657"
typography:
  plate-name-cyrillic:
    fontFamily: "Fira Sans Condensed"
    fontSize: "84px"
    fontWeight: 700
    letterSpacing: "0.01em"
  street-cyrillic:
    fontFamily: "Fira Sans Condensed"
    fontSize: "74px"
    fontWeight: 700
    letterSpacing: "0.02em"
  house-number:
    fontFamily: "Fira Sans Condensed"
    fontSize: "62px"
    fontWeight: 700
    letterSpacing: "0"
    fontFeature: "tnum"
  plate-name-latin:
    fontFamily: "Fira Sans Condensed"
    fontSize: "46px"
    fontWeight: 600
    letterSpacing: "0"
  street-latin:
    fontFamily: "Fira Sans Condensed"
    fontSize: "40px"
    fontWeight: 600
    letterSpacing: "0"
  house-date:
    fontFamily: "Fira Sans Condensed"
    fontSize: "32px"
    fontWeight: 600
    letterSpacing: "0.02em"
    fontFeature: "tnum"
  district:
    fontFamily: "Fira Sans Condensed"
    fontSize: "30px"
    fontWeight: 600
    letterSpacing: "0.08em"
rounded:
  plate: "14px"
  border: "7px"
spacing:
  canvas-pad: "4px"
  border-inset: "11px"
  border-stroke: "4px"
  plate-gap: "16px"
  district-rule: "3px"
components:
  name-plate:
    backgroundColor: "{colors.enamel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    width: "852px"
    height: "256px"
  street-plate:
    backgroundColor: "{colors.enamel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    width: "568px"
    height: "184px"
  house-plate:
    backgroundColor: "{colors.enamel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    typography: "{typography.house-number}"
    width: "268px"
    height: "184px"
---

# Design System: nklmilojevic

## Overview

**Creative North Star: "The Belgrade Street Plate"**

Each project is a street in Belgrade and its latest release is the house number on the wall. The whole visual system is one material, vitreous-enamel signage: a blue field, white letters, one white inset border, a soft cast shadow where the plate sits off the wall. Cyrillic reads first and Latin second, the way the city's own plates are set. Release tags and dates are real numbers, regenerated hourly by `scripts/render.py`. A number that cannot be fetched does not get typed in by hand.

The plates are the only designed objects on the page. Everything between them is GitHub's own Markdown: its body text, links, code blocks and theme colours, untouched. That is partly a sanitizer constraint (no CSS reaches the README) and partly the point: the profile sits quietly next to the GitHub UI, and the plates are what make it specific. Plates are SVG files embedded through `<picture>`, with light and dark variants that differ only in their cast shadow, and they scale to the column at `width="100%"`. They hold at phone width because their type is sized inside a fixed 860-unit viewBox.

The system rejects the usual profile furniture: emoji bullet lists, stats cards and skill-badge walls.

**Key Characteristics:**
- One material: enamel blue field, near-white ink, a single inset border.
- Cyrillic over Latin, in Fira Sans Condensed embedded as a woff2 subset.
- Live numbers only (release tag, release date), set in tabular figures.
- Exactly one moving thing: the house number rolls into place once on load.
- Outside the plates, only GitHub's own text and colours.

## Colors

Two colours do all the work, and the plates never vary them by theme. Only the shadow beneath a plate adapts to the page.

### Primary
- **Belgrade Enamel Blue** (`enamel`): the field of every plate. It is the only wayfinding colour on the page, and no other hue appears inside a plate.

### Neutral
- **Enamel White** (`ink`): every letter, the inset border, and the district rule. Measured contrast against Enamel Blue is about 8.5:1.
- **Wall Shadow Navy** (`enamel-shadow`): the cast shadow under plates in GitHub's light theme, at 0.28 opacity. In the dark theme the shadow switches to pure black at 0.55 opacity (see Elevation & Depth).

### Named Rules
**The One Enamel Rule.** Plates are Enamel Blue with Enamel White and nothing else. No accent colours, gradients, status colours or per-project tints, and none in dark mode either.

**The Borrowed Page Rule.** Outside the plates, colour belongs to GitHub. Do not try to tint the text, links or code blocks around the plates.

## Typography

**Display Font:** Fira Sans Condensed Bold (embedded as `'Plate Bold'`)
**Secondary Font:** Fira Sans Condensed SemiBold (embedded as `'Plate'`)
**Body Font:** GitHub's own Markdown text; not set by this system.

**Character:** A condensed humanist grotesk with full Cyrillic support, close in spirit to municipal signage lettering. Bold carries the primary-script name and the house number; SemiBold carries the Latin transliteration, the date and the district strip.

Sizes are SVG user units inside the 860-unit viewBox, so they scale with the column. Faces are subset to the glyphs each plate uses, keeping only the `kern`, `tnum` and `locl` features, then embedded as base64 woff2, because an SVG loaded through `<img>` cannot fetch fonts.

### Hierarchy
- **Name, Cyrillic** (700, 84 max, 0.01em): НИКОЛА МИЛОЈЕВИЋ on the name plate. It shrinks one unit at a time until it fits the inner width.
- **Street, Cyrillic** (700, 74, 0.02em): the project name in Cyrillic capitals on a street plate.
- **House number** (700, 62 max, tabular, centred): the live release tag. Shrinks to fit the house plate width minus 56.
- **Name, Latin** (600, 46 max): Nikola Milojević, directly under the Cyrillic.
- **Street, Latin** (600, 40): the project name in Latin title case.
- **House date** (600, 32 max, 0.02em, tabular, centred): the release date in Serbian order, `D. M. YYYY.`
- **District** (600, 30 max, 0.08em, uppercase): BEOGRAD · CTO @ MAILERLITE, under the rule on the name plate only.

### Named Rules
**The Two Scripts Rule.** Every name plate and street plate sets Cyrillic capitals above Latin title case. Latin never leads.

**The Tabular Number Rule.** House numbers and dates always use tabular figures (`font-variant-numeric: tabular-nums`) and share one centred axis on the house plate.

**The Embedded Face Rule.** Plate text is always Fira Sans Condensed embedded in the SVG. It never falls back to a system face.

## Layout

The page is a single column with full-width modules, stacked in reading order: name plate, one GitHub sentence, then for each project a plate row, its description, an install or download line, and a links row separated by ` · `. A `<br>` separates projects, and a final links row closes the page. There are no breakpoints. Every plate is an `<img width="100%">` inside a `<picture>`, so plates scale down as one unit on mobile while GitHub's text reflows around them.

All plates share an 860-unit-wide canvas with a 4-unit outer pad (`canvas-pad`). A project row pairs a street plate (568 wide) with a house plate (268 wide), separated by a 16-unit gap (`plate-gap`). The house plate always sits at the right. Street and house plates share one height (184). The name plate spans the full width at 256 tall, so the system has two module heights, not one. Text inside a plate is left-aligned on street and name plates and centred on house plates. Each plate is wrapped in a single `<a>` to its destination (site or repository), because an SVG loaded through `<img>` cannot carry links.

## Elevation & Depth

Plates sit slightly off the wall. Every plate casts one soft shadow, offset 3 units down with a 3-unit Gaussian blur. The shadow is the same shape as the plate. Nothing else on the page has depth.

### Shadow Vocabulary
- **Wall shadow, light theme** (`fill #0e2657, opacity 0.28, offset y +3, feGaussianBlur stdDeviation 3`): under every plate in `*-light.svg`.
- **Wall shadow, dark theme** (`fill #000000, opacity 0.55, offset y +3, feGaussianBlur stdDeviation 3`): under every plate in `*-dark.svg`. The light-theme navy disappears against GitHub's dark canvas, so the dark variant uses black.

### Named Rules
**The Soft Mount Rule.** The shadow is soft and short. It is never a hard offset block, never larger than the 3-unit drop, and never used on anything except a plate.

## Shapes

Two radii, nested. The plate has gently rounded corners (`rounded.plate`, 14). The inset border runs 11 units inside the plate edge (`border-inset`), drawn as a 4-unit Enamel White stroke (`border-stroke`) with tighter corners (`rounded.border`, 7). On the name plate a 3-unit Enamel White rule (`district-rule`) divides the names from the district strip and spans the text measure, inside the border.

**The Single Border Rule.** The inset border is the only ornament. Plates carry no icons, emblems, patterns or second frame. The district rule is part of the name plate's structure, used only to separate the district strip, and is not a decorative device for other plates.

## Components

### Name Plate
Full-width, one per page, and the first thing on it. It holds the Cyrillic name, the Latin name, a rule, and the district strip (city and role). It links to nikola.milojevic.me.
- **Size:** 852 × 256 inside the 860 × 268 canvas.
- **Content:** name in Cyrillic (display), name in Latin, `district-rule`, district text. Text starts at x 48 and the rule spans 48 to 812.

### Street Plate
One per featured project, on the left of a plate row. It carries only the project name: Cyrillic over Latin. It never carries a description, a tagline or any number.
- **Size:** 568 × 184.
- **Content:** Cyrillic capitals (baseline 98), Latin title case (baseline 146).

### House Plate
To the right of its street plate, at the same height. It holds the live release tag and the release date, nothing else.
- **Size:** 268 × 184.
- **Content:** tag (baseline 94) and date (baseline 142), both centred and tabular.
- **Motion (signature):** the tag sits behind a clip window (the plate width minus 36, 88 tall). On load, after a 0.3s delay, it accelerates up and out by 70 units (ease `cubic-bezier(.7,0,.84,0)`), reappears 70 units below, and settles into place (ease `cubic-bezier(.16,1,.3,1)`). The whole roll takes 1.1s and plays once. Under `prefers-reduced-motion: reduce` there is no animation. Nothing else on the page moves.

### Page text (GitHub-native)
Description paragraphs open with the project name in bold lowercase. The install line is a fenced `sh` code block, and a download link is set in bold. Links rows are inline links separated by ` · `. All of it uses GitHub's own styling.

## Do's and Don'ts

### Do:
- **Do** generate every plate from `scripts/render.py`, so release tags and dates come from the GitHub API on each hourly run.
- **Do** ship every plate in both `-light.svg` and `-dark.svg`, changing only the wall shadow between them.
- **Do** put a new featured project on a street plate (568 × 184) paired with a house plate (268 × 184), Cyrillic over Latin, at a 16-unit gap.
- **Do** keep alt text complete on every plate: the name, what the project is, and the latest release with its date.
- **Do** keep the house-number roll as the only motion, play it once, and disable it under reduced motion.

### Don't:
- **Don't** use emoji bullet lists, stats cards or skill-badge walls.
- **Don't** add a second colour, gradient or per-project tint to any plate.
- **Don't** add ornament beyond the single inset border: no icons, logos, glyph decorations or extra frames.
- **Don't** hand-type a number on a plate or in the README. If it can't be fetched, leave it out.
- **Don't** set plate text in a system or fallback face, or link a remote font.
- **Don't** animate anything other than the house number, and never loop that animation.
