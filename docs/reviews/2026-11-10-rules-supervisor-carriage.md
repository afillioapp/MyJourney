# Rules audit: the supervisor's carriage of FS §20 LLLL to XXXX (git a3b9a4f..7ad6990)

Date: 2026-11-10. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-197 at the start; this audit adds R-198 to R-209 and `Updated` lines on R-121 (superseded), R-138, R-146 and R-156.

**Targets.** Every change in `a3b9a4f..7ad6990` (nine commits, 6760478 to 7ad6990), written by the supervisor on 2026-11-10 with no rules audit:

- FS §20 LLLL to XXXX and the FS §7, §8, §9, §15 lines that carry them; `CLAUDE.md` Capture, Reveal, Reflect, Network lines; Concept §29 pointers
- `Phase-1-Amendments.md` §14 (NNNN), §15 (MMMM, blocking), §16 (VVVV, WWWW), and the §13.1, §13.4.1 date moves
- `Phase-1-Proposal.md` D9, the Reflection and Overview `year_index` rows, `prototype_option`, §3.5 and §3.7 fixture dates
- `Decisions-Needed.md` B11, B12, C6, B56 decided; B62 to B78; E2 to E9
- `Screen-Inventory.md` (S-04, S-05, S-06, S-08, S-12, S-13, S-14, S-16, S-17, S-21 to S-25, T-02, OQ-51/52/55–57); `Flows.md` (Flows 1 to 10, FQ table, DC-8, DC-15); `Microcopy.md` (M-05, M-06a, M-08, M-17, M-18, M-25, MQ-1/2/8); `Art-Direction.md` §7.x
- The friend-screens audit fixes V1, V2 (542b705)

**Knowledge graph.** `graphify query` was run ("reflection slot anniversary marker reminder"; "block user ring count unknown user"). The graph is **stale**: `graphify-out/graph.json` is dated 2026-10-27 and has no node for Amendments §12 to §16, blocking, or any 2026-11 ruling. It was used only as a map (it did point at `Master-Prompt.md` beside Reflect, which is finding V9). Everything below is from grep and reading. The graph needs `/graphify . --update`.

**Verdict: FAIL**, with 9 violations and 5 notes.

**What holds up.**

- **Fixture arithmetic is right, every cell** (table in "Auto checks" 4). Every moved reflection sits inside its VVVV slot, every pinned capture date sits inside its journey's year, and every "reflection left" audience line in Amendments §13.4.1 agrees with fr-1 to fr-11 under event-time B48. 18 fixed reflections (5 + 3 + 3 + 1 + 6) is right; round-1's depth 3 is right.
- **NNNN in the model is sound:** `person_tag_rows()` owner only, no "where you appear" route, no subject returned on a "path crossed" row, three switches left. B11, B12, C6, M-18, M-25, R-139, R-146 to R-148 agree.
- **The time-limit circle (XXXX, B77) is a fixed drawing** in every doc that names it (Art-Direction §7.x, SI S-12, S-13, Flows 2a, 3, R-140 update). No doc lets it move, fill or show time left.
- **The highlight dismiss way (B76) does not appear or disappear with the 3 hours**, and its refusal is one sentence for every cause, with no time or number (M-06a).
- **S-25 Blocked** has no count, no time, A to Z, names lead nowhere, and its way in is always present. Nothing tells anyone "blocked".
- **RRRR, SSSS, TTTT** are carried in SI, Flows and Microcopy. M-17's second line names no one and is true under both B2 settings.
- The friend-screens fixes V1 and V2 hold: SI and Flows now carry B57 to B61, and Flows' Second Wind row keeps her request to Long Way Round.

**What fails, in one line each**

