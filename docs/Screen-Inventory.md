# My Journey — Screen Inventory

Phase 1 deliverable (`Build-Plan.md:65`): every screen the app needs, named, nothing designed yet. Phase 2 writes the flows from this list and Phase 4 builds the screens from it.

Written: 2026-10-27, by the UX agent. Simulated baseline used throughout: **2026-10-25** (`Phase-1-Proposal.md:200`).

What this file does: names each screen, traces it to the spec by file and line, says who can see it, and says what it holds and must never show at each point in simulated time. What it does not do: layout, colour, type, final copy or flows. Where the spec is silent or contradicts itself, the gap is listed under **Open questions** and left open.

Sources, in the order of trust set by `CLAUDE.md`: `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29, then the rest of `Functional-Spec.md`, then `Phase-1-Proposal.md`, then `Master-Prompt.md`, `Build-Plan.md` and the rest of the Concept doc. `Overview.md` is not cited anywhere. File names below are shortened: **Spec** = `Functional-Spec.md`, **Proposal** = `Phase-1-Proposal.md`, **Plan** = `Build-Plan.md`, **Brief** = `Master-Prompt.md`, **Concept** = `My-Journey-Concept.md`. All are in `docs/`.

---

## Time states

Defined once and used in every states table. All but `no-journey` describe **one journey**. A screen that shows several journeys (a profile, a path) shows each in its own state: at baseline Steady Lantern has #1–#5 in `later-years` and #6 `sealed` (Proposal:218–223).

| State | Definition | Source |
|---|---|---|
| `no-journey` | User-level. The user has no sealed journey. Two cases: **never committed** (First Light) and **between journeys** (the last journey has unlocked and no new Commit yet, as Long Way Round). Commit is open. It can sit alongside the last journey's `unlock-day`, `reveal-open`, `reveal-finished` or `later-years` | Spec:30, Spec:273 (§20 C), Proposal:16 (D3), Proposal:209–210 |
| `sealed` | `committed_at ≤ now < unlocks_at`. Nothing in the journey is readable, the owner included | Spec:73–76, Spec:234, Proposal:48, Proposal:80 |
| `sealed · highlight open` | Sub-state of `sealed`: a highlight the user started is within its 24 hours, cut off at `unlocks_at` | Spec:264, Spec:284 (§20 N), Proposal:133 |
| `sealed · note window` | Sub-state of `sealed`: within 15 minutes of a photo's capture, while that photo has no note | Spec:281 (§20 K), Proposal:108 |
| `unlock-day` | The moment `now` first reaches `unlocks_at`: the whole journey unlocks as one event, and no reveal choice has been made yet. The data model does not separate it from `reveal-open` (Proposal:81). It is listed on its own because the weighted line "Your Journey is ready" belongs to it (Plan:79, Concept:740). See OQ-15 | Spec:73, Spec:255 (§20 A), Spec:273, Proposal:194 ("jump to the next unlock") |
| `reveal-open` | Unlocked, reveal not finished, inside reflection slot 1 (unlock to unlock + 1 year). No deadline for finishing is stated (OQ-16) | Proposal:81, Spec:269 (§20 9), Spec:274 (§20 D) |
| `reveal-finished` | Reveal finished, still inside slot 1. Visibility, people tags, chapter and feeling tags are locked | Proposal:82, Proposal:164, Spec:276 (§20 F) |
| `later-years` | `now ≥ unlock + 1 year`: reflection and overview slot *k* ≥ 2. Two variants: `later-years · finished` and `later-years · never finished` (Long Way Round #4 from 2027-09-06) | Spec:274 (§20 D), Spec:275 (§20 E), Spec:269, Proposal:333 |

**Viewers**, used in every screen entry:

| Viewer | Meaning | Source |
|---|---|---|
| owner | The user whose journey, photo or map it is | Spec:100, Spec:145 |
| network | A user on the owner's map, any ring. "Network" and "a user on the owner's map" are the same set | Spec:146, Proposal:344 (R2) |
| public | Any user, including one on no one's map (First Light) | Spec:147, Proposal:313 |
| tagged | A user tagged in the owner's photos. Being tagged gives no access by itself | Spec:196, Proposal:288 |
| demoer | Whoever runs the prototype. Only for T-01 | Spec:299 |

**Applies to every screen.** None of these ever appears, in any state, for any viewer (Brief:37–47, Spec:226–247): "No retakes" · "No edits to reflections" · "No comments from anyone else" · "No face recognition" · "No ads, anywhere" · "No streaks, counters, progress bars, reminders" · "No re-engagement notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed" · "Nothing leaks from a sealed year" · "No layer is ever shown to the person on it". The schema scan words are banned as screen elements too: "comment, reply, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:180). The tables below quote only the banned items most at risk on that screen.

---

## Screens: the nine Build-Plan screens, in ritual order (Plan:103–113)

### S-01 Commit

- **Purpose:** the user picks one of three journey types and presses Commit, which cannot be undone.
- **Spec source:** Spec:34–47 (§3); Spec:263, Spec:273 (§20 3, C); Proposal:14–17 (D1–D4); Plan:105
- **Viewer:** owner (the committing user)
- **Reached from:** Profile (own) S-05 or app entry (not specified, OQ-34). **Leads to:** The sealed year S-03

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed | The three types with difficulty, cadence, photos per year and highlights (Spec:38–42). The Commit action (Spec:44–45). Available on any day (Spec:36, Proposal:15) | A pre-selected type: "No default type is pre-selected" (Spec:46). A softer verb: "'Commit' carries weight; 'Start' and 'Create' do not" (Concept:115) |
| `no-journey` · between journeys | The same. Open as soon as the last journey has unlocked, even while its reveal is still open (Spec:273: "the next Commit is only possible once the current one has unlocked") | Any prompt to commit again: "Remind a user to capture, reflect, or return" (Spec:242) |
| `sealed` | Not available. One journey at a time (Spec:273; Proposal:177, check 3) | A second Commit. Any way to change type or abandon: "It cannot be changed for that year" (Spec:44), "No abandoning" (Spec:263) |
| `unlock-day`, `reveal-open`, `reveal-finished`, `later-years` | Only through `no-journey` · between journeys (above) | As above |

- **Reads:** User, Journey (Proposal §2.2); `journey_type` constants (Proposal:167)
- **Copy:** the Commit moment and the button itself `[copy: copywriter]` (Plan:79, Spec:45). The three type descriptions `[copy: copywriter]`. See OQ-13 on the "old 24–48 range" wording

### S-02 Capture

- **Purpose:** take one photo inside the app, at the moment, in three taps. It is sealed at once.
- **Spec source:** Spec:51–59 (§4); Spec:228 (§18); Spec:261–266 (§20 1, 2, 5, 6); Proposal:94–99; Plan:106
- **Viewer:** owner
- **Reached from:** The sealed year S-03, Start a highlight S-13. **Leads to:** The note step S-12, then back to S-03

| State | Holds | Must never show |
|---|---|---|
| `sealed`, a normal frame available | The in-app camera, photos only. Three taps, then the photo is sealed. The only result is accepted (Proposal:49, 97) | "No retakes" (Spec:55). "no review-before-save" (Spec:228). The photo just taken, as a preview or thumbnail: "No previews, no counts of what is inside, no thumbnails" (Spec:75). "No tagging, no writing, no choices" (Spec:54). Video: "No video" (Spec:57). A quality check (Spec:56). Import of a photo not taken in the app (Spec:53). Frames used or left (Proposal:49; Spec:243) |
| `sealed · highlight open` | The same camera. The frame limit does not apply, up to the type's yearly quota (Spec:65, Spec:265, Proposal:96) | Highlight photos left, highlights left (Proposal:49). Whether the time left in the window may show is OQ-26 |
| `sealed`, no frame available and no highlight open | The capture is refused (Proposal:97–99). What the user sees is not specified: OQ-25 | Any count or target: "Show a count of how much of their quota is left in a way that reads as a target" (Spec:243) |
| `sealed · note window` | Capture works as normal; the note step for the earlier photo is S-12 | As in `sealed` |
| `unlock-day` onward, `no-journey` | Not available. `capture()` "only works on a sealed journey, so nothing can be captured after unlock" (Proposal:99) | A way to add a photo to an unlocked journey |

- **Reads:** Journey, Photo (written, never read back), Highlight (Proposal §2.2), through `capture()`'s accepted or refused only
- **Copy:** the capture refusal `[copy: copywriter]`. The no-retake line "No retakes. That moment is gone." (Brief:120) `[copy: copywriter]` decides where it sits

### S-03 The sealed year

- **Purpose:** the owner's current journey while it is sealed: an empty state that leaks nothing and reads as intended, and the way out to what the user does instead.
- **Spec source:** Spec:71–76 (§6); Spec:233–234 (§18); Spec:246 (§19); Spec:279 (§20 I); Proposal:48–50, Proposal:84; Plan:107; Brief:71, Brief:130
- **Viewer:** owner. How others see a sealed journey is a state of S-16 and S-06 ("exists only", Proposal:310)
- **Reached from:** Commit S-01, app entry while `sealed` (OQ-34). **Leads to:** Capture S-02, Start a highlight S-13, Positivity Feed S-09, Feed S-08, Layers S-07, Another user's profile S-16, Profile (own) S-05

**What the spec allows this screen to hold. Exactly this list:**

| # | Element | Source |
|---|---|---|
| 1 | That the owner has a journey underway | Proposal:84 ("The owner also sees type, commit date and unlock date. Nothing else."), Proposal:309 |
| 2 | The journey's type | Proposal:84 |
| 3 | The commit date | Proposal:84 |
| 4 | The unlock date. Whether it may be shown relative to today is OQ-27 | Proposal:84 |
| 5 | The way to Capture (S-02) | Spec:53, Proposal:99 |
| 6 | The way to start a highlight (S-13) | Spec:264 |
| 7 | The way to what the user does instead: other people's unlocked journeys, through the Positivity Feed, the Feed, Layers and profiles | Spec:76 ("The user's engagement during this period is other people's unlocked journeys, not their own"), Brief:71, Concept:446, Concept:555 |
| 8 | Words that make the wait read as deliberate `[copy: copywriter]` | Plan:79 ("Microcopy for the moments that carry weight: Commit, sealed, …"), Brief:138 |

Not on the list, and not decided: the owner's own earlier, unlocked journeys (OQ-10); whether a highlight is open and when it ends (OQ-26).

**Why it must read as intended, not broken.** The data returns nothing at all: as the owner, "photos return 0 rows, `count(*)` returns 0" (Proposal:178). So any empty-list or still-loading pattern would look like a fault. The emptiness is the product (Brief:130; `ux.md:21`). Phase 2 and the copywriter make it read that way. This file does not.

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Elements 1–8 above | "No previews, no counts of what is inside, no thumbnails" (Spec:75). "Not thumbnails, not counts, not '3 moments captured'" (Brief:46). Frames used, frames left, highlights left (Proposal:49). The year's activity graph or line: "Never during the sealed year" (Spec:187). Anything derived from `captured_at`, such as the last capture or which months have photos, since it is unreadable (Proposal:48, 50). Any note (sealed, Proposal:105). "No visible counters, no progress bars, no reminders during the sealed year" (Spec:233). A reminder to capture (Spec:242). A prompt to photograph a low point: "The app does not prompt anyone to document a bad moment" (Spec:209). A way to change type or abandon (Spec:44, Spec:263). A second Commit (Spec:273) |
| `sealed · highlight open` | Elements 1–8. Whether the open window may show is OQ-26 | As in `sealed`, and highlight photos taken or left (Proposal:49) |
| `sealed · note window` | Elements 1–8, and the way back to the note step for the photo just taken. How the user gets back to it is OQ-24 | As in `sealed`. The photo the note belongs to |
| `unlock-day` | The screen gives way to Reveal S-04 | Nothing from the sealed list carries over: the whole journey opens at once (Spec:73) |
| `no-journey` | Not reached. Commit S-01 is open instead | |

- **Reads:** Journey (type, `committed_at`, `unlocks_at` only) (Proposal §2.2)
- **Copy:** the sealed state `[copy: copywriter]` (Plan:79). Approved lines exist (Brief:115–122, for example "This app takes time, like many other good things."). Where each goes is the copywriter's call

### S-04 Reveal

- **Purpose:** the annual moment. The whole journey opens and the owner writes reflections, tags people, applies the chapter and feeling tags, writes the overview and sets visibility, each choice once.
- **Spec source:** Spec:80–91 (§7); Spec:269 (§20 9); Spec:276 (§20 F); Spec:285–286 (§20 O, P); Proposal:25 (D12); Proposal:347 (R5); Plan:108; Brief:73
- **Viewer:** owner
- **Reached from:** the unlock (how is OQ-15), Profile (own) S-05. **Leads to:** Reflect S-14, Tag people S-18, Chapter and feeling tags S-19, Journey overview S-15, Visibility S-20, Finish the reveal S-21

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not reachable | Anything: "Sealed content is unreadable by the owner, not merely hidden in the UI" (Spec:234) |
| `unlock-day` | The whole journey at once: every photo and its note (Spec:73, Spec:255). Every photo is Network until the owner chooses (Spec:151). "Your Journey is ready" `[copy: copywriter]` (Plan:79, Concept:740) | Photos opening one by one: "Photos do not open individually" (Spec:73) |
| `reveal-open` | The five reveal steps (Spec:84–88), each reachable. Which choices are already set, and that they are now fixed (Spec:286, Proposal:347) | A way to change a set choice: "Each reveal choice is set once, even before the reveal is finished" (Spec:286). A way to edit or delete a photo: "A photo can never be deleted" (Spec:266). Suggested faces: "No face recognition, ever" (Spec:127). A reminder to finish (Spec:242). A completion bar: "No streaks, counters, progress bars, reminders" (Brief:42). The album order step: "Optionally orders the physical album (phase 2)" (Spec:89) is the album phase, not in this build |
| `reveal-finished` | The journey with its choices, locked and read-only (Spec:276). Reflect and Journey overview stay open for slot 1 (Proposal:117; overview timing is OQ-14) | Any way to change visibility, people tags, chapter or feeling tags (Spec:276, Proposal:46) |
| `later-years · finished` | As `reveal-finished`, with slot *k* open for Reflect and Journey overview | As `reveal-finished` |
| `later-years · never finished` | Photos still Network, no chapter, no tags (Spec:269). Whether the reveal can still be finished is OQ-16 | "no 'journey launched'" and no layer update until finished (Spec:269) |

- **Reads:** Journey, Photo, Handwritten note, Reflection, Journey overview, Tag (Proposal §2.2); `journey_reveal`, `person_tag`, `photo_visibility` (Proposal:164–166)
- **Copy:** "Your Journey is ready" `[copy: copywriter]`; the reveal itself `[copy: copywriter]` (Plan:79, Brief:138)

### S-05 Profile (own)

- **Purpose:** the owner's destination: the circle around the profile picture, one ring per year, the activity line twisted into it, and the way into their own journeys.
- **Spec source:** Spec:181–187 (§14); Spec:29 (§2); Proposal:65; Concept:681–714 (§21); Plan:109; Brief:85
- **Viewer:** owner. Others see S-16
- **Reached from:** app entry (OQ-34), Reveal S-04, Layers S-07 (the core). **Leads to:** Walking a path S-06 (own), Reveal S-04 when a reveal is open, Commit S-01 in `no-journey`, Journey overview S-15, The sealed year S-03

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed | Name, profile picture, the circle with no rings (whether a ring counts years with the app or finished reveals is OQ-6). "A person who joined this year is not behind; their circle is simply younger" (Concept:694) | "no scores, no levels, no leaderboard, no badges, no comparison between users" (Spec:185). Anything that "signals how the person looks or how well they are doing" (Spec:29) |
| `sealed` (current journey) | Rings and activity lines of earlier journeys. The current journey as existing, with type, commit date and unlock date only (Proposal:84) | The current year's activity graph: "Never during the sealed year. A visible grid being filled is a streak mechanic and is banned" (Spec:187). Any thumbnail or count from the sealed journey (Spec:75) |
| `unlock-day`, `reveal-open` | The year's activity graph may now appear: "only after the year unlocks" (Spec:187). Whether its ring and twisted line appear now or at finish is OQ-6 and OQ-7. The way into Reveal S-04 | As in `sealed`, for any other journey still sealed |
| `reveal-finished` | A new ring: "one ring per journey whose reveal is finished" (Proposal:65). The year's activity line twisted into the circle (Spec:186) | A ring presented as an achievement: "A record, not a rank" (Spec:185) |
| `later-years` | Rings accumulate. The overview stack, readable back to back (Spec:121) | As above |
| `no-journey` · between journeys | As `reveal-open`, `reveal-finished` or `later-years` for the last journey, plus the way to Commit S-01 | As above |

- **Reads:** User, Journey, Photo (`captured_at`, for the activity graph, after unlock only, Proposal:50), Journey overview (Proposal §2.2)
- **Copy:** the young circle of a new user `[copy: copywriter]`

### S-06 Walking a path

- **Purpose:** read a person's journeys from the beginning to now, in order, with the hard times and the reflections written later.
- **Spec source:** Spec:191–196 (§15); Spec:149 (§11); Spec:177 (§13); Concept:563–582 (§16); Plan:110
- **Viewer:** owner, network, public, tagged. What each sees depends on photo visibility (Spec:143–147, Proposal:305–313)
- **Reached from:** Profile (own) S-05, Another user's profile S-16, Feed S-08, Positivity Feed S-09. **Leads to:** A photo, followed forward S-17, Journey overview S-15, Another user's profile S-16

| State (of each journey on the path) | Holds | Must never show |
|---|---|---|
| `sealed` | Owner: exists, type, commit date, unlock date. Others: exists only (Spec:279, Proposal:84, Proposal:310) | "Reveal anything about a sealed journey, including its existence in detail" (Spec:246). Any photo, count, thumbnail or capture date (Spec:75) |
| `unlock-day`, `reveal-open` | Owner: every photo. Network: every photo not yet set Private, because Network is the default (Spec:151, Proposal:311: Open Hands reads Long Way Round #4). Public: only photos already set Public. No chapter or feeling tags until set. Whether others should see a journey before its reveal is finished is OQ-9 | Private photos to anyone but the owner (Spec:145, Proposal:29) |
| `reveal-finished` | Photos by their locked visibility. Reflections follow their photo (Spec:276). The overview, to the owner and network only (Spec:275). Chapter and feeling tags | As above |
| `later-years` | As `reveal-finished`, with deeper reflection stacks and an overview stack (Spec:121) | As above |

On every journey, for every viewer, never: a grid: "in order, not as a grid" (Spec:193). An effortless scroll into it: "It must not be as effortless as scrolling" (Spec:177). A comment or reply: "Others may read; only the owner writes" (Spec:100). The viewer's own ring on this person's map (Spec:164, Spec:235). Access through being tagged: "being tagged doesn't give access" (Proposal:288). How the tagged reader's appearances are shown, given layer invisibility, is OQ-19.

- **Reads:** User, Journey, Photo, Handwritten note, Reflection, Journey overview, Tag (Proposal §2.2); `photo_visibility`, `person_tag` (Proposal:165–166)
- **Copy:** the moment a reader finds themselves in someone's hard year `[copy: copywriter]` (Concept:578–582: "Design for it deliberately")

### S-07 Layers

- **Purpose:** the owner's own map: the user at the core, people on concentric rings earned by crossing journeys, and the way to their profiles.
- **Spec source:** Spec:156–165 (§12); Spec:277–278, Spec:282 (§20 G, H, L); Proposal:27–29 (D14–D16); Proposal:145–160; Plan:111; Brief:81
- **Viewer:** owner only. "Each user sees only their own map" (Spec:164)
- **Reached from:** Profile (own) S-05, The sealed year S-03, app entry (OQ-34). **Leads to:** Another user's profile S-16

The map changes only when the owner finishes a reveal. So the table follows the **owner's** journey states.

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed, or no reveal ever finished | The core only: "First Light's map is empty" (Proposal:286). What an empty map holds is OQ-23 | People who were never tagged. A way to add someone by choice: "Earned, not chosen" (Spec:160) |
| `sealed` | The map as computed at the last finished reveal, unchanged | Any change: "Layers are recalculated at this point, never during the sealed year" (Spec:91) |
| `unlock-day`, `reveal-open` | Unchanged | Any change before finish: "the layers aren't recomputed" (Spec:269) |
| `reveal-finished` | Recomputed: users tagged in the journey at tight (5+), middle (2–4) or outer (1) by count, straight to that ring (Spec:161, Spec:282). Untagged members out one ring (Spec:165) | Anyone dropping off: "Nobody ever drops off the map" (Spec:165). Typed names: "Typed names never count" (Spec:163) |
| `later-years` | Unchanged until the next finished reveal | |

On every state, never: another user's map, or where the owner sits on it: "A person is never shown which layer they are on" (Spec:164), "No endpoint returns which layer a viewer sits on in someone else's map" (Spec:235). A list: "the Apple Watch app menu, not a list" (Spec:159). Extra access for the inner ring: close friends "see nothing beyond the rest of the network" (Spec:150; see OQ-4). "No ranking, levels, badges or leaderboards" (Brief:44). Whether past rings, drift history or shared-photo counts appear is OQ-36.

- **Reads:** Layer, User (Proposal §2.2)
- **Copy:** drift outward, framed as expected: "treated as a feature, not a failure" (Spec:165) `[copy: copywriter]`. The empty map `[copy: copywriter]`

### S-08 Feed

- **Purpose:** announcements only, on three events, each a line the reader may choose to act on.
- **Spec source:** Spec:169–177 (§13); Spec:280, Spec:283 (§20 J, M); Proposal:31 (D18); Proposal:168; Proposal:344 (R2); Plan:112; Brief:83
- **Viewer:** any user, each announcement to its own audience: "journey launched" and "path crossed" to the owner's network (Spec:283); "reflection left" only to people who can see that photo (Spec:282)
- **Reached from:** app entry (OQ-34), The sealed year S-03. **Leads to:** Another user's profile S-16, Walking a path S-06, A photo, followed forward S-17, each by "a small deliberate act" (Spec:177)

The table follows the state of the **announced** journey.

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Nothing about it. No announcement exists for Commit or capture | Anything about a sealed journey (Spec:246) |
| `unlock-day`, `reveal-open` | "Reflection left", if the owner writes one (Proposal:117), to those who can see the photo | "Journey launched" or "path crossed" before finish: "There's no chapter, no tags, no 'journey launched'" (Spec:269) |
| `reveal-finished` | "Journey launched" (Spec:280). "Path crossed", one per crossing (Spec:280). "Reflection left" | Who is named in "path crossed", and whether it reaches the crossed person, is OQ-21 |
| `later-years` | "Reflection left" for new slot reflections | |
| (viewer with an empty network) | Only "reflection left" on public photos would reach them (Spec:282 with Spec:147). Whether that is intended is OQ-22. What an empty feed holds is OQ-23 | |

On every state, never: an image: "Announcements only. No photographs in the stream" (Spec:171), "no media column" (Proposal:168). A fourth event type (Proposal:168, Proposal:183). A count: "no count column" (Proposal:168). Likes, replies or popularity (Proposal:180). A push to return: "No re-engagement notifications of any kind" (Spec:236).

- **Reads:** User, Journey, Photo (visibility, for the audience), Reflection (Proposal §2.2); `announcement` (Proposal:168)
- **Copy:** the three announcement lines `[copy: copywriter]`. The source wording ("published their Journey", Concept:424, 440) uses "publish": see OQ-3

### S-09 Positivity Feed

- **Purpose:** reflections written years later on other people's hard moments, filtered by tags of endurance and gratitude, so someone on a bad day finds a person who was where they are.
- **Spec source:** Spec:200–209 (§16); Spec:30 (§2); Proposal:315–324; Concept:450–559 (§15); Plan:113; Brief:87
- **Viewer:** any user. Content is public only (Spec:147, Spec:203)
- **Reached from:** Sign up (day one, Spec:30), The sealed year S-03, app entry (OQ-34). **Leads to:** A photo, followed forward S-17, Walking a path S-06, Another user's profile S-16

The table follows the state of the **source** journey. The reader's own state changes nothing: the same feed serves a new user (Spec:30) and a user in a sealed year (Concept:555).

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Nothing from it | Anything (Spec:246) |
| `unlock-day`, `reveal-open` | Nothing on `unlock-day` (every photo is Network by default, Spec:151). Whether a photo set Public before the reveal is finished enters the feed is OQ-30 | Network or private content |
| `reveal-finished` | Public photos and their reflections, from journeys with endurance and gratitude feeling tags (Proposal:317). Whether the photo image itself appears is OQ-11 | Ordering by popularity: "never by popularity" (Spec:202). "Public means readable, not commentable" (Spec:152) |
| `later-years` | The same, with reflections written years after the moment, which is the feed's primary use (Spec:204) | As above |

On every state, never: a prompt to capture a low point: "invited, never nudged" (Spec:209). Likes, reactions, views or counts (Proposal:180). Which tags qualify, chapter filtering and order are OQ-30. "Journeys set to public" versus per-photo visibility is OQ-12.

- **Reads:** Photo, Reflection, Tag, Journey, User (Proposal §2.2); `photo_visibility` (Proposal:166)
- **Copy:** the feed's purpose, for someone having a bad day `[copy: copywriter]`; the founding line "the hard part was the start" is a drafted tag (Spec:207, Concept:544)

---

## Screens the spec implies beyond the nine

### S-10 Sign up

- **Purpose:** an open way in for anyone, invited or not.
- **Spec source:** Spec:25–30 (§2)
- **Viewer:** a person without an account
- **Reached from:** outside the app; invitation is the main path (Spec:28; how it works is OQ-32). **Leads to:** Choose a name S-11, then the day-one experience: Positivity Feed S-09 and other people's profiles (Spec:30)

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed (only state) | Sign up | An invite gate: "Open signup. Anyone can join. No invite gate" (Spec:27). Any field about looks or status (Spec:29) |

- **Reads:** User (Proposal §2.2)
- **Copy:** the arrival `[copy: copywriter]`. Whether the prototype has sign-up at all, given "Real authentication … not in this plan" (Plan:228), is OQ-35

### S-11 Choose a name

- **Purpose:** the user chooses a name from within, once, for good.
- **Spec source:** Spec:29 (§2); Spec:268 (§20 8); Proposal:32 (D19); Proposal:61; Concept:665–677 (§20)
- **Viewer:** owner (new user)
- **Reached from:** Sign up S-10. **Leads to:** Positivity Feed S-09 (Spec:30)

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed (only state) | The name, chosen once (Spec:268). The profile picture is a User property (Spec:13); when and how it is set is OQ-31 | A way to change the name later: "Set once, immutable" (Proposal:61). A yearly name: "Decided 2026-10-25: no" (Concept:677). A prompt toward physical or earthly attributes (Spec:29) |

- **Reads:** User (Proposal §2.2)
- **Copy:** what "a name from within" means, and that it is kept `[copy: copywriter]`

### S-12 The note step

- **Purpose:** straight after capture, an optional, skippable offer to photograph a handwritten A4 page, which becomes the writing on the back of the photo.
- **Spec source:** Spec:16 (§1); Spec:257 (§20 B); Spec:281 (§20 K); Proposal:21 (D8); Proposal:101–108; Brief:69
- **Viewer:** owner
- **Reached from:** Capture S-02; re-entry within 15 minutes is OQ-24. **Leads to:** The sealed year S-03 or Capture S-02

| State | Holds | Must never show |
|---|---|---|
| `sealed · note window` | The offer to photograph one handwritten A4 page, and a way to skip (Spec:257). One note per photo (Proposal:104) | The photo it belongs to (Spec:75). A typed text field in place of the page: it is "A photographed A4 page" (Spec:16). Anything that holds up capture: "Skippable, so capture stays fast" (Spec:257). A second note for the same photo |
| `sealed`, after 15 minutes | Not offered: "up to 15 minutes after capture, never after" (Spec:281) | |
| `unlock-day` onward | Not a writing step. The note is read as the back of its photo in S-17 | Any way to rewrite it: "written once" (Spec:16) |

- **Reads:** Photo (id only), Handwritten note (Proposal §2.2)
- **Copy:** the offer, and the skip `[copy: copywriter]`. Whether the page can be re-photographed before saving is OQ-24

### S-13 Start a highlight

- **Purpose:** the user opens a 24-hour window in which the frame limit does not apply.
- **Spec source:** Spec:63–67 (§5); Spec:264–265 (§20 4, 5); Spec:284 (§20 N); Proposal:19 (D6); Proposal:128–135; Brief:65
- **Viewer:** owner
- **Reached from:** The sealed year S-03. **Leads to:** Capture S-02

| State | Holds | Must never show |
|---|---|---|
| `sealed`, no highlight open | The way to start one. Accepted, or refused once the type's allowance is used (Proposal:135). The window is 24 hours, cut off at unlock (Proposal:133) | Highlights left or used: "Frames used, frames left and highlights left are counted inside them and never stored or returned" (Proposal:49). The season as a rule: "Explorer's 'one per season' is a description, not a rule" (Spec:264) |
| `sealed · highlight open` | Starting another is refused (Spec:284) | As above. Whether the open window shows is OQ-26 |
| `unlock-day` onward, `no-journey` | Not available: "Only on a sealed journey" (Proposal:135) | |

- **Reads:** Highlight, Journey (Proposal §2.2), through `start_highlight()`'s accepted or refused only
- **Copy:** starting a highlight; the refusal `[copy: copywriter]`

### S-14 Reflect

- **Purpose:** the owner writes one reflection on one photo for the current slot, added to the stack and never edited.
- **Spec source:** Spec:95–102 (§8); Spec:274 (§20 D); Proposal:22 (D9); Proposal:24 (D11); Proposal:110–117; Brief:75
- **Viewer:** owner writes. Readers are the photo's readers (Spec:276)
- **Reached from:** Reveal S-04, A photo, followed forward S-17. **Leads to:** back to where it came from. Writing one emits "reflection left" (Spec:282), seen in S-08

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | The photo (Spec:234) |
| `unlock-day`, `reveal-open`, `reveal-finished` | Slot 1 open: one reflection per photo (Proposal:117: "any time after unlock (reveal finished or not)") | A second reflection in a slot already used: "One reflection per photo, per year" (Spec:97) |
| `later-years` (either variant) | Slot *k* open. Earlier reflections read-only, in order. All photos of the journey move to the next slot together on the unlock anniversary (Spec:101) | Per-photo anniversaries (see OQ-1) |

On every state, never: an edit or delete: "Immutable. No edits, ever" (Spec:99). Anyone else writing: "No comments from others" (Spec:100). A push: "The user is never pushed or reminded to write one" (Spec:102). A requirement to write one.

- **Reads:** Photo, Handwritten note, Reflection (Proposal §2.2)
- **Copy:** that a reflection is final once written `[copy: copywriter]`. "Strict at capture. Generous at reflect." (Brief:119)

### S-15 Journey overview

- **Purpose:** the owner writes how their views changed across the year, once per journey per year, and reads the stack.
- **Spec source:** Spec:115–121 (§9); Spec:275 (§20 E); Spec:285 (§20 O); Proposal:23 (D10); Proposal:119–126; Brief:77
- **Viewer:** owner writes. Owner and network read (Spec:275, Proposal:126). Not public
- **Reached from:** Reveal S-04, Profile (own) S-05, Walking a path S-06. **Leads to:** back to where it came from

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Nothing | Anything about the journey (Spec:234) |
| `unlock-day`, `reveal-open` | Slot 1 overview may be written. Optional (Spec:285) | A requirement to write one before finishing: "A reveal can be finished without one" (Spec:285) |
| `reveal-finished` | The slot 1 overview, if written. Whether it can still be written after finish is OQ-14 | |
| `later-years` | A new overview for slot *k*. The stack, readable back to back (Spec:121) | |

On every state, never: an edit: "Immutable, like everything else" (Spec:120). A reminder. A public reader.

- **Reads:** Journey, Journey overview (Proposal §2.2)
- **Copy:** the prompt to look back across the year `[copy: copywriter]`

### S-16 Another user's profile

- **Purpose:** another person's circle, rings and the way into their journey, read on purpose.
- **Spec source:** Spec:181–187 (§14); Spec:149–150 (§11); Spec:164 (§12); Spec:279 (§20 I); Proposal:30 (D17); Proposal:84; Proposal:305–313
- **Viewer:** network or public (any other user)
- **Reached from:** Feed S-08, Layers S-07, Positivity Feed S-09, A photo, followed forward S-17 (via a person tag, OQ-20). **Leads to:** Walking a path S-06

The table follows the state of the **profile owner's** journeys.

| State | Holds | Must never show |
|---|---|---|
| `no-journey` · never committed | Name, profile picture, circle (OQ-6) | "no comparison between users" (Spec:185) |
| `sealed` | That a journey exists, and nothing else: "Others may know only that one exists" (Spec:279) | Type, dates, counts, thumbnails, the year's activity: "Others see only `has_journey_underway(user)`" (Proposal:84); "including its existence in detail" (Spec:246) |
| `unlock-day`, `reveal-open` | The way into the journey, readable by visibility (Spec:149). Whether the activity graph shows here, and to whom, is OQ-7 and OQ-28 | Private photos |
| `reveal-finished` | The new ring. The journey by locked visibility | As above |
| `later-years` | Rings, and the overview stack for network viewers | As above |

On every state, never: the viewer's ring on this person's map, or this person's map at all (Spec:164, Spec:235). Extra access for the inner ring (Spec:150, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). Follower or view counts (Proposal:180). Anything that "signals how the person looks or how well they are doing" (Spec:29).

- **Reads:** User, Journey, Photo (`captured_at` after unlock, visibility), Journey overview (Proposal §2.2)
- **Copy:** none weighted

### S-17 A photo, followed forward

- **Purpose:** one photo read across time: the original moment, the handwritten note on its back, then the reflections that came after, in order.
- **Spec source:** Spec:195 (§15); Spec:15–17 (§1); Concept:162–168; Concept:569
- **Viewer:** owner, network, public, by the photo's visibility (Spec:143–147)
- **Reached from:** Walking a path S-06, Positivity Feed S-09, Feed S-08 ("reflection left"). **Leads to:** Reflect S-14 (owner), Walking a path S-06

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not reachable | Anything (Spec:234) |
| `unlock-day`, `reveal-open` | The photo, its note if any, the slot 1 reflection if written. Readers: owner, and network while the photo is Network by default (OQ-9) | The photo to a non-owner once it is Private |
| `reveal-finished` | As above, with visibility locked | As above |
| `later-years` | The reflection stack grows by at most one per slot (Spec:97) | As above |

On every state, never: a comment, reply or like (Spec:230, Proposal:180). A caption: "There's no caption" (Proposal:94). Edit or delete (Spec:266). Access through being tagged (Proposal:288). Whether people tags are shown to readers is OQ-20. What "the follow-up" is is OQ-29.

- **Reads:** Photo, Handwritten note, Reflection, Tag (Proposal §2.2); `person_tag`, `photo_visibility` (Proposal:165–166)
- **Copy:** none weighted beyond S-14

### S-18 Tag people (reveal step)

- **Purpose:** the owner tags, by hand, the people in each photo: users, or a typed name.
- **Spec source:** Spec:85 (§7); Spec:127 (§10); Spec:267 (§20 7); Proposal:26 (D13); Proposal:165
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Reveal S-04

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | Tagging at capture: "All tags are applied at reveal, never at capture" (Spec:133) |
| `unlock-day`, `reveal-open` | Per photo: tag a user, or type a name (Spec:267). Each tag, once set, is fixed (Spec:286). How a user is found is OQ-33 | Suggested faces: "No face recognition, ever" (Spec:127), "No face detection anywhere in the pipeline" (Spec:231). A way to remove a set tag (Spec:286). Any hint of where the tagged person will sit on the owner's map, shown to that person (Spec:164) |
| `reveal-finished`, `later-years · finished` | Tags, read-only (Spec:276) | Any change |
| `later-years · never finished` | OQ-16 | |

- **Reads:** Photo, User, Tag (Proposal §2.2); `person_tag` (Proposal:165)
- **Copy:** that this is deliberate, manual work `[copy: copywriter]`

### S-19 Chapter and feeling tags (reveal step)

- **Purpose:** the owner applies one chapter from the fixed catalogue and any free-text feeling tags.
- **Spec source:** Spec:86 (§7); Spec:129–135 (§10); Proposal:137–143; Concept:469–529
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Reveal S-04

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | |
| `unlock-day`, `reveal-open` | One chapter, from fixed categories under ME → ME, ME → YOU, ME → IT (Spec:129). Feeling tags as free text inside the category (Spec:131). Each set once (Spec:286). Whether a chapter is required to finish is OQ-17 | A second chapter: "One per journey" (Spec:129). A way to change a set tag |
| `reveal-finished`, `later-years · finished` | The tags, read-only | Any change (Spec:276) |
| `later-years · never finished` | None: "There's no chapter, no tags" (Spec:269). Whether they can still be set is OQ-16 | |

- **Reads:** Journey, Tag (Proposal §2.2); `chapter` catalogue (Proposal:167)
- **Copy:** the tone rule "even through hard chapters it stays positive and hopeful" (Spec:135) `[copy: copywriter]`

### S-20 Visibility (reveal step)

- **Purpose:** the owner sets, per photo, who can read it: Private, Network or Public.
- **Spec source:** Spec:139–152 (§11); Spec:276 (§20 F); Proposal:25 (D12); Proposal:166
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Reveal S-04

| State | Holds | Must never show |
|---|---|---|
| `sealed` | Not available | A visibility choice at capture: "chosen at publish time, not at capture" (Spec:141; "publish" is OQ-3) |
| `unlock-day`, `reveal-open` | Per photo: Private, Network, Public. Network until the owner chooses (Spec:151). Each set once (Spec:286) | A "close friends" level: they "see nothing beyond the rest of the network" (Spec:150). A way to change a set choice |
| `reveal-finished`, `later-years · finished` | Visibility, read-only (Spec:276) | Any change |
| `later-years · never finished` | Every photo stays Network (Spec:269). Whether it can still be set is OQ-16 | |

- **Reads:** Photo (Proposal §2.2); `photo_visibility` (Proposal:166)
- **Copy:** "Public means readable, not commentable" (Spec:152) `[copy: copywriter]`; that each choice is final (OQ-18) `[copy: copywriter]`

### S-21 Finish the reveal

- **Purpose:** the owner ends the reveal. Choices lock, the map is recomputed, "path crossed" and "journey launched" go out, and the year becomes a ring.
- **Spec source:** Spec:276 (§20 F); Spec:162 (§12); Spec:280 (§20 J); Proposal:25 (D12); Proposal:65; Proposal:152–160; Proposal:164
- **Viewer:** owner
- **Reached from:** Reveal S-04. **Leads to:** Profile (own) S-05 (the new ring)

| State | Holds | Must never show |
|---|---|---|
| `unlock-day`, `reveal-open` | The act of finishing ("Insert-only, only after unlock", Proposal:164). Whether it asks for confirmation is OQ-18; which steps must be done first is OQ-17 | A requirement to write an overview (Spec:285) or reflections (Spec:102). A reminder to finish (Spec:242) |
| `reveal-finished`, `later-years · finished` | Done. It cannot happen twice (Proposal:164) | An undo |
| `sealed` | Not available: nothing is readable yet (Spec:234) | |
| `later-years · never finished` | OQ-16 | |

- **Reads:** Journey, Tag, Layer (Proposal §2.2); `journey_reveal`, `announcement` (Proposal:164, 168)
- **Copy:** the finish, the weightiest act after Commit `[copy: copywriter]`

---

## Prototype only: not part of the product

### T-01 Time control

- **Purpose:** move the one simulated clock forward so the reveal, the reflection stacks, the rings and the paths crossing can be seen.
- **Spec source:** Spec:299 (§21); Proposal:191–200 (§3.1); Proposal:326–335 (§3.8); Plan:92
- **Viewer:** demoer only. It is not part of the product and is never shown as a product feature
- **Holds:** +1 day, +1 month, +1 year, +5 years, jump to the next unlock, reset to baseline (Proposal:194). On each jump: unlocks (derived), scripted actions, layers, announcements, in that order (Proposal:195–199)
- **Must never show:** a backward jump: "Forward only. To look at an earlier moment, reset and jump again" (Proposal:194)
- **Reads:** `sim_clock` (Proposal:169)

| Simulated point | What the product shows that it could not before | Source |
|---|---|---|
| Baseline 2026-10-25 | Four sealed journeys (S-03, S-16 "exists only"). Long Way Round #4 unlocked, never revealed. First Light with no journey and an empty map | Proposal:200–210, Proposal:241, Proposal:286 |
| 2027-01-01 | Steady Lantern #6 unlocks: `unlock-day`. "The reveal is left for whoever is demoing" | Proposal:200, Proposal:330 |
| 2027-04-25 | Second Wind finishes #6: "path crossed", "journey launched", a reflection and an overview | Proposal:331 |
| 2027-06-20 | Open Hands finishes #4, tagging Lantern once | Proposal:332 |
| +5 years | Long Way Round #4 still Network by default. The world goes quiet | Proposal:333–335 |

How the demoer chooses which fixture user they are viewing as is not specified (OQ-35).

---

## Not in this build

Listed only so no screen is built for them.

| Item | Source |
|---|---|
| The album phase: ordering, the physical album, print-shop ritual. Spec §7 step 6 calls it "phase 2"; that is the business stage, not a build phase | Spec:89, Spec:213–220, Plan:228 |
| Export and data ownership | Spec:290 |
| Age gating and parental consent | Spec:291 |
| Real authentication and real photo storage | Plan:228 |

---

## Open questions

Each one is a place the sources are silent or disagree. None is answered here. Where two docs disagree, both lines are cited and neither is picked.

**Contradictions between documents**

1. **Reflection timing in the example.** Spec:104–111 and Concept:203–210 date reflections on the photo's own anniversary (7 Jan), and Concept:200 says "on the photo's anniversary". Spec:101 and Spec:274 (§20 D), Concept:852 and Proposal:22 (D9) say all photos of a journey move to their next slot together, on the journey's unlock anniversary. §20 wins by `CLAUDE.md`. Should the example be corrected? Affects S-14, S-17.
2. **"Written a year or more after the moment."** Spec:98 conflicts with Spec:274 (§20 D): a photo taken in month 12 gets its slot 1 reflection weeks after the moment. Affects S-14.
3. **"Publish" names no real step.** Spec:141 ("chosen at publish time"), Concept:365–367, Concept:424, Concept:440 ("They published their Journey."). The decided steps are "reveal finished" and "journey launched" (Spec:276, Spec:280). Does "publish" mean "the reveal is finished"? Also open in `Learnings/index.md:54`. Affects S-20, S-08 copy.
4. **Close friends.** Concept:807 says "close friends get everything"; Concept:381–383 says close friends can be granted access to both. Spec:150, Spec:278 (§20 H) and Concept:864 say they see nothing extra. §20 wins. Should Concept:807 be marked superseded? Affects S-07, S-16, S-20.
5. **When layers are computed.** Concept:401 says "Calculated when Journeys are uploaded and ready to reflect on"; Concept:828–832 leaves the upload fork open. Spec:91, Spec:162 and Proposal:152 say when the reveal is finished. Also open in `Learnings/index.md:53`. Affects S-07.
6. **What a ring counts.** Spec:185 says "One ring per year with the app" and Concept:687 says "Each year with the app adds a ring". Proposal:65 says "one ring per journey whose reveal is finished". They differ for First Light (joined 2026-10-01, no journey), for Long Way Round #4 (never finished), and for any gap between journeys. Affects S-05, S-16.
7. **When the activity line is twisted in, and when the graph appears.** Spec:186 says "at the end of the journey", Spec:187 says "only after the year unlocks", Concept:706 says "At the end of the Journey". Proposal:65 adds the ring at reveal finished. In `unlock-day` and `reveal-open`, is there a graph without a ring? And what does the activity line record besides `captured_at` (Proposal:50; Concept:704: "the app records activity")? Affects S-05, S-16.
8. **Spec journey states.** Spec:14 lists "committed / sealed / unlocked". Proposal:76–84 collapses committed into sealed and splits unlocked into revealing and revealed. Spec §1 was not updated. Confirm the time states above follow the Proposal.
9. **Who sees a journey before its reveal is finished.** Concept:362 says sharing is "Only possible after unlock, and as a finished story or album". Spec:151, Spec:269 and Proposal:311 (Open Hands reads Long Way Round #4, never revealed) let the network read every photo from the moment of unlock, before the owner has set anything Private. Is that intended? Affects S-06, S-16, S-17 at `unlock-day` and `reveal-open`.
10. **Engagement in the sealed year.** Spec:76: "other people's unlocked journeys, not their own". Spec:274 (§20 D) keeps reflection slots open on the owner's earlier journeys during a new sealed year (Proposal:294: lantern-1 slot 5 on 2026-02-20, while #6 is sealed; Proposal:241: Long Way Round reflects on 2026-09-10). Does the sealed-year screen point to the owner's own earlier journeys? Affects S-03.
11. **Positivity Feed and "No photo feed".** Brief:45 says "No photo feed: The feed carries announcements only, never images"; Spec:171 says "No photographs in the stream". Proposal:317 fills the Positivity Feed with "Public photos (and their reflections)". Spec:204 speaks only of reading reflections. Does the Positivity Feed show the photograph? Affects S-09.
12. **"Journeys set to public."** Spec:203 and Concept:375 say the Positivity Feed is fed "only by journeys set to public". Spec:141 and Concept:379 set visibility per photo, not per journey. Affects S-09.
13. **The type arithmetic.** Spec:47, Concept:99 and Concept:128 say the three types sit on the old 24–48 range's "ceiling, middle and floor". 12 is outside that range, and the middle of 24–48 is 36. Concept:799 still says "Frame range 24–48". Affects S-01 copy.
14. **Overview timing.** Spec:118 says "Written at reveal". Spec:275 (§20 E) and Proposal:124 give it the same yearly windows as reflections. Can the slot 1 overview be written after the reveal is finished? Is it readable by the network before then (Proposal:126 sets no gate)? Affects S-15.

**Where the spec is silent**

15. **Unlock day.** How does the owner learn that the journey has unlocked, when there are "No re-engagement notifications of any kind" (Spec:236) and the app must never "Remind a user … to return" (Spec:242)? Concept:156 contrasts the reveal with "an unlock notification with nothing to do". Where does "Your Journey is ready" (Plan:79, Concept:740) appear? Is `unlock-day` a distinct state at all, given that the data model has none (Proposal:81)? Affects S-04, S-03.
16. **Does the reveal ever close?** No deadline is stated (Proposal:164: "only after unlock"; Spec:269). Proposal:333 says Long Way Round's #4 "stays unfinished" at +5 years, but not whether finishing is still possible. Can visibility, tags and chapter still be set in `later-years · never finished`? Affects S-04, S-18–S-21.
17. **What must be done before finishing.** Overviews are optional (Spec:285) and reflections are optional (Spec:102). Is a chapter required ("One per journey", Spec:129)? Are people tags or a visibility choice required? Affects S-21, S-19.
18. **Confirmation of a set-once choice.** Every reveal choice is final the moment it is made (Spec:286, Proposal:347 R5). Is the owner warned or asked to confirm, per choice and at finish? Affects S-18, S-19, S-20, S-21.
19. **"Where you appear" and layer invisibility.** Spec:196 and Concept:570 say the reader sees where they appear in someone's journey. Spec:164 and Spec:235 say no one learns their layer. Showing a reader the photos they appear in lets them count them and infer their ring (5+ tight, Spec:161). Only photos they can already see would show (Proposal:288). How is this shown without revealing the ring? Affects S-06.
20. **People tags shown to readers.** Can a reader see who else is tagged in a photo, and can a tag lead to that person's profile? Not specified. Affects S-17, S-16.
21. **"Path crossed" reaches the crossed person.** It goes to the owner's network (Spec:283). The crossed user is on the owner's map, so they receive it and learn they are on it. Does the announcement name them, and is that consistent with Spec:164? Spec:175 says "with a friend". Affects S-08.
22. **"Reflection left" on a public photo reaches everyone.** It goes to "people who can see that photo" (Spec:282), and a public photo is visible to anyone (Spec:147). So every user, First Light included, would receive it. Is that intended, given Spec:30 names the Positivity Feed and profiles as the day-one experience? Affects S-08.
23. **Empty states other than the sealed year.** What do an empty map (Proposal:286), an empty Feed and an empty profile circle hold? Not specified. Affects S-07, S-08, S-05.
24. **The note step after leaving it.** A note "can be added up to 15 minutes after capture" (Spec:281). The photo is unreadable at once, even to the owner (Spec:234, Proposal:48). How does the user get back to that photo inside the 15 minutes? And can the page be re-photographed before it is saved ("written once", Spec:16; "No retakes", Spec:55)? Affects S-12, S-03.
25. **A refused capture.** What does the user see when there is no frame (Proposal:97–99)? Is the camera offered at all? Spec:243 bans a quota count "in a way that reads as a target", which leaves room for some other kind of count. Proposal:49 returns no number at all. Affects S-02.
26. **An open highlight.** May the owner see that a highlight is open and when it ends? Proposal:49 forbids returning highlights left. The window itself is not addressed. Affects S-02, S-03, S-13.
27. **The unlock date shown relative to today.** The owner may see the unlock date (Proposal:84). Is "in 64 days" a counter under Spec:233? Affects S-03.
28. **Who sees the activity graph.** It is built from `captured_at` (Proposal:50), including private photos. Shown to network or public, it would reveal when private photos were taken (Spec:145). Is it owner-only, or built only from photos the viewer can see? Affects S-16.
29. **The "follow-up".** Spec:195: "the original moment, then the follow-up". Concept:569: "the follow-up photo or memory that came later". The data model has no link between photos (Proposal:86–99). Is the follow-up only the reflection stack? Affects S-17.
30. **Positivity Feed rules.** (a) Which tags qualify: only the drafted list (Spec:207), or free text too (Proposal:222 "slow is still forward"; Proposal:324 "tests a tag that isn't on the drafted list")? (b) Can it filter by chapter, as Spec:205, Concept:467 and Concept:614 ("filterable by phase") suggest, when Spec:202 names only endurance and gratitude tags? (c) In what order, since "never by popularity" (Spec:202) names no other? (d) Does a photo set Public enter before its reveal is finished? Affects S-09.
31. **Profile picture.** It is a User property (Spec:13), but "Nothing on a profile signals how the person looks" (Spec:29; Brief:113). What may it show, when is it set, and can it change? Only the name is immutable (Proposal:45, Proposal:61). Affects S-11, S-05, S-16.
32. **Invitation and onboarding.** Invitation is "the main arrival path" (Spec:28), but no invitation step is described. No onboarding beyond sign-up is described either. Affects S-10.
33. **Finding a user.** Tagging any user (Spec:163, Spec:267) and visiting profiles on day one (Spec:30) both need a way to find a person. No search or directory is described. Affects S-18, S-16.
34. **App entry.** Which screen opens the app in each time state? Only the new user's day one is stated (Spec:30). Concept:438–444 names Feed, Layers and Profile as the architecture but no entry point. Affects S-01, S-03, S-05, S-07, S-08, S-09.
35. **The prototype viewer.** Real authentication is out of this build (Plan:228), but the access matrix needs the demo to be seen as each fixture user (Proposal:305–313). How the demoer switches viewer, and whether T-01 shows the simulated date, are not specified. Affects S-10, T-01.
36. **The map's detail.** Does the owner's map show past years' rings or drift, or the number of shared photos (Proposal:150: "The owner's current map is the latest entry per member"; Concept:407 on reflecting on drift)? A count may fall under "No streaks, counters" (Brief:42). Affects S-07.

---

## Index of weighted moments `[copy: copywriter]`

The Commit moment and button (S-01). The capture refusal and the no-retake line (S-02). The sealed state (S-03). "Your Journey is ready" and the reveal (S-04). The young circle (S-05). Finding yourself in someone's hard year (S-06). Drift, and the empty map (S-07). The three announcement lines (S-08). The Positivity Feed's purpose (S-09). The arrival (S-10). "A name from within" (S-11). The note offer and skip (S-12). Starting a highlight, and its refusal (S-13). A reflection is final (S-14). The overview prompt (S-15). Manual tagging (S-18). The tone of chapters (S-19). "Readable, not commentable" and final choices (S-20). Finishing the reveal (S-21).
