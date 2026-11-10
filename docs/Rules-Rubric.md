# My Journey: Rules Rubric

Owner: Rules Guardian (`.claude/agents/rules-guardian.md`). Build Plan Phase 1 deliverable, "The rules list as testable statements, one line each" (`Build-Plan.md:63`).

Version 1, 2026-10-27. No code exists yet. Nothing below has been audited.

Last updated: 2026-10-27 (second pass). Aligned with the provisional defaults in `Decisions-Needed.md` (B1–B16, C1–C16, approved by the user on 2026-10-27 for the prototype). Added R-141 to R-149. Added "Provisional default" lines to checks and Gaps. Marked the Gaps that section A is fixing. Re-cited every `CL:` line after the 2026-10-27 rule zero rewrite moved `CLAUDE.md` down (old 15 → 17; old 21 onward +9). No check renumbered or removed.

Updated 2026-10-30 (re-audit of `Screen-Inventory.md` round 1, `docs/reviews/2026-10-30-rules-screen-inventory-r1.md`): added R-150. Added `Provisional default` lines for B17, B18 and B19, which `Decisions-Needed.md` gained in commit fdb83d3, under R-009, R-103, G-14 and G-17. No check renumbered or removed.

Updated 2026-10-30 (rules audit `docs/reviews/2026-10-30-rules-phase-1-r4.md`, after FS §20 T–DD and Decisions-Needed B20–B26): added R-151 (highlight facts after unlock, FS §20 DD, B24) and R-152 (journey type, dates, chapter and feeling tags never public, FS §20 T, CC). Added `Decided` lines for FS §20 U (R-040, R-043), X (R-068, R-142) and Z (R-141), and `Provisional default` lines for B20–B26 under R-040, R-117, R-119 and R-141. Corrected R-103's B9 reading, which still said "may be filtered by chapter" after FS §20 Y, and R-116's source `FS:299` (now §20 W) to `FS:321` (§21). No check renumbered or removed.

Updated 2026-10-30 (rules audit `docs/reviews/2026-10-30-rules-phase-1-r5.md`, after FS §20 EE–HH): added R-153 (only the panel moves time or flips switches, FS §20 EE) and R-154 (non-owners see a capture date, never its time, FS §20 GG). Added `Decided` lines for FS §20 EE (R-141), FF (R-070), GG (R-151 residual) and HH (R-063, R-142). No check renumbered or removed.

Updated 2026-10-31 (rules audit `docs/reviews/2026-10-31-rules-phase-1-r6.md`, after FS §20 II–VV): added R-155 to R-165 and G-23. FS §20 MM and OO leave the product roles with no privilege on any user-content table, so a direct `count(*)` is refused rather than 0. `Updated 2026-10-31` how-to-check lines therefore move each affected test onto the readers and the table owner (R-164 lists them). Added `Decided` lines for FS §20 TT (R-008, R-152), SS (R-152), LL and JJ (R-154), UU (R-088, R-089), and PP and VV (R-031). Corrected R-116's source: §21 moved to FS:335 when §20 grew. The highlight list proposed in `Phase-1-Amendments.md` §4 item 1, now including `highlight_rows`, is R-156. The id and sequence check of §4 item 6 is R-155. No check renumbered or removed.

