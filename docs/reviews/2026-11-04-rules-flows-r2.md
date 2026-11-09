# Rules audit: `docs/Flows.md`, round 2

Date: 2026-11-04. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-178 after this audit).

**Target:** `docs/Flows.md` after revision round 1, modified 22:24:58, 735 lines. It is untracked, so no diff exists: the changes were found by reading the file against the r1 text. Lines that did not change were not re-audited.

Previous audit: `docs/reviews/2026-11-04-rules-flows.md` (FAIL: V1–V13, N1–N6).

**Verdict: FAIL.** 6 violations and 6 notes.

All 13 r1 violations are fixed, with one part-exception: half of r1 V7 was my own error (r2 V4). None of the six new violations puts a banned thing on a screen. Five were made by the fixes, and the sixth went stale after them:

- **V1:** the new column header says "never on any screen" over facts that do reach a screen. Two rows contradict a ruling or a default. The wording of my own R-176 invited this.
- **V2, V3:** the new "for now" wording landed on a counter ban and on a §20 ruling, so the opening now tells a new reader a count might yet appear.
- **V4:** "no press of its own" is not in C5's row. It came from my r1 V7, and the ux worker followed it.

---

## Each r1 finding, against the current file

| r1 | Now at | Result |
|---|---|---|
| V1 sealed count as "what you see" | `:155` | **Fixed.** "On screen" holds type, plain dates, camera, note offer or a refusal with no number. The figures moved to the setup column |
| V2 tag total | `:163` | **Fixed.** "On screen" is a mark in place, with no total. The setup column says neither figure is ever shown to Wind |
| V3 "Nothing can be added" | `:238` | **Fixed.** "Nothing can be captured after unlock (Proposal:99). Reveal writes go on". The citation now holds |
| V4 ring's drift | `:159` | **Fixed.** Current ring only, labelled C8 |
| V5 opening's defaults | `:19–33`, `:37–53` | **Fixed**, with new faults: r2 V2, V3 |
| V6 unlabelled defaults | `:131`, `:161–164`, `:68`, `:347`, `:393`, `:547`, `:549`, `:550`, `:619` | **Fixed.** The greps below find no unlabelled use on a state or table row |
| V7 FQ-8 | `:381`, `:705` | **Part fixed.** Repetition holds. "No press of its own" does not: r2 V4 |
| V8 leaving after unlock | `:228`, `:231`, `:274`, `:280`, `:294`, `:707` | **Fixed**: shown, not settled (below) |
| V9 Flow 2a end | `:252`, `:254`, `:708` | **Fixed**: shown, not settled (below) |
| V10 "exactly this" | `:317`, `:331`, `:730` | **Fixed**: shown, not settled (below). The decision is the user's |
| V11 C-n IDs | `:676`, `:717–730` | **Fixed.** R-177's scan is clean for this file. One new false pointer: r2 V6 |
| V12 status line | `:3` | **Fixed.** DDDD is still the latest ruling (`Functional-Spec.md:366`) |
| V13 "Naming people" | `:29` | **Fixed** (below) |
| N1 "24 hours from now" | `:244` | **Fixed**, with one question left: r2 N1 |
| N2 no-copy list | `:670` | **Fixed.** All four missing places are added, and the lost-press wording is precise |
| N3 15 minutes | `:266`, `:267`, `:709` | **Fixed.** Raised as FQ-12. `Microcopy.md` Q-1 (`Microcopy.md:217`) is the same question, as `:709` says |
| N5 C17 wording | `:147` | **Fixed.** Matches SI:533 and SI:691 |
| N4, N6 | | Not claimed as addressed, and they stand: r2 N2, N3 |

---

## What the brief asked to test

**The setup column: does it break anything, given the file is read by people?** The sealed count and tag figures do not. They are the fixture's own (Proposal:228, :266), every copy of them is now marked as off-screen, and R-006 and R-139 govern what the product shows. A person reading `:155` now learns that the count exists and that the screen withholds it, which is correct. The column's header is the fault: r2 V1. It is also the place a demoer learns how many frames are left, which is a fair use of a fixture note.

