# My Journey: Rules Rubric

Owner: Rules Guardian (`.claude/agents/rules-guardian.md`). Build Plan Phase 1 deliverable, "The rules list as testable statements, one line each" (`Build-Plan.md:63`).

Version 1, 2026-10-27. No code exists yet. Nothing below has been audited.

Last updated: 2026-10-27 (second pass). Aligned with the provisional defaults in `Decisions-Needed.md` (B1–B16, C1–C16, approved by the user on 2026-10-27 for the prototype). Added R-141 to R-149. Added "Provisional default" lines to checks and Gaps. Marked the Gaps that section A is fixing. Re-cited every `CL:` line after the 2026-10-27 rule zero rewrite moved `CLAUDE.md` down (old 15 → 17; old 21 onward +9). No check renumbered or removed.

Updated 2026-10-30 (re-audit of `Screen-Inventory.md` round 1, `docs/reviews/2026-10-30-rules-screen-inventory-r1.md`): added R-150. Added `Provisional default` lines for B17, B18 and B19, which `Decisions-Needed.md` gained in commit fdb83d3, under R-009, R-103, G-14 and G-17. No check renumbered or removed.

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
| DN | `docs/Decisions-Needed.md` (cited by ID: A1–A12, B1–B19, C1–C18 (C17, C18 added 2026-10-30); B17–B19 added 2026-10-27 in fdb83d3) |

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

### R-002
- **Statement:** Before unlock, every stored image of a sealed journey, photo and note alike, is ciphertext to everyone, and nothing releases its key until unlock.
- **Type:** auto · **Applies to:** data
- **Source:** FS:234, P1:48b, P1:105. **= §2.5 check 4** (blobs)
- **How to check:** Read the raw stored bytes of a Lantern #6 photo and note before unlock. They must not start with any image signature (JPEG `FF D8 FF`, PNG `89 50 4E 47`, WebP `RIFF....WEBP`, HEIC `ftyp`). Call the key-release path before unlock: refused. Call it at unlock: key returned.
- **Current implementation:** per-journey key released by one function, only after unlock (P1:48b).

### R-003
- **Statement:** Before unlock, no handwritten note, tag, person tag or reflection belonging to a sealed journey is readable by anyone, the owner included.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:74, FS:234, P1:48a. **= §2.5 check 4** (extended to the other sealed rows P1:48 names)
- **How to check:** The R-001 access test, run against every table and endpoint that holds note, tag, person-tag or reflection data for Lantern #6.

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
- **Provisional default:** Decisions-Needed B6: Others learn nothing about highlights. Holds as written, and now explicitly covers the highlight record, which `P1:48` does not seal: no endpoint or screen tells anyone but the owner that a highlight was started, is open, or when. Add to the comparison a run where Steady Lantern has a highlight open: Second Wind's responses must still match the First Light run apart from the journey-underway flag (closes G-13 for others)

### R-009
- **Statement:** The owner of a sealed journey sees its type, commit date and unlock date, and nothing else about it.
- **Type:** auto · **Applies to:** API, UI
- **Source:** P1:84, FS:74. See G-17
- **How to check:** As Steady Lantern before 2027-01-01, list every field returned about Lantern #6. Anything beyond type, commit date, unlock date and identifiers fails.
- **Provisional default:** Decisions-Needed C2: The unlock date is shown as a plain date, never relative ("in 64 days"). The owner's unlock date is allowed as a date only (see R-013)
- **Provisional default:** Decisions-Needed B6: The owner sees only "a highlight is open", with no end time and no countdown. Under B6 the check reads: type, commit date, unlock date and, while a highlight is open, the bare fact that one is open. Its start time, end time, elapsed or remaining time, how many highlights are used or left, and any photo count in it all fail
- **Provisional default:** Decisions-Needed C3: The sealed-year screen does not point to earlier journeys. Nothing about an earlier journey, including an open reflection slot, appears on the sealed-year screen
- **Provisional default:** Decisions-Needed B19: The owner of a sealed journey sees its type, commit date and unlock date and nothing else (`P1:84`; `FS:74` read as covering the contents). Holds as written; B19 settles the first half of G-17 for the prototype. B19's "nothing else" and B6's "a highlight is open" (line above) read against each other. **Decided 2026-10-30 (FS §20 S):** B6 holds; the owner sees "a highlight is open", nothing more

### R-010
- **Statement:** A capture changes nothing that any reader can observe, the owner included: no "last captured", "active today", "captured this week", recent-activity mark or announcement.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:246, FS:74, CL:73
- **How to check:** As Lantern, Second Wind and First Light, snapshot every read endpoint about Lantern. Capture a photo as Lantern. Snapshot again. Every snapshot must match its earlier one. The capture call's own `accepted` reply is the only thing that differs.

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
- **Provisional default:** Decisions-Needed C2: The unlock date is shown as a plain date, never relative ("in 64 days"). Firm under C2: any relative form of the unlock date fails, including "next month", "soon", "in a few weeks", "this winter" and `Intl.RelativeTimeFormat` or a library's `fromNow`/`formatDistance` applied to `unlocks_at`. Add those to the grep

### R-014
- **Statement:** Every path that can return data applies the seal: search, export, error messages, logs shown to users, debug and admin routes, and the time-control panel.
- **Type:** auto · **Applies to:** API, UI
- **Source:** CL:81 ("unreadable, not merely hidden in the UI"), FS:234
- **How to check:** Build the route list from the code. Run the R-001 and R-008 tests against every route. Trigger each capture refusal and confirm the error text holds no number and no photo data.

---

## 2. Immutability and append-only

