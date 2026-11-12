# Rules audit: the dotted circle, Spec §20 AAAAA (git a2c9ff4..1177709)

Date: 2026-11-12. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-210 and G-1 to G-28 at the start. This audit adds R-211 to R-213 and G-29, and `Updated 2026-11-12` lines on R-011, R-098, R-144, R-149, R-150, R-151, R-155, R-165, R-185, R-187, R-210 and G-7.

**Scope.** Everything changed in commits 93a5196, 39e7f96 and 1177709:

- **Docs:** `Functional-Spec.md` §14 and §20 AAAAA; `Art-Direction.md` §0, §2, §3.2, §3.3, §3.5, §3.6, §4, §8, §10, §11, §12; `Decisions-Needed.md` B27, B34 and B86 to B89; `CLAUDE.md` (the profile paragraph); `Status.md`.
- **Code:** `preview/build.py` and the `preview/index.html` it generates; `preview/test_build.py`; `prototype/index.html` (the circle and the fixture highlights); `prototype/test_prototype.mjs`.

I also read every other doc that describes the circle, to see whether AAAAA reached it.

**Knowledge graph.** I used it to find where things are, and nothing else. `graphify-out/graph.json` is dated 2026-10-27, so it predates every November ruling, AAAAA included. `graphify query` led to `Functional-Spec.md:181` (§14), `My-Journey-Concept.md:681` and `:702`. `graphify path "Profile Circle and Rings" "No streaks, counters, progress bars, reminders" --undirected` found a link only through INFERRED edges, and I did not act on it. Every finding below cites the source file and line.

**Verdict: FAIL.** I found 7 violations (V1 to V7). The rubric's own rows still assumed the retired ring line (V8); I have updated them. Two residuals go to the user (R1, R2), and there are two weak points (W1, W2).

## What holds up

- **Nothing leaks from a sealed year.** No ring is drawn for a sealed journey. The owner's circle is byte-identical on 2026-02-01, 2026-07-01 and 2026-12-31, and after a capture (prototype test 6; R-012, R-143).
- **To anyone but the owner, the circle comes from the count alone (B88).** Every ring is 52 dots of one size. As First Light, Second Wind's circle and Steady Lantern's circle (five rings each) are byte-identical once the name and the `aria-label` are masked (probe, auto check 6). The start angle `θ_k` depends only on the finishing order `k`, so no position is taken from a date (R-179). `highlight_id` and the weeks that held photos never reach a non-owner (Spec §20 DD; R-151).
- **No dot grows with the number of photos.** Each week takes `max(size, 1)`, and a highlight's week takes size 2 (`prototype/index.html:310–314`, `preview/build.py:272–281`). There are at most three radii per ring (prototype test 2).
- **A highlight that held no photo draws no biggest dot** (B87; prototype test 7).
- **The newest ring is next to the name and in full ink. Older rings move out a step finer and keep their pattern** (AAAAA (c); prototype tests 3 and 5). The ink is set by place, never by a count (IIII as kept by AAAAA).
- **No number reaches a screen reader.** The rings are `aria-hidden`, and the label is `<name>'s circle` (prototype test 9; Art-Direction §11 check 8).
- **B88 is the strictest reading.** It is stricter than AD-24 as first proposed, and B5's switch does not loosen it.
- **The generated preview matches its generator.** I rebuilt it in memory without writing: `preview/index.html in sync: True`.
- **No banned word or token was added to the code** (auto check 5).

---

## Auto checks run

**1. The two test suites.**

```
$ python3 -m unittest discover -s preview
..................
Ran 18 tests in 0.006s
OK

$ node --test prototype/test_prototype.mjs
✔ the owner's profile at baseline shows one ring of 52 dots per finished reveal
✔ the owner sees at most three sizes, and her highlight weeks are the biggest
✔ the newest ring is next to the name, in full ink, and holds the newest journey
✔ anyone else sees the same rings as even dots, with no sizes
✔ a finished reveal adds its ring next to the name, and older rings move out keeping their pattern
✔ the sealed year adds nothing to the circle, photo or no photo
✔ a highlight that held no photo leaves no biggest dot (B87)
✔ the fixture highlights hold their photos inside their 24 hours (Proposal §3.3)
✔ the circle's markup carries no number for a screen reader
ℹ tests 9  ℹ pass 9  ℹ fail 0
```

