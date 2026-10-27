# My Journey: Rules Rubric

Owner: Rules Guardian (`.claude/agents/rules-guardian.md`). Build Plan Phase 1 deliverable, "The rules list as testable statements, one line each" (`Build-Plan.md:63`).

Version 1, 2026-10-27. No code exists yet. Nothing below has been audited.

---

## What this is for

Every later audit and every rules test runs against this list. Each check states a behaviour the product guarantees, written so that an auditor can decide it and a test author can automate it.

- **auto**: a test, scan or script can decide it. These must run in the build and fail it (R-137)
- **review**: a person has to read the screen, copy or design to decide it

The stack and database host are not decided yet (`Status.md` Open decisions 1, L-004). Each statement describes behaviour. Where a check names Postgres grants, triggers or row-level security, that is the **current implementation** from `Phase-1-Proposal.md` §2.1, recorded so the test author knows where the rule lives today. If the stack changes, the statement stays and the mechanism changes.

## How the rubric grows

- **It never shrinks.** No check is deleted. A check that stops applying is marked `Superseded by R-nnn on <date>` and stays in place (`Build-Plan.md:222`)
- **It never renumbers.** A new check takes the next free number and goes under its area heading, so numbers inside an area need not be consecutive
- **Every finding becomes a check.** When an audit finds a new kind of violation, the check is added here before the audit report is closed (`Build-Plan.md:220–222`)
- A check marked **Provisional** depends on a contradiction listed under Gaps. It runs as written until the user settles the gap, then it is confirmed or superseded

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

`docs/Overview.md` is historical and is never cited.

Test fixtures named below come from `Phase-1-Proposal.md` §3. Steady Lantern #6 (committed 2026-01-01, unlocks 2027-01-01) is the standard sealed journey. Baseline is 2026-10-25.

---

## 1. Sealing and leaks

### R-001
- **Statement:** As the owner, before unlock, no query or endpoint returns any photo row, photo count or photo image from the sealed journey.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:64, CL:72, FS:74–75, FS:234, P1:48. **= §2.5 check 4** (rows and count)
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
- **Source:** CL:64 ("Not thumbnails"), MP:46, FS:75, FS:234
- **How to check:** In a browser test, capture one photo and one note, then (a) scan server storage for files with image signatures that belong to the sealed journey, (b) grep server logs for base64 image data, (c) list Cache Storage, IndexedDB and localStorage and confirm no image bytes, (d) confirm every `URL.createObjectURL` made during capture has been revoked. Grep the capture path for resize, thumbnail, `sharp`, `jimp`, `canvas.toBlob` writes that are kept.

### R-005
- **Statement:** Once the shutter is pressed, the app shows nothing of the photo just taken: no preview, no "last shot" corner thumbnail, no review screen.
- **Type:** auto · **Applies to:** UI
- **Source:** FS:58, FS:74, FS:228 ("no review-before-save"), CL:90 ("Sealed instantly")
- **How to check:** UI test: after the shutter tap, no `img`, `canvas`, `video` or CSS background in the DOM is sourced from the captured frame. The live viewfinder before the tap is allowed. Same after the note photo is taken.

