# Rules audit: Screen Inventory, round 2 re-audit

- **Target:** `docs/Screen-Inventory.md` at commit 1faa949 ("Screen inventory round 2: apply B17-B19, fix N4 and N11"), 704 lines
- **Against:** `docs/Rules-Rubric.md` (R-001 to R-150), `docs/Decisions-Needed.md` "Provisional defaults in force" (B1–B19, C1–C16)
- **Previous audit:** `docs/reviews/2026-10-30-rules-screen-inventory-r1.md` (FAIL, N1–N11)
- **Auditor:** Rules Guardian, 2026-10-30
- **Verdict:** **FAIL**. Round 2 introduced no new violation, and N1 and N11 are resolved. Two confirmed violations from round 1 still stand: N2 and N3, both waiting on the user. N4 is only partly resolved (N12). Four new notes and weak points (N12–N15)

Line numbers are `Screen-Inventory.md` lines (SI) unless another file is named. Short names: FS = `Functional-Spec.md`, P1 = `Phase-1-Proposal.md`, CL = `CLAUDE.md`, DN = `Decisions-Needed.md`, RR = `Rules-Rubric.md`. `docs/Overview.md` is not cited. `graphify-out/` does not exist in this checkout, so no graph query was run.

---

## 1. Automated checks

**No automated checks or test scripts exist yet.** There is no code, so none of the rubric's auto checks can run as build tests (R-137 has nothing to map). The scans below are R-149 and R-150 steps 1–3 run as shell over the inventory, as evidence for this audit only.

### 1.1 R-150 step 1: table IDs never labelled in the inventory

```
$ F=docs/Screen-Inventory.md
$ comm -13 <(grep -oE 'PROVISIONAL: [BC][0-9]{1,2}' $F | grep -oE '[BC][0-9]+' | sort -u) \
           <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]+' | sort -u)
(no output)
== labels in the inventory that are not in DN
(no output)
== malformed labels (PROVISIONAL with no ": <ID>")
(no output)
```

Round 1 printed `B17 B18 B19` and a malformed label at SI:565. Both are gone.

### 1.2 R-150 step 2: DN rows that name an inventory question

```
$ grep -oE '^\| [BC][0-9]+ \|.*Raised as[^|]*' docs/Decisions-Needed.md | while read -r l; do ... done
(no output)
```

Round 1 printed `OQ-37 lacks B17`, `OQ-38 lacks B18`, `OQ-39 lacks B19`. Now clean.

### 1.3 R-150 step 3: "no default", "still open, no ID", stale ranges

```
$ grep -niE 'no default|still open, no ID|B1–B1[0-9]' docs/Screen-Inventory.md
11:  ... (B1–B19 and C1–C16) ... A question with no default stays open.
574: - **No ID**: still open, with no default. ...
593: ... What the line records besides `captured_at` is not covered by B5: **still open, no ID**.
622: ... whether a tag leads to that person's profile is not covered by the switch: **still open, no ID**.
630: ... **Residual: still open, no ID.**
648: ... how matches are ordered are not covered by C10: **still open, no ID** ...
```

Each was read against DN. SI:11 now states the full range. SI:574 is the legend. SI:593, 622, 630 and 648 are residuals that their row does not cover. That is correct under R-150. None of them is a question that a row answers.

### 1.4 Grep aids for B17, B18 and B19 (RR:762 grep aid, plus the B19 terms)

```
$ grep -niE 'commit date|type by name|by name only|categor|popular|suggest|surface' docs/Screen-Inventory.md
```

Every hit was read; the results are sorted in section 3. In S-19, "category" now appears only for the chapter catalogue (SI:463, FS:129) and in the quoted conflict (SI:458, 658). "Popular" and "suggest" appear only inside bans or quotations.

---

## 2. Status of N1–N11