### R-015
- **Statement:** Nobody, the owner and the app's own role included, can change or delete a reflection once it is written.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:65, CL:80, MP:38, FS:99, FS:229, P1:44. **= §2.5 check 1**
- **How to check:** As the app role, run UPDATE, DELETE and TRUNCATE on the reflection store: each raises. Confirm no API route accepts an edit or delete of a reflection.
- **Current implementation:** INSERT and SELECT grants only, plus a trigger that raises on UPDATE, DELETE and TRUNCATE (P1:44).

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

### R-022
- **Statement:** A user's name is chosen once and never changes.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:268 (§20 mechanics 8), P1:32 (D19), P1:61. **= §2.5 check 1**
- **How to check:** UPDATE on the user name raises. No settings screen offers a rename.

### R-023
- **Statement:** A finished reveal cannot be un-finished or re-opened.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:164, FS:151. **= §2.5 check 1**
- **How to check:** UPDATE and DELETE on the reveal-finished record raise. No route re-opens a reveal.

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

### R-027
- **Statement:** Once the current journey has unlocked, the next Commit is accepted, whether or not that journey's reveal is finished.
- **Type:** auto · **Applies to:** API
- **Source:** FS:273, P1:16 (D3), P1:209 (Long Way Round between journeys)
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

### R-041
- **Statement:** Only one highlight can be open at a time. Starting another while one is open is refused.
- **Type:** auto · **Applies to:** API
- **Source:** FS:284 (§20 N), P1:345 (R3), CL:97, MP:65
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
- **Source:** FS:286 (§20 P), P1:347 (R5), CL:103, MP:73
- **How to check:** On Lantern #6 after unlock, set a photo's visibility, then try to change it: refused. Add a people tag, try to remove it: refused. Set the chapter, try another: refused. No UI control offers change or removal.
- **Current implementation:** these records are insert-only (P1:46).
- **Provisional default:** Decisions-Needed C5: Each set-once choice shows a one-line "this can't be changed" before it is saved. Holds as written. Under C5 that line is a statement, not a second chance: after the choice is saved there is still no change or undo control
- **Provisional default:** Decisions-Needed B3: Each reveal choice takes effect when made. Under B3 a choice set during a reveal not yet finished is live at once: a photo set to Private is readable by its owner only from that moment (R-059), not from reveal finished

