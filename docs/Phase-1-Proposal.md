# Phase 1 Proposal: data model and fixtures

Status: **APPROVED 2026-10-25.** The data model, the fixtures and readings R1–R5 were all approved as written. No code written yet.
Date: 2026-10-25

This version folds in every decision made on 2026-10-25. They're listed in section 1 and recorded in `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29. The five readings in section 4 were approved too.

---

## 1. Decisions this proposal is built on

| # | Decision |
|---|---|
| D1 | A journey runs **12 months from its commit date** and unlocks then, as one event |
| D2 | Commit can be pressed **on any day** |
| D3 | **One journey at a time.** The next Commit is only possible once the current journey has unlocked |
| D4 | No abandoning. A committed journey always runs its full 12 months |
| D5 | Each **month of the journey** (counted from the commit date) has its own limit. Unused frames **carry forward** to later months of the same journey and lapse when it ends |
| D6 | The user starts a **highlight** whenever they choose. It lasts **24 hours** and holds up to the type's yearly quota (E 48, W 24, C 12). Its photos don't count against normal frames. All Explorer highlights can be used at any time |
| D7 | A photo can **never be deleted** |
| D8 | Note: can be added up to **15 minutes after capture**, never after |
| D9 | Reflection slots: **all photos of a journey open together**, on the journey's unlock anniversary. Slot *k* runs from unlock + (k−1) years to unlock + k years |
| D10 | A **new overview every year** on each journey, stacking. Readable by the owner's **network** |
| D11 | Reflections follow their photo's visibility |
| D12 | Visibility is **Network until the owner chooses.** Reveal choices (visibility, people tags, chapter, feeling tags) **lock when the reveal is finished.** If the owner never finishes the reveal, the photos stay Network |
| D13 | People tags: **users, or a typed name.** Typed names never count towards crossings or rings |
| D14 | A tag puts the tagged user **on the tagger's map only**. Any user counts, whether or not they've ever had a journey. Private photos count |
| D15 | **Three rings:** tight 5+ shared photos, middle 2–4, outer 1. A journey with no crossing moves someone **out one ring**. Nobody ever drops off the map |
| D16 | Close friends **are** the innermost ring. They see nothing beyond the rest of the network. Private is owner-only |
| D17 | Others may know **only that a sealed journey exists** |
| D18 | Feed: "journey launched" goes out when the reveal is finished. "Reflection left" reaches only people who can see that photo. "Path crossed" goes out for every crossing |
| D19 | One name, chosen once and kept |

---

## 2. Data model

### 2.1 Where the rules live

Postgres, local. The rules sit in the database itself: grants, triggers, row-level security and constraints. So they hold even when app code is wrong.

| Rule | Mechanism |
|---|---|
| Append-only reflections and overviews | The app role has INSERT and SELECT only. A trigger also raises on UPDATE, DELETE and TRUNCATE |
| Photo, note, journey, user name immutable | The same grant and trigger pair. No delete path exists anywhere (D7) |
| Reveal choices lock at finish (D12) | Visibility, people tags, chapter and feeling tags are insert-only. A trigger also refuses any insert once that journey's reveal is finished |
| One journey at a time (D3) | An exclusion constraint: no two journeys of one user may have overlapping `[committed_at, unlocks_at)` |
| Sealed means unreadable | (a) Row-level security: photo, note, tag and reflection rows are readable only once `app_now() >= unlocks_at`, **including by the owner**, so `count(*)` returns 0. (b) Image blobs are encrypted with a per-journey key that only one function releases, and only after unlock |
| No counters | `capture()` and `start_highlight()` return only `accepted` or `refused`. Frames used, frames left and highlights left are counted inside them and never stored or returned |
| Activity graph only after unlock | It's built from `captured_at`, which is unreadable while sealed |
| Layer invisibility | Layer rows are readable only where `owner = viewer`. Nothing callable takes a member and returns an owner |
| Only the owner writes on a photo | The reflection table has no author column. The insert function checks the caller owns the photo |
| No comments, likes, captions, ranks | These objects don't exist. A schema test fails if one appears |

### 2.2 The nine objects

**User**
| Field | Rule |
|---|---|
| id | |
| name | Set once, immutable (D19) |
| profile_picture | |
| joined_at | |

