# Rules audit: `docs/Flows.md`, round 3 (final revision)

Date: 2026-11-05. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-186; nothing added by this audit).

**Target:** `docs/Flows.md` after revision round 3 of 3, modified 2026-11-05 15:16:49, 736 lines. It is untracked, so the changes were found by reading the r2 lines again. Lines that did not change were not re-audited, except where a changed line depends on them.

Previous audits: `2026-11-04-rules-flows.md` (r1, FAIL: 13 violations) and `2026-11-04-rules-flows-r2.md` (r2, FAIL: 6 violations).

**Verdict: FAIL.** 1 violation and 5 notes.

All six r2 violations are fixed, and so are r2 N1, N5 and N6. The one violation left is a label fault I missed in r2: it is the same kind as r2 V2, on the unlock date instead of the refusal. It does not put anything banned on a screen.

A user previewing the flows would not be misled about what the product shows. They could be misled about what is still open for them to decide: V1 on C2, and N1 on B11, where the source doc frames the choice the same way.

---

## Each r2 finding, against the current file

| r2 | Now at | Result |
|---|---|---|
| V1 "never on any screen" over-claimed | `:149`, `:151`, `:155`, `:159`, `:160`, `:163`, `:164` | **Fixed.** The header is "Fixture setup". "**Never shown**" now marks only the four facts no screen shows: the sealed count, Wind's earlier rings, First Light's ring, and Wind's tag figures. `:160` now puts Hands' announcements on First Light's screen, labelled B11. `:164` gives the reveal state to the network reader (Spec §20 SS) |
| V2 "for now" on the no-count refusal | `:21`, `:44` | **Fixed.** `:21` has no hedge. `:44` reads "How the refusal is worded. That it carries no number is not open" |
| V3 "for now" on §20 O | `:25`, `:47` | **Fixed.** "Writing is optional, and you may leave the whole thing unfinished" is now stated plainly. "For now" covers only "nothing else is required ... not even a chapter" (C5) and "no deadline" (B3). `:47` cites §20 O, §20 9 and §8 as decided |
| V4 "no press of its own" | `:381`, `:705` | **Fixed.** "Whether the line needs answering, and what act saves a choice" is now one question, FQ-8. C5 is credited with repetition only, which `Decisions-Needed.md:43` supports ("Each set-once choice") |
| V5 Round's "ready" line | `:154`, `:157` | **Fixed.** Both rows read "if it still shows ... C18, which is open" |
| V6 false `Status.md` pointer | `:676` | **Fixed.** The sentence is gone |
| N1 S-13 window length | `:244`, `:712` | **Fixed.** Raised as FQ-13, not settled |
| N5 FQ-10 pointers | `:284`, `:368` | **Fixed** |
| N6 Q-1 collision | `:709` | **Fixed.** Renamed MQ-1 in `Microcopy.md`, and R-177's scan is now empty |
| N2 (`:21` cap), N3 (weakest points), N4 (FQ-11) | | Not claimed as fixed. They stand as r3 N3, N4, N5 |

**The changes the ux worker listed beyond the r2 findings:**

- **`:179`:** "12 months from today" became "a journey that runs 12 months", with "No relative form of the unlock date". That is the strictest reading, as the worker says. The C2 label on that sentence is part of V1.
- **`:186`, `:443`, `:702`:** the three R-180 rewordings hold. "this flow adds none", "This flow shows only reflections that exist" and "do not claim that this is the act" each described a buildable state. Each now only raises FQ-2, FQ-7 or FQ-5.
- **`:709`:** the MQ-1 rename holds.

---

## Auto checks run

The rubric's auto checks that need a running system do not apply. The graph was queried first. It is still stale (L-006), so it was used only to find sections.