**The opening and the section at `:37`.** The section at `:37–53` is accurate. Each of its 11 rows matches its Decisions row, and each ID is labelled again in the flows, as `:39` promises. I found no default in the opening that it misses. "whatever feelings fit" at `:25` leans on B17 but does not state free text. The opening's leak test still passes. Two uses of "for now" are wrong: r2 V2, V3.

**Flow 2a Ends, FQ-10, FQ-11, FQ-12 and DC-14.** All five show the gap without settling it:

- **`:254`** says the camera is "the only way on that SI gives this screen", which is SI:357, and sends anything else to FQ-11. It does not say a refused owner goes to the camera. Weakest point: r2 N4.
- **FQ-10 (`:707`)** names both readings of the press and does not lean. `:280` limits end 3 to "before the unlock instant". `:231` limits S-03 to "while the journey is sealed". One loose end: r2 N5.
- **FQ-11 (`:708`)** is unsettled. Its `Proposal:135` supports the refusal, not the way out, but SI S-13 carries the claim.
- **FQ-12 (`:709`)** is unsettled. `:266` and `:267` assert nothing about telling the owner. "You have up to 15 minutes" at `:19` sits in a section marked "not product copy" (`:13`).
- **DC-14 (`:730`)** cites both SI lines and picks neither. `:331` keeps the way out as a bullet, marked **Gap**. Its claim that S-05 is reachable anyway holds: SI:170 lists the core of Layers, and C12 the next open.

**`:29`, "When you finish, the people you named who are on the app are placed on your map".** It passes.

| Test | Result |
|---|---|
| Spec §20 7: typed names never count | "A name you only typed in never counts" |
| Spec §12: computed when a reveal is finished | "When you finish". A reveal never finished changes nothing (§20 9) |
| Spec §12: any user counts, with or without a journey | "who are on the app" |
| Spec §20 L: straight to the ring the count gives | "placed", then the three thresholds |
| Spec §12: drift, nobody drops off | Next sentence, unchanged |

It leaves out that tagging yourself never counts (Proposal:156) and that Private photos count. Neither omission misstates a rule. The B11 point in r2 N3 stands next to it.

**FQ-8 at `:705`, and "C5 answers confirmation and repetition".** Repetition holds. Confirmation does not, as stated: r2 V4.

---

## Auto checks run

The rubric's auto checks that need a running system do not apply. Graph first (still stale, used only to find sections; L-006):

```
$ graphify query "sealed year leak fixture setup prototype table"
Graph: graphify-out/graph.json (253 nodes) | Start: ['Sealed-year empty state', 'Nothing leaks from a sealed year', ...
```

`F=docs/Flows.md`. Hits are cut short, and each was read in full.

