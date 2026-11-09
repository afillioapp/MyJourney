# Rules audit: Screen Inventory, round 1 re-audit

- **Target:** `docs/Screen-Inventory.md` at commit fdb83d3 ("Screen inventory round 1: fix 16 audit findings, apply defaults"), 696 lines
- **Against:** `docs/Rules-Rubric.md` (R-001 to R-149), plus R-150 added by this audit; `docs/Decisions-Needed.md` "Provisional defaults in force" (B1–B19, C1–C16)
- **Previous audit:** `docs/reviews/2026-10-27-rules-screen-inventory.md` (FAIL, 16 findings)
- **Auditor:** Rules Guardian, 2026-10-30
- **Verdict:** **FAIL**: 3 confirmed violations (N1, N2, N3), 3 risks or weak points (N4, N5, N6), 5 notes and open questions (N7 to N11)

Line numbers are `Screen-Inventory.md` lines (SI) unless another file is named. Short names: FS = `Functional-Spec.md`, P1 = `Phase-1-Proposal.md`, CL = `CLAUDE.md`, DN = `Decisions-Needed.md`, MP = `Master-Prompt.md`, RR = `Rules-Rubric.md` (line numbers after this audit's additions). `docs/Overview.md` is not cited. `graphify-out/` does not exist in this checkout, so no graph query was run.

---

## 1. Automated checks

**No automated checks exist yet.** There is no code and no test script, so none of the rubric's auto checks can run as tests (R-137 has nothing to map). What follows are text scans over the inventory, run as evidence for this audit. They are not the build's checks.

### 1.1 Provisional labels against the Decisions table (R-149 steps 1–2, adapted to a doc)

```
$ F=docs/Screen-Inventory.md; D=docs/Decisions-Needed.md
$ grep -oE 'PROVISIONAL: [BC][0-9]{1,2}[a-f]?' $F | grep -oE '[BC][0-9]+' | sort -u
B1 B10 B11 B12 B13 B14 B15 B16 B2 B3 B4 B5 B6 B7 B8 B9 C1 C10 C11 C12 C13 C14 C15 C16 C2 C3 C4 C5 C6 C7 C8 C9
$ grep -oE '^\| [BC][0-9]{1,2} \|' $D | grep -oE '[BC][0-9]+' | sort -u
B1 B10 B11 B12 B13 B14 B15 B16 B17 B18 B19 B2 B3 ... C9
== In DN, never labelled PROVISIONAL in inventory:
B17 B18 B19
== Labelled in inventory but not in DN:
(none)
== Malformed labels:
565:PROVISIONAL                       <- "Decisions C11 (`PROVISIONAL`)", no ID in the label
== Any mention of B17/B18/B19 in inventory:
(none)
```

### 1.2 Decisions rows that name an inventory question (R-150 step 2, new)

```
$ grep -oE '^\| [BC][0-9]+ \|.*Raised as[^|]*' docs/Decisions-Needed.md | while read -r l; do ... done
OQ-37 lacks B17
OQ-38 lacks B18
OQ-39 lacks B19
--- control (OQ-36 should contain C8): found
```

### 1.3 Stale default range

```
$ grep -nE 'B1–B16' docs/Screen-Inventory.md
11:**Provisional defaults.** Where a screen depends on a question that Decisions answers with a provisional default ("Provisional defaults in force", B1–B16 and C1–C16) ...
```

### 1.4 Banned words in "Holds" cells (scanner in the scratchpad, `scan2.py`, run with `python3 -I`)

Every hit in a Holds cell, sorted:

| Line | Hit | Sorted |
|---|---|---|
| 23, 28, 30, 69, 148, 175, 200, 378, 446, 499 | "later", "new Commit", "still open", "Optional" | State names and the decided optional overview (FS:285). Fine |
| 39 | "appearances" | B12, see N9 |
| 111 | "no countdown" | A ban inside an element. Fine |
| 223 | "by count" | The owner's map computation (FS:161), with the count banned from display at the same row (C8). Fine |
| 251, 380 | "new slot", "A new overview" | Not a marker. Fine |
| 276, 541 | "with the photograph", "with photographs" | B9 (a) option: **N3** |
| 327 | "photograph one handwritten A4 page" | The note. Fine |

No banned word sits in a Holds cell as a thing allowed to appear, apart from the B9 (a) option.

### 1.5 Citation spot check

Read against the source files: FS:16, 29, 30, 44, 46, 53–57, 65, 73–76, 99–102, 127–135, 141–152, 158–165, 171, 177, 184–187, 193–196, 202–209, 228–247, 255–286, 299; P1:14–32, 44–53, 61–65, 84, 94–108, 115–143, 150–168, 180, 194–210, 222, 241, 286–288, 294, 301, 305–335, 343–347; MP:37–49, 71, 111–122, 130, 138; BP:65, 79, 92, 103–113, 228; MJC:115, 362, 446, 555, 569, 578–582, 687, 694, 740; `.claude/agents/ux.md:21`. Every one says what the inventory cites it for. The four wrong citations of finding 15 are fixed.

---

## 2. The 16 original findings

| # | Original finding | Status | Evidence |
|---|---|---|---|
| 1 | VIOLATION: sealed screen showed a way back to the note step | **RESOLVED** | The note-window state now exists only inside capture and changes only S-02 and S-12 (SI:26). S-03 never leads to S-12 (SI:99, SI:117). `sealed · note window` is "Identical to `sealed`", and the way back is banned (SI:127). S-12 can be reached from S-02 only (SI:323), with no way back after it ends (SI:328). Matches C4 (DN:42) and R-045's C4 line |
| 2 | Unlock date open to a countdown | **RESOLVED** | Plain date, never relative (SI:108). Banned on every screen (SI:48) and named on S-03, S-05 and S-06 (SI:125, 171, 199). FS:74 is now cited against P1:84 (SI:106–107), but OQ-39 ignores B19 (see N1) |
| 3 | No timer ban on the note or highlight window | **RESOLVED** | SI:87, 88, 126, 327 and 344 ban the end time, "ends in", time left, a timer and a shrinking bar or ring (R-140, B6) |
| 4 | Room for a review or re-shoot of the note page | **RESOLVED** | SI:327 bans a preview, thumbnail, review-before-save, re-shoot or gallery import of the page (R-005, R-020, R-031, R-048 under C4) |
| 5 | Controls could reveal availability | **PARTLY RESOLVED** | "None left" is covered on S-02, S-03 and S-13 (SI:85, 109, 110, 125, 343). R-138 under B6 also requires that the start control is not hidden, greyed or relabelled **while a highlight is open**. Nothing in the inventory says so (SI:344): **N4** |
| 6 | The type card could carry the quota | **RESOLVED** | Type by name only (SI:106). Quota, cadence and allowance are banned on S-03 and S-05 (SI:125, 171) |
| 7 | The profile could draw a filling ring | **RESOLVED** | Banned on S-05, S-06 and S-16 (SI:171, 199, 401). A residual under B4's other setting is **N6** |
| 8 | Rings tied to finishing, stated as settled | **RESOLVED** | Both B4 settings are described and labelled (SI:160–164, 173, 489). "(the new ring)" is gone (SI:492). Ring as reward or celebration banned (SI:173, 496) |
| 9 | "Which choices are set" invited a completion meter | **RESOLVED** | Checklist, tick per photo or step, "12 of 24", percentage and done-or-left summary are banned, with both FS:233 and MP:42 cited (SI:145). Also on S-14, S-18, S-20 and S-21 (SI:363, 444, 480, 496) |
| 10 | Readers could total tags and read rings | **RESOLVED**, standing residual | B12 and C6 are described with both settings (SI:191–195, 418–420). Totals, groupings and "people in this journey" lists are banned (SI:204, 406, 429). The S-16 route via a tag now exists only under C6 "shown" and is marked open (SI:392). The residual that R-139 and R-147 require every audit to report is **N9** |
| 11 | Feed lacked an unread-marker ban, and its order was not raised | **RESOLVED** | Banned on every screen (SI:45) and on S-08 (SI:254). Order is newest first under C14 (SI:238, OQ-40 at SI:664–665). SI:53 says an item missing from a screen's table is still banned |
| 12 | Positivity Feed said "Public photos", with no endless-content ban | **RESOLVED** in the inventory | Holds rewritten under B9 (SI:266–268, 276). Endless scroll, autoplay, "more like this" and pull to refresh banned (SI:279). R-145 still requires the "with photographs" setting to be reported: **N3** |
| 13 | No ban on an in-app "reflections are open" marker | **RESOLVED** | SI:46, 147, 174, 202, 361, 380, 427 |
| 14 | Feeling tags followed one doc, and "popular ones surface" was not raised | **PARTLY RESOLVED** | Both sides are cited and OQ-37 and OQ-38 are raised (SI:458, 463, 658–661), which was the round-1 ask. But the same commit added B17 and B18 to DN (DN:36–37), and the inventory still says "with no default" and describes both shapes: **N1** |
| 15 | Citations pointed at the wrong line | **RESOLVED** | "Reflection left" now cites Spec:280 (SI:235, 355, 626). Popularity no longer cites P1:180 (SI:254). Spec:282 is now used only for §20 L, where it belongs (SI:212, 223). Spot check in 1.5 is clean |
| 16 | Time control not shown to apply the seal | **PARTLY RESOLVED** | T-01 applies the seal, reports nothing from a sealed journey, and labels "jump to the next unlock" without whose or when (SI:516). It sits outside the product (SI:508, 534, 550). But the panel shows the simulated date (SI:515, 546), so after the jump that date is the next unlock. The "when" comes back: **N8** |

Summary: 12 resolved, 4 partly resolved, 0 not resolved, 0 regressed.

---

## 3. Findings

### N1: CONFIRMED VIOLATION. Provisional defaults B17, B18 and B19 exist but the inventory ignores them

- **Check:** R-150 (new), R-135 (provisional line, RR:990), R-134
- **Where:** SI:11, SI:106, SI:107, SI:171, SI:199, SI:458, SI:463, SI:658–663; against DN:36, DN:37, DN:38
- **What is wrong:** Commit fdb83d3 added three rows to DN: B17 "Feeling tags are free text on the journey, with no category" (DN:36), B18 "Tags never 'surface' by popularity. No suggestions and no counts" (DN:37), and B19 "The owner of a sealed journey sees its type, commit date and unlock date and nothing else" (DN:38). Each row names the inventory question it answers (OQ-37, OQ-38, OQ-39). The same commit's inventory:
  - names the default range as "B1–B16 and C1–C16" (SI:11)
  - says S-19 has "Two places the docs disagree, **with no default**" (SI:458)
  - offers feeling tags "inside a category (Spec:131) **or** on the journey (Proposal:141)" (SI:463). B17 says no category
  - says "whether popular tags surface at all is OQ-38" (SI:463). B18 says never
  - marks OQ-37, OQ-38 and OQ-39 "**Still open, no ID**" (SI:659, 661, 663)
  - shows the type and commit date on S-03, S-05 and S-06 under P1:84 alone, with "see OQ-39" and no `PROVISIONAL: B19` (SI:106–107, 171, 199)
- **Why it breaks the rule:** CL:21: "If the item has a provisional default, build that, and nothing else". R-135's provisional line (RR:990): "Building the other side, a third reading, or the default without its `PROVISIONAL:` label still fails." SI:463 describes the other side (a category) as something the step may hold. SI:106–107 build B19 without its label. Calling B18's question open (SI:463, 661) leaves a later phase free to surface popular tags, which B18 bans. The scans in 1.1 and 1.2 show this mechanically.
- **Severity:** violation
- **Fix belongs to:** the UX agent (apply B17–B19 with labels, update SI:11, 458, 463, 659–663)

### N2: CONFIRMED VIOLATION. B2's "only after reveal finished" setting is extended to Public photos and to every reader

- **Check:** R-142 (RR:1017), R-068 provisional line (RR:514), R-134, R-150 (new), CL:22
- **Where:** SI:189, SI:200, SI:372, SI:402, SI:425, SI:607; against DN:21, DN:89
- **What is wrong:** SI:189 defines B2's other setting as "No one but the owner reads it until the reveal is finished (strictest reading of the option, since it names only the network)". SI:200: "Under B2's option: others, nothing yet". SI:425: "under B2's option, the owner only until finished". SI:372 and SI:607 apply the same to overviews. So under that setting a photo the owner has already set **Public** during an unfinished reveal (in force at once under B3) is still unreadable to the public.
- **Why it breaks the rule:** DN B2 (DN:21, question at DN:89) is about whether **the network** can read an unlocked journey before its reveal is finished. R-142: "the setting changes only when the owner's network may read an unlocked journey's Network-default photos." R-068's provisional line says this exact combination "is not stated in `Decisions-Needed.md` ... if one is needed it goes to the supervisor, not into the build". CL:22: "If it is not listed, stop and ask the supervisor. Do not pick." The "strictest reading" rule (CL:24) only settles a clash between a default and the banned list. Who may read a Public photo is not a banned-list item. The reading is stated in the inventory, but it is never raised as an open question (OQ-9 at SI:596–597 does not mention it), and the screens are written under it.
- **Severity:** violation
- **Fix belongs to:** the UX agent (describe the setting as DN states it and raise the Public case as a question), then the supervisor

### N3: CONFIRMED (standing, R-145). The Positivity Feed "with photographs" setting is a photo feed

- **Check:** R-145 (RR:1035), R-086, CL:72, CL:24
- **Where:** SI:268, SI:276, SI:541
- **What is wrong:** Under B9 (a)'s other setting "Each entry shows the photograph with its reflections" (SI:268), offered on the options panel (SI:541).
- **Why it breaks the rule:** CL:72 and MP:45: "No photo feed: The feed carries announcements only, never images." Under the strictest reading (CL:24), a stream of photographs is a photo feed. R-145 says every audit lists this as a finding until the user rules on G-8. The inventory does what it should: the default is "text only" (SI:267, SI:541 lists it first), and SI:268 cites both sides and OQ-11. The fix is not the inventory's to make. It needs the user's ruling on G-8. Recorded as confirmed so the ruling is not forgotten. It is not softened because the remedy lies elsewhere.
- **Severity:** violation (standing, pending the user)

### N4: RISK. The start-highlight control may be greyed or relabelled while a highlight is open

- **Check:** R-138 (B6 line, RR:375)
- **Where:** SI:110, SI:343, SI:344
- **What is wrong:** In `sealed · highlight open`, S-13 holds "Starting another is refused (Spec:284)" (SI:344), and its never cell is "As above". "Above" bans a control hidden, greyed or relabelled "because none is left" (SI:343). It does not cover "because one is open". S-03 element 6 is "offered the same whether or not a highlight is left" (SI:110), again with nothing on the open case.
- **Why it breaks the rule:** R-138 under B6: "the start-highlight control is not hidden, greyed or relabelled while one is open; a second start is refused on tap (R-041)". A designer's reflex is to grey out "Start a highlight" while one is running. That greyed state ends exactly at start + 24 hours, so it becomes a second open-or-closed signal that tracks time.
- **Severity:** risk

### N5: RISK. "Your Journey is ready" may stand on the profile for the whole open reveal

- **Check:** R-095 (C1 line, RR:704), R-134
- **Where:** SI:172, SI:175, SI:27, SI:139, SI:612; against DN:39
- **What is wrong:** S-05 puts "Your Journey is ready" in the Holds of the `unlock-day, reveal-open` row (SI:172), and `between journeys` repeats `reveal-open` (SI:175). `reveal-open` has no end until finish or slot 2, up to a year (SI:28). Nothing says whether the line shows once, on the first open after unlock, or on every open while the reveal is unfinished. For Long Way Round #4 the second reading means a year-long banner. OQ-15's residual (SI:612) raises where the line sits, not how long.
- **Why it breaks the rule:** C1 (DN:39) says "appears on next open", in the singular. A line repeated on every open until the owner acts is an in-app nudge to finish the reveal, which R-095 bans ("no banner ... finish a reveal"). How long it shows is not settled in any doc or default, so under CL:22 it must be raised, not left to Phase 2's reflex.
- **Severity:** risk

### N6: WEAK POINT. Under B4's "per year with the app" setting, the day a ring appears is not stated or raised

- **Check:** R-143 (RR:1026), R-012, R-134
- **Where:** SI:162, SI:171, SI:172
- **What is wrong:** The other setting reads "Rings follow years since joining" (SI:162). SI:171 bans any ring that changes with the date inside a sealed year. A user whose joining anniversary falls inside their sealed year gets either a ring mid-year, which SI:171 bans, or no ring that year, which departs from "per year with the app". The inventory does not say which, and does not raise it.
- **Why it is a weak point:** R-143: "Under 'per year with the app' the docs do not say on which date a year's ring appears. If the build needs that, it goes to the supervisor". The inventory should carry this as an open question so Phase 2 does not fill it.
- **Severity:** weak point

### N7: OPEN QUESTION (note). B19 and B6 read against each other

- **Check:** R-135, R-009 (RR:111)
- **Where:** SI:111, SI:126, SI:131; DN:38 against DN:25
- **What disagrees:** B19 (DN:38): the owner of a sealed journey sees "its type, commit date and unlock date **and nothing else**". B6 (DN:25): "The owner sees only 'a highlight is open'". The inventory shows element 7 under B6 (SI:111). Read strictly (CL:24), B19 removes element 7. Read as the narrower, specific row, B6 keeps it. Both are provisional rows in the same table, neither ranks higher, and FS:74 ("not to the user") sits behind B19.
- **Not picked here.** Raised for the user. The rubric records it under R-009 and G-17 without settling it.
- **Severity:** note (not a violation: the inventory follows B6, which is labelled)

### N8: WEAK POINT / OPEN QUESTION. "Jump to the next unlock" plus the simulated date tells the demoer someone's unlock date

- **Check:** R-014, R-008
- **Where:** SI:515, SI:516, SI:546; against P1:194, P1:200, DN:54 (C16), FS:279
- **What is wrong:** T-01 offers "jump to the next unlock" (SI:515, from P1:194), and T-02 shows the simulated date (SI:546, C16). The label hides whose unlock and when (SI:516), but after the jump the shown date is the earliest unlock among all fixture users. Viewing as First Light, a jump to 2027-01-01 tells them a sealed journey unlocks that day.
- **Why it matters:** R-014 lists "the time-control panel" among the paths that must apply the seal. FS:279 (§20 I): others may know only that a sealed journey exists. The control (P1:194, approved) and the date display (C16) are both sourced, and the demoer is not a product user. So the docs pull two ways. **Not picked here.** Raised for the user: is the demoer exempt from R-008, or does "jump to the next unlock" jump only to the selected viewer's own next unlock?
- **Severity:** weak point

### N9: NOTE (standing weakest point, R-139, R-147, R-148)

- **Where:** SI:192 (B12 "shown"), SI:392 and SI:420 (C6 "shown" tag to profile)
- Under B12's default a reader sees, in place, each photo where they are tagged (SI:192). With no total, they can still count by scrolling and get a floor on their ring (G-12). R-139 and R-147 require every audit to report this until the user decides. Under C6 "shown", whether a tag leads to that person's profile is still open (OQ-20, SI:622). R-148 says a tag that links to a profile is a finding until the supervisor answers. The inventory marks it open, so it is a note here.
- **Severity:** note

### N10: NOTE. Readings filled in on residuals that are raised

- **Check:** R-134
- **Where:** SI:327 with SI:630 (skip ends the note step); SI:87 with SI:634 (B6 shown on S-03 and S-13, not S-02); SI:139 and SI:172 with SI:612 (C1 and C12 together place "ready" on the profile)
- Each is labelled as the inventory's reading and raised in an open question, so none is silent. They still shape the screens, and each needs the user's yes before Phase 2 treats it as settled. One related observation: the note step closing at 15 minutes while the user is on it (SI:327) is itself a visible time signal. No timer is shown (R-140 holds), and OQ-24's residual raises what the user sees then.
- **Severity:** note

### N11: WEAK POINT. A provisional label without its ID

- **Check:** R-149 (form), R-150
- **Where:** SI:565 "Decisions C11 (`PROVISIONAL`)"
- The label form is `PROVISIONAL: <ID>` (DN:16, SI:11). This one carries no ID, so a label scan (1.1) cannot trace it. Trivial to fix, and the kind of thing that drifts into code.
- **Severity:** weak point

---

## 4. What held

Recorded so the next audit does not reopen it:

- Every one of B1–B16 and C1–C16 the inventory uses matches its DN row's wording. That covers B1 (SI:257, 479), B3, B4, B5 (the line is fixed and the graph switchable, consistent with R-144), B6, B7, B8, B9 (b)–(f), B10, B11 (named or unnamed, as R-146), B12, B13, B14, B15, B16, and C1–C16. The exceptions are N1 and N2
- All seven switchable defaults are on T-02 with exactly two settings, the default first (SI:538–544). Nothing else is switchable, and the panel bans any switch not marked switchable (SI:550; R-141)
- No new leak from a sealed year: S-03, S-05, S-06 and S-16 hold only what P1:84 and FS:279 allow (SI:105–113, 171, 199, 401), and the note-window state no longer touches S-03
- No edit path on reflections or overviews (SI:363, 382). No image in the announcement feed, including avatars (SI:254). No layer shown to the person on it (SI:204, 226, 406, 444)
- The "applies to every screen" block (SI:42–53) now carries B8, R-096, R-095, R-104, C2, C7, C15 and B15, and says an item missing from a table is still banned

---

## 5. Rubric additions

| ID | Area | Statement (short) | From | Automatable |
|---|---|---|---|---|
| R-150 | 14. Provisional defaults | A deliverable (doc or code) describes each question that has a provisional default under that default only, worded as the row, labelled `PROVISIONAL: <ID>`. It never calls such a question open, never states a range that omits rows, and never extends a default or switch setting to cases its row does not name | N1, N2 | Steps 1–3 are auto (shell, tested on this inventory: step 2 printed `OQ-37 lacks B17`, `OQ-38 lacks B18`, `OQ-39 lacks B19`; control OQ-36/C8 found). Step 4 is review |

Also added, without renumbering or removing anything:

- `Provisional default` lines for B19 under R-009 (with the B6 tension, N7), B18 under R-103, and B17 and B18 under G-14, B19 under G-17
- The source key now lists B1–B19
- A dated note under R-149 that its sample (`B17` caught as missing) is out of date, since B17 now exists
- A line under the banned-list coverage table saying R-150 applies to every row

**Could be automated now:** R-149 and R-150 steps 1–3 run on docs today and should run on every deliverable before audit. R-013, R-096, R-124 and R-140 grep aids can run as copy scans over the inventory, as in 1.4, until code exists.

---

## Report
- Files changed: /home/user/MyJourney/docs/Rules-Rubric.md, /home/user/MyJourney/docs/reviews/2026-10-30-rules-screen-inventory-r1.md
- Findings: 11
  - N1, R-150/R-135/R-134, SI:11, 458, 463, 659–663, 106–107: B17, B18 and B19 (DN:36–38) not applied or labelled; OQ-37 to OQ-39 called "no ID"; S-19 still offers a category (CONFIRMED)
  - N2, R-142/R-068/R-134/R-150, SI:189, 200, 372, 425: B2's "only after reveal finished" setting extended to Public photos and all readers, never raised (CONFIRMED)
  - N3, R-145/CL:72, SI:268, 276, 541: B9 (a) "with photographs" is a photo feed under the strictest reading, pending the user's ruling on G-8 (CONFIRMED, standing)
  - N4, R-138, SI:344, 110: start-highlight control not protected from greying while a highlight is open (risk)
  - N5, R-095/R-134, SI:172, 175: how long "Your Journey is ready" shows is not stated or raised; it could stand all year (risk)
  - N6, R-143/R-012, SI:162, 171: under B4 "per year with the app", the day a ring appears is not raised (weak point)
  - N7, R-135/R-009, SI:111 vs DN:38 and DN:25: B19 "nothing else" against B6 "a highlight is open" (open question)
  - N8, R-014/R-008, SI:515–516, 546: jumping to the next unlock and then showing the date reveals someone's unlock date (open question)
  - N9, R-139/R-147/R-148, SI:192, 392: count-by-scrolling residual; tag-to-profile link still open (standing note)
  - N10, R-134, SI:327, 87, 612: readings filled in on residuals that are raised (note)
  - N11, R-149/R-150, SI:565: `PROVISIONAL` label without an ID (weak point)
- Rubric additions: R-150; Provisional default lines for B17–B19 under R-009, R-103, G-14 and G-17
- Verdict: FAIL

---

## Supervisor verification (2026-10-30)

Each confirmed finding was checked against the files. None dropped.

- **N1 holds.** DN:36–38 define B17–B19. SI:11 still says "B1–B16". SI:458 says "with no default". SI:659–663 mark OQ-37/38/39 "Still open, no ID". `grep B17\|B18\|B19` on the inventory returns nothing.
- **N2 holds.** SI:189 reads the B2 option as "No one but the owner reads it". DN:21 names only the network. R-142 limits the setting to Network-default photos, and the R-068 note sends the Public case to the supervisor.
- **N3 holds as a standing finding.** R-145 requires every audit to list the "with photographs" setting until the user rules on G-8. The inventory's default is "text only" (SI:268, 276), which is correct.
