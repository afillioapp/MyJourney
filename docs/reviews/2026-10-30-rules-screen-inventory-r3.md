# Rules audit: Screen Inventory, round 3 re-audit (final)

- **Target:** `docs/Screen-Inventory.md` at commit f781223 ("Record user rulings: G-8 text only, B2 Public case, B6 over B19, local Postgres"), with 6fc8779 (fixes for N12–N14)
- **Also checked for consistency with the rulings:** `docs/Functional-Spec.md` §20 Q–S, `docs/Decisions-Needed.md`, `docs/Rules-Rubric.md`
- **Against:** `docs/Rules-Rubric.md` (R-001 to R-150), DN "Provisional defaults in force"
- **Previous audit:** `docs/reviews/2026-10-30-rules-screen-inventory-r2.md` (FAIL on N2 and N3 only)
- **Auditor:** Rules Guardian, 2026-10-30
- **Verdict:** **PASS** (zero confirmed violations). N2 and N3 are settled by the user's dated rulings (FS §20 R and Q), and the inventory's text now matches them. N12–N14 are fixed. Five new findings remain, all stale restatements or weak points (N16–N20). None of them builds a banned item or decides a behaviour silently. N16 should still be fixed before Phase 2 builds S-09

Short names: SI = `Screen-Inventory.md`, FS = `Functional-Spec.md`, DN = `Decisions-Needed.md`, RR = `Rules-Rubric.md`, CL = `CLAUDE.md`. `graphify-out/` is absent, so no graph query was run. There is no code, so no auto check can run as a build test. The scans below are R-150 steps 1–3 and grep aids, run as shell over the docs.

---

## 1. Automated scans

### 1.1 R-150 step 1, unlabelled IDs, labels outside DN, malformed labels

```
$ F=docs/Screen-Inventory.md
$ comm -13 <(grep -oE 'PROVISIONAL: [BC][0-9]{1,2}' $F | ...) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | ...)
(no output)
== labels not in DN
(no output)
== malformed
(no output)
```

### 1.2 Stale ruling text across the four docs

```
$ grep -rn -i 'with photographs\|seven switchable\|B9 (a).*switch\|B9a' docs/*.md   (reviews excluded)
RR:1008  "Seven defaults were switchable ... six remain"          -> annotated, correct
RR:1011  R-141 "the seven switchable defaults"                     -> STALE (tidied, section 5)
RR:1035  R-145 statement, decided + original                       -> correct
RR:1038  R-145 how to check "Under each setting ... 'With photographs'" -> STALE (tidied, section 5)
RR:1164, 1166  G-8 decided + historical default                    -> correct
SI:709   revision log                                              -> correct
$ grep -n 'switchable' docs/Screen-Inventory.md
SI:266   "**`PROVISIONAL: B9`.** ... Only (a) is switchable:"      -> STALE (N16)
SI:599   OQ-11 "Decided 2026-10-30 ... Not switchable."            -> correct
SI:536-542  T-02 lists six switches, no B9                          -> correct
```

R-103's B9 line (RR:761) also still said "The (a) setting is switchable (R-145)". I tidied it (section 5).

### 1.3 Ruling wording, side by side

| Ruling | FS §20 | DN | SI | RR | Consistent |
|---|---|---|---|---|---|
| Q: Positivity Feed text only | FS:290 | DN:28 "(a) decided … text only, no longer switchable" | SI:268, 275, 599; T-02 row removed | R-145, G-8 (RR:1164) | **Yes**, except SI:266 (N16), SI:531 (N17), and the rubric text I tidied |
| R: Public waits under B2's option | FS:291 | DN:21 | SI:189, 200, 249, 424, 595 | R-068 line (RR:514), R-142 | **Yes**. R-142's how to check had no Public case (tidied) |
| S: owner sees "a highlight is open" over B19 | FS:292 | DN:25, DN:38 | SI:111, 661 | R-009 lines (RR:111), G-17 (RR:1206) | **Yes** in substance. Restatements at SI:126, 131, 343, 346 and 632 are not updated (N18) |

