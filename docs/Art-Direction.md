# My Journey: art direction

Phase 2 deliverable (`Build-Plan.md:77`), owner art-director. Written 2026-11-04, revised 2026-11-05 after the rules audit `docs/reviews/2026-11-04-rules-art-microcopy.md` (round 1: ART-1 to ART-12). Spec §20 was read in full, rulings **A to DDDD**; DDDD is the last ruling in `Functional-Spec.md` on 2026-11-05. It holds the circle system, colour, type and texture. It holds no flows or screen structure (ux, `Flows.md`), no final copy (copywriter) and no code.

**How to read this file**

- **[AD]** marks an art-direction choice. It covers colour, type, geometry and texture only (R-181). The docs give the look but not the value, so the Art Director picked it, for the user to review.
- Anything that says who sees something, on which screen, or when it appears is not [AD]. It either rests on the line cited beside it or is an open question, AD-n, in [§12](#12-open-questions).
- `PROVISIONAL: <ID>` is a default from `Decisions-Needed.md`, not a decision. Rule zero applies, and the code that draws it carries the same label (`CLAUDE.md:17–24`).
- **An AD-n is a question, never a default** (R-180). Where the build has to draw something before the user answers, the art director has proposed a default to the supervisor for `Decisions-Needed.md`. Those rows are B27 to B42 (added by the supervisor 2026-11-05), and this file names each one with its `PROVISIONAL: B<n>` label.
- Short names: **CL** `CLAUDE.md`, **Brief** `Master-Prompt.md`, **Concept** `My-Journey-Concept.md`, **Spec** `Functional-Spec.md`, **SI** `Screen-Inventory.md`, **DN** `Decisions-Needed.md`, **Proposal** `Phase-1-Proposal.md`, **Flows** `Flows.md`, **R-n** a check in `Rules-Rubric.md`. Spec §20 rulings are cited by letter, as SI does.

---

## 1. The register

**A family album from the 1970s to the 90s, deliberately not a modern photo book or photo app** (Brief:109; Concept:305; `art-director.md:22`).

What that means on screen:

| The album has | So the app has | Source |
|---|---|---|
| A cream page you can feel | A warm paper ground with grain, never white or grey | Concept:308 |
| A black-card page in older albums | The dark theme: chalk on black card, not "dark mode grey" | [AD], Concept:305 |
| Classic prints with a white border | A photo is a print on the page, with a border and square corners | Concept:308 |
| A thin plastic sheet over the photographs | One faint sheen over a print | Concept:309 |
| Handwritten names beside people | Names beside people in a ballpoint hand, never tags or handles | Concept:310, Spec:217 |
| Typed labels and soft 1970s headline type | A typewriter label for dates, a soft serif for headlines | [AD] |
| Dropping film off and waiting for prints | The sealed year is a shut film envelope | Concept:323 |

What it is not: no glass, no blur, no gradients as decoration, no pills, no card shadows that float, no feed layout, no sans-serif app chrome. "Nothing should ask the user to perform" (Brief:112; CL:127).

**No filter on any photograph.** No sepia, fade or film effect is applied to the image: a filter is the instant-app habit this product rejects, and it would make "the real year" look staged (Concept:312, 738). [AD]

The one thing laid over a photograph is the plastic-sheet sheen ([§9](#9-texture-and-prints)). It lightens the image a little where it falls, so the photo does not look exactly as taken.

---

## 2. The circle is one drawing

The logo, the profile frame, the rings and the navigation are one system (Brief:110; Concept:270, 683). One line runs through all of them: **a straight line bent round until its two ends cross.** That crossing is the visual proof of circling back, "a straight year bent into a ring" (Concept:708).

| Use | What is drawn |
|---|---|
| The mark (logo) | The line, closed, ends crossing |
| The frame | The mark at profile size, with the person's name inside |
| The rings | One line per ring, outward from the frame |
| The core on the map | The mark with the owner's name inside, no rings |
| Navigation | The circle holding a small plain sign ([§7](#7-navigation-marks)) |

**No profile picture, anywhere.** The name sits in the circle (Spec §20 YY, XXX; DN C7, decided 2026-10-31). Older lines saying the circle frames a picture are superseded (see [§12 B](#b-where-the-docs-disagree)).

**Where rings are drawn.** SI names rings on Profile (own) S-05 and Another user's profile S-16 (SI:167, SI:407). Elsewhere:

- The map shows "each person by name" (SI:230).
- Announcements carry no image (DN C7, decided; Flows:359).

No line says whether rings may be drawn on any other screen: **AD-13**, provisional default `PROVISIONAL: B37`.

---

## 3. Construction

Everything is drawn in a **320 × 320 box**, centre (160, 160), and scaled uniformly. Stroke widths scale with the box. [AD]

- Display it at `min(320px, available width)`, and no smaller than 240 px.
- The box is the same size for everyone. Only the rings inside it differ.

Angles are in degrees, **clockwise from 12 o'clock**. A point at radius R and angle φ is `x = 160 + R·sin φ`, `y = 160 − R·cos φ`.

### 3.1 The mark and the frame

The line is a true circle whose ends leave it and cross, like the tail of a loop of string. The crossing sits at upper left, never at 12 o'clock: a line that starts at 12 o'clock is a progress ring. [AD]

Exact paths. Stroke only, no fill, round caps and joins, colour `--mj-ink`:

| Use | Box | Stroke | Path |
|---|---|---|---|
| Frame (core line) | 320 | 2 | `M87.75 109.41 Q108.92 95.79 126.19 87.50 A80 80 0 1 1 94.47 114.11 Q105.63 98.55 122.73 80.06` |
| Map core | 360 | 1.5 | `M145.60 155.91 Q155.72 149.48 163.94 145.56 A38 38 0 1 1 148.87 158.20 Q154.16 150.79 162.25 141.94` |
| Mark, large | 48 | 3 | `M5.02 13.91 Q12.89 9.68 18.75 7.83 A17 17 0 1 1 8.99 16.02 Q11.83 10.57 17.36 3.55` |
| Mark, small | 24 | 1.5 to 2.25 | `M2.51 6.95 Q6.45 4.84 9.37 3.92 A8.5 8.5 0 1 1 4.49 8.01 Q5.91 5.29 8.68 1.78` |

Logo rules [AD]:

- Stroke by display size, using the 48 path: 96 px → 2.6; 48 px → 3; 32 px → 3.2; 24 px → 3.6; 16 px → 4.4. Nothing below 16 px.
- Clear space on all sides: one radius of the circle.
- One colour only, `--mj-ink` on the theme's page. No gradient, metal, gold, emboss or glow.
- Never a number, ring, dot or badge on or beside it, app icon included (SI:49; R-096).
- The product name is a working name, "not final" (Concept:720, 725), so the identity is the circle. A wordmark is the name set in `heading` type beside the mark. It is not drawn as artwork until the name is settled.

**The name in the circle** [AD]. Fraunces, `name` style, `--mj-ink`, centred on (160, 160). Break at word spaces, balanced, on up to two lines, each line fitting 127 wide.

- Too wide: step down to 22/25, then to 19/22, where three lines of up to 120 are allowed.
- All the fixture names fit two lines at 26/29.
- Never truncate. Never fill the core with an image or initials.
- A name that still does not fit: **AD-5**.

### 3.2 The rings

A ring is a record, like a tree ring: "a ring tells you the age, it does not claim the tree is better" (Concept:689). What adds a ring is `PROVISIONAL: B4`, switchable: one ring per finished reveal by default (Proposal:65), one per year with the app as the option, on the owner's own profile only (Spec §20 WW).

The geometry is the same under both settings. Only the number of rings, `n`, differs, and who sees which `n` is set out in [§3.6](#36-who-sees-what-on-a-circle).

The owner sees the same activity under both settings (R-141, R-187). Only what carries it differs (`PROVISIONAL: B28`):

- Under the default, the journey's ring carries the line from reveal finished.
- Under the per-year option, each finished journey's day marks go on the owner's ring for the year that holds that journey's reveal-finished date.
- That ring is drawn only later, so until it exists the journey's flat graph stays shown to the owner. This applies under this option only, as an exception to `PROVISIONAL: B31`.

- That ring's day 0 is still the journey's commit date, at the ring's own start angle `θ_k`, so the line is drawn exactly as under the default.
- A per-year ring that holds no finished journey is a plain ring.
- Two reveals finished in the same year (possible under `PROVISIONAL: B3`) both put their marks on that year's ring, each from its own day 0, merged by `max`. Whether that is wanted is part of AD-2.

Rings work like a tree's: each new ring is a little finer than the one before, so the circle keeps growing, by a smaller step each year, and never reaches an edge. [AD]

**Ring `k`, counted from the frame outward (1 is the first ring added):**

| Value | Formula | Note |
|---|---|---|
| Pitch `p_k` | `6 × 0.92^(k−1)` | Each ring is 92% the width of the one inside it |
| Radius `r_k` | `80 + p_1 + p_2 + … + p_k` | Depends on `k` only, never on `n`. A ring, once drawn, never moves |
| Stroke `w_k` | `0.22 × p_k` | The ink-to-paper share is the same 22% for every ring and every count |
| Start angle `θ_k` | `(k × 137.508) mod 360` | The joins scatter like grain in wood. No shared start, no gauge |
| Join overlap `σ` | `12°` | The line overruns itself by this much |
| Join flare `s_k` | `0.42 × p_k` | How far each end leaves the ring as it crosses |

The outer edge `80 + 75·(1 − 0.92ⁿ)` approaches radius 155 and never reaches it. Nothing is drawn there.

**To draw ring `k`.** A single open path, sampled every 0.5°, round caps and joins, colour `--mj-ink`, no fill, stroke `w_k`. For `φ` from 0 to 372°, at angle `θ_k + φ`, the radius is `r_k + flare(φ) + mark(φ)`:

- `flare(φ)` is `s_k·(1 − e(φ/12))` for φ below 12, and `s_k·e((φ − 360)/12)` for φ above 360. Otherwise it is 0. Here `e(x) = x²(3 − 2x)`.
- `mark(φ)` is 0 for a plain ring. For the owner's day marks, see [§3.3](#33-the-activity-line).

Worked values, for checking a build. These hold at every count `n`, because ring `k` does not depend on `n`:

| Ring k | p_k | w_k | s_k | Day-mark height | r_k (outer edge when n = k) | w_k at 240 px display |
|---|---|---|---|---|---|---|
| 1 | 6.00 | 1.32 | 2.52 | 1.68 | 86.00 | 0.99 |
| 5 | 4.30 | 0.95 | 1.81 | 1.20 | 105.57 | 0.71 |
| 9 | 3.08 | 0.68 | 1.29 | 0.86 | 119.59 | 0.51 |
| 10 | 2.83 | 0.62 | 1.19 | 0.79 | 122.42 | 0.47 |
| 17 | 1.58 | 0.35 | 0.66 | 0.44 | 136.83 | 0.26 |
| 25 | 0.81 | 0.18 | 0.34 | 0.23 | 145.67 | 0.13 |
| 40 | 0.23 | 0.05 | 0.10 | 0.07 | 152.33 | 0.04 |

**What holds at every value these formulas allow** (R-185):

- **Tone does not rise with count.** The ink share across the rings is 22% at every `n`.
- **Weight does not rise with count.** Each ring's stroke is fixed by its place, and is the same at every `n`.
- **Size is not a capacity.** The circle grows by a smaller step each time and never reaches an edge. No boundary, track or band is drawn or kept as a token. It does grow: "more years means a more elaborate circle" (Concept:687) and it "grows more sophisticated year by year" (Concept:700).
- **There are no steps or tiers.** One formula from the first ring to the last, with no boundary where the drawing changes.
- **Nothing is drawn beyond the newest ring**: no ghost ring, outline or track.
- **Every ring is the same ink.** Rings are never collapsed, summarised or scrolled, and there is no "+12".
- **The count is never printed or announced** (SI:176; R-166). See [§11](#11-checks-for-the-phase-6-art-review) for screen readers.

Where the fine outer rings stop being legible is **AD-17**.

**Questions that sit with the rings:**

- Labels on rings: none are drawn for a public viewer, which is a rule (Spec §20 CCC; SI:421). Whether the owner or the network may see a year or date on a ring is **AD-14**, provisional default `PROVISIONAL: B38`.
- Where a reveal finished years late puts its ring: **AD-9**, provisional default `PROVISIONAL: B34`.

### 3.3 The activity line

"The user's linear journey literally becomes a circle" (Concept:706). The line twists in when the reveal is finished (`PROVISIONAL: B5`; SI:178; Flows:361). It never appears during the sealed year (Spec:187; Concept:712; R-011).

What the line records beyond capture dates is open (SI OQ-7). **AD-8**, provisional default `PROVISIONAL: B33`. The drawing below takes capture dates (Proposal:50).

**The drawing: the ring itself, with a small soft rise on each day a photo was taken.** For the owner, day 0, the commit date, is at the ring's own start angle `θ_k`. A ring is one journey, not a calendar year. [AD]

For a journey of `N` days (365 or 366, UTC, `PROVISIONAL: B16`), a photo on day index `d` gives a mark centred at `φ_d = 360·(d + 0.5)/N`, with half-width `h = 360·4/N` (about 4 days):

```
height a_k = 0.28 × p_k
mark(φ)    = a_k · max over all d of cos²(π·Δ / (2h)),  where Δ = the angle from φ to φ_d, for Δ < h; else 0
```

Rules for the drawing [AD]:

- One day, one rise, the same height. A day with one photo and a day with forty look the same.
- Overlapping rises merge into a plateau and never stack (`max`, not a sum), so the line prints no count (R-144; `PROVISIONAL: B8`).
- Same weight and same colour. No intensity scale, no heat colours, no green.
- No colour, weight or pattern is assigned to a type.

**What the line still shows.** Density follows how many days had photos.

- An Explorer's 48 photos merge into an almost unbroken raised line. A Contemplator's 12 are separate bumps, and a Contemplator has at most 13 such days.
- So the line shows, roughly, the journey's type and how full the year was.
- A clean ring beside a busy one marks a quiet year.
- Fullness can be read as a score, which is what a contribution graph is read for.

Under B5's default only the owner sees this, after unlock. This file does not settle it: **AD-11**, raised next to AD-1.

### 3.4 The flat graph

Between unlock and reveal finished, the owner sees the year as a straight line (Spec:187; SI:184; `PROVISIONAL: B5`). It is the same line, not yet bent. [AD] for the drawing:

- Length 300, stroke 1.25, `--mj-ink`, round caps, in a 320 × 24 box.
- A photo on day `d` rises at `x = 10 + 300·(d + 0.5)/N`, height 3, half-width `300·4/N`, with the same `cos²` and `max`.
- No axis, grid, month labels, totals or tooltips (R-144).
- It never touches, points to or sits inside the circle. No arrow, no ghost ring: anything like that asks the owner to finish (Spec:242; Flows:514).

**The commit-date anchor** (R-179). Placing a rise at `d`, counted from the commit date, ties the drawing to that date.

- The owner and the network read journey dates (Spec §20 T), so for them it gives nothing new.
- A public viewer may not read journey dates (Spec §20 T; R-152). From one dated photo they could recover the commit date.
- Whether a public viewer gets a flat graph at all under B5's option, and if so what it may be anchored to: **AD-12**, provisional default `PROVISIONAL: B36`.

Whether the flat graph stays once the line has twisted in: **AD-6**, provisional default `PROVISIONAL: B31`. Under B4's per-year option it stays until the year's ring is drawn (`PROVISIONAL: B28`, an exception to B31).

### 3.5 How the line twists in

At reveal finished, the ring is there the next time the circle is drawn, with no celebration (SI:185; Flows:523).

Whether the line visibly bends is **AD-3**, provisional default `PROVISIONAL: B29`. The geometry is ready if the user wants it [AD]:

- Keep the line's length constant at `2π·r_k`.
- For bend `t` from 0 to 1, draw it as an arc of angle `360°·t` and radius `r_k / t`, ending on the ring.
- Timing is `--mj-motion-bend`.

### 3.6 Who sees what on a circle

What each viewer sees comes from the docs. Where they are silent, the cell names the provisional default in `Decisions-Needed.md` the build follows, with its AD-n question beside it (R-180).

| Viewer | B4 setting | Rings on the profile | B5 setting | Day marks in rings | Flat graph |
|---|---|---|---|---|---|
| Owner, S-05 | per finished reveal (default) | One per finished reveal (Proposal:65; SI:173) | either | Yes, after reveal finished (SI:178, 185) | From unlock (SI:184) until reveal finished, then not shown (`PROVISIONAL: B31`; AD-6) |
| Owner, S-05 | per year with the app | One per year with the app, own profile only (Spec §20 WW; SI:174). When a ring appears: `PROVISIONAL: B28` (AD-2) | either | Yes, after reveal finished: each finished journey's marks on the ring for the year holding its reveal-finished date (`PROVISIONAL: B28`; AD-2). Rings holding no finished journey are plain | From unlock, and after reveal finished until the year's ring is drawn (`PROVISIONAL: B28`, an exception to B31; AD-2, AD-6) |
| Network, S-16 | **either** | One per finished reveal (Spec §20 WW; SI:412). Never per year, which would give the join date (Spec §20 TT) | owner only (default) | None: plain rings (`PROVISIONAL: B27`; AD-1) | None (SI:412) |
| Network, S-16 | either | As above | built from photos the viewer can see | None: plain rings (`PROVISIONAL: B27`; AD-1) | From photos this viewer can read, one-day resolution (SI:412; Spec §20 GG). Anchored to the commit date, which the network reads (Spec §20 T). From unlock until reveal finished, then not shown (`PROVISIONAL: B31`; AD-6) |
| Public, S-16 | **either** | One per finished reveal, from the count alone, no date (Spec §20 CCC, WW; SI:412) | owner only (default) | None: a public viewer's rings come from the count alone (Spec §20 CCC) | None (SI:412) |
| Public, S-16 | either | As above | built from photos the viewer can see | None (Spec §20 CCC) | None (`PROVISIONAL: B36`; AD-12) |

**Drawing facts that follow from the geometry, not decisions.**

- A ring without day marks depends on `k` alone. So any two plain circles with the same number of rings are drawn identically, apart from the name.
- `θ_k` depends on `k` alone, so no plain ring points at a date (R-179).

Being on someone's map, or in their inner ring, changes nothing in the drawing. Close friends get no extra line, tint or mark (Spec §20 H; Concept:864). A viewer's own position on someone's map is never drawn (Spec:164, 235; CL:74).

---

## 4. The states of the circle

States are named by ring count and journey state only, never by a name for a stage (R-185; Concept:693).

| State | Drawn | Source |
|---|---|---|
| **0 rings** (never committed, or no finished reveal, under B4's default) | The frame and the name, centred in the same 320 box. Nothing else: no ghost ring, start line or placeholder | SI:182; Concept:694; `PROVISIONAL: B4`, `C9` |
| **1 or more rings** | Rings `1…n` as [§3.2](#32-the-rings) gives them. Every count is drawn by the same formula | Concept:687, 689 |
| **A journey sealed** | The circle is unchanged. The current year adds nothing to it: no ring, arc, segment, tick or dash | SI:183; R-012; R-143 |
| **Unlocked, reveal not finished** | The circle is unchanged. The flat graph, to the owner | SI:184; `PROVISIONAL: B4`, `B5` |
| **Reveal finished** | Under B4's default, ring `n + 1` is added outside, in order of finishing; its day marks to the owner. Under the option, the day marks go on the ring for that year; until that ring is drawn, the flat graph stays shown to the owner | SI:185; `PROVISIONAL: B4`, `B5`, `B28`, `B34` |
| **Reveal never finished** | No ring for that journey, under B4's default. Nothing marks the absence | SI:173; Proposal:65; `PROVISIONAL: B4` |

Under B4's per-year option the owner's ring count follows years with the app (SI:174). When such a ring appears, which ring carries a journey's day marks, and the flat graph staying shown until that ring is drawn, all follow `PROVISIONAL: B28` (AD-2).

An empty circle states what is there and offers no button or suggestion (`PROVISIONAL: C9`; R-095). Its words are the copywriter's (SI:190).

---

## 5. The sealed year

"The hardest screen in the product and the most important: it must feel intentional, not broken" (Brief:130). Underneath, the data returns nothing, so any empty-list or loading pattern would look like a fault (SI:131; Flows:286, 308).

### The drawing: one shut envelope

A kraft film envelope, shut with the circle. You dropped your film off, and it is not back yet (Concept:323). On The sealed year S-03 it is the picture of element 1, "That the owner has a journey underway" (SI:117). The drawing itself is [AD].

Drawn in a 280 × 196 box, displayed at `min(280px, available width)`, with `--mj-texture-grain` over the paper:

| Part | Value |
|---|---|
| Body | Rectangle 278.5 × 194.5 at (0.75, 0.75), radius 2, fill `--mj-kraft`, stroke 1.5 `--mj-ink` |
| Flap | Triangle (1, 1), (140, 112), (279, 1), fill `--mj-kraft-shade`, stroke 1.25 `--mj-ink`, round joins |
| Seal | Circle at (140, 112), radius 28, fill `--mj-print`, stroke 1.25 `--mj-ink` |
| Mark on the seal | The 48-box mark, translated (116, 88), stroke 2.4, `--mj-ink` |

The drawing contains no words, numbers or dates.

### The rules that make it leak nothing

1. **It is one fixed image, byte for byte identical** for every user, on every date of the sealed year, before and after every capture, for a journey holding no photos or many (SI:133; R-010, R-012; Flows:309). Only the theme changes it.
2. **It never varies with how many photos were taken.** No thickness, bulge, weight, stack, peeking corner or second envelope.
3. **It never varies with time.** No wear, ageing, fading, thread being unwound, wax softening or anything that advances.
4. **It never varies with type.** Explorer, Wanderer and Contemplator get the same envelope.
5. **No thumbnails or stand-ins for them.** No blurred, frosted, pixelated or silhouetted images, empty frames, grey rectangles or skeleton blocks (Spec:75; CL:73).
6. **No count-revealing marks.** No ticks, tally, film-frame numbers, sprocket holes that fill, or strip of frames (Spec:75; SI:137).
7. **No padlock.** A padlock says "paywall" or "you are shut out". An envelope says "this was done on purpose". [AD]
8. **No loading signs.** No spinner, shimmer or fade-in that looks as if something else is coming (SI:131).
9. **No motion at all.** The flap does not lift, the seal does not pulse (R-012; SI:137).

Type styles for the words on S-03, which belong to the copywriter and ux:

- Type name and the two plain dates (SI:118–120; `PROVISIONAL: B19`; Spec §20 EEEE): `label` style, `--mj-ink-soft`.
- The sealed line: `display-m`, `--mj-ink` `[copy: copywriter]`.
- An open highlight (Spec §20 S; SI:123): `body` style. No icon, ring, bar or timer, and the envelope does not change (SI:138).

The ways to capture and to start a highlight look the same whether or not a frame or a highlight is left (SI:121–122; R-138; `PROVISIONAL: B7`). That is why **there is no disabled colour token in this file**.

### How others see a sealed journey

SI's S-16 `sealed` row holds "That a journey exists, and nothing else" (SI:419; Spec §20 I; Flows:324). SI does not say whether that fact is drawn or written, or where it sits. Shown beside a person's name and only while a journey is under way, any drawing works as a status flag. This file draws nothing for it: **AD-15**, provisional default `PROVISIONAL: B39`.

---

## 6. Layers: the map

The owner's own map, and only ever theirs (Spec:164; CL:74). "The Apple Watch app menu, not a list" (Spec:159) is taken as an arrangement only: concentric, not a list. Its bubbles that swell toward the centre are not taken, because size by closeness is rank (Spec:185). [AD]

**Keeping two ring systems apart.** Identity rings are close, inked lines with a name in the middle. Layer rings are wide, thin lines with people's names on them. The map's core is the plain map-core mark, with no identity rings. [AD]

Drawn in a 360 × 360 box, centre (180, 180) [AD]:

| Part | Value |
|---|---|
| Core | The map core path, stroke 1.5, `--mj-ink`, with the owner's name in `core-name` style |
| Layer rings | True circles at radius 80 (tight), 115 (middle), 150 (outer), stroke 1, `--mj-line`. Equal steps, no join and no crossing |
| A person | Their name, `hand` style, `--mj-ballpoint`, centred on their ring, with a 4 px `--mj-page` halo so the ring breaks behind it |
| Angle of a person | With `m` people on the whole map, sorted by member id: `t = (j + 0.5)/m × 280`. Angle is `−70 + t` for t below 140, else `110 + (t − 140)`. This keeps names clear of 3 and 9 o'clock |

Ids are random (Spec §20 JJ; `Phase-1-Amendments.md:25`), so position around a ring carries nothing. The placement is tested to the fixtures' maps, which hold at most four names.

**The rules for the drawing** (Spec:185; R-102; Concept:691):

- Every layer ring has the same weight and colour.
- Every name has the same size, weight and colour on every ring.
- No tint, glow or gradient from the centre, and no fading with distance.
- No person's picture or initials (Spec §20 XXX).
- Current rings only: no counts, past positions, trails, arrows, or "moved in" and "moved out" marks (`PROVISIONAL: C8`; SI:237).
- Nobody moves on screen. When a reveal is finished, the map is drawn as it now stands. An animated move outward is visible demotion (Concept:422; SI:237; `PROVISIONAL: C8`).
- An empty map is the core alone (SI:234; Flows:460).

**Behaviour this file does not settle:**

- Whether a layer ring with nobody on it is drawn, on a map that has people: **AD-16**, provisional default `PROVISIONAL: B40`. Flows:455 says "three rings". A ring that vanishes when its last person drifts would show drift.
- Words naming the rings, and a map busier than the fixtures': **AD-7**, provisional default `PROVISIONAL: B32`.
- No drawing on any other screen shows where a viewer sits on someone else's map, and no other person's map is ever drawn (Spec:164, 235; SI:240).

---

## 7. Navigation marks

"The circle should run through the vocabulary, the visual language and the navigation" (Concept:270; Brief:110). A mark is given **only for a way that a Screen-Inventory "Leads to" row names** (R-186).

Each mark is the same circle holding a small plain sign. On a 24 grid, centre (12, 12), stroke only, round caps and joins. Geometry is [AD].

| Way to | Named by | Geometry |
|---|---|---|
| Profile (own) S-05 | S-03 (SI:111); the map's core (SI:170) | The small mark path from [§3.1](#31-the-mark-and-the-frame) |
| Walking a path S-06 (own) | S-05 (SI:170) | Circle r 9.5; curve `M6.5 14.5 C9 8.5, 15 15.5, 17.5 9.5` |
| Journey overview S-15 | S-05 (SI:170) | Circle r 9.5; `M8 8H14.5V15H8Z`; `M10 15V17H16.5V10H14.5` |
| Layers S-07 | S-05 (SI:170), S-03 (SI:111) | Circles r 9.5, 5.75, 2 |
| Feed S-08 | S-05 (SI:170), S-03 (SI:111) | Circle r 9.5; lines (7.5, 9)–(16.5, 9), (7.5, 12)–(16.5, 12), (7.5, 15)–(13, 15). Text lines, because the feed carries no images (CL:72) |
| Positivity Feed S-09 | S-05 (SI:170), S-03 (SI:111) | Circle r 9.5; line (6, 15.5)–(18, 15.5); half circle r 3.5 on that line, centre (12, 15.5) |
| Capture S-02 | **S-03 only** (SI:111, element 5) | Circles r 9.5, 5. Shown the same whether or not a frame is left (SI:121; R-138; `PROVISIONAL: B7`) |
| Start a highlight S-13 | **S-03 only** (SI:111, element 6) | Circle r 9.5; circle r 3; rays (12, 5.5)–(12, 7), (12, 17)–(12, 18.5), (5.5, 12)–(7, 12), (17, 12)–(18.5, 12). Shown the same whether or not a highlight is left or open (SI:122) |
| The sealed year S-03 | S-05, present while a journey is sealed (SI:170; `PROVISIONAL: B42`) | Circle r 9.5; rectangle (6.5, 8.5)–(17.5, 15.5); flap lines (6.5, 8.5)–(12, 12.5)–(17.5, 8.5) |
| Commit S-01 | S-05, present in `no-journey` (SI:170; `PROVISIONAL: B42`) | Circle r 9.5; line (7, 12)–(17, 12) |
| Reveal S-04 | S-05, present while a reveal is open (SI:151, SI:170; `PROVISIONAL: B41`) | **No mark of its own.** A plain way in `label` style, styled like every other way, with no emphasis. C1's "Your Journey is ready" line is a second way in (`PROVISIONAL: C1`). That line shows once, on the first open after unlock (Spec §20 FFFF), so the plain way is what reaches an unfinished reveal afterwards |

How every mark is drawn [AD]:

- At rest: stroke 1.5, `--mj-ink-soft`. Current screen: stroke 2.25, `--mj-ink`. No fill, no colour change.
- Always beside a word, in `label` style `[copy: copywriter]`.
- Touch target at least 44 × 44 (`--mj-target`). The mark displays at 24 to 32.
- All marks have the same weight. None is louder than another: Commit is not in rust as a way in, Capture is not larger. A louder way is a prompt (Flows:509, 525; SI:50).
- A mark has two appearances, at rest and current, and no more. It never takes a dot, number, badge, tint, pulse or changed shape because of content (SI:49–50; R-096). There is no slot left for one.
- Marks are static (CL:76).

**Behaviour this file does not settle:**

- **Ways that appear and disappear by journey state.** SI:170 makes three of S-05's ways conditional:
  - the sealed year, while a journey is sealed;
  - Commit, in `no-journey`;
  - Reveal, while a reveal is open.

  The build follows `PROVISIONAL: B41` for Reveal and `PROVISIONAL: B42` for Commit and the sealed year. Each such way is drawn like every other way, with no emphasis, no "new" marker and nothing that announces the change (SI:77; R-095, R-096).

  R-186 says no way appears, disappears or changes because of content. So whether a way appearing by state is itself a marker stays **AD-18**, for the user. It is sharpest at unlock: the sealed-year way goes and the Commit and Reveal ways come on the same day as "Your Journey is ready".
- **Where the ways sit, and whether a ring can be pressed:** **AD-10**. Rings have no press or hover state (`PROVISIONAL: B35`). Where the ways sit is for ux.

---

### 7.x The time-limit circle (Spec §20 XXXX, 2026-11-10)

*Added by the supervisor for the art-director's review.* Where the app states a window's length (the note's 15 minutes on S-12, the highlight's "up to 24 hours" and its 3-hour grace on S-13), it shows a small fixed circle beside the words: a clock face of the window's own unit with one arc from twelve o'clock, a quarter of an hour face for 15 minutes, an eighth of a day face for 3 hours, a full day face for 24 hours (`PROVISIONAL: B77`). Same stroke and tones as the navigation marks. **It never moves, fills, empties or shows time left**, and it looks identical at every moment of the window (Spec §20 S; R-138, R-140). It is a statement of the rule, not a timer.

## 8. Tokens

Copy-ready. All values are [AD], resting on the register in [§1](#1-the-register). **No green, red, gold, silver or bronze exists in this palette**, so no colour can mean "success", "failure" or "achievement". Rust means a weighty act, and ballpoint means a hand or a link. Neither ever appears on a ring.

```css
:root {
  color-scheme: light;

  /* Paper */
  --mj-page:        #F2E9D8;  /* cream album page */
  --mj-print:       #FBF7EC;  /* print border, paper label */

  /* Ink */
  --mj-ink:         #2A211B;  /* text, the mark, identity rings */
  --mj-ink-soft:    #574A3E;  /* secondary text, marks at rest */
  --mj-ink-faint:   #675849;  /* least important text; still passes AA */
  --mj-line:        #857461;  /* layer rings, input edges */
  --mj-rule:        #CFC2A9;  /* decoration only; never the only signal */

  /* Accents */
  --mj-ballpoint:   #23397A;  /* names beside people, links, focus */
  --mj-rust:        #8E3F1C;  /* the Commit press and the Finish press only */
  --mj-on-rust:     #FBF7EC;

  /* Envelope */
  --mj-kraft:       #B4935F;
  --mj-kraft-shade: #A5854F;

  /* Texture */
  --mj-texture-grain: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .2 0 0 0 0 .15 0 0 0 0 .1 0 0 0 .09 0'/></filter><rect width='180' height='180' filter='url(%23g)'/></svg>");
  --mj-film-sheen: linear-gradient(115deg, rgb(255 255 255 / .10) 0%, rgb(255 255 255 / 0) 38%, rgb(255 255 255 / .05) 62%, rgb(255 255 255 / 0) 100%);
  --mj-print-shadow: 0 1px 2px rgb(42 33 27 / .25);

  /* Type families */
  --mj-font-display: "Fraunces", Georgia, serif;
  --mj-font-text:    "Source Serif 4", Georgia, serif;
  --mj-font-label:   "Courier Prime", "Courier New", monospace;
  --mj-font-hand:    "Caveat", "Bradley Hand", cursive;

  /* Spacing: 4 px base */
  --mj-space-1: 4px;   --mj-space-2: 8px;   --mj-space-3: 12px;
  --mj-space-4: 16px;  --mj-space-5: 24px;  --mj-space-6: 32px;
  --mj-space-7: 48px;  --mj-space-8: 64px;  --mj-space-9: 96px;
  --mj-measure: 34rem; /* longest line of reading text */
  --mj-target:  44px;  /* least touch target */

  /* Radii: paper has square corners. Circles belong to the mark */
  --mj-radius-print:  0;
  --mj-radius-paper:  2px;  /* envelope, label, press */

  /* Prints */
  --mj-print-border: 10px;

  /* Focus */
  --mj-focus: 2px solid var(--mj-ballpoint);
  --mj-focus-offset: 2px;

  /* Motion: none of it loops, and all of it stops under prefers-reduced-motion */
  --mj-motion-page: 140ms ease-out;     /* opacity only, between screens */
  --mj-motion-bend: 1600ms ease-in-out; /* only if AD-3 is answered yes */

  /* Circle constants, in the 320 box */
  --mj-circle-box: 320;
  --mj-core-r: 80;
  --mj-core-stroke: 2;
  --mj-ring-first-pitch: 6;
  --mj-ring-pitch-ratio: .92;
  --mj-ring-ink-share: .22;
  --mj-ring-angle-step: 137.508;
  --mj-ring-overlap-deg: 12;
  --mj-ring-flare-ratio: .42;
  --mj-mark-height-ratio: .28;
  --mj-mark-halfwidth-days: 4;
}

/* Black-card album page. How this theme is chosen: AD-4 */
[data-mj-theme="dark"] {
  color-scheme: dark;

  --mj-page:        #1B1714;
  --mj-print:       #2A241E;

  --mj-ink:         #F0E7D7;
  --mj-ink-soft:    #CDBFAB;
  --mj-ink-faint:   #AE9F8B;
  --mj-line:        #8F8171;
  --mj-rule:        #40372E;

  --mj-ballpoint:   #AFC1EE;
  --mj-rust:        #E5935F;
  --mj-on-rust:     #1B1714;

  --mj-kraft:       #7A6240;
  --mj-kraft-shade: #6B5536;

  --mj-texture-grain: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .94 0 0 0 0 .91 0 0 0 0 .84 0 0 0 .09 0'/></filter><rect width='180' height='180' filter='url(%23g)'/></svg>");
  --mj-film-sheen: linear-gradient(115deg, rgb(255 255 255 / .06) 0%, rgb(255 255 255 / 0) 38%, rgb(255 255 255 / .03) 62%, rgb(255 255 255 / 0) 100%);
  --mj-print-shadow: 0 1px 2px rgb(0 0 0 / .5);
}
```

**Deliberately absent:** disabled, success, warning, error and "new" colours; progress, meter and band tokens; a badge token; a gradient for rings; a pill radius. A refusal is plain text in `--mj-ink` (`PROVISIONAL: B7`). A control that is offered is never greyed (R-138).

**Where rust goes** [AD]:

- Only on the press that commits (S-01) and the press that finishes a reveal (S-21), "the weightiest act after Commit" (Spec:45; SI:520; Flows:355).
- Not on any way into them, and not on "Your Journey is ready" (`PROVISIONAL: C1`). A rust line on the profile would be a prompt (Spec:242; SI:50).
- On S-01 the three types look the same, and none is preselected (Spec:46). A chosen type gains a 2 px `--mj-ink` edge, with no colour and no difficulty scale.

### Contrast

Calculated on 2026-11-04 with the WCAG 2.1 relative-luminance formula, by script.

- **Flat** is against the plain token.
- **With grain** is against the page mixed with the grain colour at its peak, 9%, the worst case. Prints carry no grain, so that column is empty for them.
- Text needs 4.5:1. Graphics needed to understand the screen need 3:1.

**Text, light theme**

| Text | On | Flat | With grain |
|---|---|---|---|
| `ink` #2A211B | `page` #F2E9D8 | 13.08 | 11.07 |
| `ink-soft` #574A3E | `page` | 7.10 | 6.01 |
| `ink-faint` #675849 | `page` | 5.68 | 4.81 |
| `ballpoint` #23397A | `page` | 8.99 | 7.61 |
| `rust` #8E3F1C | `page` | 6.05 | 5.12 |
| `ink` | `print` #FBF7EC | 14.73 | |
| `ink-soft` | `print` | 7.99 | |
| `ink-faint` | `print` | 6.39 | |
| `ballpoint` | `print` | 10.12 | |
| `rust` | `print` | 6.82 | |
| `on-rust` #FBF7EC | `rust` | 6.82 | |

**Text, dark theme**

| Text | On | Flat | With grain |
|---|---|---|---|
| `ink` #F0E7D7 | `page` #1B1714 | 14.51 | 11.60 |
| `ink-soft` #CDBFAB | `page` | 9.87 | 7.89 |
| `ink-faint` #AE9F8B | `page` | 6.90 | 5.51 |
| `ballpoint` #AFC1EE | `page` | 9.91 | 7.92 |
| `rust` #E5935F | `page` | 7.35 | 5.88 |
| `ink` | `print` #2A241E | 12.50 | |
| `ink-soft` | `print` | 8.50 | |
| `ink-faint` | `print` | 5.94 | |
| `ballpoint` | `print` | 8.53 | |
| `rust` | `print` | 6.33 | |
| `on-rust` #1B1714 | `rust` | 7.35 | |

All text pairs pass AA at any size.

**Graphics** (light / dark, flat; with grain in brackets where the ground carries it)

| Graphic | Against | Light | Dark |
|---|---|---|---|
| Identity rings, mark: `ink` | `page` | 13.08 (11.07) | 14.51 (11.60) |
| Marks at rest: `ink-soft` | `page` | 7.10 (6.01) | 9.87 (7.89) |
| Layer rings: `line` | `page` | 3.73 (3.16) | 4.70 (3.76) |
| Input edge: `line` | `print` | 4.20 | 4.05 |
| Focus: `ballpoint` | `page` | 8.99 (7.61) | 9.91 (7.92) |
| Envelope lines: `ink` | `kraft` | 5.47 | 4.69 |
| Envelope lines: `ink` | `kraft-shade` | 4.56 | 5.75 |
| Seal mark: `ink` | `print` | 14.73 | 12.50 |

`--mj-rule` is 1.46 (light) and 1.53 (dark) against the page. It is decoration only and must never carry meaning.

**Fine rings fall short.** Each ring line is full `ink`, but outer rings are thin.

- When a stroke is thinner than a device pixel, the line blurs toward the band's 22% ink tone.
- That tone measures **1.54 (light) and 1.88 (dark)** against the page: below 3:1.
- This is not accepted here. It is **AD-17**, with the numbers.

### Type

Four families, all under the **SIL Open Font License 1.1**, free to use and self-host. Licence files checked on 2026-11-04 in `github.com/google/fonts`:

| Family | Role | Source | Axes or styles |
|---|---|---|---|
| **Fraunces** | Headlines, the name in the circle. A soft "old style" serif in the manner of 1970s display type | `ofl/fraunces` | `opsz` 9–144, `wght` 100–900, `SOFT` 0–100, `WONK` 0–1 |
| **Source Serif 4** | Reading text: reflections, overviews, announcements | `ofl/sourceserif4` | `opsz` 8–60, `wght` 200–900 |
| **Courier Prime** | Typed labels: dates, the type's name | `ofl/courierprime` | 400, 700, with italics |
| **Caveat** | Names beside people, in a ballpoint hand | `ofl/caveat` | `wght` 400–700 |

**Self-host them.** Do not load the fonts from a third-party CDN: that sends each visit to someone else, against "no usage analytics or telemetry of any kind" (`PROVISIONAL: B15`).

Scale: 1.25 from 20 up. 14 px is the floor. [AD]

| Style | Family | Size / line (px) | rem | Weight | Settings |
|---|---|---|---|---|---|
| `display-l` | Fraunces | 39 / 44 | 2.4375 | 400 | `"SOFT" 100, "WONK" 1` |
| `display-m` | Fraunces | 31 / 36 | 1.9375 | 400 | `"SOFT" 100, "WONK" 1` |
| `title` | Fraunces | 25 / 30 | 1.5625 | 500 | `"SOFT" 100, "WONK" 1` |
| `name` | Fraunces | 26 / 29, then 22 / 25, 19 / 22 | 1.625 | 500 | `"SOFT" 100, "WONK" 1` |
| `heading` | Fraunces | 20 / 26 | 1.25 | 500 | `"SOFT" 100, "WONK" 0` |
| `core-name` | Fraunces | 15 / 18 | 0.9375 | 500 | `"SOFT" 100, "WONK" 0` |
| `body` | Source Serif 4 | 17 / 26 | 1.0625 | 400 | `opsz` auto |
| `small` | Source Serif 4 | 15 / 22 | 0.9375 | 400 | `opsz` auto |
| `label` | Courier Prime | 14 / 20 | 0.875 | 400 | |
| `hand` | Caveat | 20 / 24 | 1.25 | 600 | Colour `--mj-ballpoint`. Never below 19 px |

Rules:

- **A hand font is for names beside people, and nothing else** (Concept:310; Spec:217). No sentences in it.
- **Reflections and overviews are typed, so they are set in `body`** (Concept:803).
- **The handwritten note is a photograph of a real page, shown as a print.** Never reset it in a font (Concept:311; Spec:16).
- Dates are plain dates in `label`, never relative (Spec §20 EEEE).
- No "@", no handles (Concept:310).
- Sentence case. No all-caps labels: they belong to apps, not albums. [AD]

**Specimens.** The six approved lines (CL:131–136), word for word. Styles only: where each goes is the copywriter's call.

| Style | Specimen |
|---|---|
| `display-l` | It's not about attention. It's about intention. |
| `display-m` | You've come further than you think. |
| `title` | Strict at capture. Generous at reflect. |
| `label` | No retakes. That moment is gone. |
| `body` | This app takes time, like many other good things. |
| `heading` | We want you here less, not more. |

---

## 9. Texture and prints

**Grain.** `--mj-texture-grain` as a repeating background on `--mj-page`, and over the envelope. It is static, fixed to the page and the same at every moment. It never appears over a photograph or a print. [AD]

**A print** (Concept:308) [AD]:

- Border `--mj-print-border` in `--mj-print`, corners `--mj-radius-print`, shadow `--mj-print-shadow`.
- No hover zoom, no filter, no caption over the image.
- A photo's quality is not graded or hidden: a dark, blurry or badly framed photo gets the same print (Spec:56).

**The plastic sheet.** `--mj-film-sheen` is laid over the photograph (Concept:309; Spec:216).

- It is white at up to 10% (light theme) and 6% (dark theme), in a diagonal band.
- **It lightens every pixel it covers**, most at the corner where the band starts. So the photograph does not look exactly as taken.
- No pixels are changed in the stored image.

Whether a sheen over the photo is wanted at all is for the user to review, as [AD].

**A handwritten note** gets the same print treatment at A4 proportion, 1 : 1.414.

**Frequency language.** "432" as "a texture in the brand world" (Concept:271) is not used anywhere in the visual system. It would need waves or vibrating motion, and its health claim is not established (Concept:273). If the user wants it, it is a copy question. [AD]

**Motion in general.**

- Only `--mj-motion-page`, and `--mj-motion-bend` if AD-3 is answered yes.
- Nothing loops, breathes, pulses or draws the eye while the screen is idle.
- No pull-to-refresh art (SI:51). Nothing is timed to bring anyone back (CL:70, 76).

---

## 10. How this must never read

Each "do" holds for every value the formulas allow (R-185).

| Rule | Do | Do not |
|---|---|---|
| **A ring is a record** (CL:71; Spec:185; R-102) | Draw each ring as a whole closed line, added outside the last, and never moved after | A ring that fills, an arc that sweeps, a percentage, a stroke-dash that grows |
| **No gap to complete** (R-012, R-143) | Nothing drawn beyond the newest ring; no band, track or edge kept as a token | A faint next ring, an outer track, a dashed outline, an open segment for this year |
| **No tiers** (Concept:693; R-185) | One formula for every ring count; states named only by count and journey state | A name for a range of counts, a style that changes at a count, gold at year 5, a new look at a milestone |
| **Tone and weight do not rise with count** (R-185) | The same 22% ink share at every count; each ring's stroke fixed by its place, not by the count | Heavier or darker circles for more rings, strokes that thicken as rings are added |
| **No "higher is better" in colour** (Concept:691) | Ink only | A warm-to-hot ramp, metal tones, saturation by age or by activity |
| **Size is not capacity** (Concept:687, 694) | Growth by a smaller step each year, toward no drawn edge, in the same box for everyone | A drawn boundary, track or band for the rings to reach (the formula's limit at radius 155 is never drawn and has no token), equal steps to a full band, circles lined up to compare |
| **The activity line prints no count** (R-144; `PROVISIONAL: B8`) | One same-height rise per day with a photo | Peaks by count, heat colours, a grid, totals. A fuller line can still read as better: AD-11 |
| **Difficulty is not drawn** (CL:89–93) | Types shown by name in plain text | A colour, icon, star or stripe per type, on a ring or anywhere near a person |
| **Layers are not rank** (Spec:185; Concept:691) | Same line and same name style on all three rings | Larger names near the core, a glow on the inner ring, "close friends" colour, fading with distance |
| **Own layer is never shown** (CL:74; Spec:164) | The same profile drawing for every viewer of the same kind | A "you" dot, a highlighted arc, a position marker, or a line joining viewer and owner |
| **No drift on show** (`PROVISIONAL: C8`; Concept:422) | Draw the map as it now stands | A name sliding outward, an arrow, a ghost at the old place, a "moved" tint |
| **Nothing signals looks or doing well** (Brief:113; Spec:29) | A name in a circle | A picture, an avatar, initials on colour, verified ticks, status words |
| **No profile picture** (Spec §20 XXX) | The name in the core | A photo in the frame, even a landscape, even the person's own journey photo |
| **No markers** (SI:49; R-096) | A mark looks the same every day | A dot, number, "new", a bold unread line, a tinted way when something is ready, an app-icon badge |
| **No countdown** (Spec §20 EEEE; R-013) | A plain date in `label` | Rings ticking round, a shrinking arc, "in 64 days", an hourglass, a moon phase, a calendar filling |
| **No pull back** (CL:69–70, 76) | Still screens that can be left | A pulse, shimmer, breathing circle, anniversary treatment, seasonal art or celebration |
| **No reward** (SI:185; Flows:514, 523) | At finish, the ring is there | Confetti, a glow, a sound, a vibration, "you earned", a burst on the seal |
| **Sealed shows nothing** (CL:73; Spec:75) | One identical shut envelope on S-03 | A thicker envelope, blurred thumbnails, empty frames, a film strip, a tally, a dimmed grid |
| **Sealed reads as meant** (Brief:130; SI:131) | A complete page, on purpose | A spinner, skeleton rows, grey placeholders, "nothing here yet", a padlock |
| **Nothing public is anchored to a hidden date** (R-179) | Plain rings from `k` alone | Any position, length or scale shown to a public viewer computed from a commit or unlock date |
| **Not a modern photo app** (Brief:109) | Paper, ink, prints, typed labels | White cards, blur, pills, sans-serif tab bars, photo filters, full-bleed feeds |

---

## 11. Checks for the Phase 6 art review

Each can be seen or run:

1. Steady Lantern's circle, at 2026-02-01, 2026-07-01 and 2026-12-31: identical (R-012, R-143).
2. The sealed screen before and after a capture, and for a journey holding none or many photos: identical, apart from the open-highlight line (SI:133; R-010).
3. Ring `k` is drawn the same at every count `n`. With the worked values in [§3.2](#32-the-rings), the band's ink share is 22% at n = 1, 5, 9, 10, 17, 25, 40 (R-185).
4. Two profiles with the same number of finished reveals, viewed by a public viewer: identical rings, apart from the name (Spec §20 CCC; R-166).
5. Under B4's per-year option, S-16 for any viewer: one ring per finished reveal (Spec §20 WW; R-161).
6. Under B5's option, as a public viewer: no drawing whose positions come from a commit date (R-179).
7. Search the app for these: `<progress`, `role="progressbar"`, `aria-valuenow`, `stroke-dashoffset`, or an arc angle computed from a date (R-012). None may be near the circle.
8. **Screen readers.** The name is real text. Rings and the flat graph are `aria-hidden`. No `aria-label`, `title` or alt text gives a number of rings or photos, because a count read aloud is still a count (R-166, R-144).
9. No element in the theme uses a colour outside [§8](#8-tokens), except inside a photograph.
10. Viewing a profile as someone on that person's tight ring, and as someone on no ring, both network: identical apart from what visibility rules give (Spec §20 H; Spec:164).
11. Every navigation mark matches a "Leads to" row in SI (R-186).
12. Code and fixtures contain no state name keyed to ring count, such as `young`, `established` or `veteran` (R-185).

---

## 12. Open questions

Nothing below is picked. Where the build has to draw something before the user answers, the art director has proposed a provisional default to the supervisor. Each now names its row in `Decisions-Needed.md` (B27 to B42, added 2026-11-05). The build follows that row, never this file (R-180).

### A. Unspecified, and implies a behaviour

| ID | Question | Why it is a behaviour | Default |
|---|---|---|---|
| **AD-1** | **Does anyone but the owner see the day marks in a ring?** Spec:186 and Concept:706 say the line twists into the circle and name no viewer. DN B5 limits "the activity graph", and SI:178 and SI:412 treat the graph apart from the line. Under B5's option, should a network viewer's rings carry marks from photos they can read? Read with AD-11 first | The marks show which days photos were taken. Spec §20 CCC settles public viewers only | Provisional default `PROVISIONAL: B27` (`Decisions-Needed.md`) |
| **AD-2** | **Under B4's "per year with the app": on which date does a year's ring appear, and which ring holds which journey's line?** Years with the app and journeys need not line up: gaps, a first year without a journey, a never-finished reveal. A ring must never appear or change inside a sealed year (R-012, R-143; Flows:514). B28 puts each finished journey's marks on the ring for the year holding its reveal-finished date, so the line survives under both B4 settings (R-187). Still open: the ring timing, which B28 states as a proposed rule; whether two reveals finished in the same year should share one ring, as B28 makes them; and how the activity is carried between finish and that year's ring. B28 keeps the flat graph shown until the ring exists. The other reading is to draw the marks on the newest existing ring until the year's own ring arrives | When a ring appears, and what it means | Provisional default `PROVISIONAL: B28` (`Decisions-Needed.md`) |
| **AD-3** | **Does the line visibly bend, once, when the owner finishes a reveal?** "Twisted and turned" (Concept:706) suggests it. "Never arrives as an achievement" (SI:176) and "no celebration" (Flows:523) warn against it. Flows:362 takes the app to S-05 straight after finish | Motion at the weightiest moment can read as a reward, and playing it on a later open would be a marker | Provisional default `PROVISIONAL: B29` (`Decisions-Needed.md`) |
| **AD-4** | **How is the dark theme chosen?** Following the device, a setting, or not at all in the prototype | A setting is a new control, and a prototype switch would join T-02 | Provisional default `PROVISIONAL: B30` (`Decisions-Needed.md`) |
| **AD-5** | **Is there a limit on a name's length?** Proposal:61 and SI S-11 say set once, and give no length. A name must fit in the core | A limit is a rule at sign-up | None needed in the prototype: all fixture names fit, and sign-up is not built (`PROVISIONAL: C11`) |
| **AD-6** | **After the line twists in, does the flat graph stay?** SI:184 lists it only for `unlock-day` and `reveal-open`, and SI:185 lists only the ring and line. Spec:187 does not say it goes away | Whether a drawing stays visible | Provisional default `PROVISIONAL: B31` (`Decisions-Needed.md`) |
| **AD-7** | **Does the map name its rings, and how does a map busier than the fixtures' look?** Flows:455 and SI:230 name no labels. Spec:159 rules out a list | Words on rings may read as grades. Scrolling or zooming a map is a screen behaviour, for ux | Labels: provisional default `PROVISIONAL: B32`. Busy map: none needed in the prototype (at most four names) |
| **AD-8** | **What does the line record besides capture dates?** Already open as SI OQ-7 (Concept:704; Proposal:50; Flows:516) | Recording more is a data decision | Provisional default `PROVISIONAL: B33` (`Decisions-Needed.md`) |
| **AD-9** | **Under `PROVISIONAL: B3`, a reveal finished years late: where does its ring go?** Outermost by order of finishing, or in its journey's time order? | It decides what a ring's place means | Provisional default `PROVISIONAL: B34` (`Decisions-Needed.md`) |
| **AD-10** | **Where do the ways sit, and can a ring be pressed?** SI:170 and SI:250 leave the navigation to Phase 2, and Flows:509 lists the ways but not where they are. SI:167 asks for a way into journeys. For a public viewer a ring can lead to no journey in particular (Spec §20 CCC) | Screen structure, for ux, and a press | Ring press: provisional default `PROVISIONAL: B35`. Arrangement: for ux |
| **AD-11** | **The line's density shows the type and how full a year was** ([§3.3](#33-the-activity-line)). An Explorer's ring is almost continuous; a Contemplator's has at most 13 separate rises; an empty year is a clean ring. Is that acceptable? If not, the user could ask for a coarser encoding, such as one mark per month with a photo. That still shows fullness, but not the type | Fullness can read as a score, and it would reach the network if AD-1 is answered yes | None needed beyond B5's default: only the owner sees it |
| **AD-12** | **Under B5's option, does a public viewer get a flat graph at all? If so, what is it anchored to?** SI:412 allows a graph "no finer than one day" and names no anchor. Anchored to the commit date, one dated photo gives the commit date away (R-152, R-179). A graph that disappears at finish would also tell a public viewer the reveal state, which Spec §20 ZZ does not list | Who sees a drawing, and when it disappears | Provisional default `PROVISIONAL: B36` (`Decisions-Needed.md`) |
| **AD-13** | **Are rings drawn anywhere other than S-05 and S-16?** SI names them only there. No line forbids them elsewhere | On which screens a drawing appears | Provisional default `PROVISIONAL: B37` (`Decisions-Needed.md`) |
| **AD-14** | **May the owner or the network see a year or date on a ring?** Banned for a public viewer (Spec §20 CCC). The owner and network read journey dates (Spec §20 T), but no line asks for labels | What a viewer can learn from the circle | Provisional default `PROVISIONAL: B38` (`Decisions-Needed.md`) |
| **AD-15** | **How is "a journey exists" shown to others on S-16 and S-06: words, a drawing, or both, and where?** SI:419 holds the fact and nothing else. A drawing beside a name, present only while a journey is under way, works as a status flag | What is shown and where | Provisional default `PROVISIONAL: B39` (`Decisions-Needed.md`) |
| **AD-16** | **On a map with people, is a layer ring with nobody on it drawn?** Flows:455 says "three rings". Drawing only occupied rings makes a ring vanish when its last person drifts out, which shows drift (`PROVISIONAL: C8`). Drawing it empty may read as a slot to fill | What appears and disappears on the map | Provisional default `PROVISIONAL: B40` (`Decisions-Needed.md`) |
| **AD-17** | **Fine outer rings fall below a device pixel.** At 240 px on a 1× screen, strokes go under 0.5 px from ring 10; at 320 px, from ring 13. On a 2× screen, from about ring 18 and 21. There the lines blur into the band's tone, 1.54 (light) and 1.88 (dark) against the page, below 3:1. The owner's day marks sit on those rings: from about ring 17 the rise is under 0.45 units, so that year's activity is no longer readable. Fixtures reach about 11 rings with the clock's +5 years. Options: accept for the prototype; a larger first pitch or slower ratio, which makes the circle grow further; or a smallest display size above 240 | It decides what an older user can still read on their own profile | None needed: the build draws the formula. For the user to review |
| **AD-18** | **Is a way that appears by journey state a marker?** S-05 leads to Reveal while a reveal is open, to Commit in `no-journey`, and to the sealed year while sealed (SI:151, SI:170). R-186 says no way appears, disappears or changes because of content, and SI:77 bans "a banner or marker that Commit is open again". On the day of unlock the sealed-year way goes and the Commit and Reveal ways come | When a way appears | Reveal: `PROVISIONAL: B41`. Commit and the sealed year: `PROVISIONAL: B42`. Whether appearing by state is a marker: for the user |
| **AD-19** | **The newest ring is always the finest** ([§3.2](#32-the-rings)). On the owner's own circle the most recent year is the faintest line, which could read as fading. A geometry within R-185 that avoids it: put the newest ring next to the frame and push older rings out one place at each finish. The tone stays 22% at every count, but every ring then moves at each finish, which contradicts `PROVISIONAL: B34` ("added outermost") and the tree reading (Concept:689). For the user to look at in the preview at +5 years | It changes where a ring sits and whether rings move | None needed: the build draws the formula and B34 **Decided 2026-11-09 (Spec §20 IIII): the newest ring stays the thinnest and is drawn the brightest. The tone is still to be specified here.** |

### B. Where the docs disagree

Both lines cited. This file follows §20 and Concept §29 where they speak, or the labelled default. IDs in brackets are `Flows.md`'s.

| Conflict | Lines | Followed here |
|---|---|---|
| The circle frames a picture, against no picture and the name in the circle (Flows DC-9) | Spec:13, Spec:184, Concept:700, CL:111, against Spec §20 YY, XXX and DN C7 | Spec §20 XXX. The older lines still need correcting (L-002) |
| What adds a ring (Flows DC-1) | Spec:185, Concept:687, CL:111, against Proposal:65 and Spec §20 WW | `PROVISIONAL: B4`, switchable |
| When the line twists in: "at the end of the journey", against reveal finished (Flows DC-12) | Spec:186, Concept:706, against DN B5, Proposal:65 | `PROVISIONAL: B5` |
| Counters banned during the sealed year, against banned at any time (Flows DC-10) | Spec:233, against CL:69, Spec:242, DN B8 | `PROVISIONAL: B8`: no count, meter or bar in any drawing at any time |
| Close friends "get everything", against nothing extra | Concept:807, Concept:383 (both carry a "superseded" note), against Spec §20 H and Concept:864 | Spec §20 H: no visual difference at all. This is L-002's known trap |
| The sealed journey's "existence in detail", against others may know it exists | Spec:246, against Spec §20 I and Concept:868 | Spec §20 I |

---

## 13. Sources for this file

Read in full or by section, 2026-11-04 to 2026-11-05:

- `CLAUDE.md`; `Status.md`; `Master-Prompt.md` "Voice and look".
- `My-Journey-Concept.md` §9, §11, §20, §21, §23, §29 and the layers section.
- `Functional-Spec.md` §12, §14, §17, §18, §19, and §20 rulings A to DDDD.
- `Screen-Inventory.md`: general rules, every "Leads to" row, S-03, S-05, S-07, S-16, S-21.
- `Decisions-Needed.md`.
- `Rules-Rubric.md` R-011, R-012, R-013, R-102, R-143, R-144, R-166, R-179, R-180, R-181, R-185, R-186.
- `Flows.md`: Flows 4, 5, 7 and 8, and its open questions.
- The audit `docs/reviews/2026-11-04-rules-art-microcopy.md`.

Not used: `Overview.md` (L-001), and `prototype/index.html`, whose colours are not a source.
