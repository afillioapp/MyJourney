# My Journey — Functional Spec

Build reference. Every behaviour below traces to a decision in `My-Journey-Concept.md`. Anything not decided is in section 20, marked as blocking or not. Nothing here is invented to fill a gap.

Last updated: 2026-11-09

---

## 1. Core objects

| Object | What it is | Key properties |
|---|---|---|
| **User** | A person with an account | Name (from within, not physical attributes), profile picture, circle (rings = years), layers, journeys |
| **Journey** | One year of a user's life | Type, commit date, unlock date (12 months on), frame quota, highlights allowance, overview, visibility defaults. Frames used and highlights used are never stored, and state is derived, never stored: sealed / revealing / revealed (`Phase-1-Proposal.md` §2.1–2.2) |
| **Photo** | One sealed moment | Image, captured-at timestamp, unlock date (its journey's, §20 A), handwritten note, reflections, people tagged, visibility |
| **Handwritten note** | A photographed A4 page | Image, belongs to exactly one photo, written once |
| **Reflection** | A typed entry on one photo | Text, written-at date, year index, immutable |
| **Journey overview** | A typed entry on a whole journey | Text, year, immutable |
| **Highlight** | An unlimited-capture window | Start, end, photos captured inside it |
| **Tag** | Chapter (fixed category) or feeling (free text) | Applied at reveal |
| **Layer** | A ring of closeness around a user | Computed yearly from crossing journeys |

---

## 2. Account and onboarding

- Open signup. Anyone can join. No invite gate
- Invitation is the main arrival path but not a requirement
- User name comes from within, not from physical or earthly attributes. Nothing on a profile signals how the person looks or how well they are doing
- New users have no sealed content to view and no path yet. Their day-one experience is the Positivity Feed and other people's profiles

---

## 3. Journey setup and Commit

The user picks one of three types and presses Commit, on any day. The journey runs 12 months from that date (§20 C):

| Type | Difficulty | Cadence | Photos/year | Highlights |
|---|---|---|---|---|
| Explorer | Easy | 4 photos monthly | 48 | 4 |
| Wanderer | Normal | 2 photos monthly | 24 | 2 |
| Contemplator | Hard | 1 photo monthly | 12 | 1 |

- Pressing **Commit** locks the choice. It cannot be changed for that year
- The word Commit is deliberate and carries the weight
- No default type is pre-selected
- Each step halves the one above: 48, 24, 12

---

## 4. Capture

- Photo must be taken inside the app, at the moment
- Three taps. No tagging, no writing, no choices
- **No retakes.** Whatever was captured is the photo
- No quality bar. Bad lighting and bad composition are accepted
- Photos only. No video
- Sealed automatically at capture. Never a later decision about inclusion
- Counts against the journey's quota

---

## 5. Highlights

- A highlight is a limited window in which the frame limit does not apply
- Allowance by type: Explorer 4, Wanderer 2, Contemplator 1
- Explorer's four are described as one per season

---

## 6. The sealed year

- The whole journey is locked and unlocks once a year, as a single event. Photos do not open individually
- Nothing in a sealed journey is visible: not to the user, not to anyone
- No previews, no counts of what is inside, no thumbnails
- The user's engagement during this period is other people's unlocked journeys, not their own

---

## 7. Reveal

When a journey unlocks, this is the single engagement moment of the year. The user:

1. Writes reflections on photos
2. Tags the people in each photo, by hand
3. Applies the chapter tag and any feeling tags
4. Writes the journey overview
5. Sets visibility
6. Optionally orders the physical album (the album phase)

Layers are recalculated at this point, never during the sealed year.

---

## 8. Reflect

- One reflection per photo, per year
- Written only once the journey has unlocked, in yearly slots counted from the unlock date (§20 D)
- **Immutable.** No edits, ever. A new reflection is added instead, in the next slot, which opens on the journey's unlock anniversary
- **No comments from others.** Others may read; only the owner writes
- The window is generous: each slot stays open for a full year, and all photos of a journey move to their next slot together, on the journey's unlock anniversary (§20 D)
- The user is never pushed or reminded to write one

Example stack on one photo, in a journey committed 1 Sep 2018 that unlocks 1 Sep 2019:

| Event | When |
|---|---|
| Photo captured | 7 Jan 2019, sealed until 1 Sep 2019 |
| First reflection | Any time in slot 1, 1 Sep 2019 to 1 Sep 2020 |
| Second reflection | Any time in slot 2, 1 Sep 2020 to 1 Sep 2021 |
| … | one slot per unlock anniversary, indefinitely |

---

## 9. Journey overview

- One per journey, per year
- A new one every year on each journey, stacking, in the same yearly slots as reflections. Readable by the owner's network (§20 E). Optional (§20 O)
- Covers how the user's views changed across that year
- Immutable, like everything else
- Stacks across years so a user can read five overviews back to back

---

## 10. Tagging

**People** — tagged by hand at reveal. **No face recognition**, ever. This is deliberate manual work.

**Chapter tags** — fixed categories supplied by the product, organised under ME → ME, ME → YOU, ME → IT. One per journey.

**Feeling tags** — free text written by the user, inside a category. Popular ones surface over time and the best get promoted into official categories.

All tags are applied at reveal, never at capture.

Tone rule: tone shifts with the chapter, but even through hard chapters it stays positive and hopeful.

---

## 11. Visibility and access

Set **per photo**, chosen at publish time, not at capture.

| Level | Who sees it |
|---|---|
| Private | Only the owner |
| Network | The owner's friends: people who accepted a friend request (§20 KKKK; before 2026-11-09, everyone in the owner's layers) |
| Public | Anyone. This is the pool the Positivity Feed draws from |