```
$ graphify query "provisional default interim state" --budget 200
Graph: graphify-out/graph.json (253 nodes) | Traversal: BFS depth=2 | Start: ['Derived Journey State (sealed / revealing ...

$ grep -nEio '.{60}(until answered|drawn as|for now|in the meantime|adds nothing|this flow (adds|shows)|until the user).{40}' docs/Flows.md     # R-180, R-178
23   For now it shows what you chose, the day you started and the day it opens, as plain dates   -> B19 passes. C2: V1
25   For now, the plan is that a line tells you                       -> C1. Pass
25   For now, nothing else is required either, not even a chapter     -> C5. Pass
25   which for now means anyone with an account                       -> B14. Pass
25   still being compared: for now they can                           -> B2. Pass
27   still being compared: for now, finishing adds one                -> B4. Pass
33   still being compared. For now, they can                          -> B12. Pass
39, 63   "until the user says so"                                     -> about decisions, not a state. Pass
550  per year with the app, finishing adds nothing here (`PROVISIONAL: B4`)   -> names a Decisions ID. Pass
   Each "for now" names a row in the table at :41–53, as R-180 requires.
   (The pattern's 60-character lead misses :676, "Each flow adds nothing at these points". Read by hand: N2.)

$ comm -12 <(grep -oE '\b[A-Z]{1,3}-[0-9]+\b' docs/Flows.md | tr -d - | sort -u) <(grep -oE '\b[A-Z]{1,2}[0-9]{1,2}\b' docs/Decisions-Needed.md | sort -u)     # R-177
(no output) Pass

$ grep -nE 'Never shown' docs/Flows.md     # R-176
149 (the header note), 155, 159, 160, 163   -> each one a fact no screen shows, read against its viewer. Pass

$ grep -nEi 'days? (left|to go|until)|unlocks? in|from today|relative' docs/Flows.md     # R-013
104, 179, 321 (bans); 426 ("relative to saving"); the rest are "the unlock instant". "from today" is gone. Pass

$ sed -n 146p docs/Decisions-Needed.md     # V1
**C2. The unlock date.** May the owner see it? As a date only, or as "in 64 days" (a countdown)? *Lean:* a plain date, no relative time.

$ grep -nE '^- \*\*[A-Z]{1,4}\.' docs/Functional-Spec.md | tail -1     # R-165 (2)
366:- **DDDD. ...   -> still the latest ruling. :3 holds
```

---

## Violation

### V1. The unlock date's plain form is labelled as undecided

- **Check:** R-178; R-013; the rubric's rule that no default may weaken a banned-list check.
- **Where:**
  - `Flows.md:23`: "For now it shows what you chose, the day you started and the day it opens, as plain dates."
  - `Flows.md:45`: "What the sealed year shows, and its plain dates | `PROVISIONAL: B19`, `C2`".
  - `Flows.md:179`: "No relative form of the unlock date (`PROVISIONAL: C2`)".
- **What is wrong:** C2 asks two things (`Decisions-Needed.md:146`): whether the owner may see the unlock date, and whether it shows "as a date only, or as 'in 64 days' (a countdown)". The first is open, under B19 and DC-2. The second is not. Decisions itself calls the relative form a countdown, and R-013 bars any countdown or relative form of the unlock date, from CL:69 and RG:28. These lines put "for now" and a provisional label on "plain", and so on "never a countdown".
- **Why it breaks the rule:** r2 V2 fixed exactly this pattern for B7, where `:44` now says "That it carries no number is not open". C2 got no such split. I passed `:23` in r2 and should not have: this finding is mine to own.
- **Severity for a user previewing the flows:** low on what they see, real on what they decide.
  - **What they see:** the next sentence, "No pictures, no count, no countdown", is absolute, so a reader learns that no countdown appears.
  - **What they decide:** the defaults table at `:37–53` is the list of choices still open to them. It presents "plain dates" as one of them, which invites the user to weigh a countdown the banned list already rules out.
- **Fix needed:** split C2 as `:44` splits B7. Whether the date is shown stays open. That it is plain is not open.

---

## Notes