---

## 2. Status of earlier findings

| # | Finding | Status | Current evidence |
|---|---|---|---|
| N2 | B2's option extended to Public photos and every reader (VIOLATION) | **RESOLVED by user ruling** (FS:291, §20 R) | The inventory's reading is now the decision: SI:189 "Public photos included (decided 2026-10-30, Spec §20 R)", SI:200, 249, 424, OQ-9 at SI:595. DN:21 matches |
| N3 | B9 (a) "with photographs" is a photo feed (VIOLATION) | **RESOLVED by user ruling** (FS:290, §20 Q) | SI:268 is text only. The T-02 B9a row is gone (SI:536–542). OQ-11 at SI:599. Residue: SI:266 (N16) and SI:531 (N17) |
| N5 | How long "Your Journey is ready" shows | **NOT RESOLVED, open, not filled in** | SI:172 states where it appears and nothing about how long. Not raised as an OQ. Not a violation, but still unasked |
| N6 | Under B4 "per year with the app", the day a ring appears | **NOT RESOLVED, open, not filled in** | SI:162 "Rings follow years since joining", with no date. OQ-6 (SI:588–589) does not raise it. RR:1026 does |
| N7 | B19 "nothing else" against B6 "a highlight is open" | **RESOLVED by user ruling** (FS:292, §20 S) | SI:111, SI:661. Label residue in N18 |
| N8 | "Jump to the next unlock" reveals another user's date | **RAISED as SI OQ-41, open** | SI:664–665 "Still open, no ID. Raised for the user." T-01 (SI:514) holds the jump from Proposal:194 and does not fill in whose. Not listed in DN (see N19) |
| N9 | Count by scrolling; whether a tag links to a profile | **STANDING** (R-139, R-147, R-148) | SI:192, 419, 617–620. The user has not ruled. Report each round |
| N10 | Readings filled in on raised residuals | **UNCHANGED, still raised** | SI:610 (C1 with C12, "for the user to confirm"), SI:628 (skip ends the note step), SI:632 (where B6 is shown) |
| N12 | S-13 open state: start control not held, hiding not banned | **RESOLVED** | SI:343: "The way to start one, offered the same as when none is open … a start control hidden, greyed out or relabelled because one is open" |
| N13 | B18 not carried to S-09; "while the owner writes" | **RESOLVED** | SI:262 source lists B18. SI:275 bans "Tags surfaced, suggested or counted by popularity (`PROVISIONAL: B18`)". SI:462 drops "while the owner writes" |
| N14 | Source lists, unlock-date label, Spec:74 wording, log | **RESOLVED** | SI:98, 155, 182 and 454 list B19 (and B17, B18). SI:108 is labelled `B19`, `C2`. SI:106–107 now say "which reads Spec:74 as covering the contents". SI:702 names S-03, S-05, S-06. New residue on T-02: N17 |
| N15 | Weakest point, the B19/B6 conflict | **RESOLVED by user ruling** (§20 S) | See N7 |

---

## 3. Findings

No confirmed violations this round. Each finding below says why it is not one.

### N16: WEAK POINT (stale restatement of ruling Q). S-09 still says "Only (a) is switchable"

- **Check:** R-145 (as decided), R-141, DN:9 ("fixes every restatement (L-002)"); compare R-150 step 4
- **Where:** SI:266, "**`PROVISIONAL: B9`.** (b) … (f) A photo enters only after its journey's reveal is finished. Only (a) is switchable:", followed by SI:268 "(a) Text only (decided 2026-10-30, Spec §20 Q)"
- **What is wrong:** the lead-in still calls B9 (a) switchable, and still puts it under the `PROVISIONAL: B9` heading. DN:28 says "(a) decided 2026-10-30: text only, no longer switchable", FS:290 records it, and the inventory's own OQ-11 (SI:599) says "Not switchable".
- **Why it matters:** this is the one ruling that touches a banned item ("No photo feed", CL:72). A switch for (a) has only one other setting in the record, "with photographs" (DN history, R-145 before 2026-10-30). A builder who reads S-09 alone is told a switch exists.
- **Why it is not a violation:** the only setting S-09 describes is text only. T-02 lists no B9 switch (SI:536–542), and SI:548 bans "a switch for any default not marked switchable". Nothing in the text builds an image into the feed.
- **Fix belongs to:** the supervisor or UX agent. Change "Only (a) is switchable:" to say (a) is decided and nothing in B9 is switchable, and take (a) out from under the `PROVISIONAL: B9` heading