- Opening someone's profile gives access to their journey
- Close friends are a list the owner chooses from among their friends (§20 KKKK, replacing the ring part of §20 H). Whether they see anything more than other friends is open (Decisions-Needed E2)
- Network is the default until the owner chooses, and choices lock when the reveal is finished (§20 F)
- Public means **readable, not commentable**

---

## 12. Layers

- The user is the **core**. Closeness radiates outward in concentric rings
- Visual reference: the Apple Watch app menu, not a list
- **Earned, not chosen.** Computed from crossing journeys: the people a user tags by hand in their own photos
- Three rings: tight (5+ shared photos in a journey), middle (2–4), outer (1). A tag puts the tagged user on the tagger's map only (§20 G)
- Computed when a reveal is finished. Recalculated with every journey
- Any user counts, whether or not they have a journey. Typed names never count
- **A person is never shown which layer they are on.** Each user sees only their own map
- Drift outward is expected and is treated as a feature, not a failure. A journey with no crossing moves someone out one ring. Nobody ever drops off the map

---

## 13. The feed

Announcements only. No photographs in the stream. It fires on exactly three events:

1. A user launches their journey
2. A user leaves a reflection
3. A path has crossed with a friend

Navigating to someone's journey should take a small deliberate act. It must not be as effortless as scrolling.

---

## 14. Profile

- The destination. Where a journey is actually read
- **The circle** frames the profile picture
- One **ring** per year with the app. A record, not a rank: no scores, no levels, no leaderboard, no badges, no comparison between users
- The year's **activity line** is twisted into the circle at the end of the journey, so the linear year becomes a ring
- **The activity graph appears only after the year unlocks.** Never during the sealed year. A visible grid being filled is a streak mechanic and is banned

---

## 15. Walking a path

- A person's journey is read from the beginning to now, in order, not as a grid
- The reader sees the hard times, then the reflection written later
- A single photo can be followed forward: the original moment, then the follow-up
- The reader sees where they themselves appear in that person's journey *(2026-11-10, §20 NNNN: the app never marks it. A reader may recognise themselves in a photo they can read, but is never shown which photos they are tagged in)*

---

## 16. The Positivity Feed

- Filtered by tags of endurance and gratitude, never by popularity
- Fed only by journeys set to public
- Primary use: someone having a bad day reads reflections written years later on other people's hard moments
- Lets a user find someone who was where they are now, one year or five years ahead

Feeling tags currently drafted: hang in there · it eventually pays off · thankful · gratification · worth it · I almost quit · the hard part was the start · worried for nothing

**Capturing low points** is invited, never nudged. The app does not prompt anyone to document a bad moment.

---

## 17. Album and print — the album phase

- Two photos per page
- Thick tactile pages, classic prints, a thin plastic sheet over the photographs
- Handwritten names beside people, never tags or handles
- The handwritten note printed on the back of or beside its photo
- Print-shop ritual: photos printed and cut in front of the user, album assembled there
- The hassle is deliberate

