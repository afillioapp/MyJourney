# Rules audit: carrying FS §20 KKKK, round 2

Date: 2026-11-09. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-196 before this audit and R-197 after it.

**Targets.** The fixes after `docs/reviews/2026-11-09-rules-kkkk.md` (r1: FAIL, V1–V4, N1–N4), in three commits:

- **d00d58c, supervisor:**
  - DN B43, B47, B48, B55, B56, E3 (c), E5;
  - FS:278 (§20 H reopened in half);
  - P1:84, 126, 143, 164, 168, 405.
- **449ab52, lead-tech:** Am §11 pointers; §12.3's event-time audience; §12.6 rows; K13, K14; B55 and B56 labels.
- **0f6b70a, fixture-designer:** Am §13.4–§13.6 audiences at event time; Q-F7, Q-F9, Q-F12.

All of it is still on paper, and no query was run.

**Verdict: FAIL**, with 1 violation, low severity, and 1 coverage gap, low. All four r1 violations are fixed.

The two questions you asked:

- **Does the event-time rule leak when a friendship began?** No path found. What a viewer learns is when their own friendship began, which they already know. No reader returns another person's start, and no recipient list exists. Details under "The event-time rule" below.
- **Does K14 cover B43?** Mostly. It tests that the way in looks the same with 0 or many requests waiting, and that only the list route reads the list. It does not test that the way is always there, or that the list itself carries no "unseen" state. Both are now in R-194 (G1).

**For the prototype**, nothing here puts a banned item on screen or leaks anything. The remaining violation would make a Phase 3 test fail correct code. The gap is two missing halves of a test.

