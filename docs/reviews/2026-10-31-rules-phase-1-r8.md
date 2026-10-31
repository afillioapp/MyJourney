# Rules audit: Phase 1 docs, round 8 (changes since 04d66c3)

Date: 2026-10-31. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-171 after this audit).

**Target:** `git diff 04d66c3..HEAD -- docs`, six commits from d9f915c to b35d37b:

- `Functional-Spec.md` §20 III–PPP: new user rulings at FS:342–350, the GGG strike at FS:340 and the date line at FS:352
- `Phase-1-Amendments.md` and `Phase-1-Proposal.md`: lead-tech carried EEE–OOO, with tests (93f82f0, c817540)
- `Screen-Inventory.md`: ux carried HHH–KKK to S-02, S-12, S-06, S-05 and S-16 (cf27908)
- **Supervisor edits:** PPP, recorded in Spec, in the Amendments OQ-12 cell (`:738`) and the OQ-35 cell (`:761`), and in `Status.md` (b35d37b)

Previous audit: `docs/reviews/2026-10-31-rules-phase-1-r7.md` (FAIL: V1, V2; N1–N6).

**Context:** no code exists and `graphify-out/` is absent, so no graph queries were run.

**Verdict: FAIL.** There are 3 confirmed violations:

- **V1:** LLL has not reached Screen-Inventory. S-12 still reads the photo id on the device.
- **V2:** PPP is carried only in two OQ cells. Its "ends early" is a new end of the note step, which S-12 does not list, so a builder would have to pick what the screen shows.
- **V3:** the status lines are stale after PPP, and Amendments `:3` still calls OQ-35 open.

Both r7 violations are resolved, and so are r7 N1, N2, N3 and N5. All three new violations come from rulings recorded after ux's last pass, LLL–PPP. None of them changes the Phase 3 schema.

---

## Auto checks run

```
$ git diff --stat 04d66c3..HEAD -- docs
 Functional-Spec 13, Phase-1-Amendments 158, Phase-1-Proposal 16, Screen-Inventory 66, Status 9

$ git log --oneline 04d66c3..HEAD
 b35d37b PPP (supervisor) | c817540 LLL-OOO carried (lead-tech) | a8747cb LLL-OOO ruled
 93f82f0 EEE-KKK carried (lead-tech) | cf27908 HHH-KKK to screens (ux) | d9f915c III-KKK ruled
 -> ux's commit cf27908 comes before a8747cb: LLL, MMM, NNN, OOO and PPP never went to ux

$ grep -nE '^- \*\*[A-Z]+\.' docs/Functional-Spec.md (tail)
 GGG 340 (struck part), HHH 341, III 342, JJJ 343, KKK 344, LLL 345, MMM 346, NNN 347, OOO 348,
 (blank) 349, PPP 350, (blank) 351, date line 352 "*AAA–PPP above were ruled on 2026-10-31.*"
 "### Still open" 354 (items 356, 357); "## 21" 361; "A time control" 365

$ grep -noE "§20 (LLL|MMM|NNN|OOO|PPP)" docs/*.md | cut -d: -f1 | sort | uniq -c
 Phase-1-Amendments 27, Phase-1-Proposal 8, Status 2, Functional-Spec (own lines)
 Screen-Inventory 0                                                          -> V1, V2

$ grep -nE "restart" docs/*.md   (rubric R-029 hits removed)
 Functional-Spec:350 (PPP); Amendments:738 (OQ-12 cell), :761 (OQ-35 cell); Status:142, :143
 -> nothing in Amendments §6 body (:526-532), P1:108 or S-12 (:329-346)        -> V2

$ grep -n "Photo (id" docs/*.md
 Screen-Inventory.md:345  "- **Reads:** Photo (id only), Handwritten note"     -> V1
 Phase-1-Amendments.md:759 (OQ-33 cites that line as the open problem)

$ R-165 (1), widened words (r7), F = Phase-1-Amendments.md, every "Settled" OQ
 hits at :3 for every OQ: one phrase, "Still open for the user: OQ-35 (§8)"   -> OQ-35 settled by PPP (V3)
 hits at :746-:758: each is another OQ row's own question text or history ("was", "Raised from it"): pass
$ same scan on Phase-1-Proposal.md -> none
$ same scan on Screen-Inventory.md :1-583 (outside Open questions)
 :75, :119, :374 state names ("still open", "is open"); :406, :434 SI's own OQ-20; :577, :578 the Spec heading: pass

$ R-165 (2), status lines
 Amendments:3  ends "... OQ-5, OQ-33 and OQ-34 settled ... Still open for the user: OQ-35 (§8)"
 Amendments:7  "FS §20 Q–OOO (`FS:290–348`; dated at `FS:328` and `FS:350`)"  (FS:350 is PPP; the date line is FS:352)
 Amendments:13-51 (§0) rows through OOO; no PPP row
 Phase-1-Proposal:3 "§20 Q–OOO"; no line saying PPP does not bear on it                    -> V3

$ grep -noE "Spec:3[4-7][0-9](–3[4-7][0-9])?" docs/Screen-Inventory.md (current body)
 :40, :522, :527 "Spec:355–365 (§21)"    -> §21 is now FS:361–371
 :577 "Spec:350" (export)                -> now FS:356; FS:350 is PPP
 :578 "Spec:351" (age gating)            -> now FS:357; FS:351 is blank
 :26, :85, :94, :192, :206, :332-:342, :694, :717-:719 (Spec:337-:344): all correct     -> N5

$ git diff 04d66c3..HEAD -- docs ':!docs/reviews' | grep '^+' | grep -ioE "streak|badge|counter|progress|remind|notif|like|
  rank|leaderboard|level|unread|retake|re-shoot|try again|press again|countdown|timer|thumbnail|preview|minutes left|time left|face|comment"
 Every hit is a refusal ("no re-shoot", "no 'try again'", "A timer ... " in a never-list, "A printed count is a counter"),
 a SQL or route term (trigger, "leads to", "reads"), or a quotation inside a never-list. No banned element is added.

$ grep -nE "refuses .d <= 0|zero interval|if that instant is still ahead" docs/Phase-1-Amendments.md
 :86 "It refuses `d <= 0`"; :107 "if that instant is still ahead"; :110 "(`clock_jump` refuses a zero interval)"
 :176 (§2.2 step 2) "For each, in one transaction: `clock_jump(event_at - app_now())`" (no such guard)  -> N1

$ grep -n "R-001–R-16" docs/Status.md
 :36 "R-001–R-165"   (r7 N4; now R-001–R-171)                                   -> N5
```

