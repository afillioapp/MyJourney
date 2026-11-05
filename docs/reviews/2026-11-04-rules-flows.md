# Rules audit: `docs/Flows.md`

Date: 2026-11-04. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-177 after this audit).

**Target:** `docs/Flows.md`, new and uncommitted, modified 2026-11-04 22:07, 704 lines. No other file was audited. `docs/Art-Direction.md` and `docs/Microcopy.md` exist in the tree and were not opened.

**Read against:** `CLAUDE.md`; `Rules-Rubric.md`; `Functional-Spec.md` in full, including §18, §19 and §20; `Phase-1-Proposal.md` in full, including §2.5; `Decisions-Needed.md`; `Screen-Inventory.md` (SI) lines 1–630, 631–735 for the OQs the flows use, and 739–744. `Overview.md` was not used (L-001).

**Verdict: FAIL.** 13 violations and 6 notes.

The sealed-year content itself is sound: Flow 4 and the plain-language opening leak nothing. The worst problems are in the file's addition beyond its brief:

- **V1, V2, V4:** the "Trying them in the prototype" table has a column headed "What you see". Three rows put banned facts in it: a sealed photo count and month number, a person's tag total, and a ring's past movement.
- **V3:** a line bars every addition to an unlocked journey, which R-174 was written to stop.
- **Copywriter:** N1 and N2 bear on `Microcopy.md`, which is already written. Whoever audits it should read them first.

---

## Auto checks run

The rubric's auto checks that need a running system (schema, API, DOM, tests) do not apply, because no code exists. These text checks do apply. Graph queries came first, as the graph rule requires.

**Graph.** `graphify query` was run for all eleven banned items, then `graphify path`. Headers only:

```
$ graphify query "sealed year leak counts"
Graph: graphify-out/graph.json (253 nodes) | Start: ['Sealed-year empty state', ..., 'Nothing leaks from a sealed year'] | 61 nodes found
NODE Nothing leaks from a sealed year [src=CLAUDE.md loc=L36 ...]
$ graphify query "layer shown to person on it"       -> 85 nodes, start 'No layer is ever shown to the person on it' [CLAUDE.md L37]
$ graphify query "reminders engagement notifications" -> 69 nodes, start 'No streaks, counters, progress bars, reminders' [CLAUDE.md L32-L33]
$ graphify query "no retakes" / "no edits to reflections" / "no comments from anyone else" / "no face recognition"
  / "no ads anywhere" / "no ranking levels badges leaderboards" / "no photo feed" / "no streaks counters progress bars"
  -> each resolves to its banned-list node plus Spec and Concept sections
$ graphify path "Flows.md" "Nothing leaks from a sealed year"
No directed path found between 'Flows.md' and 'Nothing leaks from a sealed year'.
```

The graph is stale (L-006). It places "Nothing leaks" at `CLAUDE.md` L36, but the line is `CLAUDE.md:73`, and it knows `Flows.md` only as a mention in `ux.md`. It was used only to find sections. No finding rests on a graph edge.

**Greps.** `F=docs/Flows.md`. Hits are cut short here, and each was read in full.