**2. Preview in sync.** I imported `preview/build.py`, patched `Path.write_text` to capture the page instead of writing it, and compared the result with the file on disk. Output: `in sync: True 388645 388645`. `git status` was clean afterwards.

**3. R-149, steps 1 to 3.**

- Step 1 printed three prose lines in `preview/index.html` (`:258`, `:461`, `:750`). Each explains what a label means, they were there before this change, and they are not code labels.
- Step 2 printed nothing.
- Step 3 printed `B2 B4 B5`.

Labels found in the two changed code files:

```
2 PROVISIONAL: B30   1 PROVISIONAL: B40   2 PROVISIONAL: B86   2 PROVISIONAL: B87   2 PROVISIONAL: B88
```

There is no `PROVISIONAL: B89` and no `PROVISIONAL: B4` in either file (V1).

**4. Scan for informal labels (the new R-213 (2)).**

```
$ grep -rnE --include='*.py' --include='*.html' --include='*.js' --include='*.mjs' --exclude-dir=graphify-out '\b[BC][0-9]{1,3} default\b|default [BC][0-9]{1,3}\b' preview prototype site | grep -v '^preview/index.html'
prototype/index.html:221:  return inNetwork(viewer, j.owner, t); // B2 default: network reads from unlock
prototype/index.html:224:// B4 default: one ring per finished reveal, in the order of finishing (§20 AAAAA; B34). §20 CCC: others get the count only.
```

Line 224 was rewritten in 1177709. Line 221 was there before.

**5. Grep aids for R-006 (a), R-013, R-096, R-097, R-098, R-099 and R-185, over the lines this change added to code.** The pattern covered `n photos`, `of n`, frames left, `so far`, `remaining`, countdown words, `<progress`, `aria-valuenow`, `stroke-dashoffset`, `streak`, `chain`, `in a row`, `new`, `badge`, `unread`, `level`, `rank`, `tier`, `veteran`, `established` and `young`. It had one hit:

```
+ "Her year is now a ring of 52 weeks next to her name, ..."   (preview/build.py, caption of the S-05 moment)
```

This is a caption in the preview that describes the construction. It is not copy shown in the app, and it is not a count. It passes.

**6. Probe of the prototype.** I ran the page's own script in a Node VM. The script is `/private/tmp/claude-501/-Users-alireza-Projects-Retro-Gram/3bbab8a0-aca7-4cf3-a433-14c9ef2aa761/scratchpad/probe.mjs`. Output, trimmed:

```
lantern1 highlight photos in window: 19
Wind sees in-highlight lantern1: [["p42","2021-07-17T11:53:41Z","network"],["p43","2021-07-17T13:09:28Z","public"],
  ["p44","2021-07-17T14:25:15Z","network"],["p48","2021-07-17T19:28:25Z","public"],["p49","2021-07-17T20:44:12Z","network"],
  ["p50","2021-07-17T22:00:00Z","network"],["p53","2021-07-18T01:47:22Z","network"],["p54","2021-07-18T03:03:09Z","network"],
  ["p56","2021-07-18T05:34:44Z","public"],["p59","2021-07-18T09:22:06Z","network"]]      <- listed in Wind's path order (day, then id)
Light (public) sees in-highlight lantern1: p43 (17 Jul), p48 (17 Jul), p56 (18 Jul)
max same-day photos visible to wind per journey: {"lantern1":7,"lantern5":5}
public svg data-place values: 5,4,3,2,1
identical after stripping name: true             <- Wind's and Lantern's circles as First Light
lantern1 [12,39,1]  lantern2 [15,37,0]  lantern3 [30,22,0]  lantern4 [28,24,0]  lantern5 [39,12,1]   <- owner: [no-photo, photo, highlight] weeks
```