### N17: NOTE. The T-02 source list still cites B9

- **Check:** traceability (CL:23), R-141
- **Where:** SI:531, "Decisions 'Provisional defaults in force' (B2, B4, B5, B9, B11, B12, C6, C11, C16)"
- **What is wrong:** T-02 no longer touches B9 (the row was removed). The list now names a switch that does not exist. It is the same class of drift as N14 and is harmless on its own, but it points the same way as N16.
- **Fix belongs to:** the supervisor (drop B9 from SI:531)

### N18: NOTE. The owner half of B6 is now decided (§20 S) but is still restated as provisional in five places

- **Check:** CL:23 (a decision lives in §20), DN:9 (L-002)
- **Where:** SI:126 (`sealed · highlight open` "plus element 7 (`PROVISIONAL: B6`)"); SI:131 (Reads, element 7, `PROVISIONAL: B6`); SI:343 ("The plain fact that a highlight is open, with no end time (`PROVISIONAL: B6`)"); SI:346 (Reads); SI:632 (OQ-26 "Decisions B6, provisional: … the owner sees only 'a highlight is open'", with no mention of §20 S, while OQ-39 at SI:661 was updated)
- **What is wrong:** SI:111 (element 7) cites §20 S, but the state row and Reads line for the same element on the same screen still call it provisional. The "others learn nothing" half of B6 is still provisional, so the labels at SI:337 and on "Anything about the highlight to anyone but the owner" (SI:343) are correct.
- **Why it is not a violation:** calling a decided behaviour provisional errs toward caution. It narrows nothing and widens nothing. A later scan that separates decided from provisional by label would still count it wrong.
- **Fix belongs to:** the supervisor. Cite §20 S on the owner half at SI:126, 131, 343 and 346, and add the §20 S exception to OQ-26 as was done for OQ-39

### N19: NOTE. "Strictest reading" is still claimed where §20 R now decides, and OQ-41 is not in DN

- **Check:** CL:19–24 (rule zero), CL:23
- **Where:**
  - SI:371 (S-15 Viewer: "strictest reading: under B2's option, not until finished") and SI:605 (OQ-14: "Network reading before finish follows B2 (strictest reading)"). FS:291 now says that under the option "no one but the owner reads the journey until the reveal is finished". That covers the overview if the overview is part of "the journey". It probably is, but §20 R names photos and does not name the overview.
  - OQ-41 (SI:664–665) is "Still open, no ID". DN has no entry for it (no match for "next unlock" or OQ-41 in DN). Rule zero step 2 sends an unlisted question to the supervisor. It is raised in the inventory, but it is tracked only there.
- **Why it is not a violation:** both points restrict, and neither builds anything. The S-15 reading is the strictest one, and OQ-41 is raised, not filled in.
- **Fix belongs to:** the supervisor. Either cite §20 R at SI:371 and SI:605, or ask the user to confirm the overview is covered. Add OQ-41 to DN's open list so it is not lost when the inventory is closed

### N20: WEAK POINT (weakest point under ruling Q). Nothing stops stepping from one opened feed photo to the next