---

## Status of r7 findings

| r7 item | Status | Evidence |
|---|---|---|
| V1: open wording and stale status lines | **Resolved, then stale again after PPP** | The "not ruled" text that was at old `:484` is gone (the scan prints nothing in the §6 body). "Open from DDD" (old `:572`) is gone. The OQ-27 cell (`:753`) now reads "Raised from it: OQ-31 and OQ-32, both settled". OQ-30's Blocks column (`:756`) reads "Nothing now (was: …)". `:3` and `:7` reach OOO, §0 has rows EEE–OOO (`:43–51`), and P1:3 reads Q–OOO. PPP has made `:3`, `:7`, §0 and P1:3 stale again: V3 |
| V2: HHH not carried | **Resolved** | P1:105 (retry, frozen instant, 14:59 edge, double refusal, III, JJJ) and P1:180 (check 5). Amendments `:518–525` and the HHH (i)–(iii) cases in "What the build runs" (`:533`); evidence `:618–651`. S-12 rows `:339`, `:340`, `:341`, and source line `:332`. `Status.md:138` is annotated |
| N1: DDD against GGG (G-24) | **Resolved by the user** | FS §20 JJJ (`FS:343`). S-02 `:94` (note offer included; a missing offer is on the never-list). S-12 `:341`. Amendments `:516–517`. G-24 is closed by a `Decided` line |
| N2: EEE not on OQ-44 | **Resolved by the user** | FS §20 KKK (`FS:344`). S-06 `:192`, `:206`. OQ-44 closed at `:694` |
| N3: ring count as text | **Resolved** | S-05 `:173`, `:182`; S-16 `:408`, `:420` (R-166) |
| N4: stale lines | **Partly resolved, partly stale again** | Resolved: the date line (FS:352 covers AAA–PPP), S-02 now cites GGG (`:85`), and SI's revision log owns the supervisor's edits (`:813–827`). Stale again: SI's §21, export and age-gating citations (N5). Still open: `Status.md:36` |
| N5: the note route's text had no evidence | **Resolved** | `mj_scratch_r8` (`:618–651`): the 14:59 edge with its counterfactual (`:625–631`) |
| N6: weakest points | **Carried forward** | C17 (`:91`, `:739`), highlight by date (R-151 residual), RR (`:750`), OQ-3 (`:729`), OQ-12 (`:738`). See N6 below |

---

## Coverage of FS §20 III–PPP in the build docs