The circle is derived: one ring per journey whose reveal is finished. There is no stored counter.

**Journey**
| Field | Rule |
|---|---|
| id, user_id | |
| seq | 1, 2, 3… per user |
| type | explorer / wanderer / contemplator. Cadence, quota and allowance come from a `journey_type` constants table |
| committed_at | `app_now()` at Commit, any day (D2) |
| unlocks_at | Generated as `committed_at` + 12 months (D1) |

The row is immutable once inserted, which is what makes Commit final. Its state is derived, never stored:

| State | Condition |
|---|---|
| sealed | `committed_at ≤ now < unlocks_at` |
| revealing | Unlocked, reveal not finished |
| revealed | Reveal finished |

The spec's separate "committed" state collapses into sealed under D1. Others see only `has_journey_underway(user)`, a true/false (D17). The owner also sees type, commit date and unlock date. Nothing else.

**Photo**
| Field | Rule |
|---|---|
| id, journey_id | |
| captured_at | `app_now()`, set inside `capture()` |
| image | Sealed, encrypted blob |
| highlight_id | Nullable |

There's no caption, and no update or delete (D7). `capture()` accepts a photo in one of two cases:

- **Inside a highlight:** a highlight is open and it holds fewer photos than the yearly quota (D6).
- **Normal frame:** the journey's normal photos so far are below `cadence × current journey month` (D5, which gives carry-forward for free).

Otherwise it refuses. It only works on a sealed journey, so nothing can be captured after unlock.

**Handwritten note**
| Field | Rule |
|---|---|
| id, photo_id | `photo_id` unique: one note per photo at most |
| image | Sealed under the journey key |
| written_at | |

Insert-only, and only within 15 minutes of the photo's `captured_at` (D8).

**Reflection**
| Field | Rule |
|---|---|
| id, photo_id | |
| text, written_at | |
| year_index | Worked out from `app_now()` against `unlocks_at` (D9). Unique per (photo, year_index) |

Insert-only, owner only, any time after unlock (reveal finished or not). Readers are the same as the photo's (D11).

**Journey overview**
| Field | Rule |
|---|---|
| id, journey_id | |
| text, written_at | |
| year_index | Same windows as reflections. Unique per (journey, year_index) (D10) |

Insert-only. Readable by the owner and the owner's network.

**Highlight**
| Field | Rule |
|---|---|
| id, journey_id | |
| started_at | `app_now()` inside `start_highlight()` |
| ends_at | `started_at` + 24 hours, cut off at `unlocks_at` (D6) |

Only on a sealed journey, at most the type's allowance per journey.

**Tag**
| Kind | Shape |
|---|---|
| Chapter | `journey_chapter` (journey_id primary key, so one per journey) → catalogue (label, relationship) |
| Feeling | `journey_feeling_tag` (journey_id, free text) |

Both are insert-only during the reveal and locked at finish (D12).

**Layer**
| Field | Rule |
|---|---|
| owner_id, member_id, journey_id, ring (tight / middle / outer), computed_at | |

Computed when the owner finishes a journey's reveal (see 2.3). Readable only by the owner. The owner's current map is the latest entry per member.

### 2.3 How layers are computed

This runs when user A finishes the reveal of journey J:

1. For every **user** B tagged in J's photos (typed names and A themself excluded): count the J photos tagging B, private ones included. 5+ is tight, 2–4 middle, 1 outer. Write the entry and emit "path crossed" (D14, D15, D18).
2. For every B already on A's map who isn't tagged in J: move out one ring. Tight goes to middle, middle to outer, and outer stays outer (D15).
3. Emit "journey launched" (D18).

B's own map never changes because of A's tags.

### 2.4 Supporting records (not new product objects)

- **journey_reveal**: (journey_id primary key, finished_at). Insert-only, only after unlock. Its existence is what locks the reveal.
- **person_tag**: (photo_id, user_id **or** typed_name; exactly one is set). Insert-only during the reveal (D12, D13).
- **photo_visibility**: (photo_id primary key, private / network / public). No row means Network (D12). Insert-only during the reveal.
- **journey_type**: constants. **chapter**: catalogue seeded from Concept §15.
- **announcement**: (type limited to journey_launched, reflection_left and path_crossed; actor; subject; at). No media column, no count column. Who sees each one is worked out from visibility (see reading R2).
- **sim_clock** and **journey_key**.