```
$ grep -nEi 'moments? captured|[0-9]+ *(photos?|moments?|frames?|shots?|pictures?)\b|\bof [0-9]+\b|frames? (left|used|remaining)|so far|holds [0-9]+' $F     # R-006, R-098
3    (no count: matches "Revision round 1 of 3")                      -> Pass
17   Explorer (4 photos a month)                                      -> the choice, before any year runs. Pass
155  Fixture setup: Journey #6 holds 9 photos ...                     -> under the setup column. Pass (R-176)
163  Fixture setup: Wind is tagged in 6 photos ...                    -> under the setup column. Pass (R-176)
223, 340, 375: bans. 463: an unlocked stack. Pass

$ grep -nEi 'days? (left|to go|until|remaining)|unlocks? in|time left|from now|time remaining|next month|\bin [0-9]+ days' $F     # R-013, R-140
228, 231, 280, 293, 294, 340, 532, 670, 685, 700, 707: "the unlock instant", or bans. 266: "no time remaining", a ban. Pass
   "24 hours from now" is gone.

$ grep -nEi 'nothing is added|nothing can be|once it unlocks|can be added' $F     # R-174
238  Nothing can be captured after unlock (Proposal:99). Reveal writes go on   -> Pass
270, 303  No note can be added                                        -> names the note. Pass

$ grep -nEo '.{50}([Ff]or now|the plan is|still being compared).{60}' $F     # R-178
21  ... the app refuses the picture. For now it does so without saying how many you have used.   -> FAIL, V2
23  For now it shows what you chose, the day you started and the day it opens   -> B19, C2. Pass
25  For now, the plan is that a line tells you your journey is ready  -> C1. Pass
25  For now, none of it is compulsory and it has no deadline          -> FAIL in part, V3
25  which for now means anyone with an account                        -> B14. Pass
25  still being compared: for now they can                            -> B2. Pass
27  still being compared: for now, finishing adds one                 -> B4. Pass
33  still being compared. For now, they can                           -> B12. Pass

$ grep -oE '\bC-[0-9]+\b' $F     # r1 V11
(no output)
$ comm -12 <(grep -oE '\b[A-Z]{1,3}-[0-9]+\b' $F | tr -d - | sort -u) <(grep -oE '\b[A-Z]{1,2}[0-9]{1,2}\b' docs/Decisions-Needed.md | sort -u)     # R-177
Q1    -> Flows:709 quoting Microcopy.md's Q-1. Not minted here: r2 N6

$ sed -n 46p docs/Status.md     # the pointer at Flows:676
... Open questions FQ-1 to FQ-12 and DC-1 to DC-14 listed there   -> no C-n: FAIL, V6

$ comm -13 <(grep -E 'PROVISIONAL: ' $F | grep -oE '\b[BC][0-9]{1,2}\b' | sort -u) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]+' | sort -u)     # R-150 step 1
B20 B22 B23 B24 B26 B9 C14 C7     -> same as r1, and read against the same lines. Pass

$ grep -nE "\b(B[0-9]{1,2}|C[0-9]{1,2})('s)?\b" $F | grep -v PROVISIONAL     # bare IDs
67–72 (the switch table), 559, 612, 676, 682, 683, 689, 691, 692, 699, 700, 703: decided rulings under either setting, or IDs
named in open questions. None states a default's outcome as fact. Pass

$ sed -n 43p docs/Decisions-Needed.md; sed -n 152p docs/Decisions-Needed.md     # V4
| C5 | Nothing is required before finishing a reveal. Each set-once choice shows a one-line "this can't be changed" before it is saved | no |
**C5. Finishing a reveal.** Is anything required before finishing, such as a chapter? Is the owner asked to confirm each set-once choice? (Inv 17, 18)
   -> no "press" in either line: FAIL, V4
```

---

## Violations

### V1. "Never on any screen" is false for most of the column it heads

- **Check:** R-176 (`Updated` this round); R-134. Against Spec §20 SS, `PROVISIONAL: B11`, R-089.
- **Where:** `Flows.md:149` ("It appears on no screen") and `:151` ("Fixture setup: never on any screen"), over `:154–164`.
- **What is wrong:** three rows hold facts that are truly never shown: `:155`, `:159`, `:163`. The others do not.

| Line | The fact under "never on any screen" | Where it reaches a screen |
|---|---|---|
| `:160` | Open Hands' tag "puts her on Hands' map" | Under B11's default, "path crossed" names both people and reaches Hands' network (R-089), which she has just joined. `:498` says "the crossed person learns they are on the map". No B11 label on the row |
| `:164` | "#4's reveal is not finished", viewing as Open Hands | Spec §20 SS: readable by the owner's network after unlock. `:564` says so |
| `:164` | "Hands is on Round's map" | Hands reads Round's Network photos, which is the row's own "On screen" |
| `:154`, `:157` | "last reveal unfinished", "never finished", viewing as the owner | The owner sees it: the way into the open reveal is the row's own "On screen" |
| `:156` | "#6 unlocks" | The same row's "On screen" |
| `:158` | "Five reflections" | The owner reads all five. Only a printed count is barred |

- **Why it breaks the rule:** a developer who takes the header at its word hides from the network what §20 SS lets it read, or drops First Light's named announcement. The disclaimer protects only if it is true. The fault started with me: R-176 asked such a table to say its facts "appear on no screen", without limiting that to the facts a screen may not show. R-176 now says so.

### V2. "For now" on the counter ban

- **Check:** new R-178; R-038; `CLAUDE.md:24`, `:69`, `:73`; the rubric's "No default may weaken a banned-list check".
- **Where:** `Flows.md:21`, "the app refuses the picture. For now it does so without saying how many you have used." `:39` defines "for now" as "what is not yet decided".
- **What is wrong:** the sentence tells a new reader that a count of photos used might yet appear. Yet `capture()` returns only `accepted` or `refused` in the approved model (Proposal:49), and §2.5 check 5 fails the build otherwise. R-038's reading of B7 is "Holds as written". The file contradicts itself two lines on: `:23` says "No pictures, no count, no countdown", with no hedge.
- **Why it breaks the rule:** B7 is a real provisional row, and its label at `:44` is correct. What is open under B7 is the wording of a refusal, and whether Spec:243's "reads as a target" leaves any room is a question R-178 says is not to be hedged in front of a reader. A default's label does not make a banned item undecided. This came from fixing r1 V5, where I listed C4, B3 and others but not B7: the worker added B7 correctly and over-applied the marker.