| Ruling | Amendments | Proposal | Screen-Inventory | Carried? |
|---|---|---|---|---|
| III | §0 `:46`; §6 `:525`; tests `:533`, `:632–635`, `:670` | 105 | S-12 `:338`, `:340`, `:342` | Yes |
| JJJ | §0 `:45`; §6 `:516–517`; tests `:533`, `:636–639`, `:669` | 105, 180 | `:26`, `:87`, `:94`, `:334`, `:341`; OQ-50 `:718` | Yes |
| KKK | §0 `:47`; OQ-30 `:756` | (none needed) | S-06 `:192`, `:206`; OQ-44 `:694` | Yes |
| LLL | §0 `:48`; §6 `:526–532`; tests `:533`, `:653–682` | 49, 108, 180 | **No.** S-12 Reads `:345` reads "Photo (id only)" | **No: V1** |
| MMM | §0 `:49`; §6 `:525`; OQ-12 `:738`, OQ-34 `:760` | 105 | (none needed: S-12 `:340` already says nothing offers it again) | Yes |
| NNN | §0 `:50`; §6 `:530`; tests `:664–667`, `:680–681` | 105, 108, 180 | S-12 `:341` ("including 15 minutes from the press"), which does not cite NNN | In effect. The letter is not cited (V1) |
| OOO | §0 `:51`; §2.2 `:177`; evidence `:226–246`; OQ-5 `:731` | 63, 176, 213 | (none needed) | Yes. Step 2 does not say how it makes a jump of zero: N1 |
| PPP | **OQ-12 cell `:738` and OQ-35 cell `:761` only**; `:3` still lists OQ-35 as open | (none) | **None** | **No: V2, V3** |

---

## Findings

### Confirmed violations

**V1. FS §20 LLL has not reached Screen-Inventory, and S-12 still reads the photo id on the device.** Rubric: R-165 (3), R-169 (new). It blocks the S-12 flow (Phase 2) and screen (Phase 4). It does not block Phase 3.

- **Where:**
  - `Screen-Inventory.md:345`, S-12: "**Reads:** Photo (id only), Handwritten note (Proposal §2.2)".
  - `Phase-1-Amendments.md:759` (OQ-33) names this line as the open problem: "S-12 reads 'Photo (id only)'". LLL settled OQ-33, but the line was never changed.
  - S-12's source line (`:332`) cites neither LLL (`FS:345`) nor NNN (`FS:347`), although the row at `:341` uses NNN's behaviour.
  - ux's last commit, cf27908, comes before the LLL–OOO rulings (a8747cb). `Status.md:141–143` sends LLL–PPP to lead-tech only, and the revision log has no entry after EEE–KKK (`:819–827`).
- **What is wrong:** LLL (`FS:345`) says the handle is "never exposed to the device as a photo id". Lead-tech carried that into `Phase-1-Amendments.md:529` ("the device never receives it") and P1:49. The screen spec still tells the S-12 builder that the screen reads the photo's id.
- **Why it breaks the rule:**
  - A decided ruling is not carried in a build doc it bears on, and that doc keeps the behaviour the ruling replaced (R-165).
  - Building S-12 as specified sends a sealed photo's id to the device during the sealed year. That is planted fault (a) in the Amendments test (`:533`, `:675`), which the build is meant to catch.

**V2. FS §20 PPP is recorded only in two OQ cells. Its "that note step then ends early" is a new end of the note step that no screen row covers.** Rubric: R-165 (3) and (5) (new), R-171 (new), R-168. It blocks the S-12 flow (Phase 2) and screen (Phase 4). The data side is unaffected.

- **Where:**
  - Spec `FS:350`: "Note handles may be lost on a server restart …; that note step then ends early and nothing wrong is stored".
  - Carried only in the OQ-12 cell (`Phase-1-Amendments.md:738`, "Also recorded here (FS §20 PPP)") and the OQ-35 cell (`:761`).
  - OQ-35's own question states the screen gap: "for an accepted photo the note step then ends earlier than its 15 minutes, which S-12 does not list as one of its ends (`Screen-Inventory.md` S-12)". The supervisor's settlement ("accepted for the local prototype") does not answer that part.
  - S-12 lists five ends: page taken, skip, leaving capture, 15 minutes (`:338`), and a page lost twice (`:340`, `:342`). There is no restart end.
  - The handle's lifetime in the body names only "one note transaction or until press + 15 minutes" (`Phase-1-Amendments.md:3`, `:529–530`; `P1:108` "drops it then or 15 minutes after the press").
  - The route answers a note press "saved" or "closed" (`:530`; evidence `:674`, "note saved / closed"). After a restart the press finds no entry and is answered as closed (`:761`). No S-12 row says what the user sees when a note press is answered "closed" inside the window, or at all.