```
$ grep -nEi 'moments? captured|[0-9]+ *(photos?|moments?|frames?|shots?|pictures?)\b|\bof [0-9]+\b|frames? (left|used|remaining)|so far' $F     # R-006, R-098
17   Explorer (4 photos a month), Wanderer (2 a month) ...            -> describes the choice, before any year runs. Pass (S-01)
133  ... the next is refused: 9 photos so far, one a month, tenth month | Proposal:97, 228     -> FAIL, V1
140  Tagged in 6 photos, of which only the 4 not Private can be seen  -> FAIL, V2
200  no number and no hint of when a frame returns                    -> a ban. Pass
313  counts, including "3 moments captured"; frames ... used or left  -> a ban. Pass
348  There is no checklist, tick, summary or "12 of 24"               -> a ban. Pass
436  The owner sees the overviews so far                              -> an unlocked stack. Pass

$ grep -nEi 'days? (left|to go|until|remaining)|unlocks? in|countdown|time left|from now|ticking|next month|in a few|soon\b|\bin [0-9]+ days' $F     # R-013, R-140
23, 86, 205, 223, 240, 267, 313, 505, 658, 673, and 31 ("as soon as this one opens"): bans or plain facts. Pass
221  say what is about to begin, 24 hours from now                    -> N1

$ grep -nEi "don't forget|remember to|you haven't|come back|we miss|still have|waiting for you|ending soon|last chance" $F     # R-095
23   The app never reminds you to take a photo or to come back.       -> a refusal. Pass

$ grep -nEi 'unread|\bbadge|\bnew\b|\bdot\b|setAppBadge' $F     # R-096
13, 62, 76, 86, 166, 371, 417, 606, 643, 649, 667: "new" as an adjective, or a ban. No marker offered. Pass

$ grep -nEi 'streak|level up|leaderboard|\brank|\bscore|points|trending|popular|likes|followers?|comment|retake|try again|edit reflection|delete' $F     # R-124
27, 190, 192, 263, 351, 353, 399, 541, 583, 619, 639, 649, 663, 693: all refusals or conflict descriptions. Pass

$ grep -nEi 'inner circle|closest|close friend|your ring|moved? (in|out|closer|further)' $F     # R-071
29 (the owner's own map), 353, 463 (no close-friends level). Pass

$ grep -nEi 'appears? in|[0-9]+ photos? (with|of)|most tagged|people in this' $F     # R-139 aid
(no output. The aid misses Flows:140's "Tagged in 6 photos". R-176 now covers that wording.)

$ grep -nEi 'abandon|cancel|quit|pause|end early|restart|start over' $F     # R-028
257  Server restart (local prototype only)                            -> Spec §20 PPP. Pass

$ grep -nEi 'nothing is added|nothing can be added|once it unlocks|after unlock|can be added' $F     # R-174
215  `unlock-day` onward | Not offered. Nothing can be added to an unlocked journey (Proposal:99)     -> FAIL, V3
244, 276  No note can be added                                        -> names the note. Pass
65, 66, 67, 228, 341, 537: about states or highlights. Pass

$ grep -n 'Overview.md' $F     # R-136
43   `Overview.md` is never cited.                                    -> Pass

$ grep -nEi 'not picked|waits? on|none yet|\bconfirm|still open|left open|not ruled|open from|no default' $F     # R-165, R-150 step 3
127  The "jump to the next unlock" control waits on C17               -> C17 is open, so R-165 passes. Wording: N5
205, 267, 268, 321, 346, 516, 580   not picked (OQ-51, 52, parked, 33, C18, 7, 20): each is open. Pass
651  ### A. Reached by a flow, with no default                        -> OQ-20, 32 and 33 have defaults that do not
                                                                         cover what is asked (SI:642, :670, :672). Pass
163, 243: confirmation of another kind. 166, 376: "still open" of a reveal. 689: C-3. Pass

$ comm -13 <(grep -E 'PROVISIONAL: ' $F | grep -oE '\b[BC][0-9]{1,2}\b' | sort -u) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]+' | sort -u)     # R-150 step 1
B20 B22 B23 B24 B26 B9 C14 C7
   Read against F: B20, B22, B23, B26 (panel details) and C14 (Feed order, a hand-off) are not touched.
   B9: only Spec §20 Q and T are used, at Flows:584. B24: Flows:585 cites the decided §20 DD. C7: decided, §20 XXX is cited. Pass

$ comm -23 <(grep -oE 'PROVISIONAL: `?[BC][0-9]{1,2}' $F | grep -oE '[BC][0-9]+' | sort -u) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]+' | sort -u)     # labels with no ID in the table
(no output) Pass

