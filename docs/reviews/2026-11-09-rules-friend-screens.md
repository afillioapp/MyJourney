# Rules audit: the friend screens (ux pass for FS §20 KKKK) and Decisions-Needed B57–B61

Date: 2026-11-09. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-197. This audit adds no new check; it adds `Updated` lines on R-150 and R-176.

**Targets.** Commit d3b94c0:

- `docs/Screen-Inventory.md` (SI):
  - S-22, S-23, S-24;
  - S-16's friend request and its pair-state table;
  - S-05's way into S-22;
  - the network lines restated across the file;
  - OQ-55 to OQ-57;
  - the T-01 rows.
- `docs/Flows.md`:
  - Flow 10;
  - the opening's "Your friends" paragraph and its working-default rows;
  - the prototype table's First Light, Round #4 and Flow 10 rows;
  - DC-15 and DC-16.
- `docs/Decisions-Needed.md` (DN) B57 to B61.

**Verdict: FAIL**, with 2 violations (low to medium) and 4 notes.

**What holds up.** The screens are careful. I found no leak and no marker on S-22, S-23, S-24 or the S-16 pair state:

- no count, dot, "new" or seen state;
- no time;
- no way to tell a decline from a pending request;
- nothing about who removed whom;
- no other user's friends;
- no way that appears by state.

S-16 also shows nothing when the other person's request waits.

No line still treats the network as the map. B57 to B61 bring in no banned item, rank nobody, and settle none of E2 to E5. The opening still passes the Phase 2 gate for a new reader.

**What fails**

- **V1:** neither SI nor Flows carries the five new defaults. Both still call the questions B57 to B61 answer "not set" and send the reader to OQ-55 to OQ-57.
- **V2:** one prototype-table row says Second Wind has no request after 2026-11-14. The fixture keeps her outgoing request to Long Way Round.

**For a user previewing the design**:

- V1 means the friend screens would be built without the profile actions, ordering and confirmation the defaults set.
- V2 would make a correct prototype look like a bug.

---

## Checks run

```
# Markers and leaks on the new screens (R-096, R-189, R-191, R-192, R-193, R-194)
SI:545 S-22 way in "present in every state and identical whether or not a request waits"            -> pass
SI:550 never: time, "2d", count (list, way in, app icon), dot, bold, "new" divider, seen/unseen, mutual friends,
       suggestions, map facts, any notification                                                       -> pass
SI:551 outgoing: pending and declined look the same; never "declined", "seen", "not answered", greyed  -> pass
SI:571 S-23 never: a count, "friends since", order by closeness/ring/recency, past friends, who removed whom -> pass
SI:587 S-24 never: a count, notice to the person, list to others, extra access, "inner ring", suggestions -> pass
SI:422–425 S-16 pair state: own request pending = declined; "friends" with no date; a waiting incoming
       request = exactly the first row, no accept offer, no dot                                      -> pass
SI:174 S-05 way to S-22 always present, byte-identical (B43, K14, R-194)                               -> pass

# Network as map
$ grep -nEi "map member|network[^.]{0,40}(layer|map|ring)|(layer|map|ring)[^.]{0,40}network|outer ring is still|inner ring|innermost" SI Flows
SI:41 (definition: network = friends), :234, :682, :693, :978–982 (revision log), Flows:507, :602, :621  -> all restate KKKK correctly
SI:267, :268, :723, :899 "the owner's network members": read under SI:41's definition (friends); S-08 carries B48 at line 10 -> pass

# B57–B61 against the banned list and the user questions
B57 way to S-23 always present, no count ; B58 add / withdraw / remove on S-16 ; B59 A–Z, "never by closeness,
by time or by activity" ; B60 removal confirmed once, no finality line ; B61 S-16 never shows an incoming request
-> no banned item, no ranking (alphabetical by a name chosen once is not a rank), none of E2–E5 settled

# Carriage of B57–B61 (R-150)
$ grep -nE 'OQ-5[5-7]' docs/Screen-Inventory.md docs/Flows.md
SI:174, 414, 423, 424, 545, 550, 551, 566, 571, 582, 816–818 ; Flows:654, 659, 667, 679, 683, 689, 780–782, 826
$ grep -c 'B5[7-9]\|B6[01]' docs/Screen-Inventory.md docs/Flows.md
docs/Screen-Inventory.md:0  docs/Flows.md:0                                                       -> V1

# Prototype table against Phase-1-Amendments §13
Flows:181 Second Wind, after 2026-11-14: "Hands among Wind's friends, no request"
Am §13.5 / Q-F12: "friend_request_rows() -> one outgoing row each, to Long Way Round (fr-10, fr-11)"  -> V2
Other rows checked against §13.1–§13.4: Lantern, Round, First Light (Flow 10); Lantern and Hands on Round #4;
First Light at 2027-06-20; SI T-01 baseline and 2026-11-14                                             -> pass
```