- **What is wrong:** PPP states a behaviour that S-12 must show, and only the OQ table records it. The "accepted residual, no build change" label holds for the schema, not for the screen. Whoever builds S-12 must decide what follows a "closed" answer at minute 5.
- **Why it breaks the rule:**
  - It is the same supervisor shortcut that r6 found for SS, TT and VV: a ruling noted in the OQ table but not carried (R-165 (3)).
  - On S-12 the builder must pick, which rule zero forbids (`CLAUDE.md:17–24`). The reflexive picks are each banned or close to it:
    - "Your 15 minutes are up" reads the window as a timer (R-140).
    - "Couldn't save your note" is an error that invites a second take (FS §20 PP, III; R-020).
    - A silent "saved" tells the user something false. That is not banned, but it is a behaviour decision.
  - Not picked here. ux should write the row, or raise it for the user.

**V3. The status lines are stale after PPP, and the Amendments status line still calls OQ-35 open.** Rubric: R-165 (1) and (2), R-134. This blocks nothing in Phase 3 behaviour, but the Amendments are the Phase 3 build source.

- **Where:**
  - `Phase-1-Amendments.md:3` ends "Still open for the user: OQ-35 (§8)". PPP settled OQ-35, and the cell at `:761` says "Settled 2026-10-31, FS §20 PPP".
  - `:7`: "FS §20 Q–OOO (`FS:290–348`; dated at `FS:328` and `FS:350`)". FS:350 is now PPP itself, and the date line is FS:352.
  - §0 (`:13–51`) has no PPP row.
  - `Phase-1-Proposal.md:3`: "§20 Q–OOO", with no line saying PPP does not bear on P1.
  - The OQ-12 cell (`:738`) runs two sentences together ("(FS §20 MMM, `FS:346`; §6) Also recorded here (FS §20 PPP)") and gives PPP no line number.
- **Why it breaks the rule:** R-165 (1): "No build doc calls a decided question open". R-165 (2): each build doc's status line reaches the latest letter, or says why it does not. A Phase 3 builder reading `:3` would treat the restart behaviour as still undecided.

### Notes blocking Phase 3

**N1. As written, the loader's step 2 fails on its first event.** Rubric: R-117, R-120 (new `Decided` line).

- **Where:**
  - `Phase-1-Amendments.md:176` (§2.2 step 2): "For each, in one transaction: `clock_jump(event_at - app_now())`".
  - `:86`: `clock_jump` "refuses `d <= 0`".
  - Under OOO, `:177` makes Lantern's join "the first event of the load, at the clock's starting instant". Each of the four join-then-commit pairs shares one instant (P1:213, "each of the four joins and commits at the same instant").
  - The panel jump already guards this case ("if that instant is still ahead", `:107`; `:110`). Step 2 does not.
- **What is wrong:**
  - The evidence (`:230–235`) shows the replay working, so lead-tech's stand-in must have skipped jumps of zero, but the doc does not say so.
  - A Phase 3 builder who follows step 2 literally fails at 2021-01-01 00:00:00.
  - The quick fix a builder would reach for is to loosen `clock_jump`'s guard. Loosened from `<= 0` to `< 0` it is harmless; loosened any further it becomes a backward jump (R-117). Step 2 needs the same "only if ahead" clause as `:107`.
- This is not a banned item. It is a gap in Phase 3 build text on the path that keeps `joined_at` honest (OOO).

### Notes for Phase 4+ (and the Phase 2 flows)

**N2. A lost press that would have been refused: raised, not picked (G-25, new).**

- **Where:**
  - `Phase-1-Amendments.md:516`: "Whether the lost press would have been accepted is never computed."
  - `:529`: "A lost press answers `accepted`".
  - JJJ (`FS:343`): "exactly like a normal press, note offer included".
- **The conflict:**
  - When no frame is left, a normal press at that instant shows the capture refusal (`Screen-Inventory.md:92`; `PROVISIONAL: B7`).
  - Amendments OQ-32 (a) (`:758`) asked exactly this: "different from an accepted press, or from what that press would have given?". The settlement answers only the accepted case.
  - As built, a user with no frame left who hits the bug sees an accepted press and a note offer. Their next press is then refused.
