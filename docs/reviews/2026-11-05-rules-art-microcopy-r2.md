# Rules audit: Art-Direction.md and Microcopy.md, round 2

Date: 2026-11-05. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-186 before this audit and R-187 after it.

**Targets**

- `docs/Art-Direction.md` (AD), 725 lines, after revision round 1 and the supervisor's label edits.
- `docs/Microcopy.md` (MC), 231 lines, after revision round 1.
- The supervisor's new rows B27 to B41 in `docs/Decisions-Needed.md` (DN:62–76).
- All are untracked or uncommitted, so changes were found by reading each r1 line again.

Previous audit: `docs/reviews/2026-11-04-rules-art-microcopy.md` (r1, FAIL: ART-1 to ART-12, COPY-1 to COPY-9).

`docs/Flows.md` was read for context only. Its last audit is `2026-11-05-rules-flows-r3.md`.

**Verdicts.** `Art-Direction.md`: **FAIL**, with 5 violations. `Microcopy.md`: **FAIL**, with 3 violations.

All 21 r1 findings are fixed. The revision is careful. The geometry now does what §10 says, and every open behaviour has a DN row or is stated as needing none.

What remains is mostly new, from three sources:

- the new defaults B27 to B41 read together with older ones;
- two rewritten copy lines;
- one ID family `Microcopy.md` did not rename when `Flows.md` did.

**For a user previewing the design**, two of the eight are noticeable in the prototype:

- **ART-R2-1:** Long Way Round's open reveal can lose its only way in.
- **ART-R2-3:** flipping B4 makes the activity line disappear, and the user would blame the wrong switch.

None of the eight lets a sealed year leak, shows a layer, or ranks a user.

---

## Checks run

```
$ graphify query "navigation way appears Commit marker"
(used only to locate sections; nothing below rests on it)

# R-131: six lines, exact string (grep -cF)
It's not about attention. It's about intention.    | AD:1 MC:2
You've come further than you think.                | AD:1 MC:2
Strict at capture. Generous at reflect.            | AD:1 MC:2
No retakes. That moment is gone.                   | AD:1 MC:2
This app takes time, like many other good things.  | AD:1 MC:3
We want you here less, not more.                   | AD:1 MC:4
  (MC: in M-28 on S-10, which is not built, and in M-10 alternative 2.
   No recommended string shows it in the prototype. MQ-5 raises this.)

# R-185: ring-count state names
$ grep -nEiw 'young|established|veteran' docs/Art-Direction.md docs/Microcopy.md
AD:666  check 12, naming the banned words        -> fine
MC:38, :134, :142  prose saying "young" is dropped -> fine
No state name in either file.

# Leftover placeholder
$ grep -nE 'pending|see report' docs/Art-Direction.md docs/Microcopy.md
AD:364  "AD-18, provisional default pending for Reveal: see report"  -> ART-R2-4

# R-013 on MC
$ grep -nEi 'days? (left|to go|until|remaining)|unlocks? in|countdown|time left|next month|\bsoon\b|from today|\btoday\b|tomorrow|next year' docs/Microcopy.md
:119  M-19 "Next year there is room for another"  -> the marker's word, about a reflection slot, not the unlock date; fine
the rest: prose and source notes ("no today", MQ-9 history)

# R-095, R-102, R-124 on MC
$ grep -nEi "don't forget|remember to|you haven't|come back|we miss|still have|waiting for you|ending soon|last chance|streak|earned?|congrat|well done|level|rank|badge|score" docs/Microcopy.md
:133  M-21 "Closeness here is earned by crossing journeys"  -> Flows:455's subject; fine
:142  source note ("no level name")

# R-183 grep aid on MC
$ grep -nEi 'missing|\bsafe\b|kept|waiting|nothing has gone wrong' docs/Microcopy.md
:100  M-12 "This is the year as you kept it."   -> COPY-R2-2
:162  M-29 "it is kept"                         -> the name, true
:77   source note

# R-150 step 1, table IDs with no label in the file
AD: B1 B10 B11 B12 B13 B14 B17 B18 B2 B20 B21 B22 B23 B24 B25 B26 B6 B9 C10 C12 C13 C14 C15 C16 C3 C4 C5 C6 C7
    Read: AD touches none of these, apart from B6 (§20 S, decided) and C7 (decided).
    B7, B8, C1, C2, C8, C9 and B27 to B41 are now labelled.
MC: B10 B15 B16 B17 B18 B2 B20 … B41 B5 B8 C12 …
    Read: B10 is a false hit (written bare in the label cell). B2 appears only in MQ-8's question.
    B39 assigns copy to the copywriter, and MC has no entry for it (N-4).

# R-177 scan: strip the hyphen and match against DN IDs
AD: (no output)
MC: C-1->C1 C-2->C2 C-3->C3 C-5->C5 C-6->C6 C-7->C7 C-8->C8 C-9->C9   -> COPY-R2-3
$ grep -oE '\bD?C-[0-9]+\b' docs/Flows.md | sort -u
DC-1 … DC-14   (Flows renamed C-n to DC-n; MC:5 and MC:211–216 still cite C-n)

# AD §3.2 and §8, recomputed by script
22% band tone against page: 1.54 light, 1.88 dark   (AD:538 agrees)
 k  p_k   w_k   r_k     ink share  a_k   w at 240 px  w at 320 px
 1  6.00  1.32   86.00  0.22       1.68  0.99         1.32
 5  4.30  0.95  105.57  0.22       1.20  0.71         0.95
10  2.83  0.62  122.42  0.22       0.79  0.47         0.62
13  2.21  0.49  129.63  0.22       0.62  0.36         0.49
17  1.58  0.35  136.83  0.22       0.44  0.26         0.35
18  1.45  0.32  138.28  0.22       0.41  0.24         0.32
21  1.13  0.25  141.98  0.22       0.32  0.19         0.25
40  0.23  0.05  152.33  0.22       0.07  0.04         0.05
Every value in AD:127–135 and every threshold in AD-17 (AD:694) checks out.
```