**7. Ink share of the even-dot band** (R-185; Python, using the §3.2 formulas):

```
band from frame r=80:        n=1 2.59%  n=2 2.96%  n=3 2.95%  n=5 2.72%  n=12 2.11%  n=20 1.89%
band from first ring's edge: n=1 4.38%  n=2 4.07%  n=3 3.73%  n=5 3.19%  n=12 2.33%  n=20 2.06%
total ink (units²):          n=1 285  n=2 490  n=3 639  n=5 824  n=10 986  n=20 1024
```

**8. Was AAAAA carried, and are B86 to B89 named, in each doc that describes the circle?** (R-150 step 1, R-165)

```
docs/Screen-Inventory.md: B86=0 B87=0 B88=0 B89=0  AAAAA=0
docs/Flows.md:            B86=0 B87=0 B88=0 B89=0  AAAAA=0
docs/Microcopy.md:                                 AAAAA=0
docs/Art-Direction.md:    B86=4 B87=4 B88=9 B89=4
```

**9. Retired wording across the docs.** I grepped for `added outermost`, `never moves`, `day marks`, `ink share`, `22%`, `thinnest`, `plain ring`, `ring line` and `twists in`, leaving out the reviews and the rubric. The hits are listed under V3, V4 and V5. Microcopy has no hit that conflicts: its "A ring being added" row (`Microcopy.md:183`) keeps the moment silent, which still holds.

---

## Findings

### V1. Two provisional defaults are built with no label: B89 everywhere it is built, and B4 in the code this change rewrote

- **Checks:** rule zero step 3 (`CLAUDE.md`, "Every provisional default is labelled in the code"); R-135's rule-zero line ("the default without its `PROVISIONAL:` label still fails"); R-149; new R-213.
- **Where:**
  - B89, "Each ring is 85% of the pitch of the ring inside it" (`Decisions-Needed.md:124`), is built at `preview/build.py:240` (`FIRST_PITCH, PITCH_RATIO, CLEARANCE = 11, 0.85, 3`) and at `prototype/index.html:300` (`PITCH_RATIO = 0.85`). There is no label on either line or in the functions that use them (`build.py:248–253`, `prototype/index.html:302–307`).
  - B4's "one ring per finished reveal" is built at `prototype/index.html:224–225` (`finishedJourneys`) and `:332–333`, and at `preview/build.py:304–310` (`circle(name, journeys)`, "one entry per finished reveal"). The prototype comment says "B4 default". That is not the labelled form, and R-149's grep cannot find it.
- **What is wrong:** Art-Direction §0 says "the preview and the prototype draw it". B89 is the geometry that decides when the oldest rings become illegible, and it is the default B89 itself says is "for the user to judge by playing". Nobody can find it by its label.
- **Why it breaks the rule:** rule zero requires every provisional default to be findable and changeable by its `PROVISIONAL:` label. R-149 checks only that each label points to a row, so an unlabelled default passed it. That gap is why R-213 is new.

### V2. Since 1177709, the prototype gives non-owners same-day photos in capture order

- **Check:** R-155 (c): "photos from one day reach a non-owner in an order that carries no time of day ... within one date it has no relation to capture time". R-155 (a): "Every id is random, nothing uses a sequence".
- **Where:**
  - Photo ids are `"p" + (pid++)`, created in capture order (`prototype/index.html:188`). Pressed photos get the next number (`:244`).
  - A non-owner's path sorts by UTC day, then by that id (`:381`).
  - The new fixture highlights put 19, 12 and 30 photos inside one 24 hours each (`:169`, `:184–186`).
- **What is wrong:** as Second Wind at baseline, Lantern #1's six photos dated 17 July 2021 come in exactly their capture order: 11:53, 13:09, 14:25, 19:28, 20:44, 22:00 (auto check 6). First Light gets the same for her two public photos of that day.
- **Why it breaks the rule:** before this change, no fixture day held two photos, because photos were spread 7.5 days or more apart, so the sequential tie-break said nothing. The fixture change made it carry the order of capture within a day, which §20 JJ rules out for anyone but the owner.