- **Status:** nothing is stored either way, so Phase 3 is unaffected. The S-02 lost-press row and R-170 wait on the user.

**N3. A lost press's note does no work, so it may be answered faster than a saved one.** Rubric: R-170 (new).

- The route "calls no note step … nothing is stripped, stored or sealed" (`Phase-1-Amendments.md:517`, `:530`). A saved note strips, seals and commits.
- If S-12 waits for the server's answer before it ends the step, the step ends sooner after a lost press. DDD and JJJ say there must be no visible difference, and a difference is the one sign that invites a second press (PP).
- The response bodies are already the same (evidence `:674`). The timing is not covered by any test. R-170 (3) makes it a Phase 4 review check.

**N4. The note handle is a sealed photo's id, held beside its press instant in route memory, and no check covers the route's own logs.** Rubric: R-169 (new), R-167 (scope note).

- `Phase-1-Amendments.md:527–529`: the handle "is the new photo's `id`", and the entry holds "the press instant, read as `app_now()`".
- The device scan (`:674–675`) covers responses only.
- R-167 covers only the Postgres server log. A route that logs requests, its memory or an error trace, which is the default in most web frameworks, would write a sealed photo's id beside its real press time. That is the record R-167 bans in the database log.
- R-169 (2) adds a scan of route output for each handle and each press instant.
- Lead-tech's choice to use the photo id as the handle, rather than a separate token, is argued (`:528`) and does not break LLL as long as the id never leaves the route. Not a silent decision.

**N5. Stale citations and records.** No behaviour changes. Each should be fixed by its owner.

- **Spec citations in Screen-Inventory:**
  - `:40`, `:522` and `:527` cite "Spec:355–365 (§21)". §21 is now FS:361–371.
  - `:577` cites Spec:350 for export, and FS:350 is now the PPP ruling. `:578` cites Spec:351, which is now a blank line. Export and age gating are at FS:356 and FS:357.
  - ux re-checked every citation on its date (`:827`). The supervisor then added LLL–PPP and blank lines without moving them. R-165 (6) now makes the editor of §20 re-check them.
- **Status:** `Status.md:36` still gives the rubric as R-001–R-165. It was R-168 after r7 and is R-171 now.
- **Evidence edited in place:**
  - `Phase-1-Amendments.md:982–991` changes "15" to "14" inside a verbatim evidence block. The change is disclosed and re-checked in `mj_scratch_r8` (`:1001`), so it passes.
  - Evidence should still be appended, not rewritten: the block no longer shows what the run printed.

**N6. Weakest points carried forward.** None is a violation today.

- **OQ-12 now holds four residuals:** acting as any user, the user-settable log parameter (FFF), III held by the route only (MMM), and handles lost on restart (PPP). All are to be revisited "before real users". No single line lists what must be closed before a deploy. The list is now long enough that one could be missed.
- **C17** (`:91`, `:739`): still no default.
- **Highlight by date** (R-151 residual), **RR** (`:750`) and **OQ-3** (`:729`) are unchanged.
- **Review-only checks:** R-169 (5), R-170 (3) and R-171 cannot be automated before Phase 4 screens and routes exist.

**N7. The rubric itself held a behaviour that JJJ retired.** This was found and fixed in this audit.

- R-160's GGG `Decided` line read "The camera returns as after any press, with no note offer". Its r7 (3) wording read "no S-12 offer".
- Both now stand as history, superseded by a JJJ `Decided` line. Nothing was deleted.

### Checked and clean

- **OOO** (`Phase-1-Amendments.md:177`, evidence `:228–246`; P1:63, :176, :213):
  - `join_user(name text)` takes no time argument, and the call with a date fails, positionally and by name.
  - The `BEFORE INSERT` trigger refuses a back-dated row even for the table owner, which meets R-164.
  - A planted join with a time argument is caught by the signature scan and by the trigger.
- **The handle mechanism** (`:527`, evidence `:657–682`):
  - The setting is transaction-local and is rolled back with its savepoint.
  - A lost press reads an empty handle, also after a saved press on the same connection: planted fault (d) is caught.
  - Entries are keyed by session and acting user (`:672–673`).
  - The NNN edges are exact on the stopped clock, at + 14:59 and + 15:00.000, and the running-clock case is shown (`:680–681`).