---

## Each r1 finding, against the current files

| r1 | Now at | Result |
|---|---|---|
| ART-1: public flat graph gives the commit date and the reveal state | AD:194–198, :221–223, :646, :660, :689; DN B36 | **Fixed.** Public viewers get no flat graph under either B5 setting (B36). The anchor problem is stated, and §10 and §11 check it. The network keeps a commit-anchored graph, which is fine because it reads dates (§20 T). SI:412 and SI:420 still describe a public graph: see N-5 |
| ART-2: §20 WW dropped | AD:101, :103, :216–223, :659 | **Fixed.** §3.6 has a B4 column. Network and public see one ring per finished reveal under either setting |
| ART-3: AD-n carried buildable defaults | AD:10, :672, :678–695; DN B27–B41 | **Fixed in substance.** Each AD-n names a DN row or says none is needed. Leftovers are in ART-R2-4. `Commit and the sealed year follow SI's rows until the user rules` is ART-R2-2 |
| ART-4: `[AD]` settled behaviours | AD:7–8, :53–58, :151, :294, :327 | **Fixed** for all four r1 cases (B37, B38, B39, B40). One case missed in r1 is ART-R2-5 |
| ART-5: "cannot read as a status badge" | AD:294 | **Fixed.** The claim is gone, and AD:294 now says any drawing works as a status flag. See N-4 on B39 |
| ART-6: bigger, heavier, tier names, capacity | AD:105–145, :236–247, :629–632, :657 | **Fixed.** Ring `k` no longer depends on `n` (checked to ring 40). Ink share is 22% at every count. Tier names are gone. The band token is gone. Growth is stated and sourced (Concept:687, 700). See N-2 and N-3 |
| ART-7: "the type never shows" | AD:174–183, :633, :688 | **Fixed.** Stated plainly and raised as AD-11 |
| ART-8: invented Capture way | AD:335–365 | **Fixed** for Capture (S-03 only), and marks are added for S-06, S-15, S-13, S-01. Conditional ways remain: ART-R2-1, ART-R2-2 |
| ART-9: contrast "accepted" | AD:535–539, :694 | **Fixed.** Not accepted. AD-17 gives the numbers, and they are correct |
| ART-10: bare DN citations | AD:51, :56 (C7, decided), :240–249, :470, :574, :637, :641 | **Fixed** |
| ART-11: "no colour change" | AD:35, :601–607 | **Fixed** |
| ART-12: no §20 range | AD:3 | **Fixed** (A to DDDD) |
| COPY-1: "12 months from today" | MC:47, :51, :52, :230 | **Fixed.** "Runs for 12 months", labelled C2. Flows:179 matches |
| COPY-2: "One press, one photo" beside "No photo was taken" | MC:60–61 | **Fixed.** The approved line alone, and both strings are true together. "That moment is gone" beside a refusal also discourages a second press, which R-160 wants |
| COPY-3: "nothing is missing" | MC:86 | **Fixed.** The new line is about the screen only. The new M-12 has the same fault: COPY-R2-2 |
| COPY-4: "Your map is earned" | MC:133 | **Fixed.** The subject is closeness, as in Flows:455 |
| COPY-5: M-17 past its marker | MC:105, :229 | **Fixed.** The lock only. MQ-8 raises what goes out at finish, with both switches named |
| COPY-6: S-05 line placed without a source | MC:142, :226 | **Fixed.** Removed. MQ-5 states plainly that R-130's app half now has nothing to read in the prototype |
| COPY-7: "young" | MC:38, :134, :142 | **Fixed.** See N-6 on M-23's new claim |
| COPY-8: labels and citations | MC:46, :102, :106 | **Fixed** |
| COPY-9: no §20 range | MC:3 | **Fixed** |