| # | Round 1 finding | Status | Current evidence |
|---|---|---|---|
| N1 | B17, B18 and B19 not applied (VIOLATION) | **RESOLVED** | Range B1–B19 at SI:11. S-19 is under B17 and B18 at SI:458 and SI:463. B19 is labelled at SI:106, 107, 171 and 199. OQ-37, 38 and 39 point to B17, B18 and B19 at SI:659, 661 and 663. Scans 1.1–1.3 are clean. The wording matches DN:36–38 (section 4). Traceability residue is in N13 and N14 |
| N2 | B2's option extended to Public photos and every reader (VIOLATION) | **AWAITING USER**, still a violation in the text | Unchanged at SI:189, 200, 249, 372 and 425. The Public case is still not raised in OQ-9 (SI:596–597) |
| N3 | B9 (a) "with photographs" is a photo feed (VIOLATION, standing, R-145) | **AWAITING USER** (G-8) | SI:268, 276, 541. The default is still "text only" (SI:267, 541) |
| N4 | Start-highlight control could be greyed while a highlight is open (risk) | **PARTLY RESOLVED** | S-03 element 6 is fixed (SI:110: "offered the same … whether or not one is open: never greyed or relabelled"). S-13 bans only greyed and relabelled for the open case, not hidden, and the open state's Holds no longer lists the control (SI:344). See **N12** |
| N5 | How long "Your Journey is ready" shows is unstated (risk) | **NOT RESOLVED** | SI:172 and 175 are unchanged. OQ-15's residual (SI:612) still raises where the line appears, not how long it stays. Not on round 2's list |
| N6 | Under B4 "per year with the app", the day a ring appears is not raised (weak point) | **NOT RESOLVED** | SI:162 and 171–172 are unchanged. OQ-6 (SI:590–591) does not raise it. Not on round 2's list |
| N7 | B19 "nothing else" against B6 "a highlight is open" (open question) | **AWAITING USER**, now raised in the inventory | SI:663: "Open conflict with B6 ("a highlight is open", S-03 element 7) raised for the user, not settled here." Element 7 is still shown under the B6 label (SI:111). That is correct until the user rules |
| N8 | "Jump to the next unlock" plus the simulated date reveals someone's unlock date (open question) | **AWAITING USER** | SI:515, 516 and 546 are unchanged. No inventory OQ raises it yet. It is carried in the r1 report only |
| N9 | Count-by-scrolling residual; whether a tag links to a profile (standing note, R-139, R-147, R-148) | **STANDING** | SI:192, 392, 420 and 622 are unchanged. It must be reported each audit until the user decides |
| N10 | Readings filled in on raised residuals (note) | **UNCHANGED, still raised** | SI:630 (skip ends the note step), SI:634 (where B6 is shown), SI:612 (C1 with C12) |
| N11 | `PROVISIONAL` label with no ID (weak point) | **RESOLVED** | SI:565 now reads "Decisions C11 (`PROVISIONAL: C11`)". Scan 1.1 finds no malformed label |

Summary: 2 resolved, 1 partly resolved, 2 not resolved, 4 awaiting the user, 1 standing, 1 unchanged note. None regressed.

---

## 3. Findings

### N2, N3: CONFIRMED VIOLATIONS, carried (not re-argued)

Both are set out in full in the r1 report (sections N2 and N3). The supervisor has deliberately left them for the user. They are listed here because the verdict rests on them. Neither is softened because the fix lies with the user.

- **N2.** Check R-142 and the provisional line under R-068. SI:189, 200, 249, 372 and 425 apply B2's "only after reveal finished" to Public photos and to every reader. DN:21 names only the network.
- **N3.** Check R-145 and CL:72. SI:268 and 541 offer a Positivity Feed of photographs as a switch setting.

### N12: RISK (N4 residual). On S-13, while a highlight is open, the start control is not held, and hiding it is not banned

- **Check:** R-138 (B6 line, RR:375): "the start-highlight control is not hidden, greyed or relabelled while one is open; a second start is refused on tap (R-041)"
- **Where:** SI:344. Compare SI:343 and SI:110.
- **What is wrong:** In `sealed · highlight open`, the S-13 Holds cell lists only "The plain fact that a highlight is open … Starting another is refused (Spec:284)". The way to start one, which the row above holds at SI:343, is not listed. Round 2 added "including a start control greyed out or relabelled because one is open" to the never cell. That covers two of R-138's three forms. "Hidden" is left out, and "As above" brings in "hidden … because none is left" only. Read as written, the open state of S-13 holds no start control at all. That is the "hidden" form R-138 bans. S-03 element 6 gets this right with "offered the same … whether or not one is open" (SI:110), so the two screens now disagree.
- **Why it matters:** a start control that disappears for exactly 24 hours and then comes back is a time signal tied to the highlight window. R-140 and B6 ban that kind of signal. The refusal has to come on tap, not by taking the control away.
- **Severity:** risk (the text does not state that the control is hidden, but it leaves hiding open, and the Holds cell reads that way)
- **Fix belongs to:** the UX agent (state in SI:344 that the start control is held as in `sealed`, and add "hidden")