- **Check:** FS:290 (§20 Q: "A photograph is shown only when the reader opens one entry"), CL:72, CL:24. Now R-145's how to check (case added this round)
- **Where:** S-17, SI:410–428. "Reached from … Positivity Feed S-09" (SI:415). "Leads to: Reflect S-14 (owner), Walking a path S-06". The "On every state, never" line at SI:428 bans comments, captions, edits and the like, but not a next, previous or swipe control.
- **What is wrong:** ruling Q keeps photographs out of the feed list. A photo screen opened from the feed with a "next" arrow or a swipe through the feed's results would show the same stream of photographs one image at a time. Product teams add that by reflex. S-17's "Leads to" does not list it, so it is not held. But it is also not banned, and S-17 is shared with S-06, where walking forward through a path in order is the purpose (SI:204).
- **Why it is not a violation:** the inventory does not hold the control. The gap is that nothing forbids it.
- **Rubric:** R-145's how to check now carries the case (section 5). The inventory should add the ban on S-17 for the S-09 entry path. That is for the UX agent.

---

## 4. Changes checked for silent decisions and banned items

I read every line changed in 6fc8779 and f781223 across all four docs. I checked each one for a leak from a sealed year (count, thumbnail, partial mark, relative date), for an engagement mechanic (badge, dot, "new" marker, reminder, countdown), for layer exposure, for an image in any feed, and for any behaviour not traced to a DN row or an FS §20 line.

- Every one of the three rulings narrows or holds. Q removes an image setting. R widens a refusal to Public photos. S allows exactly one bare fact to the owner, "with no end time and no countdown", which R-140 and SI:126 and SI:343 still guard.
- Each ruling is recorded once in FS §20 (FS:289–292) as a dated decision, which is what CL:23 requires. The restatements point back to it.
- OQ-41 is raised and not filled in.
- N12's fix adds a ban. N13's fix adds a ban and removes a narrowing. N14's fixes are labels and wording.

**Nothing in the changes breaks the banned list or decides a behaviour silently.**

---

## 5. Rubric changes (text I own that was stale because of the rulings)

The rubric did not shrink. The earlier wording is kept as "Before 2026-10-30 …" in each case.

- **R-103, B9 line (RR:761):** "The (a) setting is switchable (R-145)" now reads "(a) was decided 2026-10-30 (FS §20 Q): text only, not switchable"
- **R-141 statement (RR:1011):** "seven switchable defaults" changed to "six (B2, B4, B5, B11, B12, C6)". B9 (a) is noted as decided, with no switch
- **R-142 (RR:1016–1020):** the statement is rewritten as one statement under §20 R: the option refuses everyone but the owner, Public photos included. The original statement said the setting changes only the network's reading of Network photos, which §20 R contradicts. FS §20 R is added to Source. The how to check gets the case that was missing: in a test copy, a Long Way Round #4 photo set Public is refused to Open Hands and First Light under the option and allowed under the default. The approved fixtures are not edited; a standing fixture goes to the supervisor
- **R-145 (RR:1034–1038):** the statement and how to check no longer run "under each setting". The feed list has no image element and no image URL or media field in its endpoint. The panel has no B9 control. An image in the list is now a violation, not a finding awaiting the user. **Added case (N20):** from an opened photo, no next, previous or swipe control steps to another feed entry's photo

**No new check number.** No confirmed violation was found, and N20's case fits inside R-145.

---

## Report
- Files changed: /home/user/MyJourney/docs/reviews/2026-10-30-rules-screen-inventory-r3.md, /home/user/MyJourney/docs/Rules-Rubric.md
- Findings: 5 (0 confirmed violations)
  - N16, R-145/R-141/L-002, SI:266: "Only (a) is switchable" contradicts §20 Q and DN:28 (weak point, stale restatement)
  - N17, traceability/R-141, SI:531: T-02 source list still cites B9 (note)
  - N18, CL:23/L-002, SI:126, 131, 343, 346, 632: B6's owner half, decided by §20 S, still labelled provisional; OQ-26 not updated (note)
  - N19, rule zero, SI:371, 605, 664–665: "strictest reading" where §20 R now decides; OQ-41 not listed in DN (note)
  - N20, FS §20 Q/CL:72, SI:410–428: nothing bans stepping from one opened feed photo to the next (weak point; case added to R-145)
- Rubric additions: none (new number). Tidied R-103 B9 line, R-141, R-142 (statement, source, Public case), R-145 (statement, source, how to check, plus the N20 case)
- Verdict: PASS (zero violations)