- **V1** B74 gives a friend a **sealed** journey's type and dates (leak).
- **V2** "A photo's first anniversary is always after unlock" is false for any Commit not made at 00:00 UTC, and `add_reflection()` now has no unlock guard of its own (leak, data layer).
- **V3** Nothing says whether the way to Reflect is present before a photo's slot opens. If it appears on the anniversary, it is the mark VVVV bans, and it now arrives photo by photo all year (marker; rule zero).
- **V4** The docs disagree on whether the person crossed receives "path crossed"; the reading most of them build lets that person tell they are on the rings, in the fixture's own case (NNNN).
- **V5** The block term misses `ring_count()` and `has_journey_underway()`, so a blocked person can tell they are blocked by a crafted call (B64).
- **V6** The block is detectable in four more ways the leak review does not list, one of which (the blocked person's own map) is an undecided screen (rule zero).
- **V7** `dismiss_highlight()` is a new reader of sealed highlight and photo rows that R-138, R-156 and Amendments §4 item 1 do not list.
- **V8** Screen-Inventory does not carry B70, B72 (screen rows), B73, B74 or B78 (R-150).
- **V9** Stale lines still state the old rules, and settled questions are still called open (R-165).

---

## Auto checks run

**1. R-150 step 1: B57 to B78 labelled where a file touches their question.**

```
for F in docs/Screen-Inventory.md docs/Flows.md docs/Microcopy.md docs/Phase-1-Amendments.md; do
  comm -13 <(grep -oE 'PROVISIONAL: `?[BC][0-9]{1,2}' $F | grep -oE '[BC][0-9]+' | sort -u) \
           <(grep -oE '^\| B(5[7-9]|6[0-9]|7[0-8]) \|' docs/Decisions-Needed.md | grep -oE 'B[0-9]+' | sort -u); done
== docs/Screen-Inventory.md: B64 B69 B70 B72 B73 B74 B78
== docs/Flows.md:            B64 B67 B68 B77
== docs/Microcopy.md:        B57 ... B78 (all but B71)
== docs/Phase-1-Amendments.md: B57–B62 B67 B68 B72–B78
```

Read against each file. In Flows, B64, B67 and B68 are cited inside a `PROVISIONAL:` group ("`PROVISIONAL: B63`, `B64`"); B77 is described ("fixed circle drawing") but never labelled, which is minor. Microcopy and Amendments do not touch most of these questions. **Screen-Inventory is the gap:** B70 (S-14), B72 (S-02 and S-12 rows), B73 (S-03, S-13, S-05), B74 (S-06, S-16) and B78 (S-01) appear nowhere in it (`grep -c` = 0 for B70, B73, B74, B78; B72 only in the OQ-51, OQ-52 notes). That is **V8**.

**2. Banned-mechanic tokens in the 434 added lines** (`git diff -U0 a3b9a4f..7ad6990 -- docs CLAUDE.md`, excluding Status and the rubric), grepping `countdown|time left|remaining|ends in|minutes? left|\bnew\b|badge|\bdot\b|remind|notif|streak|progress|count|on this day|anniversary|setInterval|animat|runs? down|you have [0-9]+`, with "no …", "never …" and "must never" lines removed. No added line introduces a timer, badge, dot, streak or reminder. Two hits need reading: "anniversary" (18 lines, every VVVV line; read as V3) and Microcopy:78, "You have 15 minutes from the photo" (N3).

**3. Old-rule phrases still standing** (CLAUDE.md, docs except reviews, preview, agents; lines with a dated pointer removed):

```
'move to their next slot together' → Master-Prompt.md:75; Screen-Inventory.md:689
'unlock anniversar'                → Decisions-Needed.md:125 (A1); Master-Prompt.md:75; Flows.md:136;
                                     Screen-Inventory.md:191; preview/index.html:287
'rites reflections' / 'reflections, tagging' → Master-Prompt.md:73; Build-Plan.md:108
'b11 = named'                      → Phase-1-Amendments.md:1757
'includes Reflect'                 → Flows.md:131; preview/index.html:282
```

The rubric's own old lines (R-071, R-092, R-139, R-141, G-12) carry `Updated` lines and are history by R-172. The rest is **V9**.

**4. Fixture arithmetic** (VVVV: slot k = [c + k years, c + (k+1) years), 00:00 UTC; journey windows from P1 §3.3; baseline 2026-10-25).

| Photo (journey, window) | Captured c | Reflection, slot | Slot window | In slot? | In journey year? |
|---|---|---|---|---|---|
| lantern-1 (L#1, 2021-01-01 → 2022-01-01) | 2021-03-14 | 2022-03-20 (1), 2023-03-22 (2), 2024-03-18 (3), 2025-03-24 (4), 2026-03-20 (5) | each [yyyy-03-14, +1y) | yes, 4–10 days in | yes |
| round-1 (R#1, 2022-09-01 → 2023-09-01) | 2022-11-08 | 2023-11-20 (1), 2024-11-15 (2), 2026-09-10 (3) | slot 3 = [2025-11-08, 2026-11-08) | yes | yes |
| wind-3 (W#3, 2023-04-02 → 2024-04-02) | 2023-04-06 | 2024-04-20 (1), 2025-05-01 (2), 2026-04-15 (3) | [yyyy-04-06, +1y) | yes | yes |
| lantern-5 (L#5, 2025-01-01 → 2026-01-01) | 2025-06-21 | 2026-07-05 (1) | [2026-06-21, 2027-06-21) | yes | yes |
| lantern-2 (L#2, 2022) | 2022-01-10 | 2023-01-21 (1) | [2023-01-10, 2024-01-10) | yes | yes |
| lantern-3 (L#3, 2023) | 2023-01-12 | 2024-01-27 (1) | [2024-01-12, …) | yes | yes |
| wind-4 (W#4, 2024-04-05 → 2025-04-05) | 2024-04-15 | 2025-04-26 (1) | [2025-04-15, …) | yes | yes |
| hands-2 (H#2, 2024-06-03 → 2025-06-03) | 2024-06-14 | 2025-06-29 (1) | [2025-06-14, …) | yes, and before the 06-18 birth highlight | yes |
| hands-3 (H#3, 2025-06-03 → 2026-06-03) | 2025-06-12 | 2026-06-27 (1) | [2026-06-12, …) | yes | yes |
| round-2 (R#2, 2023-09-04 → 2024-09-04) | 2023-09-10 | 2024-09-22 (1) | [2024-09-10, …) | yes | yes |

Round-1: at baseline slots 1 to 3 have opened (slot 4 opens 2026-11-08), so depth 3 is the most it can hold. Every reflection is still 7 days after its reveal finished (§3.7), so each is written after the photo was set Public.

**"Reflection left" audiences** (Amendments §13.4.1 against §13.1, event-time B48: a friend whose current friendship began strictly before the event; fr-2 was removed, so it never counts):

- lantern-1: Wind from 2021-03-17, so all 5. Hands from 2023-06-11, so 2024, 2025, 2026: 3. Round from 2025-10-02, so 2026-03-20 only: 1. Matches, and is unchanged by the move.
- lantern-2 (2023-01-21): Wind only. lantern-3 (2024-01-27): Wind, Hands. lantern-5 (2026-07-05): Wind, Hands, Round. All match.
- round-1: Round's only counting friendship is fr-4 from 2025-10-02, so only 2026-09-10 reaches Lantern. round-2 (2024-09-22): nobody. Both match.
- wind-3, wind-4: Lantern; Hands is a friend from 2026-11-14, after every event. hands-2, hands-3: Lantern; Wind from 2026-11-14, after both. All match.

No moved date falls on a friendship act's date (§13.1, "Clear of P1's fixed instants" updated for 2023-03-22). **Pass.**

One test-design defect: see N4 (§16.1 check (1) cannot run on the loaded fixture).

---

## Findings

### V1. B74 gives a friend a sealed journey's type and dates

- **Check:** R-008 (anyone but the owner learns only that a sealed journey exists); new R-201
- **Where:** `Decisions-Needed.md:109` (B74); `Flows.md:626`; against `Screen-Inventory.md:216` (S-06 `sealed`: "Others: exists only"), FS §20 I (`Functional-Spec.md:279`), FS §20 T (`:296`, "after unlock"), `CLAUDE.md:106`
- **What is wrong:** B74 says "A journey with no photo this reader can see is not shown on the path at all to a public reader; to a friend it shows as a place with its type and dates only". A sealed journey is a journey with no photo any reader can see. Read as written, B74 shows a friend the sealed journey's type, commit date and unlock date, and hides from a public reader the bare existence S-06 allows. The fix is one word, "unlocked" journey, but it is not there, and Flows repeats the row as written.
- **Why it breaks the rule:** "Nothing leaks from a sealed year". The type and dates of a sealed journey are exactly what R-008 lists. A builder implementing the default literally ships the leak.
- **How serious for the prototype:** high. It is a supervisor default proposed for the user's one-go OK, and a builder would build it as worded.

### V2. "Always after unlock" is false, and `add_reflection()` lost its unlock guard

- **Check:** R-003 (no reflection of a sealed journey is readable or written before unlock), CLAUDE.md "Sealed content is unreadable"; new R-198, R-199
- **Where:** `Phase-1-Amendments.md:2164` ("*c* + 1 year ≥ `unlocks_at`"), `:2163` (reads `captured_at` as a definer; refuses only slot 0); `Functional-Spec.md:98` ("which always falls after unlock"); FS §20 VVVV (`:395`, "Every slot opens after unlock"); against `Phase-1-Proposal.md:73–74` (`committed_at` = `app_now()` at Commit, any time; `unlocks_at` = `committed_at` + 12 months) and `:117`
- **What is wrong:** slot 1 opens at 00:00 UTC on the photo's capture date plus one year. `unlocks_at` keeps the Commit's time of day. A Commit at 14:37 UTC unlocks at 14:37 a year later, so a photo taken later that same UTC day has slot 1 open from 00:00, about 14.6 hours before its journey unlocks. The claim holds only for midnight Commits. The fixture's Commits are all at 00:00:00, so the fixture never shows the gap. The demoer's live Commit (First Light, or Lantern's next one after 2027-01-01) does.

  Under the old D9, `year_index` was computed against `unlocks_at`, so "after unlock" was enforced by the slot arithmetic itself. §16.1 replaces that arithmetic, keeps only the slot-0 refusal, and reads `captured_at` as a definer, past the seal's row security. Nothing left in the text refuses a reflection on a still-sealed photo. Its accepted-or-refused answer would also tell a caller holding a sealed photo's id when that photo was taken.
- **Why it breaks the rule:** sealed content must be unreadable and unwritable "in code, not by convention". The model relies on a date invariant that does not hold.
- **How serious for the prototype:** medium. It needs a non-midnight Commit and a crafted call, but it is a hole in the data layer that the Phase 3 tests would be written around the false invariant. Fix in the text: `add_reflection()` also refuses while `app_now() < unlocks_at`, stated on its own, and FS §8 and VVVV drop "always".

### V3. The way to Reflect on its anniversary: an unsettled mark, now arriving photo by photo

- **Check:** R-095, R-096, R-186 (no way appears or disappears because of content), FS §20 VVVV ("Nothing marks a slot opening: no dot, count or notice"); new R-200
- **Where:** `Screen-Inventory.md:451` (S-17 "Leads to: Reflect S-14 (owner)", with no state), `:383` (S-14: "closed until the photo's first anniversary"); `Flows.md:441` ("If this photo's current slot is open and holds no reflection, the owner may write one"), `:454` ("Between unlock and a photo's first anniversary it can be read, not reflected on"); `Phase-1-Amendments.md:2167` ("no reader returns 'open slots' for anyone but the owner's own Reflect screen")
- **What is wrong:** three things.
  - **(a) The way is never described per state.** No doc says whether S-17's way to Reflect is present, and the same, before the slot opens and after a reflection fills it. The natural build is a way that appears on the anniversary and vanishes once used. That is a "mark that a slot opened" in all but name, the same shape that B76 and R-194 rule out for the dismiss way and the requests way.
  - **(b) VVVV makes the shape worse.** The old D9 opened every slot of a journey on one day a year. Now a journey's photos become reflectable one by one, on each day a year after they were taken. That is an "on this day" mechanic: a reason to open the app any day, which "We want you here less" rules out.
  - **(c) An undefined reader.** §16.1 mentions an "open slots" reader for the owner's own Reflect screen that is defined nowhere. A reader that lists photos with an open, unwritten slot is a to-do list. Its length is a count.
- **Why it breaks the rule:** rule zero. The docs leave a banned-list question undecided, and the strictest reading (the way looks the same in every unlocked state, or the question goes to the user) is not stated.
- **How serious for the prototype:** medium to high. This is the single most likely place for a builder to add an engagement mechanic by reflex. It needs a default from the supervisor, and arguably a word from the user, since it shapes the ritual.

### V4. Who receives "path crossed": the docs disagree, and the built reading lets the person crossed tell

- **Check:** R-146, R-197, FS §20 NNNN ("No one can tell that they are on someone else's rings"); new R-208
- **Where:**
  - "subject left out": `Phase-1-Amendments.md:1739` (§13.4.3: "always unnamed, which is the last column below"; the last column is "If the subject were left out (not built)") and `:2081` (§14.4: "§13.4.3's 'would-be' column is now what is built")
  - "subject included": `:2059` (§14.1 changes only what the row returns), `Screen-Inventory.md:257`, `Flows.md:514` ("a crossed person who is a friend receives the same unnamed line as everyone else"), R-146's 2026-11-10 update; the counts at `Phase-1-Amendments.md` §13.4.1 (13 / 9 / 5 / 2 / 0) also assume it
  - stale: `:1757` (§13.4.4, "as built, `b11 = named`", no pointer)
- **What is wrong:**
  - **The docs disagree.** Two lines of Amendments say the subject is left out of the audience; §14.1, SI, Flows, the rubric and the fixture counts say the subject is included. "Unnamed" (NNNN (a)) and "the subject left out" (the alternative raised under E3 (a)) are two different things; §13.4.3 and §14.4 treat them as one. Under "left out", §13.4.1's counts would be 8 / 6 / 4 / 2 / 0.
  - **The "included" reading leaks in the fixture's own case.** §13.4.3's first row has Lantern #1 and #2's crossings reaching **Wind alone**. Wind is Lantern's only friend at the time, and the only user tagged in each. At the finish, Wind receives "Steady Lantern launched their journey." and one "Steady Lantern's path crossed with someone else's." She can read 4 of the 6 Lantern #1 photos of herself (3 Network, 1 Public; P1 §3.4). One crossing, at the moment the photos of her become readable, is a system signal that someone in them was tagged. Together they let her tell she is on Lantern's rings. §14.2's "The person crossed cannot tell it was them" overstates it: recognising yourself is the photo, but the line is the app.
  - **The wording adds to it.** Microcopy M-18's "someone else's" reads, to the person crossed, as "not you".
- **Why it breaks the rule:** NNNN is about whether a person can tell, not only about a name in a payload. Leaving the subject out closes this path; including them keeps it open. The user ruled "unnamed", not which audience, so this is a product question, not a doc fix.
- **How serious for the prototype:** medium. The Phase 3 test expectations differ by reading, and the leak shows on the first fixture user anyone tries. **For the user** (E3 (a), second half): should the person crossed receive the line at all?

### V5. The block term misses `ring_count()` and `has_journey_underway()`

- **Check:** B64 ("To them the blocker looks the same as a name that does not exist"), CLAUDE.md "Enforce rules in code"; new R-202
- **Where:** `Phase-1-Amendments.md` §15.3 table (`:2111–2125`); against §11 `ring_count(profile_id uuid)` (`:1136`, FS §20 CCC, "the same for every viewer") and `has_journey_underway()` (`:19`, `:1395`)
- **What is wrong:** §15.3 adds `block_between()` to the photo, overview, journey, announcement, Positivity Feed, `user_rows()` and request readers. It does not add it to the two readers that answer about a profile by id: the ring count, and whether a sealed journey is underway. A blocked person who holds the blocker's id can call `ring_count(blocker)`. Holding the id is easy: their own `layer` rows and old payloads carry it. They get a number where an unknown id gets none. That is the "blocked" answer B64 promises never to give.
- **Why it breaks the rule:** B64's "byte for byte" must hold at the data layer, not only on the screens that are reached through `user_rows()`.
- **How serious for the prototype:** low to medium. It needs a crafted call, but the fix is two rows of the table, and §15.5 has no case for it.

### V6. The block is detectable in ways the leak review does not list, and one screen is undecided

- **Check:** B64, R-186, rule zero; new R-203
- **Where:** `Phase-1-Amendments.md:2132` (§15.4: "learns of the block only by absence … That is the friendship ending, which removal already allows"); `:2107` (§15.2 step 3); `Screen-Inventory.md:415` (S-16 reached from Layers S-07); `Decisions-Needed.md` B64, B69
- **What is wrong:** four tells beyond "absence of a friendship".
  - **(a) Their own map, and an undecided screen.** Under B69 the blocked person's own map S-07 still holds the blocker by name (FS §20 G), and its way to S-16 now opens an "unknown user". A person on your own map cannot be unknown. What S-07 shows or links for a blocked pair, both for the blocker's map and for the blocked person's, is stated nowhere.
  - **(b) Their outgoing request vanishes.** A blocked sender's outgoing request leaves their list without their act (§15.2 step 3). Under B44 that never otherwise happens, since a decline looks like pending.
  - **(c) Their feed changes.** Earlier announcements from the blocker vanish from their feed.
  - **(d) Their own tags.** Their own person tags of the blocker, on their own photos, still name someone who "does not exist".
- **Why it breaks the rule:** (b) to (d) are the Instagram reference's own tells, and acceptable if said so. But §15.4 claims otherwise, and (a) is a behaviour no doc settles. Rule zero: raise it, do not pick. It touches the rings: an S-07 that drops or unnames the blocker would change the map, which B69 says a block does not do.
- **How serious for the prototype:** low to medium. The demoer will block from a profile and then open Layers, so (a) will be met at once.

### V7. `dismiss_highlight()` is a new reader of sealed rows that the closed lists do not include

- **Check:** R-138 ("no call other than capture and starting a highlight works it out or reports it"), R-156 (the set must equal {`capture`, `start_highlight`, `highlight_open`, `highlight_rows`}); new R-205, R-209
- **Where:** `Phase-1-Amendments.md:2172–2177` (§16.2); `:336` (§4 item 1's list, unchanged); `Rules-Rubric.md` R-156, R-138
- **What is wrong:**
  - **It reads sealed rows.** During the sealed year, `dismiss_highlight()` reads the highlight row and the journey's photo rows (`highlight_id`), and answers on whether any photo is in the highlight. `start_highlight()`, `capture()` and `highlight_open()` now also read the new `highlight_dismissal` table.
  - **The lists are not updated.** §16.2 says the function "joins §4 item 1's list", but the list at `:336` was not edited, R-156's set was not updated, and R-138's "only capture and start-highlight" now fails as written.
  - **After unlock, unstated.** Not said: whether the owner's after-unlock reader (`highlight_rows()`, B24) returns a dismissed highlight, and with which end. Its stored `ends_at` would still read start + 24 hours.
- **Why it breaks the rule:** the seal is enforced by closed lists of the only functions that may touch highlight rows. A function added to the model and not to the lists is how a stray reader gets in (R-156's own reason for existing). What the owner learns (zero photos or some) is their own act, so this is not yet a leak. It is an unenforced rule.
- **How serious for the prototype:** low now (on paper), certain to fail R-156's scan in Phase 3.

### V8. Screen-Inventory does not carry B70, B72, B73, B74 or B78

- **Check:** R-150 step 1 (auto check 1)
- **Where:** `Screen-Inventory.md`:
  - S-01 (`:71`): no B78
  - S-02 and S-12 state rows: B72 only in OQ-51 and OQ-52 at `:829–830`
  - S-03, S-13, S-05: no B73
  - S-06 (`:197`) and S-16 (`:410`): no B74; S-16 still "Leads to: Walking a path S-06" in every state, which B74 contradicts for a person with nothing to show
  - S-14 (`:373`): no B70
- **What is wrong:** the defaults were carried into Flows (commit 2822ab3) but not into the inventory a builder builds screens from.
- **How serious for the prototype:** low to medium. A builder working from SI builds the old screens, including a path way for a person with nothing to show.

### V9. Stale lines still state the old rules, and settled questions are called open

- **Check:** R-165 (every dated ruling is carried; no build doc keeps a replaced behaviour or calls a decided question open)
- **Where and what:**
  1. `Master-Prompt.md:73` (the reveal "writes reflections") and `:75` ("All photos of a journey move to their next slot together, on the journey's unlock anniversary"). The brief was kept in step with §20 D in 2026-10; it is now wrong.
  2. `Build-Plan.md:108`: "Reveal — … reflections, tagging, …".
  3. `Flows.md:131` and `:136`, the opening map: "Reveal (5) --- includes Reflect (6)" and "every unlock anniversary: Reflect (6) again". The regenerated preview carries the same, at `preview/index.html:282`, `:287`. This is the first thing a new reader meets.
  4. `Screen-Inventory.md:689` (OQ-1, says §20 D wins), `:191` (S-05 `later-years`, "On the unlock anniversary"); `Decisions-Needed.md:125` (A1, §20 D); none has a pointer to VVVV.
  5. `Phase-1-Proposal.md:117`: "Insert-only, owner only, any time after unlock". Now true only from each photo's first anniversary. Amendments §16.1 cites this very line.
  6. `Phase-1-Proposal.md:368`: §3.7's "Slot 1" column still holds the old unlock-based windows under the header "Slot 1". The note says so, but a test author reading the table reads a wrong window.
  7. `Functional-Spec.md:388`, `:389`, `:393`: PPPP, QQQQ and UUUU still say "being clarified with the user (Decisions-Needed E7 / E8 / E9)", with no pointer to VVVV, WWWW and XXXX, which settled them.
  8. `Flows.md:244`: the camera bullet keeps "Gap: … SI OQ-51, not picked here" and "Gap: a press on the way out … FQ-10" beside the B72 that settled both. `Flows.md:397`: "what act saves a choice: FQ-8", after FQ-8 was decided in the same sentence.
  9. `Phase-1-Amendments.md:3`: the status line says "MMMM (blocking) is carried in §15, to come" and does not mention §16. §0 Summary has no rows for §14, §15 or §16, though §15 and §16 are model changes.
  10. `Phase-1-Amendments.md:1757`: §13.4.4 "as built, `b11 = named`" (also under V4).
  11. `Decisions-Needed.md:112` (B77) cites `Art-Direction.md` "§7.x", a placeholder number (`Art-Direction.md:386`).
- **How serious for the prototype:** low each. Items 1 and 3 together are the two places a new reader starts, and both still teach the old ritual.

---

## Notes (not violations)

- **N1. B75 sends a Positivity Feed reader from one photo straight into the path**, bypassing the profile. RRRR says a feed line leads to the profile only. Whether the Positivity Feed is "the feed" under RRRR is the user's call; B75 is already marked for the user's OK. Worth naming it to the user as that question.
- **N2. Dismiss and start can cycle.** A highlight can be started and dismissed any number of times before a photo, each time given back. Not a banned item. It does mean M-05's "keep it for later" is unbounded, which is fine, but the copywriter should not imply a limit.
- **N3. Microcopy M-08's "You have 15 minutes from the photo."** It is fixed and true at every moment, so XXXX holds. But "You have …" is the voice of time left, and it is on screen through the whole window. "A page can be added up to 15 minutes after the photo." says the rule without addressing the user's remaining time. For the copywriter.
- **N4. §16.1 check (1) and R-121's updated how-to-check cannot run on the loaded fixture.** They reflect on lantern-5 at 2026-06-20 and 2026-06-21. The clock only moves forward (O1, `clock_jump(interval > 0)`), and lantern-5 already holds its fixed slot-1 reflection of 2026-07-05. The check needs a throwaway copy replayed only to before 2026-06-21, or another photo. R-198 says so.
- **N5. B78's wording has two readings.** "Not offered until a type is picked" (hidden) against "Instagram-style disabled button" (greyed). Not a banned item, since nothing sealed is shown, but pick one.
- **Process (for the record).** The supervisor rewrote R-121's statement inside an `Updated` line. The rubric's rule is to supersede, not rewrite (R-172, "How the rubric grows"). This audit marks R-121 superseded by R-198 and keeps the supervisor's line as history.

**Weakest point after the fixes above:** R-200 (V3) is a review check on a screen that does not exist yet. Until the supervisor or the user settles how the way to Reflect behaves, the most natural build is a marker, and no auto check can catch it.

---

## Rubric additions

R-198 to R-209 added, each under its area:

- R-198: per-photo slots (area 11); supersedes R-121
- R-199: no writer accepts on a sealed photo, by its own unlock test (area 1)
- R-200: nothing marks a slot opening; no open-slots list (area 8, Provisional)
- R-201: "nothing visible" defaults never sweep in a sealed journey (area 1)
- R-202: the block term covers every id-taking reader (area 5)
- R-203: block effects, unblock, and the pair's own screens stated (area 5)
- R-204: S-25 (area 5)
- R-205: the highlight dismissal (area 3)
- R-206: feed lines lead to the profile only (area 7)
- R-207: no gap in a reflection stack (area 8)
- R-208: one stated audience per announcement, counts recomputed (area 13)
- R-209: closed function lists updated with the model (area 13)

`Updated` lines on R-121 (superseded by R-198), R-138, R-146 and R-156. R-140's 2026-11-10 `Updated` line, which the supervisor had placed after the area 8 separator, was moved back under R-140 with its text unchanged.

Banned-list coverage additions:

- "No streaks, counters": R-200, R-204, R-207
- "No re-engagement notifications": R-200
- "Nothing leaks from a sealed year": R-199, R-201, R-205
- "No layer is ever shown": R-202, R-203

No check renumbered or removed.

## Report
- Files changed: `docs/reviews/2026-11-10-rules-supervisor-carriage.md`, `docs/Rules-Rubric.md`
- Findings: 9 violations, 5 notes.
  - V1 (R-008, R-201): `Decisions-Needed.md:109`, `Flows.md:626`. B74 shows a friend a sealed journey's type and dates.
  - V2 (R-003, R-198, R-199): `Phase-1-Amendments.md:2163–2164`, `Functional-Spec.md:98`, `:395`. The "always after unlock" claim fails for non-midnight Commits, and `add_reflection()` has no unlock guard.
  - V3 (R-095, R-096, R-186, R-200): `Screen-Inventory.md:451`, `:383`, `Flows.md:441`, `:454`, `Phase-1-Amendments.md:2167`. The way to Reflect is unstated per slot state, and the open-slots reader is undefined.
  - V4 (R-146, R-197, R-208): `Phase-1-Amendments.md:1739`, `:2081` against `:2059`, `Screen-Inventory.md:257`, `Flows.md:514`. Docs disagree on the "path crossed" audience, and the included subject can tell (Wind, Lantern #1 and #2).
  - V5 (B64, R-202): `Phase-1-Amendments.md:2111–2125`. The block term misses `ring_count()` and `has_journey_underway()`.
  - V6 (B64, R-186, R-203): `Phase-1-Amendments.md:2132`, `:2107`, `Screen-Inventory.md:415`. Four unlisted tells; S-07 under a block is undecided.
  - V7 (R-138, R-156, R-205, R-209): `Phase-1-Amendments.md:2172–2177`, `:336`. `dismiss_highlight()` is not in the closed lists.
  - V8 (R-150): Screen-Inventory S-01, S-02, S-12, S-03, S-13, S-05, S-06, S-16, S-14. B70, B72, B73, B74, B78 not carried.
  - V9 (R-165): `Master-Prompt.md:73`, `:75`; `Build-Plan.md:108`; `Flows.md:131`, `:136`, `:244`, `:397`; `preview/index.html:282`, `:287`; `Screen-Inventory.md:191`, `:689`; `Decisions-Needed.md:125`, `:112`; `Phase-1-Proposal.md:117`, `:368`; `Functional-Spec.md:388`, `:389`, `:393`; `Phase-1-Amendments.md:3`, `:1757`. Old rules and settled questions still stand.
- Rubric additions: R-198, R-199, R-200, R-201, R-202, R-203, R-204, R-205, R-206, R-207, R-208, R-209; `Updated` lines on R-121 (superseded), R-138, R-146, R-156
- Verdict: FAIL
