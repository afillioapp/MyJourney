# Rules audit: Art-Direction.md and Microcopy.md, round 3 (final)

Date: 2026-11-05. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-187. This run added an `Updated` line to R-187 and no new check.

**Targets**

- `docs/Art-Direction.md` (AD), 739 lines, after revision round 2.
- `docs/Microcopy.md` (MC), 232 lines, after revision round 2.
- The supervisor's revised B28 and B41 and new B42 in `docs/Decisions-Needed.md` (DN:63, :76, :77), audited as part of the art direction.
- All are untracked or uncommitted, so changes were found by reading each r2 line again.

Previous audits: r1 `2026-11-04-rules-art-microcopy.md` (FAIL, 21 findings); r2 `2026-11-05-rules-art-microcopy-r2.md` (FAIL, 8 violations, 7 notes).

This is the last audit before the remaining findings go to the user.

**Verdicts.** `Art-Direction.md`: **FAIL**, with 2 violations, one medium and one low. `Microcopy.md`: **PASS**, with zero violations. Its weakest points are listed below.

All eight r2 violations are fixed, and so are r2 N-3, N-4 and N-6. B41 and B42 hold under R-187.

The medium violation is in revised B28. It puts a finished journey's activity line on a ring that does not exist yet. So under B4's per-year option the line is missing for most of a year after each finish, and the fixtures reach that state on 2027-04-25. Flipping B4 therefore still changes what B5 shows for that period, and AD:105 says it does not.

---

## Checks run

```
$ grep -nE 'pending|see report' docs/Art-Direction.md docs/Microcopy.md
(no output)                                          -> r2 ART-R2-4 stale line gone

$ grep -n 'boundary the rings' docs/Art-Direction.md
(no output)                                          -> r2 N-3 gone

$ grep -n 'B27 to B4' docs/Art-Direction.md
:10   "Those rows are B27 to B42"
:685  "(B27 to B41, added 2026-11-05)"              -> ART-R3-2

# R-177: Microcopy's Flows IDs against Flows' own table
MC:211–216 cite DC-1, DC-2, DC-3, DC-5 to DC-9. Flows:718–731 hold DC-1 to DC-14 with the same subjects:
DC-5 "publish", DC-8 "where they appear", DC-9 profile picture, DC-6/DC-7 feeling tags.
Hyphen-stripped, "DC5" etc. match nothing in Decisions-Needed.          -> pass

# R-182 on S-13 (M-05, M-06, M-07 together)
"Starting a highlight opens a window in which the monthly limit does not apply."
"A highlight is open."
"No highlight was started."
Read together in each S-13 state (none open, one open, allowance used): no contradiction.  -> pass

# R-183 on the rewritten lines
M-12 "Your year has opened, all at once." true after a lost press or page, with no photos, at any later open -> pass
M-23 "Your circle is a record, not a measure of how you are doing." true under both B4 settings, 0 or many rings, +5 years -> pass

# R-187 (1) on B28: fixture timing (P1:211, P1:390)
Second Wind joined 2021-03-15. Wind's per-year "year" containing 2027-04-25 runs 2027-03-15 to 2028-03-15.
Wind finishes #6 on 2027-04-25. B31: the flat graph stops at finish.
B28: #6's marks go on the ring for the year holding 2027-04-25. That ring is added at
     the 2028-03-15 anniversary, or later, at the unlock of a journey sealed then.
=> Under B4 per-year: #6's line is shown nowhere from 2027-04-25 until at least 2028-03-15.
   Under B4 default: shown on ring n+1 from 2027-04-25.                  -> ART-R3-1
```

---

## Each r2 finding, against the current files

