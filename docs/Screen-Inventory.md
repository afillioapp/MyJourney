# My Journey — Screen Inventory

Phase 1 deliverable (`Build-Plan.md:65`): every screen the app needs, named, nothing designed yet. Phase 2 writes the flows from this list and Phase 4 builds the screens from it.

Written: 2026-10-27, by the UX agent. Revised 2026-10-27 (round 1 of 3) after the rules audit `docs/reviews/2026-10-27-rules-screen-inventory.md` (FAIL: 1 violation, 11 risks, 4 weak points) and the user's approval of provisional defaults. What changed is listed under **Revision log** at the end. Simulated baseline used throughout: **2026-10-25** (`Phase-1-Proposal.md:201`).

What this file does: names each screen, traces it to the spec by file and line, says who can see it, and says what it holds and must never show at each point in simulated time. What it does not do: layout, colour, type, final copy or flows. Where the spec is silent or contradicts itself, the gap is listed under **Open questions**.

Sources, in the order of trust set by `CLAUDE.md`: `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29, then the rest of `Functional-Spec.md`, then `Phase-1-Proposal.md`, then `Master-Prompt.md`, `Build-Plan.md` and the rest of the Concept doc. `Overview.md` is not cited anywhere. File names below are shortened: **Spec** = `Functional-Spec.md`, **Proposal** = `Phase-1-Proposal.md`, **Plan** = `Build-Plan.md`, **Brief** = `Master-Prompt.md`, **Concept** = `My-Journey-Concept.md`, **Decisions** = `Decisions-Needed.md`, **Rubric** = `Rules-Rubric.md`. All are in `docs/`. Rubric checks (R-nnn) and gaps (G-n) are cited as rules a screen must not break; behaviour still traces to the spec.

**Provisional defaults.** Where a screen depends on a question that Decisions answers with a provisional default ("Provisional defaults in force", B1–B26 and C1–C16), the screen is described under that default and labelled `PROVISIONAL: <ID>`. A provisional default is **not a decision**. It becomes one only when the user says so and it moves into Spec §20 (`CLAUDE.md`, rule zero). For the six switchable defaults (B2, B4, B5, B11, B12, C6), both options are described and the default is marked. The user compares them in the prototype options panel, T-02. A question with no default stays open.

---

## Time states

Defined once and used in every states table. All but `no-journey` describe **one journey**. A screen that shows several journeys (a profile, a path) shows each in its own state: at baseline Steady Lantern has #1–#5 in `later-years` and #6 `sealed` (Proposal:223–228).

Calendar edges for every state: a commit on the 29th–31st uses the last day of shorter months; the prototype uses one time zone, UTC; exactly 15:00 minutes after capture is outside the note window; a highlight lasts 24 hours of elapsed time (`PROVISIONAL: B16`).

| State | Definition | Source |
|---|---|---|
| `no-journey` | User-level. The user has no sealed journey. Two cases: **never committed** (First Light) and **between journeys** (the last journey has unlocked and no new Commit yet, as Long Way Round). Commit is open. It can sit alongside the last journey's `unlock-day`, `reveal-open`, `reveal-finished` or `later-years` | Spec:30, Spec:273 (§20 C), Proposal:16 (D3), Proposal:210–211 |
| `sealed` | `committed_at ≤ now < unlocks_at`. Nothing in the journey is readable, the owner included | Spec:73–76, Spec:234, Proposal:48, Proposal:80 |
| `sealed · highlight open` | Sub-state of `sealed`: a highlight the user started is within its 24 hours, cut off at `unlocks_at`. Only the owner's own screens differ in it, and only by the plain fact that a highlight is open (`PROVISIONAL: B6`) | Spec:264, Spec:284 (§20 N), Proposal:133, Decisions B6 |
| `sealed · note window` | Sub-state of `sealed`, **inside the capture flow only**: straight after a photo is taken, while that photo has no note, the user has not left capture, and less than 15 minutes have passed. Leaving capture ends it (`PROVISIONAL: C4`). It changes only Capture S-02 and the note step S-12. No other screen differs in it, because "A capture changes nothing that any reader can observe, the owner included" (Rubric R-010) | Spec:281 (§20 K), Proposal:108, Decisions C4 |
| `unlock-day` | The moment `now` first reaches `unlocks_at`: the whole journey unlocks as one event, and no reveal choice has been made yet. The data model does not separate it from `reveal-open` (Proposal:81). It is listed on its own because the weighted line "Your Journey is ready" belongs to it (Plan:79, Concept:740), shown on the owner's next open and never as a notification (`PROVISIONAL: C1`). See OQ-15 | Spec:73, Spec:255 (§20 A), Spec:273, Proposal:195 ("jump to the next unlock"), Decisions C1 |
| `reveal-open` | Unlocked, reveal not finished, inside reflection slot 1 (unlock to unlock + 1 year). No deadline: a reveal can be finished at any later time, and each choice takes effect when made (`PROVISIONAL: B3`) | Proposal:81, Spec:269 (§20 9), Spec:274 (§20 D), Decisions B3 |
| `reveal-finished` | Reveal finished, still inside slot 1. Visibility, people tags, chapter and feeling tags are locked | Proposal:82, Proposal:164, Spec:276 (§20 F) |
| `later-years` | `now ≥ unlock + 1 year`: reflection and overview slot *k* ≥ 2. Two variants: `later-years · finished` and `later-years · never finished` (Long Way Round #4 from 2027-09-06). A never-finished reveal can still be finished (`PROVISIONAL: B3`) | Spec:274 (§20 D), Spec:275 (§20 E), Spec:269, Proposal:392, Decisions B3 |

**Viewers**, used in every screen entry:

| Viewer | Meaning | Source |
|---|---|---|
| owner | The user whose journey, photo or map it is | Spec:100, Spec:145 |
| network | A user on the owner's map, any ring. "Network" and "a user on the owner's map" are the same set | Spec:146, Proposal:405 (R2) |
| public | Any **signed-in** user, including one on no one's map (First Light, until the scripted 2027-06-20 tag). A signed-out visitor is not a public reader (`PROVISIONAL: B14`) | Spec:147, Proposal:320, Decisions B14 |
| tagged | A user tagged in the owner's photos. Being tagged gives no access by itself. What a tagged reader sees of their own appearances is B12 (switchable) | Spec:196, Proposal:293, Decisions B12 |
| demoer | Whoever runs the prototype. Only for T-01 and T-02, through the panel, a separate role from the acting viewer. The acting viewer chosen in T-02 never moves time or flips a switch (decided 2026-10-30, Spec §20 EE) | Spec:346–356 (§21), Spec:309 (§20 EE), Decisions C11, C16, Rubric R-153 |

**Journey facts after unlock.** A journey's type, dates (commit and unlock), chapter and feeling tags are read by the owner and the owner's network only, never by a public reader (decided 2026-10-30, Spec §20 T, Spec:296). A feeling tag is never shown to a public reader, including where the Positivity Feed selects by it (Spec §20 CC, Spec:307). Under B2's "only after reveal finished" option the network still reads all four from unlock; only photos, and what follows them, wait (Spec §20 X, Spec:301). Whether a photo was taken in a highlight is the owner's alone, also after unlock (Spec §20 DD, Spec:308; `PROVISIONAL: B24`, Decisions B6). Whether a journey's reveal is finished reaches the owner and the owner's network after unlock, never a public reader (decided 2026-10-31, Spec §20 SS, Spec:323). No screen shows a public reader the reveal state as a field, label or marker: no "finished", "launched", "in reveal" or "not yet revealed" beside a journey or photo (Spec §20 ZZ, Spec:333). A public reader may still infer it from what appears: Positivity Feed entries, rings and photos (Spec §20 ZZ). Every reader screen below carries these.

**Applies to every screen.** None of these ever appears, in any state, for any viewer (Brief:37–47, Spec:226–247): "No retakes" · "No edits to reflections" · "No comments from anyone else" · "No face recognition" · "No ads, anywhere" · "No streaks, counters, progress bars, reminders" · "No re-engagement notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed" · "Nothing leaks from a sealed year" · "No layer is ever shown to the person on it". The schema scan words are banned as screen elements too: "comment, reply, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:181). Also on every screen:

- No counter, progress bar, completion meter or percentage at any time, not only while sealed (`PROVISIONAL: B8`). Spec:233 limits the ban to "during the sealed year"; Brief:42 bans them outright (Rubric G-4, R-099)
- No unread dot, badge count, "new" marker, "since your last visit" divider, or badge on a screen's way in or on the app icon (Rubric R-096)
- No in-app nudge to capture, reflect, finish a reveal, write an overview, use a highlight or come back: no banner, toast, modal or empty-state call to action (Spec:242; Rubric R-095)
- No surface built to make a visit longer: no endless or infinite scroll, autoplay, "more like this", or pull to refresh into new content. "If a decision would increase time in app, it is probably the wrong decision" (Brief:49; Rubric R-104)
- No countdown or relative date to any unlock (`PROVISIONAL: C2`; Rubric R-013)
- No profile picture: the field stays unused (decided 2026-10-31, Spec §20 YY, Spec:332; Decisions C7)
- No other user's join date. A user's `joined_at` is readable by that user only; everyone reads names (decided 2026-10-31, Spec §20 TT, Spec:324). No screen derives it for anyone else either, such as by rings per year with the app (Spec §20 WW, Spec:330; see S-05, S-16)
- No request for notification permission (`PROVISIONAL: C15`)
- No usage analytics or telemetry (`PROVISIONAL: B15`)
- To anyone but the owner, no photo's capture time of day, only its capture date; no activity graph finer than one day. The owner sees the full time (decided 2026-10-30, Spec §20 GG, Spec:311; Rubric R-154)
- To anyone but the owner, never when a handwritten note was written, not even the date. The owner sees the full time (decided 2026-10-30, Spec §20 LL, Spec:316)
- To anyone but the owner, photos that share a capture date are shown in a fixed order that carries no time information (decided 2026-10-30, Spec §20 JJ, Spec:314; OQ-46)

The tables below repeat the items most at risk on each screen. **An item missing from a screen's table is still banned on that screen.**

---

## Screens: the nine Build-Plan screens, in ritual order (Plan:103–113)

### S-01 Commit

- **Purpose:** the user picks one of three journey types and presses Commit, which cannot be undone.
- **Spec source:** Spec:34–47 (§3); Spec:263, Spec:273 (§20 3, C); Proposal:14–17 (D1–D4); Plan:105
- **Viewer:** owner (the committing user)
- **Reached from:** Profile (own) S-05, where the app opens (`PROVISIONAL: C12`). **Leads to:** The sealed year S-03

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed | The three types with difficulty, cadence, photos per year and highlights (Spec:38–42). Here they describe a choice, before any year is running. The Commit action (Spec:44–45). Available on any day (Spec:36, Proposal:15) | A pre-selected type: "No default type is pre-selected" (Spec:46). A softer verb: "'Commit' carries weight; 'Start' and 'Create' do not" (Concept:115) |
| `no-journey` · between journeys | The same. Open as soon as the last journey has unlocked, even while its reveal is still open (Spec:273: "the next Commit is only possible once the current one has unlocked") | Any prompt to commit again: "Remind a user to capture, reflect, or return" (Spec:242). A banner or marker that Commit is open again (Rubric R-095, R-096) |
| `sealed` | Not available. One journey at a time (Spec:273; Proposal:178, check 3) | A second Commit. Any way to change type or abandon: "It cannot be changed for that year" (Spec:44), "No abandoning" (Spec:263) |
| `unlock-day`, `reveal-open`, `reveal-finished`, `later-years` | Only through `no-journey` · between journeys (above) | As above |

- **Reads:** User, Journey (Proposal §2.2); `journey_type` constants (Proposal:167)
- **Copy:** the Commit moment and the button itself `[copy: copywriter]` (Plan:79, Spec:45). The three type descriptions `[copy: copywriter]`. The type arithmetic now reads "48, 24, 12" (Spec:47, corrected under Decisions A7; OQ-13)

### S-02 Capture

- **Purpose:** take one photo inside the app, at the moment, in three taps. It is sealed at once.
- **Spec source:** Spec:51–59 (§4); Spec:228 (§18); Spec:261–266 (§20 1, 2, 5, 6); Spec:320 (§20 PP); Spec:321 (§20 QQ); Spec:326 (§20 VV); Spec:331 (§20 XX); Spec:334 (§20 AAA); Spec:337 (§20 DDD); Proposal:94–99; Plan:106; Decisions B6, B7, C4
- **Viewer:** owner
- **Reached from:** The sealed year S-03, Start a highlight S-13. **Leads to:** after every accepted shutter, straight to the note step S-12 for that photo (`PROVISIONAL: C4`); from there back to the camera, or out of capture to S-03

| State | Holds | Must never show |
|---|---|---|
| `sealed` | The in-app camera, photos only. It is offered and looks the same whether or not a frame is available: availability is learned only by trying (`PROVISIONAL: B7`; Rubric R-138). Three taps, then the photo is sealed. The only results are accepted or refused (Proposal:49, 97) | "No retakes" (Spec:55). "no review-before-save" (Spec:228). The photo just taken, as a preview or thumbnail: "No previews, no counts of what is inside, no thumbnails" (Spec:75); no "last shot" corner (Rubric R-005). "No tagging, no writing, no choices" (Spec:54). Video: "No video" (Spec:57). A quality check (Spec:56). Import of a photo not taken in the app (Spec:53). Frames used or left (Proposal:49; Spec:243). A camera control hidden, greyed out or relabelled because no frame is left (Rubric R-138) |
| `sealed`, capture refused (no frame, or the highlight's quota reached) | The refusal. It says capture was refused, with no number (`PROVISIONAL: B7`) `[copy: copywriter]` | Any count or target: "Show a count of how much of their quota is left in a way that reads as a target" (Spec:243); no number at all (Proposal:49; `PROVISIONAL: B7`). When the next frame becomes available (Rubric R-138). **This refusal used for a metadata guard refusal**: that refusal never reaches the user (Spec §20 PP) |
| `sealed`, metadata guard refuses the image (a bug, not a state the user sees) | Nothing the user can tell apart from the press it was. The app strips again and saves that moment once (Spec §20 VV, Spec:326). The retry is judged at the original press instant, so the press gives the photo it would have given: accepted and on to S-12 as after any accepted shutter, or refused as in the row above only if it would have been refused at that instant (Spec §20 XX, Spec:331). It is stored at the original press instant, never later: "The press instant wins", and VV's "the stored time may be slightly later" is retired (decided 2026-10-31, Spec §20 AAA, Spec:334). "One press is one photo, never a retake" (Spec §20 PP, Spec:320). While the app strips again, the camera shows nothing different: "the user sees nothing different" (decided 2026-10-31, Spec §20 DDD, Spec:337) | Any error, warning or refusal from the guard: "A metadata refusal never reaches the user" (Spec §20 PP). The capture refusal copy above in its place. "Try again", a request to press again, or anything that invites a second press for that moment (Spec §20 PP, DDD; Spec:55). A wait, busy or "saving" indicator for the second strip (Spec §20 DDD; Rubric R-140). Two photos from one press (Spec §20 VV). No photo from a press that would have been accepted, except as in the row below (Spec §20 XX, DDD) |
| `sealed`, stripping fails twice for one press (a bug, not a state the user sees) | Nothing different: "the user sees nothing different; that press gives no photo and the bug is logged" (decided 2026-10-31, Spec §20 DDD, Spec:337). The log is not on any screen. The camera then returns as after any press, with no note offer (no S-12), and no frame or highlight place is used (decided 2026-10-31, Spec §20 GGG) | "No error, no 'try again'" (Spec §20 DDD). Any error, warning, refusal or the capture refusal copy (Spec §20 PP). Any sign that this press gave no photo. A request to press again, or anything that invites a second press for that moment (Spec §20 PP; Spec:55). The logged bug, to the user |
| `sealed · highlight open` | The same camera, looking the same. The frame limit does not apply, up to the type's yearly quota (Spec:65, Spec:265, Proposal:96). The plain fact that a highlight is open is shown on S-03 and S-13, not here (`PROVISIONAL: B6`; strictest reading of where it shows) | Highlight photos taken or left, highlights left (Proposal:49). The highlight's end time, "ends in", time left, a timer, or a shrinking bar or ring (`PROVISIONAL: B6`; Rubric R-140) |
| `sealed · note window` | After an accepted shutter, the camera hands straight to the note step S-12 for that photo (`PROVISIONAL: C4`). Nothing on the camera itself marks that a note window is open | As in `sealed`. A timer or time left on the 15 minutes (Rubric R-140) |
| `unlock-day` onward, `no-journey` | Not available. `capture()` "only works on a sealed journey, so nothing can be captured after unlock" (Proposal:99) | A way to add a photo to an unlocked journey |

- **Reads:** Journey, Photo (written, never read back), Highlight (Proposal §2.2), through `capture()`'s accepted or refused only
- **Stored format:** the photo is stored as baseline JPEG; the strip step re-encodes to it (decided 2026-10-30, Spec §20 QQ, Spec:321). None of this is visible to the user: no format, re-encode or quality setting or message on the screen, since there is no quality bar (Spec:56)
- **Copy:** the capture refusal `[copy: copywriter]`. The no-retake line "No retakes. That moment is gone." (Brief:120) `[copy: copywriter]` decides where it sits

### S-03 The sealed year

- **Purpose:** the owner's current journey while it is sealed: an empty state that leaks nothing and reads as intended, and the way out to what the user does instead.
- **Spec source:** Spec:71–76 (§6); Spec:233–234 (§18); Spec:246 (§19); Spec:279 (§20 I); Proposal:48–50, Proposal:84; Plan:107; Brief:71, Brief:130; Decisions B6, B7, B19, C2, C3, C4
- **Viewer:** owner. How others see a sealed journey is a state of S-16 and S-06 ("exists only", Proposal:317)
- **Reached from:** Profile (own) S-05, where the app opens (`PROVISIONAL: C12`); Commit S-01. **Leads to:** Capture S-02, Start a highlight S-13, Positivity Feed S-09, Feed S-08, Layers S-07, Another user's profile S-16, Profile (own) S-05. **Never to** the note step S-12 (`PROVISIONAL: C4`)

**What the spec allows this screen to hold. Exactly this list:**

| # | Element | Source |
|---|---|---|
| 1 | That the owner has a journey underway | Proposal:84 ("The owner also sees type, commit date and unlock date. Nothing else."), Proposal:316 |
| 2 | The journey's type, **by name only**. Not its photos per year, cadence or highlight allowance: at Commit those describe a choice, but beside a running year they read as a target (Spec:243; Rubric R-098). Shown under `PROVISIONAL: B19`, which reads Spec:74 as covering the contents (OQ-39) | Proposal:84, Decisions B19 |
| 3 | The commit date, as a plain date (`PROVISIONAL: B19`, which reads Spec:74 as covering the contents; OQ-39) | Proposal:84, Decisions B19 |
| 4 | The unlock date, as a plain date, never relative to today (`PROVISIONAL: B19`, `C2`) | Proposal:84, Decisions B19, C2, Rubric R-013 |
| 5 | The way to Capture (S-02), offered the same whether or not a frame is left (`PROVISIONAL: B7`; Rubric R-138) | Spec:53, Proposal:99 |
| 6 | The way to start a highlight (S-13), offered the same whether or not a highlight is left, and whether or not one is open: never greyed or relabelled (Rubric R-138) | Spec:264, Proposal:135 |
| 7 | Only in `sealed · highlight open`: the plain fact that a highlight is open, with no end time and no countdown (decided 2026-10-30, Spec §20 S) | Decisions B6, Spec §20 S, Rubric R-140 |
| 8 | The way to what the user does instead: other people's unlocked journeys, through the Positivity Feed, the Feed, Layers and profiles | Spec:76 ("The user's engagement during this period is other people's unlocked journeys, not their own"), Brief:71, Concept:446, Concept:555 |
| 9 | Words that make the wait read as deliberate `[copy: copywriter]` | Plan:79 ("Microcopy for the moments that carry weight: Commit, sealed, …"), Brief:138 |

Not on the list:
- The owner's own earlier, unlocked journeys. This screen does not point to them; their open reflection slots are reached from Profile (own) S-05 (`PROVISIONAL: C3`).
- The note step. It lives only inside capture, S-02 and S-12, and leaving capture ends it, so there is no way back from this screen (`PROVISIONAL: C4`).

**Why it must read as intended, not broken.** The data returns nothing at all: as the owner, no photos and a count of zero (Proposal:179). So any empty-list or still-loading pattern would look like a fault. The emptiness is the product (Brief:130; `ux.md:21`). Phase 2 and the copywriter make it read that way. This file does not.

**The same on every date.** Apart from element 7 while a highlight is open, this screen is identical on every date of the sealed year and before and after every capture (Rubric R-010, R-012).

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Elements 1–6, 8 and 9 | "No previews, no counts of what is inside, no thumbnails" (Spec:75). "Not thumbnails, not counts, not '3 moments captured'" (Brief:46). Frames used, frames left, highlights left (Proposal:49). The year's activity graph or line: "Never during the sealed year" (Spec:187). Anything derived from `captured_at`, such as the last capture or which months have photos, since it is unreadable (Proposal:48, 50). Any note (sealed, Proposal:105). "No visible counters, no progress bars, no reminders during the sealed year" (Spec:233). A countdown or relative date: "in 64 days", "unlocks in", days to go, a timer or a ticking display (`PROVISIONAL: C2`; Rubric R-013). Anything that fills, grows or advances with the date: "month 7 of 12", an elapsed-time bar or arc (Rubric R-012). The type's photos per year, cadence or highlight allowance (Spec:243; Rubric R-098). The Capture or highlight control hidden, greyed out or relabelled because nothing is left, or any hint of when a frame comes back (Rubric R-138). A pointer to open reflection slots on earlier journeys (`PROVISIONAL: C3`). A way back to the note step (`PROVISIONAL: C4`). A reminder to capture (Spec:242). A prompt to photograph a low point: "The app does not prompt anyone to document a bad moment" (Spec:209). A way to change type or abandon (Spec:44, Spec:263). A second Commit (Spec:273) |
| `sealed · highlight open` | Elements 1–9: as `sealed`, plus element 7 (Spec §20 S) | As in `sealed`. Highlight photos taken or left (Proposal:49). The highlight's end time, "ends in", time left, a timer, or a shrinking bar or ring (`PROVISIONAL: B6`; Rubric R-140) |
| `sealed · note window` | **Identical to `sealed`.** The note step is not reachable from here (`PROVISIONAL: C4`) | As in `sealed`. Any way back to the note step (`PROVISIONAL: C4`). Anything that differs because a photo was just taken: "A capture changes nothing that any reader can observe, the owner included" (Rubric R-010). The photo the note belongs to |
| `unlock-day` | The screen gives way to Reveal S-04, reached on the owner's next open through "Your Journey is ready" (`PROVISIONAL: C1`) | Nothing from the sealed list carries over: the whole journey opens at once (Spec:73). A notification that it has unlocked (`PROVISIONAL: C1`; Spec:236) |
| `no-journey` | Not reached. Commit S-01 is open instead | |

- **Reads:** Journey (type, `committed_at`, `unlocks_at` only); for element 7, whether a highlight is open, and nothing else about it (Proposal §2.2; Spec §20 S)
- **Copy:** the sealed state `[copy: copywriter]` (Plan:79). Approved lines exist (Brief:115–122, for example "This app takes time, like many other good things."). Where each goes is the copywriter's call

### S-04 Reveal

- **Purpose:** the annual moment. The whole journey opens and the owner writes reflections, tags people, applies the chapter and feeling tags, writes the overview and sets visibility, each choice once.
- **Spec source:** Spec:80–91 (§7); Spec:269 (§20 9); Spec:276 (§20 F); Spec:285–286 (§20 O, P); Proposal:25 (D12); Proposal:408 (R5); Plan:108; Brief:73; Decisions B3, B8, B13, C1, C5
- **Viewer:** owner
- **Reached from:** the owner's next open after unlock, through "Your Journey is ready" on Profile (own) S-05, where the app opens (`PROVISIONAL: C1` with `C12`); Profile (own) S-05 at any later time. **Leads to:** Reflect S-14, Tag people S-18, Chapter and feeling tags S-19, Journey overview S-15, Visibility S-20, Finish the reveal S-21

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not reachable | Anything: "Sealed content is unreadable by the owner, not merely hidden in the UI" (Spec:234) |
| `unlock-day` | The whole journey at once: every photo and its note (Spec:73, Spec:255). Every photo is Network until the owner chooses (Spec:151). "Your Journey is ready" `[copy: copywriter]` (Plan:79, Concept:740), shown on the owner's next open (`PROVISIONAL: C1`) | Photos opening one by one: "Photos do not open individually" (Spec:73). A notification at unlock (`PROVISIONAL: C1`; Spec:236) |
| `reveal-open` | The five reveal steps (Spec:84–88), each reachable, **none required** before finishing (`PROVISIONAL: C5`). A choice already made is shown where it was made, with its own photo, read-only (Spec:286, Proposal:408). Before each set-once choice is saved, one line saying it can't be changed (`PROVISIONAL: C5`) `[copy: copywriter]` | A way to change a set choice: "Each reveal choice is set once, even before the reveal is finished" (Spec:286). A way to edit or delete a photo: "A photo can never be deleted" (Spec:266). Suggested faces: "No face recognition, ever" (Spec:127). A reminder to finish (Spec:242). **A completion meter in any form**: a progress bar, a percentage, "12 of 24 tagged" or "reflected", a checklist of steps, a tick per photo or step, or a summary of how much is done or left (`PROVISIONAL: B8`; Brief:42 bans them outright, Spec:233 only during the sealed year; Rubric G-4, R-099). The album order step: "Optionally orders the physical album (the album phase)" (Spec:89) is not in this build |
| `reveal-finished` | The journey with its choices, locked and read-only (Spec:276). Reflect stays open for slot 1 (Proposal:117). The slot 1 overview can still be written while slot 1 lasts (`PROVISIONAL: B13`) | Any way to change visibility, people tags, chapter or feeling tags (Spec:276, Proposal:46) |
| `later-years · finished` | As `reveal-finished`, with slot *k* open for Reflect and Journey overview | As `reveal-finished`. A banner, dot or marker that slot *k* is open (Spec:102; Rubric R-095, R-096) |
| `later-years · never finished` | Every photo Network unless the owner already made a choice, which took effect when made. The reveal can still be finished at any later time, and each unmade choice can still be made once (`PROVISIONAL: B3`). Spec:269 says "There's no chapter, no tags"; B3 reads that as "none unless set" (Rubric G-11) | "no 'journey launched'" and no layer update until finished (Spec:269). A reminder or marker that the reveal is unfinished (Spec:242; Rubric R-095) |

- **Reads:** Journey, Photo, Handwritten note, Reflection, Journey overview, Tag (Proposal §2.2); `journey_reveal`, `person_tag`, `photo_visibility` (Proposal:164–166)
- **Copy:** "Your Journey is ready" `[copy: copywriter]`; the reveal itself `[copy: copywriter]` (Plan:79, Brief:138); the one-line "this can't be changed" `[copy: copywriter]`

### S-05 Profile (own)

- **Purpose:** the owner's destination, and where the app opens: the circle with the owner's name in it, its rings, the activity line twisted into it, and the way into their own journeys.
- **Spec source:** Spec:181–187 (§14); Spec:29 (§2); Proposal:65; Concept:681–714 (§21); Plan:109; Brief:85; Decisions B4, B5, B19, C1, C3, C7, C9, C12
- **Viewer:** owner. Others see S-16
- **Reached from:** app entry, in every state (`PROVISIONAL: C12`); Reveal S-04; Layers S-07 (the core). **Leads to:** Walking a path S-06 (own), and through it the owner's earlier journeys, where open reflection slots are reached (`PROVISIONAL: C3`); Reveal S-04 when a reveal is open; Commit S-01 in `no-journey`; Journey overview S-15; The sealed year S-03; and the app's other screens, Layers S-07, Feed S-08 and Positivity Feed S-09 (how is Phase 2)

**Rings: `PROVISIONAL: B4` (switchable).** Spec:185 ("One ring per year with the app") and Concept:687 disagree with Proposal:65 ("one ring per journey whose reveal is finished") (Rubric G-7; OQ-6).
- **Default: one ring per finished reveal** (Proposal:65). A journey whose reveal is never finished adds no ring (Long Way Round #4). A user with no finished reveal has none (First Light).
- **Option: one ring per year with the app** (Spec:185). Rings follow years since joining. Finishing a reveal adds nothing to the circle. These per-year rings show **only here, on the owner's own profile**. Every other viewer sees this user's circle on S-16 with one ring per finished reveal, so no one else learns the join year (decided 2026-10-31, Spec §20 WW, Spec:330; Spec §20 TT).

Under either option a ring is a record of time, not a reward. It never arrives as an achievement, with a celebration or "you earned", and more rings never read as better (Spec:185: "A record, not a rank"; Rubric R-102).

**Activity line and graph: `PROVISIONAL: B5`.** The line twists into the circle when the reveal is finished (not switchable). The graph is switchable: **default owner only**; option, built only from the photos the viewer can see. On this screen the viewer is the owner, so the switch changes nothing here. It changes S-16.

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed | The owner's name in the circle, no rings (`PROVISIONAL: C7`, `B4`). "A person who joined this year is not behind; their circle is simply younger" (Concept:694). An empty circle is a plain statement (`PROVISIONAL: C9`) | "no scores, no levels, no leaderboard, no badges, no comparison between users" (Spec:185). Anything that "signals how the person looks or how well they are doing" (Spec:29). A profile picture (Spec §20 YY) |
| `sealed` (current journey) | Rings and activity lines of earlier journeys. The current journey as existing, with its type by name and its commit and unlock dates as plain dates (Proposal:84; `PROVISIONAL: B19`, `C2`; see OQ-39) | The current year's activity graph: "Never during the sealed year. A visible grid being filled is a streak mechanic and is banned" (Spec:187). **A ring, arc or segment for the current year that is partial, growing, dated or filling**, or anything that changes with the date inside the sealed year (Rubric R-012). A countdown or relative unlock date (`PROVISIONAL: C2`; Rubric R-013). The type's photos per year, cadence or allowance (Rubric R-098). Any thumbnail or count from the sealed journey (Spec:75). A banner, dot or marker that reflections are open on an earlier journey (Spec:102; Rubric R-095, R-096) |
| `unlock-day`, `reveal-open` | "Your Journey is ready", on the owner's next open after unlock, as the way into Reveal S-04 (`PROVISIONAL: C1`, `C12`). The year's activity graph, to the owner: "only after the year unlocks" (Spec:187; `PROVISIONAL: B5`). The activity line is not twisted in yet (`PROVISIONAL: B5`). Under B4's default this journey has no ring yet; under the option, rings follow years with the app | As in `sealed`, for any other journey still sealed. A completion meter for the reveal (`PROVISIONAL: B8`). A reminder to finish (Spec:242) |
| `reveal-finished` | Under B4's default, this journey's ring. The year's activity line twisted into the circle (Spec:186; `PROVISIONAL: B5`) | A ring presented as an achievement or a reward for finishing: "A record, not a rank" (Spec:185; Rubric R-102) |
| `later-years` | Rings as B4 gives them. The overview stack, readable back to back (Spec:121). The way into earlier journeys, where slot *k* reflections are reached (`PROVISIONAL: C3`) | As above. **On the unlock anniversary, an in-app banner, dot, toast or "Year 3 reflections are open" marker** (Spec:102: "never pushed or reminded to write one"; Rubric R-095, R-096) |
| `no-journey` · between journeys | As `reveal-open`, `reveal-finished` or `later-years` for the last journey, plus the way to Commit S-01 | As above. A prompt to commit again (Spec:242) |

- **Reads:** User (name; the owner's own `joined_at`, only for B4's per-year option, Spec §20 TT, WW), Journey, Photo (`captured_at`, for the activity graph, after unlock only, Proposal:50; the full time, since the viewer is the owner, Spec §20 GG), Journey overview (Proposal §2.2)
- **Copy:** the young circle of a new user `[copy: copywriter]`; the empty circle `[copy: copywriter]` (`PROVISIONAL: C9`)

### S-06 Walking a path

- **Purpose:** read a person's journeys from the beginning to now, in order, with the hard times and the reflections written later.
- **Spec source:** Spec:191–196 (§15); Spec:149 (§11); Spec:177 (§13); Concept:563–582 (§16); Plan:110; Decisions B2, B12, B19, C6
- **Viewer:** owner, network, public (signed-in, `PROVISIONAL: B14`), tagged. What each sees of the photos depends on photo visibility (Spec:143–147, Proposal:312–320). A journey's type, dates, chapter and feeling tags reach the owner and network only, never public (Spec §20 T, CC); a tagged reader who is not on the owner's network reads them as public
- **Reached from:** Profile (own) S-05, Another user's profile S-16, Feed S-08, Positivity Feed S-09. **Leads to:** A photo, followed forward S-17, Journey overview S-15, Another user's profile S-16

**Before the reveal is finished: `PROVISIONAL: B2` (switchable).** Concept:362 ("Only possible after unlock, and as a finished story or album") disagrees with Spec:151, Spec:269 and Proposal:318 (OQ-9).
- **Default: from unlock.** Others read an unlocked journey from the moment of unlock, by each photo's visibility, Network by default (Proposal:25 D12, Proposal:318).
- **Option: only after reveal finished.** No one but the owner reads it until the reveal is finished, Public photos included (decided 2026-10-30, Spec §20 R).

**Where the reader appears: `PROVISIONAL: B12` (switchable).** Spec:196 ("The reader sees where they themselves appear") against Spec:164 and Spec:235 (OQ-19; Rubric G-12).
- **Default: shown.** On photos the reader can already see (Proposal:293), those where the reader is tagged say so, in place, in journey order. No total, no grouping, no separate list of "your" photos (Decisions B12; Rubric R-139).
- **Option: hidden.** The path reads the same for a tagged reader as for any other.

**Other people's tags: `PROVISIONAL: C6` (switchable).** **Default: hidden from readers.** Option: shown, in place on each photo, under the same bans (no count, no grouping, no list; Rubric R-139). See S-17.

| State (of each journey on the path) | Holds | Must never show |
|---|---|---|
| `sealed` | Owner: exists, type by name, commit date and unlock date as plain dates (`PROVISIONAL: B19`). Others: exists only (Spec:279, Proposal:84, Proposal:317) | "Reveal anything about a sealed journey, including its existence in detail" (Spec:246). Any photo, count, thumbnail or capture date (Spec:75). A countdown or relative unlock date (`PROVISIONAL: C2`). A partial or growing mark for the year (Rubric R-012) |
| `unlock-day`, `reveal-open` | Owner: every photo. Under B2's default: network, every photo not yet set Private, because Network is the default (Spec:151, Proposal:318: Open Hands reads Long Way Round #4); public, only photos already set Public, since a choice takes effect when made (`PROVISIONAL: B3`). Under B2's option: no photo for anyone but the owner yet, Public included (Spec §20 R), nothing that follows a photo, and no journey overview (Spec §20 HH); the network still reads the journey's type and dates, and its chapter and feeling tags once set (Spec §20 X). Owner and network, under either option: type and dates, and chapter and feeling tags once set (Spec §20 T). Public: none of the four. No chapter or feeling tags until set | Private photos to anyone but the owner (Spec:145, Proposal:29). **Type, dates, chapter or feeling tags to a public reader** (Spec §20 T, CC; Rubric R-152) |
| `reveal-finished` | Photos by their locked visibility. Reflections follow their photo (Spec:276). The overview, to the owner and network only (Spec:275; `PROVISIONAL: B13`). Type, dates, chapter and feeling tags, to the owner and network only (Spec §20 T) | As above |
| `later-years` | As `reveal-finished`, with deeper reflection stacks and an overview stack (Spec:121) | As above. For the owner, a banner, dot or marker that slot *k* is open (Rubric R-095, R-096) |

On every journey, for every viewer, never: a grid: "in order, not as a grid" (Spec:193). An effortless scroll into it: "It must not be as effortless as scrolling" (Spec:177). Endless or infinite scroll, autoplay, or "more like this" (Brief:49; Rubric R-104). A comment or reply: "Others may read; only the owner writes" (Spec:100). The viewer's own ring on this person's map (Spec:164, Spec:235). A total of the photos anyone appears in, a grouping of photos by the person tagged, or a "people in this journey" list (Rubric R-139). Access through being tagged: "being tagged doesn't give access" (Proposal:293). **To a public reader, the journey's type, commit or unlock date, chapter or feeling tags** (Spec §20 T, CC; Rubric R-152). **To anyone but the owner, whether a photo was taken in a highlight, also after unlock: no marker, grouping or label on highlight photos** (Spec §20 DD; `PROVISIONAL: B24`; Rubric R-151). **To anyone but the owner, a photo's capture time of day: a non-owner reads the capture date only** (decided 2026-10-30, Spec §20 GG; Rubric R-154). **To anyone but the owner, when a photo's note was written, not even the date** (decided 2026-10-30, Spec §20 LL, Spec:316). **To anyone but the owner, an order of same-day photos that carries time**: where the path runs "in order" (Spec:193), photos sharing a capture date sit in a fixed order with no time information (decided 2026-10-30, Spec §20 JJ, Spec:314; OQ-46). **To a public reader, whether a journey's reveal is finished, as a field, label or marker** (Spec §20 SS, ZZ; inferring it from which photos appear is allowed, Spec §20 ZZ). **Another user's join date** (Spec §20 TT).

- **Reads:** User (name; `joined_at` never, unless the viewer is that user, Spec §20 TT), Journey (type, dates, chapter and feeling tags for owner and network only, Spec §20 T; whether the reveal is finished for owner and network only, Spec §20 SS), Photo (`captured_at` in full for the owner, as a date only for anyone else, Spec §20 GG; never `highlight_id` for a non-owner, Spec §20 DD), Handwritten note (for a non-owner, never when it was written, not even the date, Spec §20 LL; Rubric R-154), Reflection, Journey overview, Tag (chapter and feeling tags as Journey; Proposal §2.2); `photo_visibility`, `person_tag` (Proposal:165–166)
- **Copy:** the moment a reader finds themselves in someone's hard year `[copy: copywriter]` (Concept:578–582: "Design for it deliberately"). Under B12's option it does not occur

### S-07 Layers

- **Purpose:** the owner's own map: the user at the core, people on concentric rings earned by crossing journeys, and the way to their profiles.
- **Spec source:** Spec:156–165 (§12); Spec:277–278, Spec:282 (§20 G, H, L); Proposal:27–29 (D14–D16); Proposal:145–160; Plan:111; Brief:81; Decisions C7, C8, C9
- **Viewer:** owner only. "Each user sees only their own map" (Spec:164)
- **Reached from:** Profile (own) S-05, The sealed year S-03. **Leads to:** Another user's profile S-16

The map changes only when the owner finishes a reveal. So the table follows the **owner's** journey states. The map shows **current rings only**: no counts, no history, no drift (`PROVISIONAL: C8`). Each person is shown by name (`PROVISIONAL: C7`).

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed, or no reveal ever finished | The core only: "First Light's map is empty" (Proposal:291). The empty map is a plain statement (`PROVISIONAL: C9`) | People who were never tagged. A way to add someone by choice: "Earned, not chosen" (Spec:160). An empty-state call to action (Rubric R-095) |
| `sealed` | The map as computed at the last finished reveal, unchanged | Any change: "Layers are recalculated at this point, never during the sealed year" (Spec:91) |
| `unlock-day`, `reveal-open` | Unchanged | Any change before finish: "the layers aren't recomputed" (Spec:269) |
| `reveal-finished` | Recomputed: users tagged in the journey at tight (5+), middle (2–4) or outer (1) by count, straight to that ring (Spec:161, Spec:282). Untagged members out one ring (Spec:165). Each person on their current ring only (`PROVISIONAL: C8`) | Anyone dropping off: "Nobody ever drops off the map" (Spec:165). Typed names: "Typed names never count" (Spec:163). The count of shared photos, a past ring, drift history, or a "moved in" or "moved out" mark (`PROVISIONAL: C8`) |
| `later-years` | Unchanged until the next finished reveal | |

On every state, never: another user's map, or where the owner sits on it: "A person is never shown which layer they are on" (Spec:164), "No endpoint returns which layer a viewer sits on in someone else's map" (Spec:235). A list: "the Apple Watch app menu, not a list" (Spec:159). Extra access for the inner ring: close friends "see nothing beyond the rest of the network" (Spec:150). "No ranking, levels, badges or leaderboards" (Brief:44). Past rings, drift history or shared-photo counts (`PROVISIONAL: C8`). A profile picture (Spec §20 YY). Anyone's join date (Spec §20 TT).

- **Reads:** Layer (latest entry per member only, Proposal:150), User (Proposal §2.2)
- **Copy:** how the map is described, including that outward drift is expected, "treated as a feature, not a failure" (Spec:165), without showing anyone's movement (`PROVISIONAL: C8`) `[copy: copywriter]`. The empty map `[copy: copywriter]`

### S-08 Feed

- **Purpose:** announcements only, on three events, each a line the reader may choose to act on.
- **Spec source:** Spec:169–177 (§13); Spec:280, Spec:283 (§20 J, M); Spec:325 (§20 UU); Spec:332 (§20 YY); Proposal:31 (D18); Proposal:168; Proposal:405 (R2); Plan:112; Brief:83; Decisions B1, B10, B11, C7, C9, C14
- **Viewer:** any user, each announcement to its own audience: "journey launched" and "path crossed" to the owner's network (Spec:283); "reflection left" only to people who can see that photo (Spec:280), which means only the owner's network members who can see it, even when the photo is public: a public reader off the owner's map never receives it (`PROVISIONAL: B10`). **The owner's own announcements:** the owner sees their own "reflection left", and never their own "journey launched" or "path crossed" (decided 2026-10-31, Spec §20 UU, Spec:325). The owner is not on their own map, so B10's network limit does not take this line away; §20 UU holds over the provisional default for the owner, and B10 still holds for everyone else (`docs/reviews/2026-10-31-rules-phase-1-r6.md` N2)
- **Reached from:** The sealed year S-03; the app's navigation from Profile (own) S-05, where the app opens (`PROVISIONAL: C12`; the navigation itself is Phase 2). **Leads to:** Another user's profile S-16, Walking a path S-06, A photo, followed forward S-17, each by "a small deliberate act" (Spec:177)

**Order: newest first** (`PROVISIONAL: C14`). No order uses read state, popularity or the reader's ring.

**"Path crossed": `PROVISIONAL: B11` (switchable).** It reaches the owner's network and never says which ring.
- **Default: named.** It names both people.
- **Option: unnamed.** It names only the owner.

The table follows the state of the **announced** journey.

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Nothing about it. No announcement exists for Commit or capture | Anything about a sealed journey (Spec:246) |
| `unlock-day`, `reveal-open` | "Reflection left", if the owner writes one (Proposal:117), to the owner's network members who can see the photo (`PROVISIONAL: B10`), and to the owner (Spec §20 UU). Under B2's option no one else can see the photo yet, so it reaches no one but the owner | "Journey launched" or "path crossed" before finish: "There's no chapter, no tags, no 'journey launched'" (Spec:269) |
| `reveal-finished` | "Journey launched" (Spec:280). "Path crossed", one per crossing (Spec:280), named or unnamed by B11. "Reflection left", to the owner's network members who can see the photo (`PROVISIONAL: B10`) and to the owner (Spec §20 UU) | Which ring anyone is on, or that anyone moved (Spec:164; `PROVISIONAL: B11`). The owner's own "journey launched" or "path crossed" in the owner's feed (Spec §20 UU). Any announcement to a public reader off the owner's map (`PROVISIONAL: B10`) |
| `later-years` | "Reflection left" for new slot reflections | |
| (viewer with an empty network) | Nothing reaches them: "reflection left" on a public photo goes only to the owner's network (`PROVISIONAL: B10`). The empty feed is a plain statement (`PROVISIONAL: C9`) | An empty-state call to action (Rubric R-095) |

On every state, never: an image: "Announcements only. No photographs in the stream" (Spec:171), "no media column" (Proposal:168), and no profile picture beside an announcement (Spec §20 YY; Decisions C7). A fourth event type (Proposal:168, Proposal:184). A count: "no count column" (Proposal:168). Likes or replies (Proposal:181). Ordering or selection by popularity: no line bans it for this feed by name; the nearest are "No ranking, levels, badges or leaderboards" (Brief:44) and the newest-first order (`PROVISIONAL: C14`). **An unread dot, badge count, "new" marker, "since your last visit" divider, or a badge on the feed's way in or on the app icon** (Rubric R-096). **Endless or infinite scroll, autoplay, or pull to refresh into new content** (Brief:49; Rubric R-104). A push to return: "No re-engagement notifications of any kind" (Spec:236).

- **Reads:** User (name only; never another user's `joined_at`, Spec §20 TT), Journey, Photo (visibility, for the audience), Reflection (Proposal §2.2); `announcement` (Proposal:168)
- **Copy:** the three announcement lines `[copy: copywriter]`. The source wording ("published their Journey", Concept:424, 440) uses "publish", which means "reveal finished" (`PROVISIONAL: B1`); the lines use "reveal finished" and "journey launched" only. The empty feed `[copy: copywriter]`

### S-09 Positivity Feed

- **Purpose:** reflections written years later on other people's hard moments, filtered by tags of endurance and gratitude, so someone on a bad day finds a person who was where they are.
- **Spec source:** Spec:200–209 (§16); Spec:30 (§2); Spec:335 (§20 BBB); Proposal:322–330; Concept:450–559 (§15); Plan:113; Brief:87; Decisions B9, B18
- **Viewer:** any signed-in user (`PROVISIONAL: B14`). Content is public only, chosen per photo (Spec:147, Spec:203; `PROVISIONAL: B9b`)
- **Reached from:** Sign up (day one, Spec:30; not in the prototype, `PROVISIONAL: C11`); The sealed year S-03; the app's navigation from Profile (own) S-05 (`PROVISIONAL: C12`). **Leads to:** A photo, followed forward S-17, Walking a path S-06, Another user's profile S-16. Each destination applies its own reader limits: a public reader arriving from here sees no type, dates, chapter or feeling tags there either (Spec §20 T, CC)

**`PROVISIONAL: B9`.** (b) Visibility is per photo, not per journey (OQ-12). (c) Only the drafted tag list qualifies (Spec:207): the four working tags, gratification, it eventually pays off, hang in there, thankful (decided 2026-10-30, Spec §20 W); a free-text tag such as Steady Lantern #5's "slow is still forward" does not. (d) No chapter filter (decided 2026-10-30, Spec §20 Y). (f) A photo enters only after its journey's reveal is finished. (a) and (e) are decided, not switchable:
- **(a) Text only (decided 2026-10-30, Spec §20 Q).** Each entry is a reflection's text. The photograph is shown only when the reader opens the entry, in S-17.
- **(e) Newest reflection first, by the reflection's written time (decided 2026-10-31, Spec §20 BBB, Spec:335).** Replaces the provisional "newest first".

The table follows the state of the **source** journey. The reader's own state changes nothing: the same feed serves a new user (Spec:30) and a user in a sealed year (Concept:555).

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Nothing from it | Anything (Spec:246) |
| `unlock-day`, `reveal-open` | Nothing from it, even a photo already set Public (`PROVISIONAL: B9f`) | Network or private content |
| `reveal-finished` | Reflections on public photos from journeys tagged with a drafted endurance or gratitude tag (Spec:202, Spec:207; Proposal:324; `PROVISIONAL: B9b`, `B9c`). Text only; the photograph only when one entry is opened (Spec §20 Q). No chapter filter (Spec §20 Y). Newest reflection first, by the reflection's written time (Spec §20 BBB) | Ordering or selection by popularity: "never by popularity" (Spec:202; Rubric R-103). "Public means readable, not commentable" (Spec:152). A tag outside the drafted list (`PROVISIONAL: B9c`). Tags surfaced, suggested or counted by popularity (`PROVISIONAL: B18`). **The feeling tag that selected an entry, or any feeling tag, chapter, journey type or date, on an entry or as a filter label**: the feed may select by feeling tag but the reader sees reflection text only (Spec §20 CC, T, Q; Rubric R-152). Whether the photo was taken in a highlight (Spec §20 DD; Rubric R-151). The source journey's reveal state as a field, label or marker, such as "launched" or "finished": that an entry appears at all may imply it, which is allowed (Spec §20 SS, ZZ; `PROVISIONAL: B9f`). The author's join date (Spec §20 TT) |
| `later-years` | The same, with reflections written years after the moment, which is the feed's primary use (Spec:204) | As above |

On every state, never: a prompt to capture a low point: "invited, never nudged" (Spec:209). Likes, reactions, views or counts (Proposal:181). **Endless or infinite scroll, autoplay, "more like this", or pull to refresh into new content** (Brief:49; Rubric R-104). An unread dot or "new" marker (Rubric R-096).

- **Reads:** Photo, Reflection, Tag, Journey, User (Proposal §2.2); `photo_visibility` (Proposal:166). Tag and Journey serve only to select entries; no tag, chapter, type or date reaches the reader (Spec §20 CC, T). How the selection runs without returning the tag is the data layer's, not this screen's
- **Copy:** the feed's purpose, for someone having a bad day `[copy: copywriter]`; the founding line "the hard part was the start" is a drafted tag (Spec:207, Concept:544)

---

## Screens the spec implies beyond the nine

### S-10 Sign up

- **Purpose:** an open way in for anyone, invited or not.
- **Spec source:** Spec:25–30 (§2)
- **Viewer:** a person without an account
- **Reached from:** outside the app; invitation is the main path (Spec:28; how it works is OQ-32). **Leads to:** Choose a name S-11, then the day-one experience: Positivity Feed S-09 and other people's profiles (Spec:30)
- **In the prototype:** not built. There is no sign-up or onboarding; fixture users are picked from the options panel T-02 (`PROVISIONAL: C11`). Listed because the product needs it

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed (only state) | Sign up | An invite gate: "Open signup. Anyone can join. No invite gate" (Spec:27). Any field about looks or status (Spec:29). A request for notification permission (`PROVISIONAL: C15`) |

- **Reads:** User (Proposal §2.2)
- **Copy:** the arrival `[copy: copywriter]`

### S-11 Choose a name

- **Purpose:** the user chooses a name from within, once, for good.
- **Spec source:** Spec:29 (§2); Spec:268 (§20 8); Proposal:32 (D19); Proposal:61; Concept:665–677 (§20)
- **Viewer:** owner (new user)
- **Reached from:** Sign up S-10. **Leads to:** Positivity Feed S-09 (Spec:30)
- **In the prototype:** not built; the fixture users already have names (`PROVISIONAL: C11`)

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed (only state) | The name, chosen once (Spec:268) | A way to change the name later: "Set once, immutable" (Proposal:61). A yearly name: "Decided 2026-10-25: no" (Concept:677). A prompt toward physical or earthly attributes (Spec:29). A profile picture (Spec §20 YY) |

- **Reads:** User (Proposal §2.2)
- **Copy:** what "a name from within" means, and that it is kept `[copy: copywriter]`

### S-12 The note step

- **Purpose:** straight after capture, inside the capture flow, an optional, skippable offer to photograph a handwritten A4 page, which becomes the writing on the back of the photo.
- **Spec source:** Spec:16 (§1); Spec:257 (§20 B); Spec:281 (§20 K); Proposal:21 (D8); Proposal:101–108; Brief:69; Decisions C4, B16
- **Viewer:** owner
- **Reached from:** Capture S-02 only, straight after an accepted shutter (`PROVISIONAL: C4`). Never from The sealed year S-03 or any other screen. **Leads to:** the camera S-02, or out of capture to S-03

| State | Holds | Must never show |
|---|---|---|
| `sealed · note window` | The offer to photograph one handwritten A4 page, live in the app's camera, once, and a way to skip (Spec:257; `PROVISIONAL: C4`). One note per photo (Proposal:104). The step ends when the page is taken, when the user skips or leaves capture, or when 15 minutes have passed since the photo, whichever comes first (Spec:281; `PROVISIONAL: C4`, `B16`; "skip ends it" is the strictest reading of C4, see OQ-24) | The photo it belongs to (Spec:75). **The page just photographed: no preview, thumbnail or review-before-save** (Spec:228; Rubric R-005). **A re-shoot of the page** (`PROVISIONAL: C4`; Rubric R-020, R-031). A page from the gallery or any import (`PROVISIONAL: C4`). **A timer, countdown, "minutes left", or a shrinking bar or ring on the 15 minutes** (Rubric R-140). A typed text field in place of the page: it is "A photographed A4 page" (Spec:16). Anything that holds up capture: "Skippable, so capture stays fast" (Spec:257). A second note for the same photo |
| `sealed`, after the step has ended | Not offered: "up to 15 minutes after capture, never after" (Spec:281). Leaving capture ends it sooner (`PROVISIONAL: C4`) | Any way back to it, from S-03 or anywhere else (`PROVISIONAL: C4`) |
| `unlock-day` onward | Not a writing step. The note is read as the back of its photo in S-17 | Any way to rewrite it: "written once" (Spec:16) |

- **Reads:** Photo (id only), Handwritten note (Proposal §2.2)
- **Copy:** the offer, and the skip `[copy: copywriter]`. That the page is taken once, like the photo `[copy: copywriter]`

### S-13 Start a highlight

- **Purpose:** the user opens a 24-hour window in which the frame limit does not apply.
- **Spec source:** Spec:63–67 (§5); Spec:264–265 (§20 4, 5); Spec:284 (§20 N); Proposal:19 (D6); Proposal:128–135; Brief:65; Decisions B6, B16
- **Viewer:** owner. Others learn nothing about highlights (`PROVISIONAL: B6`; Spec:279)
- **Reached from:** The sealed year S-03. **Leads to:** Capture S-02

| State | Holds | Must never show |
|---|---|---|
| `sealed`, no highlight open | The way to start one, offered the same whether or not any highlight is left: availability is learned only by trying (Rubric R-138). Accepted, or refused once the type's allowance is used (Proposal:135). The window is 24 hours of elapsed time, cut off at unlock (Proposal:133; `PROVISIONAL: B16`) | Highlights left or used: "Frames used, frames left and highlights left are counted inside them and never stored or returned" (Proposal:49). A start control hidden, greyed out or relabelled because none is left (Rubric R-138). The season as a rule: "Explorer's 'one per season' is a description, not a rule" (Spec:264) |
| `sealed · highlight open` | The plain fact that a highlight is open, with no end time (Spec §20 S). The way to start one, offered the same as when none is open; starting another is refused (Spec:284; Rubric R-138) | As above, including a start control hidden, greyed out or relabelled because one is open (Rubric R-138). **The highlight's end time, "ends in", time left, a timer, or a shrinking bar or ring** (`PROVISIONAL: B6`; Rubric R-140). Highlight photos taken or left (Proposal:49). Anything about the highlight to anyone but the owner (`PROVISIONAL: B6`; Rubric R-008) |
| `unlock-day` onward, `no-journey` | Not available: "Only on a sealed journey" (Proposal:135) | |

- **Reads:** Highlight, Journey (Proposal §2.2), through `start_highlight()`'s accepted or refused only, and whether a highlight is open (Spec §20 S)
- **Copy:** starting a highlight; the refusal `[copy: copywriter]`

### S-14 Reflect

- **Purpose:** the owner writes one reflection on one photo for the current slot, added to the stack and never edited.
- **Spec source:** Spec:95–102 (§8); Spec:274 (§20 D); Proposal:22 (D9); Proposal:24 (D11); Proposal:110–117; Brief:75; Decisions B10, C3
- **Viewer:** owner writes. Readers are the photo's readers (Spec:276)
- **Reached from:** Reveal S-04, A photo, followed forward S-17 (on earlier journeys, from Profile (own) S-05, `PROVISIONAL: C3`). **Leads to:** back to where it came from. Writing one emits "reflection left" (Spec:280) to the owner's network members who can see the photo, even when it is public (`PROVISIONAL: B10`), and to the owner (Spec §20 UU), seen in S-08

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | The photo (Spec:234) |
| `unlock-day`, `reveal-open`, `reveal-finished` | Slot 1 open: one reflection per photo (Proposal:117: "any time after unlock (reveal finished or not)") | A second reflection in a slot already used: "One reflection per photo, per year" (Spec:97) |
| `later-years` (either variant) | Slot *k* open. Earlier reflections read-only, in order. All photos of the journey move to the next slot together on the unlock anniversary (Spec:101) | Per-photo anniversaries (OQ-1; corrected under Decisions A1). **On the anniversary, an in-app banner, dot, toast or "Year 3 reflections are open" marker** (Spec:102; Rubric R-095, R-096) |

On every state, never: an edit or delete: "Immutable. No edits, ever" (Spec:99). Anyone else writing: "No comments from others" (Spec:100). A push: "The user is never pushed or reminded to write one" (Spec:102). A requirement to write one. A count of photos reflected on or still without a reflection in this slot, or any completion meter (`PROVISIONAL: B8`; Rubric R-099).

- **Reads:** Photo, Handwritten note, Reflection (Proposal §2.2)
- **Copy:** that a reflection is final once written `[copy: copywriter]`. "Strict at capture. Generous at reflect." (Brief:119)

### S-15 Journey overview

- **Purpose:** the owner writes how their views changed across the year, once per journey per year, and reads the stack.
- **Spec source:** Spec:115–121 (§9); Spec:275 (§20 E); Spec:285 (§20 O); Spec:312 (§20 HH); Proposal:23 (D10); Proposal:119–126; Brief:77; Decisions B13, B2
- **Viewer:** owner writes. Owner and network read (Spec:275, Proposal:126), never public and never signed-out (`PROVISIONAL: B13`, `B14`). Before the reveal is finished, others read it as B2 allows for the rest of the journey: under B2's default, from unlock; under B2's option, the network reads it only once the reveal is finished (decided 2026-10-30, Spec §20 HH, Spec:312)
- **Reached from:** Reveal S-04, Profile (own) S-05, Walking a path S-06. **Leads to:** back to where it came from

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Nothing | Anything about the journey (Spec:234) |
| `unlock-day`, `reveal-open` | Slot 1 overview may be written. Optional (Spec:285) | A requirement to write one before finishing: "A reveal can be finished without one" (Spec:285) |
| `reveal-finished` | The slot 1 overview, if written, and the way to write it while slot 1 lasts (`PROVISIONAL: B13`) | |
| `later-years` | A new overview for slot *k*. The stack, readable back to back (Spec:121) | A banner, dot or marker that slot *k* is open (Rubric R-095, R-096) |

On every state, never: an edit: "Immutable, like everything else" (Spec:120). A reminder. A public or signed-out reader (`PROVISIONAL: B13`, `B14`).

- **Reads:** Journey, Journey overview (Proposal §2.2)
- **Copy:** the prompt to look back across the year `[copy: copywriter]`

### S-16 Another user's profile

- **Purpose:** another person's circle with their name in it, their rings and the way into their journey, read on purpose.
- **Spec source:** Spec:181–187 (§14); Spec:149–150 (§11); Spec:164 (§12); Spec:279 (§20 I); Spec:323–324 (§20 SS, TT); Spec:330 (§20 WW); Spec:332–333 (§20 YY, ZZ); Spec:336 (§20 CCC); Proposal:30 (D17); Proposal:84; Proposal:312–320; Decisions B2, B4, B5, C6, C7, C10
- **Viewer:** network or public (any other signed-in user, `PROVISIONAL: B14`). After unlock, a journey's type, dates, chapter and feeling tags reach a network viewer only, never a public one (Spec §20 T, CC)
- **Reached from:** Feed S-08, Layers S-07, Positivity Feed S-09, a name search (`PROVISIONAL: C10`). Only under C6's "shown" option, and only if a shown tag leads to a profile, a person tag on S-17 (still open, OQ-20). **Leads to:** Walking a path S-06

**Rings: one ring per finished reveal, under both B4 settings.** B4's "per year with the app" option shows only on the owner's own profile S-05; here every viewer sees one ring per finished reveal, so the join year never shows (decided 2026-10-31, Spec §20 WW, Spec:330; Spec §20 TT, Spec:324). A public viewer may infer from a ring that a reveal is finished; that is allowed, but no ring carries a "finished" label (Spec §20 ZZ). **To a public viewer, rings come from a count only**: one reader returns the number of finished reveals for this profile, "and nothing else, no dates" (decided 2026-10-31, Spec §20 CCC, Spec:336). So no ring carries a date, a year or anything tied to one journey for a public viewer, and a public viewer's rings differ from one another in nothing the count does not give. The activity graph follows B5. Under B5's default the graph is **never shown here** (owner only); under the option it is built only from the photos this viewer can see, so no private photo's capture time shows (Spec:145), and it is **no finer than one day**: this viewer is not the owner, so it may place a photo on its capture date, never at a time of day (decided 2026-10-30, Spec §20 GG; Rubric R-154).

The table follows the state of the **profile owner's** journeys.

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed | The name in the circle (`PROVISIONAL: C7`), and no rings: with no finished reveal there is none, under either B4 setting (Spec §20 WW); for a public viewer the count is zero (Spec §20 CCC) | "no comparison between users" (Spec:185). A profile picture (Spec §20 YY). Rings per year with the app, or anything else that gives the join date (Spec §20 TT, WW) |
| `sealed` | That a journey exists, and nothing else: "Others may know only that one exists" (Spec:279) | Type, dates, counts, thumbnails, the year's activity: "Others see only `has_journey_underway(user)`" (Proposal:84); "including its existence in detail" (Spec:246). A partial, growing or dated ring or arc for the sealed year (Rubric R-012). A highlight, open or not (`PROVISIONAL: B6`) |
| `unlock-day`, `reveal-open` | The way into the journey, its photos readable by visibility (Spec:149): from unlock under B2's default, only once finished under the option. To a network viewer, under either option, the journey's type and dates from unlock, and chapter and feeling tags once set (Spec §20 T, X). The activity graph by B5 | Private photos. An activity graph that includes private photos' capture times (Spec:145; `PROVISIONAL: B5`). An activity graph finer than one day (Spec §20 GG; Rubric R-154). **Type, dates, chapter or feeling tags to a public viewer** (Spec §20 T, CC; Rubric R-152) |
| `reveal-finished` | To a network viewer, this journey's ring, under either B4 setting (Spec §20 WW). To a public viewer, one more ring from the count of finished reveals, with no date and nothing that ties it to this journey (Spec §20 CCC). The journey by locked visibility. Type, dates, chapter and feeling tags to a network viewer only (Spec §20 T) | As above. A ring presented as an achievement (Spec:185; Rubric R-102). **To a public viewer, a date, year or journey label on any ring** (Spec §20 CCC, T) |
| `later-years` | Rings: for a public viewer, from the count only (Spec §20 CCC). The overview stack for network viewers | As above |

On every state, never: the viewer's ring on this person's map, or this person's map at all (Spec:164, Spec:235). Who else is tagged in this person's journeys, or how often anyone appears (Rubric R-139). Extra access for the inner ring (Spec:150, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). Follower or view counts (Proposal:181). Anything that "signals how the person looks or how well they are doing" (Spec:29). **To a public viewer, any journey's type, commit or unlock date, chapter or feeling tags** (Spec §20 T, CC; Rubric R-152). **Whether any photo was taken in a highlight, or that a highlight happened, also after unlock** (Spec §20 DD; `PROVISIONAL: B24`; Rubric R-151). **Any photo's capture time of day: this viewer reads the capture date only** (decided 2026-10-30, Spec §20 GG; Rubric R-154). **When any note was written, not even the date** (Spec §20 LL). **This person's join date**, or rings per year with the app, which would give it (Spec §20 TT, WW). **To a public viewer, whether a reveal is finished, as a field, label or marker** (Spec §20 SS, ZZ). **To a public viewer, a date, year or journey label on any ring** (Spec §20 CCC). A profile picture (Spec §20 YY).

- **Reads:** User (name only; never `joined_at`, Spec §20 TT), Journey (type, dates, chapter and feeling tags for network viewers only, Spec §20 T; whether the reveal is finished for network viewers only, Spec §20 SS; rings are counted from finished reveals, Spec §20 WW; for a public viewer, only the one reader that returns the number of finished reveals and nothing else, Spec §20 CCC), Photo (`captured_at` after unlock as a date only, never the time, Spec §20 GG; visibility; never `highlight_id`, Spec §20 DD), Journey overview (Proposal §2.2)
- **Copy:** none weighted

### S-17 A photo, followed forward

- **Purpose:** one photo read across time: the original moment, the handwritten note on its back, then the reflections that came after, in order. The follow-up is the reflection stack (`PROVISIONAL: C13`).
- **Spec source:** Spec:195 (§15); Spec:15–17 (§1); Concept:162–168; Concept:569; Decisions B2, B12, C6, C13
- **Viewer:** owner, network, public, by the photo's visibility (Spec:143–147). The photo's journey's type, dates, chapter and feeling tags reach the owner and network only, even on a Public photo (Spec §20 T, CC)
- **Reached from:** Walking a path S-06, Positivity Feed S-09, Feed S-08 ("reflection left"). **Leads to:** Reflect S-14 (owner), Walking a path S-06

**People tags for readers: `PROVISIONAL: C6` (switchable).** The owner always sees their own tags, read-only after finish (Spec:276). A reader's own tag follows B12 (see S-06).
- **Default: hidden.** A reader sees no one else tagged on the photo.
- **Option: shown.** Tags appear on this photo, in place. No count, no grouping, no list across the journey (Rubric R-139). Whether a shown tag leads to that person's profile is not settled by the switch (OQ-20).

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not reachable | Anything (Spec:234) |
| `unlock-day`, `reveal-open` | The photo, its note if any, the slot 1 reflection if written. Readers: the owner; under B2's default, also the network while the photo is Network by default, and anyone once it is set Public; under B2's option, the owner only until finished | The photo to a non-owner once it is Private. A next, previous or swipe control that steps to another feed entry's photo: it would rebuild a photo feed one image at a time (Spec §20 Q; Rubric R-145) |
| `reveal-finished` | As above, with visibility locked | As above |
| `later-years` | The reflection stack grows by at most one per slot (Spec:97) | As above. For the owner, a marker that a new slot is open (Rubric R-095, R-096) |

On every state, never: a comment, reply or like (Spec:230, Proposal:181). A caption: "There's no caption" (Proposal:94). Edit or delete (Spec:266). Access through being tagged (Proposal:293). A count or list of everyone tagged across the journey (Rubric R-139). A link to another photo as its "follow-up": the data model has none (Proposal:86–99; `PROVISIONAL: C13`). **To a public reader, the journey's type, commit or unlock date, chapter or feeling tags, including on a photo reached from the Positivity Feed** (Spec §20 T, CC; Rubric R-152). **To anyone but the owner, whether this photo was taken in a highlight, also after unlock** (Spec §20 DD; `PROVISIONAL: B24`; Rubric R-151). **To anyone but the owner, this photo's capture time of day: a non-owner reads the capture date only; the owner reads the full time** (decided 2026-10-30, Spec §20 GG; Rubric R-154). **To anyone but the owner, when its note was written, not even the date** (decided 2026-10-30, Spec §20 LL, Spec:316). **To a public reader, whether the journey's reveal is finished, as a field, label or marker**, also on a photo reached from the Positivity Feed (Spec §20 SS, ZZ). The owner's join date (Spec §20 TT).

- **Reads:** Photo (`captured_at` in full for the owner, as a date only for anyone else, Spec §20 GG; never `highlight_id` for a non-owner, Spec §20 DD), Handwritten note (for a non-owner, never when it was written, not even the date, Spec §20 LL; Rubric R-154), Reflection, Tag (people tags by C6 and B12; chapter and feeling tags for owner and network only, Spec §20 T) (Proposal §2.2); `person_tag`, `photo_visibility` (Proposal:165–166)
- **Copy:** none weighted beyond S-14

### S-18 Tag people (reveal step)

- **Purpose:** the owner tags, by hand, the people in each photo: users, or a typed name.
- **Spec source:** Spec:85 (§7); Spec:127 (§10); Spec:267 (§20 7); Proposal:26 (D13); Proposal:165; Decisions B3, C5, C10
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Reveal S-04

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | Tagging at capture: "All tags are applied at reveal, never at capture" (Spec:133) |
| `unlock-day`, `reveal-open` | Per photo: tag a user, found by name search, or type a name for someone who is not a user (Spec:267; `PROVISIONAL: C10`). Each tag, once set, is fixed (Spec:286). Before it is saved, one line saying it can't be changed (`PROVISIONAL: C5`) | Suggested faces: "No face recognition, ever" (Spec:127), "No face detection anywhere in the pipeline" (Spec:231). Suggested people: tagging is "deliberate manual work" (Spec:127). Search results ordered by closeness, ring or popularity (Rubric R-071; Brief:44). A running count of tags per person, or of photos tagged so far (`PROVISIONAL: B8`, `C8`). A way to remove a set tag (Spec:286). Any hint of where the tagged person will sit on the owner's map, shown to that person (Spec:164) |
| `reveal-finished`, `later-years · finished` | Tags, read-only (Spec:276) | Any change |
| `later-years · never finished` | As `reveal-open`: each tag can still be set once, and the reveal finished later (`PROVISIONAL: B3`) | As `reveal-open` |

- **Reads:** Photo, User (name only, for the search; never another user's `joined_at`, Spec §20 TT), Tag (Proposal §2.2); `person_tag` (Proposal:165)
- **Copy:** that this is deliberate, manual work `[copy: copywriter]`; the one-line "this can't be changed" `[copy: copywriter]`

### S-19 Chapter and feeling tags (reveal step)

- **Purpose:** the owner applies one chapter from the fixed catalogue and any free-text feeling tags.
- **Spec source:** Spec:86 (§7); Spec:129–135 (§10); Proposal:137–143; Concept:469–529; Decisions B3, B17, B18, C5
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Reveal S-04

**Two places the docs disagree, each with a provisional default (Rubric G-14):** Spec:131 writes feeling tags "inside a category", while Proposal:141 stores them on the journey as free text with no category (OQ-37; `PROVISIONAL: B17` follows Proposal:141). Spec:131 also says "Popular ones surface over time", while Spec:202 says the Positivity Feed is "never by popularity" (OQ-38; `PROVISIONAL: B18`: tags never surface by popularity, no suggestions, no counts).

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | |
| `unlock-day`, `reveal-open` | One chapter, from fixed categories under ME → ME, ME → YOU, ME → IT (Spec:129). Feeling tags as free text on the journey, with no category (`PROVISIONAL: B17`; Proposal:141). Each set once (Spec:286), with one line saying it can't be changed before it is saved (`PROVISIONAL: C5`). Neither is required to finish (`PROVISIONAL: C5`) | A second chapter: "One per journey" (Spec:129). A way to change a set tag. **Suggested, popular or trending feeling tags, or how many people use a tag**: tags never surface by popularity (`PROVISIONAL: B18`), and no count is ever shown (Brief:42) |
| `reveal-finished`, `later-years · finished` | The tags, read-only | Any change (Spec:276) |
| `later-years · never finished` | None set yet unless the owner set them, which took effect when made. They can still be set, once each (`PROVISIONAL: B3`; Spec:269 says "There's no chapter, no tags", Rubric G-11) | |

- **Reads:** Journey, Tag (Proposal §2.2); `chapter` catalogue (Proposal:167)
- **Copy:** the tone rule "even through hard chapters it stays positive and hopeful" (Spec:135) `[copy: copywriter]`

### S-20 Visibility (reveal step)

- **Purpose:** the owner sets, per photo, who can read it: Private, Network or Public.
- **Spec source:** Spec:139–152 (§11); Spec:276 (§20 F); Proposal:25 (D12); Proposal:166; Decisions B1, B3, B14, C5
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Reveal S-04

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | A visibility choice at capture: "chosen at publish time, not at capture" (Spec:141), where "publish" means the reveal is finished (`PROVISIONAL: B1`) |
| `unlock-day`, `reveal-open` | Per photo: Private, Network, Public. Network until the owner chooses (Spec:151). Each set once (Spec:286), taking effect when made (`PROVISIONAL: B3`), with one line saying it can't be changed before it is saved (`PROVISIONAL: C5`). Public means signed-in users (`PROVISIONAL: B14`) | A "close friends" level: they "see nothing beyond the rest of the network" (Spec:150). A way to change a set choice. A count of photos set or still unset (`PROVISIONAL: B8`) |
| `reveal-finished`, `later-years · finished` | Visibility, read-only (Spec:276) | Any change |
| `later-years · never finished` | Every photo Network unless a choice was already made (Spec:269 with `PROVISIONAL: B3`). Each unmade choice can still be made once (`PROVISIONAL: B3`) | A way to change a set choice |

- **Reads:** Photo (Proposal §2.2); `photo_visibility` (Proposal:166)
- **Copy:** "Public means readable, not commentable" (Spec:152) `[copy: copywriter]`; that each choice is final (`PROVISIONAL: C5`) `[copy: copywriter]`

### S-21 Finish the reveal

- **Purpose:** the owner ends the reveal. Choices lock, the map is recomputed, and "path crossed" and "journey launched" go out. Under B4's default the owner's circle on S-05 also gains this journey's ring; under the per-year option it does not (`PROVISIONAL: B4`). On S-16, as others see it, the circle gains this journey's ring under either setting (Spec §20 WW).
- **Spec source:** Spec:276 (§20 F); Spec:162 (§12); Spec:280 (§20 J); Proposal:25 (D12); Proposal:65; Proposal:152–160; Proposal:164; Decisions B3, B4, C5
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Profile (own) S-05

| State | Holds | Must never show |
|---|---|---|
| `unlock-day`, `reveal-open` | The act of finishing ("Insert-only, only after unlock", Proposal:164). Nothing is required first (`PROVISIONAL: C5`). Before it is saved, one line saying it can't be changed (`PROVISIONAL: C5`) | A requirement to write an overview (Spec:285) or reflections (Spec:102). A reminder to finish (Spec:242). A summary of what is done or left, or any completion meter (`PROVISIONAL: B8`; Rubric R-099). The ring presented as a reward for finishing, or a celebration (Spec:185; Rubric R-102) |
| `reveal-finished`, `later-years · finished` | Done. It cannot happen twice (Proposal:164) | An undo |
| `sealed` | Not available: nothing is readable yet (Spec:234) | |
| `later-years · never finished` | Available: the reveal can be finished at any later time (`PROVISIONAL: B3`). Finishing then does what it does at any finish (Proposal:152–160) | As `reveal-open` |

- **Reads:** Journey, Tag, Layer (Proposal §2.2); `journey_reveal`, `announcement` (Proposal:164, 168)
- **Copy:** the finish, the weightiest act after Commit `[copy: copywriter]`

---

## Prototype only: not part of the product

Nothing in this section is part of the product. It is never shown as a product feature, it sits outside the product's own screens and navigation, and no product screen links to it. Only the panel, a separate role, moves time or flips a switch; the acting viewer never can, by any route (decided 2026-10-30, Spec §20 EE, Spec:309; Rubric R-153). It exists so the demoer can see a year pass and compare the switchable defaults (Spec:346–356, §21; Decisions "Provisional defaults in force": "a toggle in the prototype options panel, next to the time control").

### T-01 Time control

- **Purpose:** move the one simulated clock forward so the reveal, the reflection stacks, the rings and the paths crossing can be seen.
- **Spec source:** Spec:346–356 (§21); Spec:298 (§20 V); Spec:309 (§20 EE); Proposal:192–201 (§3.1); Proposal:383–396 (§3.8); Plan:92; Decisions B20, B21, B22, B26, C16, C17
- **Viewer:** demoer only, through the panel role. The jumps, "jump to the next unlock" and reset are the panel's alone: the acting viewer chosen in T-02 can never move the clock, from a product screen or any other route (decided 2026-10-30, Spec §20 EE; Rubric R-153)
- **Holds:** +1 minute, +1 hour (`PROVISIONAL: B20`), +1 day, +1 month, +1 year, +5 years, jump to the next unlock, reset to baseline (Proposal:195). Baseline is 2026-10-25 00:00:00 UTC (`PROVISIONAL: B21`). Reset also puts every option switch in T-02 back to its default (`PROVISIONAL: B22`). **The clock runs at real speed from the last jump**, so a note window or a highlight closes on its own while the demoer watches (decided 2026-10-30, Spec §20 V; Proposal:169, 195). On each jump: unlocks (derived), scripted actions, layers, announcements, in that order (Proposal:196–200); a scripted action the running clock has already passed is applied at the next jump (`PROVISIONAL: B26`). The simulated date, as a plain date (`PROVISIONAL: C16`). "Jump to the next unlock" is still built while Decisions C17 is open (OQ-41)
- **Must never show:** any control that moves the clock inside a product screen, or any way for the acting viewer to move it (Spec §20 EE; Rubric R-153). A backward jump: "Forward only. To look at an earlier moment, reset and jump again" (Proposal:195; Rubric R-117). A timer, time left or countdown on a note window or a highlight, even though the clock now runs: the running clock closes them, it never displays how long is left (Rubric R-140). **Anything the seal hides: the panel applies the seal like every other path** (Rubric R-014). So it never reports what a jump applied inside a sealed journey: no "Second Wind captured 3 photos", no counts, no capture times, no highlight (Spec:75; Rubric R-008). "Jump to the next unlock" is labelled without whose journey it is or when it falls (Rubric R-008). No countdown to any unlock (Rubric R-013). No layer row of anyone but the viewer chosen in T-02 (Spec:164; Rubric R-139)
- **Reads:** `sim_clock` (Proposal:169)

This table is for the reader of this inventory. The panel shows none of it.

| Simulated point | What the product shows that it could not before | Source |
|---|---|---|
| Baseline 2026-10-25 | Four sealed journeys (S-03, S-16 "exists only"). Long Way Round #4 unlocked, never revealed. First Light with no journey and an empty map | Proposal:201–211, Proposal:246, Proposal:291 |
| 2027-01-01 | Steady Lantern #6 unlocks: `unlock-day`. "The reveal is left for whoever is demoing" | Proposal:201, Proposal:389 |
| 2027-04-25 | Second Wind finishes #6: "path crossed", "journey launched", a reflection and an overview | Proposal:390 |
| 2027-06-20 | Open Hands finishes #4, tagging Lantern once and First Light once (she has no journey: the D14 test, Proposal §3.8 amended 2026-10-30) | Proposal:391 |
| +5 years | Long Way Round #4 still Network by default. The world goes quiet | Proposal:392–396 |

### T-02 Prototype options panel

- **Purpose:** let the demoer compare the switchable provisional defaults, choose which fixture user to view the app as, and see the simulated date. Not part of the product.
- **Spec source:** `CLAUDE.md` rule zero, item 3; Spec:303 (§20 Z); Spec:309 (§20 EE); Decisions "Provisional defaults in force" (B2, B4, B5, B11, B12, C6, C11, C16, B22, B23); Proposal:170 (`prototype_option`); Proposal:205–211 (the fixture users); Proposal:312–320 (the access matrix the viewer switcher tests)
- **Viewer:** demoer only, through the panel role. Picking a fixture user here sets who the product screens are seen as; that acting viewer can never flip a switch or move the clock (decided 2026-10-30, Spec §20 EE; Rubric R-153)
- **Reached from:** T-01, beside it. Never from a product screen

| Holds | Options (**default** first) | Screens it changes |
|---|---|---|
| Switch B2: reading a journey before its reveal is finished | **from unlock** / only after reveal finished | S-06, S-08, S-15, S-16, S-17 |
| Switch B4: what adds a ring | **per finished reveal** / per year with the app | S-05, S-21. Not S-16: others always see one ring per finished reveal (Spec §20 WW) |
| Switch B5: who sees the activity graph | **owner only** / built from the photos the viewer can see | S-16 (S-05 is always the owner) |
| Switch B11: "path crossed" | **named** / unnamed | S-08 |
| Switch B12: where the reader appears | **shown** / hidden | S-06, S-17 |
| Switch C6: people tags for readers | **hidden** / shown | S-17, S-06, S-16 |
| Viewer switcher: the five fixture users, by name: Steady Lantern, Second Wind, Open Hands, Long Way Round, First Light (`PROVISIONAL: C16`, `C11`) | Picking one shows the whole app as that user | Every screen |
| The simulated date, as a plain date (`PROVISIONAL: C16`) | | |

Each switch is labelled as provisional with its Decisions ID, so no one reads a default as decided (`CLAUDE.md`, rule zero).

The six switches live in the database, in the one `prototype_option` row, and change only through `set_option()` (decided 2026-10-30, Spec §20 Z; Proposal:170), which only the panel role can call, never the acting viewer (decided 2026-10-30, Spec §20 EE; Rubric R-153). They are **one global setting, not per viewer**: picking another fixture user in the viewer switcher leaves every switch as it is (`PROVISIONAL: B23`). **Reset to baseline in T-01 puts every switch back to its default** (`PROVISIONAL: B22`).

- **Must never show:** the panel or any switch inside a product screen. Any way for the acting viewer to flip a switch or move the clock (Spec §20 EE; Rubric R-153). A per-viewer copy of a switch (`PROVISIONAL: B23`). Anything beyond each fixture user's name in the viewer switcher: not who has a sealed journey, no type or dates, no rings, no counts, no "who is on whose map" (Rubric R-008, R-014, R-139). A relative date or countdown beside the simulated date (Rubric R-013). A switch for any default not marked switchable in Decisions
- **Reads:** `sim_clock` (Proposal:169); `prototype_option`, written only through `set_option()` (Proposal:170; Spec §20 Z); the fixture users (Proposal:205–211)

---

## Not in this build

Listed only so no screen is built for them.

| Item | Source |
|---|---|
| The album phase: ordering, the physical album, print-shop ritual. Spec §7 step 6 and §17 now call it "the album phase", the business stage, not a build phase | Spec:89, Spec:213–220, Plan:228, Decisions A11 |
| Export and data ownership | Spec:341 (§20 "Still open — can wait", item 1) |
| Age gating and parental consent | Spec:342 (§20 "Still open — can wait", item 2) |
| Real authentication and real photo storage | Plan:228 |
| Sign up and choosing a name, in the prototype only. S-10 and S-11 stay in the product inventory | Decisions C11 (`PROVISIONAL: C11`) |

---

## Open questions

Each one is a place the sources are silent or disagree. The questions are kept as first raised; nothing is deleted. Each now ends with its Decisions ID and status:
- **A** items: text corrections the user approved on 2026-10-27, being applied. These are decisions, not defaults.
- **B** and **C** items: a provisional default in force. Not a decision. Switchable ones are marked.
- **C17, C18**: listed in Decisions with an ID but no default. Still open.
- **No ID**: still open, with no default. Nothing on the screens above depends on picking a side.

Where two docs disagree, both lines are cited and neither is picked unless Decisions gives a default.

**Contradictions between documents**

1. **Reflection timing in the example.** Spec:104–111 and Concept:203–210 date reflections on the photo's own anniversary (7 Jan), and Concept:200 says "on the photo's anniversary". Spec:101 and Spec:274 (§20 D), Concept:852 and Proposal:22 (D9) say all photos of a journey move to their next slot together, on the journey's unlock anniversary. §20 wins by `CLAUDE.md`. Should the example be corrected? Affects S-14, S-17.
   → Decisions A1: correction approved 2026-10-27, being applied (§20 D stands).
2. **"Written a year or more after the moment."** Spec:98 conflicts with Spec:274 (§20 D): a photo taken in month 12 gets its slot 1 reflection weeks after the moment. Affects S-14.
   → Decisions A2: correction approved 2026-10-27, being applied.
3. **"Publish" names no real step.** Spec:141 ("chosen at publish time"), Concept:365–367, Concept:424, Concept:440 ("They published their Journey."). The decided steps are "reveal finished" and "journey launched" (Spec:276, Spec:280). Does "publish" mean "the reveal is finished"? Also open in `Learnings/index.md:54`. Affects S-20, S-08 copy.
   → Decisions B1, provisional: "publish" means "reveal finished". Not switchable.
4. **Close friends.** Concept:807 says "close friends get everything"; Concept:381–383 says close friends can be granted access to both. Spec:150, Spec:278 (§20 H) and Concept:864 say they see nothing extra. §20 wins. Should Concept:807 be marked superseded? Affects S-07, S-16, S-20.
   → Decisions A3: correction approved 2026-10-27, being applied (§20 H stands).
5. **When layers are computed.** Concept:401 says "Calculated when Journeys are uploaded and ready to reflect on"; Concept:828–832 leaves the upload fork open. Spec:91, Spec:162 and Proposal:152 say when the reveal is finished. Also open in `Learnings/index.md:53`. Affects S-07.
   → Decisions A4 and A9: corrections approved 2026-10-27, being applied.
6. **What a ring counts.** Spec:185 says "One ring per year with the app" and Concept:687 says "Each year with the app adds a ring". Proposal:65 says "one ring per journey whose reveal is finished". They differ for First Light (joined 2026-10-01, no journey), for Long Way Round #4 (never finished), and for any gap between journeys. Affects S-05, S-16.
   → Decisions B4, provisional: one ring per finished reveal (**switchable**: per finished reveal / per year with the app). Also affects S-21. Decided 2026-10-31 (Spec §20 WW, Spec:330): the per-year option shows only on the user's own profile S-05; others, on S-16, see one ring per finished reveal under either setting, so TT holds.
7. **When the activity line is twisted in, and when the graph appears.** Spec:186 says "at the end of the journey", Spec:187 says "only after the year unlocks", Concept:706 says "At the end of the Journey". Proposal:65 adds the ring at reveal finished. In `unlock-day` and `reveal-open`, is there a graph without a ring? And what does the activity line record besides `captured_at` (Proposal:50; Concept:704: "the app records activity")? Affects S-05, S-16.
   → Decisions B5, provisional: the line twists in at reveal finished; the graph is owner-only (**switchable** for the graph: owner only / built from the photos the viewer can see). What the line records besides `captured_at` is not covered by B5: **still open, no ID**.
8. **Spec journey states.** Spec:14 lists "committed / sealed / unlocked". Proposal:76–84 collapses committed into sealed and splits unlocked into revealing and revealed. Spec §1 was not updated. Confirm the time states above follow the Proposal.
   → Decisions A5: correction approved 2026-10-27, being applied. Spec:14 now follows the Proposal.
9. **Who sees a journey before its reveal is finished.** Concept:362 says sharing is "Only possible after unlock, and as a finished story or album". Spec:151, Spec:269 and Proposal:318 (Open Hands reads Long Way Round #4, never revealed) let the network read every photo from the moment of unlock, before the owner has set anything Private. Is that intended? Affects S-06, S-16, S-17 at `unlock-day` and `reveal-open`.
   → Decisions B2, provisional: the network can read from unlock (**switchable**: from unlock / only after reveal finished). Under the option, Public photos wait too (decided 2026-10-30, Spec §20 R). Also affects S-08, S-15.
10. **Engagement in the sealed year.** Spec:76: "other people's unlocked journeys, not their own". Spec:274 (§20 D) keeps reflection slots open on the owner's earlier journeys during a new sealed year (Proposal:299: lantern-1 slot 5 on 2026-02-20, while #6 is sealed; Proposal:246: Long Way Round reflects on 2026-09-10). Does the sealed-year screen point to the owner's own earlier journeys? Affects S-03.
    → Decisions C3, provisional: no; open slots are reached from the owner's profile. Not switchable.
11. **Positivity Feed and "No photo feed".** Brief:45 says "No photo feed: The feed carries announcements only, never images"; Spec:171 says "No photographs in the stream". Proposal:324 fills the Positivity Feed with "Public photos (and their reflections)". Spec:204 speaks only of reading reflections. Does the Positivity Feed show the photograph? Affects S-09.
    → Decided 2026-10-30 (Spec §20 Q): reflection text only, the photo shown when one entry is opened. Not switchable.
12. **"Journeys set to public."** Spec:203 and Concept:375 say the Positivity Feed is fed "only by journeys set to public". Spec:141 and Concept:379 set visibility per photo, not per journey. Affects S-09.
    → Decisions B9(b), provisional: per photo. Not switchable.
13. **The type arithmetic.** Spec:47, Concept:99 and Concept:128 say the three types sit on the old 24–48 range's "ceiling, middle and floor". 12 is outside that range, and the middle of 24–48 is 36. Concept:799 still says "Frame range 24–48". Affects S-01 copy.
    → Decisions A7: correction approved 2026-10-27, being applied.
14. **Overview timing.** Spec:118 says "Written at reveal". Spec:275 (§20 E) and Proposal:124 give it the same yearly windows as reflections. Can the slot 1 overview be written after the reveal is finished? Is it readable by the network before then (Proposal:126 sets no gate)? Affects S-15.
    → Decisions A6 (the "written at reveal" text, approved 2026-10-27, being applied) and B13, provisional: slot 1 can be written after finish, within the slot; network only. Not switchable. Network reading before finish follows B2 (strictest reading). Decided 2026-10-30 (Spec §20 HH, Spec:312): under B2's option the network reads the overview only once the reveal is finished.

**Where the spec is silent**

15. **Unlock day.** How does the owner learn that the journey has unlocked, when there are "No re-engagement notifications of any kind" (Spec:236) and the app must never "Remind a user … to return" (Spec:242)? Concept:156 contrasts the reveal with "an unlock notification with nothing to do". Where does "Your Journey is ready" (Plan:79, Concept:740) appear? Is `unlock-day` a distinct state at all, given that the data model has none (Proposal:81)? Affects S-04, S-03.
    → Decisions C1, provisional: on next open, never as a notification. Not switchable. With C12 it appears on Profile (own) S-05; that combination is this inventory's reading of the two defaults and is for the user to confirm.
16. **Does the reveal ever close?** No deadline is stated (Proposal:164: "only after unlock"; Spec:269). Proposal:392 says Long Way Round's #4 "stays unfinished" at +5 years, but not whether finishing is still possible. Can visibility, tags and chapter still be set in `later-years · never finished`? Affects S-04, S-18–S-21.
    → Decisions B3, provisional: each choice takes effect when made; a reveal can be finished at any later time. Not switchable.
17. **What must be done before finishing.** Overviews are optional (Spec:285) and reflections are optional (Spec:102). Is a chapter required ("One per journey", Spec:129)? Are people tags or a visibility choice required? Affects S-21, S-19.
    → Decisions C5, provisional: nothing is required. Not switchable.
18. **Confirmation of a set-once choice.** Every reveal choice is final the moment it is made (Spec:286, Proposal:408 R5). Is the owner warned or asked to confirm, per choice and at finish? Affects S-18, S-19, S-20, S-21.
    → Decisions C5, provisional: a one-line "this can't be changed" before each set-once choice is saved. Not switchable.
19. **"Where you appear" and layer invisibility.** Spec:196 and Concept:570 say the reader sees where they appear in someone's journey. Spec:164 and Spec:235 say no one learns their layer. Showing a reader the photos they appear in lets them count them and infer their ring (5+ tight, Spec:161). Only photos they can already see would show (Proposal:293). How is this shown without revealing the ring? Affects S-06.
    → Decisions B12, provisional: shown, in journey order, with no total and no grouping (**switchable**: shown / hidden). Also affects S-17.
20. **People tags shown to readers.** Can a reader see who else is tagged in a photo, and can a tag lead to that person's profile? Not specified. Affects S-17, S-16.
    → Decisions C6, provisional: not shown to readers (**switchable**: hidden / shown). Under "shown", whether a tag leads to that person's profile is not covered by the switch: **still open, no ID**.
21. **"Path crossed" reaches the crossed person.** It goes to the owner's network (Spec:283). The crossed user is on the owner's map, so they receive it and learn they are on it. Does the announcement name them, and is that consistent with Spec:164? Spec:175 says "with a friend". Affects S-08.
    → Decisions B11, provisional: names both people, reaches the owner's network, never says which ring (**switchable**: named / unnamed).
22. **"Reflection left" on a public photo reaches everyone.** It goes to "people who can see that photo" (Spec:280), and a public photo is visible to anyone (Spec:147). So every user, First Light included, would receive it. Is that intended, given Spec:30 names the Positivity Feed and profiles as the day-one experience? Affects S-08.
    → Decisions B10, provisional: only the owner's network members who can see the photo, even when public. Not switchable. (Citation corrected 2026-10-27: was Spec:282, which is §20 L.) Decided 2026-10-31 (Spec §20 UU, Spec:325): the owner also sees their own "reflection left", but not their own "journey launched" or "path crossed". UU holds over B10 for the owner only (r6 N2).
23. **Empty states other than the sealed year.** What do an empty map (Proposal:291), an empty Feed and an empty profile circle hold? Not specified. Affects S-07, S-08, S-05.
    → Decisions C9, provisional: a plain statement; copy in Phase 2. Not switchable.
24. **The note step after leaving it.** A note "can be added up to 15 minutes after capture" (Spec:281). The photo is unreadable at once, even to the owner (Spec:234, Proposal:48). How does the user get back to that photo inside the 15 minutes? And can the page be re-photographed before it is saved ("written once", Spec:16; "No retakes", Spec:55)? Affects S-12, S-03.
    → Decisions C4, provisional: offered only inside the capture flow, straight after the photo, up to 15 minutes; leaving capture ends it, so there is no way back from S-03; the page is taken live, once, with no re-shoot. Not switchable. Two residual points C4 does not state: whether skipping also ends it (this inventory takes the strictest reading, yes), and what the user sees if still on the step at 15 minutes (no timer either way, R-140). **Residual: still open, no ID.**
25. **A refused capture.** What does the user see when there is no frame (Proposal:97–99)? Is the camera offered at all? Spec:243 bans a quota count "in a way that reads as a target", which leaves room for some other kind of count. Proposal:49 returns no number at all. Affects S-02.
    → Decisions B7, provisional: frames left are never shown; a refused capture says so with no number. Not switchable. The camera is offered the same either way (Rubric R-138, provisional on this question).
26. **An open highlight.** May the owner see that a highlight is open and when it ends? Proposal:49 forbids returning highlights left. The window itself is not addressed. Affects S-02, S-03, S-13.
    → Decisions B6: the owner sees only "a highlight is open", with no end time and no countdown (decided 2026-10-30, Spec §20 S); others learn nothing (provisional). Not switchable. This inventory shows it on S-03 and S-13, not on S-02 (strictest reading of where).
27. **The unlock date shown relative to today.** The owner may see the unlock date (Proposal:84). Is "in 64 days" a counter under Spec:233? Affects S-03.
    → Decisions C2, provisional: a plain date, never relative. Not switchable. (Rubric R-013 already bans the countdown; the audit, finding 2, noted this question should not have been framed as open.)
28. **Who sees the activity graph.** It is built from `captured_at` (Proposal:50), including private photos. Shown to network or public, it would reveal when private photos were taken (Spec:145). Is it owner-only, or built only from photos the viewer can see? Affects S-16.
    → Decisions B5, provisional: owner only (**switchable**: owner only / built from the photos the viewer can see).
29. **The "follow-up".** Spec:195: "the original moment, then the follow-up". Concept:569: "the follow-up photo or memory that came later". The data model has no link between photos (Proposal:86–99). Is the follow-up only the reflection stack? Affects S-17.
    → Decisions C13, provisional: the follow-up is the reflection stack. Not switchable.
30. **Positivity Feed rules.** (a) Which tags qualify: only the drafted list (Spec:207), or free text too (Proposal:227 "slow is still forward"; Proposal:364, §3.7: "What the exclusions test: Steady Lantern #5's free-text tag is not on the list")? (Citation corrected 2026-10-30: was Proposal:330 "tests a tag that isn't on the drafted list", a sentence §3.7 no longer has.) (b) Can it filter by chapter, as Spec:205, Concept:467 and Concept:614 ("filterable by phase") suggest, when Spec:202 names only endurance and gratitude tags? (c) In what order, since "never by popularity" (Spec:202) names no other? (d) Does a photo set Public enter before its reveal is finished? Affects S-09.
    → Decisions B9 (c), (d), (e), (f), provisional: drafted list only; no chapter filter (Spec §20 Y, decided 2026-10-30); newest first; only after reveal finished. Not switchable. (The letters here differ from Decisions': this question's (a)–(d) are its (c)–(f).) This question's (c), the order, decided 2026-10-31 (Spec §20 BBB, Spec:335): newest reflection first, by the reflection's written time. `PROVISIONAL: B9e` is retired on S-09.
31. **Profile picture.** It is a User property (Spec:13), but "Nothing on a profile signals how the person looks" (Spec:29; Brief:113). What may it show, when is it set, and can it change? Only the name is immutable (Proposal:45, Proposal:61). Affects S-11, S-05, S-16.
    → Decisions C7, provisional: no profile picture anywhere; the name sits in the circle; announcements carry no image. Not switchable. Also affects S-07, S-08. Decided 2026-10-31 (Spec §20 YY, Spec:332): no profile picture; the field stays unused. Whether YY also settles C7's other two parts is OQ-49.
32. **Invitation and onboarding.** Invitation is "the main arrival path" (Spec:28), but no invitation step is described. No onboarding beyond sign-up is described either. Affects S-10.
    → Decisions C11, provisional: no sign-up or onboarding in the prototype; fixture users are picked from the panel. Not switchable. How invitation works in the product is not covered by the default.
33. **Finding a user.** Tagging any user (Spec:163, Spec:267) and visiting profiles on day one (Spec:30) both need a way to find a person. No search or directory is described. Affects S-18, S-16.
    → Decisions C10, provisional: name search, plus typed names for non-users. Not switchable. Where the search sits for visiting profiles (its own screen, or part of another) and how matches are ordered are not covered by C10: **still open, no ID** (any order by ring, closeness or popularity is banned, Rubric R-071).
34. **App entry.** Which screen opens the app in each time state? Only the new user's day one is stated (Spec:30). Concept:438–444 names Feed, Layers and Profile as the architecture but no entry point. Affects S-01, S-03, S-05, S-07, S-08, S-09.
    → Decisions C12, provisional: the app opens on Profile (own) S-05, in every state. Not switchable.
35. **The prototype viewer.** Real authentication is out of this build (Plan:228), but the access matrix needs the demo to be seen as each fixture user (Proposal:312–320). How the demoer switches viewer, and whether T-01 shows the simulated date, are not specified. Affects S-10, T-01.
    → Decisions C16, provisional: a viewer switcher of fixture users in the prototype panel, and the simulated date shown. Not switchable. See T-02.
36. **The map's detail.** Does the owner's map show past years' rings or drift, or the number of shared photos (Proposal:150: "The owner's current map is the latest entry per member"; Concept:407 on reflecting on drift)? A count may fall under "No streaks, counters" (Brief:42). Affects S-07.
    → Decisions C8, provisional: current rings only; no counts, no history, no drift. Not switchable.

**Raised by the 2026-10-27 audit**

37. **Feeling tags and categories.** Spec:131 says feeling tags are written "inside a category". Proposal:141 stores them as (journey, free text), with no category. Which shape does the tag step offer? Affects S-19. (Audit finding 14; Rubric G-14.)
    → Decisions B17, provisional: free text on the journey, no category. Not switchable.
38. **"Popular ones surface."** Spec:131 says popular feeling tags "surface over time and the best get promoted into official categories". Spec:202 says the Positivity Feed is "never by popularity". Does any screen surface or suggest popular tags, and by what measure? Affects S-19, S-09. (Audit finding 14; Rubric G-14.)
    → Decisions B18, provisional: tags never surface by popularity; no suggestions, no counts. Not switchable.
39. **What the owner sees of a sealed journey besides the unlock date.** Spec:74 says nothing in a sealed journey is visible, "not to the user". Proposal:84 lets the owner see its type, commit date and unlock date. Do the type and commit date show on S-03, S-05 and S-06? Affects S-03, S-05, S-06. (Audit finding 2; Rubric G-17.)
    → Decisions B19, provisional: the owner sees type, commit date and unlock date, nothing else (C2 sets the unlock date's form). Not switchable. Exception: "a highlight is open", S-03 element 7 (decided 2026-10-30, Spec §20 S).
40. **The announcement feed's order.** No source states it (Rubric Question 1). Affects S-08. (Audit finding 11.)
    → Decisions C14, provisional: newest first. Not switchable.
41. **"Jump to the next unlock" and another user's date.** T-01's jump plus the simulated date it shows (C16) tells the demoer when another user's journey unlocks (Rubric R-014, R-008). Is the demoer exempt as a prototype tool, or does the jump go to the chosen viewer's own next unlock? Affects T-01. (Re-audit N8.)
    → **Decisions C17: still open, no default.** Raised for the user. T-01 still holds the jump (Proposal:195); panel acceptance waits on C17.
42. **How long "Your Journey is ready" stays.** Decisions C1 says it appears on the owner's "next open". Once only, or on every open until the reveal is finished? Shown on every open for a year it becomes a nudge (Rubric R-095). Affects S-05, S-03. (Re-audit N5.)
    → **Decisions C18: still open, no default.** Raised for the user.

**Raised by the 2026-10-30 round 4 audit** (`docs/reviews/2026-10-30-rules-phase-1-r4.md`)

43. **The simulated time of day in T-02.** Spec §20 V makes the clock run, and B20 adds +1 minute and +1 hour, but C16 shows only "the simulated date". Does the panel also show the time of day, and if so does it tick? A ticking display is banned on product screens (Rubric R-013); the panel is not a product screen, but no source says either way. Affects T-01, T-02.
    → **Still open, no ID.** T-01 and T-02 hold only what C16 states, the date; nothing is added until the user answers.
44. **Rings and journey order to a public viewer.** Spec §20 T keeps a journey's dates from public readers. S-16 shows a public viewer rings (B4) and S-06 shows journeys "in order" (Spec:193). Whether a ring or a journey's place on the path may carry a year or any date label for a public viewer is not stated. Affects S-16, S-06.
    → **Still open, no ID.** S-06 and S-16 add no date label for a public viewer, because a dated ring or path entry would show a journey's dates, which §20 T withholds. Whether an undated ring or path order is itself too much is for the user. Partly settled 2026-10-31: on S-16 rings are one per finished reveal for every viewer (Spec §20 WW), and a public viewer may infer from rings that a reveal is finished (Spec §20 ZZ, Spec:333). Neither ruling says whether a ring may carry a date label, so the date-label question stays open.
    → Rings settled 2026-10-31 (Spec §20 CCC, Spec:336): a public viewer's rings come from a count of finished reveals only, "and nothing else, no dates". No ring carries a date for a public viewer, and an undated ring drawn from the count is allowed. S-16 states this. **Still open, no ID, for S-06 only:** CCC speaks of rings on a profile, not of a journey's place on a path. S-06 still adds no date label for a public viewer (Spec §20 T); whether the path order itself is too much is for the user.
45. **Capture times and highlights.** Spec §20 DD keeps `highlight_id` owner-only, but a reader shown `captured_at` on many photos from one day can still infer a highlight (audit N8; Rubric R-151, residual risk). No screen here shows a photo's capture time to a non-owner except through B5's option graph. Whether any reader screen may show it is not stated. Affects S-06, S-16, S-17.
    → Decided 2026-10-30 (Spec §20 GG): readers see the capture date only, never the time; the owner sees the full time.

**Raised 2026-10-30, after Spec §20 GG** (`docs/reviews/2026-10-30-gate-1-r4.md` NB-22; `docs/reviews/2026-10-30-rules-phase-1-r5.md` V3)

46. **The order of photos within one day, for a non-owner.** Spec §20 GG (Spec:311) gives a non-owner the capture date, never the time. A path runs "in order, not as a grid" (Spec:193), and S-17 sits in that order. When several photos share a date, ordering them by capture time, or by anything that follows it such as sequential photo ids, would tell a non-owner the order the moments happened in, which GG may or may not count as "time". No source says how same-day photos are ordered for a non-owner. A second, smaller point: GG grants the capture date only; whether a non-owner may see the note's written **date** (which, near midnight, can differ from the capture date and so pin the time, Rubric R-154) is not stated either. Affects S-06, S-16, S-17.
    → Decided 2026-10-30: same-day photos for a non-owner carry no time order, and ids are not sequential across users (Spec §20 JJ); a non-owner never sees when a note was written, not even the date (Spec §20 LL).

**Raised 2026-10-31, after Spec §20 PP–ZZ** (`docs/reviews/2026-10-31-rules-phase-1-r6.md` V4; `docs/reviews/2026-10-31-gate-1-r5.md` CF-28)

47. **What the camera shows while the app strips again.** Spec §20 VV (Spec:326) and XX (Spec:331) say the guard-bug retry is silent and judged at the press instant, and PP (Spec:320) says the refusal never reaches the user. None of them says whether the camera waits during the second strip, or what it shows if it does. Any wait indicator must not read as a refusal, a timer or an invitation to press again (PP; Rubric R-140). Affects S-02, S-12.
    → **Still open, no ID.** S-02 states only what never shows. It adds no wait state.
    → Decided 2026-10-31 (Spec §20 DDD, Spec:337): the user sees nothing different. If stripping fails twice for one press, that press gives no photo and the bug is logged; no error, no "try again". S-02 holds no wait state and bans a wait indicator, and a new row covers the twice-failed press. What follows that press on screen is OQ-50.
48. **The stored capture time on a guard-bug retry: VV against XX.** Spec §20 VV (Spec:326) says "the stored time may be slightly later". Spec §20 XX (Spec:331), from the same date, says the retry is "judged and stamped at the original press instant". These read differently on what is stored. It matters on screen because the owner sees the full capture time after unlock (Spec §20 GG; S-05, S-06, S-17), and the note window runs from capture (Spec:281). XX looks like the later and narrower ruling, but neither line says it replaces the other. Affects S-02, S-12, S-17.
    → **Not picked. Raised for the user.** S-02 cites both. No screen shows anything that depends on the gap.
    → Decided 2026-10-31 (Spec §20 AAA, Spec:334): "The press instant wins." The retry is stored at the original press instant (XX), and VV's "the stored time may be slightly later" is retired. S-02 now says so.
49. **How much of C7 Spec §20 YY decides.** YY (Spec:332) says "No profile picture. The field stays unused, as Decisions-Needed C7". C7 also says "The profile shows the name in the circle" and "Announcements carry no image". Spec:171 already bans images in the feed. Whether YY also turns "the name in the circle" into a decision is not stated. Affects S-05, S-07, S-16.
    → **Not picked.** The profile-picture bans now cite Spec §20 YY. "The name in the circle" and "shown by name" keep `PROVISIONAL: C7`. Still open on 2026-10-31: AAA–DDD do not touch it.

**Raised 2026-10-31, after Spec §20 AAA–DDD**

50. **What follows a press whose stripping failed twice.** Spec §20 DDD (Spec:337) says "the user sees nothing different; that press gives no photo". After an accepted press the camera hands to the note step S-12 (`PROVISIONAL: C4`); after a refused one it shows the refusal. A twice-failed press is neither. If S-12 is offered, the user may write and photograph a note for a photo that does not exist. If it is not, the press looks different from an accepted one, and DDD says nothing different shows. Also not stated: whether that press used a frame or a highlight slot, which the user would learn later, and only by a capture being refused (`PROVISIONAL: B7`). Affects S-02, S-12.
    → Decided 2026-10-31 (Spec §20 GGG): back to the camera as after any press, no note offer, no frame used. A note image that fails twice is handled the same way on S-12 (Spec §20 HHH).

---

## Index of weighted moments `[copy: copywriter]`

The Commit moment and button (S-01). The capture refusal, with no number, and the no-retake line (S-02). The sealed state (S-03). "Your Journey is ready" on next open, and the reveal (S-04, S-05). The young circle and the empty circle (S-05). Finding yourself in someone's hard year (S-06). How the map is described, and the empty map (S-07). The three announcement lines and the empty feed (S-08). The Positivity Feed's purpose (S-09). The arrival (S-10). "A name from within" (S-11). The note offer and skip, and that the page is taken once (S-12). Starting a highlight, the plain "a highlight is open", and the refusal (S-13). A reflection is final (S-14). The overview prompt (S-15). Manual tagging (S-18). The tone of chapters (S-19). "Readable, not commentable" (S-20). The one-line "this can't be changed" (S-18–S-21). Finishing the reveal (S-21).

---

## Revision log

**2026-10-27, round 1 of 3.** Against `docs/reviews/2026-10-27-rules-screen-inventory.md`:

| Finding | What changed |
|---|---|
| 1 (violation): sealed screen showed a way back to the note step | Removed from S-03. `sealed · note window` is now identical to `sealed` on S-03, with the way back banned. The note step lives only in S-02 and S-12 (`PROVISIONAL: C4`). The time state now says it changes only S-02 and S-12 (Rubric R-010) |
| 2: unlock date open to a countdown | S-03 element 4 is a plain date (`PROVISIONAL: C2`). Countdown, relative date, timer and ticking display banned on S-03, S-05, S-06 and every screen (R-013). Spec:74 cited against Proposal:84 (OQ-39) |
| 3: no ban on a timer for the note or highlight window | Timer, time left, "ends in" and shrinking bar or ring banned on S-02, S-03, S-12, S-13 (R-140; `PROVISIONAL: B6`) |
| 4: room for a review or re-shoot of the note page | S-12 bans preview, review-before-save, re-shoot and gallery import of the page (R-005, R-020; `PROVISIONAL: C4`) |
| 5: controls may reveal availability | Capture and highlight controls are offered the same whatever is left; no hidden, greyed or relabelled state; no hint of when a frame returns (S-02, S-03, S-13; R-138; `PROVISIONAL: B7`) |
| 6: type card could carry the quota | S-03 element 2 is the type by name only; quota, cadence and allowance banned on S-03 and S-05 (R-098) |
| 7: profile could draw a filling ring | Partial, growing, dated or filling ring or arc for the sealed year banned on S-05, S-06, S-16 (R-012) |
| 8: rings tied to finishing, stated as settled | Both B4 options described on S-05, S-16, S-21; "the year becomes a ring" and "(the new ring)" removed; ring as reward or achievement banned (R-102) |
| 9: "which choices are set" invited a completion meter | S-04 now shows each made choice in place, read-only; checklist, ticks, "12 of 24", percentage and done-or-left summary banned (`PROVISIONAL: B8`; Spec:233 and Brief:42 both cited). Also on S-14, S-18, S-20, S-21 |
| 10: readers could total tags and read rings | B12 and C6 described with both options on S-06 and S-17; totals, grouping and "people in this journey" lists banned (R-139). S-16's route from a person tag now exists only under C6's "shown" option, and is still open (OQ-20) |
| 11: feed lacked unread-marker ban; order not raised | S-08 bans unread dots, badges, "new" markers, "since your last visit" dividers and entry-point or app-icon badges (R-096), and endless scroll and pull to refresh (R-104). Order: newest first (`PROVISIONAL: C14`, OQ-40). "Applies to every screen" now says a missing item is still banned |
| 12: Positivity Feed Holds said "Public photos"; no endless-content ban | S-09 Holds rewritten under B9 with both B9(a) options; endless scroll, autoplay, "more like this" and pull to refresh banned (R-104) |
| 13: no ban on an in-app "reflections are open" marker | Banned on S-05, S-14, S-06, S-15, S-17, S-04 (R-095, R-096; Spec:102) |
| 14: feeling tags followed one doc; "popular ones surface" not raised | S-19 cites Spec:131 and Proposal:141 without picking; suggestions and popularity counts held out; OQ-37 and OQ-38 added (no ID) |
| 15: wrong citations | "Reflection left" audience now cites Spec:280 (was Spec:282) on S-08, S-14 and OQ-22. S-08's popularity ban no longer cites Proposal:181; it cites Brief:44 and C14 and says no line names it for this feed |
| 16: time control not shown to apply the seal | T-01 applies the seal (R-014), reports nothing from a sealed journey, labels "jump to the next unlock" without whose or when (R-008), and sits outside the product's screens and navigation. T-02 added |

**2026-10-30, round 2 of 3.** Against `docs/reviews/2026-10-30-rules-screen-inventory-r1.md`. Clear findings only; N2, N3, N7 and N8 wait for the user:

| Finding | What changed |
|---|---|
| N1: B17–B19 not applied | Range now B1–B19. S-19 follows B17 (free text on the journey, no category) and B18 (no popularity, suggestions or counts). Type and commit date on S-03, S-05 and S-06 labelled `PROVISIONAL: B19`. OQ-37, OQ-38, OQ-39 now point to B17, B18, B19 |
| N4: start-highlight control while one is open | S-03 element 6 and S-13 `sealed · highlight open` ban greying or relabelling it (R-138) |
| N11: label with no ID | Out-of-scope C11 row now `PROVISIONAL: C11` |

**2026-10-30, round 2 follow-up.** Against `docs/reviews/2026-10-30-rules-screen-inventory-r2.md`: S-13 open state holds the start control and bans hiding it (N12). B18 applied to S-09; S-19's ban no longer limited to "while the owner writes" (N13). Source lists on S-03, S-05, S-06, S-09, S-19 carry B17–B19; unlock date labelled B19; Spec:74 wording follows the B19 row; log screen names corrected (N14).


**2026-10-30, user rulings.** G-8: Positivity Feed text only, the B9a switch removed (S-09, T-02). B2 option: Public photos wait too (S-06, OQ-9). B6 holds over B19 on S-03 element 7. All recorded in Spec §20 Q–S. N8 raised as OQ-41.

**2026-10-30, after the round 3 audit** (`docs/reviews/2026-10-30-rules-screen-inventory-r3.md`, PASS): B9 (a) no longer called switchable (N16); T-02 source drops B9 (N17); the owner half of B6 cites Spec §20 S, OQ-26 updated (N18); S-17 bans stepping photo to photo from the feed (N20); N5 raised as OQ-42.

**2026-10-30, after the round 4 audit** (`docs/reviews/2026-10-30-rules-phase-1-r4.md`, FAIL). Screen-Inventory part only; Amendments and Proposal are fixed elsewhere:

| Finding | What changed |
|---|---|
| V1: type, dates, chapter and feeling tags open to public readers | New "Journey facts after unlock" paragraph under Viewers (Spec §20 T, X, CC, DD). S-06, S-16, S-17: viewer lines limit the four facts to owner and network; Holds give them to owner and network only; "Must never show" bans them to a public reader (R-152). S-09: no tag, chapter, type or date on any entry; Tag and Journey only select; its destinations carry their own limits (Spec §20 CC) |
| V2: highlight marker after unlock | S-06, S-16, S-17 ban, to anyone but the owner and also after unlock, any sign a photo was taken in a highlight; Reads exclude `highlight_id` (Spec §20 DD; `PROVISIONAL: B24`; R-151). Also on S-09 |
| V3: T-01 and T-02 behind B20–B23 and §20 V, Z | T-01 adds +1 minute and +1 hour (B20), baseline time (B21), reset restores switches (B22), the running clock (Spec §20 V), late scripted actions (B26), and bans a timer on note or highlight windows (R-140). T-02: switches in `prototype_option` via `set_option()` (Spec §20 Z), one global setting (B23), reset restores defaults (B22); Reads adds `prototype_option`. Defaults range now B1–B26 |
| N1: B2's option said "others, nothing yet" | S-06 `unlock-day` row: under B2's option the network still reads type, dates, chapter and tags from unlock; only photos and what follows them wait (Spec §20 X) |
| N3: stale citations | OQ-30 now cites Proposal:364 (§3.7). Spec:299 → Spec:317–327 (§21) under Viewers, the prototype section and T-01. Not in this build: Spec:290–291 → Spec:312–313 |
| N4: OQ-41, OQ-42 had IDs | Now point to Decisions C17 and C18, still no default |
| New | OQ-43 (time of day in T-02), OQ-44 (dates on rings and path order for a public viewer), OQ-45 (capture times and highlight inference, audit N8) |

**2026-10-30, after the user rulings Spec §20 EE–HH** (`docs/reviews/2026-10-30-gate-1-r4.md` CF-22, CF-23; `docs/reviews/2026-10-30-rules-phase-1-r5.md` V3, N4). Screen-Inventory part only:

| Finding | What changed |
|---|---|
| CF-22 / r5 V3: non-owners given the full capture time (Spec §20 GG) | "Applies to every screen" bans, to anyone but the owner, a capture time of day, a note's written time and an activity graph finer than a day (R-154). S-16: Reads give `captured_at` as a date only; B5's option graph no finer than a day; the ban added to `unlock-day` and "on every state". S-06, S-17: the ban added to "on every state"; Reads give the full time to the owner, the date only to others, and never a note's written time. S-05 Reads: the owner sees the full time |
| NB-22: same-day order for non-owners | Not picked. Raised as OQ-46, with the note's written date as a second point |
| EE: only the panel moves time or flips switches (Spec §20 EE) | Viewers table, prototype section, T-01 and T-02: the panel is a separate role; the acting viewer never moves the clock or flips a switch, and no such control appears on a product screen (R-153). T-01 and T-02 cite Spec:309 |
| r5 N4 / HH: S-15 cited "strictest reading" | S-15 viewer line cites Spec §20 HH (Spec:312); source list adds it. S-06 `unlock-day` row: under B2's option no overview either. OQ-14 records HH |
| CF-23: Spec citations off by four lines | §21: Spec:317–327 → Spec:321–331 in the Viewers table, the prototype section and T-01. Not in this build: Spec:312–313 → Spec:316 (export), Spec:317 (age gating). Every other Spec:2xx–3xx citation checked against `Functional-Spec.md` at this date: Spec:296 (T), :298 (V), :301 (X), :303 (Z), :307 (CC), :308 (DD) unchanged and correct. The round 4 log row above keeps its old numbers as history |

**2026-10-31, after the user rulings Spec §20 PP–ZZ** (`docs/reviews/2026-10-31-rules-phase-1-r6.md` V4, N2, N4; `docs/reviews/2026-10-31-gate-1-r5.md` CF-28, NB-24–NB-26). Screen-Inventory part only. Amendments and Proposal are fixed elsewhere:

| Finding | What changed |
|---|---|
| CF-28 / r6 N4: Spec citations stale again | §21 is now Spec:342–352, after SS–ZZ added 11 lines. Spec:321–331 → Spec:342–352 in the Viewers table, the prototype section and T-01. Export Spec:316 → Spec:337, age gating Spec:317 → Spec:338 (§20 "Still open — can wait"). The gate review's targets (FS:335–345, :330–331) went stale when WW–ZZ landed, so the current lines are used. Every other Spec:29x–3xx citation was re-checked against `Functional-Spec.md` on this date: :296 T, :298 V, :301 X, :303 Z, :307 CC, :308 DD, :309 EE, :311 GG, :312 HH are all correct. History rows keep their old numbers |
| r6 V4: S-02 silent on PP, VV, QQ | S-02 source adds Spec:320, :321, :326, :331. New row for the guard bug, which the user never sees: one press is one photo, never a retake (PP). The app strips again and saves once (VV), judged and stamped at the press instant (XX). The guard's refusal never reaches the user and never reuses the capture refusal copy. New "Stored format" line: baseline JPEG, nothing shown to the user (QQ). OQ-47 and OQ-48 raised |
| r6 N4: JJ and LL | "Applies to every screen": the OQ-46 "not settled" line becomes JJ's fixed order with no time. "Written time" becomes LL's "never when a note was written, not even the date". The same change is made on S-06 (never list, Reads) and S-17 (never list, Reads) |
| TT | "Applies to every screen" bans another user's join date. Reads on S-06, S-08, S-16 and S-18 now say name only, never `joined_at`. S-05 reads the owner's own `joined_at` only for B4's option. S-06, S-07, S-09, S-16 and S-17 add the ban |
| WW (gate NB-24) | S-05: B4's per-year rings show only on the owner's own profile. S-16: one ring per finished reveal under both settings. Its `no-journey` and `reveal-finished` rows are rewritten to match. S-21 purpose and T-02's B4 row (S-16 no longer changes) are updated. OQ-6 records WW, and OQ-44 is partly settled |
| YY (gate NB-26) | The profile-picture bans on every screen, S-05, S-07, S-08, S-11 and S-16 now cite Spec §20 YY. OQ-31 records it. OQ-49 asks whether YY also decides the rest of C7 |
| SS, ZZ | "Journey facts after unlock" adds the rule: the reveal state goes to the owner and network after unlock, and is never a field, label or marker for a public reader. Inferring it from the Positivity Feed, rings or photos is allowed. Bans added on S-06, S-09, S-16 and S-17. Reads on S-06 and S-16 limit `journey_reveal` to owner and network |
| UU, B10 | S-08: the owner sees their own "reflection left", never their own "journey launched" or "path crossed" (UU). "Reflection left" goes only to the owner's network members who can see the photo, even a public one, and never to a public reader off the map (`PROVISIONAL: B10`). Under B2's option it reaches the owner only. The same change is made on S-14 and recorded in OQ-22 |

**2026-10-31, after the user rulings Spec §20 AAA–DDD.** Screen-Inventory part only:

| Ruling | What changed |
|---|---|
| AAA (Spec:334) | S-02 source adds Spec:334. The guard-bug row now says the retry is stored at the original press instant, never later, and VV's "slightly later" is retired. OQ-48 records it as decided |
| BBB (Spec:335) | S-09 source adds Spec:335. B9 (e) leaves the provisional list and is decided: newest reflection first, by the reflection's written time. The `reveal-finished` row's `PROVISIONAL: B9e` is replaced. OQ-30 records it |
| CCC (Spec:336) | S-16 source adds Spec:336. The rings paragraph, the `no-journey`, `reveal-finished` and `later-years` rows, the "on every state" list and Reads now say a public viewer's rings come from a count of finished reveals only, with no date, year or journey label on any ring. OQ-44 is settled for S-16 rings and stays open for S-06 path order |
| DDD (Spec:337) | S-02 source adds Spec:337. The guard-bug row says the camera shows nothing different while the app strips again and bans a wait indicator. A new row covers a press whose stripping fails twice: nothing different, no photo, no error, no "try again", and the logged bug never shown. OQ-47 records it as decided. OQ-50 is raised for what follows that press (S-12 or not, and whether a frame was used) |
| C7 | OQ-49 stays open |
| Citations | AAA–DDD added four lines to §20. §21 is now Spec:346–356 (was 342–352) in the Viewers table, the prototype section and T-01. Export is now Spec:341 (was 337) and age gating Spec:342 (was 338). Every other Spec:3xx citation was re-checked against `Functional-Spec.md` on this date: :301 X, :303 Z, :307 CC, :308 DD, :309 EE, :311 GG, :312 HH, :314 JJ, :316 LL, :320 PP, :321 QQ, :323 SS, :324 TT, :325 UU, :326 VV, :330 WW, :331 XX, :332 YY and :333 ZZ are all correct. History rows keep their old numbers |