$ grep -rlE '\bC-[0-9]+\b' docs/*.md     # V11
docs/Art-Direction.md   docs/Flows.md   docs/Status.md
   Status.md:46 only points to Flows.md. No earlier doc owns C-n.

$ # §20 letters never cited in Flows (R-165 (3))
V W Y Z AA BB FF II KK MM NN OO QQ RR BBB FFF LLL MMM OOO SSS TTT
   Read each. All are data, panel or Positivity Feed rulings with no step in a flow, or residuals with no screen. Carriage passes.
```

---

## Violations

### V1. A sealed count, cadence and month number listed as what you see

- **Check:** R-006, R-012, R-098; new R-176. `CLAUDE.md:73`.
- **Where:** `Flows.md:133`. The column is "What you see"; viewing as Steady Lantern, flows 2, 3, 4: "Sealed journey #6. One press is accepted, then the next is refused: 9 photos so far, one a month, tenth month".
- **What is wrong:** "9 photos so far" is the sealed journey's count. "tenth month" is R-012's "month 7 of 12". "one a month" is the cadence that S-03 withholds beside a running year (SI:118, `Flows.md:292`). The row covers Flow 4, the screen whose test at `Flows.md:313` bans all three.
- **Why it breaks the rule:** the fixture does hold these facts (Proposal:228), and a doc may state them. It may not state them as what the viewer sees. This section addresses a reader who "has never heard of the product" (`Flows.md:7`), and it tells them the opposite of `Flows.md:15`, "Not a preview, not a number". A developer building to this table has a line saying the count is on screen. SI's equivalent table carries the disclaimer this one lacks: "This table is for the reader of this inventory. The panel shows none of it" (SI:537).

### V2. A tag total and a private photo's existence, listed as what a tagged reader sees

- **Check:** R-139, R-147, R-071; new R-176. `CLAUDE.md:74`.
- **Where:** `Flows.md:140`. Viewing as Second Wind on Steady Lantern #1, "What you see": "Tagged in 6 photos, of which only the 4 not Private can be seen".
- **What is wrong:** under either B12 setting Wind sees neither figure. Under "shown" Wind sees a mark on 4 photos in place, with no total (`Flows.md:567`, R-139). Under "hidden" Wind sees nothing. Wind must never learn that 2 Private photos tag him.
- **Why it breaks the rule:** the row states a total that fixes a ring, since 6 is 5+, tight (Spec §12). It does so while viewing as the person on that ring. It is the flow's own worked example of the moment R-139 exists to protect.

### V3. "Nothing can be added to an unlocked journey"

- **Check:** R-174. Also a citation that does not hold.
- **Where:** `Flows.md:215`, cited to Proposal:99.
- **What is wrong:** Proposal:99 says "nothing can be **captured** after unlock". The flow widens it to everything. Tags, chapters, feelings, visibility, reflections and overviews are all added to an unlocked journey: Flow 5 and Flow 6 in this same file.
- **Why it breaks the rule:** R-174 exists for exactly this sentence: a general bar on writes after unlock must name the photo and the note. Spec §20 YYY was reworded on 2026-10-31 for the same reason ("the reveal is unaffected"). R-174's own grep list holds "nothing is added", so the words here are one token away.

### V4. A ring's past movement listed as what you see

- **Check:** R-150 under `PROVISIONAL: C8`; new R-176.
- **Where:** `Flows.md:137`. Viewing as Steady Lantern at baseline, "What you see": "Second Wind's ring, which drifted out and came back".
- **What is wrong:** C8 says "current rings only: no counts, no history, no drift". At baseline Lantern sees Wind on the tight ring, and nothing else. The file says so itself at `Flows.md:484`: "Lantern sees only the current ring, never this table".
- **Why it breaks the rule:** the drift is pre-baseline fixture history (Proposal:264–270). The clock is forward only (Proposal:195), so no panel move reaches it either. Under C8 the demoer can see a ring move only as two current states on either side of a finished reveal. The row also carries no C8 label.

### V5. The plain-language opening states provisional defaults as fact

- **Check:** R-150 ("labelled `PROVISIONAL: <ID>`"); `CLAUDE.md:26`.
- **Where:** `Flows.md:19, 23, 25, 27, 33`. The only label is one line at `Flows.md:35`: "Some details above are working defaults the product owner is still comparing. The flows below label them."
- **What is wrong:** that line does not say which details. A reader cannot tell a default from a ruling.

| Line | Stated as fact | Default |
|---|---|---|
| 19 | "You get one go at it" | C4 |
| 23 | "the day you started, the day it opens" | B19, C2 |
| 25 | "a line tells you your journey is ready" | C1 |
| 25 | "it has no deadline" | B3 |
| 25 | "anyone using the app" | B14 |
| 25 | "Each choice can be made only once, and the app says so before it saves" (the second half) | C5 |
| 25 | "Until you decide, a photo can be read by the people on your map" | **B2, switchable** |
| 27 | "A ring is added to the circle" | **B4, switchable** |
| 27 | "the year's line of activity is bent into it" | B5 |
| 33 | "may find they were there in your hard year" | **B12, switchable** |

- **Why it breaks the rule:** the three switchable rows become false when the panel is flipped, in the one section that "needs nothing else" (`Flows.md:7`). Plain words are what the gate asks for, and this is not an objection to them. The objection is that the section's label names no IDs. I checked the promise "the flows below label them": each item above is labelled further down. So the fault is limited to the opening.

### V6. Unlabelled defaults in the prototype table and the state tables

- **Check:** R-150; R-141 to R-148 (a switchable default must hold under both settings).
- **Where:**
  - `Flows.md:139`: "No rings; no ring for the unfinished journey" is B4's default, with no label.
  - `Flows.md:140`: depends on B12 and C6, with no label.
  - `Flows.md:141`: "A network reader before the reveal is finished" is B2's default. Under the option Open Hands reads nothing. No label.
  - `Flows.md:105`: the diagram has the ring arriving at finish. That is B4's default, with no label.
  - `Flows.md:320`: labelled, but states only the default's outcome, "the owner's circle has no rings". The table at `Flows.md:50` does not list Flow 4 among those B4 changes.
  - `Flows.md:520`: "Name, no rings" for a user who never committed, with no label. It is false under "per year with the app" once such a user passes a year (SI:174). `Flows.md:514` states that option but does not carry it to this row.
  - `Flows.md:522, 523, 592`: refer to "B4's default" or "B2's setting", or state the outcome, with no `PROVISIONAL:` label.
- **Why it breaks the rule:** the table at `Flows.md:47–54` is the only place that says what each switch changes. Rows that hold under one setting and do not say so read as decided. The prototype table is where a demoer would notice this, and it is the one with no labels at all.

### V7. FQ-8 reopens a question C5 answers

- **Check:** R-150 ("never calls such a question open").
- **Where:** `Flows.md:678` ("Does the line need its own press, and does it repeat every time?") and `Flows.md:354`.
- **What is wrong:** C5's question in `Decisions-Needed.md:152` is "Is the owner asked to confirm each set-once choice?". The default at `Decisions-Needed.md:43` answers it: "Each set-once choice shows a one-line 'this can't be changed' before it is saved". So "does it repeat" is answered, and `Flows.md:354` already assumes it ("the same weight each time"). "Its own press" is the confirm question the default answers with a line and no press.
- **Why it breaks the rule:** FQ-8 sits under "Nothing below was picked". The concern about volume is real and the user should hear it, but as a challenge to C5 under its label, not as an open question.

### V8. Leaving the camera or note step after the unlock instant: settled by implication, not raised

- **Check:** R-134, R-171; rule zero, `CLAUDE.md:17`.
- **Where:** `Flows.md:194` ("They press again or leave to S-03"), `:208` ("at S-03 when the owner leaves"), `:254` (end 3, "That screen").
- **What is wrong:** Spec §20 CCCC says the next press after the unlock instant is not taken and the app goes to the profile. A press on the control that leaves the camera or the note step is a press. Nothing says whether it is CCCC's "next press". SI OQ-52 (SI:735) asks this about the skip only. FQ-3 (`Flows.md:673`) asks about presses on S-03 and S-13, not about the way out of S-02 and S-12.
- **Why it breaks the rule:** the flow sends this press to S-03, or to "that screen". Its own table says S-03 is gone by then: `Flows.md:333`, "Gives way to Reveal S-04, reached on the next open through S-05". Note end 3 also overlaps end 7, so "S-12 lists exactly these seven" does not say which applies. This is the same family as OQ-51, OQ-52 and FQ-3, and it needs its own question.

### V9. Flow 2a has no end, and the refused owner has nowhere to go

- **Check:** R-134.
- **Where:** `Flows.md:219–228`; the shape promised at `Flows.md:41`.
- **What is wrong:** every other flow has an "Ends" line, and Flow 2a does not. Its refusal at `:226` names no destination. SI:357 gives S-13 one exit, "Leads to: Capture S-02". So the only documented way out for an owner refused a highlight, or one who reaches S-13 and decides not to start, is the camera.
- **Why it breaks the rule:** that is a behaviour nobody decided, and it is not raised. FQ-2 and FQ-3 touch S-13 but not this. `Flows.md:649` says each flow "adds nothing at these points", and this gap is not listed among those points.

### V10. "Exactly this and nothing more" does not hold

- **Check:** R-168, R-135.
- **Where:** `Flows.md:290` against `Flows.md:304`.
- **What is wrong:** `:290` says S-03 "holds exactly this and nothing more (SI S-03, elements 1–9)". `:304` offers a tenth element, the way to S-05. Elements 5, 6 and 8 name the ways out, and S-05 is not one of them.
- **Why it breaks the rule:** the conflict is inherited from SI, where S-03 lists S-05 under "Leads to" (SI:111) and then gives "Exactly this list" (SI:113). The flow cites the list and uses the way out without raising it. This matters more than most: the way to S-05 is how an owner in a sealed year reaches earlier journeys (C3), and the list is the screen's leak test. Do not pick here. It goes to the supervisor.

### V11. C-1 to C-13 are new IDs, called existing, and they collide with Decisions IDs

- **Check:** new R-177; R-134; L-002.
- **Where:** `Flows.md:649` ("SI OQ-n and C-n are existing IDs"), `:685–699`; used at `:138` ("see C-13") and `:366` ("C-3").
- **What is wrong:** C-1 to C-13 first appear in this file. `Status.md:46` only points back to it, and `grep` finds no earlier owner, so the statement at `:649` is false.
- **Why it breaks the rule:** they sit one hyphen from `Decisions-Needed.md` C1 to C18, in a file that labels `PROVISIONAL: C3`, `C4`, `C6`, `C8`, `C9`, `C10`, `C11`, `C12` and `C13`. "C-13" is a conflict about First Light's map, and C13 is the follow-up default. `Flows.md:366` cites "C-3" while `:304` cites `C3`. A reader acting on the wrong one acts on a different rule.

### V12. The status line names no §20 range

- **Check:** R-165 (2).
- **Where:** `Flows.md:3`.
- **What is wrong:** it does not say the file carries §20 up to DDDD, or why later letters do not bear. Carriage itself passes: DDDD is the latest ruling and is cited, and the uncited letters do not bear on a flow (see the grep above). Only the statement is missing.
- **Why it breaks the rule:** two rounds of this project's audits found §20 rulings recorded after a doc's last edit. This line is what makes that checkable.

### V13. "Naming people draws your map"

- **Check:** R-134; Spec §20 7, G, §7, §12.
- **Where:** `Flows.md:29`.
- **What is wrong:** naming someone by typed name never counts (Spec §20 7), and `Flows.md:25` has just told the reader they "name, by hand, who is in each picture". Tagging also draws nothing until the reveal is finished (`Flows.md:467`, Spec §12).
- **Why it breaks the rule:** the sentence states a general rule that two rulings contradict, in the section a new reader relies on alone.

---

## Notes

These are not violations as they stand, but each is a place one could slip in. N1 and N2 are aimed at a deliverable already written.

- **N1. R-140, `PROVISIONAL: B6`: `Flows.md:221`, "say what is about to begin, 24 hours from now".** This is a copy brief, not a display, and S-13 may state the window's length (SI:361). But the wording asks for a relative end time, and it can be read as a start 24 hours away. It also cannot be true on every press. A highlight started under 24 hours before unlock is cut off at unlock (Proposal:133), and S-13 must look the same regardless (R-138), so a stated "24 hours" would then be wrong. S-13 also looks the same while a highlight is open. Check how `Microcopy.md` took this.

- **N2. `Flows.md:643`, the list of places with no copy.** Every item on it holds against its source. Item by item:
  - **Sources:** VVV, UUU, RRR, YYY, CCCC, WWW, DDDD, DDD, HHH and C8 hold. Spec §14 and R-102 ban a reward rather than a line, so "no line" is a stricter reading, which is allowed.
  - **Missing:** an accepted shutter (`Flows.md:193`; VVV says "as after capture"); the camera open at the unlock instant, since the list says "note window" only and CCCC bans a message on the camera too (SI:99); a highlight closing, or filling and falling through to a normal frame (`Flows.md:202`, R-140, §20 U); Commit opening again (`Flows.md:153`, R-095, R-096).
  - **Imprecise:** "a lost press" carries the normal note offer or refusal copy. Only its loss is silent.

  A reader of this list could take anything absent as open for a line. Check `Microcopy.md` against the four missing places.

- **N3. R-134: `Flows.md:19` tells a new reader "within 15 minutes", and `:240`'s copy brief says only "No time left."** No source says whether the note offer may state the 15 minutes as a plain fact. R-140 bans a countdown, not the length. It matters: an owner who walks off to write, unaware, comes back to a press "simply not taken" with no line (`Flows.md:255`). "No time left" also reads badly out of context. Not raised as an FQ. It should be.

- **N4. `Flows.md:21`, "the monthly limit is lifted".** The highlight's cap at the yearly quota (Spec §20 5) is not mentioned. Spec:65 uses similar words, so this is not a contradiction, but a new reader is told there is no limit.

- **N5. `Flows.md:127`, "the 'jump to the next unlock' control waits on C17".** The sources say more narrowly: "T-01 still holds the jump (Proposal:195); panel acceptance waits on C17" (SI:691), and "is still built while Decisions C17 is open" (SI:533). SI:99 uses the jump to reach the very branch at `Flows.md:205`. It does not pick a side of C17, but it reads as though the control is withheld. It should say that the control exists and only its acceptance waits.

- **N6. Weakest points, reported because the rubric requires them.**
  - **R-139 / G-12:** B12's "shown" still lets a reader count by reading. `Flows.md:585` says so plainly.
  - **R-151 residual:** `Flows.md:564` gives non-owners the capture date, so Lantern #1's 19 photos dated one day still suggest a highlight, despite `:585`. The file does not mention this. It waits on the user.
  - **B11, default named:** `Flows.md:471` says the crossed person learns they are on the map. It does not say that every other network member learns it too. `Flows.md:29`, "Only you ever see your map", holds for the map and rings but not for who is on it. R-146 accepts this, so it is not a violation, but a new reader is not told.

---

## What the brief asked to check

**Leaks from a sealed year.** Flow 4 is clean: `:290–299`, the test at `:306–311` and the list at `:313` meet R-006 to R-013. The opening is clean too: `Flows.md:15, 19, 21, 23` carry no count, thumbnail or frames left, and nothing varies with the number of photos. `:23` says "No pictures, no count, no countdown". S-03 stays the same before and after a capture (`:318`). Others see "exists only" (`:324`, `:538`, `:591`). The leaks are in the table: V1.

**Engagement mechanics.** None offered. Reminders, dots, "new" markers and countdowns appear only as bans (`:86`, `:153`, `:346`, `:384`, `:417`, `:521–525`). "Your Journey is ready" stays under C1, with R-095's condition carried (`:346`).

**Layer exposure.** Flow 7 is clean: `:462`, `:471`, `:484`, `:541`, `:585`. The exposure is in the table: V2.

**No-default questions.**

| Question | Result |
|---|---|
| C17 | Not settled. Wording at N5 |
| C18 | Not settled. `:346` and `:522` mark it. `:25` "the next time" is C1's wording |
| SI OQ-51 | Not settled. `:205`, `:657` |
| SI OQ-52 | Not settled. `:258` is read with `:267`, which flags it |

The neighbouring gap the file does not flag is V8.

**L-002's two stale traps: the ux worker's report holds.**

- `Functional-Spec.md:104–111` now gives "Any time in slot 1, 1 Sep 2019 to 1 Sep 2020", on slots.
- `My-Journey-Concept.md:807` now carries "*(superseded 2026-10-25: see §29 and Functional-Spec §20 H)*". So do `:200`, `:203` and `:383`.
- `Flows.md:703` is correct. The index line at `Learnings/index.md:14` still lists both as traps, and that is the stale part. It is outside this audit.

**Citations.** About 60 were opened in the source: Spec, Proposal, Concept 115, 140, 362, 365–367, 423, 582, 687, 694, 704, 706, 807, 860; Brief 115–122, 130; `Build-Plan.md:78`; `Phase-1-Amendments.md:576`; r10 lines 161, 181, 262; `Status.md`; R-143; G-11, G-12, G-27, G-28; the SI rows and OQs. Two do not hold: `:215` (V3) and `:649` (V11). One is loose: `:127` (N5). The rest hold. That includes the ones most likely to fail: `Phase-1-Amendments.md:576` does say the device reads the unlock date, and `Concept:860` does carry "a tag never gives the tagger access".

**The prototype table (`:129–141`).**

| Rows | Result |
|---|---|
| 131, 132, 134, 135, 136, 138 | Hold against the fixture and need no label |
| 133, 140 | V1, V2 |
| 137 | V4 |
| 139, 141 | V6 |

It invents no control. T-01 and T-02 exist as cited.

**The no-copy list (`:643`).** N2.

**Index of weighted moments (`:614–641`).** All 20 SI entries (SI:741) are present, split into 26 rows. "Three type descriptions" comes from S-01. Pass.

**Other checks read and passed:** R-024, R-029 to R-034, R-036, R-037, R-040 to R-048, R-049 to R-058, R-059 to R-068, R-072 to R-083, R-084 to R-093, R-102, R-104, R-105 to R-109, R-112, R-121, R-122, R-125, R-128, R-133, R-136, R-142 to R-148, R-151, R-152, R-154, R-155, R-160, R-161, R-162, R-166, R-170, R-171 (except V8), R-173. R-175 does not bear: `Flows.md` assigns the skip request to no screen, and S-12 holds it (SI:341).

---

## Rubric additions

- **R-176:** a doc's description of what a viewer sees holds only what that viewer's screen may show. From V1, V2, V4.
- **R-177:** a new ID is declared as new and cannot be misread as an ID from another family. From V11.

R-176 is added to the "Nothing leaks" and "No layer" rows of Banned-list coverage. Nothing was removed or renumbered.

---

## Report
- Files changed: `docs/reviews/2026-11-04-rules-flows.md` (new); `docs/Rules-Rubric.md` (R-176, R-177, one dated log line, two coverage rows)
- Findings: 19 (13 violations, 6 notes)
  - V1 R-006, R-012, R-098, R-176, `docs/Flows.md:133`: "What you see" lists 9 photos so far, one a month, tenth month for a sealed journey
  - V2 R-139, R-147, R-176, `docs/Flows.md:140`: "What you see" lists a tagged reader's total of 6, and 2 Private photos, which fixes a ring
  - V3 R-174, `docs/Flows.md:215`: "Nothing can be added to an unlocked journey"; Proposal:99 says only captured
  - V4 R-150 (C8), R-176, `docs/Flows.md:137`: "What you see" lists a ring's drift, which C8 bans and the file's own line 484 denies
  - V5 R-150, `docs/Flows.md:19, 23, 25, 27, 33, 35`: opening states defaults as fact, including switchable B2, B4, B12; the blanket label names no IDs
  - V6 R-150, `docs/Flows.md:105, 139, 140, 141, 320, 520, 522, 523, 592, 50`: unlabelled defaults; line 520 is false under B4's other setting
  - V7 R-150, `docs/Flows.md:678, 354`: FQ-8 reopens what C5 answers
  - V8 R-134, R-171, `docs/Flows.md:194, 208, 254`: leaving the camera or note step after unlock is sent to S-03, which line 333 says is gone; not raised
  - V9 R-134, `docs/Flows.md:219-228`: Flow 2a has no end; a refused owner's only documented exit is the camera; not raised
  - V10 R-168, R-135, `docs/Flows.md:290, 304`: "exactly this and nothing more", then a tenth element; inherited from SI:111 against SI:113; goes to the supervisor
  - V11 R-177, R-134, `docs/Flows.md:649, 685-699, 138, 366`: C-1 to C-13 are new, called existing, and sit one hyphen from Decisions C1 to C18
  - V12 R-165 (2), `docs/Flows.md:3`: status line names no §20 range; carriage itself passes
  - V13 R-134, `docs/Flows.md:29`: "Naming people draws your map", against Spec §20 7, §12
  - N1 R-140, B6, `docs/Flows.md:221`: copy brief "24 hours from now"; false near unlock; check `Microcopy.md`
  - N2 `docs/Flows.md:643`: no-copy list holds but omits accepted shutter, camera at unlock, highlight closing or filling, Commit reopening; check `Microcopy.md`
  - N3 R-134, `docs/Flows.md:19, 240, 255`: whether the offer may state 15 minutes is not raised
  - N4 `docs/Flows.md:21`: highlight cap not mentioned to a new reader
  - N5 `docs/Flows.md:127`: "control waits on C17" is looser than SI:533, SI:691
  - N6 R-139 / G-12, R-151 residual, B11, `docs/Flows.md:585, 564, 471, 29`: weakest points, not violations
- Rubric additions: R-176, R-177
- Verdict: FAIL