I also found that **four `Updated` lines I wrote in r1** (R-088, R-089, R-146, and R-064's "read the same") went stale when B48 moved to event time. They are now superseded by second-pass lines, kept as history (R-172).

---

## Checks run

```
# r1 V1–V4 against the current files
DN:83  B48 "fixed when the event happens … strictest reading … a visibility question for the user (E3 c)"; no "Instagram reference"
DN:228 E3 (c) raised                                                          -> V1 fixed
FS:278 H "(reopened 2026-11-09 … meanwhile provisional default B55)"; DN:90 B55; DN:82 B47 "until then B55 applies"
DN:216 E2 "Until answered, provisional default B55 applies"                   -> V2 fixed (R-178: no "for now" left)
P1:84, 126, 143, 164, 168 dated notes; P1:405 R2 "Superseded 2026-11-09 by FS §20 KKKK (e)"
Am:1107, 1118, 1119, 1149 "Since 2026-11-09 (FS §20 KKKK)" pointers to §12.3 / §12.1  -> V3 fixed
DN:78  B43 "The way into that list is always present on the profile and looks the same whether or not any request waits"
Am §12.6 row "requests waiting"; K14                                          -> V4 fixed (coverage: G1)

# r1 notes
N2 -> DN:230 E5 (blocking) raised. N3 -> R-155 scoped in r1. N4 -> DN:91 B56, labelled in K7 (Am:1493)   -> all closed

# Event-time arithmetic, recomputed from Am §13.1 accepts and §13.4.1 dates
Lantern: Wind 5+3 (after 2021-03-17) + Hands 3+2 (after 2023-06-11) + Round 0 (2023-09-12 inside removed fr-2;
         2024-09-15 between; 2025-09-21 before fr-4) = 13
Wind 9 ; Hands: Lantern #3, #4, #5 + crossings of #4, #5 = 5 ; Round: Lantern #5 + its crossing = 2 ; First Light 0
lantern-1 to Hands 3 and Round 1; lantern-3 not Round (2024-01-27 inside fr-2); round-1 to Lantern only 2026-09-10  -> all agree

# Stale text under event time
$ grep -n 'worked out when they are read\|at read time' docs/Phase-1-Amendments.md  (after line 1280)
:1549 §12.9 instruction to the fixture-designer (history, describes the change) ; :1557 OQ-41 history ; :1700 history note -> fine
$ grep -n 'read time' docs/Rules-Rubric.md
R-088, R-089, R-146 first-pass lines (mine)                                   -> superseded this run
K8 (Am:1494) "a close friend and an ordinary friend read exactly the same"   -> V1 below
```

---

## Each r1 finding, against the current files

| r1 | Now at | Result |
|---|---|---|
| V1: B48 settled a visibility question as "Instagram reference" | DN:83, DN:228 (E3 c); Am §12.3 (event-time row and paragraph), K13, §13.4 | **Fixed.** B48 is now the strictest reading, labelled so, with the question to the user. A new friend no longer receives years of "path crossed" lines (Q-F12 shows it). The arithmetic is checked above |
| V2: §20 H left half in force | FS:278; DN:90 (B55), :82, :216; Am:1356, K8 | **Fixed.** H's second half is marked reopened, and B55 carries "nothing extra" as its own default |
| V3: R2 and §11 still read the map | P1:84, 126, 143, 164, 168, 405; Am:1107, 1118, 1119, 1149 | **Fixed.** Each line carries a dated pointer, and R2 is marked superseded |
| V4: the way into the requests list was unstated | DN:78; Am §12.6, K14 | **Fixed.** B43 states it, and the route rule keeps the reader off every other route. Test coverage: G1 |
| N2: no block | DN:230 (E5) | **Raised** for the user |
| N4: E4's state had no B-row | DN:91 (B56); Am:1424, K7 | **Fixed** |

---

## The event-time rule: can it leak when a friendship began?

Every path I could find:

1. **A viewer comparing their feed with what the actor has done.** A later friend can see an older journey's content, because B45 gives content access at once. They can also see its reveal state (SS) and get no "journey launched" for it. That tells them their friendship began after that event, which they already know. The withheld "path crossed" lines are not recoverable from the content under the defaults:
   - person tags are hidden under `c6 = hidden`;
   - B12 shows a reader only their own appearances.
   
   Under `c6 = shown` the tags on older photos do show who was on the map then. §12.3 says so and leaves it to E3 (b). It is listed in R-197 as outside B48's reach. **No leak.**
2. **Two friends of the same actor, with different start dates.** Each sees a different set of the actor's announcements. No reader shows anyone another person's feed, friendships or start date (K7, B56). An off-app comparison shows each person only their own start. **No leak.**
3. **The actor.** No recipient list is stored, and no per-viewer row exists (Am §12.3), so the actor cannot see who received what. **No leak.**
4. **A removal and a re-friending.** The removed friend's earlier announcements disappear, and the new friendship counts from its own start. Both people know both facts. A third party sees nothing. **No leak.**
5. **The instants used.** The predicate reads `answered_at`, which is returned by no reader, and `at`, which every recipient already reads (P1:168). The tie rule is strict `<`, and no fixture tie exists (§13.1 acts are dated clear of every announcement). **No leak.** Timing stays FS §20 RR's residual.
6. **Against the rulings.** B48 narrows FS §20 M's "shown to the owner's network" for later friends. M does not say when the audience is worked out, so this is a reading, raised as E3 (c), not a contradiction. FS §20 J's "for every crossing" still holds: Round → Hands #1 is emitted and simply reaches nobody now (§13.4.3).

---

## Findings

### V1. K8 says a close friend and an ordinary friend "read exactly the same", which is false under the event-time B48
- **Checks:** R-168, R-134 (a check must not fail the behaviour its rules require); R-064.
- **Where:** `Phase-1-Amendments.md:1494` (K8: "a close friend and an ordinary friend read exactly the same … *Test:* the K2 fingerprint over o's content for f1 … and f2 …, which must be equal"). Compare `:1906–1912` (Q-F7, which restricts the announcement comparison to after "the latest of the three accepts" because "under B48 the earlier rows differ by when each friendship began").
- **What is wrong.** Under B48, two friends whose friendships began at different instants read different "journey launched" and "path crossed" rows. K8's behaviour and its scratch test compare the whole fingerprint, `announcement_rows()` included, with no restriction. As written, K8 fails correct code whenever f1 and f2 were befriended at different times.
  - The fixture-designer saw this and restricted Q-F7, but the check itself was not changed.
  - A Phase 3 developer meeting a failing K8 could "fix" it by making announcements read-time again. That would undo r1 V1.
  - My own R-064 line from r1 had the same flaw. It is now corrected by a second-pass line.
- **How serious.** **None for the prototype. Low for Phase 3:** a false failure that points toward the wrong fix.
- **Fix belongs to:** lead-tech. In K8, befriend f1 and f2 in one panel transaction, or compare announcements only after the later accept, as Q-F7 does.

### G1. K14 covers half of B43
- **Checks:** R-194, R-096, R-186.
- **Where:** `Decisions-Needed.md:78` (B43); `Phase-1-Amendments.md` K14.
- **What K14 covers.**
  - The way in, and every other response, is byte-identical with 0 and with 3 incoming requests.
  - `friend_request_rows()` is called only by the list route, after the list is opened.
  - A send writes no announcement or other row.
  - Planted faults: a profile route reading the list to decide on an entry; a dot or bold style.
  
  That catches an entry that appears only while requests wait, which was r1 V4's case.
- **What it misses.**
  1. **"Always present."** If the way is drawn nowhere, both renders are equal and K14 passes. B43 says it is always on the profile.
  2. **Inside the list.** K14 excludes the list's own rows. A "new" divider, a bold unseen row or any seen/unseen state would sit there. That needs a read-state record, which R-096 bans, but no K-check tests the list screen for it.
  3. **Carriage.** No screen in `Screen-Inventory.md` holds the requests list, and S-05's "Leads to" does not name the way. R-186 and the art direction (AD:335) give a navigation mark only to a way SI names, so ux has to add the row before it is built.
- **How serious.** **Low for the prototype.** The likely failure is a "new" treatment inside the list, which is a marker the user would see the first time a request arrives. R-194 now carries both halves.
- **Fix belongs to:**
  - lead-tech: two cases added to K14;
  - ux: an S-05 "Leads to" row and a requests-list screen.

### Notes

- **N1. My own r1 rubric lines went stale.** I wrote R-088, R-089 and R-146 under the read-time B48, and R-064's "reads exactly the same" without a time condition. All four are now superseded by second-pass `Updated` lines; the old lines stay as history (R-172). R-089's counts are now 13 / 9 / 5 / 2 / 0.
- **N2. `c6 = shown` bypasses B48 for older journeys.** A later friend reads the person tags on older photos and so sees who was on the map then. This is stated at Am §12.3 and belongs to E3 (b). The user should decide E3 (b) and E3 (c) together.
- **N3. DN lists E5 before E4** (DN:230, :232). Cosmetic.

## Tested and clean this round

- All four r1 violations and N2 to N4.
- The event-time oracle (K13, Q-F9) and its planted faults: read time; "a friend at the event" with no current friendship; "ever friends and friends now"; `<=`.
- §13.4's per-viewer counts and reflection lists, recomputed by date.
- Q-F12: the 2026-11-14 accept gives neither friend any earlier announcement.
- §13.4.2's scripted recipients: unchanged, since both friendships predate them.
- B55 and B56 labels in K7 and K8.
- The §12.6 route rule for the requests list.

---

## Rubric changes made in this run

- **R-197 (new, area 7):** the event-time announcement audience, from K13. It includes "nothing stored about recipients" and "no reader tells anyone when another's friendship began". Added to Banned-list coverage under "No layer is ever shown".
- **Second-pass `Updated` lines on R-064, R-088, R-089 and R-146,** superseding my r1 lines for event time. R-089's counts are now 13 / 9 / 5 / 2 / 0, with the read-time planted fault giving 17 / 9 / 9 / 9 / 0.
- **`Updated` line on R-194:** the way in is always present, and there is no read state inside the list. The way must be in SI first.
- Log entry added. No check renumbered or removed.

---

## Report
- Files changed:
  - `docs/reviews/2026-11-09-rules-kkkk-r2.md`
  - `docs/Rules-Rubric.md`: R-197; second-pass `Updated` lines on R-064, R-088, R-089 and R-146; an `Updated` line on R-194; coverage; log entry.
- Findings: 1 violation, 1 gap and 3 notes. All four r1 violations are fixed, and r1 N2 and N4 are closed.
  - **V1:** R-168, R-134, Am:1494 (K8). "A close friend and an ordinary friend read exactly the same" fails correct code under the event-time B48, and points to the wrong fix. **None for the prototype, low for Phase 3.**
  - **G1:** R-194, R-096, R-186, DN:78, K14. K14 does not test that the way in is always present, or that the list itself has no seen/unseen state, and SI has no row for the way. **Low for the prototype.**
  - **Notes:**
    - N1: my r1 rubric lines went stale under event time and are superseded.
    - N2: `c6 = shown` bypasses B48 for older journeys; decide E3 (b) with E3 (c).
    - N3: E5 is listed before E4.
  - **The event-time rule leaks no friendship start:** six paths were checked, none found.
- Rubric additions: R-197. Second-pass `Updated` lines on R-064, R-088, R-089 and R-146; an `Updated` line on R-194.
- Verdict: FAIL (1 low-severity violation).
