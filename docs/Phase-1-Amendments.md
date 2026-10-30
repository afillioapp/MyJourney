# Phase 1 Amendments: gate-1 items O1–O4, and rulings T and U

Status: **2026-10-30: O1, O2 accepted (no model change). O3 APPROVED by the user (Spec §20 Z). O4 NOT approved: waiting on the user.** OQ-10 → Spec §20 X; OQ-11 → §20 Y; OQ-2, 4, 6, 7, 8, 9 and the extra jumps → Decisions-Needed B20–B26 (provisional). Owner: lead-tech.

This file amends `Phase-1-Proposal.md` (P1, approved 2026-10-25) without editing it. Where P1 needs a matching line, §7 lists it for the supervisor to apply once the amendments are approved. Every amendment is the smallest change that closes its gate item. Nothing here redesigns §2.

Sources: `docs/reviews/2026-10-30-gate-1.md` (GC), P1 §2–§3, `Functional-Spec.md` (FS) §20 Q–W (`FS:290–299`), `Decisions-Needed.md` (DN) provisional defaults, `Rules-Rubric.md` (RR). Stack: local Postgres 16 (decided 2026-10-30, DN D1). No deploy host is assumed.

---

## 0. Summary

| Item | Amendment, in one line | Rubric checks served | Changes the approved model? |
|---|---|---|---|
| O1 | `app_now()` = the last jump's instant plus the real time elapsed since then, frozen per transaction. One forward-only primitive, `clock_jump(interval > 0)`, reaches any exact instant. The panel gains small jumps | R-001, R-040, R-046, R-116, R-115, R-117, R-118, R-119, R-120, R-123; §2.5 check 10 | No. The panel's small jump sizes need user confirmation (OQ-1) |
| O2 | The fixture is loaded by replaying 2021–2026 through the real functions, as the app role, on a clock started at 2021-01-01. The result is kept as a template database. Reset clones the template. No role bypasses the rules and no row is ever deleted | R-117, R-120, R-002, R-003, R-119; P1:40 | No |
| O3 | One new supporting record, `prototype_option`: a single row with one column per switchable default (B2, B4, B5, B11, B12, C6), two allowed values each. RLS reads B2 (and C6, B11) from it | R-141, R-142, R-068, R-144, R-146, R-147, R-148, R-149 | **Yes. NEEDS USER APPROVAL** |
| O4 | Highlight rows join the sealed list at P1:48 (a), owner included. One owner-only function, `highlight_open(journey)`, returns true or false and nothing else | G-13, R-008, R-009, R-010, R-014, R-138, R-040, R-041 | **Yes. NEEDS USER APPROVAL** |
| §20 T | Journey, chapter and feeling-tag rows after unlock: owner and network only, never public. Before unlock, unchanged (owner: type and dates; others: `has_journey_underway()`) | R-008, R-009, R-063, R-068 | No. It records a decided ruling. P1 needs matching lines |
| §20 U | `capture()` runs in a fixed order: the open highlight if not full, else a normal frame if one is left, else refuse | R-040, R-043, R-038, R-138 | No. P1:94–99 needs a matching line |

---

## 1. O1: the clock reaches exact instants

### Problem

GC:63: P1's controls are +1 day, +1 month, +1 year, +5 years, next unlock and reset (`P1:194`). The rubric needs 2026-12-31 23:59:59 (R-001, `RR:55`), capture + 14:59, 15:00.000 and 15:01 (R-046, `RR:351–353`), highlight + 23:59 and + 24:01 and "2 hours before unlock" (R-040, `RR:314`), and "a date far from the real one" (R-116, `RR:860`). GC:56 (U3) asked whether the clock stands still between jumps. FS §20 V (`FS:298`) answers: "Simulated time runs at real speed from the last jump … Small jumps for testing edges are allowed."

### Amendment

**1.1 `sim_clock`.** P1:169 names the table but gives no columns, so this defines them without adding an object:

| Column | Rule |
|---|---|
| `sim_at` | The simulated instant set by the last jump |
| `real_at` | The real instant of that jump. NULL means **not started**: this is used only while the fixture is loaded and in the baseline template (§2) |

There is exactly one row (a boolean primary key fixed to `true`). The app role has no INSERT, UPDATE, DELETE or TRUNCATE grant on it. A trigger refuses INSERT, DELETE and TRUNCATE, and refuses any UPDATE that would make `app_now()` earlier than it was.

**1.2 `app_now()`.**

```
app_now() = sim_at                                          if real_at is NULL
          = sim_at + (transaction_timestamp() - real_at)    otherwise
```

- **Real speed (§20 V).** Between jumps, simulated time moves at real speed, so a note window or a highlight closes on its own.
- **One instant per transaction.** Every rule evaluated in one transaction sees the same instant. This is what lets a test land on an exact instant while the clock runs (1.4).
- **The clock module.** It is `app_now()`, `clock_jump()`, `clock_start()`, `clock_jump_to_next_unlock()` and the `sim_clock` trigger, and nothing else. These are the only places allowed to call `transaction_timestamp()` or any other system-clock function (§2.5 check 10, R-115). The R-115 scan uses this list as its allow-list.
- **UTC (B16).** All calendar arithmetic is done in UTC explicitly (`(t AT TIME ZONE 'UTC' + i) AT TIME ZONE 'UTC'`), never in the session time zone. `journey.unlocks_at` is generated this way. Postgres accepts that expression in a generated column, and gives 2028-02-29 → 2029-02-28 (R-118, B16) under any session time zone.

**1.3 Jumps (forward only).**

- **The primitive** is `clock_jump(d interval)`. It refuses `d <= 0`. It sets `sim_at = app_now() + d` (in UTC) and `real_at = transaction_timestamp()`, and leaves `real_at` NULL while the clock is not started.
- **Panel controls.** These are built on the primitive:
  - unchanged from P1:194: +1 day, +1 month, +1 year, +5 years, jump to the next unlock, reset
  - **added under §20 V:** +1 minute and +1 hour. *Proposed sizes; §20 V allows small jumps but names none (OQ-1)*
  - "+1 month" uses the same UTC month arithmetic as journeys, so it is clamped under B16. For example, 01-31 + 1 month gives 02-28
- **Jump to the next unlock** stays as P1:194 defines it: the global next `unlocks_at` after `app_now()`. DN C17 is still open and has no default.
- **Reset** is in §2.

**1.4 How tests reach exact instants.** Each test case runs in **one transaction**. Inside it, `clock_jump(target - app_now())` lands exactly on `target`, and later jumps are exact offsets. For example: capture, then `clock_jump('15 minutes')`, then add the note. That puts the note at capture + 15:00.000 exactly (B16: refused).

| Rubric need | How it is reached |
|---|---|
| R-001: 2026-12-31 23:59:59, then 2027-01-01 00:00:00 | `clock_jump('2026-12-31 23:59:59+00' - app_now())`, assert, `clock_jump('1 second')`, assert |
| R-040: highlight + 23:59 and + 24:01; start 2 h before unlock | `clock_jump('23 hours 59 minutes')`, then `clock_jump('2 minutes')`. Or jump to `unlocks_at - 2 hours` |
| R-046: capture + 14:59, 15:00.000, 15:01 | Exact offsets from the capture, in one transaction each |
| R-116: a date far from the real one | `clock_jump('5 years')` or more. The rules run as of the app clock |
| R-121: 2023-12-31 and 2024-01-01 | Exact jumps |

**1.5 Jump order under a running clock** (P1:195–199). A jump from `t0` to `t1` runs as follows:

1. Unlocks need nothing to run (unchanged).
2. Each scripted action (P1 §3.8) that has not been applied yet and is dated at or before `t1` is applied, in date order. For each one, the clock first jumps to the action's instant, if that instant is still ahead. The action then runs **through the same functions the app uses, as the acting fixture user**, so its rows carry the scripted times. Whether an action has been applied is read from the data (for example, Wind #6's `journey_reveal` row exists). No table records it.
3. Layers are computed when a reveal is finished, inside the finish function (P1:154). This satisfies P1:198 as well (GC NB-11).
4. Announcements are emitted by the same function, after the layer rows.
5. The clock jumps to `t1`.

If real-time running has already carried the clock past an action's instant, the action is applied at `app_now()` at the start of the next jump, which is late. The clock cannot go back. **Not specified; OQ-2.**

**Rubric served:** R-001, R-040, R-046, R-116 (GC:63), and R-115 (check 10), R-117, R-118, R-119, R-120, R-121, R-123.

**Model change:** none. P1:169 names `sim_clock` without columns. The extra jump sizes are within §20 V. P1 §3.1 needs matching lines (§7).

**Evidence (feasibility, throwaway database `mj_scratch_amend` on the local Postgres 16, since dropped):**

```
clock_jump(interval '-1 second')         -> ERROR: clock_jump: forward only
UPDATE sim_clock ... (as mj_app)         -> ERROR: permission denied for table sim_clock
two transactions 1.1 s apart             -> elapsed 00:00:01.103012
in one txn: start 10:00, +23:59          -> 2026-10-26 09:59:00+00 | open = t
            +2 minutes                   -> 2026-10-26 10:01:00+00 | open = f
jump to 2026-12-31 23:59:59              -> 2026-12-31 23:59:59+00 (exact)
generated unlocks_at, session tz Tehran  -> 2026-01-01 -> 2027-01-01 00:00:00+00; 2028-02-29 -> 2029-02-28
```

---

## 2. O2: loading the 2021–2026 fixture, and reset

### Problem

GC:64: `capture()` sets `captured_at = app_now()` (P1:90). Triggers refuse inserts after a reveal is finished (P1:46). The clock is forward-only from 2026-10-25 (P1:194, 200). So history cannot be inserted through the guarded path at baseline. A bulk insert by a role that bypasses the rules would create exactly what P1:40 says must not be needed. Reset (R-117) depends on the answer.

### Amendment: replay, with no bypass role

**2.1 Two roles.**

| Role | Used by | May do |
|---|---|---|
| `mj_owner` | Migrations and the reset script only. Never the app, never the loader | Owns the schema, functions and databases. Never writes a product row |
| `mj_app` | The app **and the fixture loader** | Exactly the grants in P1 §2.1 (`P1:44` "the app role"). No UPDATE, DELETE or TRUNCATE anywhere. Every rule applies to it |

The acting user is set per transaction (a session setting read by `viewer()`). The loader acts as each fixture user in the same way the C16 viewer switcher does. Acting as a user gives that user's rights and nothing more. A deployed build would need real authentication instead; OQ-12 records this, and it does not block Phase 3.

**2.2 Building the baseline.**

1. Create a fresh database from the migrations. `sim_clock` starts **stopped** at **2021-01-01 00:00:00 UTC**, the earliest fixture instant (`joined_at` of Lantern, Wind, Hands and Round, P1 §3.2 as amended 2026-10-30).
2. The loader (as `mj_app`) walks every fixture event in time order. For each: `clock_jump(event_at - app_now())`, then call the function the app would call, as that user:
   - join (each user before their first action; Lantern's join comes before Lantern's commit at the same instant, P1 §3.2)
   - `commit()`
   - `start_highlight()`, `capture()` (placeholder image) and the note within 15 minutes
   - after unlock: the visibility, person-tag, chapter and feeling-tag inserts
   - finishing the reveal, which computes layers and emits announcements (P1 §2.3)
   - reflections and overviews in their slots
3. Stop with `clock_jump` to the **baseline instant, 2026-10-25 00:00:00 UTC** (P1:200; the time of day is OQ-4). The clock stays stopped. Mark the database as a template (`myjourney_baseline`, no connections allowed).