### V3. "For now" on a §20 ruling

- **Check:** R-165 ("No build doc calls a decided question open"); new R-178.
- **Where:** `Flows.md:25`, "For now, none of it is compulsory", and `:47`, which labels "Nothing compulsory" as C5 alone.
- **What is wrong:** "none of it" covers reflections and the overview. Those are decided: the overview is optional (Spec §20 O), "A reveal can be finished without one"; a reflection is never pushed (Spec:102), and `CLAUDE.md:105` says "Both are optional". Spec §20 9 also lets a reveal stay unfinished. C5 is open only for what else might be required before finishing, "such as a chapter" (`Decisions-Needed.md:152`).
- **Why it breaks the rule:** under `:39`'s own definition, the sentence calls a ruling undecided and tells the reader reflections might become compulsory. "it has no deadline" (B3) is correctly marked, in the same sentence.

### V4. "No press of its own" is not in C5

- **Check:** R-150 ("never extends a default or a switch setting to cases its row does not name"; step 4, "each labelled passage says what its row says, no more").
- **Where:** `Flows.md:381` ("The line asks for no press of its own (`PROVISIONAL: C5`)") and `:705` ("with no press of its own (`Decisions-Needed.md:43`, `:152`; `PROVISIONAL: C5`)").
- **What is wrong:** C5's row says the line shows before the choice is saved. `:152` is only the question. Neither says anything about a press, and SI S-18 to S-21 do not either, so the citation does not hold for that clause. FQ-8 also undoes the claim: it keeps open "whether saving is a separate act", and a separate act of saving, taken after the line shows, is the press `:381` says does not exist.
- **Why it breaks the rule:** a reading the row does not state is raised as a question, not labelled as the default. **This one is mine.** r1 V7 said: "'Its own press' is the confirm question the default answers with a line and no press". That was my inference, not the row's words, and the worker carried it into the file.
- **Corrected reading of r1 V7:** C5 answers **repetition** ("Each set-once choice"), so FQ-8 was right to drop it, and that part of `:705` holds. On **confirmation**, C5 says a line shows. It does not say whether that line needs answering. That stays open, or goes to the user, and it is one question with "what act saves a choice", not two.

### V5. The new "On screen" column drops the "ready" line for Long Way Round

- **Check:** R-134; rule zero; a no-default question settled by implication (C18).
- **Where:** `Flows.md:154`, `:157`, against `:156` and `:549`.
- **What is wrong:** `:549` puts "Your Journey is ready" on S-05 in `reveal-open`, marked "C18 open". Round #4 is `reveal-open` at baseline. `:156` shows the line for Lantern at unlock and tags it `C18 open`. `:154` and `:157` list Round's profile and reveal without the line and without the tag, and Round has already been back since unlock (Proposal:246, 2026-09-10).
- **Why it breaks the rule:** read together, these rows show the line once and then gone, which is one of the answers C18 leaves open, and `:149` makes this column the reference for what a screen holds. Under "every open until the reveal is finished", `:154` would be wrong. These rows were new in this round.

### V6. A pointer that is already false

- **Check:** R-134; L-002.
- **Where:** `Flows.md:676`, "`Art-Direction.md:597–600` and `Status.md:46` still use it."
- **What is wrong:** `Status.md:46` now reads "DC-1 to DC-14". It was edited at 22:25:32, 34 seconds after this file, so this was true when written. `Art-Direction.md` still uses it and is being handled, which will make the rest false too.
- **Why it breaks the rule:** a doc's statement about another doc's current text goes stale with no one watching it. It is a one-line matter, and the sentence need not exist: `:676` already says the IDs are new.

---

## Notes

These are not violations.

