# My Journey — Master Build Prompt

Hand this to any agent or person working on the build. It is self-contained. Reference files in the same folder: `Functional-Spec.md`, `Build-Plan.md`, `My-Journey-Concept.md`.

---

## The one instruction that matters most

**Never invent a behaviour.** If something you need is not specified, stop and ask. Do not fill the gap with what a normal app would do, because almost every normal app behaviour is something this product has deliberately banned. A plausible guess here is worse than a blocked task.

---

## What you are building

A marketing website and a web app prototype, running on dummy data, for **My Journey**: a photo app where every picture is sealed the moment it is taken and the whole year unlocks exactly one year later.

The product is not about photographs. It is about what happens when time becomes part of the product.

Positioning: **not attention, intention.** Tone: self-recognition, self-progression, self-awareness.

The three jobs underneath it:

1. Keep hope alive through the hard times
2. Let people appreciate what they have done and achieved
3. Stop the overthinking and the worrying

The core message: **people do not see how far they have come.** The product is the proof against that, because you cannot argue with your own photo from a year ago.

---

## The banned list — read before you design anything

This product deliberately refuses things every other app does. Breaking one of these is a build failure, not a style disagreement.

| Never | Why |
|---|---|
| **No retakes** | The moment is gone. However imperfect, that is the photo |
| **No edits to reflections** | You never rewrite your past self. You add a new one |
| **No comments from anyone else** | The only voice on a photo is the owner's |
| **No face recognition** | People are tagged by hand, deliberately |
| **No ads, anywhere** | Ads need attention, which the product rejects |
| **No streaks, counters, progress bars, reminders** | Engagement mechanics are banned outright |
| **No re-engagement notifications** | We are not trying to get users onto the app |
| **No ranking, levels, badges or leaderboards** | The circle is a record, not a rank |
| **No photo feed** | The feed carries announcements only, never images |
| **Nothing leaks from a sealed year** | Not thumbnails, not counts, not "3 moments captured" |
| **No layer is ever shown to the person on it** | Each user sees only their own map |

**Low usage is the goal, and the product says so publicly.** If a decision would increase time in app, it is probably the wrong decision.

---

## How the product works

**Commit.** On any day, the user picks one of three journey types and presses **Commit**. The word is deliberate. Once committed, it cannot be changed or abandoned. The journey runs 12 months from that date. One journey at a time: the next Commit is only possible once the current one has unlocked.

| Type | Difficulty | Cadence | Photos/year | Highlights |
|---|---|---|---|---|
| Explorer | Easy | 4 photos monthly | 48 | 4 |
| Wanderer | Normal | 2 photos monthly | 24 | 2 |
| Contemplator | Hard | 1 photo monthly | 12 | 1 |

**Frames.** Each month of the journey has its own limit. Unused frames carry forward to later months of the same journey and lapse when it ends.

A **highlight** is a limited window where the frame limit does not apply. The user starts it whenever they choose, and it lasts 24 hours. Only one can be open at a time. It holds up to the type's yearly quota, on top of normal frames.

**Capture.** Inside the app, at the moment, three taps. No tagging, no writing, no choices, no retakes, no quality bar. Photos only, no video. Sealed instantly. A photo can never be deleted.

**The handwritten note.** Straight after capture the app offers an optional second step: write something by hand on a sheet of A4 and photograph it. It becomes the writing on the back of the photo. Skippable. Capture is never held up. The note can be added up to 15 minutes after capture, never after.

**The sealed year.** Nothing is visible, to anyone, including the owner. Others may know only that a sealed journey exists. During this time the user lives their life. When they do open the app, they read other people's unlocked journeys.

**Reveal.** The whole journey unlocks 12 months after Commit, as one event. This is the single engagement moment of the year. The user writes reflections, tags people by hand (users, or a typed name), applies tags, writes the year overview, and sets visibility. Each choice is set once, and everything locks when the reveal is finished.

**Reflect.** One reflection per photo, per year. Immutable and optional. All photos of a journey move to their next slot together, on the journey's unlock anniversary, forever. Each is a new layer, never an edit.

**The journey overview.** A new one every year on each journey: how the user's views changed. Also immutable, optional, stacking. Readable by the owner's network.

