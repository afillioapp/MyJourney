# Rules audit: Phase 1 docs, round 7 (changes since 796333c)

Date: 2026-10-31. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-168 after this audit).

**Target:** `git diff 796333c..HEAD -- docs`, seven commits from 4ae4858 to 5451b4e. The diff covers:

- `Functional-Spec.md` §20 WW–HHH: new user rulings, at FS:330–341, and the UU rewording at FS:325
- `Phase-1-Amendments.md` and `Phase-1-Proposal.md`: lead-tech carried SS–DDD and B10, with tests (796a03d, 1aad170)
- `Screen-Inventory.md`: ux carried JJ–DDD and B10 (8c429e1, 150608d)
- **Supervisor edits in 5451b4e (EEE–HHH):** Amendments `:485–486` (§6), the OQ-30 to OQ-32 cells (`:641–643`), Screen-Inventory S-02 `:94`, OQ-50 `:711`, FS:338–341 and `Status.md:138`
- `Decisions-Needed.md` B9 and `Status.md`

Previous audit: `docs/reviews/2026-10-31-rules-phase-1-r6.md` (FAIL: V1–V4, N1–N6).

**Context:** no code exists, and `graphify-out/` is absent, so no graph queries were run.

**Verdict: FAIL.** There are 2 confirmed violations:

- **V1:** the Amendments body still calls HHH and the OQ-31 and OQ-32 questions open, and three status lines stop at DDD.
- **V2:** HHH is carried only in Amendments §6. The Proposal and the note-step screen S-12 do not carry it, and the build check has no case for it.

All four r6 violations (V1–V4) are resolved. Both new violations are in lines the supervisor wrote or should have updated in 5451b4e.

---

## Auto checks run

```
$ git diff --stat 796333c..HEAD -- docs
 Decisions-Needed 2, Functional-Spec 17, Phase-1-Amendments 227, Phase-1-Proposal 26, Screen-Inventory 136, Status 9

$ git diff -U0 5451b4e~1..5451b4e -- docs | grep '^@@'        (the supervisor's EEE-HHH commit)
 Functional-Spec  +338..341
 Phase-1-Amendments  @@ -485 +485,2   (adds :485 GGG, :486 HHH)   @@ -640,3 +641,3  (OQ-30..32 cells)
 Screen-Inventory    @@ -94 +94   (S-02 twice-failed row)   @@ -711 +711  (OQ-50 answer)
 Status +138
 -> S-12 (Screen-Inventory :327-341) is not touched. Phase-1-Proposal is not touched.

$ grep -nE '^- \*\*(PP|...|HHH)\.' docs/Functional-Spec.md
 PP 320, QQ 321, SS 323, TT 324, UU 325, VV 326, WW 330, XX 331, YY 332, ZZ 333,
 AAA 334, BBB 335, CCC 336, DDD 337, EEE 338, FFF 339, GGG 340, HHH 341
 "### Still open" 343 (items 345, 346); "## 21" 350; "A time control" 354

$ git diff 796333c..HEAD -- docs ':!docs/reviews' | grep '^+' | grep -ioE "streak|badge|counter|progress|remind|notif|like|
  rank|leaderboard|level|unread|retake|try again|press again|countdown|timer|thumbnail|new marker|dot"
  Every hit is a refusal ("never a retake", "no 'try again'", "no stored counter", "An unread dot ... "
  in a never-list), a SQL term (row-level, statement-level) or a quotation in a never-list. No banned element is added.

$ R-165 (1) as written, F = Phase-1-Amendments.md (every OQ-1..OQ-32 except 3, 5, 12, 13, 14 is "Settled")
  hits at 631, 632, 633, 637, 639: history in other OQ rows ("was OQ-n", "Left open by PP: OQ-26"), pass
  638 (OQ-27 cell): "Left open: OQ-31, OQ-32"  -> both now settled (FFF, GGG, HHH): stale
$ same scan, words widened to "not ruled|open from|open:" (now in R-165's Updated line)
  484: "whether the note step retries is not ruled (OQ-32)"          -> HHH rules it (V1)
  572: "Open from DDD: OQ-31, OQ-32 (§8)."                           -> FFF, GGG, HHH settle both (V1)
  643: "...is not ruled **Settled 2026-10-31, FS §20 GGG (a) and HHH (b)**" -> own row, question text: pass
$ grep -niE "not settled|not picked|waits? on|none yet|confirm|still open|not ruled" docs/Phase-1-Proposal.md -> none
$ same on Screen-Inventory.md outside its Open questions (579-714): only state names ("highlight open",
  "slot k is open"), the "Still open — can wait" citations at 572-573, and revision-log history. Pass

$ R-165 (2), status lines
  Phase-1-Amendments.md:3   ends "§20 AAA–DDD ... New for the user: OQ-30, OQ-31, OQ-32"   (no EEE-HHH)
  Phase-1-Amendments.md:7   "§20 Q–DDD (`FS:290–337`)"
  Phase-1-Amendments.md:13-42 (§0 summary): rows through DDD; none for EEE, FFF, GGG, HHH
  Phase-1-Proposal.md:3     "§20 Q–DDD"

$ grep -n "EEE\|FFF\|GGG\|HHH" docs/*.md
  Functional-Spec 338-341; Amendments 485, 486, 641, 642, 643; Screen-Inventory 94, 711; Status 138
  -> HHH: Amendments :486, :643 and SI :711 only. Nothing in Phase-1-Proposal.md, nothing in S-12

$ sed -n 327,341p docs/Screen-Inventory.md | grep -iE "HHH|strip|guard|refus|Spec:320|Spec:321"  -> no match

$ grep -noE "Spec:3[4-6][0-9](–3[4-6][0-9])?" docs/Screen-Inventory.md
  40, 517, 522: "Spec:346–356" (§21 is now 350–360); 572: "Spec:341" (now 345); 573: "Spec:342" (now 346)
$ Rules-Rubric R-116: "now FS:339 (heading FS:335)"  -> now FS:354 (heading FS:350); Updated line added

$ R-150 step 1 (labels) on the changed lines
  B10: Amendments :36, :786 and P1:168 carry `PROVISIONAL: B10`;  B11: :786;  B2: :780;  B4: :234, P1:65
  B9 (e): DN:28 now "decided (BBB)"; Amendments :800 and SI :275, :277 drop the label to match. Pass
$ grep -n "count(\*)" .claude/agents/lead-tech.md -> 30 (Amendments :825 now cites it correctly; r6 N4 closed)
```