### V3. §20 AAAAA (a) contradicts B4's per-year option, and the carriage settled it without raising it

- **Checks:** R-135 (docs disagree: cite both lines, do not pick); R-134 (a behaviour with no source); R-187 (defaults hold when read together). New gap G-29.
- **Where:**
  - FS §20 AAAAA (a) (`Functional-Spec.md:404`): "Each ring is one journey ... The ring line with its day marks is retired."
  - Against it: FS §20 GGGG (`:372`), "B4 itself remains a switchable provisional default", with "each finished journey's day marks go on the ring for the year"; DN B4 (`Decisions-Needed.md:23`, switchable); DN B28 (`:63`, still "day marks"); `Functional-Spec.md:185`, "One ring per year with the app", which sits beside the line this change annotated.
  - `Art-Direction.md` §3.2 keeps the option (`:132`, `:138–146`) and fills the gap with three readings that no row states:
    - "A per-year ring that holds no finished journey is a ring of even dots" (`:145`, `:249`).
    - On a ring shared by two journeys, "a week takes the larger of the two sizes" (`:146`).
    - `θ_k` is set by "the journey's place in the order of finishing" (`:159`). A per-year ring that holds no journey, or two, has no such place.
  - Art-Direction §12 B, "What adds a ring" (`:751`), was not updated for AAAAA.
- **What is wrong:** with dots, an even-dot ring means "a year with no photo" (§3.3, `:216`: "A ring of small dots beside a busy one marks a quiet year"). Under B28's timing, a journey's weeks go on the ring for the year it was finished in. The ring for the year it was taken in is then drawn as 52 empty weeks. Flipping B4 therefore changes what the owner's own circle says about their activity. That is R-187's failure, and it is new with dots, because a plain line carried no such meaning.
- **Why it breaks the rule:** two §20 rulings disagree, and the carriage followed one of them (GGGG) and invented readings, without citing both and raising the question. Nothing built depends on it yet: the prototype has no B4 switch, and the preview draws only the default.

### V4. §3.6 rows rewritten in 93a5196 still carry B5's and B31's defaults from before 2026-11-10

- **Check:** R-150 ("never describes the other side ... as what the screen holds").
- **Where:**
  - `Art-Direction.md:250` and `:252` label B5's "owner only" as "(default)".
  - `:248` and `:251` say the flat graph is shown "until reveal finished, then not shown (`PROVISIONAL: B31`)".
  - DN B5 (`Decisions-Needed.md:24`) has had "built from the photos the viewer can see" as its default since 2026-11-10 (B80). DN B31 (`:66`) has said since 2026-11-10 that "the flat timeline stays on the profile after the reveal is finished" (B81). Art-Direction's own §0 says the same (`:29`: "The profile timelines below the circle keep their sparks").
  - `:219` reads "Under B5's default only the owner sees the sizes". The sizes are the owner's under both B5 settings, by B88, and B5's default is now built from what the viewer can see.
  - AD-11 (`:733`) still reads "None needed beyond B5's default: only the owner sees it", and still describes the retired line ("rises", "a clean ring").
- **What is wrong:** these rows were rewritten in this change, yet they describe the old side of two defaults.
- **Why it breaks the rule:** a builder who reads §3.6 would build the replaced behaviour for the timelines (R-150), and would tie the dot sizes to the B5 switch, which B88 rules out.

### V5. AAAAA did not reach Screen-Inventory or Flows, and two status lines are stale