The clock stays stopped during the load so that every fixture timestamp is exact (for example, commits at 00:00:00, NB-6). The prototype never runs on a stopped clock. §20 V governs from `clock_start()` on.

This answers the rest of GC:64:

- **Blobs of sealed journeys** are encrypted by `capture()` itself under the journey key, the same way as live captures. There is no load-only path (R-002).
- **Historical layers and announcements** are produced by the replay of each finished reveal. They are not inserted.
- **The fixture passes the guards as designed**, given the §20 U order (§6). Highlight photos must be captured inside their windows (P1 §3.3). Lantern #5 fills its highlight to 12. Hands #2's 48 normal photos fit its cadence. Round's 2026-09-10 reflection, made before any reveal is finished, is allowed by P1:117.

**2.3 Reset** (P1:194, R-117). The reset script runs as `mj_owner`:

1. Drop the working database.
2. `CREATE DATABASE … TEMPLATE myjourney_baseline`.
3. Call `clock_start()`. This sets `real_at` from NULL to now. `app_now()` reads exactly the baseline both before and after, so it is not a backward move.

No DELETE or TRUNCATE path exists on any product table. The panel's reset control reaches this script through the prototype's control process. The app role cannot call it.

**2.4 New check (proposed, for the rules-guardian to number).** These fail the build:

- the fixture loader opens a connection as anything other than `mj_app`
- the loader's source contains an INSERT, UPDATE, DELETE, COPY or TRUNCATE statement against a product table
- after load, the baseline differs from the P1 §3 expectations: the counts per journey, the §3.4 rings and the §3.6 matrix

**Rubric served:** R-117 (reset equals the baseline load), R-120 (stored times come from the app clock, including during the load), R-002 and R-003 (sealed at load), R-119, P1:40.

**Model change:** none. There is no new table or field. The roles follow P1:44's "app role". The template and reset script are infrastructure.

**Needs from the fixture-designer** (P1 §3, not this file):

- the exact instant of every event (NB-4, NB-6, generated with a fixed seed)
- the time of day of the scripted actions (OQ-15)
- the journey of Wind's 2027-04-25 overview (GC O6, still open per commit 0601bf5)

**Evidence (feasibility, throwaway databases, since dropped):**

```
template built with clock stopped at baseline; clone; clock_start()  -> 2026-10-25 00:00:00.002804+00 | journeys 1
clock_jump('5 years')                                                -> 2031-10-25 00:00:00.052772+00
drop working DB (force); clone template again; clock_start()         -> 2026-10-25 00:00:00.003424+00
```

---

## 3. O3: where the switchable defaults live, so the database can enforce B2

### Problem

GC:65: B2 changes who can read photos, and P1:48 enforces reading in RLS. P1 §2.4 (P1:162–169) has no record for the options panel, so the photo policy cannot follow the switch. Adding a record changes the approved model.

### Amendment: **NEEDS USER APPROVAL**

Add one supporting record to P1 §2.4:

**`prototype_option`**: exactly one row (a boolean primary key fixed to `true`). The settings are the ones in DN's "Provisional defaults in force" table. Each column is NOT NULL, checked to exactly its two settings (R-141: no "both", "auto" or free value), and defaults to the provisional default. Each carries a `PROVISIONAL: <ID>` comment (R-149).

| Column | Settings (first = default) | Who reads it |
|---|---|---|
| `b2` | `from_unlock` / `after_reveal_finished` | RLS on photo, photo_visibility and reflection (and on journey, chapter and feeling tags, subject to OQ-10) |
| `b4` | `per_finished_reveal` / `per_year_with_app` | App (the circle is derived) |
| `b5` | `owner_only` / `viewer_visible` | App (the activity graph) |
| `b11` | `named` / `unnamed` | The announcement read function (under `unnamed`, readers get no subject, R-146) |
| `b12` | `shown` / `hidden` | App (Walking a path) |
| `c6` | `hidden` / `shown` | RLS on `person_tag` for non-owners (strictest reading, R-148: absent from the data, not only the UI) |