---

## Status of r6 findings

| r6 item | Status | Evidence |
|---|---|---|
| V1: TT not carried | **Resolved** | Amendments `:35`, `:774` (`joined_at` only on the viewer's own row), `:793`, tested `:887`, `:892`, `:895`. P1 `:63`. SI `:52`, `:186`, `:215`, `:265`, `:417` |
| V2: SS not carried | **Resolved** | Amendments `:34`, `:787`, `:794` (policy changed, predicate not executable), tested `:888`, `:896–902`. P1 `:48` (h), `:164`. SI `:42`, `:417` |
| V3: B10 dropped | **Resolved** | Amendments `:36`, `:786`, `:795`, `:829`; the rule oracle catches the pre-r6 rule (`:894`: 48 / 14 / 34). P1 `:168`. SI `:244`, `:258` |
| V4: VV not carried | **Resolved** | Amendments `:472–479`, evidence `:526–539`. P1 `:91`. SI S-02 `:93` |
| N1: SS against the inference paths (G-23) | **Resolved by the user** | FS §20 ZZ (`FS:333`), WW (`FS:330`), CCC (`FS:336`). G-23 is now closed by a `Decided` line in the rubric |
| N2: UU against B10 | **Resolved** | FS:325 reworded ("As the model carried it"). Amendments `:786` applies UU to the actor and B10 to everyone else. SI `:244` |
| N3: VV's retry at a later instant | **Resolved by the user** | FS §20 XX (`FS:331`) and AAA (`FS:334`). Amendments `:477`: one transaction, judged and stamped at the press instant. The R-160 `Open` note is closed by a `Decided` line |
| N4: stale lines | **Mostly resolved, then partly stale again** | Resolved: SI `:55–57` (JJ, LL); P1:48 (a) "through the readers"; Amendments `:825` now cites `lead-tech.md:30`; `Status.md:36` R-001–R-165; B11 labelled at `:786`. Stale again after 5451b4e: P1:3, Amendments `:3` and `:7` (V1), and SI's §21 citations (N4 below) |
| N5: highlight name scan | **Resolved** | Amendments `:273`, evidence `:386–400` |
| N6: weakest points | **Partly resolved** | Feed sort key: resolved by BBB (`:800`, `:819`). Highlight UPDATE path: resolved (insert-only, `:274`; P1:45). Still open: C17 (`:624`), the highlight-by-date residual (`:281`), RR (`:760`), OQ-3 (`:614`), OQ-12 (`:623`) |

---

## Coverage of FS §20 WW–HHH in the build docs

| Ruling | Amendments | Proposal | Screen-Inventory | Carried? |
|---|---|---|---|---|
| WW | §3 `:234`, §0 `:38` | 65 | 52, 171, 409, 412, 548, 602 | Yes |
| XX | §6 `:472–479`, evidence `:526–539` | 91 | S-02 `:93` | Yes |
| YY | §11 `:774` | 62 | 51, 179, 322, 415 and others | Yes |
| ZZ | §11 `:787`, `:794` | 48 (h), 164 | 42, 285, 415, 438 | Yes |
| AAA | §6 `:472`, `:477`, evidence `:545–547` | 91, 180 | S-02 `:93`, OQ-48 | Yes |
| BBB | §11 `:800–803`, `:819`; tested `:911–917` | 117 | S-09 `:277`, `:285` | Yes |
| CCC | §11 `:804–809`, §3 `:234`; tested `:918–939` | 65, 164, 179 | S-16 `:403`, `:409`, `:412–417` | Yes. Only the general counter ban covers a numeral on S-16: N3 |
| DDD | §6 `:480–484`; tested `:541–570` | 91, 180 | S-02 `:93–94` | Yes |
| EEE | OQ-30 cell `:641` only ("no change") | (none needed) | **Nothing**; OQ-44 `:688` not reconciled | Data side: no change needed. Screen side: N2 |
| FFF | OQ-31 cell `:642` only; `:483` still calls the gap "a residual (OQ-31)" | (none needed) | (none needed) | Yes, in effect. `:572` still calls OQ-31 open: V1 |
| GGG | §6 `:485` | (none needed: P1:91 has "both calls roll back") | S-02 `:94`; OQ-50 | Yes, but S-02 `:94` contradicts itself: N1 |
| HHH | §6 `:486`; **`:484` says "not ruled"** | **No** (P1:105, P1:180) | **No** (S-12 `:327–341`); only OQ-50 `:711` | **No: V1, V2** |

---

## Findings

### Confirmed violations

**V1. The Amendments body still calls HHH, OQ-31 and OQ-32 open, and three status lines stop at DDD.** Rubric: R-165 (1) and (2), R-134. Blocks Phase 3, because the Amendments are the Phase 3 build source.

- **Where:**
  - `Phase-1-Amendments.md:484`: "whether the note step retries is not ruled (OQ-32)". The supervisor added HHH two lines below (`:486`) and left this line as it was.
  - `:572`: "Open from DDD: OQ-31, OQ-32 (§8)."
  - `:638`, OQ-27 cell: "Left open: OQ-31, OQ-32".
  - `:641`, OQ-30's Blocks column still reads "`reflection_rows()` columns for a public reader (Phase 3)", although the cell records EEE as "inference allowed; no change".
  - Status lines: `:3` ends at AAA–DDD and lists OQ-30, OQ-31 and OQ-32 as "New for the user". `:7` reads "§20 Q–DDD (`FS:290–337`)". The §0 summary (`:13–42`) has no row for EEE, FFF, GGG or HHH. `Phase-1-Proposal.md:3` reads "§20 Q–DDD".
- **What is wrong:** FS §20 FFF (`FS:339`), GGG (`FS:340`) and HHH (`FS:341`) settle OQ-31 and OQ-32. EEE (`FS:338`) settles OQ-30. The build source still says, in four places, that the questions are open or that they block Phase 3.
- **Why it breaks the rule:**
  - R-165: "No build doc calls a decided question open".
  - A Phase 3 builder reading `:484` and `:572` meets two readings of the note-step path, one open and one ruled, and has to pick. That is the r6 V4 failure again, on the same path the no-retake ban protects (`CLAUDE.md:64`).
  - R-165 (1), as written in r6, missed `:484` and `:572` because "not ruled" and "Open from" were not on its word list. The list is widened in this audit.

**V2. FS §20 HHH is carried only in Amendments §6. The Proposal, the build check and the note-step screen S-12 do not carry it.** Rubric: R-165 (3), R-160 (new (4)), R-031, R-020. The data side blocks Phase 3, and the screen side blocks Phase 2 flows and Phase 4.

- **Where:**
  - `Phase-1-Proposal.md:105` (note image): "the note step first refuses ... as `capture()` does (FS §20 KK, NN, PP, QQ)". It does not mention a retry, the press instant or the double-failure path. Compare P1:91, where lead-tech carried VV, XX, AAA and DDD for the photo.
  - `Phase-1-Proposal.md:180` (§2.5 check 5): the retry and double-refusal cases are given for `capture()` only.
  - `Phase-1-Amendments.md:487` ("What the build runs"): the VV, XX and DDD cases are given for `capture()` only, and there is no HHH case. `:486` describes the note route's transaction, but no evidence block tests it. The supervisor wrote it and lead-tech has not verified it.
  - `Screen-Inventory.md` S-12 (`:327–341`): it has no row for a note image refused by the guard, retried or lost twice, and its source line (`:330`) cites none of PP, QQ, VV, XX, AAA, DDD or HHH. Only the OQ-50 answer (`:711`) says "A note image that fails twice is handled the same way on S-12 (Spec §20 HHH)", and S-12 does not say so.
  - `Status.md:138` reports HHH as carried into "Screen-Inventory S-02". HHH is about the note step, which is S-12.
- **What is wrong:** HHH: "The note step retries like capture: strip again and save once at the original instant; if it fails twice, nothing is shown and the bug is logged". As written:
  - The Phase 3 test list does not prove the retry for notes.
  - A Phase 2 or Phase 4 builder of S-12 has no line saying that a guard refusal shows nothing.
  - Nothing says what S-12 does after a lost note. One reading ends the step as after a page was taken. The other keeps the offer open inside the 15 minutes, which would let the user photograph the page again. That would be a re-shoot under C4 (`PROVISIONAL: C4`; R-020).
- **Why it breaks the rule:**
  - A decided ruling is carried in a table cell and one body bullet, but not in the build docs it bears on (R-165 (3)).
  - On S-12 a builder must decide the lost-note behaviour, which rule zero forbids. The default most builders would reach for, a "couldn't save, try again" message, is exactly what PP and HHH ban.
  - The rubric now reads HHH strictly: the step ends as after a page taken, and no route offers it again (R-160 (4)). That reading is mine, under CL:24, and needs the supervisor's confirmation. It is not a decision.

### Notes blocking Phase 3

None beyond V1 and the data half of V2.

### Notes for Phase 4+ (and the Phase 2 flows, which read the same screen rows)

**N1. Conflict, raised and not picked: DDD "the user sees nothing different" against GGG "no note offer".** Rubric: G-24 (new), R-168 (new), R-160 (3).

- **Where:** `Screen-Inventory.md:94` holds "The camera then returns as after any press, with no note offer (no S-12)". The same row's never-list bans "Any sign that this press gave no photo". `:87` and `:96` send every accepted press straight to S-12 (`PROVISIONAL: C4`).
- **Why it matters:** a missing note offer is exactly the sign the row bans. A user who notices it may press again for the same moment, which PP (`FS:320`, "nothing invites a second press") and the no-retake ban (`CLAUDE.md:64`) exist to prevent.
- **Status:** both lines are dated §20 rulings, so the build may not pick between them (CL:30). The S-02 and S-12 flows wait on the user. Phase 3 is unaffected, because the data side is the same under either reading.

**N2. EEE has not reached Screen-Inventory.** `Screen-Inventory.md:688` (OQ-44) still holds "Still open, no ID, for S-06 only: ... whether the path order itself is too much is for the user".

- EEE (`FS:338`) rules that narrowing journey dates from capture and reflection dates the reader can already see is allowed. A public reader's path order follows capture dates they already read.
- EEE may settle that remainder, but the supervisor did not record it either way. Not picked here. OQ-44 needs an answer that cites EEE, or a line saying why EEE does not reach it.
- "Journey facts after unlock" (`:42`) is consistent with EEE as worded ("never by a public reader", meaning as fields).

**N3. The ring count reaches every viewer, and only the general counter ban keeps it off the screen as a number.** Rubric: R-166 (new). This is a weakest point, not a gap.

- `Screen-Inventory.md:46` bans "No counter, progress bar, completion meter or percentage at any time" on every screen (`PROVISIONAL: B8`), so a numeral is already banned.
- S-16 (`:403`, `:412–415`) bans dates and labels on rings and "a ring presented as an achievement", but S-16 and S-05 never name the case of text beside the circle, such as "3 journeys" or "4 years".
- Since CCC, `ring_count()` returns that integer to every viewer (Amendments `:804`), so printing it is the reflexive build. It would be a counter and a comparison between users (`CLAUDE.md:69`, `:71`; FS:185).
- R-166 (4) makes this a named review check for Phase 4. Naming it on S-16 is ux's choice.

**N4. Stale lines that do not change behaviour.** Each should be fixed by its owner.

- **§21 citations:** `Screen-Inventory.md:40`, `:517` and `:522` cite "Spec:346–356 (§21)", but §21 is now FS:350–360. `:572` and `:573` cite Spec:341 and :342, but the items are now at FS:345 and :346. 5451b4e added four lines and did not move them. `:803` (the revision log) is history and passes.
- **Dates and sources:** FS:327's date note covers SS–ZZ only. AAA–HHH carry no ruling date in §20, though `Status.md:136` and `:138` give 2026-10-31. S-02's source line (`:85`) does not cite GGG (FS:340), although `:94` uses it.
- **Records:** Screen-Inventory's revision log has no entry for the supervisor's S-02 and OQ-50 edits. `Status.md:36` gives the rubric range as R-001–R-165, and it is now R-001–R-168.

**N5. Supervisor mechanism text without evidence.** Amendments `:486` describes the note route: one transaction, a savepoint, and "the 15-minute window (FS §20 K) is judged once".

- It mirrors §6's capture design, so it does not change behaviour. But it is design text written outside its owner's role and not tested.
- One edge needs a test: a note pressed at capture + 14:59 whose retry finishes after 15:00 must be accepted, because `app_now()` is frozen for the transaction.
- R-160 (4) now requires this test. Lead-tech should confirm the text and add evidence (part of V2's fix).

**N6. Weakest points carried forward.** None is a violation today.

- **C17** (Amendments `:624`): the next-unlock jump still has no default, and it shows another user's unlock date to the demoer.
- **Highlight by date** (R-151 residual, `:281`): many photos on one date can still suggest a highlight.
- **Query timing** (RR, `:760`) and **the user-settable log parameter** (OQ-31 (a), accepted by FFF, `:642`): both are accepted until real users or deploy, with OQ-12. They are recorded on R-157 and R-167.
- **The virtual transaction id in the log prefix** (`:482`) is a server counter beside a real time. It is safe only while no product role can read the log and nothing copies the log into the database. R-155 now says so.
- **R-166 (4) and R-168 are review-only.** No script can find a numeral beside a circle, or a state that holds what it bans, before Phase 4 screens exist.
- **OQ-3** (`:614`) and **OQ-12** (`:623`) are unchanged.

### Restated as asked (lead-tech's flag)

**R-160's `Open` note.** It is closed by XX (`FS:331`) and AAA (`FS:334`). The retry runs inside the press's own transaction, so it is judged and stamped at the press instant. If the highlight closes, the month turns or the journey unlocks while the retry runs, the press still lands where it would have landed, and `captured_at` is the press instant (Amendments `:473–479`; evidence `:526–539`, `:545–547`).

- **(3), double failure (DDD, GGG):** zero rows, no frame or highlight place used, no third call, nothing shown, two log lines with one transaction id. The camera returns with no note offer. "No visible difference" is held open by G-24.
- **(4), new (HHH):** the same retry for the note step.
- The `Open` note stays in place as history.

**R-155 (d), against AAA, BBB and DDD:**

- **BBB.** The Positivity Feed reader's body ends `ORDER BY r.written_at DESC, r.id` and orders by nothing else. It returns no time-typed column, and the app re-sorts by nothing.
  - The test reads the reader `WITH ORDINALITY` against a plain-SQL oracle, with a planted `captured_at` sort that must be caught (`:917`).
  - Any sort by `captured_at`, `captured_on`, a note's `written_at`, `ctid`, `xmin`, `finished_at`, `unlocks_at` or `committed_at` fails.
  - C14 (the announcement feed's order) is still provisional.
- **AAA.** A retried photo's time, date and order position are exactly those of an ordinary press at that instant. Nothing marks a photo as retried. This is added to (c).
- **DDD.** The log's real time and virtual transaction id are outside the product data and unreadable (R-167), so (a) and (b) do not reach them. No table, column or reader may copy in a log line, a transaction id or a log time.

### Checked and clean

- **`positivity_feed_rows()`** (`:800–803`): no time column; it is selected by B9 (b), (f) and the four working tags. It returns no tag or journey field, so CC, T and ZZ hold. Its order is redundant with times the reader can already read.
- **`ring_count()`** (`:804–809`):
  - Scalar, constant estimate, and the same answer for every viewer, so it reveals no place on anyone's map (R-069).
  - It moves only on `finish_reveal()`, which is proven by polling against the network's "journey launched", and three planted faults are caught (`:927–939`).
  - Nothing about a sealed journey moves it (`:929–932`).
- **The DDD log** (`:480–484`, evidence `:541–570`):
  - Fixed text and no statement.
  - The image travels as a bind parameter; superuser-only role settings keep it out of the log, and a marker test confirms it.
  - The file is unreadable by both product roles, natively and after `SET ROLE`.
  - The counterfactuals show why each setting is needed.
- **The insert-only highlight trigger** (`:274`, `:395–400`) is statement-level, so it also fires where FORCEd RLS matches no row.
- **The rule-oracle half of §11 check 3** (`:840`) answers R-158 (3) and caught the pre-r6 B10 gap (`:894`).
- **DN B9** (`DN:28`): (e) is marked decided by BBB, and (b) and (f) remain provisional and labelled.
- **No silent decision** was found in the lead-tech or ux carriage. The one gap a builder would have to fill, the end of S-12 after a lost note, is in V2.

---

## Rubric changes

**Added:**

| Check | What it covers | Comes from |
|---|---|---|
| R-166 | Another user's circle gives only a count of finished reveals: it moves only on a finish, has no date, and is drawn as rings, never as a number | FS §20 CCC, WW, ZZ; Amendments §11 checks 2 and 5 (proposed for numbering); N3 |
| R-167 | The guard-bug log holds no image, id, app time or statement; no product role reads it; it never enters the product data; the FFF residual | FS §20 DDD, FFF, HHH; Amendments §6 `:487` (proposed for numbering) |
| R-168 | No screen state holds what its own never-list, or another state of the same screen, bans; a forced contradiction goes to the user | N1 (a new kind of finding: `Screen-Inventory.md:94`) |
| G-24 | DDD "nothing different" against GGG "no note offer" | N1 |

**`Decided` lines added:**

- XX and AAA (closing the `Open` note), DDD and GGG, and HHH on R-160
- BBB, AAA and DDD on R-155
- EEE on R-152
- WW on R-161
- ZZ and CCC on R-162
- ZZ, WW, CCC and EEE on G-23, which is now closed

**`Updated` lines added:**

- R-116 (§21 now at FS:350; "A time control" at FS:354)
- R-160 ((3) restated; new (4) for the note step)
- R-161 and R-162 (the implementation is now specified)
- R-165 (wider word list, run also on the Proposal and the Screen-Inventory body, and new (4): an OQ answer that names a screen must be matched by that screen)

**Other changes:**

- The banned-list coverage rows are extended: R-166 under "counters" and "ranking", and R-167 under "Nothing leaks", plus one new paragraph.
- A header line is added.
- **Nothing was renumbered or removed.** The only changed lines are the three coverage rows, each kept whole with text appended.