- **JJJ data path:** row counts are unchanged and P has no note. The planted "latest unnoted photo" route is caught twice (`:639`, `:669`).
- **KKK:** no journey date is returned to a public reader, and path order rests on `(captured_on, id)`. S-06 `:206` bans date labels.
- **The GGG strike in Spec** (`FS:340`): it follows JJJ's own words ("which is retired") and keeps the struck text. Pass.
- **No banned element** was added in any changed line (scan above).
- **No silent decision** was found in the lead-tech or ux carriage. The two places a builder would have to pick are V2 and G-25.

---

## Rubric changes

**Added:**

| Check | What it covers | Comes from |
|---|---|---|
| R-169 | Nothing that ties a press to its sealed photo leaves the server route: not to the device, a log, a trace or a store; one note transaction; gone by press + 15 minutes | FS §20 LLL, MMM, NNN, PPP; V1, N4 |
| R-170 | A lost press and its note cannot be told apart from a saved press and note: the same answers, the same next state, nothing timed on a difference | FS §20 DDD, JJJ, NNN, PP; N3 |
| R-171 | Every route answer and every end of the note step has a screen row | Rule zero; FS §20 PPP; V2 |
| G-25 | A lost press that would have been refused: "normal press" means accepted, or the refusal? | FS §20 JJJ against SI:92 and B7; N2 |

**`Decided` lines added:**

- JJJ (superseding GGG's note-offer line and the r7 (3) wording), III and MMM, LLL and NNN, and PPP on R-160
- JJJ on R-168
- JJJ on G-24, which is now closed
- KKK on R-152
- OOO on R-120, with its current implementation

**`Updated` lines added:**

- R-116 (§21 is now at FS:361; "A time control" at FS:365)
- R-165 (new (5): rulings recorded as residuals are still checked against screens; new (6): whoever edits §20 re-checks the line citations)
- R-167 (scope: the database log only; the route's output is R-169's)

**Other changes:**

- The coverage rows are extended: R-170 under "No retakes", and R-169 under "Nothing leaks".
- One coverage paragraph and one header line are added.
- **Nothing was renumbered or removed.** The only changed lines are the two coverage rows, each kept whole with text appended.

## Report
- Files changed: `/home/user/MyJourney/docs/Rules-Rubric.md`, `/home/user/MyJourney/docs/reviews/2026-10-31-rules-phase-1-r8.md`
- Findings: 10
  - V1 (R-165 (3), R-169): `Screen-Inventory.md:345`. S-12 still "Reads: Photo (id only)" against FS §20 LLL (`FS:345`). No LLL or NNN citation on S-12 (`:332`)
  - V2 (R-165 (3) and (5), R-171): `Phase-1-Amendments.md:738`, `:761`; `Screen-Inventory.md:338`, `:342`. PPP's "ends early" is carried only in OQ cells. S-12 has no row for a "closed" note answer
  - V3 (R-165 (1) and (2)): `Phase-1-Amendments.md:3` ("Still open for the user: OQ-35"), `:7` ("dated at FS:350"), §0 `:13–51` (no PPP row), `Phase-1-Proposal.md:3` (Q–OOO)
  - N1 (R-117, R-120), blocks Phase 3: `Phase-1-Amendments.md:176` calls `clock_jump(event_at - app_now())` for every event, but `:86` refuses zero, and OOO puts join and commit at one instant (`:177`, P1:213)
  - N2 (G-25): `Phase-1-Amendments.md:516`, `:529`. A lost press that would have been refused is answered `accepted`. OQ-32 (a) asked this and its settlement does not answer it. Not picked
  - N3 (R-170): `Phase-1-Amendments.md:517`, `:530`. A lost press's note does no work and may be answered faster. Phase 4 timing review
  - N4 (R-169, R-167): `Phase-1-Amendments.md:527–529`. The handle is the sealed photo id plus press instant in route memory, and no check covers the route's own logs
  - N5: `Screen-Inventory.md:40`, `:522`, `:527` (§21 is now FS:361–371), `:577`, `:578` (Spec:350 is now PPP; export and age gating at FS:356 and :357); `Status.md:36` (R-001–R-165); evidence edited in place at `Phase-1-Amendments.md:982–991`
  - N6: OQ-12 (`Phase-1-Amendments.md:738`) holds four residuals with no pre-deploy list. C17, RR, OQ-3 and the highlight-by-date residual are unchanged
  - N7 (R-160, fixed here): `Rules-Rubric.md` R-160's GGG line and its r7 (3) wording held "no note offer", which JJJ retired. Superseded by a `Decided` line
- Rubric additions: R-169, R-170, R-171, G-25; `Decided` lines on R-120, R-152, R-160, R-168, G-24; `Updated` lines on R-116, R-165, R-167
- Verdict: FAIL