---

## 18. Rules the system must enforce

| Rule | Enforcement |
|---|---|
| No retakes | The capture screen offers no retake, no review-before-save |
| No edits to reflections | Reflections are append-only at the data layer |
| No comments | There is no comment object on a photo |
| No face recognition | No face detection anywhere in the pipeline |
| No ads | No ad surface exists |
| No streaks | No visible counters, no progress bars, no reminders during the sealed year |
| Sealed means sealed | Sealed content is unreadable by the owner, not merely hidden in the UI |
| Layer invisibility | No endpoint returns which layer a viewer sits on in someone else's map |
| Low usage is the goal | No re-engagement notifications of any kind |

---

## 19. What the system must never do

- Remind a user to capture, reflect, or return
- Show a count of how much of their quota is left in a way that reads as a target
- Rank users against each other
- Let anyone write on someone else's photo
- Reveal anything about a sealed journey, including its existence in detail
- Sell, train on, or transfer user memories

---

## 20. Decisions on what was undecided, and what is still open

### Two contradictions in the existing material

**A. Unlock — RESOLVED 2026-10-25.** The **whole journey unlocks once a year**, as a single event. Photos do not drip open on their own anniversaries. The reveal stays one annual moment.

**B. The handwritten note — RESOLVED 2026-10-25.** The note is an **optional second step after capture**. The photo is taken in three taps, then the app offers to add a handwritten note. Skippable, so capture stays fast and the moment is never held up.

### Mechanics — RESOLVED 2026-10-25

1. **Frames carry forward.** Each month of the journey (counted from the commit date) has its own limit, and unused frames carry forward to later months of the same journey. Whatever is unused when the journey ends is gone
2. **Cadence is per month of the journey**, with the carry-forward above. It's not a bare annual total
3. **No abandoning.** A committed journey always runs its full 12 months
4. **Highlights are started by the user**, whenever they choose, and last 24 hours. Explorer's "one per season" is a description, not a rule: all four can be used at any time
5. **A highlight is capped at the type's yearly quota** (Explorer 48, Wanderer 24, Contemplator 12). Its photos don't count against the journey's normal frames
6. **A photo can never be deleted**
7. **Tagging: users, or a name the owner types in.** Typed names never count towards crossings or layers
8. **One name, chosen once and kept.** It doesn't change yearly
9. **A reveal that's never finished:** the journey still unlocks on its date, and every photo stays Network (the default). There's no chapter, no tags, no "journey launched", and the layers aren't recomputed

### Also resolved 2026-10-25 (gaps found in Phase 1)

- **C. Journey timing.** A journey runs 12 months from its own commit date and unlocks then, as one event. Commit can be pressed on any day. One journey at a time: the next Commit is only possible once the current one has unlocked
- **D. Reflection slots.** All photos of a journey open together, on the journey's unlock anniversary. Slot *k* runs from unlock + (k−1) years to unlock + k years
- **E. Overviews.** A new overview every year on each journey, stacking. Readable by the owner's network
- **F. Visibility.** Network is the default, until the owner chooses. Reflections follow their photo's visibility. Reveal choices (visibility, people tags, chapter, feeling tags) lock when the reveal is finished
- **G. Layers.** A tag puts the tagged user on the tagger's map only. The tagged person's map doesn't change. Any user counts, whether or not they have a journey. Private photos count. Three rings: tight 5+ shared photos, middle 2–4, outer 1. A journey with no crossing moves someone out one ring, and nobody ever drops off the map
- **H. Close friends** are the innermost ring *(ring part superseded 2026-11-09 by KKKK: close friends are now chosen from among friends)*. They see nothing beyond the rest of the network *(reopened 2026-11-09: the user wants close friends to get something extra, not yet chosen, Decisions-Needed E2; meanwhile provisional default B55)*, and Private stays owner-only
- **I. Sealed journeys.** Others may know only that one exists
- **J. Feed.** "Journey launched" goes out when the reveal is finished. "Reflection left" reaches only people who can see that photo. "Path crossed" goes out for every crossing
- **K. Handwritten note.** It can be added up to 15 minutes after capture, never after
- **L. Ring changes.** Someone crossed again with fewer photos goes straight to the ring that count gives. The one-ring drift only applies when they aren't tagged at all
- **M. Feed audience.** "Journey launched" and "path crossed" are shown to the owner's network
- **N. One highlight at a time.** Starting one while another is open is refused
- **O. Overviews are optional**, like reflections. A reveal can be finished without one
- **P. Each reveal choice is set once**, even before the reveal is finished