### 2.5 Checks that ship with the schema

Each one fails the build:

1. UPDATE or DELETE on reflection, overview, note, photo, journey, user name or journey_reveal raises an error.
2. Inserting visibility, tags or chapter after the reveal is finished raises an error.
3. A second Commit while a journey is sealed raises an error.
4. Before unlock, as the owner, photos return 0 rows, `count(*)` returns 0 and blobs are ciphertext.
5. `capture()` and `start_highlight()` return no number.
6. A schema scan finds no comment, reply, like, reaction, caption, score, rank, streak, badge, view or follower.
7. As B, no layer row with owner ≠ B is readable. A tag by A never creates a row on B's map.
8. A typed-name tag never produces a layer row.
9. Announcements have no media column and only the three types.
10. Nothing outside the clock module reads the system clock.
11. No face or vision library appears in the dependencies.

---

## 3. Fixtures and time control

### 3.1 Time control

- **One clock:** `sim_clock`, read through `app_now()`.
- **Controls:** +1 day, +1 month, +1 year, +5 years, jump to the next unlock, reset to baseline. **Forward only.** To look at an earlier moment, reset and jump again.
- **On each jump, in this order:**
  1. Unlocks need nothing to run, since state is derived from the clock.
  2. Scripted fixture actions dated at or before the new time are applied.
  3. Layers are computed for every reveal finished since the last jump.
  4. Announcements are emitted.
- **Baseline: 2026-10-25.** The next interesting points are 2027-01-01 (Steady Lantern unlocks), 2027-04-12 (Second Wind unlocks) and 2027-06-05 (Open Hands unlocks).

### 3.2 Users

| Key | Name | Who | Joined (`joined_at`) | At baseline |
|---|---|---|---|---|
| lantern | **Steady Lantern** | Primary demo persona, ME → ME | 2021-01-01 | 5 revealed journeys, 1 sealed |
| wind | **Second Wind** | The friend whose path crosses again | 2021-01-01 | 5 revealed, 1 sealed |
| hands | **Open Hands** | Parent, ME → YOU | 2021-01-01 | 3 revealed, 1 sealed |
| round | **Long Way Round** | Founder, ME → IT. The main source for the Positivity Feed | 2021-01-01 | 3 revealed, 1 **unlocked but never revealed**, between journeys |
| light | **First Light** | Joined 2026-10-01 | 2026-10-01 | No journey. Can commit on any day during the demo (D2) |