**Visibility.** Per photo: private, network, or public. Network until the owner chooses at reveal, because a year later you know how the year turned out. Reflections follow their photo's visibility.

**Layers.** The user is the core, closeness radiating outward in rings, like the Apple Watch menu. Layers are **earned by crossing journeys**: a tag puts the tagged user on the tagger's map only, and typed names never count. There are three rings: tight (5+ shared photos in a journey), middle (2–4) and outer (1). A journey with no crossing moves someone out one ring, and nobody drops off. Close friends are the innermost ring and see nothing extra. A friendship can drift outward, and two paths can cross again after years apart.

**The feed.** Announcements only, on three events: a journey launched (when its reveal is finished), a reflection left (only to people who can see that photo), a path crossed (every crossing).

**The profile.** The destination, where a journey is read. The circle frames the profile picture, gaining a ring each year. The year's activity line is twisted into that circle. The activity graph appears only after the year unlocks, never during it.

**The Positivity Feed.** Filtered by tags of endurance and gratitude. Someone having a bad day reads reflections written years later on other people's hard moments, and finds a person who was where they are now, a few years ahead.

---

## The thing that will sink this build if you skip it

Nothing in this product is visible until a year has passed. Build the **fixture data and a time control first**, before any screen.

Required fixtures:

- At least one user with five years of journeys
- Two users whose paths cross in some years and not others, so layers visibly shift and a path visibly crosses again after a gap
- All three journey types represented
- Mixed visibility: private, network, public
- Reflection stacks of different depths: one photo with a single reflection, one with five
- One sealed journey in progress, so the current-year empty state can be seen
- A control that jumps the clock forward a year or five

---

## Voice and look

- Nostalgic, 1970s to 90s family album, deliberately not modern-photo-book
- The circle is the identity system: the logo, the profile frame, the rings, the navigation
- "Circling back" is the product's phrase: we are all in a circle, going round and round
- Nothing should ask the user to perform
- Nothing on a profile signals how someone looks or how well they are doing

Lines that must appear, stated plainly and early:

- "It's not about attention. It's about intention."
- "You've come further than you think."
- "Strict at capture. Generous at reflect."
- "No retakes. That moment is gone."
- "This app takes time, like many other good things."
- "We want you here less, not more."

---

## Role briefs

**Lead Tech** — data model for the nine objects in the spec. Append-only wherever the rules demand it: reflections and overviews are never updated, only added. Owns the time control. Sealed means unreadable at the data layer, not merely hidden in the UI. The data model is approved in `Phase-1-Proposal.md`: build it, don't redesign it.

**UX** — flows, not visuals: Commit, capture, the note step, the sealed-year empty state, reveal, reflect, layers, profile, walking a path. The sealed-year empty state is the hardest screen in the product and the most important: it must feel intentional, not broken.

**Art Director** — the circle system and the nostalgic register. The rings, the activity line twisted into a circle, the album feel. Not a modern photo app.

**Fixture Designer** — the dataset above, now designed and approved in `Phase-1-Proposal.md` §3. This is a design job, not a data-entry job: the demo's emotional punch comes from two paths crossing again after years apart, and that has to be composed.

**Developer** — frontend and data layer. The marketing site is static and can be built in parallel. The app needs state.

**Content Manager and Copywriter** — the site carries the founder story, attention versus intention, the ritual, the reveal, the album, the relationships. State plainly and early that we are not trying to get users onto the app. Microcopy matters most at Commit, the sealed state, and "Your Journey is ready."

**Rules Guardian** — audit every screen against the banned list. This role exists because every banned item is something a competent designer would otherwise add by reflex.

**QA** — every flow at several points in simulated time. A flow that works today and breaks after a simulated year is a failed flow.

---

## Definition of done

- Every flow works against fixture data at several points in simulated time
- A rules audit returns zero findings
- Someone who has never heard of the product can use the prototype and explain the ritual back
- Nothing was invented to fill a gap. Every gap was asked about

---

## Still undecided — ask, do not assume

The mechanics questions were all decided on 2026-10-25. They're recorded in `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29. Two are still open:

1. Export and data ownership
2. Age gating and parental consent, if teenagers are a target audience

Anything else not written down anywhere is also undecided. Ask.