Updated 2026-10-31 (rules audit `docs/reviews/2026-10-31-rules-phase-1-r7.md`, after FS §20 WW–HHH): added R-166 (another user's circle comes from a count that moves only on a finished reveal and is never shown as a number, FS §20 CCC, WW), R-167 (the guard-bug log carries nothing about a user and no product role reads it, FS §20 DDD, FFF), R-168 (no screen state holds what its own never-list bans) and G-24 (DDD against GGG). Added `Decided` lines for FS §20 XX, AAA, DDD, GGG and HHH (R-160, whose r6 `Open` note is closed by XX and AAA), AAA, BBB and DDD (R-155 (d)), EEE (R-152), WW (R-161), ZZ and CCC (R-162, G-23). `Updated` lines on R-116 (§21 moved to FS:350), R-160 (note-step cases), R-161 and R-162 (implementation now specified) and R-165 (wider open-word list; OQ answers that name a screen). No check renumbered or removed.

Updated 2026-10-31 (rules audit `docs/reviews/2026-10-31-rules-phase-1-r8.md`, after FS §20 III–PPP): added R-169 (the note handle never leaves the server route, FS §20 LLL), R-170 (a lost press and its note look and answer exactly like a saved one, FS §20 DDD, JJJ, NNN), R-171 (every note-route answer and every end of the note step has a screen row, FS §20 PPP) and G-25 (a lost press that would have been refused). Added `Decided` lines for FS §20 JJJ (R-160, closing G-24, and R-168), III, LLL, MMM, NNN and PPP (R-160), KKK (R-152), OOO (R-120, R-161). R-160's GGG line and its r7 (3) wording ("no S-12 offer") held the behaviour JJJ retired: they are kept as history and superseded by the JJJ line, not deleted. `Updated` lines on R-116 (§21 moved to FS:361), R-165 ((5) and (6)) and R-167 (scope). No check renumbered or removed.

Updated 2026-10-31 (rules audit `docs/reviews/2026-10-31-rules-phase-1-r9.md`, after FS §20 QQQ–XXX): added R-172 (a dated record is appended to, never rewritten to cite a later ruling), R-173 (a note step that has ended on screen has ended at the server: no later note press for that press is taken, whatever the device sends, FS §20 WWW, III) and G-26 (a note window that crosses the journey's unlock). Added `Decided` lines for FS §20 QQQ (R-160, R-170, closing R-170's `Open` note and G-25), RRR, UUU, VVV and WWW (R-160, R-171), XXX (R-086, R-126, G-9, G-10), and `Accepted residual` lines for SSS (R-138, R-160) and TTT (R-170). `Updated` lines on R-116 (§21 moved to FS:371), R-159 (the guard now runs after the press is judged, FS §20 QQQ), R-170 ((3) read "a lost press does no strip", which r8 N3's carriage retired; added (4), the press's own timing) and R-171 (the ends list after WWW and UUU). Lead-tech flagged R-170 (3) and the R-170 G-25 `Open` line as stale; both are kept as history and superseded, not deleted. No check renumbered or removed.

Updated 2026-10-31 (rules audit `docs/reviews/2026-10-31-rules-phase-1-r10.md`, after FS §20 YYY–BBBB): added R-174 (a ruling's general words are carried only with the thing it rules, so "nothing is added to a journey once it unlocks" never bars a reveal write), R-175 (a client act that a server rule depends on is stated on the screen that performs it, for every trigger the server design names), G-27 (capture or the note step open at the unlock instant) and G-28 (what counts as leaving capture). Closed G-26 (FS §20 YYY, BBBB). Added `Decided` lines for YYY (R-170, R-171, G-26), ZZZ (R-160, R-170), BBBB (R-171) and `Accepted residual` lines for AAAA (R-170) and BBBB (a) (R-173). `Updated` lines on R-116 (§21 moved to FS:375, "A time control" FS:379), R-165 ((4) also covers body lines that assign a behaviour to a named screen), R-169 ((2) also scans for the journey id, which the route entry now holds) and R-170 ((4): a busy indicator shown only after a delay fails). No check renumbered or removed.

Updated 2026-11-04 (rules audit `docs/reviews/2026-11-04-rules-flows.md`, of `Flows.md`): added R-176 (a doc's "what you see" holds only what that viewer's screen may show) and R-177 (a new ID is declared as new and cannot be misread as an ID from another family). Added R-176 to two rows of Banned-list coverage. No check renumbered or removed.

Updated 2026-11-04 (rules re-audit `docs/reviews/2026-11-04-rules-flows-r2.md`, of `Flows.md` revision round 1): added R-178 (a word marking something undecided is never attached to a banned-list rule or a §20 ruling) and an `Updated` line on R-176 (a blanket "never on any screen" fails). Added R-178 to two rows of Banned-list coverage. No check renumbered or removed.

Updated 2026-11-05 (supervisor, from rules audit `docs/reviews/2026-11-04-rules-art-microcopy.md` P-1 to P-8): added R-179 to R-186 after R-178. Each names its area, because they were added in one place to keep numbering in order. No check renumbered or removed.

Updated 2026-11-05 (rules re-audit `docs/reviews/2026-11-05-rules-art-microcopy-r2.md`, of `Art-Direction.md`, `Microcopy.md` and Decisions-Needed B27–B41): added R-187 after R-186, in area 14 (provisional defaults hold when read together). Added `Updated` lines on R-177 (cited IDs after another doc renames its family) and R-180 (a cell naming only an AD-n, or following one side "until the user rules"). No check renumbered or removed.

Updated 2026-11-05 (rules re-audit `docs/reviews/2026-11-05-rules-art-microcopy-r3.md`, final round of `Art-Direction.md` and `Microcopy.md`): an `Updated` line on R-187 (compare at more than one clock point). No new check. No check renumbered or removed.

Updated 2026-11-09 (supervisor, user rulings FS §20 EEEE–HHHH): C2's checks now read as decided (EEEE); R-130 gains an `Updated` line (HHHH). No check renumbered or removed.

Updated 2026-11-09 (rules audit `docs/reviews/2026-11-09-rules-kkkk.md`, of FS §20 KKKK's carriage: `Phase-1-Amendments.md` §12–§13, Decisions-Needed E1–E4 and B43–B54, and the FS, Concept, P1 and CLAUDE.md lines): added R-188 to R-196 after R-187, each naming its area, from §12.7's proposed K2–K7, K10, K12 and the audit's own V1 and V4. Added R-188, R-192, R-193 and R-194 to three rows of Banned-list coverage. Added `Updated` lines for KKKK on R-053, R-060, R-061, R-063, R-064, R-065, R-066, R-069, R-070, R-081, R-088, R-089, R-142, R-146, R-155, R-157, R-162 and G-3 (OQ-49, OQ-53, and R-053, R-142, R-162, which OQ-53 missed). No check renumbered or removed.

Updated 2026-11-09 (rules re-audit `docs/reviews/2026-11-09-rules-kkkk-r2.md`, after the fixes for the KKKK audit): added R-197 after R-196 (the event-time announcement audience, K13). Second-pass `Updated` lines on R-064, R-088, R-089 and R-146, because `PROVISIONAL: B48` changed from read time to event time after this rubric's first-pass lines were written; those lines are kept as history and superseded, not rewritten (R-172). `Updated` line on R-194 (the way in is always present; no read state inside the list). Added R-197 to Banned-list coverage. No check renumbered or removed.

Updated 2026-11-09 (rules audit `docs/reviews/2026-11-09-rules-friend-screens.md`, of the ux pass for FS §20 KKKK (`Screen-Inventory.md` S-05, S-16, S-22 to S-24, OQ-55 to OQ-57; `Flows.md` Flow 10, opening, prototype table, DC-15, DC-16) and Decisions-Needed B57–B61): `Updated` lines on R-150 (step 2 also finds rows added "from Screen-Inventory OQ-n" or that "settle" an OQ or DC) and R-176 (prototype "On screen" cells checked against the fixture's derived state, untouched rows included). No new check. No check renumbered or removed.

Updated 2026-11-10 (supervisor, carrying FS §20 NNNN, LLLL, MMMM; not an audit): `Updated` lines on R-071, R-092, R-139, R-141, R-146, R-147, R-148, R-149, the §14 intro and G-12. B11, B12 and C6 are no longer switches: B11 is always unnamed, B12 and C6 always hidden. No check added, renumbered or removed. The rules-guardian should re-read these on the next audit.

Updated 2026-11-10, second pass (supervisor, carrying FS §20 MMMM, OOOO to XXXX; not an audit): `Updated` lines on R-121, R-122, R-138, R-140 and the C5 line; G-1 closed. Blocking (MMMM, Phase-1-Amendments §15) has no check yet: §15.5 lists the cases for the rules-guardian to turn into checks.

Updated 2026-11-10 (rules audit `docs/reviews/2026-11-10-rules-supervisor-carriage.md`, of the supervisor's carriage of FS §20 LLLL–XXXX, git a3b9a4f..7ad6990): added R-198 to R-209, each under its area (R-198 supersedes R-121; R-199, R-201 in area 1; R-205 in 3; R-202 to R-204 in 5; R-206 in 7; R-200, R-207 in 8; R-198 in 11; R-208, R-209 in 13). Blocking (MMMM) now has checks R-202 to R-204, from `Phase-1-Amendments.md` §15.5. `Updated` lines on R-121 (superseded), R-138, R-146, R-156. R-140's 2026-11-10 `Updated` line, which sat after the area 8 separator, moved back under R-140 with its text unchanged. Banned-list coverage gains R-199 to R-205 and R-207. No check renumbered or removed.

---

## What this is for

Every later audit and every rules test runs against this list. Each check states a behaviour the product guarantees, written so that an auditor can decide it and a test author can automate it.

- **auto**: a test, scan or script can decide it. These must run in the build and fail it (R-137)
- **review**: a person has to read the screen, copy or design to decide it

The stack was decided 2026-10-30: local Postgres first (`Status.md`); the deploy host is still open (L-004). Each statement describes behaviour. Where a check names Postgres grants, triggers or row-level security, that is the **current implementation** from `Phase-1-Proposal.md` §2.1, recorded so the test author knows where the rule lives today. If the stack changes, the statement stays and the mechanism changes.

## How the rubric grows

- **It never shrinks.** No check is deleted. A check that stops applying is marked `Superseded by R-nnn on <date>` and stays in place (`Build-Plan.md:222`)
- **It never renumbers.** A new check takes the next free number and goes under its area heading, so numbers inside an area need not be consecutive
- **Every finding becomes a check.** When an audit finds a new kind of violation, the check is added here before the audit report is closed (`Build-Plan.md:220–222`)
- A check marked **Provisional** depends on a contradiction listed under Gaps. It runs as written until the user settles the gap, then it is confirmed or superseded
- **Provisional defaults (rule zero as of 2026-10-27, CL:19–24).** Where `Decisions-Needed.md` "Provisional defaults in force" covers a check or a Gap, a line `Provisional default: Decisions-Needed <ID>: <default>` says how the check reads under that default. The prototype is audited against that reading. A provisional default is not a decision: the check is confirmed or superseded only when the user decides and `FS` §20 records it. Where the default is **switchable**, the check must pass under both settings (R-141 to R-148). No default may weaken a banned-list check; where a default and the banned list could be read two ways, the strictest reading wins (CL:24)

## Source key

| Short | File |
|---|---|
| CL | `CLAUDE.md` |
| MP | `docs/Master-Prompt.md` |
| FS | `docs/Functional-Spec.md` |
| P1 | `docs/Phase-1-Proposal.md` |
| BP | `docs/Build-Plan.md` |
| MJC | `docs/My-Journey-Concept.md` (cited only for §29 and under Gaps) |
| RG | `.claude/agents/rules-guardian.md` |
| DN | `docs/Decisions-Needed.md` (cited by ID: A1–A12, B1–B26, C1–C18 (C17, C18 added 2026-10-30); B17–B19 added 2026-10-27 in fdb83d3) |

`docs/Overview.md` is historical and is never cited.

Test fixtures named below come from `Phase-1-Proposal.md` §3. Steady Lantern #6 (committed 2026-01-01, unlocks 2027-01-01) is the standard sealed journey. Baseline is 2026-10-25.

---

## 1. Sealing and leaks

### R-001
- **Statement:** As the owner, before unlock, no query or endpoint returns any photo row, photo count or photo image from the sealed journey.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:73, CL:81, FS:74–75, FS:234, P1:48. **= §2.5 check 4** (rows and count)
- **How to check:** As Steady Lantern at simulated 2026-12-31 23:59:59, list Lantern #6 photos (expect 0 rows), count them (expect 0), and fetch a known photo id from the fixture (expect not found or refused). Repeat at 2027-01-01 00:00:00 and expect the rows. Run the same as the app's own database role, not only through the API.
- **Current implementation:** row-level security on photo rows, readable only when `app_now() >= unlocks_at`, owner included (P1:48a).
- **Updated 2026-10-31 (FS §20 MM, OO; R-164):** the viewer role holds no privilege on any user-content table, so "list" and "count" are read through `photo_read` and `note_read` (expect 0 rows, `count(*)` 0), and the same statements on the tables themselves, `EXPLAIN` included, must be refused (`permission denied`). The refusal on the table does not stand in for the 0-row half: both are required. `EXPLAIN` on each reader shows the fixed estimate before and after (R-157)

### R-002
- **Statement:** Before unlock, every stored image of a sealed journey, photo and note alike, is ciphertext to everyone, and nothing releases its key until unlock.
- **Type:** auto · **Applies to:** data
- **Source:** FS:234, P1:48b, P1:105. **= §2.5 check 4** (blobs)
- **How to check:** Read the raw stored bytes of a Lantern #6 photo and note before unlock. They must not start with any image signature (JPEG `FF D8 FF`, PNG `89 50 4E 47`, WebP `RIFF....WEBP`, HEIC `ftyp`). Call the key-release path before unlock: refused. Call it at unlock: key returned.
- **Current implementation:** per-journey key released by one function, only after unlock (P1:48b).
- **Updated 2026-10-31 (FS §20 MM, OO; R-164):** no product role can read the stored bytes (the tables refuse, and before unlock the readers return no row), so the test reads the raw bytes as the table's owning role, outside any product connection, and runs the signature check on those. Added: after unlock, the decrypted image has no metadata segment (R-159)

### R-003
- **Statement:** Before unlock, no handwritten note, tag, person tag or reflection belonging to a sealed journey is readable by anyone, the owner included.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:74, FS:234, P1:48a. **= §2.5 check 4** (extended to the other sealed rows P1:48 names)
- **How to check:** The R-001 access test, run against every table and endpoint that holds note, tag, person-tag or reflection data for Lantern #6.
- **Updated 2026-10-31 (FS §20 OO; R-164):** "every table and endpoint" now means every reader (`note_read`, `person_tag_rows()`, `journey_chapter_rows()`, `journey_feeling_tag_rows()`, `reflection_rows()`, `photo_visibility_rows()`, `highlight_rows()`) and every route: 0 rows for Lantern #6. Each of those tables refuses the viewer role directly

### R-004
- **Statement:** No plaintext copy, thumbnail, resized preview or other derivative of a sealed photo or note exists anywhere: server storage, CDN, logs, browser cache, IndexedDB, local storage, service-worker cache or a live object URL.
- **Type:** auto · **Applies to:** data, UI
- **Source:** CL:73 ("Not thumbnails"), MP:46, FS:75, FS:234
- **How to check:** In a browser test, capture one photo and one note, then (a) scan server storage for files with image signatures that belong to the sealed journey, (b) grep server logs for base64 image data, (c) list Cache Storage, IndexedDB and localStorage and confirm no image bytes, (d) confirm every `URL.createObjectURL` made during capture has been revoked. Grep the capture path for resize, thumbnail, `sharp`, `jimp`, `canvas.toBlob` writes that are kept.

### R-005
- **Statement:** Once the shutter is pressed, the app shows nothing of the photo just taken: no preview, no "last shot" corner thumbnail, no review screen.
- **Type:** auto · **Applies to:** UI
- **Source:** FS:58, FS:74, FS:228 ("no review-before-save"), CL:99 ("Sealed instantly")
- **How to check:** UI test: after the shutter tap, no `img`, `canvas`, `video` or CSS background in the DOM is sourced from the captured frame. The live viewfinder before the tap is allowed. Same after the note photo is taken.

### R-006
- **Statement:** Nothing shows or returns how many photos a sealed journey holds, in any form: a number, "3 moments captured", "n frames", "n of 24", tally marks, dots, a list length, a pagination total, or a response whose size grows with the count.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** CL:73, MP:46, FS:75, FS:243, FS:246
- **How to check:** (a) Grep all copy and templates for `moments? captured`, `\d+\s*(photos?|moments?|frames?|shots?|pictures?)`, `\bof \d+\b`, `frames? (left|used|remaining)`, `so far`. (b) As owner and as another user, call every endpoint about a sealed journey holding 0 photos and one holding 17 (Open Hands #4): the responses must be byte-identical apart from ids. (c) Review every screen showing a sealed journey for any visual tally.

### R-007
- **Statement:** A sealed photo never appears as a placeholder: no blurred, greyed, locked, disabled-but-visible or silhouette tile stands for it.
- **Type:** auto · **Applies to:** UI
- **Source:** FS:75 ("No previews ... no thumbnails"), CL:73
- **How to check:** Render the sealed-journey view for a journey with 0 photos and one with 17. The DOM trees must be identical. Review the sealed-year empty state for per-photo shapes.

### R-008
- **Statement:** Anyone other than the owner learns only that a sealed journey exists: a single yes or no. Not its type, commit date, unlock date, highlights, frames used or when anything was captured.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:246, FS:279 (§20 I), P1:30 (D17), P1:84, CL:101
- **How to check:** As Second Wind, call every endpoint and open every screen about Steady Lantern during Lantern #6. Compare with the same calls about First Light (no journey). The only difference allowed is the journey-underway flag.
- **Current implementation:** `has_journey_underway(user)` returns true or false (P1:84).
- **Provisional default:** Decisions-Needed B6: Others learn nothing about highlights. Holds as written, and now explicitly covers the highlight record, which `P1:48` did not seal until FS §20 AA (2026-10-30) sealed it: no endpoint or screen tells anyone but the owner that a highlight was started, is open, or when. Add to the comparison a run where Steady Lantern has a highlight open: Second Wind's responses must still match the First Light run apart from the journey-underway flag (closes G-13 for others)
- **Decided 2026-10-31 (FS §20 TT, `FS:324`):** others never learn a user's join date (R-161). A join date can equal the commit date of a journey that is still sealed

### R-009
- **Statement:** The owner of a sealed journey sees its type, commit date and unlock date, and nothing else about it.
- **Type:** auto · **Applies to:** API, UI
- **Source:** P1:84, FS:74. See G-17
- **How to check:** As Steady Lantern before 2027-01-01, list every field returned about Lantern #6. Anything beyond type, commit date, unlock date and identifiers fails.
- **Decided 2026-11-09 (FS §20 EEEE, was Decisions-Needed C2):** The unlock date is shown as a plain date, never relative ("in 64 days"). The owner's unlock date is allowed as a date only (see R-013)
- **Provisional default:** Decisions-Needed B6: The owner sees only "a highlight is open", with no end time and no countdown. Under B6 the check reads: type, commit date, unlock date and, while a highlight is open, the bare fact that one is open. Its start time, end time, elapsed or remaining time, how many highlights are used or left, and any photo count in it all fail
- **Provisional default:** Decisions-Needed C3: The sealed-year screen does not point to earlier journeys. Nothing about an earlier journey, including an open reflection slot, appears on the sealed-year screen
- **Provisional default:** Decisions-Needed B19: The owner of a sealed journey sees its type, commit date and unlock date and nothing else (`P1:84`; `FS:74` read as covering the contents). Holds as written; B19 settles the first half of G-17 for the prototype. B19's "nothing else" and B6's "a highlight is open" (line above) read against each other. **Decided 2026-10-30 (FS §20 S):** B6 holds; the owner sees "a highlight is open", nothing more

### R-010
- **Statement:** A capture changes nothing that any reader can observe, the owner included: no "last captured", "active today", "captured this week", recent-activity mark or announcement.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:246, FS:74, CL:73
- **How to check:** As Lantern, Second Wind and First Light, snapshot every read endpoint about Lantern. Capture a photo as Lantern. Snapshot again. Every snapshot must match its earlier one. The capture call's own `accepted` reply is the only thing that differs.
- **Updated 2026-10-31 (FS §20 MM, OO):** the snapshots cover every reader's output for each of the three viewers, plus the R-157 differential catalog fingerprint. A direct `count(*)` on a table is refused and does not count as a snapshot

### R-011
- **Statement:** The activity graph for a journey is never shown or returned while that journey is sealed. It appears only after the year unlocks.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:187, CL:111, MP:85, P1:50
- **How to check:** As owner and as a network member before 2027-01-01, request activity data for Lantern #6 (expect none) and render Lantern's profile (no activity element for #6). After unlock, expect it.
- **Current implementation:** built from `captured_at`, unreadable while sealed (P1:50).
- **Provisional default:** Decisions-Needed B5 (switchable, R-144): The activity line twists in at reveal finished; the graph is visible to the owner only (other setting: built from the photos the viewer can see). Holds as written under both settings. Tighter under B5: for a journey that has unlocked but whose reveal is not finished (Long Way Round #4), the line does not twist into the circle

### R-012
- **Statement:** During a sealed year nothing fills, grows or advances to show how far the year or the quota has got: no progress ring or arc on the circle for the current year, no "month 7 of 12", no elapsed-time bar, no grid being filled.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:186–187, FS:233, CL:69, CL:111
- **How to check:** Review the profile circle and every journey screen at several simulated dates inside one sealed year (for example 2026-02-01, 2026-07-01, 2026-12-31). Nothing may differ between those dates except the plain unlock date. Grep aid: `<progress`, `role="progressbar"`, `aria-valuenow`, `stroke-dashoffset` or arc angles computed from the date.

### R-013
- **Statement:** There is no countdown to unlock: no "n days to go", "unlocks in", timer or ticking display. The owner may see the unlock date as a date.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:69 (counters), FS:233 ("No visible counters"), RG:28 ("timers counting down to unlock"), P1:84 (date shown to owner). See G-17
- **How to check:** Grep copy and code for `days? (left|to go|until|remaining)`, `unlocks? in`, `countdown`, `time left`, `\d+\s*d\s*\d+\s*h`, and any `setInterval` or `requestAnimationFrame` that formats a time until `unlocks_at`.
- **Decided 2026-11-09 (FS §20 EEEE, was Decisions-Needed C2):** The unlock date is shown as a plain date, never relative ("in 64 days"). Firm under C2: any relative form of the unlock date fails, including "next month", "soon", "in a few weeks", "this winter" and `Intl.RelativeTimeFormat` or a library's `fromNow`/`formatDistance` applied to `unlocks_at`. Add those to the grep

### R-014
- **Statement:** Every path that can return data applies the seal: search, export, error messages, logs shown to users, debug and admin routes, and the time-control panel.
- **Type:** auto · **Applies to:** API, UI
- **Source:** CL:81 ("unreadable, not merely hidden in the UI"), FS:234
- **How to check:** Build the route list from the code. Run the R-001 and R-008 tests against every route. Trigger each capture refusal and confirm the error text holds no number and no photo data.

### R-151
- **Statement:** After unlock, only the owner learns anything about the journey's highlights: whether a photo was taken in a highlight, when a highlight started or ended, and how many there were. No other reader, network or public, learns it from any row, column, field, marker or grouping.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS §20 DD (`photo.highlight_id` owner only, also after unlock), DN B24 (highlight rows owner only after unlock), DN B6 ("Others learn nothing about highlights", with no time limit), FS §20 AA. R-008 covers only the sealed year. Found by `docs/reviews/2026-10-30-rules-phase-1-r4.md` finding V2 (`Phase-1-Amendments.md:226` still makes `highlight_id` "as readable as the photo itself")
- **How to check:** At baseline, as Second Wind (on Lantern's map) and as First Light (public reader), read every Lantern #1 photo Wind or Light can read, 4 of Wind's tagged photos being inside the graduation-party highlight (P1:266): no response carries `highlight_id`, a highlight id, or any field that differs between highlight and normal photos; `highlight` rows return 0 rows. Repeat as Lantern: `highlight_id` and the highlight rows are present. UI review of Walking a path, A photo followed forward and Another user's profile as a non-owner: no "highlight" label, badge, border, grouping or section. Grep aid: `highlight` in reader-side components and serializers.
- **Current implementation:** RLS on `highlight` with owner-only readers after unlock (B24); `photo.highlight_id` withheld from non-owners by a column grant or an owner-aware view, since row-level security alone cannot hide one column of a readable row. Before 2026-10-30, `P1:92` did not say how. **Updated 2026-10-30:** now stated in `P1:48` (e) and `P1:92`: column grant without `highlight_id`, owner-only `photo_highlight_id()`, read view `photo_read` (Phase-1-Amendments §4 item 4).
- **Provisional default:** Decisions-Needed B24: After unlock, highlight rows are readable by the owner only. Holds as written
- **Residual (weakest point, reported by every audit; narrowed by FS §20 GG on 2026-10-30, see next line):** readers who can see `captured_at` of many photos from one day (Lantern #1: 19 in 24 hours) can infer a highlight. Neither DD nor B24 addresses it; it goes to the supervisor, not into the build
- **Decided 2026-10-30 (FS §20 GG, `FS:311`):** readers other than the owner see a photo's capture date, never its time (R-154). This narrows the residual above but does not close it: 19 Lantern #1 photos dated the same day still suggest a highlight. The residual stays reported until the user rules on it
- **Updated 2026-10-31 (FS §20 MM, OO):** "`highlight` rows return 0 rows" is read through `highlight_rows()`; the `highlight` table refuses every product role. The only ways highlight rows can be reached are fixed by R-156

### R-156
- **Statement:** Highlight rows can be reached by a product session in four ways only: `capture()` and `start_highlight()` (which answer accepted or refused), `highlight_open()` (true or false, owner only, R-009) and the owner's reader after unlock. No other function, view, policy, rule or trigger can read or write them.
- **Type:** auto · **Applies to:** data
- **Source:** FS §20 AA, DD, MM; DN B6, B24; R-008, R-151. Proposed by `Phase-1-Amendments.md` §4 item 1 (line 264), with the list extended to `highlight_rows` for FS §20 MM (§10). Numbered by `docs/reviews/2026-10-31-rules-phase-1-r6.md`
- **How to check:** As the table owner, list every object whose definition names the relation `highlight` as a whole identifier, not as part of another name (`highlight_id`, `highlight_open`, `start_highlight`). Scan `pg_get_functiondef()` for every function, `pg_get_viewdef()` for every view and materialised view, `pg_policies.qual` and `with_check` for policies on every other table, `pg_rewrite` rules and trigger functions, and, for SQL-standard bodies, `pg_depend` rows on `'highlight'::regclass`. The set must equal {`capture`, `start_highlight`, `highlight_open`, `highlight_rows`}. A name scan cannot see a table named at run time, so the check also fails on any function owned by the table owner whose body builds SQL at run time (PL/pgSQL `EXECUTE`, `format(` used to build a statement, `query_to_xml`, `dblink`), unless the rules-guardian has reviewed it onto a closed list. The R-151 and R-008 tests must then pass.
- **Current implementation:** highlight RLS is FORCEd, and the `highlight_rules` policy lets any table-owner definer function called from an app or panel session see every row (`Phase-1-Amendments.md` §4 item 1, lines 260–265). That policy is why this check exists: a new definer function or owner-owned view that names `highlight` would read every user's highlights
- **Updated 2026-11-10 (`docs/reviews/2026-11-10-rules-supervisor-carriage.md` V7):** `Phase-1-Amendments.md` §16.2 adds `dismiss_highlight()`, which names `highlight`, and says it "joins §4 item 1's list"; §4 item 1 (`:336`) and this check's set were not changed. The set becomes {`capture`, `start_highlight`, `highlight_open`, `highlight_rows`, `dismiss_highlight`} only once §4 item 1 lists it; until then the scan fails. `highlight_dismissal` is held to the same scan (R-209)

### R-157
- **Statement:** Nobody can tell from the database's own bookkeeping that anyone captured, started a highlight, reflected, tagged or committed in content they cannot read. No statistic, row estimate, table size, transaction or WAL counter, lock, session list or other database changes in a way they can see.
- **Type:** auto · **Applies to:** data
- **Source:** FS §20 MM (`FS:317`), OO (`FS:319`), RR (`FS:322`); R-006 ("a response whose size grows with the count"), R-010. Proposed by `Phase-1-Amendments.md` §10 checks 1–4 (lines 638–643) and §11 check 4 (line 721). Numbered by r6
- **How to check:** (1) The differential catalog test of `Phase-1-Amendments.md` §10 check 1, with targets extended to every user-content table and its primary key (§11 check 4). Run it as the viewer role, then as the panel role both directly and after its switch to the viewer role. Only the fixed allow-list of clock and random functions may differ. (2) The named refusals of §10 check 2. (3) After reset, the working database's ACL grants CONNECT to the two product roles only, and neither role can connect to any other database. (4) No statistics extension is installed or preloaded (§10 (d)). (5) `EXPLAIN` on every reader shows the same fixed estimate before and after the activity in (1).
- **Accepted residual (FS §20 RR, `FS:322`):** the time a read takes may still depend slightly on rows the viewer cannot read. This is accepted for the prototype on dummy data and must be revisited before any real user's data enters the system. A reader that scans a whole table and then filters is not covered by the residual, and it fails R-158
- **Current implementation:** the product roles hold no table privilege; the cluster superuser closes the catalog; the one-database CONNECT grant is re-applied after every clone (`Phase-1-Amendments.md` §10, §2.3; `P1:48` (h), `P1:179`)

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** friendship acts are activity too. The differential catalog test gains the six friendship tables as targets, and a send, an answer, a decline, a withdrawal, a removal and a close-friend entry and exit between two other users as the watched activity (`Phase-1-Amendments.md` §12.7 K11)
### R-158
- **Statement:** Every read of user content goes through a reader that returns exactly what that content's read rule allows. Beyond the accepted timing residual, it says nothing about the size, shape or timing of what it holds back. No product role reads or writes a user-content table directly.
- **Type:** auto · **Applies to:** data
- **Source:** FS §20 OO (`FS:319`), MM, RR. Proposed by `Phase-1-Amendments.md` §11 checks 1–3 (lines 716–720). Numbered by r6
- **How to check:** (1) The viewer role, the panel role and PUBLIC hold no table or column privilege on any table in the product schema, except SELECT on `journey_type`, `chapter` and `prototype_option`. A new table fails until it is listed there or given a reader. (2) Every set-returning function the viewer role may execute is a definer function with a fixed row estimate. With sequential scans disabled, the plan of its body has no sequential scan on any user-content table other than `user`. (3) For each fixture viewer, at several clock points and under every setting of `b2` and `c6`, each reader returns exactly the rows its read rule allows. The read rule is checked against this rubric and the provisional defaults, not only against the table's policy: an equivalence test against a wrong policy still passes (r6 V3, B10). (4) Every write goes through a definer function whose body carries the check its insert policy carried. The refusal cases of R-026, R-046, R-052, R-057 and R-122 are run through those functions (R-164).
- **Current implementation:** `Phase-1-Amendments.md` §11 (one reader per table, `ROWS 1000`, journey first), `P1:44–45`, `P1:48` (h)

### R-199
- **Statement:** No writer accepts anything on a photo, note or highlight of a journey that has not unlocked, whatever date arithmetic of its own says. Each writer that reads sealed rows as a definer refuses before `unlocks_at` by its own explicit test, and its answer before unlock is the same for an existing and a non-existent id.
- **Type:** auto · **Applies to:** data, API
- **Area:** 1. Sealing and leaks
- **Source:** CL "Sealed content is unreadable"; P1:48, P1:117; FS §20 VVVV; `Phase-1-Amendments.md` §16.1. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V2 (`add_reflection()` lost the unlock guard the old D9 arithmetic gave it; "c + 1 year ≥ unlocks_at" is false for a Commit not at 00:00 UTC, since `unlocks_at` keeps the Commit's time of day, P1:73–74)
- **How to check:** In a throwaway copy, Commit at 14:37:00 UTC on day d, capture a photo at 15:00 the same day, jump to d + 1 year 00:00:00 and to 14:36:59: `add_reflection()` on that photo is refused at both, with the same answer as for a random uuid; at 14:37:00 it is accepted (slot 1). Repeat for every definer writer that takes a photo, note or highlight id. Code scan: each such writer names `unlocks_at` (or the seal predicate) itself.

### R-201
- **Statement:** A provisional default or screen rule written for "nothing this reader can see", "no photo yet" or "an empty journey" never applies to a sealed journey. A sealed journey reaches anyone but its owner as "exists" only (R-008), whatever such a rule says, and reaches the owner as B19 allows.
- **Type:** review, then auto · **Applies to:** UI, data, copy
- **Area:** 1. Sealing and leaks
- **Source:** R-008, FS §20 I (`FS:279`), FS §20 T, CL:106. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V1 (B74, `Decisions-Needed.md:109`, `Flows.md:626`: "to a friend it shows as a place with its type and dates only", with no exception for a sealed journey)
- **How to check:** For every default or SI/Flows row that conditions on visible content, read whether a sealed journey meets its condition; if it does, the row must except it in words. UI test: as Second Wind (Lantern's friend) at baseline, render Lantern's path: Lantern #6 (sealed) shows existence only, no type and no date. As First Light, the same journey shows the same existence line, not nothing, unless FS §20 I is changed.

---

## 2. Immutability and append-only

### R-015
- **Statement:** Nobody, the owner and the app's own role included, can change or delete a reflection once it is written.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:65, CL:80, MP:38, FS:99, FS:229, P1:44. **= §2.5 check 1**
- **How to check:** As the app role, run UPDATE, DELETE and TRUNCATE on the reflection store: each raises. Confirm no API route accepts an edit or delete of a reflection.
- **Current implementation:** INSERT and SELECT grants only, plus a trigger that raises on UPDATE, DELETE and TRUNCATE (P1:44).
- **Updated 2026-10-31 (FS §20 OO; R-164):** the viewer role now holds no privilege on the reflection table, so its UPDATE, DELETE and TRUNCATE fail on privilege before the trigger runs. Run them also as the table's owning role: the append-only trigger must raise its own error

### R-016
- **Statement:** No screen offers to edit, delete, undo or replace a saved reflection.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:65, FS:99
- **How to check:** UI test on a photo with five reflections (lantern-1): no edit, delete or undo control on any of them. Grep reflection components for `edit`, `delete`, `remove`, `undo`, `contenteditable` on saved text.

### R-017
- **Statement:** Nobody can change or delete a journey overview once it is written.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** CL:80, FS:120, P1:23 (D10), P1:44. **= §2.5 check 1**
- **How to check:** As R-015 and R-016, on the overview store and overview screens.

### R-018
- **Statement:** A photo can never be deleted or replaced, by anyone.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:266 (§20 mechanics 6), P1:20 (D7), P1:45, CL:99. **= §2.5 check 1**
- **How to check:** UPDATE, DELETE and TRUNCATE on photo rows and their images raise. No API route deletes a photo or swaps its image.
- **Updated 2026-10-31 (FS §20 OO; R-164):** run the UPDATE, DELETE and TRUNCATE also as the table's owning role; the trigger, not a missing privilege, must raise

### R-019
- **Statement:** No screen offers to delete, remove or replace a photo.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** FS:266, CL:99
- **How to check:** UI test on owner views of revealed journeys: no delete, remove, trash or replace control. Grep for `delete`, `remove`, `trash`, `bin`, `replace` near photo components.

### R-020
- **Statement:** A handwritten note cannot be changed or deleted once added.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:16 ("written once"), P1:45, P1:108. **= §2.5 check 1**
- **How to check:** As R-015, on the note store. No UI control re-takes or removes a note.

### R-021
- **Statement:** Once Commit is pressed, the journey's type, commit date and unlock date can never change.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:44, CL:87, MP:55, P1:76. **= §2.5 check 1**
- **How to check:** UPDATE and DELETE on journey rows raise. No route or screen changes a journey's type.
- **Updated 2026-10-31 (FS §20 OO; R-164):** run the UPDATE and DELETE also as the table's owning role; the trigger, not a missing privilege, must raise

### R-022
- **Statement:** A user's name is chosen once and never changes.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:268 (§20 mechanics 8), P1:32 (D19), P1:61. **= §2.5 check 1**
- **How to check:** UPDATE on the user name raises. No settings screen offers a rename.
- **Updated 2026-10-31 (FS §20 OO; R-164):** run the UPDATE also as the table's owning role; the trigger, not a missing privilege, must raise

### R-023
- **Statement:** A finished reveal cannot be un-finished or re-opened.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:164, FS:151. **= §2.5 check 1**
- **How to check:** UPDATE and DELETE on the reveal-finished record raise. No route re-opens a reveal.
- **Updated 2026-10-31 (FS §20 OO; R-164):** run the UPDATE and DELETE also as the table's owning role; the trigger, not a missing privilege, must raise

---

## 3. Capture and cadence

Commit, capture, frames, highlights and the note.

### R-024
- **Statement:** The Commit screen pre-selects no journey type.
- **Type:** auto · **Applies to:** UI
- **Source:** FS:46
- **How to check:** UI test: on first render, none of Explorer, Wanderer or Contemplator is selected, checked or highlighted as a default.

### R-025
- **Statement:** Commit is accepted on any calendar day.
- **Type:** auto · **Applies to:** API
- **Source:** FS:36, FS:273 (§20 C), P1:15 (D2)
- **How to check:** As First Light, commit at the 1st, 15th, 28th, 29th, 30th and 31st of various months (resetting between runs). Each accepted. See G-18 for month-end dates.
- **Provisional default:** Decisions-Needed B16: A commit on the 29th–31st uses the last day of shorter months; one time zone for the prototype (UTC). Add 29 February to the dates tried: accepted. A "day" is a UTC day

### R-026
- **Statement:** A second Commit while the user has a sealed journey is refused.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:273 (§20 C), P1:16 (D3), CL:87. **= §2.5 check 3**
- **How to check:** As Steady Lantern at baseline, call Commit: refused. Also try inserting a second journey directly as the app role: raises.
- **Current implementation:** exclusion constraint on overlapping `[committed_at, unlocks_at)` per user (P1:47).
- **Updated 2026-10-31 (FS §20 OO; R-164):** a direct insert by the viewer role is now refused for lack of privilege, which no longer tests the one-journey rule. Call `commit()` as Lantern (refused), and insert an overlapping journey as the table's owning role (the exclusion constraint raises)

### R-027
- **Statement:** Once the current journey has unlocked, the next Commit is accepted, whether or not that journey's reveal is finished.
- **Type:** auto · **Applies to:** API
- **Source:** FS:273, P1:16 (D3), P1:210 (Long Way Round between journeys)
- **How to check:** As Long Way Round at baseline (#4 unlocked, reveal never finished), Commit: accepted. As Steady Lantern at exactly 2027-01-01 00:00:00: accepted.

### R-028
- **Statement:** A committed journey cannot be abandoned, cancelled, paused, ended early or restarted.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** FS:263 (§20 mechanics 3), P1:17 (D4), CL:87, MP:55
- **How to check:** No route or control for any of these. Grep for `abandon`, `cancel journey`, `quit`, `pause`, `end early`, `restart`, `start over` in routes and copy.

### R-029
- **Statement:** A photo can only be taken live in the app, at the moment. No existing image can be imported from a gallery, camera roll, file or drag-and-drop.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:53, MP:67, CL:99
- **How to check:** Grep the client for `<input type="file"`, `showOpenFilePicker`, `ondrop`/`dragover` handlers and gallery pickers on any capture path. Capture must use the live camera stream. Note: a file input with `capture` opens the phone's own camera, which offers its own Retake and may offer the gallery, so it fails R-029 and R-031.

### R-030
- **Statement:** Capture is three taps and asks for nothing: no tags, no text, no caption, no visibility, no filter, crop or other choice.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:54, MP:67, CL:99
- **How to check:** The capture API accepts the image and nothing else (send extra fields: rejected or ignored, never stored). UI test: from opening capture to the photo being sealed takes at most three taps, with no input field or option on the way.

### R-031
- **Statement:** There are no retakes. Once the shutter is pressed the photo is final: no retake, no "use photo or retake" step, no undo, no discard.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** CL:64, MP:37, FS:55, FS:228
- **How to check:** UI test: after the shutter tap, no control returns to the viewfinder for the same frame. Grep for `retake`, `re-take`, `try again`, `redo`, `discard`, `undo`, `use photo`. No API route replaces a photo (R-018).
- **Decided 2026-10-30 and 2026-10-31 (FS §20 PP, `FS:320`; VV, `FS:326`):** a metadata refusal never reaches the user, and the app's single automatic re-save of the same press is not a retake. Covered by R-160

### R-032
- **Statement:** Capture never refuses or warns because of image quality: blur, darkness, composition or framing.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** FS:56
- **How to check:** List every refusal reason in the capture path. The only reasons allowed are no sealed journey, the frame limit, and the highlight cap. Grep for `blur`, `too dark`, `low light`, `quality`, `out of focus`.

### R-033
- **Statement:** Capture takes still photos only: no video and no moving image.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:57, MP:67, CL:99
- **How to check:** Capture rejects any non-still-image media type. Grep the client for `MediaRecorder`, `video/` uploads and `capture="camcorder"`.

### R-034
- **Statement:** A photo is sealed into the journey the moment it is taken. There is no later step that decides whether it is included.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:58, CL:99
- **How to check:** Capture either seals the photo into the journey in one call or refuses. No "add to journey", draft or pending state exists in the data or the UI.

### R-035
- **Statement:** Capture works only while the user has a sealed journey. Before Commit and after unlock it is refused.
- **Type:** auto · **Applies to:** API
- **Source:** P1:99, FS:73
- **How to check:** As First Light (no journey): refused. As Long Way Round (#4 unlocked): refused. As Lantern at 2027-01-01 00:00:00: refused.

### R-036
- **Statement:** A normal photo is accepted only while the journey's normal photos so far are below the type's monthly cadence times the current month of the journey, so unused frames carry forward.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261–262 (§20 mechanics 1–2), P1:18 (D5), P1:97, CL:95
- **How to check:** For each type, fill month 1 to cadence and try one more: refused. Skip month 1 and in month 2 take two months' worth: all accepted (Wanderer: 4). Replay Lantern #3's 0 in March and 4 in April.

### R-037
- **Statement:** Frames unused when a journey ends are gone. Nothing carries into the next journey.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261, P1:18 (D5), CL:95
- **How to check:** End a journey with frames unused, Commit the next, and in its month 1 take cadence + 1 photos: the last is refused.

### R-038
- **Statement:** Capturing a photo and starting a highlight answer only "accepted" or "refused". They never return a number: not frames used, frames left, highlights left or photos so far.
- **Type:** auto · **Applies to:** API
- **Source:** P1:49, FS:243, CL:69. **= §2.5 check 5**
- **How to check:** Inspect the response schema of both calls. Any numeric field, or any string containing a digit that reports a count, fails.
- **Provisional default:** Decisions-Needed B7: Frames left are never shown; a refused capture says so with no number (copy in Phase 2). Holds as written. The refusal may say that it was refused; it may not say how many, how long until the next frame, or which month the next frame opens

### R-039
- **Statement:** The number of frames used, frames left and highlights left is never stored. It is worked out at the moment of capture and discarded.
- **Type:** auto · **Applies to:** data
- **Source:** P1:49. See G-6
- **How to check:** Schema scan for columns or cache keys named like `frames_used`, `frames_left`, `remaining`, `highlights_used`, `highlights_left`, `photo_count`, `quota_left`.

### R-040
- **Statement:** A highlight starts only when the user starts it, and lasts 24 hours or until the journey unlocks, whichever is first.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:264 (§20 mechanics 4), P1:19 (D6), P1:133, CL:97
- **How to check:** No job or rule starts a highlight. Start one and capture at +23:59 (accepted as highlight) and +24:01 (treated as normal frame or refused). Start one 2 hours before unlock: it ends at unlock.
- **Provisional default:** Decisions-Needed B16: A highlight lasts 24 hours of elapsed time; one time zone (UTC). The end is start + 86,400 seconds on the app clock, never a wall-clock "same time tomorrow"
- **Decided 2026-10-30 (FS §20 U):** a capture at +24:01 is no longer "normal frame or refused" by choice: it takes a normal frame if one is left, otherwise it is refused. Test both states
- **Provisional default:** Decisions-Needed B25: A highlight is closed at exactly its end time. Add the case: a capture at exactly start + 24:00:00.000 is not a highlight photo, and `highlight_open()` returns false at that instant

### R-041
- **Statement:** Only one highlight can be open at a time. Starting another while one is open is refused.
- **Type:** auto · **Applies to:** API
- **Source:** FS:284 (§20 N), P1:406 (R3), CL:97, MP:65
- **How to check:** Start a highlight, then start a second inside the 24 hours: refused.

### R-042
- **Statement:** A journey has at most its type's highlights (Explorer 4, Wanderer 2, Contemplator 1), and they can be used at any time in the journey, with no season rule.
- **Type:** auto · **Applies to:** API
- **Source:** FS:66, FS:264, P1:135, CL:89–93
- **How to check:** For each type, start highlights back to back up to the allowance (all in one month for Explorer): accepted. One more: refused.

### R-043
- **Statement:** A highlight holds up to the type's yearly quota (48, 24, 12), and its photos never count against the journey's normal frames.
- **Type:** auto · **Applies to:** API
- **Source:** FS:265 (§20 mechanics 5), P1:19 (D6), P1:96, CL:97
- **How to check:** Fill a Contemplator highlight to 12 (Lantern #5 shape), try a 13th: refused as a highlight photo. After the highlight, normal frames are still available at the same count as before it.
- **Decided 2026-10-30 (FS §20 U):** inside an open highlight, capture uses the highlight first; once it is full, a normal frame if one is left, otherwise refused. The 13th photo above is accepted as a normal frame when one is left and refused when none is; it is never a highlight photo. In both cases the reply is only `accepted` or `refused` (R-038)

### R-044
- **Statement:** A highlight can only be started on a sealed journey.
- **Type:** auto · **Applies to:** API
- **Source:** P1:135
- **How to check:** Start a highlight with no journey, and after unlock: both refused.

### R-045
- **Statement:** The handwritten note is an optional step offered only after the photo is already sealed. Skipping it costs nothing, and capture never waits on it.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:257 (§20 B), MP:69, CL:99
- **How to check:** The photo exists, sealed, before the note step appears. Skip the note: the photo is unchanged. The note step has a skip control on first render.
- **Provisional default:** Decisions-Needed C4: The note step is offered only inside the capture flow, straight after the photo, for up to 15 minutes. Leaving capture ends it; there is no way back from the sealed screen. Under C4 the check adds: no route, screen or control outside the capture flow opens the note step for an earlier photo, and after leaving capture the note call for that photo is refused even inside the 15 minutes

### R-046
- **Statement:** A note can be added up to 15 minutes after its photo was captured, never after.
- **Type:** auto · **Applies to:** API
- **Source:** FS:281 (§20 K), P1:21 (D8), P1:108, CL:99, MP:69
- **How to check:** On the app clock, add a note at capture + 14:59: accepted. At capture + 15:01: refused. See G-18 for exactly 15:00.
- **Provisional default:** Decisions-Needed B16: Exactly 15:00 is out. Add the case: at capture + 15:00.000 the note is refused. Also C4: leaving the capture flow ends the window early (R-045)

### R-047
- **Statement:** A photo has at most one note.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:16 ("belongs to exactly one photo, written once"), P1:104
- **How to check:** Add a second note to the same photo within the window: refused.

### R-048
- **Statement:** A note is a photograph of a handwritten page. There is no typed note.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:16, MP:69, CL:99
- **How to check:** The note API accepts an image only. The note step shows no text field or keyboard input.
- **Provisional default:** Decisions-Needed C4: The page is taken live, once, with no re-shoot. Under C4 the note photo follows R-029 and R-031 exactly as the photo does: live camera only, no gallery, file or drag-and-drop, and no retake, "use photo" step or second attempt (answers Question 3)

### R-138
- **Statement:** Whether a frame or a highlight is available is learned only by trying. No control is hidden, greyed out or relabelled because of availability, and no call other than capture and starting a highlight works it out or reports it.
- **Type:** auto · **Applies to:** API, UI
- **Status:** Provisional. Depends on G-5 and Question 5 (what a refused capture may say). If the user decides the camera is not offered when no frame is available, this check is superseded
- **Source:** P1:49 ("counted inside them and never stored or returned"), FS:243, RG:28 ("disabled-but-visible states"). Found by `docs/reviews/2026-10-27-rules-screen-inventory.md` finding 5
- **How to check:** List every route and function that reads a journey's photo or highlight rows: only capture and start-highlight may compute frames or highlights available. UI test as Steady Lantern on Lantern #6, once with a normal frame available and once with none, and once with highlights unused and once with all used: the sealed-year, capture and start-highlight screens render the same DOM before any tap.
- **Provisional default:** Decisions-Needed B7: Frames left are never shown; a refused capture says so with no number (copy in Phase 2). Firm under B7: the camera is always offered and availability is learned only by trying. The supersede condition above does not arise while B7 is in force
- **Provisional default:** Decisions-Needed B6: The owner sees only "a highlight is open", with no end time and no countdown. Under B6 the one allowed DOM difference is that plain "a highlight is open" state while one is open. Highlights unused and highlights all used must still render the same DOM, and the start-highlight control is not hidden, greyed or relabelled while one is open; a second start is refused on tap (R-041)
- **Accepted residual (FS §20 SSS, `FS:355`; Before real users item 7):** since FS §20 QQQ, code that holds a product connection can call `capture()` with an image that fails the guard and learn whether a press would be accepted without using a frame (`Phase-1-Amendments.md` OQ-36 (b)). The device cannot reach it, because the server strips every image. This check's "no call other than capture" still holds: the probe is `capture()` itself. Revisit with OQ-12
- **Updated 2026-11-10 (FS §20 WWWW; `PROVISIONAL: B76`):** S-13's dismiss way is present and identical for the whole open highlight; its refusal after 3 hours and after a photo is the same words, with no time or number
- **Updated 2026-11-10 (`docs/reviews/2026-11-10-rules-supervisor-carriage.md` V7):** "no call other than capture and starting a highlight" now also meets `dismiss_highlight()` (§16.2), which reads the sealed journey's highlight row and photo rows and answers on whether a photo is in the highlight, and the new `highlight_dismissal` table read by `capture()`, `start_highlight()` and `highlight_open()`. Until the docs name it here and in R-156 (R-209), this check fails as written for §16.2

### R-159
- **Statement:** No stored image, photo or note, carries a time or a place inside its file, for anyone, the owner included. An image that would carry one is never stored.
- **Type:** auto · **Applies to:** data
- **Source:** FS §20 KK (`FS:315`), NN (`FS:318`), QQ (`FS:321`); FS §20 GG; R-154, R-004. Proposed by `Phase-1-Amendments.md` §6 (line 446). Numbered by r6
- **How to check:** Use the §6 sample set, generated with a fixed seed. A clean baseline JPEG is accepted by `capture()` and by the note step. Both refuse every other sample, storing no row and using no frame or highlight place: EXIF (date or GPS only), XMP, IPTC, ICC, COM, bytes after EOI, progressive, SOF1 or 12-bit frames, PNG (clean or with text, time or EXIF chunks), WebP and HEIC. Every fixture placeholder passes. After unlock, decrypt every fixture image and confirm it holds only the allowed baseline JPEG segments. The other half of PP is R-160.
- **Current implementation:** before encryption, the strip step re-encodes the image to baseline JPEG, and `image_metadata_free()` runs as the first step of `capture()` and of the note step (`Phase-1-Amendments.md` §6; `P1:91`, `P1:105`, `P1:180`)
- **Updated 2026-10-31 (r9; FS §20 QQQ, `FS:352`):** the line above held until QQQ. `capture()` now judges the press first (the §20 U steps 1–5) and runs `image_metadata_free()` only on a press judged accepted, still before encryption and the insert; the note step still runs it first (`Phase-1-Amendments.md` §6 lines 515 and 523; `P1:91`). The sample check therefore runs `capture()` as the owner of a sealed journey with a frame left; a press judged refused is answered `refused` whatever its image, and that is R-160's QQQ case, not a pass of this check

### R-160
- **Statement:** One shutter press is one photo. A metadata refusal never reaches the user: no error, no "try again", nothing that invites a second press. If the guard refuses anyway, the app strips the same image again and saves it once, with no action from the user and no visible difference.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** FS §20 PP (`FS:320`), VV (`FS:326`); CL:64 (no retakes); R-031, R-005. Found by r6 V4 (`Phase-1-Amendments.md:445` still calls the case "not settled")
- **How to check:** (1) Build: every decodable §6 sample, after the strip step, is accepted by `capture()` and by the note step, so the bug cannot be reached with any sample (PP). (2) UI test with the strip step forced to emit a refused image on its first pass. One press stores exactly one photo (read through the owner's reader after unlock, or by the test as the table owner). No refusal copy appears. No control returns to the viewfinder for that frame. The camera after the press is identical to an ordinary accepted press. (3) With the strip step forced to fail twice: still at most one row, and no prompt to the user. Grep aid: retry loops around `capture(` in the client, and user-facing error strings on the capture path.
- **Open (raised by r6, not decided here):** the re-save is a second `capture()` call at a later instant. If the highlight closes, the month's frames lapse or the journey unlocks between the two calls, the re-save is refused or lands as a normal frame. "One press is still one photo" cannot hold as worded in that case. This goes to the supervisor
- **Decided 2026-10-31 (FS §20 XX, AAA, `FS:331`, `FS:334`); closes the `Open` note above:** the retry runs inside the press's own transaction, so it is judged and stamped at the press instant. If the highlight closes, the month turns or the journey unlocks while the retry runs, the press still lands where it would have landed, and the stored `captured_at` is the press instant (`Phase-1-Amendments.md` §6, lines 473–479, evidence 526–539 and 545–547). The `Open` note stays as history
- **Decided 2026-10-31 (FS §20 DDD, GGG, `FS:337`, `FS:340`), for (3):** if the second strip also fails, the press gives no photo, no frame or highlight place is used, nothing is shown, there is no third call, and the bug is logged (R-167). The camera returns as after any press, with no note offer. "No visible difference" in the statement is read against GGG: see G-24
- **Decided 2026-10-31 (FS §20 HHH, `FS:341`):** the note step retries the same way: strip again and save once at the note press's instant; on a second refusal nothing is stored, nothing is shown, and the bug is logged
- **Updated 2026-10-31 (r7):** (3) now reads: with the strip step forced to fail twice, zero new photos, no prompt, no copy, no S-12 offer, the frame and highlight counts unchanged (a later capture is accepted exactly as if the press never happened), and two refusal lines with one transaction id in the server log. Added (4), the note step: with its strip step forced to fail once, exactly one note, `written_at` equal to the note press's `app_now()`, even when the 15-minute window closes during the retry; forced to fail twice, no note row, nothing shown, the step ends as after a page taken, and no route offers the note step again for that photo (C4, R-020). The DB-level half of (4) runs in Phase 3 with the §6 sample set; the screen half in Phase 4
- **Decided 2026-10-31 (FS §20 JJJ, `FS:343`); supersedes the GGG line above and the "no S-12 offer" in (3):** after a lost press the screen looks exactly like a normal press, note offer included; GGG's "no note offer" is retired. (3) now reads: zero new photos, no prompt, no copy, **the S-12 offer shown exactly as after a saved press**, the frame and highlight counts unchanged, and two refusal lines with one transaction id. A note written for a lost press stores nothing, attaches to no other photo (a planted "latest photo without a note" route must be caught) and is answered exactly as a saved note (R-170). The two lines above are history
- **Decided 2026-10-31 (FS §20 III, MMM, `FS:342`, `FS:346`), for (4):** a note lost twice ends the note step as after a page taken, and nothing offers it again. The database stores nothing about a lost note, so (4)'s "no route offers the note step again" is a route test only (Phase 4); the database accepting a later note-step call is an accepted residual, with OQ-12
- **Decided 2026-10-31 (FS §20 LLL, NNN, `FS:345`, `FS:347`):** the note step finds its photo through a server-side handle the device never holds (R-169). After a lost press the note step closes 15 minutes after the press, as after a photo: at press + 14:59 and + 15:00.000 the lost press's note gets the same answer as a photo's
- **Decided 2026-10-31 (FS §20 PPP, `FS:350`):** handles lost on a server restart end that note step early, and nothing wrong is stored. Accepted for the local prototype, with OQ-12. What the screen shows then is R-171
- **Decided 2026-10-31 (FS §20 QQQ, `FS:352`), for (3):** a lost press looks like the normal press it would have been, judged first at the press instant. (3) is run in each of the six `Phase-1-Amendments.md` §6 QQQ states against a rolled-back normal press at the same instant: where that press is refused, the lost press gets the normal refusal, byte-identical, no log line and no note offer; where it is accepted, the S-12 offer as in the JJJ line above. A `capture()` with the guard first must be caught
- **Decided 2026-10-31 (FS §20 RRR, UUU, VVV, WWW, `FS:353`, `FS:357`–`FS:359`), for (4) and the note step:** a note press answered "closed" looks exactly as when the window has ended; when the window ends while the user is on the step, nothing on screen changes on its own and the next note press is simply not taken; a saved page shows no confirmation; skipping ends the step for good. A UI test of S-12 must find no confirmation after a saved page, no change at press + 15:00 while idle, and no way back after a skip
- **Accepted residual (FS §20 SSS, `FS:355`):** a strip fault on a press judged refused is neither detected nor logged, and the server log holds refusal lines only for presses judged accepted (`Phase-1-Amendments.md` OQ-36 (a), (c)). Before real users, item 7
- **Decided 2026-10-31 (FS §20 ZZZ, `FS:362`), for (4):** a note lost twice gets the same answer as a saved note, byte for byte. (4) gains: the device response to a note lost twice is compared with a saved note's, status line, headers and body, and must be identical (`Phase-1-Amendments.md:577`; planted fault (h))

### R-167
- **Statement:** When a captured image or a note image is lost to the guard bug, the record of it carries nothing about the user: no image, no user, journey or photo id, no app time and no statement text. No product role can read it, and it never enters the product data.
- **Type:** auto · **Applies to:** data, dependencies
- **Source:** FS §20 DDD (`FS:337`), FFF (`FS:339`), HHH (`FS:341`); CL:73 (nothing leaks); R-160, R-155. Proposed by `Phase-1-Amendments.md` §6 "What the build runs" (line 487). Numbered by r7
- **How to check:** In one press, force the strip step to fail twice, with a fixed marker byte sequence in the image sent as a bind parameter. The server log then holds exactly two refusal lines with one transaction id (one line for a press saved by the retry), no `STATEMENT` line, the marker nowhere in hex or text, and no uuid in the refusal lines. Repeat for the note step. As the viewer role and the panel role, natively and after the role switch: the file-reading and log-listing functions, server-side large-object import and `COPY … FROM` a file are refused, neither role is a member of the file-reading or monitoring roles, and setting `log_min_error_statement` is refused. No table, view or reader in the product schema holds log content.
- **Accepted residual (FS §20 FFF):** `log_parameter_max_length_on_error` is user-settable, so code that holds a product connection can write its own image into the log (Phase-1-Amendments OQ-31 (a)). Accepted with OQ-12 until real authentication; it must be revisited before any deploy
- **Current implementation:** role settings and `%v` in `log_line_prefix`, set by the cluster script (`Phase-1-Amendments.md` §6, lines 482–484, evidence 541–570)
- **Updated 2026-10-31 (r8):** this check covers the database server's log only. The route's own logs, traces and error output are R-169's, since under FS §20 LLL the route holds a sealed photo's id and its press instant

### R-169
- **Statement:** Nothing that ties a press to its sealed photo leaves the server route. The device never receives the note handle or any photo id, no log, trace, store or response holds it, it serves one note transaction, and it is gone once that transaction ends or 15 minutes after the press, whichever comes first.
- **Type:** auto (responses, logs, planted faults) and review (route code) · **Applies to:** API, data, dependencies
- **Source:** FS §20 LLL (`FS:345`), MMM (`FS:346`), NNN (`FS:347`), PPP (`FS:350`); CL:73 (nothing leaks); P1:48 (a), P1:49, P1:108; R-002, R-010, R-167. Found by r8 (N4; V1: `Screen-Inventory.md:345` still has S-12 read "Photo (id only)")
- **How to check:** (1) Run the capture and note flows (saved, retried, lost press, lost note, closed window) and scan every byte the device receives, status lines and headers included, for a uuid: none. (2) In the same run, scan the route's stdout, stderr, access log, error output and any trace for each handle value and for each press instant at sub-second precision: none. (3) No table, file, cache, cookie or client storage holds a handle; after a note transaction ends, and after press + 15:00.000 on the app clock, the route holds no entry for that press. (4) The `Phase-1-Amendments.md` §6 planted faults are caught: handle in the press response, entry kept after a lost note, no window check for a lost press, a session-level handle. Add: a route that logs the handle is caught by (2). (5) Review: no screen spec or client code reads a photo id during the sealed year.
- **Current implementation:** `capture()` sets the transaction-local `mj.note_handle`; the route keeps it in process memory keyed by device session and acting user; `add_note(handle uuid, img bytea)` (`Phase-1-Amendments.md` §6 lines 526–532, evidence 653–682; `P1:49`, `P1:105`, `P1:108`, `P1:180`)
- **Accepted residual (FS §20 MMM, PPP):** code holding a product connection and a handle can call the note step again inside the 15 minutes, and a restart drops every handle. Both are revisited before real users, with OQ-12
- **Updated 2026-10-31 (r10; FS §20 YYY):** the route's entry now also holds the id of the journey the press was into (`Phase-1-Amendments.md:562`). A sealed journey's id beside a real time records that its owner pressed then (`Phase-1-Amendments.md:946`, FFF). (2) also scans every route output for each journey id in the run, in any form: none. "What the route writes" (`:563`) must list the journey id with the handle, the press instant and the user id

### R-170
- **Statement:** A press lost to the guard bug, and a note written after it, cannot be told apart by the user from a saved press and a saved note: the device gets the same answers, the screen goes to the same next state, and nothing on screen depends on a difference in how the server handled them.
- **Type:** auto (responses) and review (UI timing) · **Applies to:** API, UI
- **Source:** FS §20 DDD (`FS:337`), JJJ (`FS:343`), NNN (`FS:347`), PP (`FS:320`); CL:64 (no retakes: a visible difference invites a second press); R-160, R-168. Found by r8 (N3)
- **How to check:** (1) For paired cases (saved press and lost press; their notes at + 1 minute, + 14:59 and + 15:00.000), compare the full device responses, status, headers other than `Date`, and body: identical. (2) UI test of S-02 and S-12 with the strip step forced to fail twice: the same sequence of screen states as a saved press, the same note offer, the same end. (3) Review: no S-12 transition, indicator or end waits on the server's note answer in a way that would end the step sooner after a lost press, which does no strip, seal or write (`Phase-1-Amendments.md` §6 line 517).
- **Open:** a lost press that would have been refused (no frame left, highlight full) is answered `accepted` (`Phase-1-Amendments.md` §6 lines 516, 529). Whether "a normal press" there means an accepted one or the refusal it would have given is G-25
- **Decided 2026-10-31 (FS §20 QQQ, `FS:352`); closes the `Open` note above and G-25:** "a normal press" is the press it would have been. A lost press is judged at the press instant before the guard reads its image; where a normal press would be refused it is answered `refused`, where accepted it is answered `accepted` with the note offer. (1) gains the six QQQ states, each compared with a rolled-back normal press at the same instant. The `Open` note stays as history
- **Updated 2026-10-31 (r9):** (3)'s "which does no strip, seal or write" held until r8 N3 was carried. A lost press's note now strips its page and runs the same route shape as a saved note (`Phase-1-Amendments.md` §6 line 554); what remains is the note step's own database work, about 5 ms at the median (line 555). (3) now reads: no S-12 transition, indicator or end waits on the note answer in a way that would show that gap. Added (4): the same review for the **press**. A lost press strips and walks the guard twice and stores nothing; a saved press strips once, encrypts and inserts; a press saved by the retry strips twice and inserts. No S-02 transition into S-12 waits on the press answer in a way that shows the difference. The press timing is not measured in any evidence yet
- **Accepted residual (FS §20 TTT, `FS:356`):** the note-save timing gap (about 5 ms) is accepted for the prototype; Before real users, item 8 (`Phase-1-Amendments.md` OQ-37)
- **Decided 2026-10-31 (FS §20 YYY, ZZZ, `FS:361`, `FS:362`):** (1) gains the unlock edge (a photo and a lost press at U − 5:00, note presses at U − 1:00, U + 0:00.000 and U + 1:00: identical answers per instant) and a note lost twice answered byte for byte as a saved note. A press at or after unlock, normal or lost, is `refused` with no entry
- **Accepted residual (FS §20 AAAA, `FS:363`):** the extra strip after a guard refusal makes a lost press 16.7 ms and a press saved by the retry 21.1 ms slower than a saved press at the median, and a note lost twice 10.8 ms and a note saved by the retry 14.4 ms slower than a saved note (`Phase-1-Amendments.md:578–600`). Before real users, item 9
- **Updated 2026-10-31 (r10):** since AAAA, (4) is what keeps the accepted gap off the screen. (4) now also reads: no busy, wait or "saving" indicator on any press or note press that appears only after a delay, or only when the answer is slow. A delayed indicator turns a 17–21 ms gap into something the user sees on exactly the presses that met the bug. An indicator shown identically on every press, from the press, is not this failure. UI test: with the strip step forced to fail once and twice, the S-02 and S-12 frames from press to next state match a saved press's

### R-173
- **Statement:** A note step that has ended on screen has ended at the server. After a skip, leaving capture, a page taken or a page lost twice, no later note press for that press is taken, whatever the device sends, inside the 15 minutes or after.
- **Type:** auto (route test) and review (client) · **Applies to:** API, UI
- **Source:** FS §20 WWW (`FS:359`: "no note can be added later in the 15 minutes"), III (`FS:342`), K (`FS:281`); CL:78–83 (enforce rules in code, not by convention); `PROVISIONAL: C4`; R-020, R-169. Found by r9 (N2): `Phase-1-Amendments.md:552` drops the entry "when the route learns that the user skipped or left capture", but no line says how it learns, and S-12 (`Screen-Inventory.md:348`) sends only the page
- **How to check:** (1) Route test on the stopped clock: a photo; the device's skip; a note press at press + 1 minute, sent directly to the route → `closed`, no note step called, no note row. The same after leaving capture, after a page taken, and after a page lost twice. (2) Review: the device's skip and its leaving capture each reach the route as a request before the camera returns, and the route drops the entry on it; or another server-side mechanism that holds WWW is named. A skip held only by the screen fails. (3) The skip request's answer is the same for a photo and a lost press (R-170).
- **Accepted residual (FS §20 BBBB (a), `FS:364`):** a client that never sends the skip request can have a note taken inside the 15 minutes; accepted with OQ-12 until real users (Before real users item 10). (2) still applies to the product's own client: S-12 sends the request on every trigger the server design names (R-175)

### R-175
- **Statement:** A client act that a server rule depends on is stated on the screen that performs it, for every trigger the server design names. No server rule is held by a request the screen inventory never asks the client to send.
- **Type:** review · **Applies to:** UI, API, docs
- **Source:** CL:78–83 (enforce rules in code); CL:17–24 (rule zero: a builder never picks); FS §20 WWW, BBBB; `PROVISIONAL: C4`; R-165 (4), R-173 (2). Found by r10 (V1): `Phase-1-Amendments.md:566` has S-12 send the skip request when the user skips **and** when it leaves capture; S-12 end (3) (`Screen-Inventory.md:340`) and Reads (`:348`) send it on skip only
- **How to check:** For each request the route design receives from the device (`Phase-1-Amendments.md` §6: press, note press, skip request), list every trigger the design names. Each trigger appears on the sending screen's row in `Screen-Inventory.md`, with the request named. A trigger in one doc and not the other fails until the two owners agree it or the user rules. Phase 4: the client sends the request on each listed trigger (UI test)

### R-205
- **Statement:** A started highlight can be dismissed only by its owner, only while it is open, before `started_at` + 3 hours and before any photo has gone into it; a dismissal gives it back to the allowance and closes it at once. The dismiss call answers accepted or refused only, with one refusal for every cause. No reader returns a dismissal, its time or a count of dismissals, to anyone, the owner included; the dismiss way on S-13 is present and identical for the whole open highlight.
- **Type:** auto (data, API), review (UI) · **Applies to:** data, API, UI, copy
- **Area:** 3. Capture and cadence
- **Source:** FS §20 WWWW, S, AA; `PROVISIONAL: B71`, `B76`; Microcopy M-06a; `Phase-1-Amendments.md` §16.2. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V7
- **How to check:** §16.2 checks (1) to (5). Add: as Second Wind, `dismiss_highlight(Lantern #6)` refused with the same answer as a refusal at +3:00:00; render S-13 at start + 0:10, + 2:59 and + 3:01, and after one photo: identical DOM. After unlock, the owner's highlight reader either omits a dismissed highlight or shows it as the docs state; whichever, it is written down before Phase 3 (raised in V7).

---

## 4. Reveal and locking

### R-049
- **Statement:** The whole journey unlocks at once, at its unlock moment. No photo opens on its own anniversary or before the rest.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:73, FS:255 (§20 A), CL:103, MP:73
- **How to check:** At unlocks_at − 1 second every Lantern #6 photo is sealed (R-001). At unlocks_at every photo is readable to the owner. No photo's readability depends on its own capture date.

### R-050
- **Statement:** Nothing that belongs to the reveal can happen before unlock: no reflection, people tag, chapter, feeling tag, visibility choice, overview or reveal finish.
- **Type:** auto · **Applies to:** API
- **Source:** FS:82–89, FS:133 ("never at capture"), P1:164
- **How to check:** As Lantern at baseline, attempt each on Lantern #6: all refused.

### R-051
- **Statement:** Each reveal choice is set once, even before the reveal is finished. A photo's visibility, each people tag, the chapter and each feeling tag cannot be changed or removed after it is set.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:286 (§20 P), P1:408 (R5), CL:103, MP:73
- **How to check:** On Lantern #6 after unlock, set a photo's visibility, then try to change it: refused. Add a people tag, try to remove it: refused. Set the chapter, try another: refused. No UI control offers change or removal.
- **Current implementation:** these records are insert-only (P1:46).
- **Provisional default:** Decisions-Needed C5: Each set-once choice shows a one-line "this can't be changed" before it is saved. Holds as written. Under C5 that line is a statement, not a second chance: after the choice is saved there is still no change or undo control
- **Updated 2026-11-10 (FS §20 QQQQ):** the line shows once per step, never once per photo; the press that picks a choice saves it; no "are you sure" anywhere except removing a friend (B60) and blocking (B62). A line repeated per photo fails
- **Provisional default:** Decisions-Needed B3: Each reveal choice takes effect when made. Under B3 a choice set during a reveal not yet finished is live at once: a photo set to Private is readable by its owner only from that moment (R-059), not from reveal finished

### R-052
- **Statement:** Once the reveal is finished, no visibility, people tag, chapter or feeling tag can be added.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:151, FS:276 (§20 F), P1:25 (D12), P1:46, CL:103. **= §2.5 check 2**
- **How to check:** On a revealed fixture journey (Lantern #5), insert each kind: each raises.
- **Current implementation:** trigger refuses inserts once the journey's reveal-finished record exists (P1:46).
- **Updated 2026-10-31 (FS §20 OO; R-164):** insert each kind through its reveal-choice writer function (refused) and as the table's owning role (the trigger raises its own error). A permission error alone does not pass

### R-053
- **Statement:** A photo with no visibility choice is Network: once unlocked, the owner's network can read it.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:151, FS:276 (§20 F), P1:25 (D12), P1:166, CL:103
- **How to check:** As Open Hands (on Round's map) at baseline, read a Long Way Round #4 photo: allowed. As First Light: refused.
- **Provisional default:** Decisions-Needed B2 (switchable, R-142): The network can read an unlocked journey from unlock, as D12 and `P1:318` say (other setting: only after reveal finished). Holds as written under the default. Under "only after reveal finished" it reads: a photo with no visibility choice is Network, and the owner's network can read it once the reveal is finished; the Open Hands read of Long Way Round #4 (reveal never finished) is refused

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** the network is now the owner's current friends (`Phase-1-Amendments.md` §12.2). Open Hands is on Round's map but not his friend, so she is **refused** Round #4 under both B2 settings (§13.3, `P1:318`). The allowed case is now Steady Lantern, Round's friend (fr-4), who is on neither map. First Light stays refused. Under B2's option the Lantern read is refused (FS §20 R)
### R-054
- **Statement:** If the reveal is never finished, the journey still unlocks on its date, no "journey launched" goes out, and the owner's map is not recomputed.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:269 (§20 mechanics 9), P1:25 (D12), MJC:855. See G-11 for what happens to choices set during an unfinished reveal
- **How to check:** Long Way Round #4 at baseline and at +5 years: photos readable by Round, no `journey_launched` announcement for #4, Round's layer entries unchanged since #3.
- **Provisional default:** Decisions-Needed B3: Each reveal choice takes effect when made. A reveal can be finished at any later time. Under B3 the check reads: while unfinished, the journey is unlocked, no "journey launched" goes out and the map is not recomputed, but any visibility, tag or chapter already set is in force (closes G-11). Finishing in a later year is accepted, and only then do the announcement and the map recompute happen (R-087, R-080). Add the case: Round finishes #4 at baseline + 2 years: accepted, one "journey launched" at that time

### R-055
- **Statement:** The owner can write reflections any time after unlock, whether or not the reveal is finished.
- **Type:** auto · **Applies to:** API
- **Source:** P1:117
- **How to check:** As Long Way Round, write a reflection on a #4 photo: accepted (fixture: round reflected on 2026-09-10, P1:246).

### R-056
- **Statement:** A journey has at most one chapter, and it comes from the fixed catalogue under ME → ME, ME → YOU or ME → IT.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:129, P1:140
- **How to check:** A second chapter is refused. A chapter not in the catalogue is refused. The chapter UI offers catalogue entries only, no free text.

### R-057
- **Statement:** Each people tag names either a user or a name the owner typed, never both and never neither.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:267 (§20 mechanics 7), P1:26 (D13), P1:165
- **How to check:** Insert a tag with both set, and with neither: each refused.
- **Updated 2026-10-31 (FS §20 OO; R-164):** run both cases through the person-tag writer function (refused) and as the table's owning role (the constraint raises)

### R-058
- **Statement:** The overview is optional. A reveal can be finished without one.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:285 (§20 O), P1:407 (R4), CL:105
- **How to check:** Finish a reveal with no overview: accepted. The finish control is not blocked by a missing overview, reflection or tag.
- **Provisional default:** Decisions-Needed C5: Nothing is required before finishing a reveal. Under C5 the check widens: a reveal with no chapter, no feeling tag, no people tag, no visibility choice, no reflection and no overview can be finished. Nothing on the finish screen lists what is "missing" or "left to do" (R-095, R-099)

---

## 5. Visibility and access

### R-059
- **Statement:** A Private photo, and its reflections, can be read by its owner and nobody else.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:145, FS:278 (§20 H), P1:29 (D16)
- **How to check:** As every fixture user except Lantern, read a Lantern #5 private photo: refused (P1:316–320).

### R-060
- **Statement:** A Network photo can be read by its owner and by every user on the owner's map, whatever their ring, and by nobody else.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:146, P1:318 ("outer ring is still network")
- **How to check:** Lantern #5 network photo: Second Wind and Open Hands allowed, Long Way Round and First Light refused.

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** the statement now reads: a Network photo can be read by its owner and by the owner's **current friends** (people with an accepted friend request, not since removed), and by nobody else. Being on the owner's map, at any ring, grants nothing (KKKK (d)). How to check, at baseline: Lantern #5 Network photo: Wind (fr-1), Hands (fr-3) and **Long Way Round (fr-4) allowed**; First Light (fr-9 pending) refused. Plus `Phase-1-Amendments.md` §12.7 K1: `viewer_in_network()` equals the plain-SQL friendship oracle for every fixture pair at several clock points, and the old map-based body, planted, is caught (Q-F4's three map-only and friend-only pairs). The old statement is kept above as history
### R-061
- **Statement:** A Public photo can be read by any user.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:147. See G-20 for signed-out visitors
- **How to check:** Every fixture user reads a Lantern #5 public photo: allowed.
- **Provisional default:** Decisions-Needed B14: "Public" means signed-in users only. Under B14 the statement reads "any signed-in user". Add the case: a signed-out request for a Lantern #5 public photo, its reflections, and any share or direct URL to it: refused, with no image bytes in the reply (closes G-20)

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** `Phase-1-Amendments.md` §12.7 K9 states B14 for the database: with no acting user, or one that names no joined user, no photo or anything that follows one is readable, and every friendship writer returns `refused`
### R-062
- **Statement:** A reflection is readable by exactly the people who can read its photo.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:276 (§20 F), P1:24 (D11), P1:117, MP:79
- **How to check:** For each visibility level, the set of users who can read the photo equals the set who can read its reflections.

### R-063
- **Statement:** A journey overview can be read by its owner and the owner's network.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:275 (§20 E), P1:23 (D10), P1:126, CL:105. See G-19 for everyone else
- **How to check:** As Second Wind, read a Lantern overview: allowed, even where every photo of that journey is private.
- **Provisional default:** Decisions-Needed B13: The slot 1 overview can be written after the reveal is finished, within the slot. Readable by the network only. Under B13 the statement reads "by its owner and the owner's network, and nobody else". Add the case: as First Light (not on Lantern's map), read a Lantern overview of a journey with public photos: refused, and the overview does not appear beside those photos in the Positivity Feed (closes G-19)
- **Decided 2026-10-30 (FS §20 HH, `FS:312`):** under B2's "only after reveal finished" setting the network reads the overview only once the reveal is finished; under "from unlock", as written. Add the case: under "only after reveal finished", a slot 1 overview written on Long Way Round #4 (reveal never finished, in a test copy) is refused to Open Hands and readable by the owner; Lantern overviews are readable by Second Wind under both settings (R-142)

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** "the owner's network" means current friends. The FS §20 HH case changes viewer: Open Hands is refused Round #4's overview under **both** B2 settings (not Round's friend), so the viewer whose answer depends on B2 is Steady Lantern: under "from unlock", allowed; under "only after reveal finished", refused. Lantern overviews stay readable by Second Wind (fr-1) under both settings. Add the K2 case: Hands, on Round's map, reads no Round overview
### R-064
- **Statement:** Close friends see nothing beyond the rest of the network. There is no close-friends access level, list or grant.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:150, FS:278 (§20 H), P1:29 (D16), CL:107, MP:81, MJC:864. See G-3
- **How to check:** For every photo, a tight-ring member and an outer-ring member of the same owner have identical access. Schema scan for `close_friend`, `inner_circle`, `favourite` access grants.

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** KKKK (f) replaces the ring half: close friends are now **a list the owner chooses from among current friends** (`close_friend_entry`, `close_friend_exit`), shown to the owner only (`PROVISIONAL: B47`). So "no close-friends … list" in the statement above is superseded; "no close-friends access level or grant" still holds until the user rules DN E2. The statement now reads: a close friend reads exactly what any other current friend of the same owner reads, and adding or removing someone changes nothing they read. How to check: `Phase-1-Amendments.md` §12.7 K8 (Wind on Lantern's list against Hands and Round, Q-F7); the R-156-style scan on the two close-friend relations finds only their writers and `close_friend_rows()`. The `close_friend` schema-scan hit is now expected for exactly those two tables, their writers and reader. Whether the second half of FS §20 H ("see nothing beyond") is still decided is raised in the KKKK audit (V2)
- **Updated 2026-11-09, second pass (`PROVISIONAL: B48` changed to event time; `docs/reviews/2026-11-09-rules-kkkk-r2.md`):** under B48 two friends whose friendships began at different instants read different announcement rows, so "reads exactly what any other current friend reads" is compared only over what both could read: content, and announcements after the later of the two accepts. Better: in the scratch test make f1 and f2 friends of o in one panel transaction, as `Phase-1-Amendments.md` Q-F7 restricts the fixture case. The earlier line's wording stands for content
### R-065
- **Statement:** Being tagged in a photo gives no access to it. A user tagged in someone's Private photo cannot read that photo.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:293, FS:145
- **How to check:** As Second Wind, read Lantern #1's two private photos tagging Wind: refused.

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** friendship gives no access through a tag either. Add the case: Open Hands, tagged by Long Way Round in Round #1 and not his friend, reads only those of the tagged photos that are Public. `P1` §3.4 fixes none of them as Network, so the Network half of the case is untested until one is fixed (`Phase-1-Amendments.md` OQ-54, declined for now)
### R-066
- **Statement:** Tagging someone gives the tagger no access to that person's photos.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:277 (§20 G), MJC:860
- **How to check:** As Open Hands, read Lantern's network photos from a journey where Lantern did not tag Hands. Access must come only from Hands being on Lantern's map, never from Hands' own tags of Lantern.

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** "Access must come only from Hands being on Lantern's map" is superseded: Hands' access to Lantern's Network photos comes only from the friendship fr-3. The tagger case is now Long Way Round, who tagged Hands in Round #1 and is not her friend: he reads only her Public photos
### R-067
- **Statement:** Visibility is set per photo, not per journey.
- **Type:** auto · **Applies to:** data, UI
- **Source:** FS:141, MJC:379 (decided 2026-10-18)
- **How to check:** Schema: visibility is keyed by photo. Fixture journeys hold mixed levels (P1:223–242). See G-8 on "journeys set to public".
- **Provisional default:** Decisions-Needed B9 (b): Positivity Feed visibility is per photo. Holds as written, including for the Positivity Feed: no control sets a whole journey public, and the feed selects photo by photo (R-103)

### R-068
- **Statement:** The baseline access matrix holds.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:312–320
- **How to check:** Run every cell of the §3.6 matrix as a test at baseline.
- **Provisional default:** Decisions-Needed B2 (switchable, R-142): The network can read an unlocked journey from unlock (`P1:318`). The §3.6 matrix is written for this setting. Under "only after reveal finished", every network-reader cell for a Network-default photo in a journey whose reveal is not finished (Long Way Round #4) flips to refused; all other cells are unchanged. Run the matrix under both settings. How "only after reveal finished" combines with a photo set Public during an unfinished reveal (B3: choices take effect when made) is not stated in `Decisions-Needed.md`; no fixture has that case, and if one is needed it goes to the supervisor, not into the build. **Decided 2026-10-30 (FS §20 R):** under that setting a Public photo is refused too, until the reveal is finished
- **Decided 2026-10-30 (FS §20 X):** under "only after reveal finished" the network still reads the journey's type, dates, chapter and feeling tags from unlock (as FS §20 T gives); only photos, and what follows them, wait for the reveal to finish. Public readers never read those rows under either setting (R-152)

### R-152
- **Statement:** A journey's type, commit and unlock dates, chapter and feeling tags are readable after unlock by the owner and the owner's network only. A reader who is not on the owner's map, including a reader of a Public photo and a Positivity Feed reader, never sees them, on any screen or in any response.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS §20 T, FS §20 CC (feeling tag selects Positivity Feed entries but is never shown to a public reader), FS §20 Y (no chapter filter), FS §20 X (network reads these from unlock under both B2 settings), P1:48 (d), P1:84, P1:143. Found by `docs/reviews/2026-10-30-rules-phase-1-r4.md` finding V1 (`Screen-Inventory.md:201` lists chapter and feeling tags for every reader of Walking a path, public included)
- **How to check:** At baseline as First Light (on no one's map), open Lantern #2 from the Positivity Feed, then Walking a path, A photo followed forward and Another user's profile for Lantern: no type, commit date, unlock date, chapter or feeling tag in the DOM or any API response, and `journey`, `journey_chapter` and `journey_feeling_tag` return 0 rows for Lantern's journeys. `photo.journey_id` leads to nothing readable. Repeat as Second Wind (network): all are readable. Positivity Feed list endpoint: no tag, chapter or journey field in any entry. Under both B2 settings (R-142).
- **Current implementation:** RLS on the three tables with the `viewer_in_network(owner_id)` predicate (`Phase-1-Amendments.md` §5); the Positivity Feed selects by tag inside a SECURITY DEFINER function that returns reflection text only
- **Updated 2026-10-31 (FS §20 OO):** the 0 rows are read through `journey_rows()`, `journey_chapter_rows()` and `journey_feeling_tag_rows()`; the tables refuse the viewer role
- **Decided 2026-10-31 (FS §20 TT, `FS:324`):** a user's join date is readable by that user only (R-161). In the fixture each join date is the first Commit date (P1:213), so a join date shown to First Light would give Lantern #1's commit date, which this check forbids
- **Decided 2026-10-31 (FS §20 SS, `FS:323`):** whether a reveal is finished joins this list: readable by the owner and the owner's network after unlock, never public (R-162; see G-23)
- **Decided 2026-10-31 (FS §20 EEE, `FS:338`):** "never sees them" means never shown and never readable as a field. A public reader may narrow a journey's dates from capture dates and reflection dates they can already read (Phase-1-Amendments OQ-30), as ZZ allows for the reveal state. The test above is unchanged: no type, date, chapter or tag field in any response or on any screen. A screen or reader that adds a new date field for a public reader, or computes the bracket for them ("about 2025"), still fails
- **Decided 2026-10-31 (FS §20 KKK, `FS:344`):** a public reader may see the order of the journeys on a path, under EEE. The order carries no commit date, unlock date, year or date label, and no reader returns a journey date to support it. A path screen that labels journeys "2023", "Year 2" or by a date range for a public reader still fails

### R-154
- **Statement:** Anyone but the owner learns a photo's capture date, never its time of day: not on any screen, not in any response, and not through another field that pins it, such as the handwritten note's written time (at most 15 minutes after capture) or an activity graph finer than one day. The owner sees the full time.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS §20 GG (`FS:311`), `Screen-Inventory.md` OQ-45, R-151 (residual), FS §20 DD. Found by `docs/reviews/2026-10-30-rules-phase-1-r5.md` finding V3 (`Phase-1-Amendments.md:226` (iii) and `Phase-1-Proposal.md:48` (e) give every reader the full `captured_at` through `photo_read`; `Phase-1-Proposal.md:106` gives every note reader `written_at`)
- **How to check:** At baseline, as Second Wind (network) and as First Light (public), read every Lantern #1 photo and note each can read, through every read path (view, function, route): no value derived from `captured_at` carries an hour, minute or second (every photo of one UTC day returns the same value), and no note returns a time of day. Under B5's "viewer" setting, the activity data for Lantern's journeys has no bucket finer than one day. Repeat as Lantern: the full `captured_at` is returned. DOM review of Walking a path, A photo followed forward and Another user's profile as a non-owner: no hh:mm. Grep aid: `captured_at`, `written_at` in reader-side serializers and views.
- **Current implementation:** not yet specified. `photo_read` (`Phase-1-Amendments.md` §4 item 4) returns the granted `captured_at` unchanged to every reader; the owner-aware view or function pattern of item 4 is one way to give non-owners the date only
- **Decided 2026-10-30 (FS §20 LL, `FS:316`):** a non-owner gets no part of a note's written time, not even its date. "No note returns a time of day" above now reads "no note returns any part of its written time"
- **Decided 2026-10-30 (FS §20 JJ, `FS:314`):** same-day photos reach a non-owner in an order that carries no time, and ids are not sequential (R-155)
- **Updated 2026-10-31:** the implementation is now specified: `photo_captured_on()`, `photo_captured_at()` and `note_written_at()`, through read views over definer readers (`Phase-1-Amendments.md` §4 item 5, §10; `P1:48` (f), `P1:90`, `P1:106`)

### R-155
- **Statement:** No identifier and no default order tells a non-owner when anything happened. Every id is random, nothing uses a sequence or a time-ordered id, and photos from one day reach a non-owner in an order that carries no time of day.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS §20 JJ (`FS:314`); FS §20 GG, LL, T; R-154. Proposed by `Phase-1-Amendments.md` §4 item 6 (line 275). Numbered by r6
- **How to check:** (a) Schema, as the table owner: no sequence in the product schemas (`pg_sequences` outside `pg_catalog` and `information_schema` is empty); no column is an identity column or defaults to `nextval(`; no default calls a time-ordered generator (`uuidv7`, `uuid_generate_v1`, `uuid_generate_v1mc`, ULID or snowflake functions); every `id` column is `uuid`. (b) Data, after the baseline load and after the JJ case: every stored `id` in every product table is version 4 (`substr(id::text, 15, 1) = '4'`) with variant `8`–`b`. (c) Order: as First Light on Lantern's public photos and as Second Wind on Lantern #1 (19 photos on one date), read photos through every reader and route twice, and once more after a reset. The order is the same each time, and within one date it has no relation to capture time (the Amendments test: 30 + 30 interleaved captures, correlation near 0). (d) Grep reader-side code and the Positivity Feed query for `ORDER BY` on `captured_at`, a note's `written_at`, `ctid` or `xmin`. Any sort of a non-owner's photo list by those fails. The Positivity Feed's "newest first" (DN B9 (e), C14) sorts by something the reader already reads, never by `captured_at`.
- **Current implementation:** `uuid DEFAULT gen_random_uuid()` on every surrogate id; `photo_read` ends `ORDER BY photo_captured_on(id), id` (`Phase-1-Amendments.md` §4 item 6; `P1:48` (g), `P1:89`, `P1:104`). `journey.seq` (P1:71) is a per-user field, not an id
- **Decided 2026-10-31 (FS §20 BBB, `FS:335`), restating (d):** the Positivity Feed sorts newest reflection first by the reflection's `written_at`, ties by the random `id`. (d) now reads: the feed reader's body ends `ORDER BY r.written_at DESC, r.id` and orders by nothing else; it returns no time-typed column; the app shows rows in the order returned and re-sorts by nothing. A sort by `captured_at`, `captured_on`, a note's `written_at`, `ctid`, `xmin`, `journey_reveal.finished_at`, `unlocks_at` or `committed_at` fails. The test reads the reader `WITH ORDINALITY` against a plain-SQL oracle, with a planted `captured_at` sort that must be caught (`Phase-1-Amendments.md` §11 check 3, evidence at line 917). C14 (the announcement feed's order) is still provisional
- **Decided 2026-10-31 (FS §20 AAA, `FS:334`), for (c):** a photo saved by the guard-bug retry is stored at the press instant, so its `captured_at`, its date and its place in any order are exactly what the press would have given. No column, id or order marks a photo as retried. Add to (c): one press saved by the retry, read by the owner and by a network reader, sits where an ordinary press at that instant sits
- **Decided 2026-10-31 (FS §20 DDD, FFF, `FS:337`, `FS:339`):** the bug log's line prefix carries a real time and a virtual transaction id, which is a server counter. It lives outside the product data and no product role can read it (R-167), so (a) and (b) do not reach it. They do reach anything that copies it in: no table, column or reader may hold a log line, a virtual or real transaction id, or a log time

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** the order clause covers photos, notes and journeys. One time-decided order is allowed, by `PROVISIONAL: B52`: a viewer's own incoming friend requests, newest first by that request's own `sent_at`, with no time value returned. It must never take its key from another table's time (R-192)
### R-161
- **Statement:** A user's join date is readable by that user only. Everyone else reads names, never when someone joined.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS §20 TT (`FS:324`); R-008, R-152 (a join date can equal a first Commit date, P1:213). Found by r6 V1 (`Phase-1-Amendments.md:679`)
- **How to check:** As First Light and as Second Wind, read every user through every reader and route. No `joined_at`, and nothing derived from it ("member since", year joined, "new here"), appears for anyone but oneself. As each user, one's own `joined_at` is present. Under B4's "per year with the app" setting, a ring count shown to others gives the join year: see G-23. UI review: Another user's profile and the name search.
- **Current implementation:** not yet specified. `user_rows()` returns every row, `joined_at` included, to every viewer (`Phase-1-Amendments.md:679`)
- **Decided 2026-10-31 (FS §20 WW, `FS:330`):** under B4's "per year with the app" setting the per-year rings show only on the user's own profile. Everyone else sees one ring per finished reveal under both settings (R-166). The G-23 sentence in the how-to-check above is settled by WW
- **Updated 2026-10-31 (r7):** the implementation is now specified: `user_rows()` returns `joined_at` only on the viewer's own row and NULL on every other, and no `profile_picture` (FS §20 YY); the person-tag writer reads it inside its definer body and returns nothing of it (`Phase-1-Amendments.md` §11, lines 774 and 793; `P1:62`, `P1:63`). The mask is tested over whole tuples against a plain-SQL oracle (§11 check 3)

### R-162
- **Statement:** Whether a journey's reveal is finished is known only to the owner and, after unlock, the owner's network. A public reader or a stranger never learns it, whether from a record, from a field or from a change in what they can read.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS §20 SS (`FS:323`), FS §20 T; R-152; P1:45. Found by r6 V2
- **How to check:** At baseline, as Long Way Round, #4 reads as not finished and #3 as finished. As Open Hands (network), the same. As First Light (public, on no one's map), no reader or route about Round returns a reveal state or a finish time, and nothing else differs between #3 and #4. G-23 lists the paths that still differ (the Positivity Feed, rings, Public photos under B2's option). Before unlock no reveal state exists, so none can be read.
- **Current implementation:** not yet specified. The `journey_reveal` reader is missing (`Phase-1-Amendments.md:692`)
- **Decided 2026-10-31 (FS §20 ZZ, `FS:333`):** "never learns it" means never shown or readable as a field. A public reader may infer it from Positivity Feed entries, rings and photos appearing. The how-to-check above reads under ZZ: no reader or route returns a reveal state, finish time or "finished" marker to First Light; the paths in G-23 may differ between #3 and #4, and nothing else may
- **Decided 2026-10-31 (FS §20 CCC, `FS:336`):** one reader, for every viewer, returns how many of a user's reveals are finished and nothing else. It is the only reveal-derived value a public reader receives (R-166)
- **Updated 2026-10-31 (r7):** the implementation is now specified: `journey_reveal_rows()` with the policy changed to the same rule, its predicate not executable by any product role (`Phase-1-Amendments.md` §11, lines 787 and 794; `P1:164`)

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** "As Open Hands (network), the same" is stale: Hands is not Round's friend. The network viewer is now Steady Lantern (fr-4). Hands, on Round's map with no friendship, reads no reveal state for #3 or #4, as First Light does (R-188)
### R-166
- **Statement:** Another user's circle tells the viewer only how many reveals that user has finished. The number moves only when a reveal is finished, carries no date, year or journey, and is drawn as rings, never shown as a number, total or comparison.
- **Type:** auto (data) and review (UI) · **Applies to:** data, API, UI
- **Source:** FS §20 CCC (`FS:336`), WW (`FS:330`), ZZ, TT; CL:69 (counters), CL:71 (ranking); FS:185; R-102, R-162. Proposed by `Phase-1-Amendments.md` §11 checks 2 and 5 ("for the rules-guardian to number"). Numbered by r7
- **How to check:** (1) The count reader is a definer function returning one integer, not a set and with no OUT column; its estimate is constant (§11 check 2). (2) For every viewer and every profile, a missing id and NULL included, it equals the plain count of that profile's finished reveals; for a network viewer it equals the owner's `journey_reveal_rows()`. (3) Polling as First Light across a capture into a sealed journey, a commit, an unlock, a reflection and finished reveals: between any two polls the change equals the change in a network member's count of that owner's "journey launched". Planted faults (count from unlock, count from commit, a date-returning variant) are caught. (4) UI review of Another user's profile, and of Profile (own) under both B4 settings: no numeral, "n journeys", "n years", total, "since" or comparison beside the circle, and no ring carries a date, year or journey label for a public viewer.
- **Current implementation:** `ring_count(profile_id uuid) → integer`, EXECUTE for the viewer role only (`Phase-1-Amendments.md` §11, lines 804–809, evidence 918–939; §3 `b4`, line 234; `P1:65`)

### R-202
- **Statement:** While either person holds an active block on the other, every reader and writer that takes a user id answers the other person exactly as it answers an id that does not exist, byte for byte: profile, name search, `ring_count()`, `has_journey_underway()`, journey, overview, photo, reflection, announcement and Positivity Feed readers, the request writer and the user-tag writer.
- **Type:** auto · **Applies to:** data, API
- **Area:** 5. Visibility and access
- **Source:** FS §20 MMMM; `PROVISIONAL: B63`, `B64`; `Phase-1-Amendments.md` §15.3, §15.5 cases 1–2. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V5 (§15.3 omits `ring_count()` and `has_journey_underway()`)
- **How to check:** List every function `mj_app` may EXECUTE that takes a user, profile or journey id. For each, as Long Way Round after Second Wind blocks him, call it with Wind's id and with a random uuid: identical result, error text and row shape. Then as Wind with Round's id. The list must equal the set §15.3 names; a function missing from §15.3 fails.

### R-203
- **Statement:** A block changes nothing on either person's map, ends a current friendship and its close-friends place, closes open requests both ways, and is reversed only by the blocker; an unblock restores nothing. Only the blocker reads the block (name and id only, no time, no count). Every place a blocked pair still meet on their own screens (their own map, their own tags, their own request lists, their own feed) is stated in Screen-Inventory, and none says "blocked" or differs from what an ended friendship shows unless the docs say so in words.
- **Type:** auto (data), review (UI) · **Applies to:** data, API, UI, copy
- **Area:** 5. Visibility and access
- **Source:** FS §20 MMMM, G, NNNN; `PROVISIONAL: B62`–`B69`; `Phase-1-Amendments.md` §15.2, §15.4, §15.5 cases 3–6. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V6 (S-07 under a block undecided; four tells beyond §15.4's "only by absence")
- **How to check:** §15.5 cases 3 to 6. Add: `layer` rows byte-identical across block and unblock; render Layers S-07 for both people after the block and compare with the docs' stated behaviour (fails while none is stated); `block_rows()` as blocked person and as a third party returns no row; grep copy for `blocked` on any screen the blocked person can reach.

### R-204
- **Statement:** The blocked list S-25 is the owner's only: names A to Z, no time, no count, names lead nowhere, a way to unblock each, and a way in from S-05 that is present and identical in every state. No other screen shows that anyone has blocked or been blocked.
- **Type:** review, then auto · **Applies to:** UI, copy
- **Area:** 5. Visibility and access
- **Source:** FS §20 MMMM; `PROVISIONAL: B65`, `B66`, `B67`, `B68`; SI S-25; R-192, R-194. Added by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` (MMMM had no check; Rubric header 2026-11-10 second pass)
- **How to check:** Render S-05 with 0 and 3 blocks: identical DOM apart from nothing. Render S-25 with 3: three names, A to Z, no digits, no dates, no links on names. Grep copy for `blocked` outside S-25 and the block confirmation.

---

## 6. Layers

### R-069
- **Statement:** No endpoint or response tells a user which ring they sit on in someone else's map. Layer data can be read only by the map's owner.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:74, CL:82, MP:47, FS:164, FS:235, P1:51. **= §2.5 check 7** (first half)
- **How to check:** As Second Wind, query every table and endpoint that holds layer data: only rows where Wind is the owner return.
- **Current implementation:** layer rows readable only where `owner = viewer` (P1:51).
- **Updated 2026-10-31 (FS §20 OO; R-164):** the layer table refuses the viewer role; read through `layer_rows()` and every other reader and route: only rows where Wind is the owner. The internal helper that takes a member and returns owners (`Phase-1-Amendments.md` §11, line 702) must not be executable by any product role (R-070). R-072, R-073, R-074 and R-080 read their map snapshots the same way, through `layer_rows()` as the map's owner

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** `Phase-1-Amendments.md` §12.7 K10 tightens this: no access decision reads the map at all. The R-156 scan pointed at the relation `layer` returns exactly {`finish_reveal`, `layer_rows`}; a policy, view or dynamic-SQL function naming `layer` is a failure. Numbered as R-188's how-to-check (2)
### R-070
- **Statement:** Nothing can be called that takes a member and returns whose maps they are on.
- **Type:** auto · **Applies to:** API
- **Source:** P1:51, FS:235
- **How to check:** List every function and route that takes a user id and touches layer data. None may return owners for a given member.
- **Decided 2026-10-30 (FS §20 FF, `FS:310`):** `viewer_in_network(owner_id)` may stay directly callable. It takes an owner and answers only for the current viewer, which reveals nothing beyond what §20 T journey rows already give a network member. The check above still fails any call that takes a member and returns owners, and any route that exposes the predicate

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** FS §20 FF's reason is replaced. `viewer_in_network(owner)` now answers whether the viewer and that owner are current friends, which `friend_rows()` already tells the viewer; it no longer reflects the map. The member-to-owners helper is gone (`Phase-1-Amendments.md` §12.1); the check above still fails any function or route that takes a member and returns owners
### R-071
- **Statement:** No screen or copy shows a person their ring on someone else's map, directly or by implication: no "you're in X's inner circle", no closeness badge or colour on their own avatar in someone else's view, no "you moved closer" or "further away", no ordering of someone else's content by the viewer's ring.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:74, FS:164, MJC:422
- **How to check:** Review every screen as a member, not the owner. Grep aid: `inner circle`, `closest`, `close friend`, `your ring`, `moved (in|out|closer|further)`. See G-12.
- **Provisional default:** Decisions-Needed B12 (switchable, R-147): Walking a path shows the photos where the reader appears, in journey order, with no total and no grouping (other setting: hidden). Holds as written under both settings. Under "shown", the "where you appear" view is checked as R-139 says
- **Provisional default:** Decisions-Needed B11 (switchable, R-146): "Path crossed" names both people, reaches the owner's network, and never says which ring (other setting: unnamed). Holds as written under both settings: the named person learns they crossed the owner's path, never their ring (R-092)
- **Updated 2026-11-10 (FS §20 NNNN):** B11 and B12 are fixed (unnamed; hidden). Read the two provisional lines above under those settings only: "path crossed" names no one, and no reader is shown where they appear

### R-072
- **Statement:** A tag by A never creates or changes anything on B's map.
- **Type:** auto · **Applies to:** data
- **Source:** FS:161, FS:277 (§20 G), P1:27 (D14), P1:160. **= §2.5 check 7** (second half)
- **How to check:** Snapshot B's layer rows, have A finish a reveal tagging B six times, snapshot again: identical.

### R-073
- **Statement:** A tag with a typed name never produces a layer entry or a crossing.
- **Type:** auto · **Applies to:** data
- **Source:** FS:163, FS:267, P1:26 (D13). **= §2.5 check 8**
- **How to check:** Open Hands → "Ava" (41 tags in Hands #2) produces no layer row and no "path crossed".

### R-074
- **Statement:** Tagging yourself never counts towards a ring.
- **Type:** auto · **Applies to:** data
- **Source:** P1:156
- **How to check:** A tags A in 5 photos and finishes the reveal: no layer row with owner = member.

### R-075
- **Statement:** Any user counts towards a ring, whether or not they have ever had a journey.
- **Type:** auto · **Applies to:** data
- **Source:** FS:163, FS:277, P1:27 (D14)
- **How to check:** Long Way Round → Open Hands in Round #1 (Hands #1 sealed then): Hands on Round's map, middle. The "no journey" case: Open Hands → First Light at the scripted Hands #4 reveal, 2027-06-20 (P1 §3.8, amended 2026-10-30): First Light on Hands' map, outer, while she has no journey; her own map stays empty.

### R-076
- **Statement:** Tags in Private photos count towards rings.
- **Type:** auto · **Applies to:** data
- **Source:** FS:277 (§20 G), P1:27 (D14), P1:156
- **How to check:** Lantern #1 tags Wind in 6 photos, 2 of them private: Wind is tight, which needs all 6.

### R-077
- **Statement:** In each finished journey, a user tagged in 5 or more photos is tight, 2 to 4 is middle, 1 is outer.
- **Type:** auto · **Applies to:** data
- **Source:** FS:161, FS:277, P1:28 (D15), CL:107
- **How to check:** Boundary cases 1, 2, 4, 5. Fixture: Lantern's map of Wind across #1–#5 (P1:264–270).

### R-078
- **Statement:** Someone on the map who is not tagged in a finished journey moves out one ring. Outer stays outer. Nobody is ever removed from a map.
- **Type:** auto · **Applies to:** data
- **Source:** FS:165, FS:277, P1:28 (D15), P1:157, CL:107
- **How to check:** Lantern #3 and #4: Wind goes middle → outer → outer, and is never absent from Lantern's map.

### R-079
- **Statement:** Someone tagged again with fewer photos goes straight to the ring that count gives.
- **Type:** auto · **Applies to:** data
- **Source:** FS:282 (§20 L), P1:404 (R1)
- **How to check:** Tight last journey, tagged once this journey: outer.

### R-080
- **Statement:** Maps change only when the owner finishes a reveal. Nothing on any map changes during a sealed year, at unlock, or for a reveal never finished.
- **Type:** auto · **Applies to:** data
- **Source:** FS:91, FS:162, FS:269, P1:150
- **How to check:** Jump the clock through a full sealed year with captures and through an unlock: layer rows unchanged. They change only at a reveal-finished event.

### R-081
- **Statement:** Closeness is earned by tags, never chosen. There is no follow, friend request or hand-picked list of close people.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:160, P1:181 ("follower"). Part of **§2.5 check 6**
- **How to check:** Schema scan for `follow`, `follower`, `friend_request`, `close_friend`. No UI control adds a person to a ring.

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** superseded in part by FS §20 KKKK. Mutual friend requests and an owner-only close-friends list now exist (§12.1). What still holds: **the map's rings are earned by tags only, never chosen**, and no UI control adds a person to a ring; there is no one-way **follow**. The schema scan now fails on `follow` and `follower` anywhere, and on `friend_request` or `close_friend` only outside the six §12.1 tables, their writers and their readers
### R-082
- **Statement:** The map is drawn as concentric rings with the user at the core, not as a list.
- **Type:** review · **Applies to:** UI
- **Source:** FS:158–159, CL:107, MP:81
- **How to check:** Review the layers screen.
- **Provisional default:** Decisions-Needed C8: The map shows current rings only: no counts, no history, no drift. Under C8 the layers screen also shows no number (people per ring, shared photos per person), no past ring, no "was middle", and no arrow, trail or animation of movement between rings. Grep aid: digits rendered on the map, `previous`, `history`, `was`, `drift`, `moved`

### R-083
- **Statement:** Drift outward is presented as expected, never as loss, failure or demotion.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:165, MJC:422
- **How to check:** Review the owner's own map and any copy about ring changes. Grep aid: `lost`, `dropped`, `demoted`, `unfriend`, `fading`.
- **Provisional default:** Decisions-Needed C8: The map shows no drift. Under C8 no screen presents drift at all (R-082), so this check applies to any copy that still mentions ring changes, such as site or help text

### R-139
- **Statement:** No screen lets any user see or work out a ring on a map that is not their own. There is no count of how often a person is tagged in someone's journey, no grouping of a journey's photos by the person tagged, and no "people in this journey" list ordered by how often they appear. This covers third parties as well as the person tagged.
- **Type:** review · **Applies to:** UI, copy
- **Status:** Provisional only for the tagged reader's own appearances, which `FS:196` asks for (G-12). For everyone else it holds as written
- **Source:** FS:164 ("Each user sees only their own map"), FS:161 (the ring is the count of tagged photos in one journey), CL:74, MP:47, P1:51. R-071 covers only the person on the ring; this check covers anyone reading someone else's journey. Found by `docs/reviews/2026-10-27-rules-screen-inventory.md` finding 10
- **How to check:** As Open Hands (on Steady Lantern's map), read Lantern #1, where Lantern tags Second Wind in 6 photos. Nothing on Walking a path, Another user's profile or A photo followed forward totals, groups or orders by how often Wind appears. Grep aid: `appears in`, `\d+ photos? (with|of)`, `most tagged`, `people in this`, and any reader-side query that groups or counts person tags by person.
- **Provisional default:** Decisions-Needed B12 (switchable, R-147): Walking a path shows the photos where the reader appears, in journey order, with no total and no grouping (other setting: hidden). Under "shown" the provisional exception narrows to exactly that: a list of the reader's own appearances, in journey order, among photos the reader can already read. Any total, "n photos", pagination count, grouping, ordering by frequency or progress-like scroll position fails. The reader can still count by scrolling (the residue of G-12); every audit reports it as the weakest point of this check until the user decides. Under "hidden" the check holds in full, with no exception
- **Provisional default:** Decisions-Needed C6 (switchable, R-148): People tags are not shown to readers (other setting: shown). Under "hidden" no reader sees any person tag, so a third party cannot count a person's tags and the check holds trivially. Under "shown" the check holds as written: tags appear on a single photo only, never totalled, grouped or listed across a journey

---

## 7. Feed and notifications
- **Updated 2026-11-10 (FS §20 NNNN (b)):** B12 and C6 are fixed to hidden. No reader sees any person tag or any mark where they appear, so the check holds trivially; any tag or mark sent to a non-owner, in the UI or the data, fails

### R-084
- **Statement:** The feed carries only three kinds of announcement: journey launched, reflection left, path crossed.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:171–175, CL:109, MP:83, P1:31 (D18), P1:168. **= §2.5 check 9** (types)
- **How to check:** Schema: the announcement type allows exactly these three values. Inserting any other raises.
- **Updated 2026-10-31 (FS §20 OO; R-164):** the "insert any other" case runs as the table's owning role (the type constraint raises); no writer function can produce another type

### R-085
- **Statement:** An announcement holds no image, media or count.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:72, MP:45, FS:171, P1:168. **= §2.5 check 9** (no media)
- **How to check:** Schema scan of the announcement store: no media, image, url, thumbnail or count field. API responses for the feed contain no image URL.

### R-086
- **Statement:** The feed screen shows no photograph: no thumbnail, preview or cover image in any announcement.
- **Type:** auto · **Applies to:** UI
- **Source:** CL:72, MP:45, FS:171. See G-9 for avatars
- **How to check:** UI test at several simulated dates: the feed DOM has no `img`, `picture`, `canvas` or background image sourced from a photo or note.
- **Provisional default:** Decisions-Needed C7: No profile picture is shown anywhere; announcements carry no image. Firm under C7: an announcement shows no avatar, profile picture or other image of a person either. The UI test widens to any `img`, `picture`, `canvas` or background image inside an announcement, whatever its source (closes G-9)
- **Decided 2026-10-31 (FS §20 XXX, `FS:360`):** C7 is decided in full. The provisional line above now holds as a decision; announcements carry no image

### R-087
- **Statement:** "Journey launched" goes out exactly when a reveal is finished, never at Commit or unlock.
- **Type:** auto · **Applies to:** data
- **Source:** FS:280 (§20 J), P1:31 (D18), P1:158, CL:109
- **How to check:** Jump through Lantern #6's unlock with no reveal finish: no announcement. Second Wind finishes #6 on 2027-04-25: one announcement at that time.

### R-088
- **Statement:** "Reflection left" is shown only to users who can read that photo.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:280 (§20 J), P1:31 (D18), CL:109
- **How to check:** Wind reflects on a private photo: no other user's feed shows it. On a network photo: only the network sees it.
- **Provisional default:** Decisions-Needed B10: "Reflection left" reaches only the owner's network members who can see the photo, even when it is public. Under B10 the statement reads "only to users on the owner's map who can read that photo". Add the case: Lantern reflects on a Lantern #5 public photo: First Light and Long Way Round (not on Lantern's map) get no announcement, although both can read the photo
- **Decided 2026-10-31 (FS §20 UU, `FS:325`):** the actor sees their own "reflection left". For the actor only, this is an exception to B10's reading, since FS §20 outranks a provisional default (CL:30). B10 still holds for every other reader: on a public photo, no reader outside the owner's network gets the announcement. `Phase-1-Amendments.md:691` leaves B10 out (r6 V3). UU's "as written in R2" is a loose citation: R2 (`P1:405`) covers only "journey launched" and "path crossed"

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** "users on the owner's map" (the B10 reading) now reads "the owner's current friends who can read that photo". The B10 case changes: Lantern reflects on a Lantern #5 public photo; **Long Way Round, now Lantern's friend (fr-4), receives it**; First Light, who can read the photo but is not a friend, does not. Audiences are worked out when read (`PROVISIONAL: B48`)
- **Updated 2026-11-09, second pass (`PROVISIONAL: B48` changed to event time; `docs/reviews/2026-11-09-rules-kkkk-r2.md`):** the earlier line's "Audiences are worked out when read" is superseded. "Reflection left" reaches the actor and otherwise a current friend whose friendship began strictly before the reflection was written and who can read the photo now (R-197). The B10 case on a Lantern #5 public photo reflected after 2025-10-02 still reaches Long Way Round; on lantern-1's 2025-02-14 reflection it does not
### R-089
- **Statement:** "Journey launched" and "path crossed" are shown to the owner's network.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:282 (§20 M), P1:405 (R2)
- **How to check:** For a fixture reveal finish, the set of feeds containing each announcement equals the owner's map members.
- **Decided 2026-10-31 (FS §20 UU, `FS:325`):** the actor does not see their own "journey launched" or "path crossed". The recipients are the map members, and the map never includes the actor (R-074)

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** "shown to the owner's network" means current friends. How to check: the feeds holding each announcement equal the actor's current friends at read time (`PROVISIONAL: B48`), never the map members. Test with `Phase-1-Amendments.md` §13.4: at baseline the five fixture viewers read 17, 9, 9, 9 and 0 "journey launched" and "path crossed" rows (Q-F9). Whether the person tagged receives "path crossed" when a friend is open with the user (DN E3 (a)); built as KKKK (e), all friends
- **Updated 2026-11-09, second pass (`PROVISIONAL: B48` changed to event time; `docs/reviews/2026-11-09-rules-kkkk-r2.md`):** the earlier line's "at read time" and its counts are superseded. Recipients are the actor's current friends whose friendship began strictly before the event (R-197). At baseline the five fixture viewers read 13, 9, 5, 2 and 0 "journey launched" and "path crossed" rows (`Phase-1-Amendments.md` §13.4.1, Q-F9); the read-time body, planted, gives 17, 9, 9, 9, 0 and must be caught
### R-090
- **Statement:** "Path crossed" goes out for every crossing: one per tagged user in each finished reveal.
- **Type:** auto · **Applies to:** data
- **Source:** FS:280 (§20 J), P1:31 (D18), P1:156, CL:109
- **How to check:** Second Wind's #6 reveal (tags Lantern): one "path crossed". Typed names: none (R-073).

### R-091
- **Statement:** Nothing else produces an announcement: not Commit, capture, a highlight, an unlock, or anything during a sealed year.
- **Type:** auto · **Applies to:** data
- **Source:** FS:171 ("exactly three events"), FS:246
- **How to check:** Commit, capture and start a highlight as First Light, then jump through an unlock. Announcement store unchanged.

### R-092
- **Statement:** A "path crossed" announcement never says how many photos or which ring.
- **Type:** auto · **Applies to:** data, UI, copy
- **Source:** FS:164, P1:168
- **How to check:** Announcement payload is type, actor, subject and time only. Rendered text has no digits and no ring words.
- **Provisional default:** Decisions-Needed B11 (switchable, R-146): "Path crossed" names both people and reaches the owner's network. It never says which ring (other setting: unnamed). Holds as written under both settings. Under "unnamed" the rendered text and the payload sent to readers carry no subject
- **Updated 2026-11-10 (FS §20 NNNN (a)):** B11 is fixed to unnamed. The "named" case is retired: no "path crossed" payload carries a subject

### R-093
- **Statement:** Getting from the feed to someone's journey takes a small deliberate act. Journey content is never shown inside the feed.
- **Type:** review · **Applies to:** UI
- **Source:** FS:177, MJC:423
- **How to check:** Review: opening a journey needs an explicit tap. The feed does not expand, autoplay or preview journey content.

### R-094
- **Statement:** No notification outside the app invites a return visit: no push, email, SMS or OS notification to capture, reflect, finish a reveal, write an overview, come back, or see what someone else did.
- **Type:** auto · **Applies to:** API, UI, dependencies, copy
- **Source:** CL:70, MP:43, FS:236, FS:242, FS:102. See G-16 for "Your Journey is ready"
- **How to check:** Dependency scan for push and mail libraries (`web-push`, `firebase/messaging`, `onesignal`, `pusher-beams`, `nodemailer`, `@sendgrid`, `postmark`, `resend`, `twilio`). Grep for `Notification.requestPermission`, `PushManager`, service-worker `push` handlers, and scheduled jobs that send messages.
- **Provisional default:** Decisions-Needed C1: "Your Journey is ready" appears on next open, never as a notification. Firm under C1: no notification of any kind goes out at unlock, and "Your Journey is ready" exists only as in-app text rendered when the owner opens the app (closes G-16)
- **Provisional default:** Decisions-Needed C15: The app never asks for notification permission. Firm under C15: any call to `Notification.requestPermission`, `PushManager.subscribe` or a native permission prompt fails, as does an in-app "turn on notifications" screen

### R-095
- **Statement:** Nothing in the app reminds or nudges the user to capture, reflect, finish a reveal, write an overview, use a highlight or come back: no banner, toast, modal, empty-state call to action, "you haven't", "frames waiting" or "highlight ending soon".
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:69, FS:102, FS:209, FS:233, FS:242, MP:42
- **How to check:** Review every screen at several simulated dates, including the sealed-year empty state and a reveal left unfinished. Grep aid: `don't forget`, `remember to`, `you haven't`, `come back`, `we miss`, `still have`, `waiting for you`, `ending soon`, `last chance`.
- **Provisional default:** Decisions-Needed C1: "Your Journey is ready" appears on next open. That text is allowed under C1; anything shown with it that asks the owner to reflect, tag, choose or finish still fails
- **Provisional default:** Decisions-Needed C9: Empty states are a plain statement; copy in Phase 2. Firm under C9: an empty map, feed or circle states what is there and offers no button, link or suggestion to act

### R-096
- **Statement:** There is no unread dot, badge count, "new" marker or app-icon badge anywhere.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:69, CL:70, FS:233, RG:28 ("badges, dots, 'new' markers")
- **How to check:** Grep for `navigator.setAppBadge`, `unread`, `badge`, `isNew`, `\bnew\b` labels, `seen_at`/`read_at` fields. Schema scan for read-state on announcements. Review navigation and feed.

### R-206
- **Statement:** Every announcement line in the feed leads only to the actor's profile (S-16, or S-05 for the owner's own line). No feed line opens a path, a journey or a photo directly.
- **Type:** auto · **Applies to:** UI
- **Area:** 7. Feed and notifications
- **Source:** FS §20 RRRR, FS §13 ("a small deliberate act"); SI S-08, S-06, S-17. Added by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` (RRRR had no check)
- **How to check:** For each of the three line types, read the link target in S-08: only the profile route. Route scan: no route into S-06 or S-17 carries a feed origin. Whether the Positivity Feed counts as "the feed" is N1 of that audit; until ruled, B75 holds and this check covers S-08 only.

---

## 8. Engagement mechanics

### R-097
- **Statement:** There are no streaks: no count of consecutive days, weeks or months, no "don't break the chain", no flame.
- **Type:** auto · **Applies to:** data, UI, copy
- **Source:** CL:69, MP:42, FS:233, P1:181. Part of **§2.5 check 6** (streak)
- **How to check:** Schema scan and copy grep for `streak`, `chain`, `consecutive`, `in a row`, `🔥`.

### R-098
- **Statement:** No count of the quota is shown in a way that reads as a target: no frames left, photos this month, "n of 48", or highlights remaining.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** FS:243, CL:69, P1:49. See G-5
- **How to check:** R-038 and R-039 hold, and copy grep for `left this month`, `remaining`, `of (12|24|48)`, `\d+ (more|to go)`.
- **Provisional default:** Decisions-Needed B7: Frames left are never shown. A refused capture says so with no number (copy in Phase 2). Firm under B7: no count of the quota is shown in any form, not only "in a way that reads as a target" (`FS:243`). Frames used, frames left, highlights used or left, and photos this month all fail, at any time, to the owner as well (closes G-5)

### R-099
- **Statement:** There is no progress bar, completion meter or percentage anywhere: not for the year, the quota, the reveal ("12 of 24 reflected"), the profile or the overview stack.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:69, MP:42, FS:233
- **Status:** Provisional. `FS:233` limits this to the sealed year. See G-4
- **How to check:** Grep for `<progress`, `role="progressbar"`, `aria-valuenow`, `%`, `complete`, `\d+ of \d+`. Review the reveal flow.
- **Provisional default:** Decisions-Needed B8: Counters and progress bars are banned at all times, not only while sealed. Firm under B8: the check holds as written at every app-clock time, sealed, unlocked, during the reveal and after it. "12 of 24 reflected", "3 photos left to tag", a reveal stepper with filled steps and a "%" on any screen all fail. The `FS:233` time limit does not apply while B8 is in force (closes G-4)

### R-100
- **Statement:** There are no likes, reactions or view counts on anything.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** P1:53, P1:181, CL:69. Part of **§2.5 check 6** (like, reaction, view)
- **How to check:** Schema scan for `like`, `reaction`, `heart`, `view`, `view_count`, `impression`. UI review for heart or reaction controls.

### R-101
- **Statement:** No user has a score, rank, level, tier, badge or position on a leaderboard, and no data compares users.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:71, MP:44, FS:185, FS:244, P1:53, P1:181. Part of **§2.5 check 6** (score, rank, badge)
- **How to check:** Schema scan for `score`, `rank`, `level`, `tier`, `badge`, `achievement`, `points`, `leaderboard`, `xp`.

### R-102
- **Statement:** The circle and its rings are a record, not a rank. No screen or copy compares users, ranks them, names a level or tier, or treats more rings as better.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:71, CL:111, FS:185, FS:244, MJC:689–694
- **How to check:** Review profiles and the circle. Grep aid: `level`, `rank`, `top`, `ahead`, `behind`, `veteran`, `elite`, `unlock achievement`.

### R-103
- **Statement:** The Positivity Feed draws only on Public photos and is filtered by endurance and gratitude tags, never ordered or filtered by popularity.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:202–203, P1:324. See G-8 and G-14
- **How to check:** As First Light, the feed holds only public photos with the listed tags. Its query uses no read, like, view or count measure for order or selection.
- **Decided 2026-10-30 (FS §20 W):** the drafted tag list is the four working tags (`MJC:454–459`). **(FS §20 Y):** no chapter filter on the Positivity Feed; B9 (d) is replaced.
- **Provisional default:** Decisions-Needed B9: Positivity Feed: (a) reflection text only, with the photo shown when opened; (b) per-photo visibility; (c) drafted tag list only; (d) ~~chapter filter available~~ no chapter filter (FS §20 Y); (e) newest first; (f) only after reveal finished. Selection by feeling tag is allowed but the tag is never shown to a public reader (FS §20 CC). Under B9 the check reads: the feed holds only photos that are themselves Public (b), from journeys whose reveal is finished (f), tagged with a tag from the drafted list, never free text (c), newest first (e), with no chapter filter (d; FS §20 Y. Before the r4 audit of 2026-10-30 this line read "and may be filtered by chapter (d)", which FS §20 Y had already replaced). Any other reader-side filter has no default and goes to the supervisor, not into the build. Under (a) "text only" each entry shows reflection text and no image until the reader opens it; opening one shows one photo. (a) was decided 2026-10-30 (FS §20 Q): text only, not switchable (R-145; before 2026-10-30 this line read "The (a) setting is switchable"). Add the cases: a Public photo in Long Way Round #4 (reveal never finished) is absent; a Network photo in a journey with other Public photos is absent; the feed order equals reverse time order with no other key
- **Provisional default:** Decisions-Needed B18: Tags never "surface" by popularity. No suggestions and no counts (`FS:202` over `FS:131`). Firm under B18: no screen suggests, sorts, ranks or counts feeling tags by how often they are used, at the tag step or anywhere else, and no job promotes a tag by use. Grep aid: `popular`, `trending`, `suggest`, `most used`, `count(` over feeling tags

### R-104
- **Statement:** No surface is designed to make a visit longer: low usage is the goal.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:76, MP:49
- **How to check:** For each screen, ask whether it would increase time in app (autoplay, endless content, "more like this", pull-to-refresh into new content). If yes, raise it.

### R-140
- **Statement:** No timer, countdown or time-left display runs on the 15-minute note window or on an open highlight: no "14:32 left to add a note", no "ends in 3h", no shrinking bar or ring.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:69 (counters), FS:233 ("No visible counters ... during the sealed year"; both windows exist only while a journey is sealed, so the time limit in G-4 does not apply), RG:28 ("timers"), FS:281, FS:264. R-013 covers only the countdown to unlock. See G-13 for whether a plain open-or-closed highlight state may show. Found by `docs/reviews/2026-10-27-rules-screen-inventory.md` finding 3
- **How to check:** Grep copy and code for `minutes? left`, `ends in`, `time left`, `remaining`, `\d+:\d\d` near note or highlight components, and any `setInterval` or `requestAnimationFrame` that formats a time until capture + 15 minutes or a highlight's end. UI test: render the note step at capture + 0:30 and + 14:00, and the sealed-year and capture screens at highlight start + 1 h and + 23 h. Each pair renders the same DOM.
- **Provisional default:** Decisions-Needed B6: Others learn nothing about highlights. The owner sees only "a highlight is open", with no end time and no countdown. Firm under B6: the plain open state is the only highlight display allowed, and it is identical at start + 1 h and start + 23 h. No end time, start time, "until 3 pm" or "tomorrow" appears (closes G-13 for the owner). Decisions-Needed C4 does not change the note half: the window still runs up to 15 minutes inside capture, and no timer is shown for it
- **Updated 2026-11-10 (FS §20 UUUU, XXXX):** stating a window's length is allowed, once, in words and with the fixed circle drawing (`PROVISIONAL: B77`). Check: render S-12 and S-13 at several instants of a window; the circle and the words are byte-identical at every one. Any drawing that moves, fills, empties or shows time left fails

### R-200
- **Statement:** Nothing marks that a photo's reflection slot has opened. The way from a photo to Reflect looks the same on the day before, the day of and the day after the photo's anniversary, and before and after a reflection fills the slot; a press when no slot is open is refused plainly. No reader returns a list or a count of photos with an open or unwritten slot.
- **Type:** review, then auto · **Applies to:** UI, API, copy
- **Area:** 8. Engagement mechanics
- **Source:** FS §20 VVVV ("Nothing marks a slot opening: no dot, count or notice"), FS §8; R-095, R-096, R-186; pattern of `PROVISIONAL: B76` and R-194. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V3
- **How to check:** As Lantern, render S-17 for lantern-5 at 2026-06-20, 2026-06-21 and 2026-07-06 (after its fixed reflection), in a throwaway copy replayed to before 2026-06-21: identical DOM apart from the stack's own rows. Catalog scan: no function returns more than one photo's slot state.
- **Status:** Provisional. It states the strictest reading of VVVV. The way's behaviour is undecided (V3, rule zero); if the user or a labelled default lets the way appear on the anniversary, this check is superseded

### R-207
- **Statement:** A reflection stack shows only the reflections that exist: no gap, blank, placeholder, year label or "nothing written" for a slot that passed unwritten, and nothing that lets a reader count the years left empty.
- **Type:** review, then auto · **Applies to:** UI, copy
- **Area:** 8. Engagement mechanics
- **Source:** FS §20 SSSS; SI S-14, S-17; Flows Flow 6. Added by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` (SSSS had no check)
- **How to check:** Render S-17 for round-1 (slots 1, 2, 3 written; a generated photo with slots 1 and 3 written if one exists, or a throwaway one): the two stacks differ only by their reflections' own rows. Grep copy for `no reflection`, `skipped`, `empty year`.

---

## 9. Comments and voice

### R-105
- **Statement:** Nobody can comment on or reply to anything: there is no comment or reply object on a photo, journey, reflection, overview or announcement.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:66, CL:83, MP:39, FS:100, FS:152, FS:230, P1:53. Part of **§2.5 check 6** (comment, reply)
- **How to check:** Schema scan for `comment`, `reply`, `thread`, `response`, `message` tables or fields attached to content.

### R-106
- **Statement:** Only the owner can write anything attached to their photo or journey: reflections, notes, overviews, people tags, chapter, feeling tags and visibility.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:100, FS:160, FS:245, P1:52
- **How to check:** As Second Wind, attempt each write on a Lantern photo or journey: all refused.

### R-107
- **Statement:** A reflection has no author of its own. Its author is always the owner of its photo.
- **Type:** auto · **Applies to:** data
- **Source:** P1:52
- **How to check:** Schema: the reflection store has no author column. The insert checks the caller owns the photo.

### R-108
- **Statement:** A photo has no caption.
- **Type:** auto · **Applies to:** data, UI
- **Source:** P1:53, P1:94. Part of **§2.5 check 6** (caption)
- **How to check:** Schema scan for `caption`, `title`, `description` on photos. No caption field at capture or reveal.

### R-109
- **Statement:** When reading someone else's journey, photo, reflection, overview or announcement, there is nowhere to type.
- **Type:** auto · **Applies to:** UI
- **Source:** CL:66, FS:152 ("readable, not commentable"), FS:245, MJC:187
- **How to check:** UI test as a non-owner on each of these views: no `textarea`, text `input` or `contenteditable`.

---

## 10. Recognition and dependencies

### R-110
- **Statement:** No face or vision library is in the dependencies.
- **Type:** auto · **Applies to:** dependencies
- **Source:** CL:67, MP:40, FS:127, FS:231. **= §2.5 check 11**
- **How to check:** Scan every manifest and lockfile for `face-api`, `@vladmandic/face-api`, `@vladmandic/human`, `@mediapipe/*`, `@tensorflow/*`, `tfjs`, `opencv`, `dlib`, `face_recognition`, `deepface`, `insightface`, `@aws-sdk/client-rekognition`, `@google-cloud/vision`, `@azure/cognitiveservices-face`, `clarifai`.

### R-111
- **Statement:** Face detection does not happen anywhere in the pipeline, including the browser's own APIs and camera settings.
- **Type:** auto · **Applies to:** UI, API
- **Source:** FS:231 ("anywhere in the pipeline")
- **How to check:** Grep for `FaceDetector`, `detectFaces`, `faceDetectionMode`, `getFaces`, `faceLandmarks`, and calls to any vision service.

### R-112
- **Statement:** People are tagged by hand. Nothing suggests, pre-fills or guesses a person from the image.
- **Type:** review · **Applies to:** UI, API
- **Source:** CL:67, FS:127, MJC:417
- **How to check:** Review the tagging step: it starts empty and offers people only from what the owner types.

### R-113
- **Statement:** There are no ads anywhere, in the app or on the site.
- **Type:** auto · **Applies to:** dependencies, UI
- **Source:** CL:68, MP:41, FS:232
- **How to check:** Scan dependencies and page source for `adsbygoogle`, `googletag`, `doubleclick`, `googlesyndication`, `admob`, `prebid`, `amazon-adsystem`, `carbonads`, `ethicalads`. Review both for sponsored or promoted content.

### R-114
- **Statement:** User memories (photos, notes, reflections, overviews, tags) are never sold, transferred or used for training.
- **Type:** review · **Applies to:** dependencies, API
- **Source:** FS:247
- **How to check:** Review every outbound call and third-party dependency for anything that receives memory content. Scan aid: `openai`, `@anthropic-ai`, `replicate`, `huggingface`, data-broker or analytics SDKs. Each hit needs a reason recorded in the audit.
- **Provisional default:** Decisions-Needed B15: No usage analytics or telemetry of any kind. Under B15 any analytics, telemetry, session-replay or error-tracking SDK that sends usage data fails, whatever reason is recorded: for example `@vercel/analytics`, `@vercel/speed-insights`, `posthog`, `mixpanel`, `amplitude`, `segment`, `gtag`, `plausible`, `hotjar`, `fullstory`, `logrocket`, `@sentry/*` session or performance features. Whether crash reporting with no usage data counts as telemetry is not stated; a hit goes to the supervisor (answers Question 2)

---

## 11. Time and the clock

### R-115
- **Statement:** Nothing outside the clock module reads the system clock.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** P1:185, P1:194. **= §2.5 check 10**
- **How to check:** Grep outside the clock module for `Date.now(`, `new Date()` with no argument, `performance.now`, `time.time`, `datetime.now`, and in SQL `now()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`, `LOCALTIMESTAMP`, `clock_timestamp`, `statement_timestamp`, `transaction_timestamp`, including column defaults.

### R-116
- **Statement:** Every time rule follows the app clock: the seal, unlock, reflection slots, the note window, highlight ends, the cadence month and Commit.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:194, FS:325 (§21 "A time control"; heading at FS:321; before 2026-10-30 r4 this read `FS:299`, which §20's growth moved onto §20 W)
- **How to check:** Set the app clock to a date far from the real one and run R-001, R-036, R-040, R-046 and R-121. Each must behave as of the app clock.
- **Updated 2026-10-31:** FS §20 grew by II–VV, so §21 "A time control" is now FS:339 (heading FS:335). The source line above was correct at r5
- **Updated 2026-10-31 (r7):** FS §20 grew again by WW–HHH, so §21 "A time control" is now FS:354 (heading FS:350). The lines above were correct when written
- **Updated 2026-10-31 (r8):** FS §20 grew again by III–PPP and a date line, so §21 "A time control" is now FS:365 (heading FS:361). The lines above were correct when written
- **Updated 2026-10-31 (r9):** FS §20 grew again by QQQ–XXX and blank lines, so §21 "A time control" is now FS:375 (heading FS:371). The lines above were correct when written
- **Updated 2026-10-31 (r10):** FS §20 grew again by YYY–BBBB, so §21 "A time control" is now FS:379 (heading FS:375). The lines above were correct when written

### R-117
- **Statement:** The time control moves forward only. To see an earlier moment, it resets to the 2026-10-25 baseline and jumps again.
- **Type:** auto · **Applies to:** API, UI
- **Source:** P1:195, P1:201
- **How to check:** Request a backward jump: refused. Reset: clock equals baseline and fixture state equals the baseline load.
- **Provisional default:** Decisions-Needed B21: Baseline is 2026-10-25 00:00:00 UTC. After reset, `app_now()` reads 2026-10-25 00:00:00 UTC plus only the real time elapsed since the reset (FS §20 V)
- **Provisional default:** Decisions-Needed B22: Reset puts every option switch back to its default. Add the case: flip every switch, reset, and each reads its first-listed setting (R-141)

### R-118
- **Statement:** A journey unlocks exactly 12 months after its commit moment, and at any app-clock time its state matches the clock with no job having to run.
- **Type:** auto · **Applies to:** data
- **Source:** FS:36, FS:273 (§20 C), P1:14 (D1), P1:74, P1:197, CL:87
- **How to check:** For each fixture journey, unlock = commit + 12 months. Jump to unlocks_at with all scheduled jobs disabled: the journey reads as unlocked. See G-18.
- **Provisional default:** Decisions-Needed B16: A commit on the 29th–31st uses the last day of shorter months. One time zone for the prototype (UTC). Add the cases, all in UTC: commit 2026-01-31 → month 2 starts 2026-02-28; commit 2028-02-29 → unlock 2029-02-28; the unlock moment carries the commit's time of day

### R-119
- **Statement:** On each clock jump, scripted fixture actions dated up to the new time are applied first, then maps are computed for reveals finished since the last jump, then announcements go out.
- **Type:** auto · **Applies to:** data
- **Source:** P1:196–200
- **How to check:** Jump from baseline to 2027-05-01. Second Wind's #6 reveal (2027-04-25) is applied, Lantern is on Wind's map at middle, then the announcements exist with times after the map entry.
- **Decided 2026-10-30 (FS §20 BB):** scripted actions run at 12:00 UTC on their dates; unlocks stay at 00:00 UTC. Second Wind's reveal above is at 2027-04-25 12:00:00 UTC
- **Provisional default:** Decisions-Needed B26: A scripted action the running clock has already passed is applied at the next jump. Add the case: let the running clock pass 2027-04-25 12:00 UTC with no jump; before the next jump nothing of the Wind #6 reveal exists; after it, the reveal, the map entry and the announcements exist
- **Open (`Phase-1-Amendments.md` OQ-3, raised to the supervisor by the r4 audit, not decided here):** the finish function writes the layer entry and the announcements at the same instant, so "times after the map entry" cannot hold as worded. Whether the test reads "not before" is for the user; the check is not weakened until then

### R-120
- **Statement:** Capture times, reflection and overview times, highlight starts and Commit times come from the app clock, never from the client.
- **Type:** auto · **Applies to:** API
- **Source:** P1:73, P1:90, P1:115, P1:132
- **How to check:** Send each write with a client timestamp a year off. The stored time equals the app clock.
- **Decided 2026-10-31 (FS §20 OOO, `FS:348`):** the join joins this list. `joined_at` is `app_now()` at join and nobody can back-date it. Add to the check: the join function has no argument of a time type, a call that passes a date fails, and a `user` row whose `joined_at` is not `app_now()` is refused, also for the table owner (R-164). The loader reaches each fixture join instant by jumping the clock, never by passing a time. Where an event falls at the clock's current instant (each fixture join and first Commit share one instant, P1:213), the loader makes no jump; it never weakens the forward-only jump to do so (R-117; r8 N1)
- **Current implementation:** `join_user(name text) → uuid` plus a `BEFORE INSERT` trigger on `user` (`Phase-1-Amendments.md` §2.2 line 177, evidence 226–246; `P1:63`, `P1:176`, `P1:213`)

### R-121
- **Statement:** All photos of a journey share reflection slots: slot k runs from unlock + (k − 1) years to unlock + k years, and each photo takes at most one reflection per slot. The slot is worked out from the app clock, never chosen by the client.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:97, FS:101, FS:274 (§20 D), P1:22 (D9), P1:115, CL:105. See G-1
- **How to check:** For Lantern #1 (unlock 2022-01-01), a reflection on 2023-12-31 is slot 2 and one on 2024-01-01 is slot 3, for every photo regardless of capture date. A second reflection in the same slot is refused. A client-supplied slot is ignored.
- **Updated 2026-11-10 (FS §20 VVVV, replacing §20 D; `Phase-1-Amendments.md` §16.1):** the statement now reads "Each photo's reflection slots follow its own capture date: slot k runs from capture date + k years to + (k+1) years, 00:00 UTC; slot 0 is refused". New how-to-check: as Lantern, reflect on lantern-5 (captured 2025-06-21) at 2026-06-20 23:59:59, refused; at 2026-06-21 00:00:00, accepted, slot 1. The 18 fixed reflections (P1 §3.5, §3.7) each load inside their slot. `PROVISIONAL: B70` for 29 February. The old case (Lantern #1, slots by unlock) is retired. G-1 is closed: FS:104–111's capture-date example was right
- **Superseded by R-198 on 2026-11-10** (`docs/reviews/2026-11-10-rules-supervisor-carriage.md`). The supervisor's 2026-11-10 `Updated` line above rewrote this statement in place; by "How the rubric grows" the new rule takes a new number. The line is kept as history (R-172). Its how-to-check cannot run on the loaded fixture (forward-only clock, lantern-5's fixed 2026-07-05 reflection); R-198 says how

### R-122
- **Statement:** Each journey takes at most one overview per slot, on the same slot windows as reflections.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:117, FS:275 (§20 E), P1:23 (D10), P1:124. See G-15
- **How to check:** Second overview in one slot: refused. Fixture count: Steady Lantern has 15 (P1:308).
- **Provisional default:** Decisions-Needed B13: The slot 1 overview can be written after the reveal is finished, within the slot. Readable by the network only. Add the case: Steady Lantern writes a slot 1 overview on Lantern #5 after its reveal is finished and before unlock + 1 year: accepted. G-15 is being fixed by A6 (2026-10-27); this check already tests the corrected wording
- **Updated 2026-10-31 (FS §20 OO; R-164):** run the second overview through the overview writer function (refused) and as the table's owning role (the uniqueness constraint raises)
- **Updated 2026-11-10 (FS §20 VVVV):** "the same slot windows as reflections" now reads "the unlock-based windows (FS §20 E)"; reflections no longer share them

### R-123
- **Statement:** The months that set the frame limit are counted from the journey's own commit date, not from calendar months.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261 (§20 mechanics 1), P1:18 (D5), CL:95
- **How to check:** Commit on the 20th. Month 1 runs to the 20th of the next month: a capture on the 1st of the next calendar month is still month 1. See G-18.
- **Provisional default:** Decisions-Needed B16: A commit on the 29th–31st uses the last day of shorter months; UTC. Add the case: commit on 2026-01-31 (UTC); month 2 starts 2026-02-28, month 3 on 2026-03-31

### R-198
- **Statement:** Each photo's reflection slots follow its own capture date: slot k (k ≥ 1) runs from capture UTC date + k years, 00:00 UTC, to + (k+1) years; slot 0 is refused, and so is any reflection before the journey unlocks (R-199). One reflection per photo per slot; the slot is worked out from the app clock, never chosen by the client. A 29 February photo opens on 28 February in other years (`PROVISIONAL: B70`).
- **Type:** auto · **Applies to:** data, API
- **Area:** 11. Time and the clock
- **Source:** FS §20 VVVV (replacing §20 D), FS §8; P1 D9 and P1:115 as amended; `Phase-1-Amendments.md` §16.1. Supersedes R-121 (2026-11-10). Numbered by `docs/reviews/2026-11-10-rules-supervisor-carriage.md`
- **How to check:** In a throwaway copy replayed only to before 2026-06-21 (the clock moves forward only, O1, and lantern-5 holds a fixed slot-1 reflection from 2026-07-05): lantern-5 at 2026-06-20 23:59:59 refused, at 2026-06-21 00:00:00 accepted (1); a second at 2027-06-20 refused, at 2027-06-21 accepted (2). The 18 fixed reflections (P1 §3.5, §3.7) each load inside their slot, cell by cell as in `docs/reviews/2026-11-10-rules-supervisor-carriage.md` auto check 4. A client-supplied slot is ignored.

---

## 12. Copy and tone

### R-124
- **Statement:** No product copy, in the app, on the site, in metadata or in any message, uses engagement, ranking, leak or retake language.
- **Type:** auto · **Applies to:** copy
- **Source:** CL:64–74, MP:37–47
- **How to check:** Grep all copy for `streak`, `level up`, `badge`, `leaderboard`, `rank`, `score`, `points`, `don't forget`, `come back`, `we miss`, `you haven't`, `moments captured`, `frames left`, `days to go`, `unread`, `new!`, `trending`, `popular`, `likes`, `followers`, `comment`, `retake`, `try again`, `edit reflection`, `delete`. Every hit goes to review, since the site may rightly say "No retakes" or "no streaks" as a refusal.

### R-125
- **Statement:** No copy asks the user to perform: no "make it count", "get the perfect shot", "show off" or "share your best".
- **Type:** review · **Applies to:** copy
- **Source:** CL:127, MP:112
- **How to check:** Read every screen's copy and the site.

### R-126
- **Statement:** Nothing on a profile signals how the person looks or how well they are doing.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:29, MP:113, MJC:696. See G-10
- **How to check:** Review profile screens for status, success markers, counts and physical descriptors.
- **Provisional default:** Decisions-Needed C7: No profile picture is shown anywhere. The profile shows the name in the circle. Firm under C7: no profile picture, avatar or uploaded image of a person appears on any profile, map, tag or announcement. Grep aid: `avatar`, `profile_picture`, `profilePicture`, `photoURL` rendered in UI (closes G-10 for the prototype)
- **Decided 2026-10-31 (FS §20 XXX, `FS:360`; extends YY):** C7 is decided in full: no profile picture anywhere, and the profile shows the owner's name in the circle. The provisional line above now holds as a decision

### R-127
- **Statement:** The name step asks for a name from within, not a handle and not a physical or earthly attribute, and says the name is kept.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:29, FS:268, P1:32 (D19)
- **How to check:** Read the name step's copy.
- **Provisional default:** Decisions-Needed C11: No sign-up or onboarding in the prototype. Fixture users are picked from the prototype panel. The name step does not exist in the prototype, so this check has nothing to read there. It stays in force for whatever build adds a name step. A prototype that adds a sign-up or name step anyway fails R-134

### R-128
- **Statement:** Capturing a low point is invited, never nudged. Nothing prompts anyone to photograph a bad moment.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:209, MJC:594–595
- **How to check:** Read all capture, sealed-state and site copy about hard times.

### R-129
- **Statement:** Copy stays positive and hopeful, even in hard chapters.
- **Type:** review · **Applies to:** copy
- **Source:** FS:135
- **How to check:** Read copy shown with hard-chapter journeys (Long Way Round #1–#2, P1:239–240).

### R-130
- **Statement:** The site and the product say plainly and early that we are not trying to get users onto the app.
- **Type:** review · **Applies to:** copy
- **Source:** CL:76, MP:49, MP:138, BP:126
- **How to check:** Check the site's first screen and the app's first-run copy.
- **Updated 2026-11-09 (FS §20 HHHH):** met by the website (Phase 5). "We want you here less, not more." belongs on the site; the app is not required to carry it in first-run copy.
- **Provisional default:** Decisions-Needed C11 and C12: No onboarding in the prototype; the app opens on the Profile. The prototype has no first-run copy, so the app half of this check is read on the Profile as first opened; the site half is unchanged

### R-131
- **Statement:** These lines appear, stated plainly: "It's not about attention. It's about intention." · "You've come further than you think." · "Strict at capture. Generous at reflect." · "No retakes. That moment is gone." · "This app takes time, like many other good things." · "We want you here less, not more."
- **Type:** auto · **Applies to:** copy
- **Source:** MP:115–122, CL:129–136
- **How to check:** Exact-string search of the site build for each line.

### R-132
- **Statement:** On the site, strict at capture, no retakes, low usage is the goal, and this app takes time appear above the fold or close to it.
- **Type:** auto · **Applies to:** copy, UI
- **Source:** BP:130
- **How to check:** Render the home page at a fixed phone and desktop viewport and check the four statements are in or just below the first viewport.

### R-133
- **Statement:** The button that starts a journey says "Commit".
- **Type:** auto · **Applies to:** UI, copy
- **Source:** FS:45, CL:87, MP:55
- **How to check:** UI test: the button's label is exactly "Commit".

---

## 13. Across every area

### R-134
- **Statement:** Every behaviour in a deliverable traces to a source line. Anything not specified was raised as a question, not filled in.
- **Type:** review · **Applies to:** data, API, UI, copy
- **Source:** CL:17, MP:9, MP:151
- **How to check:** For each behaviour in the target, find its source. Anything without one is a finding.
- **Provisional default:** Rule zero as of 2026-10-27 (CL:19–24): a behaviour built from a `Decisions-Needed.md` provisional default, with its `PROVISIONAL: <ID>` label (R-149), has a source. A behaviour the docs do not settle and no default covers is still a finding, even if it looks like the obvious choice

### R-135
- **Statement:** Where two docs disagree, the deliverable cites both and raises the question. It does not pick one.
- **Type:** review · **Applies to:** data, API, UI, copy
- **Source:** CL:30
- **How to check:** Compare the target against the Gaps below. A deliverable that silently follows one side fails.
- **Provisional default:** Rule zero as of 2026-10-27 (CL:19–24): where a Gap now carries a provisional default, building that default with its label is not picking a side. Building the other side, a third reading, or the default without its `PROVISIONAL:` label still fails. Gaps marked "still open" below have no default and fall under the original wording

### R-136
- **Statement:** No deliverable is built or audited from `docs/Overview.md`.
- **Type:** auto · **Applies to:** copy
- **Source:** CL:41
- **How to check:** Grep deliverables and briefs for `Overview.md` cited as a source.

### R-137
- **Statement:** Every auto check in this rubric runs in the build and fails it when broken.
- **Type:** auto · **Applies to:** data, API, UI, dependencies
- **Source:** P1:174 ("Each one fails the build"), BP:203, CL:78
- **How to check:** Map each auto R-ID to a test in the suite. An auto check without a test is a finding.

### R-164
- **Statement:** A test of a rule's guard passes only on the path that could otherwise succeed. A refusal caused by a missing privilege does not prove the rule. Where the product roles hold no privilege on a table, each guard (trigger, constraint, insert-only rule, seal) is also tested through the definer function that writes or reads that table, and as the role that owns the table. Both must refuse for the rule's own reason.
- **Type:** auto · **Applies to:** data
- **Source:** FS §20 MM, OO; `Phase-1-Amendments.md` §11, "Where OO meets an existing rule", item 2 (line 710); R-137. Found by r6: lead-tech flagged that direct-table tests now pass by refusal
- **How to check:** Every auto check whose test touches a table has three cases: (a) the product-role refusal (`permission denied`); (b) the writer or reader function case, with the expected refusal or 0 rows; (c) where the guard is a trigger or constraint, the table-owner case, raising the trigger's or constraint's own error, not `permission denied`. A test with only (a) fails. Counts are read through the readers, never by `count(*)` on a table as a product role. Checks updated for this on 2026-10-31: R-001, R-002, R-003, R-010, R-015, R-018, R-021, R-022, R-023, R-026, R-052, R-057, R-069 (with R-072, R-073, R-074, R-080), R-084, R-122, R-151, R-152, and §2.5 check 4

### R-165
- **Statement:** Every dated ruling in FS §20 is carried in each build doc it bears on. No build doc calls a decided question open, "not picked", "waits on", "none yet" or "confirm", and none keeps a behaviour the ruling replaced.
- **Type:** auto (open-word scan) and review (carriage) · **Applies to:** data, API, UI, copy
- **Source:** CL:28–30 (FS §20 wins); R-134; R-150 (the same rule for provisional defaults). Found by r5 V1–V3 and r6 V1, V2 and V4: the same kind of finding in two rounds running
- **How to check:** (1) For `Phase-1-Amendments.md`, list body lines that name an OQ marked "Settled" in the §8 table together with an open word. It must print nothing: `F=docs/Phase-1-Amendments.md; for n in $(grep -oE '^\| OQ-[0-9]+ \|.*Settled' $F | grep -oE '^\| OQ-[0-9]+' | grep -oE '[0-9]+'); do grep -nE "OQ-$n\b" $F | grep -vE "^[0-9]+:\| OQ-$n \|" | grep -iE "not settled|not picked|waits? on|none yet|confirm|still open|left open"; done`. Read each hit: a line that is only history ("was OQ-n") passes. (2) Each build doc's status line names the §20 range up to the latest letter, or says why the later letters do not bear on it. (3) Review: each §20 item recorded since the doc's last edit is either carried, with its letter cited, or stated as not bearing on the doc.
- **Updated 2026-10-31 (r7):** the word list in (1) also takes `not ruled`, `open from`, `left open` and `open:`. r7 found `Phase-1-Amendments.md:484` ("is not ruled (OQ-32)") and `:572` ("Open from DDD: OQ-31, OQ-32"), which the r6 list missed. Run (1) also on `Phase-1-Proposal.md` and on `Screen-Inventory.md` outside its Open questions section. Added (4): where an OQ answer, in any doc, says a ruling is handled on a named screen or section, that screen's table or that section carries it. r7 found `Screen-Inventory.md:711` ("handled the same way on S-12 (Spec §20 HHH)") with nothing on S-12
- **Updated 2026-10-31 (r8):** added (5): a ruling recorded as an accepted residual or "no build change" is still checked under (3) against every screen whose behaviour its words state. r8 found FS §20 PPP ("that note step then ends early") recorded only in two OQ cells, with S-12 listing no such end. Added (6): after any edit to FS §20, every `Spec:` and `FS:` line citation in the build docs that points at or after the edit is re-checked by the editor, not only by the doc's owner. r8 found `Screen-Inventory.md:577` citing Spec:350 for export, which since PPP is a ruling line
- **Updated 2026-10-31 (r10):** (4) also covers a body line, in any build doc, that assigns a behaviour to a named screen ("S-12 sends …", "the screen row is ux's"). That screen's rows carry the behaviour with every trigger the line names. r10 found `Phase-1-Amendments.md:566` and OQ-39 `:954` ("S-12 sends it on skip and on leaving capture"), while S-12 (`Screen-Inventory.md:340` end (3), `:348`) sends it on skip only. (3) is run per doc against the order of commits: a ruling recorded after a doc's last edit (here AAAA, BBBB after `Screen-Inventory.md`'s b89299a) is either carried there or stated as not bearing

### R-168
- **Statement:** No screen state holds anything that its own "must never show" column, or another state of the same screen, bans. Where two rulings force a state to do both, the build stops and the conflict goes to the user; neither side is built by choice.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:30 ("When two docs disagree, do not pick"); CL:24 (strictest reading); R-134, R-165. Found by r7 (`Screen-Inventory.md:94` holds "no note offer (no S-12)" and bans "Any sign that this press gave no photo", while `:87` sends every accepted press to S-12; G-24)
- **How to check:** For each screen in `Screen-Inventory.md`, read each state's "Holds" against the same row's "Must never show" and against the screen's "Leads to" line and its other states. Any element that is both required and banned, or whose absence is itself something banned, fails until the user rules.
- **Decided 2026-10-31 (FS §20 JJJ, `FS:343`):** the r7 case is settled: DDD wins, the note offer is shown after a lost press, and a note written for it is discarded. `Screen-Inventory.md:94` and `:341` now hold it, and the missing offer is in `:94`'s never-list

### R-171
- **Statement:** Every answer the server can give to a capture or note press, and every way the note step can end, has a screen row saying what the user sees. No answer reaches a screen that has no row for it.
- **Type:** review · **Applies to:** UI, API
- **Source:** CL:17–24 (rule zero: a builder never picks a behaviour); FS §20 PPP (`FS:350`), NNN, III, JJJ, K; R-165, R-168. Found by r8 V2
- **How to check:** List the route's answers from `Phase-1-Amendments.md` §6 (press: accepted, refused; note press: saved, closed, and the no-entry case answered as closed) and the note step's ends (page taken, skip, leaving capture, 15 minutes, a page lost twice, the handles lost on restart under PPP). Match each to a row of S-02 or S-12. An answer or end with no row fails, until ux writes the row or the user rules. A row must not show anything its own never-list or R-160, R-170 bans.
- **Updated 2026-10-31 (r9; FS §20 RRR, UUU, VVV, WWW):** the ends are now decided: a page taken ends with no confirmation (VVV); a skip ends the step for good (WWW, no longer a strictest reading of C4); at 15 minutes nothing changes on its own and the next note press is simply not taken (UUU); a "closed" answer for any reason looks like the window having ended (RRR). The list gains the skip request (R-173) and the note step's `refused` inside the window, which no route answer covers yet (G-26)
- **Decided 2026-10-31 (FS §20 YYY, BBBB, `FS:361`, `FS:364`):** the ends list gains (7), the journey's unlock, which looks exactly like (4). The note step's `refused` inside a window the route read as open is answered with the one `closed` (BBBB (b)), so G-26 (b) is closed. Still open under this check: a press at or after unlock is answered `refused` (`Phase-1-Amendments.md:574`), and S-02's only refusal row is "no frame, or the highlight's quota reached" while its `unlock-day` row is "Not available"; and S-12 end (7) leads to a camera that is not available (G-27)

### R-172
- **Statement:** A dated record is appended to, never rewritten. A revision-log row, an OQ arrow, an "applied" row, a status-log line or an evidence block keeps the words it had on its date; a later ruling is added as a new line, never substituted into the old one.
- **Type:** auto (diff scan) and review · **Applies to:** docs
- **Source:** CL:30 (cite both lines, do not pick); R-134, R-165. Found by r8 N5 (evidence edited in place, disclosed) and r9 V3 (`Phase-1-Amendments.md:795`, lead-tech's tenth-round row, changed from "Q–RRR" to "Q–VVV" and then "Q–XXX" by the supervisor; `Screen-Inventory.md:718`, OQ-49's "Not picked" arrow, changed from "keep `PROVISIONAL: C7`" to "keep Spec §20 XXX", so it now says a decided label is not picked and still open)
- **How to check:** (1) `git diff <last audit>..HEAD -- docs` and list every removed line (`^-`) that sits in a revision log, an OQ arrow (`→`), an §7 "Applied" row, a `Status.md` log line or a fenced evidence block. Each must be either a typo fix that changes no fact, or disclosed in the same line as a correction with its date. (2) Review: a blanket label replacement (for example every `PROVISIONAL: Cn` to `Spec §20 X`) touches state rows only, never history lines.

### R-174
- **Statement:** A ruling's general words are carried only together with the thing it rules. A line that bars writes after unlock bars the photo and the note, never a reveal write: tags, chapters, feelings, visibility, reflections and the overview are still added to an unlocked journey.
- **Type:** review (docs, schema) and auto (schema test) · **Applies to:** docs, data
- **Source:** FS §20 YYY (`FS:361`: "Nothing is added to a journey once it unlocks"), against the reveal (`CLAUDE.md:103`; FS §20 A); CL:30 (do not pick between two lines). Found by r10 (N3): the phrase is repeated as a reason at `Screen-Inventory.md:340` end (7) and `:346`
- **How to check:** (1) Grep the build docs and code comments for "nothing is added", "once it unlocks" and "after unlock": each hit names the photo or the note, or sits in a sentence about them. (2) Schema test: after unlock and before the reveal is finished, every reveal write the reveal allows succeeds as the owner; only `capture()`, `add_note()` and the `note` trigger refuse on `unlocks_at`. A trigger that refuses any insert under an unlocked journey fails

### R-176
- **Statement:** A doc's description of what a viewer sees holds only what that viewer's screen may show. A fixture fact that the screen must never show (a photo count, a month number, a total of tags, a private photo's existence, a past ring) is never written as something the viewer sees, and a table that carries such facts says plainly that they are for the reader of the doc and appear on no screen.
- **Type:** review · **Applies to:** docs, copy
- **Source:** CL:73–74, R-006, R-012, R-098, R-139, R-147, DN C8. The precedent is `Screen-Inventory.md:537` ("This table is for the reader of this inventory. The panel shows none of it"). Found by `docs/reviews/2026-11-04-rules-flows.md` V1, V2 and V4 (`Flows.md:133`, `:137`, `:140`)
- **How to check:** Find every table column or sentence that says what a person sees, tries or gets when viewing as a named user. Run the R-006 (a) and R-139 grep aids over it, then read each line as that viewer in the screen's own "must never show" column. A hit fails unless the line states that the fact appears on no screen. A sealed journey's or another person's fact listed as something "you see" fails
- **Updated 2026-11-04 (r2 of the same audit, V1):** the statement's "appear on no screen" covers only facts no screen may show. A blanket "never on any screen" over a column that also holds facts a screen does show, or that a ruling lets a viewer read, is false and fails: `Flows.md:151` covers `:160` (B11's named announcement) and `:164` (FS §20 SS). The first wording of this check invited that reading. Each row of such a column is read against its viewer

- **Updated 2026-11-09 (`docs/reviews/2026-11-09-rules-friend-screens.md` V2):** a prototype table's "On screen" cell is checked against the fixture's derived state at that clock point (`Phase-1-Amendments.md` §13.1, §13.5 and the Q-F queries), including what a scripted act leaves untouched. A cell that says a list is empty, or that something is gone, when the fixture still holds a row for that viewer, fails. Found at `Flows.md:181`: after 2026-11-14 Second Wind's requests list still holds her outgoing request to Long Way Round (fr-10; Q-F12)
### R-177
- **Statement:** An ID a doc introduces is declared as new in that doc and cannot be misread as an ID from another family. No doc mints an ID that differs from an existing one by punctuation alone, and none calls its own new IDs "existing".
- **Type:** auto (scan) and review · **Applies to:** docs
- **Source:** L-002 (every cross-reference matches); CL:21–23 and R-149 (a `PROVISIONAL:` ID must be findable); R-150. Found by `docs/reviews/2026-11-04-rules-flows.md` V11: `Flows.md:685–699` mints C-1 to C-13 beside Decisions-Needed C1 to C18, and `Flows.md:649` calls them existing
- **How to check:** For a doc `F`: `grep -oE '\b[A-Z]{1,3}-[0-9]+\b' F | sort -u`, strip the hyphen from each, and compare with the IDs in `docs/Decisions-Needed.md`. Any match fails (R-nnn and G-n are the rubric's own and match nothing there). Review: every new prefix is named as new in `F`, and `grep -rlE '\b<prefix>-[0-9]+\b' docs` shows no earlier owner
- **Updated 2026-11-05 (`docs/reviews/2026-11-05-rules-art-microcopy-r2.md` COPY-R2-3):** the check also covers IDs a doc *cites* from another doc. Once a doc renames an ID family, every other doc citing the old IDs fails until it is updated, because the old ID now points at nothing, or at a Decisions-Needed ID. Found at `Microcopy.md:5`, `:211–216`, still citing Flows C-n after `Flows.md` renamed them DC-n. Run the scan above on every doc that cites the renamed doc

### R-178
- **Statement:** A word that marks something as undecided ("for now", "still being compared", "the plan is") is never attached to a banned-list rule or a §20 ruling, even where a provisional default's row repeats that rule. A reader never learns from such a word that a banned thing might yet appear, or that a decided thing might yet change.
- **Type:** review · **Applies to:** docs, copy
- **Source:** CL:24 (a default may never break the banned list), this rubric's "How the rubric grows" (no default may weaken a banned-list check), R-165, R-038, P1:49. Found by `docs/reviews/2026-11-04-rules-flows-r2.md` V2 and V3 (`Flows.md:21`, `:25`), both made while fixing the missing labels of r1 V5
- **How to check:** Grep the doc for its undecided words. For each hit, name what is marked as undecided. It fails if that thing is on the banned list (`CLAUDE.md:64–74`), is checked by `P1` §2.5, or is ruled in FS §20. The default's own label on the same fact is not a defence: label the open part only

### R-179
- **Statement:** No position, length or scale in a drawing shown to a public reader is computed from a journey date that reader may not read. Nothing a public viewer can see appears or disappears at reveal finished, other than the paths named in FS §20 ZZ.
- **Type:** review, then auto · **Applies to:** UI, API
- **Area:** 5. Visibility and access
- **Source:** R-152, R-162, FS §20 T, ZZ, EEE. Found as ART-1 (`Art-Direction.md:137`, `:158`, `:180`). Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-1, numbered by the supervisor 2026-11-05
- **How to check:** For each drawing a public viewer receives, take one element the viewer can date from a field they can read, and try to recover the commit or unlock date from its position. Any success fails. The reader behind the drawing returns no day index or commit date to a public viewer.

### R-180
- **Statement:** A deliverable holds no buildable interim behaviour outside `Decisions-Needed.md`. A doc-local question ID (AD-n, Q-n, FQ-n, DC-n) may raise a question, but may not carry a state the build draws, because no valid code label can name it (R-149).
- **Type:** review · **Applies to:** docs
- **Area:** 13. Across every area
- **Source:** Rule zero (CL:19–24), R-134, R-149, R-150. Found as ART-3 (`Art-Direction.md` §12). Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-2, numbered by the supervisor 2026-11-05
- **How to check:** List every "until answered", "for now" and "drawn as" cell. Each one names a Decisions-Needed ID, or is blank, or says the build stops there.
- **Updated 2026-11-05 (`docs/reviews/2026-11-05-rules-art-microcopy-r2.md` ART-R2-2, ART-R2-4):** (1) a table cell that names only an AD-n (or other doc-local ID) whose Decisions-Needed row exists fails: the builder reads the cell, so the cell carries the `PROVISIONAL:` label. (2) "follows one side until the user rules", where the two sides are a raised conflict and no Decisions-Needed row covers it, is a buildable interim state and fails, as R-135 does. Found at `Art-Direction.md:218–223`, `:247` and `:364`

### R-181
- **Statement:** An art-direction or taste label (such as `[AD]`) covers colour, type, geometry and texture only. A line under it saying who sees something, on which screen, when it appears or disappears, or what a press does is a behaviour and goes to the open questions.
- **Type:** review · **Applies to:** docs
- **Area:** 13. Across every area
- **Source:** R-134, CL:17. Found as ART-4. Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-3, numbered by the supervisor 2026-11-05
- **How to check:** Read every `[AD]` line against that list. Any line that decides visibility, placement on a screen, timing or a press fails.

### R-182
- **Statement:** Strings that can show in the same screen state do not contradict each other, and a string's "where it sits" note agrees with the states it shows in.
- **Type:** review · **Applies to:** copy
- **Area:** 12. Copy and tone
- **Source:** R-168, R-134, SI:94, FS §20 U, QQQ. Found as COPY-2 (`Microcopy.md:60–61`). Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-4, numbered by the supervisor 2026-11-05
- **How to check:** For each screen state in `Screen-Inventory.md`, list every string the copy file places there and read them together.

### R-183
- **Statement:** A line is true in every state that reaches it: the bug paths (lost press, lost page), both settings of every switchable default it touches, and the clock at +5 years. A line about a sealed year says nothing about its contents, including reassurance that is the same for everyone.
- **Type:** review · **Applies to:** copy
- **Area:** 12. Copy and tone
- **Source:** R-009, B19, FS §20 DDD, HHH, R-141, R-143. Found as COPY-3, COPY-7. Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-5, numbered by the supervisor 2026-11-05
- **How to check:** Run each weighted line against First Light at +5 years under B4's option, a lost press, a lost page, and a journey with no photos. Grep aid on S-03 copy: `missing`, `safe`, `kept`, `waiting`, `nothing has gone wrong`.

### R-184
- **Statement:** A type's cadence, yearly photos and highlight numbers appear on S-01 only, and on no screen reachable while a journey is sealed.
- **Type:** auto · **Applies to:** copy, UI
- **Area:** 1. Sealing and leaks
- **Source:** R-006, SI:76, SI:78, SI:118. Found in testing M-01 (`Microcopy.md:46`). Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-6, numbered by the supervisor 2026-11-05
- **How to check:** Grep the app's copy for the M-01 strings and fail on any file outside S-01's components. R-006 (a) hits on those strings inside S-01 are expected and pass.

### R-185
- **Statement:** The ring-count states have no user-facing or code-facing names that read as levels, and each "do" in the art rules holds for every value its own formulas allow.
- **Type:** review, then auto · **Applies to:** docs, UI, code
- **Area:** 8. Engagement mechanics
- **Source:** R-102, R-143, MJC:693 ("no tier name"), art-director brief. Found as ART-6 (`Art-Direction.md:193–195`). Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-7, numbered by the supervisor 2026-11-05
- **How to check:** Grep code and fixtures for `established`, `veteran`, `young` as a state name keyed to ring count. Read the art direction's "never read" rules against the worked values at n = 1, 5, 9, 10, 17, 25, 40.

### R-186
- **Statement:** A navigation way exists only where a `Screen-Inventory.md` "Leads to" row names it from that screen, and no way appears, disappears or changes because of content.
- **Type:** review · **Applies to:** docs, UI
- **Area:** 8. Engagement mechanics
- **Source:** R-096, R-134, R-168. Found as ART-8 (`Art-Direction.md:285–296`). Proposed in `docs/reviews/2026-11-04-rules-art-microcopy.md` as P-8, numbered by the supervisor 2026-11-05
- **How to check:** Compare the navigation marks with each screen's "Leads to" row in every state, `no-journey` included. A way appearing on the day a reveal opens is reported under R-096 until the user rules.

### R-187
- **Statement:** Provisional defaults hold when read together. Flipping one switch, with every other default in force, changes only the behaviour that switch names. No default forces the answer to a question that has no default, and none leaves a screen without a way in that its "Reached from" row requires, under any answer to such a question.
- **Type:** review · **Applies to:** docs, UI
- **Area:** 14. Provisional defaults and the options panel
- **Source:** R-141 (a switch changes nothing but its own behaviour), rule zero (CL:19–24: a builder never picks; a question with no default is not answered by another row), R-150, R-168. Found by `docs/reviews/2026-11-05-rules-art-microcopy-r2.md`. ART-R2-1: B41 makes C1's line the only way into Reveal S-04, which forces C18 and can strand an unfinished reveal against `Screen-Inventory.md:151`. ART-R2-3: B28 with B31 removes the owner's activity line under B4's option, so flipping B4 changes B5's behaviour
- **How to check:** (1) For each new or changed Decisions-Needed row, list every other row and every switch setting touching the same screen, drawing or data. For each switch, compare what each screen shows under its two settings with every other default in force: anything that changes beyond the switch's own ID fails. (2) For each row, list the open questions (no default) its behaviour depends on. Read the row under each possible answer. If one answer leaves a screen unreachable that a "Reached from" row requires, or turns the row into a banned mechanic (R-095, R-096), the row has forced that question and fails
- **Updated 2026-11-05 (`docs/reviews/2026-11-05-rules-art-microcopy-r3.md` ART-R3-1):** a default can hold at one clock point and fail in between. Run (1) at more than one clock point: at each scripted fixture event the row touches, at the day after it, and at the next event that completes the behaviour (for example the next anniversary or unlock). Found when revised B28 put a finished journey's day marks on a ring not drawn until the next join anniversary, so from Second Wind's 2027-04-25 finish the line showed nowhere under B4's per-year option and on ring n+1 under the default


### R-188
- **Statement:** Being on someone's map grants nothing. A person on the owner's map who is not the owner's friend reads exactly what a stranger reads, and no read rule, policy or audience consults the map.
- **Type:** auto · **Applies to:** data, API
- **Area:** 5. Visibility and access
- **Source:** FS §20 KKKK (d); CL:74; R-069. Proposed by `Phase-1-Amendments.md` §12.7 as K2 and K10; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** (1) K2: two test users, m on owner o's map and s on no map, neither a friend; at several clock points and under both settings of `b2` and `c6`, the fingerprint of every reader is equal for m and s once the viewer's own `user_rows()` row is masked. Planted fault: a "friend or map member" body. In the fixture: Hands against Wind on Round's content (Q-F7). (2) K10: the R-156 scan on the relation `layer` returns exactly {`finish_reveal`, `layer_rows`}. Not yet run: no database exists on this machine

### R-189
- **Statement:** A declined friend request never shows to its sender. Nothing the sender can read or do differs between a declined request and a pending one, before, during or after any later friendship.
- **Type:** auto · **Applies to:** data, API, UI
- **Area:** 5. Visibility and access
- **Source:** FS §20 KKKK (a); `PROVISIONAL: B44`, `B50`, `B53`. Proposed by `Phase-1-Amendments.md` §12.7 as K3; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** K3's twin run: reader rows, a second send (refused both), a withdrawal (accepted both), `viewer_in_network()` (false both), a crossed request from the decliner (accepted), and the differential catalog test around the decline. Planted faults as listed in K3. UI: the sender's screen for a declined request is the pending screen, byte for byte. Not yet run

### R-190
- **Statement:** A friendship exists only after the recipient of a request accepts it. At most one friendship is current per pair, and no request is open while the pair are friends.
- **Type:** auto · **Applies to:** data, API
- **Area:** 5. Visibility and access
- **Source:** FS §20 KKKK (a); `PROVISIONAL: B53`. Proposed by `Phase-1-Amendments.md` §12.7 as K4; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** K4's cases, including two sessions accepting crossed requests at once (one friendship, one `refused`). Not yet run

### R-191
- **Statement:** Removing a friend takes effect at once and touches nothing else. From the next statement the removed person reads the remover's content as a stranger does. Nobody else's reads change, both maps stay as they were, and no record says who removed whom.
- **Type:** auto · **Applies to:** data, API
- **Area:** 5. Visibility and access
- **Source:** FS §20 KKKK; `PROVISIONAL: B45`, `B48`, `B49`. Proposed by `Phase-1-Amendments.md` §12.7 as K5; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** K5 (Q-F8 in the fixture). Read "no record says who removed whom" exactly: between the two friends the person who did not remove can always tell by elimination. The check is that no stored value and no reader adds to that, and that no third party learns anything. Not yet run

### R-192
- **Statement:** No friend count, request count, friendship limit or friendship time value reaches anyone. The one order a time decides is a viewer's own incoming requests, newest first, keyed on each request's own send instant and nothing else.
- **Type:** auto · **Applies to:** data, API, UI
- **Area:** 8. Engagement mechanics
- **Source:** CL:69 (counters); FS §20 KKKK (c); `PROVISIONAL: B46`, `B51`, `B52`; R-155. Proposed by `Phase-1-Amendments.md` §12.7 as K6; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** K6: reader result types hold no integer, numeric or time-typed column; the `ORDER BY` of `friend_request_rows()` names `friend_request.sent_at` as its only time; planted faults (a returned `sent_at`, a key from another table's time) are caught. UI: no screen prints a number of friends or requests, or a request's time ("2d", "new"). Not yet run

### R-193
- **Statement:** Only the two people involved can read a friendship or a friend request. Only the owner can read their close-friends list. No one can ask for another user's friends.
- **Type:** auto · **Applies to:** data, API, UI
- **Area:** 5. Visibility and access
- **Source:** FS §20 KKKK; `PROVISIONAL: B47`; DN E4 (built: no one can, while open with the user). Proposed by `Phase-1-Amendments.md` §12.7 as K7; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** K7. A signature scan finds no set reader on the six friendship tables that takes an argument. UI: no screen shows another user's friends, mutual friends or close friends. Not yet run

### R-194
- **Statement:** The friend requests list carries no marker. The way to it looks the same whether no request or many are waiting, and a request arriving changes nothing outside that list's rows.
- **Type:** review, then auto · **Applies to:** UI, copy
- **Area:** 8. Engagement mechanics
- **Source:** FS §20 KKKK (c) ("no notification"); CL:69–70; R-095, R-096, R-186; `PROVISIONAL: B43`; rule zero step 5 (the banned list wins over the Instagram reference). The reference product shows its requests entry only while requests wait. Found by `docs/reviews/2026-11-09-rules-kkkk.md` V4
- **How to check:** Render every screen that leads to the requests list, as a viewer with 0 and with 3 incoming requests: identical DOM apart from the list's own rows. No "Requests" entry, line or section appears only when one waits, and none takes bold, a dot, a number or new copy. Grep aid: `pending`, `request` near conditional rendering

- **Updated 2026-11-09, second pass (`PROVISIONAL: B48` changed to event time; `docs/reviews/2026-11-09-rules-kkkk-r2.md`):** `Phase-1-Amendments.md` §12.7 K14 tests the "looks the same" half. Two more halves are part of this check: (1) the way in is **present** in every state, so a render with 0 requests must contain it (a way drawn nowhere also passes K14's comparison); (2) inside the list, a request seen before and one not yet seen render the same: no read state, "new" divider or bold unseen row (R-096). The way must also be named in `Screen-Inventory.md` S-05's "Leads to" before it is built (R-186)
### R-195
- **Statement:** Friendship records are append-only, and every time they hold comes from the app clock at the moment of the act.
- **Type:** auto · **Applies to:** data
- **Area:** 2. Immutability and append-only
- **Source:** FS §20 KKKK; FS §20 OOO (the same pattern as `joined_at`); R-164. Proposed by `Phase-1-Amendments.md` §12.7 as K12, with §2.5 check 1's six tables; numbered by `docs/reviews/2026-11-09-rules-kkkk.md`
- **How to check:** As R-164 (a) to (c): UPDATE, DELETE and TRUNCATE on each of the six tables raise an error as the product role, through a planted definer function and as the table owner. An insert with a time other than `app_now()` is refused. Not yet run

### R-196
- **Statement:** An "Instagram reference" default (CLAUDE.md rule zero step 5) settles only a generic app question. A row that decides who reads My Journey's own objects (announcements, journeys, photos, reflections, layers, close friends' access), or that reopens or reads a §20 ruling, goes to the user, however the reference product behaves.
- **Type:** review · **Applies to:** docs
- **Area:** 14. Provisional defaults and the options panel
- **Source:** CL rule zero step 5 ("Questions about what makes My Journey itself, such as … layers, visibility … go to the user"); R-150, R-187. Found by `docs/reviews/2026-11-09-rules-kkkk.md` V1 (`PROVISIONAL: B48` decides that a new friend reads the whole earlier announcement history, a visibility question)
- **How to check:** For each row marked "Instagram reference", name what it decides. It fails if it sets an audience, a reader, a visibility or what a layer or close friend gets, or if it rests on a reading of a §20 ruling. Such a row needs a user answer, or a strictest-reading default under steps 1 to 4, labelled as such


### R-197
- **Statement:** An announcement reaches a viewer other than the actor only through a current friendship with the actor that began strictly before the event. A later friend never receives earlier announcements, a removed friend stops receiving them, and a friendship that ends and starts again counts from its new start. Who received an announcement is stored nowhere, and no reader tells anyone when anyone else's friendship began.
- **Type:** auto · **Applies to:** data, API
- **Area:** 7. Feed and notifications
- **Source:** FS §20 J, M, UU, KKKK (e); `PROVISIONAL: B48` (strictest reading, raised to the user as DN E3 (c)); R-196. Proposed by `Phase-1-Amendments.md` §12.7 as K13; numbered by `docs/reviews/2026-11-09-rules-kkkk-r2.md`
- **How to check:** K13's oracle against every viewer's `announcement_rows()` at several clock points, with its scratch case (finish, accept, finish, remove, re-friend, finish), the same-instant tie (not received), and its planted faults (read time, "a friend at the event" without the current friendship, "ever friends at the event and friends now", `<=`). A catalog and result scan finds no recipient list and no time-typed column in `announcement_rows()` other than `at`. In the fixture: 13 / 9 / 5 / 2 / 0 at baseline (Q-F9). Under `c6 = shown` a later friend can still read the person tags on older photos, which B48 does not cover; that is DN E3 (b), not a failure of this check. Not yet run

### R-208
- **Statement:** Who receives each announcement type is stated once, in words, and every doc that states it agrees; a ruling that settles an audience never does so by pointing at a column of an older table. Every fixture count that depends on an audience is recomputed when the audience changes, and names the reading it assumes.
- **Type:** review · **Applies to:** data, copy
- **Area:** 13. Across every area
- **Source:** FS §20 J, M, UU, KKKK (e), NNNN; R-146, R-197. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V4 (`Phase-1-Amendments.md:1739`, `:2081` say "the subject left out" is built; §14.1, SI S-08, Flows Flow 7 and §13.4.1's counts say the subject is included)
- **How to check:** For "path crossed", "journey launched" and "reflection left", grep every doc for its audience and list each statement; they must agree. Recompute §13.4.1's per-viewer counts from the stated audience (13 / 9 / 5 / 2 / 0 with the subject included; 8 / 6 / 4 / 2 / 0 with the subject left out).

### R-209
- **Statement:** A carriage that adds a function, table or reader to the model in the same change updates every closed list a rubric check holds of the functions allowed to touch that data (R-138, R-156, R-202, §4 item 1), or the change fails.
- **Type:** auto · **Applies to:** data
- **Area:** 13. Across every area
- **Source:** R-138, R-156; `Phase-1-Amendments.md` §4 item 1 (`:336`), §16.2. Found by `docs/reviews/2026-11-10-rules-supervisor-carriage.md` V7 (`dismiss_highlight()` and `highlight_dismissal` added; no list updated)
- **How to check:** For each new function named in an Amendments section, grep R-138, R-156, R-202 and §4 item 1: it is in each list it belongs to, or the section says why not.

---

## 14. Provisional defaults and the options panel

Added 2026-10-27 for the playable prototype (rule zero, CL:19–24; `Decisions-Needed.md` "Provisional defaults in force"). Seven defaults were switchable: B2, B4, B5, B9 (a), B11, B12, C6. **2026-10-30:** B9 (a) decided as text only (FS §20 Q); six remain. **2026-11-10:** B11, B12 and C6 decided (FS §20 NNNN: unnamed, hidden, hidden); three remain, B2, B4, B5. R-146 to R-148 now check one fixed setting each. Each switch must keep the banned list under **both** of its settings, so the user can compare them without the comparison itself breaking a rule.

### R-141
- **Statement:** The prototype options panel holds only the time control, the viewer switcher with the simulated date, and the six switchable defaults (B2, B4, B5, B11, B12, C6; B9 (a) was decided 2026-10-30, FS §20 Q, and has no switch; before 2026-10-30 this read "seven"). Each switch offers exactly its two documented settings, starts on the provisional default, and changes nothing but the behaviour its ID names.
- **Type:** auto · **Applies to:** UI, API
- **Source:** CL:23, DN "Provisional defaults in force" (Switchable column), DN C16, CL:24
- **How to check:** List the panel's controls from the DOM and from code. Compare with the Switchable column: no extra switch, none missing, and no setting beyond the two listed (no "both", "auto" or free value). On first load each switch is on the first-listed setting, which is the default. Flip each switch alone and diff every read endpoint for every fixture user: only the behaviour named by that ID changes (R-142 to R-148). The panel is itself a data path under R-014: it shows no count, photo or field from a sealed journey, and the viewer switcher lists fixture users by name only, with no picture (C7).
- **Decided 2026-10-30 (FS §20 Z):** the switches live in one `prototype_option` row, changed only through `set_option()`; each column allows exactly its two settings (current implementation)
- **Provisional default:** Decisions-Needed B20: The clock jumps also include +1 minute and +1 hour. They are the only additions to the time control; any other size, or a free date field, fails
- **Provisional default:** Decisions-Needed B23: Option switches are one global setting, not per viewer. Switching the viewer in the panel changes no switch
- **Provisional default:** Decisions-Needed B22: Reset puts every option switch back to its default (R-117)
- **Decided 2026-10-30 (FS §20 EE, `FS:309`):** only the panel moves time or flips switches. `clock_jump()`, the jump to the next unlock and `set_option()` are callable by a separate panel role, never by the acting viewer (R-153)
- **Updated 2026-11-10 (FS §20 NNNN):** the panel holds **three** switches, B2, B4 and B5. A switch for B11, B12 or C6 fails

### R-142
- **Statement:** B2, under both settings ("from unlock" / "only after reveal finished"): nothing from a sealed journey is readable by anyone. The setting changes only who besides the owner may read an unlocked journey whose reveal is not finished: under "from unlock", the network reads photos not set Private and anyone signed in reads photos already set Public (B3, B14); under "only after reveal finished", no one but the owner reads any of it, Public photos included (**decided 2026-10-30, FS §20 R**). Before 2026-10-30 the statement read: "B2, under both settings ("from unlock" / "only after reveal finished"): nothing from a sealed journey is readable by anyone, and the setting changes only when the owner's network may read an unlocked journey's Network-default photos."
- **Type:** auto · **Applies to:** data, API
- **Source:** DN B2, FS §20 R, FS:151, FS:269, P1:318, CL:73 (nothing leaks), CL:24
- **How to check:** Under each setting: R-001 to R-008 pass for Lantern #6 at 2026-12-31 23:59:59. As Open Hands at baseline, read a Long Way Round #4 photo (reveal never finished): "from unlock" allowed, "only after reveal finished" refused. In a test copy, set one Long Way Round #4 photo Public (B3: takes effect when made) and read it as Open Hands and as First Light: "from unlock" allowed to both, "only after reveal finished" refused to both (FS §20 R); the owner reads it under both. This is a test-copy change, not a fixture change: the approved fixtures (P1 §3) are not edited, and a standing fixture for this case goes to the supervisor. Every Lantern #5 cell of the §3.6 matrix (reveal finished) is identical under both settings (R-068).
- **Decided 2026-10-30 (FS §20 X):** "no one but the owner reads any of it" covers photos and what follows them (reflections, notes, people tags). The journey's type, dates, chapter and feeling tags are read by the network from unlock under both settings, and never by a public reader (FS §20 T, R-152). Add the case: under "only after reveal finished", as Open Hands at baseline, read Long Way Round #4's type and dates: allowed; read any #4 photo: refused
- **Decided 2026-10-30 (FS §20 HH, `FS:312`):** "what follows them" includes the journey overview. Under "only after reveal finished" the network reads the overview only once the reveal is finished (R-063)

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** the Open Hands cases are stale: Hands is not Round's friend, so she is refused Round #4 under both settings. Use Steady Lantern (fr-4): under "from unlock", allowed; under "only after reveal finished", refused. In the test-copy Public case, First Light and Hands are both public readers. The FS §20 X case likewise moves to Lantern: as Lantern at baseline under "only after reveal finished", Round #4's type and dates allowed, any #4 photo refused. Hands now reads neither
### R-143
- **Statement:** B4, under both settings ("per finished reveal" / "per year with the app"): the circle is a record, not a rank, and nothing on it fills, grows or advances during a sealed year.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** DN B4, P1:65, FS:185, CL:69, CL:71, CL:111
- **How to check:** Render Long Way Round's profile at baseline under each setting: "per finished reveal" shows no ring for #4. Under both, R-102 and R-012 pass: Steady Lantern's circle renders the same DOM at 2026-02-01, 2026-07-01 and 2026-12-31; no ring count is printed; no copy treats more rings as better. Under "per year with the app" the docs do not say on which date a year's ring appears. If the build needs that, it goes to the supervisor (rule zero); a ring that appears, fills or changes inside a sealed year fails R-012.

### R-144
- **Statement:** B5, under both settings ("owner only" / "built from the photos the viewer can see"): the activity graph shows nothing from a sealed journey, no viewer learns when a photo they cannot read was captured, and the graph prints no count.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** DN B5, DN B8, FS:145, FS:187, P1:50, CL:73
- **How to check:** Under each setting R-011 passes, and the line twists into the circle only at reveal finished (none for Long Way Round #4). "Owner only": as Second Wind, request activity data for Lantern #5: none returned, no graph rendered. "Built from the photos the viewer can see": as Second Wind, the Lantern #5 graph equals one built from only the #5 photos Wind can read; changing a private photo's `captured_at` in a test copy leaves Wind's API response byte-identical. Under both, no axis label, tooltip or caption prints a number of photos (R-099 under B8).
- **Updated 2026-11-10 (DN B80, B79):** B5's default is now "built from the photos the viewer can see", shown as sparks on a closed timeline; a journey under way is one plain line with no mark (B79). Check under both settings as before, plus: a public viewer gets no line (B36), and the under-way line is byte-identical on 2026-02-01, 2026-07-01 and 2026-12-31 for Lantern #6 (R-012)

### R-145
- **Statement:** The Positivity Feed is text only (**decided 2026-10-30, FS §20 Q**): each entry is a reflection's text, no photograph appears in the list, and opening one entry shows that one photo. B9 (a) has no switch. The announcement feed shows no image (R-086), and the Positivity Feed meets B9 (b)–(f). Before 2026-10-30 the statement read: "B9 (a), under both settings ("text only" / "with photographs"): the announcement feed shows no image, and the Positivity Feed meets B9 (b)–(f). The "with photographs" setting is reported as a finding against "No photo feed" until the user rules on G-8."
- **Type:** auto · **Applies to:** UI, API
- **Source:** FS §20 Q, DN B9, CL:72 ("No photo feed ... never images"), FS:171, FS:202–204, CL:24. See G-8
- **How to check:** R-086 passes on the announcement feed, and the R-103 cases pass. The Positivity Feed DOM has no `img`, `picture`, `canvas`, `video` or background image before an entry is opened, and its list endpoint returns no image URL or media field; opening one entry shows that one photo. From that opened photo there is no next, previous or swipe control that steps to another feed entry's photo: stepping photo to photo through the feed's results is a photo feed shown one image at a time (strictest reading of FS §20 Q with CL:72, CL:24; added 2026-10-30 by `docs/reviews/2026-10-30-rules-screen-inventory-r3.md` N20). The options panel has no B9 control (R-141). Any photograph in the feed list, or a setting that adds one, is a violation of CL:72 and FS §20 Q, not a finding awaiting the user. Before 2026-10-30 this check ran under both settings and reported "with photographs" as a finding against CL:72 until the user decided G-8.

### R-146
- **Statement:** B11, under both settings ("named" / "unnamed"): a "path crossed" announcement reaches only the owner's network, and never says which ring, how many photos, or anything that orders or ranks.
- **Type:** auto · **Applies to:** data, API, UI, copy
- **Source:** DN B11, FS:164, FS:282 (§20 M), P1:168, CL:74
- **How to check:** Jump from baseline to 2027-05-01 (Second Wind finishes #6 on 2027-04-25, tagging Lantern). "Named": the announcement names Wind and Lantern. "Unnamed": it names Wind only, and the payload sent to readers has no subject. Under both: the recipients equal Wind's map members (R-089); the text has no digits and no ring words (R-092); Lantern's own view of it says nothing about Lantern's ring, closeness or count (R-071).

- **Updated 2026-11-09 (FS §20 KKKK, `FS:378`; `docs/reviews/2026-11-09-rules-kkkk.md`):** "recipients equal Wind's map members" now reads "Wind's current friends at read time". At 2027-05-01 those are Steady Lantern and Open Hands, who became friends on 2026-11-14 by script (`Phase-1-Amendments.md` §13.5)
- **Updated 2026-11-09, second pass (`PROVISIONAL: B48` changed to event time; `docs/reviews/2026-11-09-rules-kkkk-r2.md`):** "Wind's current friends at read time" now reads "Wind's current friends whose friendship began before the event". At 2027-05-01 these are still Steady Lantern and Open Hands, since the 2026-11-14 accept predates the 2027-04-25 finish
- **Updated 2026-11-10 (FS §20 NNNN (a)):** no longer a switch. Check "unnamed" only: at 2027-05-01 the "path crossed" line names Wind only, and no field of the payload sent to Lantern or Hands carries a subject. A "named" line anywhere fails
- **Updated 2026-11-10 (`docs/reviews/2026-11-10-rules-supervisor-carriage.md` V4):** the docs disagree on whether the person crossed receives the unnamed line (`Phase-1-Amendments.md:1739`, `:2081` against §14.1, SI S-08, Flows Flow 7). This check runs on the "subject included" reading that §14.1 and the fixture counts use, and reports the residual: in §13.4.3, Lantern #1 and #2's crossings reach Wind alone, who can read 4 of the 6 photos of her, so one unnamed line at the finish lets her tell she is on Lantern's rings. For the user (R-208)
- **Updated 2026-11-10 (DN B83):** the person crossed never receives the line. At 2027-05-01, Lantern receives nothing about Wind #6's crossing of her; Hands receives the unnamed line

### R-147
- **Statement:** B12, under both settings ("shown" / "hidden"): Walking a path never gives a reader a total, grouping or ordering of the photos they appear in, and never shows a photo the reader cannot otherwise read.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** DN B12, FS:196, FS:164, CL:74, P1:51. See R-139 and G-12
- **How to check:** As Second Wind on Lantern #1 (Wind tagged in 6, 2 of them private). "Shown": only the tagged photos Wind can read appear (not the 2 private ones, R-065), in journey order, with no count, total, "n of", pagination total or grouping in the DOM, and no count field in the API response. "Hidden": no "where you appear" view, route or response field exists for a reader. Under both, R-139 passes. Every audit of "shown" reports R-139's residual risk (a reader can count by scrolling) as its weakest point.
- **Updated 2026-11-10 (FS §20 NNNN (b)):** no longer a switch. Check "hidden" only: no "where you appear" view, route, mark or response field exists for any reader. The residual risk under "shown" is gone

### R-148
- **Statement:** C6, under both settings ("hidden" / "shown"): no reader can total, group or rank how often a person is tagged, and no tag on a photo the reader cannot read is revealed.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** DN C6, FS:164, FS:277, CL:74, CL:24. See R-139
- **How to check:** As Open Hands on Lantern #1. "Hidden": no person tag appears in any screen or API response for a photo Hands does not own; under the strictest reading (CL:24) it is absent from the data sent, not only from the UI. "Shown": person tags appear only on the single photo they belong to; no journey-level list, count, grouping or ordering by person (R-139); tags on photos Hands cannot read are absent. C6's question also asks whether a tag leads to that person's profile. No default answers that, so a tag that links to a profile is a finding until the supervisor answers (R-134).
- **Updated 2026-11-10 (FS §20 NNNN (b)):** no longer a switch. Check "hidden" only, for every non-owner and every photo, Public included: no person tag in any screen or API response. The profile-link question is gone

### R-149
- **Statement:** Every `PROVISIONAL:` label in the code names an ID in the "Provisional defaults in force" table of `Decisions-Needed.md`, and each switch on the options panel carries the label of its own switchable ID.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** CL:22–23, DN "Provisional defaults in force" ("Every default is labelled in code as `PROVISIONAL: <ID>`")
- **How to check:** From the repo root (flags written inline; zsh does not split a variable into flags). Labels in prose are excluded: `CLAUDE.md:23` itself holds an example label.
  1. Malformed or non-default labels (for example `PROVISIONAL: A3`, `PROVISIONAL B2`). Must print nothing:
     `grep -rnE --exclude='*.md' --exclude-dir=docs --exclude-dir=graphify-out --exclude-dir=node_modules --exclude-dir=.claude --exclude-dir=.git 'PROVISIONAL' . | grep -vE 'PROVISIONAL: (Decisions-Needed )?[BC][0-9]{1,2}[a-f]?([^0-9A-Za-z]|$)'`
  2. IDs not in the table. Must print nothing:
     `comm -23 <(grep -rhoE --exclude='*.md' --exclude-dir=docs --exclude-dir=graphify-out --exclude-dir=node_modules --exclude-dir=.claude --exclude-dir=.git 'PROVISIONAL: (Decisions-Needed )?[BC][0-9]{1,2}' . | grep -oE '[BC][0-9]{1,2}$' | sort -u) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]{1,2}' | sort -u)`
  3. Switchable IDs from the table, to compare with the IDs labelled in the options-panel code. The two sets must be equal:
     `grep -E '^\| [BC][0-9]{1,2} \|.*\| \*\*yes\*\*' docs/Decisions-Needed.md | grep -oE '^\| [BC][0-9]{1,2}' | grep -oE '[BC][0-9]+'` (today: B2 B4 B5 B9 B11 B12 C6)

  A table ID with no label in code is not a failure: some defaults are an absence (B15, C15). `B9a`–`B9f` match row B9. Tested 2026-10-27 on a sample file: step 1 caught `A3` and `PROVISIONAL B2`, step 2 caught `B17`. Baseline 2026-10-27: no code labels yet. Review aid, not part of the auto result: for each label, the code beside it does what that table row says.

  Note 2026-10-30: B17 has since been added to the table (fdb83d3), so the sample above no longer shows a missing ID. A fresh sample should use an ID past the table's last row.
- **Updated 2026-11-10 (FS §20 NNNN):** today's grep lists B2 B4 B5 B9; B9 (a) has no switch (FS §20 Q), so three switches. B11, B12 and C6 labels may stay in code only as `// Spec §20 NNNN` references, never on a switch

### R-150
- **Statement:** A deliverable (doc or code) describes every question that `Decisions-Needed.md` answers with a provisional default under that default only, worded as the table row states it, and labelled `PROVISIONAL: <ID>`. It never calls such a question open or "no default", never states a default range that leaves out rows in the table, never describes the other side or a third reading as what the screen holds, and never extends a default or a switch setting to cases its row does not name.
- **Type:** auto (labels and cross-references) and review (wording) · **Applies to:** copy, UI, data, API
- **Source:** CL:19–24 (rule zero: "build that, and nothing else"), CL:30, DN "Provisional defaults in force". R-149 covers labels in code only; R-135 covers picking a side. Found by `docs/reviews/2026-10-30-rules-screen-inventory-r1.md` finding N1 (B17–B19 missing from `Screen-Inventory.md`) and N2 (B2's option extended to Public photos)
- **How to check:** From the repo root, for a deliverable `F`:
  1. Every table ID is labelled in `F` if `F` touches its question. List table IDs not labelled in `F`, then read each against `F`: `comm -13 <(grep -oE 'PROVISIONAL: [BC][0-9]{1,2}' F | grep -oE '[BC][0-9]+' | sort -u) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]+' | sort -u)`
  2. Every row that says "Raised as ... OQ-n" is named in `F`'s OQ-n status line. Must print nothing: `grep -oE '^\| [BC][0-9]+ \|.*Raised as[^|]*' docs/Decisions-Needed.md | while read -r l; do id=$(echo "$l" | grep -oE '^\| [BC][0-9]+' | grep -oE '[BC][0-9]+'); for n in $(echo "$l" | grep -oE 'OQ-[0-9]+' | grep -oE '[0-9]+'); do awk -v n="$n" -v id="$id" '$0 ~ "^"n"\\. "{f=1;next} f && /^[0-9]+\. /{exit} f && index($0,id){ok=1} END{if(!ok) print "OQ-"n" lacks "id}' F; done; done`
  3. Grep `F` for `no default`, `still open, no ID` and `B1–B1[0-9]` ranges, and confirm each against the table.
  4. Review: each labelled passage says what its row says, no more. A reading the row does not state (for example, what a switch setting does to a case the row does not name) is raised as a question, not built.

- **Updated 2026-11-09 (`docs/reviews/2026-11-09-rules-friend-screens.md` V1):** step 2's pattern finds only rows that say "Raised as … OQ-n". Rows added later name their source differently ("added … from Screen-Inventory OQ-55", "settles Screen-Inventory OQ-57 and Flows DC-15"). Step 2 now also takes every Decisions-Needed row matching `from (Screen-Inventory|SI) OQ-[0-9]+` or `settles [^|]*(OQ|DC)-[0-9]+`. For each, the named OQ or DC line in the deliverable that raised it, and every body line that sends a reader to that OQ ("… is OQ-55", "Not set", "not picked"), must name the B-row and describe the screen under it. A deliverable that still calls such a question open, or still says "not set", fails. Run it on both the doc that raised the question and every doc that cites it (here `Screen-Inventory.md` and `Flows.md`)
### R-153
- **Statement:** Only the prototype panel can move the clock or change an option switch. No acting viewer, through any route, function or direct database call, can jump time, jump to the next unlock or flip a switch.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS §20 EE (`FS:309`), FS §20 Z, DN C16, R-141, R-117. Found by `docs/reviews/2026-10-30-rules-phase-1-r5.md` finding V1 (`Phase-1-Amendments.md:55` says `mj_app` holds EXECUTE on `clock_jump()` and calls the question unsettled; `:193` calls `set_option()` EXECUTE unsettled)
- **How to check:** Connected as the viewer role with each fixture user set as the acting viewer, call `clock_jump('1 day')`, the next-unlock jump and `set_option('b2', 'after_reveal_finished')`: each is refused, and `app_now()` and `prototype_option` are unchanged. `has_function_privilege(<viewer role>, <fn>, 'EXECUTE')` is false for all three. No API route reachable from a product screen calls them. As the panel role: each succeeds.
- **Current implementation:** a separate panel role holds EXECUTE on the three functions; the viewer role (`mj_app`) holds none

### R-163
- **Statement:** The fixture loader and the schema tests act as a user only the way a viewer does. They connect as the panel role and switch, one way, to the viewer role for each action. They never write a product row any other way, and the viewer role can never become the panel role.
- **Type:** auto · **Applies to:** data, dependencies
- **Source:** FS §20 II (`FS:313`), EE; R-117, R-120, R-153; P1:40. Proposed by `Phase-1-Amendments.md` §2.4 (lines 183–188). r5 left it unnumbered because II was not yet ruled. Numbered by r6
- **How to check:** (1) The loader and the test harness open connections as the panel role only, never as the table owner or directly as the viewer role. (2) As the panel role without the role switch, calling one product function (for example `finish_reveal`) is refused. (3) The loader's source contains no INSERT, UPDATE, DELETE, COPY or TRUNCATE on a product table. (4) After load, the baseline matches P1 §3: counts per journey, the §3.4 rings and the §3.6 matrix. (5) `pg_auth_members`: the viewer role is not a member of the panel role, and the panel role's membership in the viewer role is non-inheriting. As the viewer role, `SET ROLE` to the panel role is refused.
- **Current implementation:** `GRANT mj_app TO mj_panel WITH INHERIT FALSE, SET TRUE`, and `SET LOCAL ROLE mj_app` for each action (`Phase-1-Amendments.md` §1.4, §1.5, §2.1, §2.2; `P1:195`)

---

## Banned-list coverage

Every row of the banned list (`CLAUDE.md:64–74`, `Master-Prompt.md:37–47`) and the checks that cover it.

| Banned item | Checks |
|---|---|
| No retakes | R-031, R-005, R-018, R-019, R-029, R-124, R-160, R-170, R-173, R-175 |
| No edits to reflections | R-015, R-016, R-124 |
| No comments from anyone else | R-105, R-106, R-107, R-109, R-124 |
| No face recognition | R-110, R-111, R-112 |
| No ads anywhere | R-113 |
| No streaks, counters, progress bars, reminders | R-097, R-098, R-099, R-038, R-039, R-012, R-013, R-095, R-096, R-124, R-138, R-140, R-143, R-144, R-166, R-178, R-192, R-194, R-200, R-204, R-207 |
| No re-engagement notifications | R-094, R-095, R-096, R-194, R-200 |
| No ranking, levels, badges, leaderboards | R-101, R-102, R-103, R-124, R-143, R-166 |
| No photo feed | R-084, R-085, R-086, R-145 |
| Nothing leaks from a sealed year | R-001 to R-014, R-091, R-138, R-142, R-144, R-156, R-157, R-158, R-161, R-167, R-169, R-176, R-178, R-199, R-201, R-205 |
| No layer is ever shown to the person on it | R-069, R-070, R-071, R-092, R-139, R-146, R-147, R-148, R-176, R-188, R-193, R-197, R-202, R-203 |

R-141 and R-149 apply to every row: no switch setting may break any item above, and every provisional default in code is labelled and traceable. R-138 sits under two rows because a control hidden or greyed for lack of frames is both a counter and a leak of how much a sealed year holds (RG:28, "disabled-but-visible states").

R-150 applies to every row as well: a deliverable that leaves out or stretches a provisional default can carry a banned item in by that route.

R-151 to R-154 carry dated rulings (FS §20 DD, T, CC, EE, GG) rather than banned items. R-153 keeps the time control from becoming a way round the seal (R-014); R-154 narrows what a reader can infer from capture times (R-151 residual). R-151 extends the "Nothing leaks" row's intent past unlock for highlights (DN B6: others learn nothing about highlights).

R-155 to R-165 (added 2026-10-31) carry FS §20 II–VV. Three of them sit under banned rows: R-160 under "No retakes" (PP, VV); R-156, R-157 and R-158 under "Nothing leaks", since a stray highlight reader, a catalog statistic or a row estimate shows activity in a sealed year (AA, MM, OO); and R-161 under "Nothing leaks" too, since a join date can be a sealed journey's commit date (TT). R-155, R-159 and R-162 narrow what a reader can infer after unlock (JJ, KK/NN/QQ, SS). R-163 keeps the loader inside a viewer's rights (II). R-164 and R-165 apply to every row: a guard tested only by a privilege refusal, or a ruling not carried, can let any banned item through.

R-166 to R-168 (added 2026-10-31, r7) carry FS §20 WW–HHH. R-166 sits under "No streaks, counters" and "No ranking": the ring count reaches every viewer, so a numeral, total or comparison beside another user's circle would turn a record into a counter (CCC). R-167 sits under "Nothing leaks": a log line holding an image or a journey id beside a real time would record that a sealed journey's owner pressed then (DDD, FFF). R-168 applies to every row: a screen state that both holds and bans an element lets the builder pick, which is how a banned item gets in.

R-169 to R-171 (added 2026-10-31, r8) carry FS §20 III–PPP. R-169 sits under "Nothing leaks": the note handle is a sealed photo's id held beside its press instant, so any copy of it outside the route records that a sealed journey's owner pressed then (LLL). R-170 sits under "No retakes": a lost press or note that looks or answers differently is the one sign that invites a second press (DDD, JJJ). R-171 applies to every row: an answer with no screen row is a behaviour the builder must pick, which is how a banned item gets in.

R-172 and R-173 (added 2026-10-31, r9) carry FS §20 QQQ–XXX. R-173 sits under "No retakes": a note step that the screen has ended but the server still accepts is a way back to a second take (III, WWW, C4). R-172 applies to every row: a history line rewritten to cite a later ruling hides what was open when, which is how a decided label and an open question end up in one sentence.

R-174 and R-175 (added 2026-10-31, r10) carry FS §20 YYY–BBBB. R-175 sits under "No retakes": a skip request the screen never sends leaves the note step open at the server, which is a way back to a second take (WWW, C4). R-174 applies to every row: a ruling's words lifted out of their subject become a rule nobody ruled on.

## `Phase-1-Proposal.md` §2.5 mapping

| §2.5 check | Line | R-IDs |
|---|---|---|
| 1. No UPDATE or DELETE on reflection, overview, note, photo, journey, user name, journey_reveal | P1:176 | R-015, R-017, R-018, R-020, R-021, R-022, R-023; tested per R-164 (2026-10-31) |
| 2. No visibility, tag or chapter insert after reveal finished | P1:177 | R-052; tested per R-164 (2026-10-31) |
| 3. No second Commit while sealed | P1:178 | R-026; tested per R-164 (2026-10-31) |
| 4. Owner before unlock: 0 rows, count 0, ciphertext | P1:179 | R-001, R-002, R-003. Since 2026-10-31 (FS §20 MM, OO): the 0 rows and count 0 are read through the readers, the tables refuse every product role, and the estimate and catalog halves are R-157 and R-158; tested per R-164 |
| 5. capture() and start_highlight() return no number | P1:180 | R-038; image samples (amended P1:180) R-159, R-160 |
| 6. No comment, reply, like, reaction, caption, score, rank, streak, badge, view, follower | P1:181 | R-105 (comment, reply), R-100 (like, reaction, view), R-108 (caption), R-101 (score, rank, badge), R-097 (streak), R-081 (follower) |
| 7. B reads no layer row with owner ≠ B; A's tag never touches B's map | P1:182 | R-069, R-072 (through `layer_rows()` since FS §20 OO) |
| 8. Typed-name tag never makes a layer row | P1:183 | R-073 |
| 9. Announcements: no media, three types | P1:184 | R-084, R-085 |
| 10. Only the clock module reads the system clock | P1:185 | R-115 |
| 11. No face or vision library | P1:186 | R-110 |

---

## Gaps

Rules that could not be made testable, and places where the sources disagree. None of these is decided here. Each needs the user.

Since 2026-10-27 each gap carries a status line under it: **being fixed** by a `Decisions-Needed.md` section A correction (approved by the user), covered for the prototype by a **provisional default**, **partly covered**, or **still open**. A provisional default is not a decision. A gap is closed only when the user decides and `FS` §20 records it, and even then it stays here, marked, because the rubric never shrinks.

### Contradictions between sources

**G-1. Reflection slot dates.** **Closed 2026-11-10 (FS §20 VVVV): slots now follow each photo's capture date, as the FS:104–111 example had them.** The example at `FS:104–111` dates reflections from the photo's own capture date (7 Jan each year). `FS:101` and `FS:274` (§20 D) say all photos of a journey move slot together on the journey's unlock anniversary, and `MJC:852` agrees. The same per-photo example is in `MJC:200` and `MJC:203–210`. R-121 tests the §20 D wording; the example needs correcting or confirming.

**Being fixed by A1, 2026-10-27** (`Decisions-Needed.md` section A, approved). R-121 already tests the corrected wording. Kept here because the rubric never shrinks.

**G-2. "Publish".** `FS:141` says visibility is "chosen at publish time", and `MJC:365–367`, `MJC:424` and `MJC:440` speak of publishing a journey. No step called publish exists. The decided terms are "reveal finished" (`FS:151`, `FS:276`) and "journey launched" (`FS:280`). Also `MJC:401` says layers are calculated when journeys are "uploaded", against `FS:162` (when a reveal is finished). Learnings open questions 1 and 2.

**Being fixed by A4, 2026-10-27** (the "uploaded" layers line, `MJC:401`). **Provisional default:** Decisions-Needed B1: "Publish" means "reveal finished"; docs use only "reveal finished" and "journey launched". Under B1 a step, control or copy called "publish" in the build fails R-134.

**G-3. Close friends.** `MJC:807` says close friends "get everything", and `MJC:383` says "everything for the people closest to you". `FS:278` (§20 H), `FS:150` and `MJC:864` say they see nothing beyond the rest of the network. R-064 tests §20 H.

**Being fixed by A3, 2026-10-27.** R-064 already tests §20 H.

**Updated 2026-11-09 (FS §20 KKKK; `docs/reviews/2026-11-09-rules-kkkk.md`).** Close friends are now a list chosen from among friends (KKKK (f)). The 2026-10-27 contradiction is replaced by a new one: FS §20 H still says they "see nothing beyond the rest of the network" (`FS:278`, only its ring part marked superseded), while KKKK, `FS:150`, `CLAUDE.md:114` and DN E2 call it open, and the user has said close friends should get something extra. Until the supervisor marks which holds, R-064 runs under B47's "nothing extra".

**G-4. When reminders, counters and progress bars are banned.** `FS:233` says "No visible counters, no progress bars, no reminders **during the sealed year**". `CLAUDE.md:69` and `Master-Prompt.md:42` ban them with no time limit, and `FS:242` bans reminders to capture, reflect or return at any time. Open: is a counter or progress bar allowed after unlock, for example "12 of 24 reflected" during the reveal? R-099 is provisional on this.

**Provisional default:** Decisions-Needed B8: Counters and progress bars are banned at all times, not only while sealed. R-099 is firm under B8.

**G-5. Showing the quota.** `FS:243` bans showing the quota left "in a way that reads as a target", which implies some way of showing it may be allowed. `P1:49` says frames used and left are never stored or returned, and `CLAUDE.md:69` bans counters. Open: may the owner ever see how many frames they have left?

**Provisional default:** Decisions-Needed B7: Frames left are never shown. A refused capture says so with no number (copy in Phase 2). R-038, R-098 and R-138 are firm under B7.

**G-6. Stored journey fields.** `FS:15` lists "frames used", "highlights used" and a state "committed / sealed / unlocked" as journey properties. `P1:49` says frame and highlight counts are never stored, and `P1:76–84` says state is derived, with "committed" folded into sealed. R-039 tests P1.

**Being fixed by A5, 2026-10-27.** R-039 already tests P1.

**G-7. What adds a ring to the circle.** `FS:185` says one ring "per year with the app", and `MJC:687` says "each year with the app adds a ring". `P1:65` says one ring "per journey whose reveal is finished". These differ for a user with a year and no journey, or a reveal never finished (Long Way Round #4).

**Provisional default:** Decisions-Needed B4 (switchable): One ring per finished reveal (`P1:65`); other setting: per year with the app. R-143 must pass under both settings. The contradiction stays open until the user decides.

**G-8. The Positivity Feed and "no photo feed".** `CLAUDE.md:72` and `Master-Prompt.md:45` say "No photo feed. The feed carries announcements only, never images". The Positivity Feed is fed by public photos and their reflections (`FS:203–204`, `P1:324`). Open: does the Positivity Feed show photographs, and if so how does that fit the ban? Also `FS:203` says it draws from "journeys set to public", while visibility is per photo (`FS:141`); `MJC:375` and `MJC:379` show the same split. And `MJC:244` says "no feed", against `FS:169–177`.

**Decided 2026-10-30 (FS §20 Q):** "No photo feed" covers the Positivity Feed. Text only; a photo shows only when one entry is opened. The "with photographs" setting is removed.

**Provisional default (before 2026-10-30):** Decisions-Needed B9: (a) reflection text only, with the photo shown when opened, switchable to "with photographs"; (b) per-photo visibility; (c) drafted tag list only; (d) chapter filter; (e) newest first; (f) only after reveal finished. Covers the per-photo split (b, R-067) and, under the default, the image question (a, R-103). **Not covered:** whether the "with photographs" setting fits "No photo feed" (R-145 reports it as a finding), and the `MJC:244` "no feed" line, which no section A item corrects.

**G-9. Images in the announcement feed.** `CLAUDE.md:72` says "never images". `FS:171` says "No photographs in the stream". Open: may an announcement show the actor's profile picture?

**Provisional default:** Decisions-Needed C7: No profile picture is shown anywhere; announcements carry no image. R-086 is firm under C7.

**Decided 2026-10-31.** FS §20 XXX (`FS:360`): C7 is decided in full; announcements carry no image. G-9 is closed.

**G-10. Profile picture and looks.** `FS:13` and `P1:62` give each user a profile picture. `FS:29` and `Master-Prompt.md:113` say nothing on a profile signals how the person looks. Open: what may the profile picture be?

**Provisional default:** Decisions-Needed C7: No profile picture is shown anywhere. The profile shows the name in the circle. R-126 is read under C7. The profile picture field in `FS:13` and `P1:62` still exists in the approved model; the default only stops it being shown.

**Decided 2026-10-31.** FS §20 XXX (`FS:360`, extends YY): no profile picture anywhere; the profile shows the owner's name in the circle. G-10 is closed.

**G-11. Choices made during a reveal that is never finished.** `FS:269` says an unfinished reveal has "no chapter, no tags", and `P1:25` and `MJC:855` say "the photos stay Network". But choices are inserted, once each, during the reveal (`FS:286` §20 P, `P1:46`, `P1:143`, `P1:165–166`, `P1:408`). Open: if the owner sets a photo to Private, or sets a chapter, and never finishes, does that choice take effect? R-054 tests only what all sources agree on.

**Provisional default:** Decisions-Needed B3: Each reveal choice takes effect when made. A reveal can be finished at any later time. R-051 and R-054 are read under B3.

**G-12. Walking a path can show a ring.** `FS:196` says the reader sees where they themselves appear in someone's journey. Counting those photos lets a reader estimate their ring on that person's map (5+ tight), against `FS:164`, `CLAUDE.md:74` and `P1:51`. Private tags count but stay hidden (`FS:277`), so the estimate is a floor, not exact. Open: is that acceptable, or should the "where you appear" view not total up?

**Closed 2026-11-10 (FS §20 NNNN (b)): the reader is never shown where they appear, so there is nothing to count. FS:196 carries the ruling.** *Before:* **Provisional default:** Decisions-Needed B12 (switchable): Walking a path shows the photos where the reader appears, in journey order, with no total and no grouping; other setting: hidden. **Partly covered:** under "shown" a reader can still count by scrolling, so the floor estimate this gap describes remains. R-139 and R-147 report it as the weakest point until the user decides. Under "hidden" the gap does not arise.

**G-13. Highlights during the sealed year.** `P1:48` sealed photo, note, tag and reflection rows, but not highlight rows. **Closed 2026-10-30: FS §20 AA seals highlight rows (P1:48 amended).** A readable highlight record would tell others that, and when, a user started one, against `FS:246` and `FS:279` (§20 I). R-008 already requires that others see nothing, so the gap is in the current implementation. ~~Open for the owner: may the owner see that a highlight is open and when it ends?~~ **Settled 2026-10-30 (FS §20 S): the owner sees only that a highlight is open, never when it ends.** Original question: A running "ends in 3h" would be a counter (`CLAUDE.md:69`); a plain open-or-closed is not addressed anywhere.

**Provisional default:** Decisions-Needed B6: Others learn nothing about highlights. The owner sees only "a highlight is open", with no end time and no countdown. Covers both halves: R-008 (others) and R-009, R-138, R-140 (owner) are read under B6. The implementation gap was closed 2026-10-30 by FS §20 AA. Before that: `P1:48` does not seal highlight rows, so the build must keep them unreadable to others without changing the approved model (CL:28); any model change goes to the supervisor.

**G-14. Feeling tags.** `FS:131` says feeling tags are written "inside a category", and `P1:141` stores them as (journey, free text) with no category. `FS:131` also says popular feeling tags "surface over time", while `FS:202` says the Positivity Feed is "never by popularity". Open: how a tag surfaces, and whether that uses any measure of popularity.

**Partly covered.** **Provisional default:** Decisions-Needed B9 (c) and (e): only the drafted tag list qualifies for the Positivity Feed, newest first, so the feed is never ordered by popularity (R-103). **Still open:** `FS:131` "inside a category" against `P1:141` (no category), and how popular feeling tags "surface over time" without a popularity measure. No default covers either; a build that surfaces tags by how often they are used fails R-134.

**Provisional default (added 2026-10-27, fdb83d3):** Decisions-Needed B17: Feeling tags are free text on the journey, with no category, as in the approved model (`P1:141`). Decisions-Needed B18: Tags never "surface" by popularity; no suggestions and no counts (`FS:202` over `FS:131`). With B9 (c) and (e) these cover the whole gap for the prototype. A deliverable that still offers a category-bound feeling tag, or treats popular surfacing as open, fails R-135 and R-150.

**G-15. When an overview is written.** `FS:118` (and `MJC:218`) says the overview is "written at reveal". `FS:275` (§20 E) says a new one every year on each journey. R-122 tests §20 E.

**Being fixed by A6, 2026-10-27.** R-122 already tests §20 E. Decisions-Needed B13 adds when slot 1 may be written (R-122).

**G-16. "Your Journey is ready."** `BP:79`, `Master-Prompt.md:138` and `MJC:740` name this as a key microcopy moment. `FS:236` bans "re-engagement notifications of any kind", and `MJC:156` contrasts the reveal with "an unlock notification with nothing to do". Open: is "Your Journey is ready" a notification sent at unlock, or only text shown when the user next opens the app? R-094 bans the notification until the user decides.

**Provisional default:** Decisions-Needed C1: "Your Journey is ready" appears on next open, never as a notification. R-094 is firm under C1.

**G-17. What the owner sees of a sealed journey.** `FS:74` says nothing in a sealed journey is visible "not to the user". `P1:84` lets the owner see its type, commit date and unlock date. These may agree (dates are about the journey, not in it), but it is worth confirming, together with whether showing the unlock date is allowed at all given the countdown ban (R-013).

**Decided 2026-11-09 (FS §20 EEEE, was Decisions-Needed C2):** The unlock date is shown as a plain date, never relative ("in 64 days"). R-009 and R-013 are read under C2. B6 adds one more thing the owner may see of a sealed journey: that a highlight is open (R-009).

**Provisional default (added 2026-10-27, fdb83d3):** Decisions-Needed B19: The owner of a sealed journey sees its type, commit date and unlock date and nothing else (`P1:84`; `FS:74` read as covering the contents). R-009 is read under B19. B19's "nothing else" and B6's highlight state read against each other. **Decided 2026-10-30 (FS §20 S):** B6 holds.

**G-23. What else tells a public reader that a reveal is finished (added 2026-10-31, r6).** FS §20 SS (`FS:323`) says whether a reveal is finished is "never public". Three other lines let a public reader infer it:
- DN B9 (f) (`DN:28`): the Positivity Feed, which public readers use, carries only journeys whose reveal is finished. An entry there therefore says the reveal is finished (Round #2 to First Light).
- DN B4 (`DN:23`), default "one ring per finished reveal": S-16 shows rings to a public viewer (`Screen-Inventory.md:405`), so a new ring says a reveal was finished. `Screen-Inventory.md` OQ-44 is still open on rings for public viewers.
- FS §20 R (`FS:291`), under B2's option: a Public photo becomes readable only once the reveal is finished.

Related: under FS §20 TT (`FS:324`), B4's other setting, "per year with the app", shows others one ring per year since joining, which gives the join year. Open: does SS cover only the `journey_reveal` record, or the fact however it is learned? And may B4's second setting show a ring count to others? Not decided here. The strictest reading (CL:24) is the fact. R-162 and R-161 run on that reading until the user rules.

**Decided 2026-10-31.** FS §20 ZZ (`FS:333`): SS covers the reveal state as a field; inferring it from the Positivity Feed, rings and photos appearing is allowed. FS §20 WW (`FS:330`): B4's per-year rings show only on the user's own profile. FS §20 CCC (`FS:336`): public viewers get a ring count only, no dates (R-166). FS §20 EEE (`FS:338`) applies the same reading to journey dates (R-152). G-23 is closed; R-161 and R-162 now read under these rulings.

**G-24. A press lost to the guard bug: "nothing different" against "no note offer" (added 2026-10-31, r7).** FS §20 DDD (`FS:337`): "the user sees nothing different; that press gives no photo". FS §20 GGG (`FS:340`): "the camera returns as after any press, with no note offer". `Screen-Inventory.md:87` and `:96` send every accepted press straight to the note step S-12 (`PROVISIONAL: C4`), so the missing offer is the one sign that the press gave no photo, which `Screen-Inventory.md:94` bans in the same row. Seeing no offer, the user may press again for the same moment, which PP (`FS:320`) bans ("nothing invites a second press"). Not picked. Open: does GGG mean the press may look different from an accepted one, or is S-12 to be offered and then end with nothing stored? R-160 (3) and R-168 hold this open until the user rules. It blocks the S-02 and S-12 flows (Phase 2) and screens (Phase 4), not the Phase 3 schema.

**Decided 2026-10-31.** FS §20 JJJ (`FS:343`): the screen after a lost press looks exactly like a normal press, note offer included; DDD wins and GGG's "no note offer" is retired. A note written for a lost press is discarded. G-24 is closed; R-160 and R-168 carry it.

**G-25. A lost press that would have been refused (added 2026-10-31, r8).** FS §20 JJJ (`FS:343`): "the screen looks exactly like a normal press, note offer included". The guard runs before the §20 U order, so whether the lost press would have been accepted is never computed, and the route answers `accepted` (`Phase-1-Amendments.md` §6 lines 516 and 529). When no frame is left, or the highlight is full, a normal press at that instant shows the capture refusal (`Screen-Inventory.md:92`; `PROVISIONAL: B7`), not a note offer. Amendments OQ-32 (a) raised exactly this ("different from an accepted press, or from what that press would have given?"), and its settlement answers only the accepted case. Not picked. Phase 3 is unaffected: nothing is stored either way. It blocks the S-02 lost-press row and R-170 (Phase 4).

**Decided 2026-10-31.** FS §20 QQQ (`FS:352`): a lost press looks like the normal press it would have been, judged first at the press instant; one a normal press would refuse shows the normal refusal. Carried in `Phase-1-Amendments.md` §6 lines 515, 539 and `Screen-Inventory.md:94`, `:96`. G-25 is closed; R-170's `Open` line is superseded.

**G-26. A note window that crosses the journey's unlock (added 2026-10-31, r9).** A photo captured less than 15 minutes before `unlocks_at` has a note window that runs past the unlock. `Phase-1-Amendments.md:551` says the note step accepts a handle "only ... while the journey is sealed", citing P1:104 and P1:108, but neither line says so: P1:108 gives only "within 15 minutes of the photo's `captured_at`" (D8), FS §20 K gives "up to 15 minutes after capture, never after", and the evidence stand-in checks only the owner and the window (`Phase-1-Amendments.md:643`). `Screen-Inventory.md:346` makes `unlock-day` onward "Not a writing step". Open: (a) may a note be added after the unlock, inside its 15 minutes, to a photo that is already readable? (b) If not, the route's window check (`:554`) passes and `add_note()` refuses, and no route answer (`saved`, `closed`) covers that refusal; a lost press at the same instant is answered `saved` (JJJ), so the device answers would differ (R-170 (1)). The prototype reaches it whenever the demoer jumps to the next unlock while S-12 is open (R-153). Not picked. It blocks `add_note()`'s refusal conditions (Phase 3) and the S-12 row (Phase 4).

**Decided 2026-10-31.** FS §20 YYY (`FS:361`): the note window ends at unlock, and that end looks exactly like the window ending (UUU, RRR); this answers (a). FS §20 BBBB (`FS:364`) answers (b): a note-step refusal inside a window the route read as open gets the one `closed`. Carried in `Phase-1-Amendments.md` §0 `:61`, `:64`, §6 `:561`, `:564`, `:567–576`, evidence `:807`, `:856`; P1:108, P1:180; `Screen-Inventory.md:340` end (7), `:346`, `:348`. G-26 is closed.

**G-27. Capture or the note step open at the unlock instant (added 2026-10-31, r10).** YYY rules the note step: at unlock it ends as at 15 minutes, and nothing on it changes on its own (`Screen-Inventory.md:340` end (7)). Nothing rules what follows. S-12 "leads to the camera S-02" (`:336`), but S-02's `unlock-day` row is "Not available" (`:99`). A press made on an open camera at or after unlock is answered `refused` (`Phase-1-Amendments.md:574`), and S-02's one refusal row is for "no frame, or the highlight's quota reached" (`:94`). S-12's never-list bans "nothing that sets end (7) apart from end (4)" (`:340`), yet after (4) the camera works and after (7) it does not. Decisions-Needed C1 says "Your Journey is ready" appears on next open. Open: (a) does an open camera change at the unlock instant, or only on the next open (C1)? (b) does a press refused for unlock show the B7 refusal, which then reads as "no frame"? (c) where does S-12 end (7) lead? Not picked. It does not block Phase 3 (`capture()` already refuses after unlock, P1:99). It blocks the S-02 and S-12 flows (Phase 2) and screens (Phase 4). The prototype reaches it whenever the demoer jumps to the next unlock with capture open (R-153).

**G-28. What counts as leaving capture (added 2026-10-31, r10).** `PROVISIONAL: C4` says leaving capture ends the note step, and since WWW the client tells the route by sending the skip request on it (`Phase-1-Amendments.md:566`). No doc says whether the app going to the background, the screen locking, an incoming call or the app being closed by the system is leaving capture. A normal app resumes the step on return; under C4 that would be a way back. Not picked. Phase 4 (and the S-12 flow in Phase 2).

### Rules that cannot be made testable yet

**G-18. Calendar arithmetic.** "12 months" (`FS:36`, `P1:14`), "month of the journey" (`FS:261`, `P1:18`) and "any day" (`P1:15`) are not defined for a commit on the 29th, 30th or 31st, for 29 February, or across time zones (whose midnight starts a day). "Up to 15 minutes ... never after" (`FS:281`) does not say whether exactly 15:00 is in or out. "24 hours" (`P1:19`) does not say what happens across a daylight-saving change. R-025, R-036, R-046, R-118 and R-123 test only away from these edges.

**Provisional default:** Decisions-Needed B16: A commit on the 29th–31st uses the last day of shorter months. One time zone for the prototype (UTC). Exactly 15:00 is out. A highlight lasts 24 hours of elapsed time. Covers every edge listed: R-025, R-040, R-046, R-118 and R-123 add the edge cases. Time zones beyond the prototype stay open: B16 sets UTC only for the prototype.

**G-19. Who else reads an overview.** `FS:275` and `P1:126` say the owner's network can read it. Nothing says whether anyone outside the network can, for example on a journey with public photos in the Positivity Feed.

**Provisional default:** Decisions-Needed B13: The slot 1 overview can be written after the reveal is finished, within the slot. Readable by the network only. R-063 is read under B13.

**G-20. "Anyone" for Public.** `FS:147` says a public photo is readable by "anyone". Open: does that include signed-out visitors, or only users?

**Provisional default:** Decisions-Needed B14: "Public" means signed-in users only. R-061 is read under B14.

**G-21. Review-only rules.** These are checks, but only a reader can decide them: tone (`FS:135`), the deliberate act to open a journey (`FS:177`), invited never nudged (`FS:209`), names from within (`FS:29`), and the time-in-app test (`CLAUDE.md:76`). `FS:247` "train on" cannot be proven by a code scan; R-114 is review for that reason.

**Still open.** No default covers it, and none can: these stay review checks.

**G-22. Stale lines in the Concept doc**, not marked as superseded: `MJC:799` says "Frame range 24–48", against the 12–48 range in `FS:38–42`. `MJC:714` points the streak ban at "section 4", which does not hold it (Learnings open question 3).

**Being fixed by A7 and A8, 2026-10-27** (the "24–48" frame range, and the streak ban's pointer to "section 4").

### Questions for the user (no source covers them)

These are not checks, since no source states a rule. A normal product would fill each by reflex. Since 2026-10-27 each has a provisional default for the prototype; none is decided.

1. **Feed order.** The announcement feed's order is not stated anywhere. Is it newest first? **Provisional default:** Decisions-Needed C14: Feed is newest first (and B9 (e) for the Positivity Feed). Reverse time order is the only sort key allowed.
2. **Analytics and telemetry.** May the app or site collect usage analytics at all? `FS:247` covers memories, not usage, and low usage is the goal (`CLAUDE.md:76`). **Provisional default:** Decisions-Needed B15: No usage analytics or telemetry of any kind. R-114 is read under B15.
3. **The note photo's source.** Must the note page be photographed live in the app, like the photo (`FS:53`), or can it come from the gallery? **Provisional default:** Decisions-Needed C4: The page is taken live, once, with no re-shoot. R-048 is read under C4.
4. **Push permission.** If no notification is ever sent (R-094), should the app ever ask for notification permission? Asking is itself a prompt. **Provisional default:** Decisions-Needed C15: The app never asks for notification permission. R-094 is read under C15.
5. **Capture refusals.** When capture is refused for the frame limit, what may the message say without becoming a counter (R-038, G-5)? **Provisional default:** Decisions-Needed B7: A refused capture says so with no number; copy in Phase 2. R-038 and R-138 are read under B7. The exact words are still open until Phase 2 copy.