- **Grants.** `mj_app` has SELECT on the row. Changes go only through `set_option(id, setting)` (SECURITY DEFINER). There is no INSERT, DELETE or TRUNCATE path.
- **Settings hold no user data,** so reading them leaks nothing (R-141 treats the panel as a data path under R-014).
- **One row for the whole prototype,** like the one clock (P1:193; one options panel, DN C16, R-141). The settings are not per viewer (OQ-7).
- **The B2 term in the photo read policy, for non-owners of an unlocked journey.** The policy reads the B2 setting from `prototype_option`:
  - when the setting is `after_reveal_finished`, the read is allowed only if a `journey_reveal` row exists for the journey (FS §20 R: Public photos included)
  - when it is `from_unlock`, the B2 term allows the read
  - the visibility, network and seal terms of P1:48 still apply in both cases
- **B4, B5 and B12** are enforced by the app, which reads the same row. They change no database grant.

**Alternative considered and rejected:** a per-session setting (`SET mj.b2 = …`). Any client can override it, so the database would not be enforcing B2.

**Rubric served:** R-141 (exactly two settings, starts on the default), R-142 and R-068 (B2 under both settings), R-144, R-146, R-147, R-148, R-149.

**Model change: yes**, one supporting record in §2.4. **NEEDS USER APPROVAL.**

**Evidence (feasibility):** `set_option_b2('both')` gives `ERROR: … violates check constraint "prototype_option_b2_check"`. `DELETE FROM prototype_option` as `mj_app` gives `ERROR: permission denied`. The row reads `from_unlock`.

---

## 4. O4: highlight rows sealed

### Problem

GC:66 and RR G-13 (`RR:1185`): P1:48 seals photo, note, tag and reflection rows, but not highlight rows. A readable `highlight` row exposes `started_at` and `ends_at`. DN B6 (`DN:25`) and FS §20 S (`FS:292`) allow the owner only the plain fact that "a highlight is open", with no end time and no countdown, and allow everyone else nothing (R-008, `RR:89–95`).

### Amendment: **NEEDS USER APPROVAL**

1. **Add `highlight` to P1:48 (a).** Highlight rows are readable only once `app_now() >= unlocks_at` of their journey, **the owner included**, so `count(*)` returns 0 before unlock. The RLS is FORCEd so that the table owner's connections are covered too. After unlock, the readers are the owner only (the strictest reading; OQ-8).
2. **One new callable: `highlight_open(journey_id) → boolean`.** SECURITY DEFINER:
   - It returns whether `started_at <= app_now() < ends_at` for some highlight of that journey.
   - **For the owner only.** For anyone else, and for a journey id that does not exist, it raises the same refusal. A non-owner therefore cannot tell another user's journey from no journey (R-008's comparison against First Light).
   - It returns no time, no count and no id.
3. `capture()` and `start_highlight()` read highlight rows internally (SECURITY DEFINER) and still return only `accepted` or `refused` (P1:49).
4. `photo.highlight_id` is a column of the photo row, which is already sealed (P1:48 a). After unlock it is as readable as the photo itself (OQ-8).

The window is half-open, `[started_at, ends_at)`, matching the journey interval at P1:47. At exactly `ends_at` the highlight is closed (OQ-9 asks for confirmation).

**Rubric served:**

- G-13
- R-008 (others learn nothing)
- R-009 (owner: type, dates and the bare "open")
- R-010 (a capture changes nothing that can be read)
- R-014 (every path)
- R-138 (the one DOM difference B6 allows)
- R-040, R-041 (the window, and one at a time)

**Model change: yes.** It changes the §2.1 sealing row (P1:48) and adds one function. **NEEDS USER APPROVAL.** There is no new table or field.

**Evidence (feasibility):**