### Resolved 2026-10-30 (Screen Inventory audits)

- **Q. The Positivity Feed is text only.** Each entry is a reflection's text. A photograph is shown only when the reader opens one entry. "No photo feed" covers the Positivity Feed (Decisions-Needed B9 (a), Rubric G-8)
- **R. Public before the reveal is finished.** Under B2's "only after reveal finished" setting, no one but the owner reads the journey until the reveal is finished, including photos already set Public (Decisions-Needed B2)
- **S. An open highlight, to the owner.** While a journey is sealed, the owner sees the plain fact that a highlight is open, with no end time and no countdown. This holds over B19's "nothing else" (Decisions-Needed B6, B19)

### Resolved 2026-10-30 (Phase 1 gate check, `docs/reviews/2026-10-30-gate-1.md`)

- **T. Who reads a journey's type, dates, chapter and feeling tags after unlock.** The owner and the owner's network, never public, the same as the journey overview (gate-1 U1)
- **U. Capture during a highlight.** A photo goes into the open highlight first. Once the highlight is full, capture uses a normal frame if one is left, otherwise it refuses (gate-1 U2)
- **V. The prototype clock.** Simulated time runs at real speed from the last jump, so a note window or highlight closes on its own. Small jumps for testing edges are allowed (gate-1 U3)
- **W. The drafted tag list for the Positivity Feed** is the four working tags: gratification, it eventually pays off, hang in there, thankful (`My-Journey-Concept.md:454–459`; Decisions-Needed B9 (c); gate-1 U4)

- **X. Type, dates and tags under B2's "only after reveal finished" setting.** The network reads a journey's type, dates, chapter and feeling tags from unlock, as under §20 T. Only photos (and what follows them) wait for the reveal to finish (Phase-1-Amendments OQ-10)
- **Y. No chapter filter on the Positivity Feed.** §20 T wins: chapters are never public. Replaces Decisions-Needed B9 (d) (Phase-1-Amendments OQ-11)
- **Z. Option switches live in the database.** One `prototype_option` row holds the six switches *(three since 2026-11-10: B11, B12 and C6 are fixed by §20 NNNN)*, changed only through `set_option()` (Phase-1-Amendments O3, approved; a model change)
- **AA. Highlight rows are sealed**, owner included. The owner learns only yes/no "a highlight is open" through one owner-only function (Phase-1-Amendments O4, approved; a model change)