| r2 | Now at | Result |
|---|---|---|
| ART-R2-1: B41 forced C18 | DN:76; AD:357, :375, :708 | **Fixed.** A plain way to S-04 is present while a reveal is open, so S-04 stays reachable whatever C18's answer (R-187 (2) passes). B41 says it does not answer C18 |
| ART-R2-2: Commit and sealed-year ways "until the user rules" | DN:77 (B42); AD:355–356, :373–377, :708 | **Fixed.** A DN row now covers them, styled like every way, and nothing announces the change. Whether a way appearing by state is a marker is named for the user (AD-18), as R-186's how-to-check requires. Not a violation now. It goes to the user below |
| ART-R2-3: flipping B4 erased the activity line | DN:63; AD:105–109, :225, :250, :253 | **Partly fixed.** The line now survives once its ring exists. It is missing until then: ART-R3-1 |
| ART-R2-4: stale "pending" line; AD-n-only cells | AD:364 gone; AD:218–228 cells carry B27, B28, B31, B36 | **Fixed.** One stale range remains, at :685: ART-R3-2 |
| ART-R2-5: `[AD]` placed the envelope | AD:265 | **Fixed.** It now cites SI:117, element 1, and only the drawing is `[AD]` |
| COPY-R2-1: "begun by this press" beside "No highlight was started." | MC:67 | **Fixed.** See the note on departing from the marker below |
| COPY-R2-2: "as you kept it" | MC:100 | **Fixed** |
| COPY-R2-3: stale C-n | MC:5, :38, :151, :211–216 | **Fixed.** DC-n, matching Flows' table |
| N-3: AD:632 wording | gone | **Fixed** |
| N-4: B39 string unwritten | MC:232 (MQ-11) | **Raised** for ux and the user. Correct, since no marker asks |
| N-6: M-23 under B4's default | MC:142, :228 | **Fixed** |
| N-1, N-2, N-5, N-7 | AD-19 (N-2) | N-2 is raised as AD-19. N-1, N-5 and N-7 stand: see below |

---

## Findings: Art-Direction.md, and its defaults in Decisions-Needed.md

### ART-R3-1. Under B4's option, revised B28 puts a finished journey's line on a ring that is not drawn yet
- **Checks:** R-141 (flipping one switch changes only its own behaviour), R-187 (1). Spec:186 and DN B5 (the line twists into the circle at reveal finished).
- **Where:** `Decisions-Needed.md:63` (B28), `:66` (B31); `Art-Direction.md:105`, `:225`, `:250`, `:253`.
- **What is wrong.**
  - B28 puts each finished journey's marks "on the owner's ring for the year that holds that journey's reveal-finished date". It adds that year's ring "at the join anniversary, unless a journey is sealed then, when it is added at that journey's unlock".
  - A reveal is always finished inside a year whose ring is not yet drawn, because that year's ring comes at its closing anniversary or later.
  - B31 stops the flat graph at finish.
  - So under the per-year option the owner sees that journey's activity nowhere, from the finish until the ring arrives. That is up to a year, longer if a journey is sealed at the anniversary. Under the default it shows from the finish.
  - AD:105 states "flipping B4 changes nothing B5 shows (R-141, R-187)". That is false for this window.
- **In the fixtures.** Second Wind finishes #6 on 2027-04-25 (P1:390), and her per-year year runs from 2027-03-15. Her #6 line is missing until 2028-03-15 at the earliest.
- **How serious for a user previewing.** **Medium.** It is the same misleading comparison as ART-R2-3, now confined to a window. Jump past Wind's scripted finish, flip B4 to per-year, and her newest year's activity is gone. A user deciding B4 would read that as a cost of the per-year option. Only a further jump of about a year brings it back.
- **Who can fix it, and how.** The supervisor or the user, in B28. Two readings would close the gap:
  - draw the marks on the newest existing ring until the year's own ring arrives;
  - or keep the flat graph shown, under the option only, until that ring is drawn.
  
  The second is a B31 exception, and it would itself be a B4-dependent behaviour. Either way this is AD-2's real question, and it is the user's.

### ART-R3-2. §12 states a default range that leaves out B42
- **Check:** R-150 (a deliverable "never states a default range that leaves out rows in the table").
- **Where:** `Art-Direction.md:685`, "Each now names its row in `Decisions-Needed.md` (B27 to B41, added 2026-11-05)". AD:10 says B27 to B42, and AD-18 (AD:708) names B42.
- **How serious for a user previewing.** **None visible.** A builder reading only §12's preamble could miss B42, but AD-18's own cell names it, so nothing would be built wrong.

---

## Microcopy.md: weakest points (not violations)

There are no violations after a full re-read of every entry against R-095, R-102, R-124, R-131, R-150, R-177, R-182 and R-183. These are the points closest to failing.

- **M-05 departs from its marker** (MC:67). The marker at Flows:244 asks for "a window, begun by this press". The line says "Starting a highlight opens a window …", because the marker's wording is false beside M-07, and the file says so in place.
  - This is not a violation. A marker's quoted words describe what the line must do, the line does it, and the departure is cited rather than silent (R-135).
  - But `Flows.md:244` still carries the false wording, and Flows is at its revision cap. A builder reading Flows rather than MC would write the contradiction back in. For the supervisor to carry.