---

## Findings: Art-Direction.md, and its defaults in Decisions-Needed.md

### ART-R2-1. B41 makes "Your Journey is ready" the only way into a reveal, which forces C18 and can strand Long Way Round's reveal
- **Checks:** Rule zero (`CL:21`), R-134, R-150 (4), R-168. C18 has no default (`DN:180`).
- **Where:** `Decisions-Needed.md:76` (B41); `Art-Direction.md:351`, `:364`, `:695`.
- **What is wrong.**
  - B41: "No navigation mark for Reveal S-04. The way in is C1's 'Your Journey is ready' line only."
  - S-04 is reached "through 'Your Journey is ready' … ; Profile (own) S-05 at any later time" (SI:151). Flows:154 gives Long Way Round at baseline "the way into the open reveal" and, separately, the ready line "if it still shows: how long it stays is C18, which is open".
  - Under B41, if C18 is answered "once, on the next open", an unfinished reveal has no way in after that open. If it is answered "every open", the line becomes the standing nudge SI OQ-42 warns about (R-095).
  - So B41 forces C18's answer, in one direction or the other. C18 has no default, and a default may not settle another question by dependency.
- **How serious for a user previewing.** **High for playability.** Long Way Round is the fixture built to show an unfinished reveal (#4 unlocked a year ago). If the prototype shows the ready line once, the user cannot reach that reveal at all. If it shows the line on every open, they see a reminder on every visit, which is exactly what they will be judging. Either way the preview misrepresents the product.
- **Fix belongs to:** the supervisor (B41's wording) and the user (C18). Not the art director, who raised the conditional way correctly.

### ART-R2-2. The Commit and sealed-year ways still appear and disappear by journey state, "until the user rules"
- **Checks:** R-186, R-096, R-180, R-135. `Screen-Inventory.md:77` bans "A banner or marker that Commit is open again".
- **Where:** `Art-Direction.md:349`, `:350`, `:364`, `:695`.
- **What is wrong.**
  - The Commit mark shows "in `no-journey`" (AD:350). That state begins at unlock, so the mark appears on the same day as "Your Journey is ready", and the sealed-year mark (AD:349) disappears at the same moment.
  - A way that appears on the day Commit opens again is the marker SI:77 and Flows:176 ban. R-186 bans a way that appears or disappears because of content.
  - SI:170, which makes the ways conditional, conflicts with SI:77 inside the same document. AD:364 raises the conflict as AD-18, then follows one side, SI:170, "until the user rules". No DN row covers it.
  - That is a buildable interim state with no ID (R-180), on one side of a raised conflict (R-135). B41 settles only Reveal.
- **How serious for a user previewing.** **Medium.** Jump Steady Lantern to 2027-01-01 and the navigation changes on that day: one way gone and a "Commit" way new, beside the ready line. It reads as "something is new, start your next year", which is the re-engagement cue the product bans. It is small, but it lands on the one day the product most needs to stay quiet.
- **Fix belongs to:** the supervisor, with a DN row for Commit and the sealed year, as was done for Reveal, or the user.

### ART-R2-3. Under B4's option the owner's activity line disappears, so flipping B4 also changes B5's behaviour
- **Check:** R-141, which says flipping each switch alone changes "only the behaviour named by that ID". Also Spec:186 and DN B5 (the line twists into the circle at reveal finished).
- **Where:** `Decisions-Needed.md:63` (B28), `:66` (B31); `Art-Direction.md:218–219`, `:247`.
- **What is wrong.**
  - B28: "Under B4's 'per year with the app', the owner's per-year rings are drawn plain, with no day marks."
  - B31: the flat graph "shows from unlock until the reveal is finished, then is not shown."
  - Together, under B4's option, once a reveal is finished the owner sees that year's activity nowhere: no graph and no marks. Under B4's default they see it in the ring.
  - So the B4 switch changes what B5 shows. R-141 requires flipping one switch to change only its own behaviour.
  - AD:219 also says the opposite of B28. It gives day marks "As above, for rings that carry a journey: AD-2", while B28 says no ring carries any.
  - B28 calls itself "Proposed rule, not a reading of the docs". DN:16 admits a default only where it is "the way the docs lean or … the strictest reading of the banned list". Dropping the line is not required by any banned-list item. It removes a feature Spec:186 states.
- **How serious for a user previewing.** **Medium.** Comparing the two ring settings is the very thing B4's switch exists for. The user would see the activity line vanish, conclude "per year" rings cost them their activity record, and decide on a false premise. The real trade-off is only where the line goes, which AD-2 asked.

### ART-R2-4. Label carriage left over from the supervisor's pass
- **Checks:** R-180, R-150.
- **Where and what:**
  - `Art-Direction.md:364`: "AD-18, provisional default pending for Reveal: see report". The phrase differs from the one the supervisor replaced, so it was missed. AD:695 has B41.
  - `:218`, `:219`, `:221`, `:223`, `:247`: the §3.6 table, the file's who-sees-what table and the one a builder will read, names "AD-6", "AD-2", "AD-1" and "AD-12" in its cells. B31, B28, B27 and B36 exist for exactly those cells. The label sits one hop away, in §12 or §3.4.
- **How serious for a user previewing.** **Low.** Every default named is strict, so nothing wrong would be built. The risk is that a builder takes "AD-1" in a table cell to mean "open" and stops, or picks.

### ART-R2-5. `[AD]` places the envelope on a screen
- **Check:** R-181. Also `Screen-Inventory.md:113` ("Exactly this list").
- **Where:** `Art-Direction.md:259`: "This drawing is for The sealed year S-03. [AD]".
- **What is wrong.** Saying which screen a drawing appears on is not colour, type, geometry or texture. S-03's list holds nine elements, and none of them is an image. The envelope can fairly be read as the picture of element 1, "That the owner has a journey underway" (SI:117). It should cite that line, not `[AD]`. r1 missed this. It was there in round 1 as "This is the one image on the screen. [AD]".
- **How serious for a user previewing.** **None visible.** The image is identical at all times and leaks nothing (§5 still holds). This is a paperwork fault.

---

## Findings: Microcopy.md

### COPY-R2-1. "begun by this press" shows beside "No highlight was started."
- **Checks:** R-182, R-183.
- **Where:** `Microcopy.md:67`, `:69`.
- **What is wrong.** M-05, on S-13 in every state: "A highlight is a window, begun by this press, in which the monthly limit does not apply." M-07, on the same screen after a refusal: "No highlight was started." Both sit there together, and they contradict each other about the same press. This is the kind COPY-2 was. MC:67 says the line "describes what a press begins, so it holds with no highlight left and while one is open". In those states the press begins nothing.
- **Where it came from.** The wording is the Flows marker's (Flows:244, "a window, begun by this press"), so `Flows.md` carries it too.
- **How serious for a user previewing.** **Low to medium.** Open Steady Lantern's S-13 while a highlight is open and press: the screen says this press begins a window and also that none was started. It will read as a bug. The same holds for Explorer and Wanderer once their allowance is used.

### COPY-R2-2. M-12's "This is the year as you kept it" is untrue after a lost press
- **Check:** R-183 (a line is true in every state, "the bug paths (lost press, lost page)" named).
- **Where:** `Microcopy.md:100`.
- **What is wrong.** After a lost press (Spec §20 DDD) the owner pressed and believed the photo was kept. The app stored nothing, by ruling, and showed nothing different. "The year as you kept it" then tells them the screen holds what they kept, and it does not. MC:100 claims the line is "true for … one whose press or page was lost". The first-round "Here is who you were" made no such claim.
- **How serious for a user previewing.** **Low.** The lost press is a planted fault, not something a demo walk-through meets. It is the same false reassurance r1 removed from M-10, now moved to S-04. "This is the year." (or the approved line alone) avoids it.

### COPY-R2-3. Flows' old C-n IDs are still cited, and they read as Decisions C1 to C9
- **Check:** R-177.
- **Where:** `Microcopy.md:5` ("*Flows* = `Flows.md` (FQ-n, C-n)"), `:211–216`.
- **What is wrong.** `Flows.md` renamed its C-1 to C-13 as DC-1 to DC-14 (r1 V11 against Flows), and AD:703–706 cite DC-n. MC still cites C-1, C-2, C-3, C-5 to C-9, which no longer exist in Flows. Stripped of the hyphen, they are DN C1 to C9.
  - `:215` "C-8 | M-25 follows B12" reads as DN C8, the map drift default.
  - `:213` "C-5 | 'Publish' is not used" reads as DN C5, nothing required before finish.
- **How serious for a user previewing.** **Low.** It shows on no screen, but anyone following MC's cross-references lands on the wrong rule, or on nothing.

---

## Notes (not violations)

- **N-1. M-25 "You were here." (R-139, R-147, G-12).** Reported again, as the rubric requires every audit to do under B12's "shown". A reader can count their appearances and estimate their ring. The user has not ruled.
- **N-2. The newest ring is always the thinnest** (AD:105, :111, :113). The geometry follows tree rings. It also means a user's most recent year is always the faintest line on their own circle. That could read as fading, which "no higher is better" does not cover. For the user to look at in the preview at +5 years. No rule is broken.
- **N-3. AD:632's "Do not" lists "A boundary the rings approach".** The formula does approach radius 155 (AD:118), undrawn and with no token. The "Do" column, "toward no drawn edge", is what holds. Wording only.
- **N-4. B39 shows "a journey exists" as words only.** Words beside a name are as much a status flag as a picture. That comes from §20 I itself, and nothing banned follows. But B39 says "Copy and placement to come (copywriter, ux)", and `Microcopy.md` has neither the string nor an MQ for it (MQ-3 lists the unmarked strings and omits it). Until someone writes it, S-16's `sealed` row (SI:419 "Holds: That a journey exists") has nothing to show.
- **N-5. B36 narrows B5's option, but SI still describes the public graph.** `Screen-Inventory.md:412` and `:420` still describe a graph for every non-owner under B5's option, public included. B36 is right (R-179), but SI now states the other side. That is SI's carriage under R-150, outside this audit's targets, and is for the supervisor.
- **N-6. M-23 "Your circle records time, not how you are doing."** MC:142 says this is true under both B4 settings. Under the default a ring is a finished reveal, which is something the owner does, not time passing. Long Way Round has had more years than rings. In the one state that shows the line (never committed, MQ-7) it holds. If MQ-7 widens where it shows, R-183 will need reading again.
- **N-7. AD-17 is reachable in the preview.** Fixture circles reach about 11 rings with the clock's +5 years. At 240 px on a 1× screen, strokes are under 0.5 px from ring 10 (verified). A previewing user who jumps +5 years on Steady Lantern will see the outer rings blur. It is raised for them correctly.

## Tested and clean this round

- **R-179.** No position shown to a public viewer derives from a date.
- **R-185.** Ring `k` is independent of `n`. The 22% share holds at every count. No state names.
- **R-182 for M-03 and M-04.**
- **Envelope §5 rules 1–9.** Unchanged and clean.
- **The layer map.** Unchanged and clean. B40 keeps all three rings, so no ring vanishes on drift.
- **B27, B29, B30, B32 to B35, B37, B38, B40.** Each is strict and breaks no banned-list item.
- **M-02, M-10, M-17, M-19, M-21, M-22.** No reminder, countdown, rank or sealed-content claim.
- **The six approved lines.** Word for word in both files.

---

## Rubric changes made in this run

- **R-187 (new, area 14):** provisional defaults hold when read together. Flipping one switch with every other default in force changes only its own behaviour. No default forces the answer to a question that has none, or removes the only way to a screen a "Reached from" row requires. Found as ART-R2-1 and ART-R2-3.
- **R-177, `Updated` line:** citing another doc's IDs after that doc renamed the family fails, as COPY-R2-3.
- **R-180, `Updated` line:** a table cell naming only an AD-n that has a DN row fails. So does "follows one side until the user rules", where no DN row covers it. Found as ART-R2-2 and ART-R2-4.
- Update log entry added. No check renumbered or removed.

## Open for the supervisor and the user

- **B41 against C18 (ART-R2-1).** Either B41 also keeps a plain way into an open reveal, or C18 is answered.
- **A DN row for the Commit and sealed-year ways (ART-R2-2).** Otherwise the user rules on SI:170 against SI:77.
- **B28 (ART-R2-3).** Where a journey's line goes under the per-year option is AD-2's real question. "No line at all" should not be the default.
- **`Screen-Inventory.md:412`, `:420`** should carry B36 (N-5).
- **`Flows.md:244`** carries the COPY-R2-1 wording.

---

## Report
- Files changed:
  - `docs/reviews/2026-11-05-rules-art-microcopy-r2.md`
  - `docs/Rules-Rubric.md`: R-187 added; `Updated` lines on R-177 and R-180; log entry.
- Findings: 8 violations and 7 notes. All 21 r1 findings are fixed.
  - **Art-Direction.md and its DN rows: 5**
    - ART-R2-1: rule zero, R-150, R-168, DN:76 (B41), AD:351/364/695. The ready line becomes the only way into a reveal, which forces C18. **High for the preview:** Long Way Round's reveal can become unreachable, or nagging.
    - ART-R2-2: R-186, R-096, R-180, R-135, AD:349/350/364. The Commit and sealed-year ways appear and disappear at unlock, "until the user rules". **Medium:** a "Commit" way appears on unlock day.
    - ART-R2-3: R-141, Spec:186, DN:63/66 (B28, B31), AD:219. Under B4's option the activity line disappears after finish, so flipping B4 changes B5. **Medium:** the user would compare B4 on a false premise.
    - ART-R2-4: R-180, AD:364/218–223/247. A stale "pending: see report" line, and table cells naming AD-n instead of their B-rows. **Low.**
    - ART-R2-5: R-181, AD:259. `[AD]` places the envelope on S-03. **Nothing visible.**
  - **Microcopy.md: 3**
    - COPY-R2-1: R-182, R-183, MC:67/69. "Begun by this press" shows beside "No highlight was started." **Low to medium:** it looks like a bug on S-13.
    - COPY-R2-2: R-183, MC:100. "The year as you kept it" is false after a lost press. **Low:** bug path only.
    - COPY-R2-3: R-177, MC:5/211–216. Stale Flows C-n IDs collide with DN C1 to C9. **Low:** doc readers only.
  - **Notes (not violations):** N-1 (M-25, the G-12 residual), N-2 (newest ring thinnest), N-3 (AD:632 wording), N-4 (B39 copy unwritten), N-5 (SI:412 and :420 against B36), N-6 (M-23 under B4's default), N-7 (AD-17 reachable at +5 years).
- Rubric additions: R-187. `Updated` lines on R-177 and R-180.
- Verdict: `docs/Art-Direction.md` FAIL. `docs/Microcopy.md` FAIL.