| Step | Result |
|---|---|
| Owner, before unlock | `count(*)` from highlight = 0 |
| Owner, at 2026-12-31 23:59:59 | 0 |
| Owner, at 2027-01-01 00:00:00 | 1 |
| Another user, after unlock | 0 |
| `highlight_open(6)` as owner, at + 23:59 | `t` |
| `highlight_open(6)` as owner, at + 24:01 | `f` |
| `highlight_open(6)` as another user | `ERROR: refused` |

---

## 5. FS §20 T: who reads a journey's type, dates, chapter and feeling tags

Ruling (`FS:296`): after unlock, the owner and the owner's network, never public, the same as the overview (P1:126). Before unlock, P1:84 and B19 (`DN:38`) are unchanged.

| Row | Sealed (`now < unlocks_at`) | Unlocked |
|---|---|---|
| `journey` (type, `committed_at`, `unlocks_at`) | Owner: these three fields only (P1:84, B19). Others: only `has_journey_underway(user)` (D17) | Owner and network. Never anyone else |
| `journey_chapter` | None exist: it is insert-only during the reveal (P1:143). It is sealed by RLS anyway | Owner and network |
| `journey_feeling_tag` | Same as `journey_chapter` | Owner and network |
| `journey_overview` | (unchanged, P1:126) | Owner and network |

- **"Network"** means the users on the owner's current map (reading R2, `P1:381`).
- **Layer rows are readable only by their owner** (P1:51). So the policy uses a SECURITY DEFINER predicate, `viewer_in_network(owner_id)`. It answers only for the current viewer, returns a boolean, and never takes a member to return an owner (P1:51).
- **A reader of a Public photo who is not in the network** reads the photo row but no journey, chapter or tag row. `photo.journey_id` leads nowhere for them.
- **Under B2's `after_reveal_finished` setting,** FS §20 R (`FS:291`) and DN B2 (`DN:21`) say "no one but the owner reads it until the reveal is finished". Read strictly, that covers these rows too. **Confirm: OQ-10.**
- **Conflict, not picked:** DN B9 (d) (`DN:28`) gives the Positivity Feed, which public readers use, a chapter filter. FS §20 T (`FS:296`) says chapters are never public. **OQ-11.**

**Model change:** none. This records a decided ruling. P1 needs matching lines at P1:48, 84 and 143 (§7).

---

## 6. FS §20 U: the capture order

Ruling (`FS:297`): the open highlight first. Once it is full, a normal frame if one is left, otherwise refuse. `capture(journey_id, image)` runs as follows:

1. **Refuse** unless the caller owns the journey and `committed_at <= app_now() < unlocks_at` (P1:99).
2. **Lock the journey** for the transaction (`pg_advisory_xact_lock`), so that two concurrent captures cannot both pass a count.
3. **Highlight.** If a highlight of this journey is open (`started_at <= app_now() < ends_at`) and holds fewer photos than the type's yearly quota (48, 24 or 12), insert the photo with that `highlight_id`. Return `accepted`.
4. **Normal frame.** Otherwise, if the journey's photos with `highlight_id IS NULL` number fewer than `cadence × m`, insert the photo with `highlight_id` NULL. Return `accepted`. Here `m` is the current journey month (1–12).
   - Month *k* starts at `committed_at + (k − 1) months`, computed from `committed_at` each time (not chained), in UTC, clamped under B16. This gives the R-123 case: commit 2026-01-31, month 2 starts 2026-02-28, month 3 starts 2026-03-31.
5. **Otherwise** return `refused`. No number is returned or stored (P1:49, R-038, R-039).

Effects on the rubric:

- **R-040.** "+24:01 (treated as normal frame or refused)" (`RR:314`) is now settled by state: a normal frame if one is left, else refused.
- **R-043.** A 13th photo in a full Contemplator highlight goes to a normal frame if one is left. It is refused as a highlight photo either way, which matches `RR:333`.
- **Wording.** Updating R-040's wording is for the rules-guardian.

**Model change:** none. P1:94–99 needs a line that gives the order (§7).

---