- **Check:** R-165 (2) and (3) (every §20 ruling is carried in each build doc it bears on, and none keeps a behaviour the ruling replaced).
- **Where:**
  - `Screen-Inventory.md` S-05: `:175` ("the activity line twisted into it"), `:187` ("The line twists into the circle"), `:192` (`sealed`: "Rings and activity lines of earlier journeys") and `:194` (`reveal-finished`: "this journey's ring. The year's activity line twisted into the circle"). Nothing says the ring arrives next to the name and the older rings move out.
  - S-16 (`:427`): its never-show list has no dot sizes, and B88 appears nowhere in SI.
  - `Flows.md` Flow 5 step 6 (`:403–404`: the ring "is added to S-05", "The year's activity line twists into the circle"). Flow 8 part A (`:550`: "earlier years' activity lines twisted in"; `:559`; `:565–566`).
  - Neither doc names AAAAA or B86 to B89 (auto check 8).
  - Status lines: `Art-Direction.md:3` still says "rulings **A to DDDD**" though the file now carries AAAAA. `Decisions-Needed.md:10` still says "Last updated: 2026-11-09" though B86 to B89 were added on 2026-11-12. `Status.md:197` lists the docs carried, and SI and Flows are not among them.
- **What is wrong:** the two docs that say what each viewer sees on S-05 and S-16 still describe the retired line. They do not say who sees the dot sizes.
- **Why it breaks the rule:** a ux or build step that reads SI or Flows gets the replaced behaviour, and no "must never show" protects B88 on the screen where it matters.

### V6. "Tone does not rise with count" names no measure, and under one fair measure it rises

- **Check:** R-185 ("each 'do' in the art rules holds for every value its own formulas allow"); the §10 "do not" line "Heavier or darker circles for more rings" (`Art-Direction.md:675`).
- **Where:** `Art-Direction.md:179`. The 22% ink-share invariant, which made the old claim testable, was removed (diff of §3.2), and nothing measurable replaced it.
- **What is wrong:** measured over the band from the frame, the ink share of even dots rises from 2.59% at one ring to 2.96% at two, then falls. Measured from the first ring's inner edge, it falls at every step. Total ink rises at every count, toward about 3.6 times one ring (auto check 7). The new wording redefines tone ring by ring ("a ring's dots are fixed by its place"), which is not the claim §10 makes about the whole circle.
- **Why it breaks the rule:** R-185 needs each "do" to hold at every value. Without a stated measure, the claim cannot be checked, and on the frame-band measure it fails at n = 2. This is a review finding. It may be fixed by stating the measure; the growth in total ink is allowed by Concept:687 ("more years means a more elaborate circle").

### V7. B86's "8 or 9 days" is false for a Commit not made at 00:00 UTC

- **Checks:** R-134 (a behaviour traces to a correct source); R-150 step 4 (a labelled passage says what its row says). This is the same mistake R-199 found.
- **Where:**
  - `Decisions-Needed.md:121` ("Week 52 also holds what is left, so it has 8 or 9 days, because a journey is 365 or 366 days").
  - `Art-Direction.md:198`.
  - Repeated in the code comments at `prototype/index.html:309` and `preview/build.py:268`.
- **What is wrong:** `unlocks_at` keeps the time of day of the Commit (`Phase-1-Proposal.md:74`). A journey committed at 14:37 therefore touches 366 UTC dates, or 367 across a 29 February, so week 52 holds 9 or 10 days. A prototype Commit is made at the running clock (`prototype/index.html:484`), so it is almost never at 00:00:00.
- **Why it breaks the rule:** the code clamps the week number (`Math.min(..., 51)`, `min(day // 7, WEEKS - 1)`), so every photo still falls in exactly one week. Nothing leaks and nothing is drawn wrongly. But the default's own text is wrong arithmetic that a later builder could take literally, for example by asserting 8 or 9. This is minor.

### V8. The rubric's own rows assumed the retired ring line (recorded and updated by the rubric's owner)

- **Checks:** R-011 (`:170`, "the line does not twist into the circle"), R-144 (`:1610`, "the line twists into the circle only at reveal finished"), R-185 (`:1469`, worked values at n = 1, 5, 9, 10, 17, 25, 40 and the 22% share), R-187 (`:1484`, "day marks on a ring"). Also R-149: its patterns take IDs of up to two digits, and the table now reaches B89, so B100 will be misread.
- **What I did:** added `Updated 2026-11-12` lines to each of these and left the old wording in place. R-210 gains a line that brings the circle under it. R-098 gains a line on highlight dots (R2).