- **BB. Scripted fixture actions happen at 12:00 UTC** on their dates, away from the 00:00 UTC unlock instant (gate-1 r2 B-1)
- **CC. The Positivity Feed may select journeys by feeling tag**, but never shows the tag to a public reader: they see reflection text only (gate-1 r2 NB-15)
- **DD. Whether a photo was taken in a highlight** (`photo.highlight_id`) is readable by the owner only, also after unlock (gate-1 r2 NB-13; matches Decisions-Needed B24)
- **EE. Only the prototype panel moves time or flips switches.** `clock_jump()`, the jump to the next unlock and `set_option()` are callable only by a separate panel role, never by the acting viewer (Phase-1-Amendments OQ-16)
- **FF. `viewer_in_network()` may stay directly callable.** It reveals nothing beyond what §20 T journey rows already give a network member (Phase-1-Amendments OQ-17; Rubric R-070)
- **GG. Readers other than the owner see a photo's capture date, never its time.** The owner sees the full time (Screen-Inventory OQ-45)
- **HH. The journey overview waits too.** Under B2's "only after reveal finished" setting, the network reads the overview only once the reveal is finished (§20 X "what follows them")
- **II. The loader and the tests run as the panel role** and act as a user only through a one-way switch to the app role; the app role can never become the panel role (Phase-1-Amendments §2.1, approved)
- **JJ. Same-day photos, for a non-owner, carry no time order.** They are shown in a fixed order that carries no time information, and photo ids are not sequential across users (Phase-1-Amendments OQ-18; Screen-Inventory OQ-46)
- **KK. Time and location metadata are stripped from images at capture** (Phase-1-Amendments OQ-19)
- **LL. A non-owner never sees when a note was written**, not even the date. The owner sees the full time (Screen-Inventory OQ-46)
- **MM. Database statistics never leak activity.** The app role cannot read catalog statistics or row estimates that would show capture into a sealed journey (Phase-1-Amendments OQ-20; strictest option)
- **NN. The database refuses an image that still carries time or location metadata**, as a second guard behind stripping at capture (§20 KK)
- **OO. Every table with user content is read only through definer readers with fixed row estimates**, not only sealed content (Phase-1-Amendments OQ-21)
- **PP. A metadata refusal never reaches the user.** The app strips before saving; a refusal is a bug. One press is one photo, never a retake (Phase-1-Amendments OQ-22)
- **QQ. Capture stores baseline JPEG**; the strip step re-encodes to it (Phase-1-Amendments OQ-23)
- **RR. The query-timing residual is accepted for now** and revisited before real users (Phase-1-Amendments OQ-24)
- **SS. Whether a reveal is finished** (`journey_reveal`) is readable by the owner and the owner's network after unlock, never public, as §20 T (Phase-1-Amendments OQ-25 b)
- **TT. A user's join date** (`joined_at`) is readable by that user only; everyone reads names (OQ-25 a)
- **UU. A user's own announcements.** As the model carried it (Phase-1-Amendments OQ-25 c; R2 covers launched and crossed): a user sees their own "reflection left", not their own "journey launched" or "path crossed" (OQ-25 c)
- **VV. If the metadata guard refuses anyway (a bug)**, the app strips again and saves that moment once; the stored time may be slightly later. One press is still one photo (Phase-1-Amendments OQ-26)

*SS–VV above were ruled on 2026-10-31; WW–ZZ below also 2026-10-31.*