### R-052
- **Statement:** Once the reveal is finished, no visibility, people tag, chapter or feeling tag can be added.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:151, FS:276 (§20 F), P1:25 (D12), P1:46, CL:103. **= §2.5 check 2**
- **How to check:** On a revealed fixture journey (Lantern #5), insert each kind: each raises.
- **Current implementation:** trigger refuses inserts once the journey's reveal-finished record exists (P1:46).

### R-053
- **Statement:** A photo with no visibility choice is Network: once unlocked, the owner's network can read it.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:151, FS:276 (§20 F), P1:25 (D12), P1:166, CL:103
- **How to check:** As Open Hands (on Round's map) at baseline, read a Long Way Round #4 photo: allowed. As First Light: refused.
- **Provisional default:** Decisions-Needed B2 (switchable, R-142): The network can read an unlocked journey from unlock, as D12 and `P1:311` say (other setting: only after reveal finished). Holds as written under the default. Under "only after reveal finished" it reads: a photo with no visibility choice is Network, and the owner's network can read it once the reveal is finished; the Open Hands read of Long Way Round #4 (reveal never finished) is refused

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
- **How to check:** As Long Way Round, write a reflection on a #4 photo: accepted (fixture: round reflected on 2026-09-10, P1:241).

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

### R-058
- **Statement:** The overview is optional. A reveal can be finished without one.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:285 (§20 O), P1:346 (R4), CL:105
- **How to check:** Finish a reveal with no overview: accepted. The finish control is not blocked by a missing overview, reflection or tag.
- **Provisional default:** Decisions-Needed C5: Nothing is required before finishing a reveal. Under C5 the check widens: a reveal with no chapter, no feeling tag, no people tag, no visibility choice, no reflection and no overview can be finished. Nothing on the finish screen lists what is "missing" or "left to do" (R-095, R-099)

---

## 5. Visibility and access

### R-059
- **Statement:** A Private photo, and its reflections, can be read by its owner and nobody else.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:145, FS:278 (§20 H), P1:29 (D16)
- **How to check:** As every fixture user except Lantern, read a Lantern #5 private photo: refused (P1:309–313).

### R-060
- **Statement:** A Network photo can be read by its owner and by every user on the owner's map, whatever their ring, and by nobody else.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:146, P1:311 ("outer ring is still network")
- **How to check:** Lantern #5 network photo: Second Wind and Open Hands allowed, Long Way Round and First Light refused.

### R-061
- **Statement:** A Public photo can be read by any user.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:147. See G-20 for signed-out visitors
- **How to check:** Every fixture user reads a Lantern #5 public photo: allowed.
- **Provisional default:** Decisions-Needed B14: "Public" means signed-in users only. Under B14 the statement reads "any signed-in user". Add the case: a signed-out request for a Lantern #5 public photo, its reflections, and any share or direct URL to it: refused, with no image bytes in the reply (closes G-20)

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

### R-064
- **Statement:** Close friends see nothing beyond the rest of the network. There is no close-friends access level, list or grant.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:150, FS:278 (§20 H), P1:29 (D16), CL:107, MP:81, MJC:864. See G-3
- **How to check:** For every photo, a tight-ring member and an outer-ring member of the same owner have identical access. Schema scan for `close_friend`, `inner_circle`, `favourite` access grants.

### R-065
- **Statement:** Being tagged in a photo gives no access to it. A user tagged in someone's Private photo cannot read that photo.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:288, FS:145
- **How to check:** As Second Wind, read Lantern #1's two private photos tagging Wind: refused.

### R-066
- **Statement:** Tagging someone gives the tagger no access to that person's photos.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:277 (§20 G), MJC:860
- **How to check:** As Open Hands, read Lantern's network photos from a journey where Lantern did not tag Hands. Access must come only from Hands being on Lantern's map, never from Hands' own tags of Lantern.

### R-067
- **Statement:** Visibility is set per photo, not per journey.
- **Type:** auto · **Applies to:** data, UI
- **Source:** FS:141, MJC:379 (decided 2026-10-18)
- **How to check:** Schema: visibility is keyed by photo. Fixture journeys hold mixed levels (P1:218–237). See G-8 on "journeys set to public".
- **Provisional default:** Decisions-Needed B9 (b): Positivity Feed visibility is per photo. Holds as written, including for the Positivity Feed: no control sets a whole journey public, and the feed selects photo by photo (R-103)

### R-068
- **Statement:** The baseline access matrix holds.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:305–313
- **How to check:** Run every cell of the §3.6 matrix as a test at baseline.
- **Provisional default:** Decisions-Needed B2 (switchable, R-142): The network can read an unlocked journey from unlock (`P1:311`). The §3.6 matrix is written for this setting. Under "only after reveal finished", every network-reader cell for a Network-default photo in a journey whose reveal is not finished (Long Way Round #4) flips to refused; all other cells are unchanged. Run the matrix under both settings. How "only after reveal finished" combines with a photo set Public during an unfinished reveal (B3: choices take effect when made) is not stated in `Decisions-Needed.md`; no fixture has that case, and if one is needed it goes to the supervisor, not into the build. **Decided 2026-10-30 (FS §20 R):** under that setting a Public photo is refused too, until the reveal is finished

---

## 6. Layers

### R-069
- **Statement:** No endpoint or response tells a user which ring they sit on in someone else's map. Layer data can be read only by the map's owner.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:74, CL:82, MP:47, FS:164, FS:235, P1:51. **= §2.5 check 7** (first half)
- **How to check:** As Second Wind, query every table and endpoint that holds layer data: only rows where Wind is the owner return.
- **Current implementation:** layer rows readable only where `owner = viewer` (P1:51).

### R-070
- **Statement:** Nothing can be called that takes a member and returns whose maps they are on.
- **Type:** auto · **Applies to:** API
- **Source:** P1:51, FS:235
- **How to check:** List every function and route that takes a user id and touches layer data. None may return owners for a given member.

### R-071
- **Statement:** No screen or copy shows a person their ring on someone else's map, directly or by implication: no "you're in X's inner circle", no closeness badge or colour on their own avatar in someone else's view, no "you moved closer" or "further away", no ordering of someone else's content by the viewer's ring.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:74, FS:164, MJC:422
- **How to check:** Review every screen as a member, not the owner. Grep aid: `inner circle`, `closest`, `close friend`, `your ring`, `moved (in|out|closer|further)`. See G-12.
- **Provisional default:** Decisions-Needed B12 (switchable, R-147): Walking a path shows the photos where the reader appears, in journey order, with no total and no grouping (other setting: hidden). Holds as written under both settings. Under "shown", the "where you appear" view is checked as R-139 says
- **Provisional default:** Decisions-Needed B11 (switchable, R-146): "Path crossed" names both people, reaches the owner's network, and never says which ring (other setting: unnamed). Holds as written under both settings: the named person learns they crossed the owner's path, never their ring (R-092)

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
- **How to check:** Long Way Round → Open Hands in Round #1 (Hands had no journey then): Hands on Round's map, middle.

### R-076
- **Statement:** Tags in Private photos count towards rings.
- **Type:** auto · **Applies to:** data
- **Source:** FS:277 (§20 G), P1:27 (D14), P1:156
- **How to check:** Lantern #1 tags Wind in 6 photos, 2 of them private: Wind is tight, which needs all 6.

### R-077
- **Statement:** In each finished journey, a user tagged in 5 or more photos is tight, 2 to 4 is middle, 1 is outer.
- **Type:** auto · **Applies to:** data
- **Source:** FS:161, FS:277, P1:28 (D15), CL:107
- **How to check:** Boundary cases 1, 2, 4, 5. Fixture: Lantern's map of Wind across #1–#5 (P1:259–265).

### R-078
- **Statement:** Someone on the map who is not tagged in a finished journey moves out one ring. Outer stays outer. Nobody is ever removed from a map.
- **Type:** auto · **Applies to:** data
- **Source:** FS:165, FS:277, P1:28 (D15), P1:157, CL:107
- **How to check:** Lantern #3 and #4: Wind goes middle → outer → outer, and is never absent from Lantern's map.

### R-079
- **Statement:** Someone tagged again with fewer photos goes straight to the ring that count gives.
- **Type:** auto · **Applies to:** data
- **Source:** FS:282 (§20 L), P1:343 (R1)
- **How to check:** Tight last journey, tagged once this journey: outer.

### R-080
- **Statement:** Maps change only when the owner finishes a reveal. Nothing on any map changes during a sealed year, at unlock, or for a reveal never finished.
- **Type:** auto · **Applies to:** data
- **Source:** FS:91, FS:162, FS:269, P1:150
- **How to check:** Jump the clock through a full sealed year with captures and through an unlock: layer rows unchanged. They change only at a reveal-finished event.

### R-081
- **Statement:** Closeness is earned by tags, never chosen. There is no follow, friend request or hand-picked list of close people.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:160, P1:180 ("follower"). Part of **§2.5 check 6**
- **How to check:** Schema scan for `follow`, `follower`, `friend_request`, `close_friend`. No UI control adds a person to a ring.

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

### R-084
- **Statement:** The feed carries only three kinds of announcement: journey launched, reflection left, path crossed.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:171–175, CL:109, MP:83, P1:31 (D18), P1:168. **= §2.5 check 9** (types)
- **How to check:** Schema: the announcement type allows exactly these three values. Inserting any other raises.

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

### R-089
- **Statement:** "Journey launched" and "path crossed" are shown to the owner's network.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:282 (§20 M), P1:344 (R2)
- **How to check:** For a fixture reveal finish, the set of feeds containing each announcement equals the owner's map members.

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

---

## 8. Engagement mechanics

### R-097
- **Statement:** There are no streaks: no count of consecutive days, weeks or months, no "don't break the chain", no flame.
- **Type:** auto · **Applies to:** data, UI, copy
- **Source:** CL:69, MP:42, FS:233, P1:180. Part of **§2.5 check 6** (streak)
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
- **Source:** P1:53, P1:180, CL:69. Part of **§2.5 check 6** (like, reaction, view)
- **How to check:** Schema scan for `like`, `reaction`, `heart`, `view`, `view_count`, `impression`. UI review for heart or reaction controls.

### R-101
- **Statement:** No user has a score, rank, level, tier, badge or position on a leaderboard, and no data compares users.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:71, MP:44, FS:185, FS:244, P1:53, P1:180. Part of **§2.5 check 6** (score, rank, badge)
- **How to check:** Schema scan for `score`, `rank`, `level`, `tier`, `badge`, `achievement`, `points`, `leaderboard`, `xp`.

### R-102
- **Statement:** The circle and its rings are a record, not a rank. No screen or copy compares users, ranks them, names a level or tier, or treats more rings as better.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:71, CL:111, FS:185, FS:244, MJC:689–694
- **How to check:** Review profiles and the circle. Grep aid: `level`, `rank`, `top`, `ahead`, `behind`, `veteran`, `elite`, `unlock achievement`.

### R-103
- **Statement:** The Positivity Feed draws only on Public photos and is filtered by endurance and gratitude tags, never ordered or filtered by popularity.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:202–203, P1:317. See G-8 and G-14
- **How to check:** As First Light, the feed holds only public photos with the listed tags. Its query uses no read, like, view or count measure for order or selection.
- **Decided 2026-10-30 (FS §20 W):** the drafted tag list is the four working tags (`MJC:454–459`). **(FS §20 Y):** no chapter filter on the Positivity Feed; B9 (d) is replaced.
- **Provisional default:** Decisions-Needed B9: Positivity Feed: (a) reflection text only, with the photo shown when opened; (b) per-photo visibility; (c) drafted tag list only; (d) chapter filter available; (e) newest first; (f) only after reveal finished. Under B9 the check reads: the feed holds only photos that are themselves Public (b), from journeys whose reveal is finished (f), tagged with a tag from the drafted list, never free text (c), newest first (e), and may be filtered by chapter (d). Any other reader-side filter has no default and goes to the supervisor, not into the build. Under (a) "text only" each entry shows reflection text and no image until the reader opens it; opening one shows one photo. (a) was decided 2026-10-30 (FS §20 Q): text only, not switchable (R-145; before 2026-10-30 this line read "The (a) setting is switchable"). Add the cases: a Public photo in Long Way Round #4 (reveal never finished) is absent; a Network photo in a journey with other Public photos is absent; the feed order equals reverse time order with no other key
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
- **Source:** P1:184, P1:193. **= §2.5 check 10**
- **How to check:** Grep outside the clock module for `Date.now(`, `new Date()` with no argument, `performance.now`, `time.time`, `datetime.now`, and in SQL `now()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`, `LOCALTIMESTAMP`, `clock_timestamp`, `statement_timestamp`, `transaction_timestamp`, including column defaults.

### R-116
- **Statement:** Every time rule follows the app clock: the seal, unlock, reflection slots, the note window, highlight ends, the cadence month and Commit.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:193, FS:299
- **How to check:** Set the app clock to a date far from the real one and run R-001, R-036, R-040, R-046 and R-121. Each must behave as of the app clock.

### R-117
- **Statement:** The time control moves forward only. To see an earlier moment, it resets to the 2026-10-25 baseline and jumps again.
- **Type:** auto · **Applies to:** API, UI
- **Source:** P1:194, P1:200
- **How to check:** Request a backward jump: refused. Reset: clock equals baseline and fixture state equals the baseline load.

### R-118
- **Statement:** A journey unlocks exactly 12 months after its commit moment, and at any app-clock time its state matches the clock with no job having to run.
- **Type:** auto · **Applies to:** data
- **Source:** FS:36, FS:273 (§20 C), P1:14 (D1), P1:74, P1:196, CL:87
- **How to check:** For each fixture journey, unlock = commit + 12 months. Jump to unlocks_at with all scheduled jobs disabled: the journey reads as unlocked. See G-18.
- **Provisional default:** Decisions-Needed B16: A commit on the 29th–31st uses the last day of shorter months. One time zone for the prototype (UTC). Add the cases, all in UTC: commit 2026-01-31 → month 2 starts 2026-02-28; commit 2028-02-29 → unlock 2029-02-28; the unlock moment carries the commit's time of day

### R-119
- **Statement:** On each clock jump, scripted fixture actions dated up to the new time are applied first, then maps are computed for reveals finished since the last jump, then announcements go out.
- **Type:** auto · **Applies to:** data
- **Source:** P1:195–199
- **How to check:** Jump from baseline to 2027-05-01. Second Wind's #6 reveal (2027-04-25) is applied, Lantern is on Wind's map at middle, then the announcements exist with times after the map entry.

### R-120
- **Statement:** Capture times, reflection and overview times, highlight starts and Commit times come from the app clock, never from the client.
- **Type:** auto · **Applies to:** API
- **Source:** P1:73, P1:90, P1:115, P1:132
- **How to check:** Send each write with a client timestamp a year off. The stored time equals the app clock.

### R-121
- **Statement:** All photos of a journey share reflection slots: slot k runs from unlock + (k − 1) years to unlock + k years, and each photo takes at most one reflection per slot. The slot is worked out from the app clock, never chosen by the client.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:97, FS:101, FS:274 (§20 D), P1:22 (D9), P1:115, CL:105. See G-1
- **How to check:** For Lantern #1 (unlock 2022-01-01), a reflection on 2023-12-31 is slot 2 and one on 2024-01-01 is slot 3, for every photo regardless of capture date. A second reflection in the same slot is refused. A client-supplied slot is ignored.

### R-122
- **Statement:** Each journey takes at most one overview per slot, on the same slot windows as reflections.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:117, FS:275 (§20 E), P1:23 (D10), P1:124. See G-15
- **How to check:** Second overview in one slot: refused. Fixture count: Steady Lantern has 15 (P1:301).
- **Provisional default:** Decisions-Needed B13: The slot 1 overview can be written after the reveal is finished, within the slot. Readable by the network only. Add the case: Steady Lantern writes a slot 1 overview on Lantern #5 after its reveal is finished and before unlock + 1 year: accepted. G-15 is being fixed by A6 (2026-10-27); this check already tests the corrected wording

### R-123
- **Statement:** The months that set the frame limit are counted from the journey's own commit date, not from calendar months.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261 (§20 mechanics 1), P1:18 (D5), CL:95
- **How to check:** Commit on the 20th. Month 1 runs to the 20th of the next month: a capture on the 1st of the next calendar month is still month 1. See G-18.
- **Provisional default:** Decisions-Needed B16: A commit on the 29th–31st uses the last day of shorter months; UTC. Add the case: commit on 2026-01-31 (UTC); month 2 starts 2026-02-28, month 3 on 2026-03-31

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
- **How to check:** Read copy shown with hard-chapter journeys (Long Way Round #1–#2, P1:234–235).

### R-130
- **Statement:** The site and the product say plainly and early that we are not trying to get users onto the app.
- **Type:** review · **Applies to:** copy
- **Source:** CL:76, MP:49, MP:138, BP:126
- **How to check:** Check the site's first screen and the app's first-run copy.
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
- **Source:** P1:173 ("Each one fails the build"), BP:203, CL:78
- **How to check:** Map each auto R-ID to a test in the suite. An auto check without a test is a finding.

---

## 14. Provisional defaults and the options panel

Added 2026-10-27 for the playable prototype (rule zero, CL:19–24; `Decisions-Needed.md` "Provisional defaults in force"). Seven defaults were switchable: B2, B4, B5, B9 (a), B11, B12, C6. **2026-10-30:** B9 (a) decided as text only (FS §20 Q); six remain. Each switch must keep the banned list under **both** of its settings, so the user can compare them without the comparison itself breaking a rule.

### R-141
- **Statement:** The prototype options panel holds only the time control, the viewer switcher with the simulated date, and the six switchable defaults (B2, B4, B5, B11, B12, C6; B9 (a) was decided 2026-10-30, FS §20 Q, and has no switch; before 2026-10-30 this read "seven"). Each switch offers exactly its two documented settings, starts on the provisional default, and changes nothing but the behaviour its ID names.
- **Type:** auto · **Applies to:** UI, API
- **Source:** CL:23, DN "Provisional defaults in force" (Switchable column), DN C16, CL:24
- **How to check:** List the panel's controls from the DOM and from code. Compare with the Switchable column: no extra switch, none missing, and no setting beyond the two listed (no "both", "auto" or free value). On first load each switch is on the first-listed setting, which is the default. Flip each switch alone and diff every read endpoint for every fixture user: only the behaviour named by that ID changes (R-142 to R-148). The panel is itself a data path under R-014: it shows no count, photo or field from a sealed journey, and the viewer switcher lists fixture users by name only, with no picture (C7).

### R-142
- **Statement:** B2, under both settings ("from unlock" / "only after reveal finished"): nothing from a sealed journey is readable by anyone. The setting changes only who besides the owner may read an unlocked journey whose reveal is not finished: under "from unlock", the network reads photos not set Private and anyone signed in reads photos already set Public (B3, B14); under "only after reveal finished", no one but the owner reads any of it, Public photos included (**decided 2026-10-30, FS §20 R**). Before 2026-10-30 the statement read: "B2, under both settings ("from unlock" / "only after reveal finished"): nothing from a sealed journey is readable by anyone, and the setting changes only when the owner's network may read an unlocked journey's Network-default photos."
- **Type:** auto · **Applies to:** data, API
- **Source:** DN B2, FS §20 R, FS:151, FS:269, P1:311, CL:73 (nothing leaks), CL:24
- **How to check:** Under each setting: R-001 to R-008 pass for Lantern #6 at 2026-12-31 23:59:59. As Open Hands at baseline, read a Long Way Round #4 photo (reveal never finished): "from unlock" allowed, "only after reveal finished" refused. In a test copy, set one Long Way Round #4 photo Public (B3: takes effect when made) and read it as Open Hands and as First Light: "from unlock" allowed to both, "only after reveal finished" refused to both (FS §20 R); the owner reads it under both. This is a test-copy change, not a fixture change: the approved fixtures (P1 §3) are not edited, and a standing fixture for this case goes to the supervisor. Every Lantern #5 cell of the §3.6 matrix (reveal finished) is identical under both settings (R-068).

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

### R-147
- **Statement:** B12, under both settings ("shown" / "hidden"): Walking a path never gives a reader a total, grouping or ordering of the photos they appear in, and never shows a photo the reader cannot otherwise read.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** DN B12, FS:196, FS:164, CL:74, P1:51. See R-139 and G-12
- **How to check:** As Second Wind on Lantern #1 (Wind tagged in 6, 2 of them private). "Shown": only the tagged photos Wind can read appear (not the 2 private ones, R-065), in journey order, with no count, total, "n of", pagination total or grouping in the DOM, and no count field in the API response. "Hidden": no "where you appear" view, route or response field exists for a reader. Under both, R-139 passes. Every audit of "shown" reports R-139's residual risk (a reader can count by scrolling) as its weakest point.

### R-148
- **Statement:** C6, under both settings ("hidden" / "shown"): no reader can total, group or rank how often a person is tagged, and no tag on a photo the reader cannot read is revealed.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** DN C6, FS:164, FS:277, CL:74, CL:24. See R-139
- **How to check:** As Open Hands on Lantern #1. "Hidden": no person tag appears in any screen or API response for a photo Hands does not own; under the strictest reading (CL:24) it is absent from the data sent, not only from the UI. "Shown": person tags appear only on the single photo they belong to; no journey-level list, count, grouping or ordering by person (R-139); tags on photos Hands cannot read are absent. C6's question also asks whether a tag leads to that person's profile. No default answers that, so a tag that links to a profile is a finding until the supervisor answers (R-134).

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

### R-150
- **Statement:** A deliverable (doc or code) describes every question that `Decisions-Needed.md` answers with a provisional default under that default only, worded as the table row states it, and labelled `PROVISIONAL: <ID>`. It never calls such a question open or "no default", never states a default range that leaves out rows in the table, never describes the other side or a third reading as what the screen holds, and never extends a default or a switch setting to cases its row does not name.
- **Type:** auto (labels and cross-references) and review (wording) · **Applies to:** copy, UI, data, API
- **Source:** CL:19–24 (rule zero: "build that, and nothing else"), CL:30, DN "Provisional defaults in force". R-149 covers labels in code only; R-135 covers picking a side. Found by `docs/reviews/2026-10-30-rules-screen-inventory-r1.md` finding N1 (B17–B19 missing from `Screen-Inventory.md`) and N2 (B2's option extended to Public photos)
- **How to check:** From the repo root, for a deliverable `F`:
  1. Every table ID is labelled in `F` if `F` touches its question. List table IDs not labelled in `F`, then read each against `F`: `comm -13 <(grep -oE 'PROVISIONAL: [BC][0-9]{1,2}' F | grep -oE '[BC][0-9]+' | sort -u) <(grep -oE '^\| [BC][0-9]{1,2} \|' docs/Decisions-Needed.md | grep -oE '[BC][0-9]+' | sort -u)`
  2. Every row that says "Raised as ... OQ-n" is named in `F`'s OQ-n status line. Must print nothing: `grep -oE '^\| [BC][0-9]+ \|.*Raised as[^|]*' docs/Decisions-Needed.md | while read -r l; do id=$(echo "$l" | grep -oE '^\| [BC][0-9]+' | grep -oE '[BC][0-9]+'); for n in $(echo "$l" | grep -oE 'OQ-[0-9]+' | grep -oE '[0-9]+'); do awk -v n="$n" -v id="$id" '$0 ~ "^"n"\\. "{f=1;next} f && /^[0-9]+\. /{exit} f && index($0,id){ok=1} END{if(!ok) print "OQ-"n" lacks "id}' F; done; done`
  3. Grep `F` for `no default`, `still open, no ID` and `B1–B1[0-9]` ranges, and confirm each against the table.
  4. Review: each labelled passage says what its row says, no more. A reading the row does not state (for example, what a switch setting does to a case the row does not name) is raised as a question, not built.

---

## Banned-list coverage

Every row of the banned list (`CLAUDE.md:64–74`, `Master-Prompt.md:37–47`) and the checks that cover it.

| Banned item | Checks |
|---|---|
| No retakes | R-031, R-005, R-018, R-019, R-029, R-124 |
| No edits to reflections | R-015, R-016, R-124 |
| No comments from anyone else | R-105, R-106, R-107, R-109, R-124 |
| No face recognition | R-110, R-111, R-112 |
| No ads anywhere | R-113 |
| No streaks, counters, progress bars, reminders | R-097, R-098, R-099, R-038, R-039, R-012, R-013, R-095, R-096, R-124, R-138, R-140, R-143, R-144 |
| No re-engagement notifications | R-094, R-095, R-096 |
| No ranking, levels, badges, leaderboards | R-101, R-102, R-103, R-124, R-143 |
| No photo feed | R-084, R-085, R-086, R-145 |
| Nothing leaks from a sealed year | R-001 to R-014, R-091, R-138, R-142, R-144 |
| No layer is ever shown to the person on it | R-069, R-070, R-071, R-092, R-139, R-146, R-147, R-148 |

R-141 and R-149 apply to every row: no switch setting may break any item above, and every provisional default in code is labelled and traceable. R-138 sits under two rows because a control hidden or greyed for lack of frames is both a counter and a leak of how much a sealed year holds (RG:28, "disabled-but-visible states").

R-150 applies to every row as well: a deliverable that leaves out or stretches a provisional default can carry a banned item in by that route.

## `Phase-1-Proposal.md` §2.5 mapping

| §2.5 check | Line | R-IDs |
|---|---|---|
| 1. No UPDATE or DELETE on reflection, overview, note, photo, journey, user name, journey_reveal | P1:175 | R-015, R-017, R-018, R-020, R-021, R-022, R-023 |
| 2. No visibility, tag or chapter insert after reveal finished | P1:176 | R-052 |
| 3. No second Commit while sealed | P1:177 | R-026 |
| 4. Owner before unlock: 0 rows, count 0, ciphertext | P1:178 | R-001, R-002, R-003 |
| 5. capture() and start_highlight() return no number | P1:179 | R-038 |
| 6. No comment, reply, like, reaction, caption, score, rank, streak, badge, view, follower | P1:180 | R-105 (comment, reply), R-100 (like, reaction, view), R-108 (caption), R-101 (score, rank, badge), R-097 (streak), R-081 (follower) |
| 7. B reads no layer row with owner ≠ B; A's tag never touches B's map | P1:181 | R-069, R-072 |
| 8. Typed-name tag never makes a layer row | P1:182 | R-073 |
| 9. Announcements: no media, three types | P1:183 | R-084, R-085 |
| 10. Only the clock module reads the system clock | P1:184 | R-115 |
| 11. No face or vision library | P1:185 | R-110 |

---

## Gaps

Rules that could not be made testable, and places where the sources disagree. None of these is decided here. Each needs the user.

Since 2026-10-27 each gap carries a status line under it: **being fixed** by a `Decisions-Needed.md` section A correction (approved by the user), covered for the prototype by a **provisional default**, **partly covered**, or **still open**. A provisional default is not a decision. A gap is closed only when the user decides and `FS` §20 records it, and even then it stays here, marked, because the rubric never shrinks.

### Contradictions between sources

**G-1. Reflection slot dates.** The example at `FS:104–111` dates reflections from the photo's own capture date (7 Jan each year). `FS:101` and `FS:274` (§20 D) say all photos of a journey move slot together on the journey's unlock anniversary, and `MJC:852` agrees. The same per-photo example is in `MJC:200` and `MJC:203–210`. R-121 tests the §20 D wording; the example needs correcting or confirming.

**Being fixed by A1, 2026-10-27** (`Decisions-Needed.md` section A, approved). R-121 already tests the corrected wording. Kept here because the rubric never shrinks.

**G-2. "Publish".** `FS:141` says visibility is "chosen at publish time", and `MJC:365–367`, `MJC:424` and `MJC:440` speak of publishing a journey. No step called publish exists. The decided terms are "reveal finished" (`FS:151`, `FS:276`) and "journey launched" (`FS:280`). Also `MJC:401` says layers are calculated when journeys are "uploaded", against `FS:162` (when a reveal is finished). Learnings open questions 1 and 2.

**Being fixed by A4, 2026-10-27** (the "uploaded" layers line, `MJC:401`). **Provisional default:** Decisions-Needed B1: "Publish" means "reveal finished"; docs use only "reveal finished" and "journey launched". Under B1 a step, control or copy called "publish" in the build fails R-134.

**G-3. Close friends.** `MJC:807` says close friends "get everything", and `MJC:383` says "everything for the people closest to you". `FS:278` (§20 H), `FS:150` and `MJC:864` say they see nothing beyond the rest of the network. R-064 tests §20 H.

**Being fixed by A3, 2026-10-27.** R-064 already tests §20 H.

**G-4. When reminders, counters and progress bars are banned.** `FS:233` says "No visible counters, no progress bars, no reminders **during the sealed year**". `CLAUDE.md:69` and `Master-Prompt.md:42` ban them with no time limit, and `FS:242` bans reminders to capture, reflect or return at any time. Open: is a counter or progress bar allowed after unlock, for example "12 of 24 reflected" during the reveal? R-099 is provisional on this.

**Provisional default:** Decisions-Needed B8: Counters and progress bars are banned at all times, not only while sealed. R-099 is firm under B8.

**G-5. Showing the quota.** `FS:243` bans showing the quota left "in a way that reads as a target", which implies some way of showing it may be allowed. `P1:49` says frames used and left are never stored or returned, and `CLAUDE.md:69` bans counters. Open: may the owner ever see how many frames they have left?

**Provisional default:** Decisions-Needed B7: Frames left are never shown. A refused capture says so with no number (copy in Phase 2). R-038, R-098 and R-138 are firm under B7.

**G-6. Stored journey fields.** `FS:15` lists "frames used", "highlights used" and a state "committed / sealed / unlocked" as journey properties. `P1:49` says frame and highlight counts are never stored, and `P1:76–84` says state is derived, with "committed" folded into sealed. R-039 tests P1.

**Being fixed by A5, 2026-10-27.** R-039 already tests P1.

**G-7. What adds a ring to the circle.** `FS:185` says one ring "per year with the app", and `MJC:687` says "each year with the app adds a ring". `P1:65` says one ring "per journey whose reveal is finished". These differ for a user with a year and no journey, or a reveal never finished (Long Way Round #4).

**Provisional default:** Decisions-Needed B4 (switchable): One ring per finished reveal (`P1:65`); other setting: per year with the app. R-143 must pass under both settings. The contradiction stays open until the user decides.

**G-8. The Positivity Feed and "no photo feed".** `CLAUDE.md:72` and `Master-Prompt.md:45` say "No photo feed. The feed carries announcements only, never images". The Positivity Feed is fed by public photos and their reflections (`FS:203–204`, `P1:317`). Open: does the Positivity Feed show photographs, and if so how does that fit the ban? Also `FS:203` says it draws from "journeys set to public", while visibility is per photo (`FS:141`); `MJC:375` and `MJC:379` show the same split. And `MJC:244` says "no feed", against `FS:169–177`.

**Decided 2026-10-30 (FS §20 Q):** "No photo feed" covers the Positivity Feed. Text only; a photo shows only when one entry is opened. The "with photographs" setting is removed.

**Provisional default (before 2026-10-30):** Decisions-Needed B9: (a) reflection text only, with the photo shown when opened, switchable to "with photographs"; (b) per-photo visibility; (c) drafted tag list only; (d) chapter filter; (e) newest first; (f) only after reveal finished. Covers the per-photo split (b, R-067) and, under the default, the image question (a, R-103). **Not covered:** whether the "with photographs" setting fits "No photo feed" (R-145 reports it as a finding), and the `MJC:244` "no feed" line, which no section A item corrects.

**G-9. Images in the announcement feed.** `CLAUDE.md:72` says "never images". `FS:171` says "No photographs in the stream". Open: may an announcement show the actor's profile picture?

**Provisional default:** Decisions-Needed C7: No profile picture is shown anywhere; announcements carry no image. R-086 is firm under C7.

**G-10. Profile picture and looks.** `FS:13` and `P1:62` give each user a profile picture. `FS:29` and `Master-Prompt.md:113` say nothing on a profile signals how the person looks. Open: what may the profile picture be?

**Provisional default:** Decisions-Needed C7: No profile picture is shown anywhere. The profile shows the name in the circle. R-126 is read under C7. The profile picture field in `FS:13` and `P1:62` still exists in the approved model; the default only stops it being shown.

**G-11. Choices made during a reveal that is never finished.** `FS:269` says an unfinished reveal has "no chapter, no tags", and `P1:25` and `MJC:855` say "the photos stay Network". But choices are inserted, once each, during the reveal (`FS:286` §20 P, `P1:46`, `P1:143`, `P1:165–166`, `P1:347`). Open: if the owner sets a photo to Private, or sets a chapter, and never finishes, does that choice take effect? R-054 tests only what all sources agree on.

**Provisional default:** Decisions-Needed B3: Each reveal choice takes effect when made. A reveal can be finished at any later time. R-051 and R-054 are read under B3.

**G-12. Walking a path can show a ring.** `FS:196` says the reader sees where they themselves appear in someone's journey. Counting those photos lets a reader estimate their ring on that person's map (5+ tight), against `FS:164`, `CLAUDE.md:74` and `P1:51`. Private tags count but stay hidden (`FS:277`), so the estimate is a floor, not exact. Open: is that acceptable, or should the "where you appear" view not total up?

**Provisional default:** Decisions-Needed B12 (switchable): Walking a path shows the photos where the reader appears, in journey order, with no total and no grouping; other setting: hidden. **Partly covered:** under "shown" a reader can still count by scrolling, so the floor estimate this gap describes remains. R-139 and R-147 report it as the weakest point until the user decides. Under "hidden" the gap does not arise.

**G-13. Highlights during the sealed year.** `P1:48` seals photo, note, tag and reflection rows, but not highlight rows. A readable highlight record would tell others that, and when, a user started one, against `FS:246` and `FS:279` (§20 I). R-008 already requires that others see nothing, so the gap is in the current implementation. Open for the owner: may the owner see that a highlight is open and when it ends? A running "ends in 3h" would be a counter (`CLAUDE.md:69`); a plain open-or-closed is not addressed anywhere.

**Provisional default:** Decisions-Needed B6: Others learn nothing about highlights. The owner sees only "a highlight is open", with no end time and no countdown. Covers both halves: R-008 (others) and R-009, R-138, R-140 (owner) are read under B6. The implementation gap remains: `P1:48` does not seal highlight rows, so the build must keep them unreadable to others without changing the approved model (CL:28); any model change goes to the supervisor.

**G-14. Feeling tags.** `FS:131` says feeling tags are written "inside a category", and `P1:141` stores them as (journey, free text) with no category. `FS:131` also says popular feeling tags "surface over time", while `FS:202` says the Positivity Feed is "never by popularity". Open: how a tag surfaces, and whether that uses any measure of popularity.

**Partly covered.** **Provisional default:** Decisions-Needed B9 (c) and (e): only the drafted tag list qualifies for the Positivity Feed, newest first, so the feed is never ordered by popularity (R-103). **Still open:** `FS:131` "inside a category" against `P1:141` (no category), and how popular feeling tags "surface over time" without a popularity measure. No default covers either; a build that surfaces tags by how often they are used fails R-134.

**Provisional default (added 2026-10-27, fdb83d3):** Decisions-Needed B17: Feeling tags are free text on the journey, with no category, as in the approved model (`P1:141`). Decisions-Needed B18: Tags never "surface" by popularity; no suggestions and no counts (`FS:202` over `FS:131`). With B9 (c) and (e) these cover the whole gap for the prototype. A deliverable that still offers a category-bound feeling tag, or treats popular surfacing as open, fails R-135 and R-150.

**G-15. When an overview is written.** `FS:118` (and `MJC:218`) says the overview is "written at reveal". `FS:275` (§20 E) says a new one every year on each journey. R-122 tests §20 E.

**Being fixed by A6, 2026-10-27.** R-122 already tests §20 E. Decisions-Needed B13 adds when slot 1 may be written (R-122).

**G-16. "Your Journey is ready."** `BP:79`, `Master-Prompt.md:138` and `MJC:740` name this as a key microcopy moment. `FS:236` bans "re-engagement notifications of any kind", and `MJC:156` contrasts the reveal with "an unlock notification with nothing to do". Open: is "Your Journey is ready" a notification sent at unlock, or only text shown when the user next opens the app? R-094 bans the notification until the user decides.

**Provisional default:** Decisions-Needed C1: "Your Journey is ready" appears on next open, never as a notification. R-094 is firm under C1.

**G-17. What the owner sees of a sealed journey.** `FS:74` says nothing in a sealed journey is visible "not to the user". `P1:84` lets the owner see its type, commit date and unlock date. These may agree (dates are about the journey, not in it), but it is worth confirming, together with whether showing the unlock date is allowed at all given the countdown ban (R-013).

**Provisional default:** Decisions-Needed C2: The unlock date is shown as a plain date, never relative ("in 64 days"). R-009 and R-013 are read under C2. B6 adds one more thing the owner may see of a sealed journey: that a highlight is open (R-009).

**Provisional default (added 2026-10-27, fdb83d3):** Decisions-Needed B19: The owner of a sealed journey sees its type, commit date and unlock date and nothing else (`P1:84`; `FS:74` read as covering the contents). R-009 is read under B19. B19's "nothing else" and B6's highlight state read against each other. **Decided 2026-10-30 (FS §20 S):** B6 holds.

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