These are not violations as the file stands. The supervisor takes them to the user.

- **N1. B11's framing understates what "unnamed" protects.** It is decision-relevant for the user.
  - **Where:** `Flows.md:160` and `:498`, which say that under "named" the crossed person "learns she is on Hands' map".
  - **What it omits:** the network is the set of users on the owner's map (SI:39). On 2027-06-20 First Light starts receiving Hands' "journey launched" (Spec §20 M), and she can read Hands' Network photos. Both happen under either B11 setting. So she learns she is on Hands' map whichever way B11 is set. "Named" adds only that she was the one crossed this year. Neither setting shows her ring.
  - **Why it is only a note:** the source frames B11 the same way: "That tells them they are on the owner's map" (`Decisions-Needed.md:122`), so the file follows its source. A user comparing the two settings in the panel would still likely take "unnamed" to keep map membership hidden, and it does not.
  - **Severity:** misleads the reader on a choice the user is about to make, though nothing banned is shown. Raise it with the user as a correction to how B11 is described, in Decisions as well as here.

- **N2. R-180: the blanket at `:676`, "Each flow adds nothing at these points".** The three local rewordings fixed the cells R-180 names. This sentence still reads, for every FQ, as "build the absence": no confirmation (FQ-2), no 15 minutes (FQ-12), no window length (FQ-13), only existing reflections (FQ-7). R-180 asks such a point to name a Decisions ID, or to say the build stops there. In context the sentence means the flows filled nothing in, which is true of the doc. It is not a cell carrying a state, so I do not count it as a violation. Rule zero still means Phase 4 must stop at each FQ, not build the blank.
  - **Severity:** none for a reader. For a builder, it is the line most likely to be misread.

- **N3. r1 N4 stands: `:21`, "the monthly limit is lifted".** The cap at the type's yearly quota (Spec §20 5) is not mentioned to a new reader.
  - **Severity:** a mild misreading in the plain-language opening. Flow 2 states the cap correctly.

- **N4. Weakest points, which the rubric requires every audit to report.**
  - **R-139 / G-12:** B12's "shown" still lets a reader count by reading (`:612`).
  - **R-151 residual:** same-day capture dates still suggest a highlight to non-owners (`:591`).
  - **"Only you ever see your map":** `:29` reads beside N1. All three wait on the user.

- **N5. FQ-11 and `:254`.** These are honest, but until FQ-11 is answered a builder has only one documented exit from S-13, the camera, and a refused owner sent there is the likely reflex. FQ-11 should reach the user before Phase 4.

---

## Rubric additions

None. V1 is a kind R-178 already covers, and N1 and N2 are not new kinds.

---

## Report
- Files changed: `docs/reviews/2026-11-05-rules-flows-r3.md` (new)
- Findings: 6 (1 violation, 5 notes). All six r2 violations fixed; r2 N1, N5, N6 fixed
  - V1 R-178, R-013, `docs/Flows.md:23, 45, 179`: the plain, never-relative unlock date is labelled "for now" and `PROVISIONAL: C2`, though C2's other option is a countdown R-013 bars. Missed by me in r2. Low on what a reader sees; misleads the user on what is open to decide
  - N1 B11, `docs/Flows.md:160, 498` (source `docs/Decisions-Needed.md:122`): under either setting First Light learns she is on Hands' map from his "journey launched" and his photos. "Unnamed" does not hide membership. Decision-relevant; raise with the user
  - N2 R-180, `docs/Flows.md:676`: "Each flow adds nothing at these points" can be read as building the blank; Phase 4 must stop at each FQ
  - N3 `docs/Flows.md:21`: highlight cap not mentioned to a new reader (r1 N4)
  - N4 R-139 / G-12, R-151 residual, `docs/Flows.md:612, 591, 29`: weakest points, not violations
  - N5 `docs/Flows.md:254`: FQ-11 should reach the user before Phase 4
- Rubric additions: none
- Verdict: FAIL