- **WW. Rings under B4's "per year with the app" option show only on the user's own profile.** Others see one ring per finished reveal, so TT holds (gate-1 r5 NB-24)
- **XX. The guard-bug retry is judged and stamped at the original press instant**, so the press always gives the photo it would have given (gate-1 r5 NB-25)
- **YY. No profile picture.** The field stays unused, as Decisions-Needed C7 (gate-1 r5 NB-26)
- **ZZ. SS means the reveal state is never shown or readable as a field to a public reader.** A public reader may infer it from the Positivity Feed, rings and photos appearing (Rubric G-23)
- **AAA. The press instant wins.** A guard-bug retry is stored at the original press instant (XX). VV's "the stored time may be slightly later" is retired (Screen-Inventory OQ-48)
- **BBB. The Positivity Feed sorts newest reflection first**, by the reflection's written time (Phase-1-Amendments OQ-28)
- **CCC. Public viewers get a ring count only**: one reader returns the number of finished reveals for a profile, and nothing else, no dates (Phase-1-Amendments OQ-29)
- **DDD. If stripping fails twice for one press**, the user sees nothing different; that press gives no photo and the bug is logged. No error, no "try again" (Phase-1-Amendments OQ-27; Screen-Inventory OQ-47)
- **EEE. Inferring dates is allowed.** §20 T means journey dates are never shown or readable as fields to a public reader; narrowing them from capture and reflection dates the reader can already see is allowed, as ZZ (Phase-1-Amendments OQ-30)
- **FFF. The bug log stays id-free**, and the trusted-code gap (a product connection changing a log setting) is accepted alongside OQ-12, to fix before real users (Phase-1-Amendments OQ-31)
- **GGG. After a press is lost (DDD)** ~~the camera returns as after any press, with no note offer~~ (note-offer part retired by JJJ); no frame or highlight place is used, because nothing was stored (Phase-1-Amendments OQ-32 a; Screen-Inventory OQ-50)
- **HHH. The note step retries like capture**: strip again and save once at the original instant; if it fails twice, nothing is shown and the bug is logged (Phase-1-Amendments OQ-32 b)
- **III. A note lost twice ends the note step**, as after a page taken. Nothing offers it again, so there is no re-shoot (gate-1 r6 NB-27)
- **JJJ. After a lost press the screen looks exactly like a normal press, note offer included (DDD wins over GGG's "no note offer", which is retired).** A note written for a lost press has no photo to attach to and is quietly discarded; nothing invites a second press. No frame or highlight place is used (Rubric G-24)
- **KKK. A public reader may see the order of journeys on a path.** EEE covers it; no dates are shown as fields (Screen-Inventory OQ-44)
- **LLL. The note step finds its photo through a server-side handle**: `capture()` gives the server route a one-time handle for that photo, valid for the note window, never exposed to the device as a photo id. No model change to P1:49's accepted/refused result as seen by the user (Phase-1-Amendments OQ-33)
- **MMM. III is enforced by the server route only**; the database stores nothing about a lost note. Accepted alongside OQ-12, revisit before real users (Phase-1-Amendments OQ-34)
- **NNN. After a lost press the note step closes 15 minutes after the press**, exactly as after a real photo (Screen-Inventory S-12 reading, confirmed)
- **OOO. `joined_at` is set to `app_now()` at join**; nobody can back-date it. The loader joins each user at the right simulated time (Phase-1-Amendments OQ-5)

- **PPP. Note handles may be lost on a server restart** in the local prototype; that note step then ends early and nothing wrong is stored. Recorded as a residual next to OQ-12, solved before real users (Phase-1-Amendments OQ-35)

- **QQQ. A lost press looks like the normal press it would have been.** Whether the press would be accepted is judged first, at the press instant: if a normal press would be refused, the normal refusal shows; if it would be accepted, it looks accepted, note offer included (JJJ). Retires the "never computed" reading under GGG (Rubric G-25)
- **RRR. A note press answered "closed" after a server restart (PPP) looks exactly as when the note window has ended**: the note step is simply not offered. No message, no timer, nothing inviting another photo (rules r8 V2)

- **SSS. The gaps left by judging a press first are accepted for the prototype** (an unlogged strip fault on a refused press; trusted code testing acceptance without a frame; accepted-only log lines), on the "Before real users" list (Phase-1-Amendments OQ-36)
- **TTT. The note-save timing gap (about 5 ms) is accepted for the prototype**, on the "Before real users" list (Phase-1-Amendments OQ-37)
- **UUU. When the note window ends while the user is on the note screen, nothing on screen changes on its own.** The next note press is simply not taken and the step quietly ends (Screen-Inventory OQ-24 residual)
- **VVV. A saved note page shows no confirmation.** The step simply ends, as after capture, so a lost note looks identical (Screen-Inventory S-12)
- **WWW. Skipping the note step ends it for good**; no note can be added later in the 15 minutes (Screen-Inventory OQ-24)
- **XXX. Decisions-Needed C7 is decided in full**: no profile picture anywhere, the profile shows the owner's name in the circle, and announcements carry no image (Screen-Inventory OQ-49; extends YY)
- **YYY. The note window ends at unlock.** No note is added once the journey unlocks (reworded 2026-10-31; the reveal is unaffected); the note step ends then, and looks exactly like the window ending (UUU, RRR) (Rubric G-26)
- **ZZZ. A note lost twice gets the same answer as a saved note**, byte for byte, so nothing differs (VVV) (gate-1 r8 NB-31)
- **AAAA. The retry's timing gap on an image-check bug (10–21 ms) is accepted for the prototype**, on the "Before real users" list (Phase-1-Amendments OQ-38)
- **BBBB. Outside code that never sends the skip could still add a note in the window: accepted with OQ-12**, on the "Before real users" list. If the note step refuses after the route read the window as open, the device gets the one "closed" answer (Phase-1-Amendments OQ-39)
- **CCCC. At the unlock instant, capture and the note step end quietly.** Nothing changes on screen on its own (as UUU); the next press is not taken, and the app goes to the profile, where "Your Journey is ready" appears (Decisions-Needed C1). No refusal about frames (Rubric G-27)
- **DDDD. "Leaving capture" means moving to another screen inside the app.** Locking the phone, a call or the app going to the background do not end the note step; the 15-minute window and unlock still apply (Rubric G-28)

*AAA–DDDD above were ruled on 2026-10-31.*

- **EEEE. The unlock date is always shown as a plain date, never relative** ("in 64 days", "unlocks in", days to go). Decisions-Needed C2 is decided. What the sealed year shows besides it stays under B19 (Flows r3 V1)
- **FFFF. "Your Journey is ready" shows once, on the first open after unlock** (Decisions-Needed C18). Afterwards an unfinished reveal is reached by the plain way on the profile (Decisions-Needed B41). It is never a notification (Spec §18)
- **GGGG. The per-year ring timing in Decisions-Needed B28 is kept.** Under B4's "per year with the app", a year's ring is added at the join anniversary, or at the unlock of a journey sealed then, never inside a sealed year. Each finished journey's day marks go on the ring for the year that holds its reveal-finished date, and its flat graph stays for the owner until that ring is drawn. B4 itself remains a switchable provisional default
- **HHHH. "We want you here less, not more." belongs on the website**, the Phase 5 marketing site, not in the app's profile (Microcopy MQ-5). Rubric R-130 is met by the site. The app is not required to carry it in first-run copy

- **IIII. The newest ring is the thinnest and the brightest.** The thinning by age stays as drawn (Art-Direction AD-19); the newest ring is also drawn the brightest of the rings. It is how a ring looks by its place, never a marker that something is new, and it never reads as a level (Rubric R-096, R-185)
- **JJJJ. The way out of Start a highlight is back to the sealed year S-03**, after a refusal or when the owner decides not to start (Flows FQ-11). Starting one still leads to the camera S-02

- **KKKK. The network is made by friend requests; the map is made by tags** (Decisions-Needed E1; replaces the network part of Spec:146 and the ring part of §20 H). (a) A friend request must be accepted by both people. (b) Anyone can be tagged by typing their name: a user found by name, or a typed name for someone not on the app, which never counts towards layers, as now. (c) Requests arrive inside the app only, with no notification, no friend count and no "people you may know". (d) Someone on your map who is not your friend sees only your Public photos. (e) "Journey launched" and "path crossed" go to your friends. (f) Close friends become a list the owner chooses from among their friends, and are no longer the inner ring. The map keeps its three rings from shared photos and is still never shown to the person on it. Whether close friends see anything more than other friends is still open (Decisions-Needed E2). The approved data model needs an amendment before Phase 3 (lead-tech)

*EEEE–KKKK above were ruled on 2026-11-09.*

- **LLLL. No one can see another user's friends** (Decisions-Needed E4; confirms B56). Each user sees only their own friend, request and close-friends lists
- **MMMM. Users can block** (Decisions-Needed E5). How a block works follows the Instagram reference, within the banned list; the details are provisional defaults to be set when it is carried. A block is a new insert-only record, so it is a data model change, carried as a Phase-1-Amendments section (on paper until Phase 3). *Carried 2026-11-10: Phase-1-Amendments §15; Instagram-reference defaults Decisions-Needed B62–B68; whether a block touches the rings is with the user (E6, `PROVISIONAL: B69`)*

- **NNNN. No one can tell that they are on someone else's rings.** It is personal (Decisions-Needed E3). (a) "Path crossed" never names the person crossed (B11 fixed to unnamed). (b) A reader of a journey is never shown which photos they are tagged in, and never sees anyone's people tags (B12 fixed to hidden, C6 fixed to hidden). (c) A new friend never sees announcements from before the friendship (B48 confirmed). Restates §12 "a person is never shown which layer they are on" as covering whether they are on the rings at all. B11, B12 and C6 stop being prototype switches; removing them from `prototype_option` is a data model change this ruling requires

*LLLL to NNNN above were ruled on 2026-11-10. E2 (what close friends get) is deferred by the user; B55 stands until then.*

### Still open — can wait

1. Export and data ownership, which the trust position depends on
2. Age gating and parental consent, if teenagers are a target audience

---

## 21. Demo and fixture requirements

The product cannot be demonstrated without these, because nothing is visible until a year has passed.

- **A time control.** The prototype needs to jump forward a year or five. Without it there is no reveal, no reflection stack, no rings, nothing to see
- **Multi-year fixture users.** At least one user with five years of journeys so the ring system, the overview stack and the reflection stack are all visible
- **Crossing paths.** At least two fixture users who appear in each other's photos in some years and not others, so layers visibly shift and a path visibly crosses again after a gap
- **All three journey types** represented, so the cadence difference is visible
- **Mixed visibility.** Private, network and public photos, so the Positivity Feed has something in it and access rules can be tested
- **Reflection stacks of different depths.** A photo with one reflection, a photo with five
- **A sealed journey in progress**, so the empty state of the current year can be seen