---

## Violations

### V1. B57 to B61 are not carried: SI and Flows still call their questions open
- **Checks:** R-150 (a deliverable describes every question that a provisional default answers under that default, and never calls it open); R-165 (3); R-177 (a cross-reference must land).
- **Where:**
  - **SI, S-05:** `:174` ("where their ways in sit is not set (OQ-55)").
  - **SI, S-16:** `:414`, `:423`, `:424` ("OQ-55", "OQ-57").
  - **SI, S-22:** `:545`, `:550`, `:551` ("OQ-55", "OQ-56").
  - **SI, S-23 and S-24:** `:566`, `:571`, `:582`.
  - **SI, open questions:** `:816–818` (OQ-55 to OQ-57: "Not picked").
  - **Flows, Flow 10:** `:654`, `:659`, `:667`, `:679`, `:683`, `:689`.
  - **Flows, open questions:** `:780–782` (still "for the supervisor").
  - **Flows, DC-15:** `:826` ("The rest of the pair's display is not picked: SI OQ-57").
- **What is wrong.** DN B57 to B61 answer most of OQ-55 to OQ-57:
  - **B57:** the ways to S-23 (from S-05, always present, no count) and to S-24 (from S-23).
  - **B58:** S-16 offers add friend, withdraw and remove.
  - **B59:** friends and close friends in A to Z order.
  - **B60:** removal is confirmed once; no other act is, and no finality line.
  - **B61:** S-16 shows only "add friend", your own pending request, or "friends". It never shows an incoming request, and it settles DC-15.
  
  Neither file names any of B57 to B61; a grep finds 0 in each. A builder reading S-16 is told what it shows "is OQ-57", which is now B61. They are told S-23's way in "is not set", which is now B57.
- **Also:** S-23's "fixed order" (SI:571) cites §12.1's random order, not B59's A to Z. And S-24 is "reached from S-23 or S-05; which one is OQ-55" (SI:582), where B57 says S-23.
- **What OQ-55 still holds.** Whether a name in S-22, S-23 or S-24 leads to S-16 (b), and how S-24 adds a friend (d). Those parts stay open correctly.
- **How serious for the prototype.** **Medium-low.** No banned item follows. A builder following SI would leave out:
  - S-16's withdraw and remove;
  - S-23's always-present way in;
  - the A to Z order;
  - the removal confirmation.
  
  Or the builder stops to ask. The user previewing would then not see the behaviour the defaults set, and could not judge it.
- **Why it happened.** The defaults were added in the same commit, after the ux text. R-150 step 2 also missed it: its pattern looks only for "Raised as … OQ-n", and these rows say "added … from Screen-Inventory OQ-55" or "settles … DC-15". R-150 now takes both forms.
- **Fix belongs to:** ux, in SI and Flows. B61's mismatch with `Phase-1-Amendments.md` §12.6's accept offer stays with lead-tech, as the supervisor noted.