- **N1. `:244`.** The brief no longer gives the window's length, and rightly, since a flat "24 hours" is false near unlock. SI:361 holds the window as "24 hours of elapsed time, cut off at unlock". Nothing says whether S-13 may state that length as a fixed fact with its cut-off. It is the same question as FQ-12, on another screen, and it is not raised.
- **N2. r1 N4 stands: `:21`, "the monthly limit is lifted".** The cap (Spec §20 5) is not mentioned to a new reader.
- **N3. r1 N6 stands. Weakest points, as the rubric requires:**
  - **R-139 / G-12:** `:612`.
  - **R-151 residual:** `:591`, same-day dates suggest a highlight. It waits on the user.
  - **B11 default:** `:29`, "Only you ever see your map", beside `:498`. A new reader is not told that the people named learn they are on it. R-146 accepts this.
- **N4. `:254` is the weakest of the fixes.** It is honest, but until FQ-11 is answered a builder has one documented exit, and a refused owner sent to the camera is the likely reflex. Rule zero says stop and ask. FQ-11 should reach the user before Phase 4.
- **N5. `:368` and `:284`.** "the next press brings them here" and row 7's "The next press is not taken" carry no pointer to FQ-10, though `:228`, `:231` and `:274` do. They read as CCCC's words and do not settle it, but `:368` is the line a Flow 5 reader meets first.
- **N6. For the guardian on `Microcopy.md`.** R-177's scan hit `Q1`: `Microcopy.md` mints Q-1 to Q-8, and `Decisions-Needed.md:5` and the rubric own Q1 to Q5. `Flows.md` only quotes it, so this is not a finding here. I did not audit `Microcopy.md`.

Not raised as a finding: the opening now holds eight "for now" or "still being compared" markers. That is a readability question for the gate, "someone who has never heard of the product can follow". It is not a rule, and it is for QA and the user.

---

## Rubric additions

- **R-178:** a word marking something as undecided is never attached to a banned-list rule or a §20 ruling. From V2, V3. Added to the "No streaks" and "Nothing leaks" rows of Banned-list coverage.
- **`Updated` line on R-176:** a blanket "never on any screen" over facts a screen shows fails. From V1.

Nothing was removed or renumbered. The other guardian was not expected to edit the rubric, and R-176 and R-177 were as I left them.

---

## Report
- Files changed: `docs/reviews/2026-11-04-rules-flows-r2.md` (new); `docs/Rules-Rubric.md` (R-178, `Updated` line on R-176, one dated log line, two coverage rows)
- Findings: 12 (6 violations, 6 notes). All r1 V1–V13 fixed, except that r1 V7's confirmation half was my own error
  - V1 R-176, R-134, `docs/Flows.md:149, 151, 160, 164`: "never on any screen" is false for most of the column; `:160` contradicts B11 and `:498`, `:164` contradicts Spec §20 SS
  - V2 R-178, R-038, `docs/Flows.md:21`: "For now" on the no-count refusal tells a reader a count might appear; contradicts `:23`, Proposal:49
  - V3 R-165, R-178, `docs/Flows.md:25, 47`: "For now, none of it is compulsory" calls Spec §20 O undecided
  - V4 R-150, `docs/Flows.md:381, 705`: "no press of its own" is not in C5's row or its cited lines, and FQ-8 undoes it; came from my r1 V7
  - V5 R-134, C18, `docs/Flows.md:154, 157`: Round's rows drop the "ready" line and the C18 tag, against `:156`, `:549`, implying an answer to C18
  - V6 R-134, `docs/Flows.md:676`: "`Status.md:46` still use it" is false since 22:25:32
  - N1 `docs/Flows.md:244`: whether S-13 may state the window's length is not raised
  - N2 `docs/Flows.md:21`: highlight cap not mentioned (r1 N4)
  - N3 R-139 / G-12, R-151 residual, B11, `docs/Flows.md:612, 591, 29, 498`: weakest points, not violations (r1 N6)
  - N4 `docs/Flows.md:254`: FQ-11 shown honestly, but should reach the user before Phase 4
  - N5 `docs/Flows.md:368, 284`: no pointer to FQ-10
  - N6 R-177, `docs/Microcopy.md` Q-1: `Q1` collision, for the guardian on that file
- Rubric additions: R-178 (and an `Updated` line on R-176)
- Verdict: FAIL