## 7. Matching lines P1 needs (for the supervisor, once approved; not applied here)

| P1 line | Change | Carries |
|---|---|---|
| 48 | Add `highlight` to "photo, note, tag and reflection rows", and name `highlight_open()` as the owner's only view | O4 (approval) |
| 48 or a new §2.1 row | "Journey, chapter and feeling-tag rows after unlock: owner and network only, never public" | §20 T |
| 84 | After "Nothing else.", add: "After unlock, the owner and the owner's network read type and dates; never public (FS §20 T)" | §20 T |
| 94–99 | "in this order: inside an open highlight that is not full; else a normal frame; else refused (FS §20 U)" | §20 U |
| 143 | Add "Readable after unlock by the owner and the owner's network only (FS §20 T)" | §20 T |
| 169 | Add `prototype_option`. Give `sim_clock` its two columns | O3 (approval), O1 |
| 194 (§3.1) | Add the small jumps, the running clock (§20 V) and the replay order of 1.5 | O1 |
| §3 (new) | Load by replay and reset by template, per §2 here | O2 |

§3 is being edited by another agent at the time of writing. The §3 lines go through the supervisor.

---

## 8. Open questions (stopped, not guessed)

| # | Question | Blocks |
|---|---|---|
| OQ-1 | Panel small jump sizes. §20 V allows small jumps but names none. Proposed: +1 minute and +1 hour. Tests use `clock_jump(interval)` directly | The panel only. Not the schema |
| OQ-2 | A scripted action whose instant the running clock has already passed is applied late, at the next jump's starting `app_now()`. Accept? | Time control |
| OQ-3 | R-119 expects announcements "with times after the map entry". Both are written at the same instant inside the finish function. Read "after" as "not before"? | R-119 test wording (rules-guardian) |
| OQ-4 | Baseline time of day: 2026-10-25 **00:00:00 UTC**? P1:200 gives only the date | Fixture load, R-117 |
| OQ-5 | How is `joined_at` set: `app_now()` at join, or given? P1:63 is blank. The replay works either way: it jumps to 2021-01-01 and joins | Schema default |
| OQ-6 | Does reset put the option switches back to their defaults? The template clone does that. Keeping them means the reset script copies the row across | O3 behaviour |
| OQ-7 | Options are one global row, not per viewer. Confirm | O3 |
| OQ-8 | After unlock, who reads highlight rows (proposed: owner only), and may a photo's reader see that it was a highlight photo (`highlight_id`)? Nothing in the docs says | O4 policy |
| OQ-9 | At exactly `ends_at` the highlight is closed (half-open, like P1:47). Confirm (B16 settles only the note's 15:00 edge) | capture(), R-040 |
| OQ-10 | Under B2 `after_reveal_finished`, does "no one but the owner reads it" (`FS:291`, `DN:21`) also cover the journey, chapter and feeling-tag rows that §20 T opens to the network at unlock? | RLS on 3 tables under one switch setting |
| OQ-11 | **Conflict:** DN B9 (d) (`DN:28`, a chapter filter on the Positivity Feed, which public readers use) against FS §20 T (`FS:296`, chapters never public). Related: B9 (c) selects feed entries by feeling tag, so a public reader learns that a journey carries one of the four working tags. §20 wins under `CLAUDE.md`, but the user should rule on both | Positivity Feed query (Phase 4) |
| OQ-12 | The prototype's viewer identity is a per-transaction setting, so anyone with the app role can act as any user (C11, C16). Acceptable for the local prototype. Real authentication is needed before any deploy | Deploy (host still open) |
| OQ-13 | DN C17 (the next-unlock jump and other users' dates) is still open, with no default. Built as P1:194 says | Panel acceptance |
| OQ-14 | GC O6 (the journey of Wind's 2027-04-25 overview) is still open with the fixture-designer | Fixture load |
| OQ-15 | The time of day of each scripted action in P1 §3.8 is not given (fixture-designer) | Fixture load, OQ-2 |