### N13: WEAK POINT. B18 is not carried to S-09, though OQ-38 says it affects S-09

- **Check:** R-150 step 4 and R-103's B18 line (RR:762: "no screen suggests, sorts, ranks or counts feeling tags by how often they are used, at the tag step **or anywhere else**")
- **Where:** SI:660 ("Affects S-19, S-09"); S-09 at SI:262 (Spec source lists "Decisions B9" only) and SI:276–281 (no `PROVISIONAL: B18`). Also SI:463: "Suggested … feeling tags **while the owner writes**"
- **What is wrong:** B18 is applied and labelled only on S-19. S-09 still bans popularity ordering under FS:202 and R-103, and counts under P1:180. So its content is covered. But the screen that OQ-38 itself names as affected does not carry B18's label. S-09 also has no ban on a suggested or "popular tags" row. Separately, SI:463 limits "suggested" to "while the owner writes", while B18's "No suggestions" has no such limit.
- **Why it is a weak point, not a violation:** scan 1.1 passes because B18 is labelled somewhere, and S-09's existing bans already exclude popularity and counts. But R-150 asks for every screen that touches the question to be described under the default. A Phase 2 builder reading S-09 alone could add "suggested tags" chips from the drafted list, ordered by use, and find no B18 line against it.
- **Severity:** weak point

### N14: NOTE. B19 is wired into the screen bodies but not into each screen's source index, and the B19 wording on S-03 drifts from the row

- **Check:** R-150 step 4 (worded as the row, no more); traceability under CL:23
- **Where:**
  - The "Spec source" Decisions lists were not updated. S-03 lists "B6, B7, C2, C3, C4" (SI:98), S-05 has no B19 (SI:155), S-06 has no B19 (SI:182), and S-19 lists "B3, C5" with no B17 or B18 (SI:454)
  - S-03 element 4, the unlock date (SI:108), is labelled C2 only. B19 covers the unlock date too (DN:38); C2 sets only its form (SI:663 says so)
  - SI:106 and 107 say "Spec:74 reads against it". The B19 row reads it the other way: "`Functional-Spec.md:74` read as covering the contents" (DN:38). Under the default, FS:74 does not read against showing the type and commit date. The underlying gap (G-17) is still the user's to decide, so citing FS:74 is right. Saying it "reads against" B19 is not what the row says
  - The revision log says B19 was labelled on "S-03, S-06 and the path" (SI:702). S-06 *is* the path. The screen labelled besides S-03 and S-06 is S-05 (SI:171)
- **Why it matters:** none of these builds anything the default forbids. They are the kind of drift that makes a label scan by screen give a wrong answer, and a log entry that names the wrong screen sends the next reviewer to the wrong place.
- **Severity:** note

### N15: NOTE (weakest point, stated plainly). Round 2 introduced no banned item and decided nothing silently. The weakest point is the B19/B6 conflict, which shapes a live screen

- **Check:** CL:19–24 (rule zero), R-009 (RR:109 and RR:111)
- **Where:** SI:111 (element 7), SI:126, SI:663
- **What I searched for:** every changed line in round 2 (SI:11, 106, 107, 110, 171, 199, 344, 458, 463, 565, 659, 661, 663, 698–704). I checked each one for a leak from a sealed year (a count, thumbnail, partial mark or relative date), for any engagement mechanic (badge, dot, "new" marker, reminder or countdown), for layer exposure, and for any behaviour not traced to a DN row or a source line. **I found none.** The added text only narrows (B17 removes the category, B18 removes popularity, B19 limits what the owner sees, and the N4 fix adds a ban).
- **The weakest point:** S-03 still shows element 7 ("a highlight is open") under B6, and B19 says "nothing else" (N7). Raising it at SI:663 is correct and is not a silent decision. But until the user rules, the build carries the more permissive of two provisional rows on the one screen that must leak nothing. If the user sides with B19, element 7, the `sealed · highlight open` row on S-03 (SI:126) and part of R-138's B6 line all change.
- **Severity:** note