### V2. The prototype table says Second Wind has no request after 2026-11-14; the fixture keeps one
- **Check:** R-176 (a "what you see" line holds what that viewer's screen shows); updated this run.
- **Where:** `Flows.md:181`. "At baseline: an incoming request from Open Hands and an outgoing one to her. After: Hands among Wind's friends, no request."
- **What is wrong.** Wind also sent fr-10 to Long Way Round on 2026-10-14. It is never answered by script (Am §13.1, §13.5), and the 2026-11-14 accept leaves it untouched. Q-F12's own words: "one outgoing row each, to Long Way Round (fr-10, fr-11), untouched by the accept".
  - So at baseline Wind's S-22 shows three rows, not two.
  - After 2026-11-14 it shows one outgoing row, not "no request".
  - The Round row two lines up (`:179`) shows the same request from the other side.
- **How serious for the prototype.** **Low-medium.** A user stepping through Flow 10 as Wind would see a request the walkthrough says is not there. They would take a correct prototype for a bug, or take the walkthrough's word and report the prototype.
- **Fix belongs to:** ux. Add fr-10 to both halves of the row: "an outgoing one to Long Way Round", and "after: one outgoing request, to Long Way Round".

---

## Notes (not violations)

- **N1. S-16 changes when the other person acts.** When the other person accepts, the viewer's S-16 for them changes from the pending state to "friends". When the other person removes the viewer, it changes from "friends" to "add friend". So S-16 does change because of someone else's act, though only when the viewer opens that one profile.
  - This is the friendship itself becoming visible, which KKKK (a) and B45 need, and nothing marks it as new. R-194 covers arriving requests only.
  - Not a violation. For the user, it means acceptance and removal are discovered, never announced, which is as the product intends.
- **N2. B58's wording leaves one state to B61.** B58 offers "add friend" "when there is no request between you". When the other person's request waits, there is one between them. B61 fills the gap (S-16 shows "add friend"). Read together they hold (R-187), but B58 alone reads as if S-16 must show something else then. Worth one clause in B58.
- **N3. The opening says "Your friends get a one-line notice that your journey is out"** (`Flows.md:27`).
  - For a new reader, "notice" can sound like a notification, next to "Nothing pings you" (`:23`). The line does not say the notice is in the feed.
  - "Out" is the word `Microcopy.md:38` dropped (B1).
  - Under B48 it is the friends at that moment who get it.
  
  The opening still passes the gate: it is plain, it is ordered as the year is lived, it keeps map and friends apart, and it labels every default in the table below it. This is one sentence to tighten.
- **N4. B59's order applies to friends and close friends only.** The order of outgoing requests stays §12.1's random id order, and SI and Flows say "a fixed order that carries no time" for it. Nothing to fix, but OQ-55 (e) is only half answered.

## Tested and clean

- **R-189:** decline never shown, on S-16, S-22 and Flow 10 part B.
- **R-191:** removal touches no map, and nothing stores who removed whom.
- **R-192:** no times or counts on any new screen.
- **R-193:** no other user's friends, mutual friends or close friends.
- **R-194:** S-16 shows nothing for a waiting incoming request.
- **R-095:** empty states with no call to action.
- **The banned list across B57–B61:**
  - B59's A to Z order is the strictest order and ranks nobody.
  - B60's confirmation is a single plain step, not an "are you sure" nudge on anything banned.
  - None answers E2 (what close friends get), E3, E4 (B56 already holds "no one sees another's friends") or E5 (blocking).
- **Network as map.** SI's viewer definition (`:41`), S-06, S-07, S-08 (B48 at its line 10) and Flows 7, 8 and 9 restate KKKK correctly.
- **Fixture rows.** Lantern on Round #4 (allowed, a friend). Hands on Round #4 (public reader, her request pending). First Light at 2027-06-20 (nothing from Hands). Flow 10's Lantern, Round and First Light rows. SI T-01 rows (`:614–615`). All against `Phase-1-Amendments.md` §13.1–§13.4.
- **DC-16.** Spec:175 against §20 J, cited both ways, not picked (`Phase-1-Amendments.md` OQ-40).
- **The plain-language opening:** see N3.

---

## Rubric changes made in this run

- **R-150, `Updated` line:** step 2 also takes Decisions-Needed rows added "from Screen-Inventory OQ-n" or that "settle" an OQ or DC. Every doc that raised or cites the question must name the B-row. A body line still saying "not set" fails.
- **R-176, `Updated` line:** a prototype table's "On screen" cell is checked against the fixture's derived state at that clock point, including what a scripted act leaves untouched.
- Log entry added. No new check. No check renumbered or removed.

---

## Report
- Files changed:
  - `docs/reviews/2026-11-09-rules-friend-screens.md`
  - `docs/Rules-Rubric.md`: `Updated` lines on R-150 and R-176; log entry.
- Findings: 2 violations and 4 notes.
  - **V1:** R-150, R-165, R-177. SI:174/414/423/424/545/550/551/566/571/582/816–818 and Flows:654/659/667/679/683/689/780–782/826. B57 to B61 are not carried, so both files still call their questions "not set", OQ-55 to OQ-57, and DC-15. **Medium-low:** the friend screens would be built without the defaults, or the build stops.
  - **V2:** R-176, Flows:181. Second Wind "no request" after 2026-11-14, but fr-10 to Long Way Round stays open (Am §13.5, Q-F12). **Low-medium:** a correct prototype would look like a bug.
  - **Notes:**
    - N1: S-16 changes when the other person accepts or removes. Discovered, not announced. Not a violation.
    - N2: B58's "no request between you" leaves the incoming case to B61.
    - N3: the opening's "one-line notice that your journey is out" can read as a notification. The gate still passes.
    - N4: B59 leaves the outgoing-request order to §12.1.
- Rubric additions: none new. `Updated` lines on R-150 and R-176.
- Verdict: FAIL.