### R-006
- **Statement:** Nothing shows or returns how many photos a sealed journey holds, in any form: a number, "3 moments captured", "n frames", "n of 24", tally marks, dots, a list length, a pagination total, or a response whose size grows with the count.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** CL:64, MP:46, FS:75, FS:243, FS:246
- **How to check:** (a) Grep all copy and templates for `moments? captured`, `\d+\s*(photos?|moments?|frames?|shots?|pictures?)`, `\bof \d+\b`, `frames? (left|used|remaining)`, `so far`. (b) As owner and as another user, call every endpoint about a sealed journey holding 0 photos and one holding 17 (Open Hands #4): the responses must be byte-identical apart from ids. (c) Review every screen showing a sealed journey for any visual tally.

### R-007
- **Statement:** A sealed photo never appears as a placeholder: no blurred, greyed, locked, disabled-but-visible or silhouette tile stands for it.
- **Type:** auto · **Applies to:** UI
- **Source:** FS:75 ("No previews ... no thumbnails"), CL:64
- **How to check:** Render the sealed-journey view for a journey with 0 photos and one with 17. The DOM trees must be identical. Review the sealed-year empty state for per-photo shapes.

### R-008
- **Statement:** Anyone other than the owner learns only that a sealed journey exists: a single yes or no. Not its type, commit date, unlock date, highlights, frames used or when anything was captured.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:246, FS:279 (§20 I), P1:30 (D17), P1:84, CL:92
- **How to check:** As Second Wind, call every endpoint and open every screen about Steady Lantern during Lantern #6. Compare with the same calls about First Light (no journey). The only difference allowed is the journey-underway flag.
- **Current implementation:** `has_journey_underway(user)` returns true or false (P1:84).

### R-009
- **Statement:** The owner of a sealed journey sees its type, commit date and unlock date, and nothing else about it.
- **Type:** auto · **Applies to:** API, UI
- **Source:** P1:84, FS:74. See G-17
- **How to check:** As Steady Lantern before 2027-01-01, list every field returned about Lantern #6. Anything beyond type, commit date, unlock date and identifiers fails.

### R-010
- **Statement:** A capture changes nothing that any reader can observe, the owner included: no "last captured", "active today", "captured this week", recent-activity mark or announcement.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:246, FS:74, CL:64
- **How to check:** As Lantern, Second Wind and First Light, snapshot every read endpoint about Lantern. Capture a photo as Lantern. Snapshot again. Every snapshot must match its earlier one. The capture call's own `accepted` reply is the only thing that differs.

### R-011
- **Statement:** The activity graph for a journey is never shown or returned while that journey is sealed. It appears only after the year unlocks.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:187, CL:102, MP:85, P1:50
- **How to check:** As owner and as a network member before 2027-01-01, request activity data for Lantern #6 (expect none) and render Lantern's profile (no activity element for #6). After unlock, expect it.
- **Current implementation:** built from `captured_at`, unreadable while sealed (P1:50).

### R-012
- **Statement:** During a sealed year nothing fills, grows or advances to show how far the year or the quota has got: no progress ring or arc on the circle for the current year, no "month 7 of 12", no elapsed-time bar, no grid being filled.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:186–187, FS:233, CL:60, CL:102
- **How to check:** Review the profile circle and every journey screen at several simulated dates inside one sealed year (for example 2026-02-01, 2026-07-01, 2026-12-31). Nothing may differ between those dates except the plain unlock date. Grep aid: `<progress`, `role="progressbar"`, `aria-valuenow`, `stroke-dashoffset` or arc angles computed from the date.

### R-013
- **Statement:** There is no countdown to unlock: no "n days to go", "unlocks in", timer or ticking display. The owner may see the unlock date as a date.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:60 (counters), FS:233 ("No visible counters"), RG:28 ("timers counting down to unlock"), P1:84 (date shown to owner). See G-17
- **How to check:** Grep copy and code for `days? (left|to go|until|remaining)`, `unlocks? in`, `countdown`, `time left`, `\d+\s*d\s*\d+\s*h`, and any `setInterval` or `requestAnimationFrame` that formats a time until `unlocks_at`.

### R-014
- **Statement:** Every path that can return data applies the seal: search, export, error messages, logs shown to users, debug and admin routes, and the time-control panel.
- **Type:** auto · **Applies to:** API, UI
- **Source:** CL:72 ("unreadable, not merely hidden in the UI"), FS:234
- **How to check:** Build the route list from the code. Run the R-001 and R-008 tests against every route. Trigger each capture refusal and confirm the error text holds no number and no photo data.

---

## 2. Immutability and append-only

### R-015
- **Statement:** Nobody, the owner and the app's own role included, can change or delete a reflection once it is written.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:56, CL:71, MP:38, FS:99, FS:229, P1:44. **= §2.5 check 1**
- **How to check:** As the app role, run UPDATE, DELETE and TRUNCATE on the reflection store: each raises. Confirm no API route accepts an edit or delete of a reflection.
- **Current implementation:** INSERT and SELECT grants only, plus a trigger that raises on UPDATE, DELETE and TRUNCATE (P1:44).

### R-016
- **Statement:** No screen offers to edit, delete, undo or replace a saved reflection.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:56, FS:99
- **How to check:** UI test on a photo with five reflections (lantern-1): no edit, delete or undo control on any of them. Grep reflection components for `edit`, `delete`, `remove`, `undo`, `contenteditable` on saved text.

### R-017
- **Statement:** Nobody can change or delete a journey overview once it is written.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** CL:71, FS:120, P1:23 (D10), P1:44. **= §2.5 check 1**
- **How to check:** As R-015 and R-016, on the overview store and overview screens.

### R-018
- **Statement:** A photo can never be deleted or replaced, by anyone.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:266 (§20 mechanics 6), P1:20 (D7), P1:45, CL:90. **= §2.5 check 1**
- **How to check:** UPDATE, DELETE and TRUNCATE on photo rows and their images raise. No API route deletes a photo or swaps its image.

### R-019
- **Statement:** No screen offers to delete, remove or replace a photo.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** FS:266, CL:90
- **How to check:** UI test on owner views of revealed journeys: no delete, remove, trash or replace control. Grep for `delete`, `remove`, `trash`, `bin`, `replace` near photo components.

### R-020
- **Statement:** A handwritten note cannot be changed or deleted once added.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:16 ("written once"), P1:45, P1:108. **= §2.5 check 1**
- **How to check:** As R-015, on the note store. No UI control re-takes or removes a note.

### R-021
- **Statement:** Once Commit is pressed, the journey's type, commit date and unlock date can never change.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:44, CL:78, MP:55, P1:76. **= §2.5 check 1**
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

### R-026
- **Statement:** A second Commit while the user has a sealed journey is refused.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:273 (§20 C), P1:16 (D3), CL:78. **= §2.5 check 3**
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
- **Source:** FS:263 (§20 mechanics 3), P1:17 (D4), CL:78, MP:55
- **How to check:** No route or control for any of these. Grep for `abandon`, `cancel journey`, `quit`, `pause`, `end early`, `restart`, `start over` in routes and copy.

### R-029
- **Statement:** A photo can only be taken live in the app, at the moment. No existing image can be imported from a gallery, camera roll, file or drag-and-drop.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:53, MP:67, CL:90
- **How to check:** Grep the client for `<input type="file"`, `showOpenFilePicker`, `ondrop`/`dragover` handlers and gallery pickers on any capture path. Capture must use the live camera stream. Note: a file input with `capture` opens the phone's own camera, which offers its own Retake and may offer the gallery, so it fails R-029 and R-031.

### R-030
- **Statement:** Capture is three taps and asks for nothing: no tags, no text, no caption, no visibility, no filter, crop or other choice.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:54, MP:67, CL:90
- **How to check:** The capture API accepts the image and nothing else (send extra fields: rejected or ignored, never stored). UI test: from opening capture to the photo being sealed takes at most three taps, with no input field or option on the way.

### R-031
- **Statement:** There are no retakes. Once the shutter is pressed the photo is final: no retake, no "use photo or retake" step, no undo, no discard.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** CL:55, MP:37, FS:55, FS:228
- **How to check:** UI test: after the shutter tap, no control returns to the viewfinder for the same frame. Grep for `retake`, `re-take`, `try again`, `redo`, `discard`, `undo`, `use photo`. No API route replaces a photo (R-018).

### R-032
- **Statement:** Capture never refuses or warns because of image quality: blur, darkness, composition or framing.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** FS:56
- **How to check:** List every refusal reason in the capture path. The only reasons allowed are no sealed journey, the frame limit, and the highlight cap. Grep for `blur`, `too dark`, `low light`, `quality`, `out of focus`.

### R-033
- **Statement:** Capture takes still photos only: no video and no moving image.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:57, MP:67, CL:90
- **How to check:** Capture rejects any non-still-image media type. Grep the client for `MediaRecorder`, `video/` uploads and `capture="camcorder"`.

### R-034
- **Statement:** A photo is sealed into the journey the moment it is taken. There is no later step that decides whether it is included.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:58, CL:90
- **How to check:** Capture either seals the photo into the journey in one call or refuses. No "add to journey", draft or pending state exists in the data or the UI.

### R-035
- **Statement:** Capture works only while the user has a sealed journey. Before Commit and after unlock it is refused.
- **Type:** auto · **Applies to:** API
- **Source:** P1:99, FS:73
- **How to check:** As First Light (no journey): refused. As Long Way Round (#4 unlocked): refused. As Lantern at 2027-01-01 00:00:00: refused.

### R-036
- **Statement:** A normal photo is accepted only while the journey's normal photos so far are below the type's monthly cadence times the current month of the journey, so unused frames carry forward.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261–262 (§20 mechanics 1–2), P1:18 (D5), P1:97, CL:86
- **How to check:** For each type, fill month 1 to cadence and try one more: refused. Skip month 1 and in month 2 take two months' worth: all accepted (Wanderer: 4). Replay Lantern #3's 0 in March and 4 in April.

### R-037
- **Statement:** Frames unused when a journey ends are gone. Nothing carries into the next journey.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261, P1:18 (D5), CL:86
- **How to check:** End a journey with frames unused, Commit the next, and in its month 1 take cadence + 1 photos: the last is refused.

### R-038
- **Statement:** Capturing a photo and starting a highlight answer only "accepted" or "refused". They never return a number: not frames used, frames left, highlights left or photos so far.
- **Type:** auto · **Applies to:** API
- **Source:** P1:49, FS:243, CL:60. **= §2.5 check 5**
- **How to check:** Inspect the response schema of both calls. Any numeric field, or any string containing a digit that reports a count, fails.

### R-039
- **Statement:** The number of frames used, frames left and highlights left is never stored. It is worked out at the moment of capture and discarded.
- **Type:** auto · **Applies to:** data
- **Source:** P1:49. See G-6
- **How to check:** Schema scan for columns or cache keys named like `frames_used`, `frames_left`, `remaining`, `highlights_used`, `highlights_left`, `photo_count`, `quota_left`.

### R-040
- **Statement:** A highlight starts only when the user starts it, and lasts 24 hours or until the journey unlocks, whichever is first.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:264 (§20 mechanics 4), P1:19 (D6), P1:133, CL:88
- **How to check:** No job or rule starts a highlight. Start one and capture at +23:59 (accepted as highlight) and +24:01 (treated as normal frame or refused). Start one 2 hours before unlock: it ends at unlock.

### R-041
- **Statement:** Only one highlight can be open at a time. Starting another while one is open is refused.
- **Type:** auto · **Applies to:** API
- **Source:** FS:284 (§20 N), P1:345 (R3), CL:88, MP:65
- **How to check:** Start a highlight, then start a second inside the 24 hours: refused.

### R-042
- **Statement:** A journey has at most its type's highlights (Explorer 4, Wanderer 2, Contemplator 1), and they can be used at any time in the journey, with no season rule.
- **Type:** auto · **Applies to:** API
- **Source:** FS:66, FS:264, P1:135, CL:80–84
- **How to check:** For each type, start highlights back to back up to the allowance (all in one month for Explorer): accepted. One more: refused.

### R-043
- **Statement:** A highlight holds up to the type's yearly quota (48, 24, 12), and its photos never count against the journey's normal frames.
- **Type:** auto · **Applies to:** API
- **Source:** FS:265 (§20 mechanics 5), P1:19 (D6), P1:96, CL:88
- **How to check:** Fill a Contemplator highlight to 12 (Lantern #5 shape), try a 13th: refused as a highlight photo. After the highlight, normal frames are still available at the same count as before it.

### R-044
- **Statement:** A highlight can only be started on a sealed journey.
- **Type:** auto · **Applies to:** API
- **Source:** P1:135
- **How to check:** Start a highlight with no journey, and after unlock: both refused.

### R-045
- **Statement:** The handwritten note is an optional step offered only after the photo is already sealed. Skipping it costs nothing, and capture never waits on it.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:257 (§20 B), MP:69, CL:90
- **How to check:** The photo exists, sealed, before the note step appears. Skip the note: the photo is unchanged. The note step has a skip control on first render.

### R-046
- **Statement:** A note can be added up to 15 minutes after its photo was captured, never after.
- **Type:** auto · **Applies to:** API
- **Source:** FS:281 (§20 K), P1:21 (D8), P1:108, CL:90, MP:69
- **How to check:** On the app clock, add a note at capture + 14:59: accepted. At capture + 15:01: refused. See G-18 for exactly 15:00.

### R-047
- **Statement:** A photo has at most one note.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:16 ("belongs to exactly one photo, written once"), P1:104
- **How to check:** Add a second note to the same photo within the window: refused.

### R-048
- **Statement:** A note is a photograph of a handwritten page. There is no typed note.
- **Type:** auto · **Applies to:** API, UI
- **Source:** FS:16, MP:69, CL:90
- **How to check:** The note API accepts an image only. The note step shows no text field or keyboard input.

### R-138
- **Statement:** Whether a frame or a highlight is available is learned only by trying. No control is hidden, greyed out or relabelled because of availability, and no call other than capture and starting a highlight works it out or reports it.
- **Type:** auto · **Applies to:** API, UI
- **Status:** Provisional. Depends on G-5 and Question 5 (what a refused capture may say). If the user decides the camera is not offered when no frame is available, this check is superseded
- **Source:** P1:49 ("counted inside them and never stored or returned"), FS:243, RG:28 ("disabled-but-visible states"). Found by `docs/reviews/2026-10-27-rules-screen-inventory.md` finding 5
- **How to check:** List every route and function that reads a journey's photo or highlight rows: only capture and start-highlight may compute frames or highlights available. UI test as Steady Lantern on Lantern #6, once with a normal frame available and once with none, and once with highlights unused and once with all used: the sealed-year, capture and start-highlight screens render the same DOM before any tap.

---

## 4. Reveal and locking

### R-049
- **Statement:** The whole journey unlocks at once, at its unlock moment. No photo opens on its own anniversary or before the rest.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:73, FS:255 (§20 A), CL:94, MP:73
- **How to check:** At unlocks_at − 1 second every Lantern #6 photo is sealed (R-001). At unlocks_at every photo is readable to the owner. No photo's readability depends on its own capture date.

### R-050
- **Statement:** Nothing that belongs to the reveal can happen before unlock: no reflection, people tag, chapter, feeling tag, visibility choice, overview or reveal finish.
- **Type:** auto · **Applies to:** API
- **Source:** FS:82–89, FS:133 ("never at capture"), P1:164
- **How to check:** As Lantern at baseline, attempt each on Lantern #6: all refused.

### R-051
- **Statement:** Each reveal choice is set once, even before the reveal is finished. A photo's visibility, each people tag, the chapter and each feeling tag cannot be changed or removed after it is set.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:286 (§20 P), P1:347 (R5), CL:94, MP:73
- **How to check:** On Lantern #6 after unlock, set a photo's visibility, then try to change it: refused. Add a people tag, try to remove it: refused. Set the chapter, try another: refused. No UI control offers change or removal.
- **Current implementation:** these records are insert-only (P1:46).

### R-052
- **Statement:** Once the reveal is finished, no visibility, people tag, chapter or feeling tag can be added.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:151, FS:276 (§20 F), P1:25 (D12), P1:46, CL:94. **= §2.5 check 2**
- **How to check:** On a revealed fixture journey (Lantern #5), insert each kind: each raises.
- **Current implementation:** trigger refuses inserts once the journey's reveal-finished record exists (P1:46).

### R-053
- **Statement:** A photo with no visibility choice is Network: once unlocked, the owner's network can read it.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:151, FS:276 (§20 F), P1:25 (D12), P1:166, CL:94
- **How to check:** As Open Hands (on Round's map) at baseline, read a Long Way Round #4 photo: allowed. As First Light: refused.

### R-054
- **Statement:** If the reveal is never finished, the journey still unlocks on its date, no "journey launched" goes out, and the owner's map is not recomputed.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:269 (§20 mechanics 9), P1:25 (D12), MJC:855. See G-11 for what happens to choices set during an unfinished reveal
- **How to check:** Long Way Round #4 at baseline and at +5 years: photos readable by Round, no `journey_launched` announcement for #4, Round's layer entries unchanged since #3.

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
- **Source:** FS:285 (§20 O), P1:346 (R4), CL:96
- **How to check:** Finish a reveal with no overview: accepted. The finish control is not blocked by a missing overview, reflection or tag.

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

### R-062
- **Statement:** A reflection is readable by exactly the people who can read its photo.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:276 (§20 F), P1:24 (D11), P1:117, MP:79
- **How to check:** For each visibility level, the set of users who can read the photo equals the set who can read its reflections.

### R-063
- **Statement:** A journey overview can be read by its owner and the owner's network.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:275 (§20 E), P1:23 (D10), P1:126, CL:96. See G-19 for everyone else
- **How to check:** As Second Wind, read a Lantern overview: allowed, even where every photo of that journey is private.

### R-064
- **Statement:** Close friends see nothing beyond the rest of the network. There is no close-friends access level, list or grant.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** FS:150, FS:278 (§20 H), P1:29 (D16), CL:98, MP:81, MJC:864. See G-3
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

### R-068
- **Statement:** The baseline access matrix holds.
- **Type:** auto · **Applies to:** data, API
- **Source:** P1:305–313
- **How to check:** Run every cell of the §3.6 matrix as a test at baseline.

---

## 6. Layers

### R-069
- **Statement:** No endpoint or response tells a user which ring they sit on in someone else's map. Layer data can be read only by the map's owner.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:65, CL:73, MP:47, FS:164, FS:235, P1:51. **= §2.5 check 7** (first half)
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
- **Source:** CL:65, FS:164, MJC:422
- **How to check:** Review every screen as a member, not the owner. Grep aid: `inner circle`, `closest`, `close friend`, `your ring`, `moved (in|out|closer|further)`. See G-12.

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
- **Source:** FS:161, FS:277, P1:28 (D15), CL:98
- **How to check:** Boundary cases 1, 2, 4, 5. Fixture: Lantern's map of Wind across #1–#5 (P1:259–265).

### R-078
- **Statement:** Someone on the map who is not tagged in a finished journey moves out one ring. Outer stays outer. Nobody is ever removed from a map.
- **Type:** auto · **Applies to:** data
- **Source:** FS:165, FS:277, P1:28 (D15), P1:157, CL:98
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
- **Source:** FS:158–159, CL:98, MP:81
- **How to check:** Review the layers screen.

### R-083
- **Statement:** Drift outward is presented as expected, never as loss, failure or demotion.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:165, MJC:422
- **How to check:** Review the owner's own map and any copy about ring changes. Grep aid: `lost`, `dropped`, `demoted`, `unfriend`, `fading`.

### R-139
- **Statement:** No screen lets any user see or work out a ring on a map that is not their own. There is no count of how often a person is tagged in someone's journey, no grouping of a journey's photos by the person tagged, and no "people in this journey" list ordered by how often they appear. This covers third parties as well as the person tagged.
- **Type:** review · **Applies to:** UI, copy
- **Status:** Provisional only for the tagged reader's own appearances, which `FS:196` asks for (G-12). For everyone else it holds as written
- **Source:** FS:164 ("Each user sees only their own map"), FS:161 (the ring is the count of tagged photos in one journey), CL:65, MP:47, P1:51. R-071 covers only the person on the ring; this check covers anyone reading someone else's journey. Found by `docs/reviews/2026-10-27-rules-screen-inventory.md` finding 10
- **How to check:** As Open Hands (on Steady Lantern's map), read Lantern #1, where Lantern tags Second Wind in 6 photos. Nothing on Walking a path, Another user's profile or A photo followed forward totals, groups or orders by how often Wind appears. Grep aid: `appears in`, `\d+ photos? (with|of)`, `most tagged`, `people in this`, and any reader-side query that groups or counts person tags by person.

---

## 7. Feed and notifications

### R-084
- **Statement:** The feed carries only three kinds of announcement: journey launched, reflection left, path crossed.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:171–175, CL:100, MP:83, P1:31 (D18), P1:168. **= §2.5 check 9** (types)
- **How to check:** Schema: the announcement type allows exactly these three values. Inserting any other raises.

### R-085
- **Statement:** An announcement holds no image, media or count.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:63, MP:45, FS:171, P1:168. **= §2.5 check 9** (no media)
- **How to check:** Schema scan of the announcement store: no media, image, url, thumbnail or count field. API responses for the feed contain no image URL.

### R-086
- **Statement:** The feed screen shows no photograph: no thumbnail, preview or cover image in any announcement.
- **Type:** auto · **Applies to:** UI
- **Source:** CL:63, MP:45, FS:171. See G-9 for avatars
- **How to check:** UI test at several simulated dates: the feed DOM has no `img`, `picture`, `canvas` or background image sourced from a photo or note.

### R-087
- **Statement:** "Journey launched" goes out exactly when a reveal is finished, never at Commit or unlock.
- **Type:** auto · **Applies to:** data
- **Source:** FS:280 (§20 J), P1:31 (D18), P1:158, CL:100
- **How to check:** Jump through Lantern #6's unlock with no reveal finish: no announcement. Second Wind finishes #6 on 2027-04-25: one announcement at that time.

### R-088
- **Statement:** "Reflection left" is shown only to users who can read that photo.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:280 (§20 J), P1:31 (D18), CL:100
- **How to check:** Wind reflects on a private photo: no other user's feed shows it. On a network photo: only the network sees it.

### R-089
- **Statement:** "Journey launched" and "path crossed" are shown to the owner's network.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:282 (§20 M), P1:344 (R2)
- **How to check:** For a fixture reveal finish, the set of feeds containing each announcement equals the owner's map members.

### R-090
- **Statement:** "Path crossed" goes out for every crossing: one per tagged user in each finished reveal.
- **Type:** auto · **Applies to:** data
- **Source:** FS:280 (§20 J), P1:31 (D18), P1:156, CL:100
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

### R-093
- **Statement:** Getting from the feed to someone's journey takes a small deliberate act. Journey content is never shown inside the feed.
- **Type:** review · **Applies to:** UI
- **Source:** FS:177, MJC:423
- **How to check:** Review: opening a journey needs an explicit tap. The feed does not expand, autoplay or preview journey content.

### R-094
- **Statement:** No notification outside the app invites a return visit: no push, email, SMS or OS notification to capture, reflect, finish a reveal, write an overview, come back, or see what someone else did.
- **Type:** auto · **Applies to:** API, UI, dependencies, copy
- **Source:** CL:61, MP:43, FS:236, FS:242, FS:102. See G-16 for "Your Journey is ready"
- **How to check:** Dependency scan for push and mail libraries (`web-push`, `firebase/messaging`, `onesignal`, `pusher-beams`, `nodemailer`, `@sendgrid`, `postmark`, `resend`, `twilio`). Grep for `Notification.requestPermission`, `PushManager`, service-worker `push` handlers, and scheduled jobs that send messages.

### R-095
- **Statement:** Nothing in the app reminds or nudges the user to capture, reflect, finish a reveal, write an overview, use a highlight or come back: no banner, toast, modal, empty-state call to action, "you haven't", "frames waiting" or "highlight ending soon".
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:60, FS:102, FS:209, FS:233, FS:242, MP:42
- **How to check:** Review every screen at several simulated dates, including the sealed-year empty state and a reveal left unfinished. Grep aid: `don't forget`, `remember to`, `you haven't`, `come back`, `we miss`, `still have`, `waiting for you`, `ending soon`, `last chance`.

### R-096
- **Statement:** There is no unread dot, badge count, "new" marker or app-icon badge anywhere.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:60, CL:61, FS:233, RG:28 ("badges, dots, 'new' markers")
- **How to check:** Grep for `navigator.setAppBadge`, `unread`, `badge`, `isNew`, `\bnew\b` labels, `seen_at`/`read_at` fields. Schema scan for read-state on announcements. Review navigation and feed.

---

## 8. Engagement mechanics

### R-097
- **Statement:** There are no streaks: no count of consecutive days, weeks or months, no "don't break the chain", no flame.
- **Type:** auto · **Applies to:** data, UI, copy
- **Source:** CL:60, MP:42, FS:233, P1:180. Part of **§2.5 check 6** (streak)
- **How to check:** Schema scan and copy grep for `streak`, `chain`, `consecutive`, `in a row`, `🔥`.

### R-098
- **Statement:** No count of the quota is shown in a way that reads as a target: no frames left, photos this month, "n of 48", or highlights remaining.
- **Type:** auto · **Applies to:** API, UI, copy
- **Source:** FS:243, CL:60, P1:49. See G-5
- **How to check:** R-038 and R-039 hold, and copy grep for `left this month`, `remaining`, `of (12|24|48)`, `\d+ (more|to go)`.

### R-099
- **Statement:** There is no progress bar, completion meter or percentage anywhere: not for the year, the quota, the reveal ("12 of 24 reflected"), the profile or the overview stack.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:60, MP:42, FS:233
- **Status:** Provisional. `FS:233` limits this to the sealed year. See G-4
- **How to check:** Grep for `<progress`, `role="progressbar"`, `aria-valuenow`, `%`, `complete`, `\d+ of \d+`. Review the reveal flow.

### R-100
- **Statement:** There are no likes, reactions or view counts on anything.
- **Type:** auto · **Applies to:** data, API, UI
- **Source:** P1:53, P1:180, CL:60. Part of **§2.5 check 6** (like, reaction, view)
- **How to check:** Schema scan for `like`, `reaction`, `heart`, `view`, `view_count`, `impression`. UI review for heart or reaction controls.

### R-101
- **Statement:** No user has a score, rank, level, tier, badge or position on a leaderboard, and no data compares users.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:62, MP:44, FS:185, FS:244, P1:53, P1:180. Part of **§2.5 check 6** (score, rank, badge)
- **How to check:** Schema scan for `score`, `rank`, `level`, `tier`, `badge`, `achievement`, `points`, `leaderboard`, `xp`.

### R-102
- **Statement:** The circle and its rings are a record, not a rank. No screen or copy compares users, ranks them, names a level or tier, or treats more rings as better.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:62, CL:102, FS:185, FS:244, MJC:689–694
- **How to check:** Review profiles and the circle. Grep aid: `level`, `rank`, `top`, `ahead`, `behind`, `veteran`, `elite`, `unlock achievement`.

### R-103
- **Statement:** The Positivity Feed draws only on Public photos and is filtered by endurance and gratitude tags, never ordered or filtered by popularity.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:202–203, P1:317. See G-8 and G-14
- **How to check:** As First Light, the feed holds only public photos with the listed tags. Its query uses no read, like, view or count measure for order or selection.

### R-104
- **Statement:** No surface is designed to make a visit longer: low usage is the goal.
- **Type:** review · **Applies to:** UI, copy
- **Source:** CL:67, MP:49
- **How to check:** For each screen, ask whether it would increase time in app (autoplay, endless content, "more like this", pull-to-refresh into new content). If yes, raise it.

### R-140
- **Statement:** No timer, countdown or time-left display runs on the 15-minute note window or on an open highlight: no "14:32 left to add a note", no "ends in 3h", no shrinking bar or ring.
- **Type:** auto · **Applies to:** UI, copy
- **Source:** CL:60 (counters), FS:233 ("No visible counters ... during the sealed year"; both windows exist only while a journey is sealed, so the time limit in G-4 does not apply), RG:28 ("timers"), FS:281, FS:264. R-013 covers only the countdown to unlock. See G-13 for whether a plain open-or-closed highlight state may show. Found by `docs/reviews/2026-10-27-rules-screen-inventory.md` finding 3
- **How to check:** Grep copy and code for `minutes? left`, `ends in`, `time left`, `remaining`, `\d+:\d\d` near note or highlight components, and any `setInterval` or `requestAnimationFrame` that formats a time until capture + 15 minutes or a highlight's end. UI test: render the note step at capture + 0:30 and + 14:00, and the sealed-year and capture screens at highlight start + 1 h and + 23 h. Each pair renders the same DOM.

---

## 9. Comments and voice

### R-105
- **Statement:** Nobody can comment on or reply to anything: there is no comment or reply object on a photo, journey, reflection, overview or announcement.
- **Type:** auto · **Applies to:** data, API
- **Source:** CL:57, CL:74, MP:39, FS:100, FS:152, FS:230, P1:53. Part of **§2.5 check 6** (comment, reply)
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
- **Source:** CL:57, FS:152 ("readable, not commentable"), FS:245, MJC:187
- **How to check:** UI test as a non-owner on each of these views: no `textarea`, text `input` or `contenteditable`.

---

## 10. Recognition and dependencies

### R-110
- **Statement:** No face or vision library is in the dependencies.
- **Type:** auto · **Applies to:** dependencies
- **Source:** CL:58, MP:40, FS:127, FS:231. **= §2.5 check 11**
- **How to check:** Scan every manifest and lockfile for `face-api`, `@vladmandic/face-api`, `@vladmandic/human`, `@mediapipe/*`, `@tensorflow/*`, `tfjs`, `opencv`, `dlib`, `face_recognition`, `deepface`, `insightface`, `@aws-sdk/client-rekognition`, `@google-cloud/vision`, `@azure/cognitiveservices-face`, `clarifai`.

### R-111
- **Statement:** Face detection does not happen anywhere in the pipeline, including the browser's own APIs and camera settings.
- **Type:** auto · **Applies to:** UI, API
- **Source:** FS:231 ("anywhere in the pipeline")
- **How to check:** Grep for `FaceDetector`, `detectFaces`, `faceDetectionMode`, `getFaces`, `faceLandmarks`, and calls to any vision service.

### R-112
- **Statement:** People are tagged by hand. Nothing suggests, pre-fills or guesses a person from the image.
- **Type:** review · **Applies to:** UI, API
- **Source:** CL:58, FS:127, MJC:417
- **How to check:** Review the tagging step: it starts empty and offers people only from what the owner types.

### R-113
- **Statement:** There are no ads anywhere, in the app or on the site.
- **Type:** auto · **Applies to:** dependencies, UI
- **Source:** CL:59, MP:41, FS:232
- **How to check:** Scan dependencies and page source for `adsbygoogle`, `googletag`, `doubleclick`, `googlesyndication`, `admob`, `prebid`, `amazon-adsystem`, `carbonads`, `ethicalads`. Review both for sponsored or promoted content.

### R-114
- **Statement:** User memories (photos, notes, reflections, overviews, tags) are never sold, transferred or used for training.
- **Type:** review · **Applies to:** dependencies, API
- **Source:** FS:247
- **How to check:** Review every outbound call and third-party dependency for anything that receives memory content. Scan aid: `openai`, `@anthropic-ai`, `replicate`, `huggingface`, data-broker or analytics SDKs. Each hit needs a reason recorded in the audit.

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
- **Source:** FS:36, FS:273 (§20 C), P1:14 (D1), P1:74, P1:196, CL:78
- **How to check:** For each fixture journey, unlock = commit + 12 months. Jump to unlocks_at with all scheduled jobs disabled: the journey reads as unlocked. See G-18.

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
- **Source:** FS:97, FS:101, FS:274 (§20 D), P1:22 (D9), P1:115, CL:96. See G-1
- **How to check:** For Lantern #1 (unlock 2022-01-01), a reflection on 2023-12-31 is slot 2 and one on 2024-01-01 is slot 3, for every photo regardless of capture date. A second reflection in the same slot is refused. A client-supplied slot is ignored.

### R-122
- **Statement:** Each journey takes at most one overview per slot, on the same slot windows as reflections.
- **Type:** auto · **Applies to:** data, API
- **Source:** FS:117, FS:275 (§20 E), P1:23 (D10), P1:124. See G-15
- **How to check:** Second overview in one slot: refused. Fixture count: Steady Lantern has 15 (P1:301).

### R-123
- **Statement:** The months that set the frame limit are counted from the journey's own commit date, not from calendar months.
- **Type:** auto · **Applies to:** API
- **Source:** FS:261 (§20 mechanics 1), P1:18 (D5), CL:86
- **How to check:** Commit on the 20th. Month 1 runs to the 20th of the next month: a capture on the 1st of the next calendar month is still month 1. See G-18.

---

## 12. Copy and tone

### R-124
- **Statement:** No product copy, in the app, on the site, in metadata or in any message, uses engagement, ranking, leak or retake language.
- **Type:** auto · **Applies to:** copy
- **Source:** CL:55–65, MP:37–47
- **How to check:** Grep all copy for `streak`, `level up`, `badge`, `leaderboard`, `rank`, `score`, `points`, `don't forget`, `come back`, `we miss`, `you haven't`, `moments captured`, `frames left`, `days to go`, `unread`, `new!`, `trending`, `popular`, `likes`, `followers`, `comment`, `retake`, `try again`, `edit reflection`, `delete`. Every hit goes to review, since the site may rightly say "No retakes" or "no streaks" as a refusal.

### R-125
- **Statement:** No copy asks the user to perform: no "make it count", "get the perfect shot", "show off" or "share your best".
- **Type:** review · **Applies to:** copy
- **Source:** CL:118, MP:112
- **How to check:** Read every screen's copy and the site.

### R-126
- **Statement:** Nothing on a profile signals how the person looks or how well they are doing.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:29, MP:113, MJC:696. See G-10
- **How to check:** Review profile screens for status, success markers, counts and physical descriptors.

### R-127
- **Statement:** The name step asks for a name from within, not a handle and not a physical or earthly attribute, and says the name is kept.
- **Type:** review · **Applies to:** UI, copy
- **Source:** FS:29, FS:268, P1:32 (D19)
- **How to check:** Read the name step's copy.

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
- **Source:** CL:67, MP:49, MP:138, BP:126
- **How to check:** Check the site's first screen and the app's first-run copy.

### R-131
- **Statement:** These lines appear, stated plainly: "It's not about attention. It's about intention." · "You've come further than you think." · "Strict at capture. Generous at reflect." · "No retakes. That moment is gone." · "This app takes time, like many other good things." · "We want you here less, not more."
- **Type:** auto · **Applies to:** copy
- **Source:** MP:115–122, CL:120–127
- **How to check:** Exact-string search of the site build for each line.

### R-132
- **Statement:** On the site, strict at capture, no retakes, low usage is the goal, and this app takes time appear above the fold or close to it.
- **Type:** auto · **Applies to:** copy, UI
- **Source:** BP:130
- **How to check:** Render the home page at a fixed phone and desktop viewport and check the four statements are in or just below the first viewport.

### R-133
- **Statement:** The button that starts a journey says "Commit".
- **Type:** auto · **Applies to:** UI, copy
- **Source:** FS:45, CL:78, MP:55
- **How to check:** UI test: the button's label is exactly "Commit".

---

## 13. Across every area

### R-134
- **Statement:** Every behaviour in a deliverable traces to a source line. Anything not specified was raised as a question, not filled in.
- **Type:** review · **Applies to:** data, API, UI, copy
- **Source:** CL:15, MP:9, MP:151
- **How to check:** For each behaviour in the target, find its source. Anything without one is a finding.

### R-135
- **Statement:** Where two docs disagree, the deliverable cites both and raises the question. It does not pick one.
- **Type:** review · **Applies to:** data, API, UI, copy
- **Source:** CL:21
- **How to check:** Compare the target against the Gaps below. A deliverable that silently follows one side fails.

### R-136
- **Statement:** No deliverable is built or audited from `docs/Overview.md`.
- **Type:** auto · **Applies to:** copy
- **Source:** CL:32
- **How to check:** Grep deliverables and briefs for `Overview.md` cited as a source.

### R-137
- **Statement:** Every auto check in this rubric runs in the build and fails it when broken.
- **Type:** auto · **Applies to:** data, API, UI, dependencies
- **Source:** P1:173 ("Each one fails the build"), BP:203, CL:69
- **How to check:** Map each auto R-ID to a test in the suite. An auto check without a test is a finding.

---

## Banned-list coverage

Every row of the banned list (`CLAUDE.md:55–65`, `Master-Prompt.md:37–47`) and the checks that cover it.

| Banned item | Checks |
|---|---|
| No retakes | R-031, R-005, R-018, R-019, R-029, R-124 |
| No edits to reflections | R-015, R-016, R-124 |
| No comments from anyone else | R-105, R-106, R-107, R-109, R-124 |
| No face recognition | R-110, R-111, R-112 |
| No ads anywhere | R-113 |
| No streaks, counters, progress bars, reminders | R-097, R-098, R-099, R-038, R-039, R-012, R-013, R-095, R-096, R-124 |
| No re-engagement notifications | R-094, R-095, R-096 |
| No ranking, levels, badges, leaderboards | R-101, R-102, R-103, R-124 |
| No photo feed | R-084, R-085, R-086 |
| Nothing leaks from a sealed year | R-001 to R-014, R-091 |
| No layer is ever shown to the person on it | R-069, R-070, R-071, R-092 |

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

### Contradictions between sources

**G-1. Reflection slot dates.** The example at `FS:104–111` dates reflections from the photo's own capture date (7 Jan each year). `FS:101` and `FS:274` (§20 D) say all photos of a journey move slot together on the journey's unlock anniversary, and `MJC:852` agrees. The same per-photo example is in `MJC:200` and `MJC:203–210`. R-121 tests the §20 D wording; the example needs correcting or confirming.

**G-2. "Publish".** `FS:141` says visibility is "chosen at publish time", and `MJC:365–367`, `MJC:424` and `MJC:440` speak of publishing a journey. No step called publish exists. The decided terms are "reveal finished" (`FS:151`, `FS:276`) and "journey launched" (`FS:280`). Also `MJC:401` says layers are calculated when journeys are "uploaded", against `FS:162` (when a reveal is finished). Learnings open questions 1 and 2.

**G-3. Close friends.** `MJC:807` says close friends "get everything", and `MJC:383` says "everything for the people closest to you". `FS:278` (§20 H), `FS:150` and `MJC:864` say they see nothing beyond the rest of the network. R-064 tests §20 H.

**G-4. When reminders, counters and progress bars are banned.** `FS:233` says "No visible counters, no progress bars, no reminders **during the sealed year**". `CLAUDE.md:60` and `Master-Prompt.md:42` ban them with no time limit, and `FS:242` bans reminders to capture, reflect or return at any time. Open: is a counter or progress bar allowed after unlock, for example "12 of 24 reflected" during the reveal? R-099 is provisional on this.

**G-5. Showing the quota.** `FS:243` bans showing the quota left "in a way that reads as a target", which implies some way of showing it may be allowed. `P1:49` says frames used and left are never stored or returned, and `CLAUDE.md:60` bans counters. Open: may the owner ever see how many frames they have left?

**G-6. Stored journey fields.** `FS:15` lists "frames used", "highlights used" and a state "committed / sealed / unlocked" as journey properties. `P1:49` says frame and highlight counts are never stored, and `P1:76–84` says state is derived, with "committed" folded into sealed. R-039 tests P1.

**G-7. What adds a ring to the circle.** `FS:185` says one ring "per year with the app", and `MJC:687` says "each year with the app adds a ring". `P1:65` says one ring "per journey whose reveal is finished". These differ for a user with a year and no journey, or a reveal never finished (Long Way Round #4).

**G-8. The Positivity Feed and "no photo feed".** `CLAUDE.md:63` and `Master-Prompt.md:45` say "No photo feed. The feed carries announcements only, never images". The Positivity Feed is fed by public photos and their reflections (`FS:203–204`, `P1:317`). Open: does the Positivity Feed show photographs, and if so how does that fit the ban? Also `FS:203` says it draws from "journeys set to public", while visibility is per photo (`FS:141`); `MJC:375` and `MJC:379` show the same split. And `MJC:244` says "no feed", against `FS:169–177`.

**G-9. Images in the announcement feed.** `CLAUDE.md:63` says "never images". `FS:171` says "No photographs in the stream". Open: may an announcement show the actor's profile picture?

**G-10. Profile picture and looks.** `FS:13` and `P1:62` give each user a profile picture. `FS:29` and `Master-Prompt.md:113` say nothing on a profile signals how the person looks. Open: what may the profile picture be?

**G-11. Choices made during a reveal that is never finished.** `FS:269` says an unfinished reveal has "no chapter, no tags", and `P1:25` and `MJC:855` say "the photos stay Network". But choices are inserted, once each, during the reveal (`FS:286` §20 P, `P1:46`, `P1:143`, `P1:165–166`, `P1:347`). Open: if the owner sets a photo to Private, or sets a chapter, and never finishes, does that choice take effect? R-054 tests only what all sources agree on.

**G-12. Walking a path can show a ring.** `FS:196` says the reader sees where they themselves appear in someone's journey. Counting those photos lets a reader estimate their ring on that person's map (5+ tight), against `FS:164`, `CLAUDE.md:65` and `P1:51`. Private tags count but stay hidden (`FS:277`), so the estimate is a floor, not exact. Open: is that acceptable, or should the "where you appear" view not total up?

**G-13. Highlights during the sealed year.** `P1:48` seals photo, note, tag and reflection rows, but not highlight rows. A readable highlight record would tell others that, and when, a user started one, against `FS:246` and `FS:279` (§20 I). R-008 already requires that others see nothing, so the gap is in the current implementation. Open for the owner: may the owner see that a highlight is open and when it ends? A running "ends in 3h" would be a counter (`CLAUDE.md:60`); a plain open-or-closed is not addressed anywhere.

**G-14. Feeling tags.** `FS:131` says feeling tags are written "inside a category", and `P1:141` stores them as (journey, free text) with no category. `FS:131` also says popular feeling tags "surface over time", while `FS:202` says the Positivity Feed is "never by popularity". Open: how a tag surfaces, and whether that uses any measure of popularity.

**G-15. When an overview is written.** `FS:118` (and `MJC:218`) says the overview is "written at reveal". `FS:275` (§20 E) says a new one every year on each journey. R-122 tests §20 E.

**G-16. "Your Journey is ready."** `BP:79`, `Master-Prompt.md:138` and `MJC:740` name this as a key microcopy moment. `FS:236` bans "re-engagement notifications of any kind", and `MJC:156` contrasts the reveal with "an unlock notification with nothing to do". Open: is "Your Journey is ready" a notification sent at unlock, or only text shown when the user next opens the app? R-094 bans the notification until the user decides.

**G-17. What the owner sees of a sealed journey.** `FS:74` says nothing in a sealed journey is visible "not to the user". `P1:84` lets the owner see its type, commit date and unlock date. These may agree (dates are about the journey, not in it), but it is worth confirming, together with whether showing the unlock date is allowed at all given the countdown ban (R-013).

### Rules that cannot be made testable yet

**G-18. Calendar arithmetic.** "12 months" (`FS:36`, `P1:14`), "month of the journey" (`FS:261`, `P1:18`) and "any day" (`P1:15`) are not defined for a commit on the 29th, 30th or 31st, for 29 February, or across time zones (whose midnight starts a day). "Up to 15 minutes ... never after" (`FS:281`) does not say whether exactly 15:00 is in or out. "24 hours" (`P1:19`) does not say what happens across a daylight-saving change. R-025, R-036, R-046, R-118 and R-123 test only away from these edges.

**G-19. Who else reads an overview.** `FS:275` and `P1:126` say the owner's network can read it. Nothing says whether anyone outside the network can, for example on a journey with public photos in the Positivity Feed.

**G-20. "Anyone" for Public.** `FS:147` says a public photo is readable by "anyone". Open: does that include signed-out visitors, or only users?

**G-21. Review-only rules.** These are checks, but only a reader can decide them: tone (`FS:135`), the deliberate act to open a journey (`FS:177`), invited never nudged (`FS:209`), names from within (`FS:29`), and the time-in-app test (`CLAUDE.md:67`). `FS:247` "train on" cannot be proven by a code scan; R-114 is review for that reason.

**G-22. Stale lines in the Concept doc**, not marked as superseded: `MJC:799` says "Frame range 24–48", against the 12–48 range in `FS:38–42`. `MJC:714` points the streak ban at "section 4", which does not hold it (Learnings open question 3).

### Questions for the user (no source covers them)

These are not checks, since no source states a rule. A normal product would fill each by reflex.

1. **Feed order.** The announcement feed's order is not stated anywhere. Is it newest first?
2. **Analytics and telemetry.** May the app or site collect usage analytics at all? `FS:247` covers memories, not usage, and low usage is the goal (`CLAUDE.md:67`).
3. **The note photo's source.** Must the note page be photographed live in the app, like the photo (`FS:53`), or can it come from the gallery?
4. **Push permission.** If no notification is ever sent (R-094), should the app ever ask for notification permission? Asking is itself a prompt.
5. **Capture refusals.** When capture is refused for the frame limit, what may the message say without becoming a counter (R-038, G-5)?
