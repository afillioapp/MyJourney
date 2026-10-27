# My Journey — Functional Spec

Build reference. Every behaviour below traces to a decision in `My-Journey-Concept.md`. Anything not decided is in section 20, marked as blocking or not. Nothing here is invented to fill a gap.

Last updated: 2026-10-25

---

## 1. Core objects

| Object | What it is | Key properties |
|---|---|---|
| **User** | A person with an account | Name (from within, not physical attributes), profile picture, circle (rings = years), layers, journeys |
| **Journey** | One year of a user's life | Type, year, frame quota, frames used, highlights allowance, highlights used, state (committed / sealed / unlocked), overview, visibility defaults |
| **Photo** | One sealed moment | Image, captured-at timestamp, unlock date, handwritten note, reflections, people tagged, visibility |
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
- Each step halves the one above; the three sit on the old 24–48 range's ceiling, middle and floor

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
6. Optionally orders the physical album (phase 2)

Layers are recalculated at this point, never during the sealed year.

---

## 8. Reflect

- One reflection per photo, per year
- Written a year or more after the moment
- **Immutable.** No edits, ever. A new reflection is added instead, on the next anniversary
- **No comments from others.** Others may read; only the owner writes
- The window is generous: each slot stays open for a full year, and all photos of a journey move to their next slot together, on the journey's unlock anniversary (§20 D)
- The user is never pushed or reminded to write one

Example stack on one photo:

| Event | Date |
|---|---|
| Photo captured | 7 Jan 2019 |
| First reflection | 7 Jan 2020 |
| Second reflection | 7 Jan 2021 |
| … | one per anniversary, indefinitely |

---

## 9. Journey overview

- One per journey, per year
- Written at reveal
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
| Network | Everyone in the owner's layers |
| Public | Anyone. This is the pool the Positivity Feed draws from |

- Opening someone's profile gives access to their journey
- Close friends are the innermost ring. They see nothing beyond the rest of the network (§20 H)
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
- The reader sees where they themselves appear in that person's journey

---

## 16. The Positivity Feed

- Filtered by tags of endurance and gratitude, never by popularity
- Fed only by journeys set to public
- Primary use: someone having a bad day reads reflections written years later on other people's hard moments
- Lets a user find someone who was where they are now, one year or five years ahead

Feeling tags currently drafted: hang in there · it eventually pays off · thankful · gratification · worth it · I almost quit · the hard part was the start · worried for nothing

**Capturing low points** is invited, never nudged. The app does not prompt anyone to document a bad moment.

---

## 17. Album and print — phase 2

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
- **H. Close friends** are the innermost ring. They see nothing beyond the rest of the network, and Private stays owner-only
- **I. Sealed journeys.** Others may know only that one exists
- **J. Feed.** "Journey launched" goes out when the reveal is finished. "Reflection left" reaches only people who can see that photo. "Path crossed" goes out for every crossing
- **K. Handwritten note.** It can be added up to 15 minutes after capture, never after
- **L. Ring changes.** Someone crossed again with fewer photos goes straight to the ring that count gives. The one-ring drift only applies when they aren't tagged at all
- **M. Feed audience.** "Journey launched" and "path crossed" are shown to the owner's network
- **N. One highlight at a time.** Starting one while another is open is refused
- **O. Overviews are optional**, like reflections. A reveal can be finished without one
- **P. Each reveal choice is set once**, even before the reveal is finished

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