---

## 4. Wording of B17, B18 and B19 against DN:36–38

| Row | DN wording | Inventory wording | Match |
|---|---|---|---|
| B17 (DN:36) | "Feeling tags are free text on the journey, with no category, as in the approved model (`Phase-1-Proposal.md:141`)" | SI:463 "Feeling tags as free text on the journey, with no category (`PROVISIONAL: B17`; Proposal:141)"; SI:458 "`PROVISIONAL: B17` follows Proposal:141"; SI:659 "free text on the journey, no category" | **Yes**. The other side ("inside a category") is cited only as the conflict, not held |
| B18 (DN:37) | "Tags never 'surface' by popularity. No suggestions and no counts (`Functional-Spec.md:202` over `:131`)" | SI:458 and 661 "tags never surface by popularity; no suggestions, no counts"; SI:463 bans suggested, popular or trending tags "while the owner writes" and any count | **Yes in meaning** on S-19 and OQ-38. SI:463's "while the owner writes" is narrower than the row, and S-09 is not carried (N13) |
| B19 (DN:38) | "The owner of a sealed journey sees its type, commit date and unlock date and nothing else (`Phase-1-Proposal.md:84`; `Functional-Spec.md:74` read as covering the contents)" | SI:663 "the owner sees type, commit date and unlock date, nothing else (C2 sets the unlock date's form)"; SI:106–107, 171, 199 labelled | **Yes in substance**. SI:106–107 "Spec:74 reads against it" departs from the row's own reading of FS:74. The unlock date (SI:108) is not labelled B19 (N14) |

Nothing is stretched past its row. No switch setting is extended. None of the three is switchable, and none appears on T-02 (SI:538–544). That is correct under R-141.

---

## 5. What held

- R-149 and R-150 steps 1–3 are clean (1.1–1.3)
- No label without an ID and no label outside DN
- The N4 fix on S-03 says it in the strongest form ("offered the same", SI:110)
- No new leak from a sealed year: B19 limits S-03, S-05 and S-06 to type, commit date and unlock date for the owner, and to "exists only" for others (SI:199)
- No new engagement mechanic, no image in any feed, and no layer exposure in the changed lines
- Round 2 kept to its stated scope (N1, N4 and N11), and the log says so (SI:698–704)

---

## 6. Rubric changes

None. N12 is already covered by R-138's B6 line (RR:375). N13 and N14 are covered by R-150 step 4 and R-103's B18 line (RR:762). N15 is covered by R-009 (RR:109, RR:111). No confirmed finding in this round falls outside an existing check.

**Could be automated next:** a per-screen version of R-150 step 1. For each `### S-nn` block, compare the IDs in its `PROVISIONAL:` labels with its "Spec source … Decisions" list, and compare each DN row's "Affects" screens, taken from the OQ text, with the screens that label that ID. That scan would have caught N13 and the index half of N14.

---

## Report
- Files changed: /home/user/MyJourney/docs/reviews/2026-10-30-rules-screen-inventory-r2.md
- Findings: 6
  - N2 (carried), R-142/R-068, SI:189, 200, 249, 372, 425: B2 option extended to Public photos and every reader. CONFIRMED, awaiting user
  - N3 (carried), R-145/CL:72, SI:268, 541: B9 (a) "with photographs" is a photo feed. CONFIRMED, awaiting user (G-8)
  - N12, R-138 (B6 line), SI:344: S-13 open state does not hold the start control and does not ban hiding it (risk, N4 residual)
  - N13, R-150/R-103 (B18 line), SI:660, 262, 276, 463: B18 not carried to S-09; "suggested" narrowed to "while the owner writes" (weak point)
  - N14, R-150, SI:98, 155, 182, 454, 108, 106–107, 702: per-screen source lists lack B17–B19; unlock date not labelled B19; "Spec:74 reads against it" departs from B19's reading; log names the wrong screen (note)
  - N15, CL:19–24/R-009, SI:111, 126, 663: no new violation or silent decision; weakest point is the B19/B6 conflict on S-03 (note)
- Rubric additions: none
- Verdict: FAIL