### R1. Residual, for the user: the photo dates in the prototype now show a highlight's burst

- **Check:** R-151 residual (accepted, and reported until the user rules).
- **Where:** `prototype/index.html:169`, `:184–186`, and `tile()`, which shows each photo's date.
- **What:** at baseline, Second Wind reads 10 of Lantern #1's 19 highlight photos, 6 dated 17 July 2021 and 4 dated 18 July. Up to 7 of the photos she reads share one date, more than an Explorer's month allows. First Light reads 3 of them (auto check 6). The circle adds nothing to this (B88). The dates carry it, as the residual says. It was on paper before, and now it can be played. Not a violation.

### R2. Residual, for the user: the owner's ring reads as a 52-cell grid, and its highlight dots can be counted

- **Checks:** R-098 under B7 ("highlights used or left ... at any time, to the owner as well"); R-097; R-099; AD-11 (open).
- **Where:**
  - AAAAA (b) (`Functional-Spec.md:404`). B87 (`Decisions-Needed.md:122`: "an Explorer has at most 4 highlight dots").
  - Art-Direction §3.3 (`:213–217`), which itself says "Fullness can be read as a score, which is what a contribution graph is read for".
- **What:**
  - On a finished ring, each small dot is a week that passed without a photo. The owner can count them. Lantern's rings run from 12 to 39 empty weeks out of 52 (auto check 6).
  - The owner can also count the highlights a journey used, one biggest dot each.
  - The cadence is monthly, but the grain is weekly. So the next year's ring may come to feel like a weekly target, although nothing is drawn while that year is sealed. Concept:712–714 answers this only for a grid seen "while you are filling it".
- **Status:** AAAAA rules the sizes, so this is not a build violation, and I have not reported it as one. AD-11, whether fullness is acceptable, is still unanswered after AAAAA. R-212 records the residual, and R-098 records the highlight count as allowed by the ruling.

### W1. Weak point: B87 reads a stored count of highlight photos

- **Where:** `prototype/index.html:313` reads `h.count > 0`. That `h.count` is incremented on every highlight capture (`:241`, `:253`). The comment at `:310` says "No count is kept".
- **Why it matters:** `Phase-1-Proposal.md:49` and R-039 keep highlight counts unstored in the real model. The prototype has no schema, so this is not a violation, but B87 should be built from the photos themselves ("a photo inside this highlight's window exists"), not from a counter.

### W2. Weak point: each ring carries its place number in the DOM

- **Where:** `data-place="1"` to `"n"` (`prototype/index.html:322`, `preview/build.py:294`). For a public viewer, the largest value equals the ring count.
- **Why it matters:** the attribute is `aria-hidden` and never shown, and the count is what Spec §20 CCC gives everyone, so R-166 passes. It is still the only numeral in the circle's markup. If anything ever reads it (a tooltip, a test, a screenshot tool), it becomes a printed count.

---

## Rubric additions

- **R-211** (area 5): to anyone but the owner, the dotted circle depends on the ring count alone. It is identical across viewers and B5 settings, and changes with no photo, highlight, visibility, date or map place.
- **R-212** (area 8): on the owner's ring, three sizes, set only by "has a photo" and "a highlight holding a photo opened here". It is drawn whole at reveal finished, with nothing for an unused highlight, a week still to come or an unfinished journey. It carries R2 as its residual.
- **R-213** (area 14): every provisional default the code builds carries its label at the code that builds it, numbers and geometry included. An informal "Bn default" is not a label. This is the direction R-149 does not check.
- **G-29:** AAAAA (a) against B4's per-year option, GGGG and B28. Still open, for the user.
- **`Updated 2026-11-12` lines:** R-011, R-098, R-144, R-149, R-150, R-151, R-155, R-165, R-185, R-187, R-210, G-7.
- **Banned-list coverage:** R-212 under "No streaks, counters"; R-211 and R-212 under "No ranking"; R-211 under "No layer is ever shown".

