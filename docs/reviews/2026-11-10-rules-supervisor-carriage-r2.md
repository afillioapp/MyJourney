# Rules re-audit r2: the supervisor's fixes for the carriage audit (git b430a54..648bf78)

Date: 2026-11-10. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-209 at the start; this re-audit adds R-210 and `Updated` lines on R-200, R-203 and R-206.

**Scope, narrow, as asked.**

1. Whether each fix for V1 to V9 of `docs/reviews/2026-11-10-rules-supervisor-carriage.md` holds.
2. The new material in 648bf78, checked against the banned list and the rubric for counters, progress marks, markers, leaks from a sealed year and ring exposure:
   - Decisions-Needed B79 to B85, E10 and the swapped B5 default
   - FS §20 YYYY and ZZZZ
   - Art-Direction "Profile timelines" and Microcopy M-06b
   - The Screen-Inventory "2026-11-10" bullets on S-01 to S-17
   - Phase-1-Amendments §15.3 (new rows) and §16.1 (changes)

Nothing else was re-audited.

**Knowledge graph.** Not used. The graph is stale (it predates every 2026-11 ruling). Everything below comes from grep and reading.

**Verdict: FAIL.** V1, V2 and V5 are fixed. V3, V4, V6, V7, V8 and V9 are only partly fixed. The new material adds three violations (R2-1 to R2-3). The report also has five notes.

**What holds up in the new material**

- **B79's under-way line passes R-012 and R-013.** It is one plain line with no position mark, no day count and no dates, and it looks the same every day. E10, the user's "day 157/365" idea, is correctly parked: it is not a switch, and the reason is given (R-141). M-06b, "A journey is under way.", has no "so far" and no number.
- **B74 as narrowed is consistent everywhere it appears** (V1). A sealed journey shows only the under-way line.
- **No banned token was added.** The scan in auto check 2 found no timer, badge, dot, streak or reminder.
- **FS §20 YYYY adds nothing that leaks.** It approves B72 to B74, with B74 narrowed.
- **FS §20 ZZZZ and B84 expose no ring.** Only the blocker's own map changes. Nobody is shown a place on anyone's rings. No third-party reader changes.
- **§15.3's new rows meet R-202 as written.** `ring_count()` and `has_journey_underway()` answer as for an unknown user. The `layer` row states ZZZZ for both sides.
- **B85 adds no limit and no number.** Repeat start and dismiss stays the owner's own act.
- **B83 is the strictest reading of NNNN.** It closes the Wind case from V4.
- **M-08 now says "The page can be added up to 15 minutes after the photo."** That answers the earlier N3.
- **The supervisor's rubric edits in 648bf78 follow the rule.** The new lines on R-144 and R-146 are added below the check as `Updated` lines and leave the original wording in place, as R-172 requires.

---

## Auto checks run

**1. R-150 step 1: B79 to B85 labelled where a file touches their question.**

```
for F in docs/Screen-Inventory.md docs/Flows.md docs/Microcopy.md docs/Phase-1-Amendments.md docs/Art-Direction.md; do
  printf "%s: " $F; for b in B79 B80 B81 B82 B83 B84 B85; do grep -q "$b" $F && printf "%s " $b; done; echo; done
docs/Screen-Inventory.md: B79 B80 B81 B82 B84 B85
docs/Flows.md: B79 B80 B81 B82 B83
docs/Microcopy.md: B79 B81 B83
docs/Phase-1-Amendments.md: B80 B82 B83 B84
docs/Art-Direction.md: B79 B80 B81
```

Read against each file:

- Screen-Inventory lacks B83, and its S-08 still states the opposite (V4 below).
- Flows lacks B84 and B85. Flow 10 part G and Flow 2a do not restate them, which is minor.
- The rest is in place.