- **M-05 and the cap (MQ-2).** "The monthly limit does not apply" is true, but a press inside an open highlight can still be refused once the highlight is full and no frame is left. S-13 may show no number. Raised, not settled.
- **M-25 "You were here." (R-139, R-147, G-12).** Reported in every round, as required. A reader can count appearances and estimate their ring. The user has not ruled.
- **R-130 has nothing to read in the prototype (MQ-5).** The only line that says it, "We want you here less, not more.", is on S-10, which is not built. Raised for the user.

---

## Notes (not violations), going to the user

- **N-1. AD-18 / B42 / B41: ways that appear by journey state.** On unlock day the sealed-year way goes and the Commit and Reveal ways come, beside "Your Journey is ready". Each is drawn like every other way and nothing announces it, but SI:77 bans "a marker that Commit is open again", and R-186 bans a way that appears by content. This is no longer a violation, because it is labelled and named for the user. It is the largest open design question in the two files. **For a previewing user: medium.** Jump Steady Lantern to 2027-01-01 and watch the navigation.
- **N-2. AD-19: the newest ring is always the finest.** The fix the art director describes would move every ring at each finish, against B34. The user should look at Steady Lantern at +5 years.
- **N-3. AD-17: fine rings blur from ring 10 at 240 px on a 1× screen.** The fixtures reach about 11 rings at +5 years. Numbers verified in r2.
- **N-4. AD-11: activity density shows the type and how full a year was, to the owner.** It matters only if AD-1 / B27 is ever opened to the network.
- **N-5. `Screen-Inventory.md:412` and `:420` still describe a public flat graph, against B36.** This is SI's carriage (R-150), outside these targets. Carried from r2.
- **N-6. B28 has two more open points.**
  - Its ring timing is stated as "a proposed rule, not a reading of the docs".
  - Two reveals finished in one year share a ring (AD:109), and one ring then carries two journeys' lines.
  
  Both are in AD-2.

## Tested and clean this round

- **B41 and B42 under R-187 (2).** S-04, S-03 and S-01 stay reachable under every answer to C18 and AD-18.
- **The §3.6 cells.** All name their DN rows (R-180).
- **R-179.** Unchanged and clean.
- **R-185.** Unchanged and clean.
- **Envelope §5.** Unchanged and clean.
- **The layer map.** Unchanged and clean.
- **MC's DC-n citations against Flows' table.**
- **M-05, M-12, M-23 under R-182 and R-183.**
- **The six approved lines.** Word for word in both files.

---

## Rubric changes made in this run

- **R-187, `Updated` line:** the switch comparison in (1) runs at more than one clock point, because a default can hold at one time and fail in between. Compare at each scripted fixture event the row touches, at the day after it, and at the next event that completes the behaviour, such as the next anniversary or unlock. Found as ART-R3-1.
- Update log entry added. No check renumbered or removed.

## Going to the user

For the supervisor to carry into the user's list:

1. B28's handling of the gap between finish and the year's ring (ART-R3-1), with AD-2's timing and shared-ring points.
2. AD-18: whether ways that appear by journey state are markers (N-1).
3. C18: how long "Your Journey is ready" stays.
4. AD-19, AD-17, AD-11: the newest ring thinnest, fine-ring legibility, and activity density.
5. MQ-2, MQ-5, MQ-11, G-12 (M-25).
6. Carriage: `Flows.md:244` (M-05's departure) and `Screen-Inventory.md:412`, `:420` (B36).

---

## Report
- Files changed:
  - `docs/reviews/2026-11-05-rules-art-microcopy-r3.md`
  - `docs/Rules-Rubric.md`: an `Updated` line on R-187; log entry.
- Findings: 2 violations and 6 notes. All 8 r2 violations are fixed, ART-R2-3 only partly, its remainder being ART-R3-1.
  - ART-R3-1: R-141, R-187 (1), DN:63 (B28), :66 (B31), AD:105/225/250/253. Under B4's option a finished journey's line goes on a ring not drawn until the next anniversary or later. The activity is missing for up to a year, and AD:105's "changes nothing B5 shows" is false. **Medium for the preview:** Wind after 2027-04-25.
  - ART-R3-2: R-150, AD:685. "B27 to B41" leaves out B42. **None visible.**
  - Microcopy.md: no violations. Weakest points: M-05's departure from Flows:244, which still carries the false wording; MQ-2; M-25 (G-12); MQ-5.
- Rubric additions: none new. An `Updated` line on R-187 (compare at several clock points).
- Verdict: `docs/Art-Direction.md` FAIL. `docs/Microcopy.md` PASS.