*(amended 2026-10-30, gate-1 O5/O6/CF-1)* **`joined_at`, how each value was set.** The fixture constrains `joined_at` from above only: a user exists before their first Commit, and before anyone tags them. Upper bounds: Lantern 2021-01-01 (#1 commit), Wind 2021-03-15 (#1 commit), Hands 2023-06-01 (#1 commit, which is earlier than Round's tag at the #1 reveal on 2023-09-12), Round 2022-09-01 (#1 commit). Nothing in the fixture sets a lower bound except where the fixture's own timeline starts, 2021-01-01, its earliest dated row. So Lantern's value is fixed by the fixture (both bounds are 2021-01-01). Wind, Hands and Round are free within their range, and each takes **the earliest date the fixture allows, 2021-01-01. This is a fixture choice, not product behaviour.** Times are 00:00:00 UTC (NB-6, B16), so Lantern joins and commits at the same instant; joining must come first in the load order. A side effect: Open Hands is a user with no journey from 2021-01-01 to 2023-06-01, which covers most of Round #1 (2022-09-01 to 2023-09-01; see the D14 row in §3.4).

### 3.3 Journeys

Photos are normal frames, plus highlight photos where shown. P / N / U is the private / network / public split.

| User | # | Committed | Unlocks | Type | Photos | P / N / U | Chapter | Feeling tags | Reveal finished |
|---|---|---|---|---|---|---|---|---|---|
| Steady Lantern | 1 | 2021-01-01 | 2022-01-01 | E | 41 + 19 highlight | 32 / 23 / 5 | first year in a new city | the hard part was the start | 2022-01-16 |
| | 2 | 2022-01-01 | 2023-01-01 | E | 37 | 20 / 13 / 4 | first year in a new job | thankful | 2023-01-14 |
| | 3 | 2023-01-01 | 2024-01-01 | W | 22 *(0 in March, 4 in April: carry-forward)* | 10 / 7 / 5 | first year of job hunting | hang in there · worried for nothing | 2024-01-20 |
| | 4 | 2024-01-01 | 2025-01-01 | W | 24 | 12 / 9 / 3 | first year of starting over | worth it | 2025-01-11 |
| | 5 | 2025-01-01 | 2026-01-01 | C | 12 + **12 highlight** *(at the cap)* | 9 / 10 / 5 | first year living alone | slow is still forward *(free text)* | 2026-01-25 |
| | 6 | 2026-01-01 | 2027-01-01 | C | 9 so far | sealed | | | |
| Second Wind | 1 | 2021-03-15 | 2022-03-15 | W | 23 | 9 / 12 / 2 | first year after graduating | | 2022-03-30 |
| | 2 | 2022-03-20 | 2023-03-20 | W | 20 | 8 / 11 / 1 | first year in a new job | | 2023-04-02 |
| | 3 | 2023-04-02 | 2024-04-02 | E | 44 | 20 / 22 / 2 | first year in a new country | I almost quit | 2024-04-20 |
| | 4 | 2024-04-05 | 2025-04-05 | E | 39 | 18 / 19 / 2 | first year of a career change | it eventually pays off | 2025-04-19 |
| | 5 | 2025-04-10 | 2026-04-10 | W | 24 | 10 / 12 / 2 | first year in a new city *(moved back)* | worth it | 2026-04-26 |
| | 6 | 2026-04-12 | 2027-04-12 | W | 11 so far | sealed | | | |
| Open Hands | 1 | 2023-06-01 | 2024-06-01 | W | 24 | 14 / 10 / 0 | first year of marriage | | 2024-06-15 |
| | 2 | 2024-06-03 | 2025-06-03 | E | **48** *(quota hit)* + 30 highlight *(the birth)* | 52 / 24 / 2 | baby's first year | thankful | 2025-06-22 |
| | 3 | 2025-06-03 | 2026-06-03 | E | 46 | 28 / 16 / 2 | first year of parenthood | gratification | 2026-06-20 |
| | 4 | 2026-06-05 | 2027-06-05 | E | 17 so far | sealed | | | |
| Long Way Round | 1 | 2022-09-01 | 2023-09-01 | C | 12 | 2 / 2 / 8 | first year of a business | I almost quit · the hard part was the start | 2023-09-12 |
| | 2 | 2023-09-04 | 2024-09-04 | C | 11 | 1 / 2 / 8 | first year of rebuilding after a failure | it eventually pays off | 2024-09-15 |
| | 3 | 2024-09-05 | 2025-09-05 | W | 21 | 5 / 4 / 12 | the year a side project became real | worried for nothing | 2025-09-21 |
| | 4 | 2025-09-06 | 2026-09-06 | W | 24 | **all Network (default)** | none | none | **never, so far** |

Every month stays within cadence once carry-forward is counted, and every sealed "so far" count stays within `cadence × months elapsed`.

The sealed journeys are where the empty state can be seen. Long Way Round #4 shows a reveal that was never finished. Round still came back on 2026-09-10 to reflect on an older photo, but the journey just unlocked, every photo is visible to the network by default, there's no chapter and no "journey launched", and the map hasn't been recomputed.

Highlights:

| Journey | Window | Occasion | Photos |
|---|---|---|---|
| Steady Lantern #1 | 2021-07-17 10:00 → 2021-07-18 10:00 | Second Wind's graduation party | 19 |
| Steady Lantern #5 | 2025-08-09 09:00 → 2025-08-10 09:00 | Moving day | 12, the Contemplator cap |
| Open Hands #2 | 2024-06-18 06:00 → 2024-06-19 06:00 | The birth | 30 |

Photos are generated placeholders with the scene drawn into the image. Scene descriptions live in the fixture source only, never in a column.

### 3.4 Crossing paths

Each map counts only its owner's own tags (D14).

**On Steady Lantern's map, Second Wind:**

| Journey | Lantern's photos tagging Wind | Ring |
|---|---|---|
| #1 (2021) | 6 *(2 private, 3 network, 1 public; 4 inside the graduation-party highlight)* | **Tight** |
| #2 (2022) | 2 | Middle |
| #3 (2023) | 0 *(Wind emigrated)* | Outer, drifted |
| #4 (2024) | 0 | Outer, the floor |
| #5 (2025) | 5 *(Wind moved back)* | **Tight again: the path crosses again after two years** |

**On Second Wind's map, Steady Lantern:**

| Journey | Wind's photos tagging Lantern | Ring |
|---|---|---|
| #1 | 5 | Tight |
| #2 | 2 | Middle |
| #3 | 0 | Outer |
| #4 | 0 | Outer |
| #5 | 6 | Tight |

Other crossings, each placed to test something:

| Tagger → tagged | Journey | Tags | Result | Tests |
|---|---|---|---|---|
| Open Hands → Steady Lantern | Hands #2 | 2 | Lantern on Hands' map, middle | |
| Open Hands → Steady Lantern | Hands #3 | 3 | Still middle | |
| Steady Lantern → Open Hands | Lantern #4 | 1 | Hands on Lantern's map, outer | **Asymmetry**: each sits on a different ring in the other's map, and neither can see it |
| Long Way Round → Open Hands | Round #1 | 2 | Hands on Round's map, middle. Hands had no journey then | D14: any user counts |
| Open Hands → "Ava" (typed name) | Hands #2 | 41 | No layer row | D13 |
| Nobody → First Light | | | First Light's map is empty | An empty network |

Lantern's 2 private photos of Wind check that **being tagged doesn't give access**.

### 3.5 Reflections, overviews, notes

| Photo | Depth | Dates (slot) | Visibility |
|---|---|---|---|
| lantern-1, 2021-03-14, "first night in the new flat", with a note | **5** | 2022-02-02 (1), 2023-02-10 (2), 2024-02-12 (3), 2025-02-14 (4), 2026-02-20 (5) | public |
| round-1, 2022-11-08, "the empty office after the co-founder left", with a note | 4 | 2023-09-20, 2024-10-01, 2025-09-15, 2026-09-10 | public |
| wind-3, 2023-04-06, "arrivals hall" | 3 | 2024-04-20, 2025-05-01, 2026-04-15 | network |
| lantern-5, 2025-06-21 | **1** | 2026-01-18 | network |

Most other photos have 0–2 reflections.

**Overviews:** every revealed journey has one per slot it has passed through. Steady Lantern has 15 (journey #1 has 5, down to journey #5 with 1). Second Wind has 15, Open Hands 6 and Long Way Round 9 (4 + 3 + 2). Long Way Round #4 has none.

**Notes:** about one photo in three has a note, each written within 15 minutes of its capture.

### 3.6 Access matrix (at baseline)

| Viewer → content | Lantern #5 private | Lantern #5 network | Lantern #5 public | Round #4 (default Network) | Any sealed journey |
|---|---|---|---|---|---|
| Steady Lantern | yes | yes | yes | no *(not on Round's map)* | own: exists + type + dates only |
| Second Wind | no | yes | yes | no | exists only |
| Open Hands | no | yes *(outer ring is still network)* | yes | **yes** *(on Round's map)* | exists only |
| Long Way Round | no | no | yes | own | exists only |
| First Light | no | no | yes | no | exists only |

### 3.7 Positivity Feed

*(amended 2026-10-30, gate-1 O5/O6/CF-1)* The earlier list here did not follow from §3.3 (gate-1 CF-1). It is recomputed from §3.3 under these rules:

- **Tags:** the journey carries at least one of the four working tags: `gratification`, `it eventually pays off`, `hang in there`, `thankful` (Functional-Spec §20 W; Decisions-Needed B9 (c)). Other tags on the 8-item draft (`worth it`, `I almost quit`, `the hard part was the start`, `worried for nothing`) and free text do not qualify
- **Reveal finished** at baseline (B9 (f))
- **Per photo:** only that journey's photos set Public (B9 (b)). Entries are the reflections on those photos, text only (§20 Q)

Derivation, every journey in §3.3 at baseline 2026-10-25:

| Journey | Feeling tags | Working tag? | Reveal finished? | Public photos | In the feed |
|---|---|---|---|---|---|
| Lantern #1 | the hard part was the start | no | yes | 5 | no |
| Lantern #2 | thankful | **yes** | yes | 4 | **yes, 4** |
| Lantern #3 | hang in there · worried for nothing | **yes** (hang in there) | yes | 5 | **yes, 5** |
| Lantern #4 | worth it | no | yes | 3 | no |
| Lantern #5 | slow is still forward *(free text)* | no | yes | 5 | no |
| Lantern #6 | | | no (sealed) | | no |
| Wind #1 | none | no | yes | 2 | no |
| Wind #2 | none | no | yes | 1 | no |
| Wind #3 | I almost quit | no | yes | 2 | no |
| Wind #4 | it eventually pays off | **yes** | yes | 2 | **yes, 2** |
| Wind #5 | worth it | no | yes | 2 | no |
| Wind #6 | | | no (sealed) | | no |
| Hands #1 | none | no | yes | 0 | no |
| Hands #2 | thankful | **yes** | yes | 2 | **yes, 2** |
| Hands #3 | gratification | **yes** | yes | 2 | **yes, 2** |
| Hands #4 | | | no (sealed) | | no |
| Round #1 | I almost quit · the hard part was the start | no | yes | 8 | no |
| Round #2 | it eventually pays off | **yes** | yes | 8 | **yes, 8** |
| Round #3 | worried for nothing | no | yes | 12 | no |
| Round #4 | none | no | **no** (never finished) | 0 (all Network) | no |

The Positivity Feed draws on the public photos (and their reflections) of:

- Steady Lantern #2 and #3 (4 + 5 public photos)
- Second Wind #4 (2)
- Open Hands #2 and #3 (2 + 2)
- Long Way Round #2 (8)

That is 6 journeys and 23 public photos at baseline. All four working tags appear: `thankful` (Lantern #2, Hands #2), `hang in there` (Lantern #3), `it eventually pays off` (Wind #4, Round #2), `gratification` (Hands #3).

What the exclusions test: Steady Lantern #5's free-text tag is not on the list. Lantern #4 and Wind #5 (`worth it`), Lantern #1, Wind #3 and Round #1 (`I almost quit`, `the hard part was the start`) and Round #3 (`worried for nothing`) carry tags from the 8-item draft that are not working tags. Lantern #3 qualifies through `hang in there` even though it also carries `worried for nothing`. Round #4 is unlocked but its reveal was never finished, so nothing from it enters (B9 (f)). Private and Network photos of qualifying journeys never enter (B9 (b)).

The scripted future (§3.8) adds nothing: the Wind #6 and Hands #4 reveals script no feeling tags.

### 3.8 Scripted future (applied on jumps)

| Date | Action |
|---|---|
| 2027-01-01 | Steady Lantern #6 unlocks. **The reveal is left for whoever is demoing** |
| 2027-04-25 | Second Wind finishes the #6 reveal, tagging Lantern in 4 photos (middle). Writes a reflection on wind-3 and an overview |
| 2027-06-20 | Open Hands finishes the #4 reveal, tagging Lantern in 1 photo |
| never | Long Way Round's #4 reveal stays unfinished. At +5 years it's still Network-by-default |

No fake user commits a new journey after baseline. From 2027 on the world goes quiet, apart from whoever is demoing, and +5 years shows that honestly.

---

## 4. Readings — approved 2026-10-25

Each one followed from the decisions without being stated outright. All five were approved as written.

- **R1.** If someone is crossed again with a lower count, they move straight to the ring that count gives. For example, tight last year and 1 photo this year puts them on the outer ring. The one-ring drift only applies when they aren't tagged at all.
- **R2.** "Journey launched" and "path crossed" are shown to the owner's network, meaning everyone on the owner's map, per Concept §14 ("visible to the user's network").
- **R3.** Only one highlight can be open at a time. Starting one while another is open is refused.
- **R4.** Overviews are optional, like reflections. A reveal can be finished without writing one.
- **R5.** Reveal choices are set once each, even during the reveal. A visibility or tag can't be changed before finish either. This is the stricter reading of D12. The looser one would let the owner change choices freely until finishing the reveal.