**2. Banned-mechanic tokens in the lines 648bf78 added** (`git diff -U0 b430a54..648bf78 -- docs CLAUDE.md ':!docs/Status.md' ':!docs/Rules-Rubric.md'`). The grep was `countdown|time left|remaining|ends in|minutes? left|\bnew\b|badge|\bdot\b|remind|notif|streak|progress|count|on this day|anniversary|animat|day [0-9]+|[0-9]+ ?/ ?[0-9]+|so far|next reflection|under way`, with "no …" and "never …" lines removed.

- No added line brings in a timer, badge, dot, streak or reminder.
- Hits that needed reading:
  - "anniversary" (VVVV lines)
  - "under way" (B79, M-06b: fine)
  - "next reflection" (B82: N1)
  - "day 157/365" (E10: parked, not built)

**3. Old-rule phrases** (the same scan as auto check 3 of the first audit). Every phrase it listed is gone or marked as history: `move to their next slot together`, `unlock anniversar`, `reflections, tagging`, `b11 = named`, `includes Reflect` and `§7.x`. Two hits remain, and both are acceptable:

- `Flows.md:484` is about overviews, which still follow the unlock anniversary under §20 E.
- `docs/Overview.md:35` is historical by CLAUDE.md.

**4. §13.4.1 per-viewer counts under B83** (the subject never receives the crossing), recomputed from §13.4.1's own dates and §13.1's accepts:

| Viewer | "Journey launched" | "Path crossed" received under B83 | Total | Doc says |
|---|---|---|---|---|
| Steady Lantern | Wind 5, Hands 3 | 0: every crossing she could read names her (Wind → Lantern #1, #2, #5; Hands → Lantern #2, #3) | **8** | 13 |
| Second Wind | Lantern 5 | 1: Lantern → Hands #4. Lantern → Wind #1, #2, #5 are about her | **6** | 9 |
| Open Hands | Lantern #3, #4, #5 | 1: Lantern → Wind #5. #4's crossing is about her | **4** | 5 |
| Long Way Round | Lantern #5 | 1: Lantern → Wind #5 | **2** | 2 |
| First Light | 0 | 0 | **0** | 0 |

This is the 8 / 6 / 4 / 2 / 0 that R-208 predicted. `Phase-1-Amendments.md:1704–1712` and the test expectation at `:1946` still say 13 / 9 / 5 / 2 / 0. **Fail** (V4).

---

## V1 to V9: do the fixes hold?

### V1. B74 and a sealed journey: **fixed**

- `Decisions-Needed.md:109`: B74 now says "an **unlocked** journey", and "A sealed journey shows only B79's line to anyone, never its type or dates".
- Carried at `Flows.md:626`, `Flows.md:592` (S-16 `sealed`: "Exists only: the plain … line"), `Screen-Inventory.md:204` (S-06 bullet) and `:221` (S-06 `sealed`: "Others: exists only"). FS §20 YYYY (`Functional-Spec.md:399`) records it as narrowed.
- R-201 passes on reading.

### V2. Reflections before unlock: **fixed**

- `Functional-Spec.md:98` now reads "or at unlock if that is later … never before unlock".
- VVVV (`:395`) reads "No slot opens before unlock: slot 1 opens at the later of the first anniversary and unlock".
- `Phase-1-Amendments.md:2166`: `add_reflection()` refuses while `app_now() < unlocks_at`, as its own first guard.
- `Phase-1-Proposal.md:117` and `Master-Prompt.md:75` carry it. Check (0) at `Phase-1-Amendments.md:2170` tests an 18:00 UTC Commit.
- One loose end is N3: R-199's "same answer as a random uuid" is not in check (0).

### V3. The way to Reflect as a marker: **partly fixed**

- **Fixed in substance.** B82 (`Decisions-Needed.md:117`) puts the way on every unlocked photo of the owner's, the same whatever the slot state, and says no reader lists open slots. It is carried at `Flows.md:441` (Flow 6 step 1), `Screen-Inventory.md:459` (S-17), `:384` (S-14) and `Phase-1-Amendments.md:2169`.
- **Not carried in Flow 9.** `Flows.md:625` still reads "On a photo with no reflection in the current slot, the owner can go on to Reflect, Flow 6." That is the conditional way. A builder working from Flow 9 builds a way that shows only when a slot is empty. That is exactly the mark VVVV and R-200 ban, and it now arrives photo by photo. It needs B82's wording.
- The mechanism behind B82 is unstated. See N2.

### V4. Who receives "path crossed": **partly fixed**

**Fixed: the question is settled.** B83 (`Decisions-Needed.md:118`) says the person crossed never receives the line. It is carried at `Flows.md:402` and `:514`, Microcopy M-18 (`Microcopy.md:108`), the Amendments §13.4.3 table header, §14.1 and §14.4 (`:2081`), and R-146's `Updated` line. Under B83 the Wind case closes: Lantern #1 and #2's crossings now reach nobody.

**Not fixed: seven places still state the old audience or its numbers** (R-208):

1. `Screen-Inventory.md:263` (S-08): "A crossed person who is a friend receives the same unnamed line as everyone else, so learns nothing". This is the opposite of B83, on the screen a builder builds the feed from.
2. `Phase-1-Amendments.md:1739` (§13.4.3): the paragraph opens "the last column below is what is built" and still ends "The last column below shows what the user would get if E3 (a) were ruled to leave the subject out. It is not built, and it is not a recommendation." The body still says "The model builds KKKK (e) as written: … the subject included". The paragraph contradicts itself.
3. `Phase-1-Amendments.md:1730` and `:1733` (§13.4.2, the scripted announcements): Wind → Lantern (2027-04-25) and Hands → Lantern (2027-06-20) still list **Lantern** as a recipient, "the subject included". §14.4 (`:2081`) declares such rows history by pointer. R-208 forbids exactly that: "a ruling that settles an audience never does so by pointing at a column of an older table".
4. `Phase-1-Amendments.md:1704–1712` (§13.4.1): still 13 / 9 / 5 / 2 / 0, "checked here against the dates, cell by cell". Under B83 the counts are 8 / 6 / 4 / 2 / 0 (auto check 4).
5. `Phase-1-Amendments.md:1946`: the test expectation still reads "per viewer Lantern 13, Wind 9, Hands 5, Round 2, First Light 0". A Phase 3 test written from it would fail a correct build of B83, and would pass a build that leaks to the subject.
6. `Phase-1-Amendments.md:1755` (§13.4.4 intro): "the crossing still reaches both of them". The bullet below it is marked history; the intro is not.
7. `Rules-Rubric.md` R-197's how-to-check also says 13 / 9 / 5 / 2 / 0. That is the rubric's own expectation. It is read under R-208's "8 / 6 / 4 / 2 / 0 with the subject left out" once the Amendments counts are recomputed.

- **Why it matters:** NNNN's protection now depends on which doc the builder or the test author opens. Two of the seven, SI S-08 and the test expectation, would ship or pass the leak V4 found.

### V5. The block term and `ring_count()`, `has_journey_underway()`: **fixed**

- `Phase-1-Amendments.md:2125` adds both, "byte for byte" as for an unknown user. R-202 passes on reading.
- §15.5 has no case for them, but R-202's own how-to-check covers every id-taking function.

### V6. Block tells and the undecided S-07: **partly fixed**

**Fixed.**

- B84 (`Decisions-Needed.md:119`) settles the blocked side, with ZZZZ (`Functional-Spec.md:400`) settling the blocker's.
- §15.4 (`Phase-1-Amendments.md:2134`) now lists the tells from absence and accepts them as the Instagram reference.
- Screen-Inventory S-07 (`:234`) states both maps. Nothing says "blocked".

**Not fixed.**

- **A check tests the replaced rule.** `Phase-1-Amendments.md:2144` (§15.5 check 4) still asserts "`layer` rows for both users are byte-identical before and after the block and after the unblock (`PROVISIONAL: B69`)". B69 was replaced by ZZZZ (`Decisions-Needed.md` B69). A build that leaves the blocked person on the blocker's rings passes this check, and a correct ZZZZ build fails it. R-203 carried the same clause; this audit adds an `Updated` line to R-203.
- **The docs disagree on where the blocker's name leads on the blocked person's map.** B84 says "leads nowhere, as a typed name does". §15.3 (`:2126`) and SI S-07 (`:234`) say it "leads to what an unknown user shows". The two behave differently. B84's comparison also does not hold: a typed name never counts (FS §20 7), so it is never on a map. Either way it is a tell, and B84 accepts it. The docs must still pick one behaviour (rule zero).

### V7. `dismiss_highlight()` and the closed lists: **partly fixed**

**Fixed.** §16.2 (`Phase-1-Amendments.md:2174`) says the function joins the fixed list and reads `photo.highlight_id` inside the definer only. §4 item 1 (`:336`) gains "*(since 2026-11-10 also `dismiss_highlight()`, §16.2)*".

**Not fixed.**

- **The list's own test is unchanged.** The same line `:336` still says "**The set must equal {`capture`, `start_highlight`, `highlight_open`, `highlight_rows`}**". The test the build will run is the old one. The set needs `dismiss_highlight`. R-156's `Updated` line makes the set five only "once §4 item 1 lists it", and it lists it in a parenthesis beside a sentence that says four.
- **The owner's after-unlock reader is unstated.** Nothing says whether `highlight_rows()` returns a dismissed highlight, or with which end. R-205 asks for it to be written down before Phase 3.

### V8. Screen-Inventory carriage of B70, B72, B73, B74, B78: **partly fixed**

**Fixed.** All five are carried in dated bullets:

- B78 on S-01 (`:74`)
- B72 on S-02 (`:92`) and S-12 (`:344`)
- B73 on S-03 (`:115`), S-13 (`:366`) and S-05 (`:176`)
- B74 on S-06 (`:204`) and S-16 (`:422`)
- B70 on S-14 (`:384`)

**Not fixed.** The same pass left B81's replacement of B75 uncarried in three rows:

- **`Screen-Inventory.md:207` (S-06 Reached from):** still "Positivity Feed S-09, by the way from its one photo (`PROVISIONAL: B75`) … Always opens at its beginning (`PROVISIONAL: B75`)". That contradicts the bullet three lines above it (`:204`, "replacing B75").
- **`Screen-Inventory.md:287` (S-09 Leads to):** "A photo, followed forward S-17, Walking a path S-06, Another user's profile S-16". B81 says a Positivity Feed photo "leads to its owner's profile, never straight into the path".
- **`Screen-Inventory.md:462` (S-17 Leads to):** still "Walking a path S-06" for an S-17 reached from S-09.

Under R-206 (updated) these routes fail.

### V9. Stale lines: **partly fixed**

**Fixed:**

| Item | Where |
|---|---|
| 1 | `Master-Prompt.md:73`, `:75` |
| 2 | `Build-Plan.md:108` |
| 3 | `Flows.md:131`, `:136`; `preview/index.html:282`, `:287` |
| 4 | `Screen-Inventory.md:191`, `:700`; `Decisions-Needed.md:132` |
| 5 | `Phase-1-Proposal.md:117` |
| 6 | `Phase-1-Proposal.md:368` |
| 7 | `Functional-Spec.md` PPPP, QQQQ, UUUU |
| 10 | `Phase-1-Amendments.md:1757` |
| 11 | `Decisions-Needed.md:112` |

**Not fixed, or newly stale:**

- **Item 8, first half.** `Flows.md:244` still ends "Gap: a press on the way out of the camera after that instant. Whether it is CCCC's 'next press', going to S-05, or goes where it points, is not stated: FQ-10". The same bullet now says B72 settles it, and B72 is decided (YYYY).
- **Item 9.** `Phase-1-Amendments.md:3` still says "MMMM (blocking) is carried in §15, to come". It is followed by a new sentence saying it is carried. §0 Summary (`:11` on) still has no rows for §14, §15 or §16, which are model changes.
- **New: the FQ table.** `Flows.md:807` (FQ-3), `:810` (FQ-6) and `:814` (FQ-10) still head their rows "Default 2026-11-10: `PROVISIONAL: B73` / `B74` / `B72`", although FS §20 YYYY decided all three. `:813` (FQ-9) still gives B75, which B81 replaced.
- **New: the Status line.** `Status.md:15`, "Waiting on you", still lists "E6 (does a block touch the rings; built as B69); OK on proposed defaults B72–B75". E6 is decided (ZZZZ), B72 to B74 are decided (YYYY), and B75 is replaced. The user reads this line.

---

## New findings in 648bf78

### R2-1. B79 against B19: the owner's sealed line both has dates and has none

- **Check:** rule zero ("When two docs disagree, do not pick"); R-012, R-099 (what a merged build risks); R-150
- **Where:**
  - B79, `Decisions-Needed.md:114`: "no dates, identical for every viewer and every day". Art-Direction "Profile timelines", `Art-Direction.md:392`: "no ends labelled".
  - Against: B19, `Decisions-Needed.md:38` ("The owner of a sealed journey sees its type, commit date and unlock date"). `Screen-Inventory.md:192` (S-05 `sealed`: "with its type by name and its commit and unlock dates as plain dates"). `Flows.md:564` (S-05 `sealed`: "its two dates as plain dates").
- **What is wrong:** S-05 now shows the current journey as B79's timeline (`Screen-Inventory.md:176`, `Flows.md:551`). One default says the owner's line has no dates and looks the same for every viewer. Two screen rows say the owner sees both dates.
- **Why it matters:** the natural merge puts the commit date at one end of the line and the unlock date at the other. That turns the line into a scale running from start to finish. The owner knows today's date, so the line reads as a progress bar with the position left for them to fill in. E10, the user's "day 157/365", is the next small step. B79 itself says "no ends labelled".
- **Strictest reading:** the line carries no dates. B19's dates, if kept, are plain words apart from the line, never at its ends.
- **Serious for the prototype:** low to medium. It is the profile, the screen every session opens on (C12).

### R2-2. B80's "one spark per photo" draws the highlight residual by default, and may draw a per-day count

- **Check:** R-151 (residual), R-144, R-154, FS §20 DD, B6, B8; new R-210
- **Where:**
  - B80 at `Decisions-Needed.md:115` ("one spark per photo, on the day it was taken"; "a friend sees sparks only for photos they can read")
  - B5's default swapped (`:24`; `Phase-1-Amendments.md` §3 `b5`)
  - `Art-Direction.md:392` ("a small spark at each photo's day")
  - `Flows.md:576`, `:584`; `Screen-Inventory.md:422`
- **What is wrong:**
  - **The default changed.** Before 648bf78, a non-owner saw activity only under B5's non-default switch. Now every friend sees, by default, a mark for each readable photo on the profile itself.
  - **R-151's residual becomes the default.** Lantern #1's graduation-party highlight holds 4 photos Wind can read on one day (P1:266). R-151 has reported this residual every round as one that "goes to the supervisor, not into the build". B80 puts it into the build, drawn.
  - **Same-day photos are unstated.** "One spark per photo" does not say what happens when several photos share a day: separate sparks, stacked, taller or darker. Any of those gives a non-owner the day's photo count without a numeral, and points straight at a highlight. FS §20 DD says a non-owner never learns that. B8 bans counters at all times.
- **Strictest reading:** for a non-owner, at most one identical spark per UTC day that holds any photo they can read (R-210).
- **Serious for the prototype:** medium. It shows on the first friend profile anyone opens, Lantern as seen by Wind.

### R2-3. A public viewer is shown every closed journey, against B74, and can count unfinished reveals

- **Check:** R-162 (the reveal state never reaches a public reader), FS §20 SS, ZZ, T; rule zero
- **Where:**
  - B80 at `Decisions-Needed.md:115` ("a public viewer sees the journey listed with no line"); `Art-Direction.md:392` ("A public viewer sees the journey's place with no line"); `Flows.md:576`; `Screen-Inventory.md:422`
  - Against: B74 at `Decisions-Needed.md:109` ("An **unlocked** journey with no photo this reader can see is not shown to a public reader")
- **What is wrong:**
  - **The docs disagree.** B80 and Art-Direction list a place for every closed journey to a public viewer. B74 says a journey with nothing they can read is not shown to them.
  - **Under B80's reading the public viewer can count unfinished reveals.** They see a place for every unlocked journey and, from `ring_count()` (FS §20 CCC), the number of finished reveals. Places minus rings gives the number of unlocked journeys whose reveal is not finished. Under B2's "only after reveal finished" setting that is every reveal-open journey.
  - **That path is not one ZZ allows.** ZZ allows a public reader to infer the reveal state only from the Positivity Feed, rings and photos appearing (G-23). Bare journey places are not on that list. FS §20 T also keeps journey rows from public readers after unlock.
- **Strictest reading:** B74. A public viewer sees a place only for a journey holding a photo they can read, which ZZ already allows.
- **Serious for the prototype:** low to medium. Visible as First Light on Lantern.

---

## Notes (not violations)

- **N1. B82's line, "the date this photo's next reflection opens".** It is shown on the owner's own press, as a calendar date, never relative. That is the same allowance R-013 gives the unlock date, so it is not a reminder. It sits close to one. The copy must not invite a return ("come back on …", "see you on …"), and the date must never sit on S-17 before the press. R-200 now says so (`Updated` line).
- **N2. How S-17 knows the slot state is unstated.** B82 needs, before any text is written, whether this photo's slot is open and empty, and the date of its next slot. §16.1 (`Phase-1-Amendments.md:2169`) says "no reader returns open slots to anyone, the owner included; the writer itself answers whether this photo's slot is open". The writer needs text, so it cannot answer that before the press. Either the app works it out from the owner's own `captured_at`, `unlocks_at` and stack, or a reader returns one photo's state, which R-200 allows ("no function returns more than one photo's slot state"). Pick one in §16.1. A reader that answers for many photos is the to-do list V3 (c) warned of.
- **N3. R-199's identical-answer test is not in §16.1 check (0)** (`Phase-1-Amendments.md:2170`). Before unlock, the refusal on an existing sealed photo must equal the refusal on a random uuid.
- **N4. The Status summary is ahead of the docs.** The 648bf78 Log line (`Status.md:194`) says "All fixed by the supervisor". V3, V4, V6, V7, V8 and V9 are partly fixed (above).
- **N5. Weakest point after these fixes: R-210 is review-heavy.** A spark's height or tone is a drawing decision, and the data check catches only a per-photo response. Until the art director states one mark per day for non-owners in `Art-Direction.md`, a reflexive "taller spark for a busy day" can come back through the drawing alone.

---

## Rubric additions

- **R-210** (area 1, after R-201): for any viewer but the owner, a drawing built from photos shows at most one identical mark per UTC day. No non-owner can read a day's photo count or a highlight's burst from marks. This is a new kind of violation: a count carried by a drawing, with no numeral.
- **`Updated` lines:**
  - **R-200:** B82 settles the way. The date line is post-press only, never relative and never an invitation, and it gets a grep aid.
  - **R-203:** FS §20 ZZZZ supersedes "changes nothing on either person's map" for the blocker's map. "Byte-identical `layer` rows" now applies to the blocked person's map only.
  - **R-206:** B81 replaces B75. The check now also covers S-09, and S-17 when reached from S-09.
- **Header:** a dated entry in the update log at the top of the file.
- **Banned-list coverage:** "No streaks, counters, progress bars, reminders" gains R-210.
- No check renumbered or removed.

## Report
- Files changed: `docs/reviews/2026-11-10-rules-supervisor-carriage-r2.md`, `docs/Rules-Rubric.md`
- Findings: 9 violations (6 partly fixed from round 1, 3 new), 5 notes. V1, V2, V5 fixed.
  - V3 (R-200, R-186): `Flows.md:625`. Flow 9 still offers the way to Reflect only "on a photo with no reflection in the current slot", against B82.
  - V4 (R-208, R-146): `Screen-Inventory.md:263`; `Phase-1-Amendments.md:1739`, `:1730`, `:1733`, `:1704–1712`, `:1946`, `:1755`. These still have the subject receive "path crossed", or keep 13 / 9 / 5 / 2 / 0 (8 / 6 / 4 / 2 / 0 under B83).
  - V6 (R-203, rule zero): `Phase-1-Amendments.md:2144`. Check 4 still asserts B69's unchanged maps. B84 (`Decisions-Needed.md:119`) "leads nowhere" disagrees with `:2126` and `Screen-Inventory.md:234` "unknown user".
  - V7 (R-156, R-205, R-209): `Phase-1-Amendments.md:336`. "The set must equal" still lists four functions. The after-unlock reader of a dismissed highlight is unstated.
  - V8 (R-150, R-206): `Screen-Inventory.md:207`, `:287`, `:462`. B75 is still carried, and S-09 and S-17 still lead straight into the path, against B81.
  - V9 (R-165): `Flows.md:244`, `:807`, `:810`, `:813`, `:814`; `Phase-1-Amendments.md:3` and §0; `Status.md:15`. Settled questions are still called gaps or defaults.
  - R2-1 (rule zero, R-012, R-099): `Decisions-Needed.md:114` and `Art-Direction.md:392` against `Decisions-Needed.md:38`, `Screen-Inventory.md:192`, `Flows.md:564`. The owner's under-way line has no dates in one place and both dates in another, and the merge reads as a progress bar.
  - R2-2 (R-151, R-144, FS §20 DD, R-210): `Decisions-Needed.md:115`, `:24`, `Art-Direction.md:392`. One spark per photo, now default for friends, draws same-day counts and highlight bursts.
  - R2-3 (R-162, FS §20 SS, ZZ, T): `Decisions-Needed.md:115`, `Art-Direction.md:392`, `Flows.md:576`, `Screen-Inventory.md:422` against `Decisions-Needed.md:109`. Public viewers see every closed journey's place, and places minus rings gives unfinished reveals.
- Rubric additions: R-210; `Updated` lines on R-200, R-203, R-206
- Verdict: FAIL

## In plain language

- **Reflect (V3).** One flow still describes the way to Reflect as appearing only when a photo can be reflected on. Built that way, it is a "you can reflect now" signal, photo by photo.
- **"Path crossed" (V4).** The settled rule says the person crossed is never sent the line. The feed screen spec and the data tests still send it to them, and the test numbers would reward that mistake.
- **Blocking (V6).** One data check still expects a block to leave both maps untouched, which the user's ruling changed. The docs also disagree on what the blocked person sees when they tap the blocker's name.
- **Highlight dismissal (V7).** The list of the only functions allowed to touch highlights still names four, not five, in the sentence the test will use.
- **Positivity Feed (V8).** Three screen rows still let it jump straight into someone's path, which the new profile-timeline default forbids.
- **Stale lines (V9).** Some say settled things are still open, including the "waiting on you" line in Status.
- **The owner's sealed line (R2-1).** One default says it shows no dates, but older screen rows give it both dates. Built together, the dates sit at the two ends and the line becomes a progress bar.
- **Sparks (R2-2).** Friends now see a spark for every photo by default. If a busy day draws as several sparks or a taller one, they can count that day's photos and spot a highlight, which they must never learn.
- **Public viewers (R2-3).** They are shown a place for every unlocked journey, even one with nothing they can read. Comparing that with the ring count tells them how many reveals are unfinished, which they must never learn.