No check was renumbered or removed. The only lines changed in place are the three coverage rows, which gained IDs.

## Notes (not rubric findings)

- **N1.** `Status.md` was last updated in 93a5196 (`:197`: "Next: preview and prototype drawing, then a rules audit"). The two build commits, 39e7f96 and 1177709, added nothing to it, although `CLAUDE.md` says "Update it after every step".
- **N2.** `CLAUDE.md`'s profile paragraph says "the week a highlight opened the biggest" and leaves out B87's condition, "only when the highlight holds at least one photo". This is a summary, and it does not mislead about a leak.
- **N3.** `Master-Prompt.md:85` ("The circle frames the profile picture, gaining a ring each year") and `Functional-Spec.md:184` ("The circle frames the profile picture") were already wrong against §20 XXX, before this change (Art-Direction §12 B, L-002). AAAAA adds "one ring per journey" against the "each year" in those lines. That is G-29.
- **N4.** The graph is stale (2026-10-27). A `/graphify . --update` after these doc changes would let the next audit use it.

## Report
- Files changed: docs/Rules-Rubric.md, docs/reviews/2026-11-12-rules-dotted-circle.md
- Findings: 12
  - V1. R-213 / R-135 / rule zero step 3, preview/build.py:240, prototype/index.html:300, :224, preview/build.py:304: B89 (85% pitch) and B4 (one ring per finished reveal) are built with no `PROVISIONAL:` label
  - V2. R-155, prototype/index.html:188, :381 (exposed by :169, :184–186): sequential ids put a non-owner's same-day photos in capture order, now that the fixture highlights hold their photos within 24 hours
  - V3. R-135 / R-134 / R-187, G-29, Functional-Spec.md:404 against :372, Decisions-Needed.md:23, :63, Art-Direction.md:145–146, :159, :249: AAAAA (a) "each ring is one journey" contradicts B4's per-year option; the carriage kept the option and invented even-dot rings that read as empty years
  - V4. R-150, Art-Direction.md:248–253, :219, :733: rewritten §3.6 rows still carry B5's "owner only (default)" and B31's "then not shown" from before 2026-11-10
  - V5. R-165, Screen-Inventory.md:175, :187, :192, :194, :427; Flows.md:403–404, :550, :559, :565–566; Art-Direction.md:3; Decisions-Needed.md:10: AAAAA and B86–B89 not carried into SI or Flows; two status lines stale
  - V6. R-185, Art-Direction.md:179, :675: "Tone does not rise with count" names no measure; on the frame-band measure the ink share rises from n=1 to n=2
  - V7. R-134 / R-150, Decisions-Needed.md:121, Art-Direction.md:198, prototype/index.html:309, preview/build.py:268: "week 52 has 8 or 9 days" is false for a Commit not at 00:00 UTC (9 or 10); the code clamps, so no wrong drawing
  - V8. R-011:170, R-144:1610, R-185:1469, R-187:1484, R-149: rubric rows assumed the retired ring line, and R-149's patterns break at B100; updated
  - R1. R-151 residual, prototype/index.html:169, :184–186: Wind reads up to 7 photos on one date in Lantern #1, so the highlight's burst can now be played (for the user)
  - R2. R-098 / R-212 residual, AD-11, Functional-Spec.md:404: the owner's ring reads as a 52-cell grid with countable empty weeks and highlight dots; ruled by AAAAA, so for the user
  - W1. R-039 (weak point), prototype/index.html:241, :310, :313: B87 reads a stored highlight photo count, while the comment says no count is kept
  - W2. R-166 (weak point), prototype/index.html:322, preview/build.py:294: `data-place` numerals in the circle markup equal the ring count
- Rubric additions: R-211, R-212, R-213, G-29 (plus Updated 2026-11-12 lines on R-011, R-098, R-144, R-149, R-150, R-151, R-155, R-165, R-185, R-187, R-210, G-7)
- Verdict: FAIL
