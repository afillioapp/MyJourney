# Phase 1 Amendments: gate-1 items O1–O4, and rulings T and U

Status: **2026-10-30: O1, O2 accepted (no model change). O3 APPROVED by the user (Spec §20 Z). O4 APPROVED by the user (Spec §20 AA).** OQ-10 → Spec §20 X; OQ-11 → §20 Y and CC; OQ-16 → §20 EE, carried by the panel role (§2.1, §1.3; gate r4 B-3, rules r5 V1); OQ-17 → §20 FF (§5); OQ-1, 2, 4, 6, 7, 8, 9 → Decisions-Needed B20, B26, B21, B22, B23, B24, B25 (provisional); OQ-8's `photo.highlight_id` half → §20 DD, enforced in §4 item 4 (rules r4 V2, gate r3 B-2). §20 GG carried in §4 item 5 (gate r4 B-4, rules r5 V3); §20 HH in §3 and §5 (gate r4 CF-20, rules r5 V2). **§20 II–LL (user rulings 2026-10-30):** II, the loader and tests as `mj_panel`, approved (§1.4, §1.5, §2.1, §2.2); JJ in §4 item 6; KK in §6; LL in §4 item 5 (vi). FORCEd `highlight` RLS reconciled with the SECURITY DEFINER readers in §4 item 1. Owner: lead-tech.

This file amends `Phase-1-Proposal.md` (P1, approved 2026-10-25) without editing it. Where P1 needs a matching line, §7 lists it for the supervisor to apply once the amendments are approved. Every amendment is the smallest change that closes its gate item. Nothing here redesigns §2.

Sources: `docs/reviews/2026-10-30-gate-1.md` (GC), P1 §2–§3, `Functional-Spec.md` (FS) §20 Q–LL (`FS:290–316`), `Decisions-Needed.md` (DN) provisional defaults, `Rules-Rubric.md` (RR). Stack: local Postgres 16 (decided 2026-10-30, DN D1). No deploy host is assumed.

---

## 0. Summary

| Item | Amendment, in one line | Rubric checks served | Changes the approved model? |
|---|---|---|---|
| O1 | `app_now()` = the last jump's instant plus the real time elapsed since then, frozen per transaction. One forward-only primitive, `clock_jump(interval > 0)`, reaches any exact instant. The panel gains small jumps | R-001, R-040, R-046, R-116, R-115, R-117, R-118, R-119, R-120, R-123; §2.5 check 10 | No. The panel's small jump sizes are a provisional default (`PROVISIONAL: B20`) |
| O2 | The fixture is loaded by replaying 2021–2026 through the real functions, on a clock started at 2021-01-01: the panel role jumps the clock and runs each action as the app role (FS §20 EE, §2.1). The result is kept as a template database. Reset clones the template. No role bypasses the rules and no row is ever deleted | R-117, R-120, R-002, R-003, R-119; P1:40 | No |
| O3 | One new supporting record, `prototype_option`: a single row with one column per switchable default (B2, B4, B5, B11, B12, C6), two allowed values each. RLS reads B2 (and C6, B11) from it | R-141, R-142, R-068, R-144, R-146, R-147, R-148, R-149 | **Yes. APPROVED 2026-10-30** |
| O4 | Highlight rows join the sealed list at P1:48 (a), owner included. One owner-only function, `highlight_open(journey)`, returns true or false and nothing else. After unlock, highlight rows (B24) and `photo.highlight_id` (FS §20 DD) reach the owner only | G-13, R-151, R-008, R-009, R-010, R-014, R-138, R-040, R-041 | **Yes. APPROVED 2026-10-30** |
| §20 T | Journey, chapter and feeling-tag rows after unlock: owner and network only, never public. Before unlock, unchanged (owner: type and dates; others: `has_journey_underway()`) | R-008, R-009, R-063, R-068 | No. It records a decided ruling. P1 needs matching lines |
| §20 U | `capture()` runs in a fixed order: the open highlight if not full, else a normal frame if one is left, else refuse | R-040, R-043, R-038, R-138 | No. P1:94–99 needs a matching line |
| §20 EE | A third role, `mj_panel`, alone holds EXECUTE on `clock_jump()`, `clock_jump_to_next_unlock()` and `set_option()`. It acts as a fixture user only through a one-way `SET ROLE mj_app` (§1.3–§1.5, §2.1, §2.2, §3) | R-153, R-141, R-117, R-014 | No. Grants and one role; no table or field |
| §20 GG | Non-owners get a photo's UTC capture date, never its time, and no part of a note's written time. Column grants plus owner-aware functions and views (§4 item 5) | R-154, R-151, R-144 | No. Grants, one view, four functions; no table or field |
| §20 HH | `b2` also governs the overview, and (through the photo) notes and person tags (§3, §5) | R-142, R-063 | No. One function; no table or field |
| §20 II | The loader and the tests connect as `mj_panel` and act as a user only through `SET LOCAL ROLE mj_app`; `mj_app` can never become `mj_panel` (§1.4, §1.5, §2.1, §2.2). Was a lead-tech proposal; approved | R-117, R-153 | No |
| §20 JJ | Every `id` is a random version-4 uuid from no sequence; non-owners get same-day photos ordered by `(captured_on, id)` (§4 item 6) | R-151, R-154 | No. P1 gives `id` no type (P1:60, 70, 89, 104, 113, 122, 131); this fills it. No table or field |
| §20 KK | `capture()` and the note step strip time and location metadata before encrypting (§6) | R-154 | No |
| §20 LL | Already carried: `note_read` gives `written_at` to the owner only, no date to anyone else (§4 item 5 (vi)) | R-154 | No |

---

## 1. O1: the clock reaches exact instants

### Problem

GC:63: P1's controls are +1 day, +1 month, +1 year, +5 years, next unlock and reset (`P1:195`). The rubric needs 2026-12-31 23:59:59 (R-001, `RR:55`), capture + 14:59, 15:00.000 and 15:01 (R-046, `RR:351–353`), highlight + 23:59 and + 24:01 and "2 hours before unlock" (R-040, `RR:314`), and "a date far from the real one" (R-116, `RR:860`). GC:56 (U3) asked whether the clock stands still between jumps. FS §20 V (`FS:298`) answers: "Simulated time runs at real speed from the last jump … Small jumps for testing edges are allowed."

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

- **The primitive** is `clock_jump(d interval)`. It refuses `d <= 0`. It sets `sim_at = app_now() + d` (in UTC) and `real_at = transaction_timestamp()`, and leaves `real_at` NULL while the clock is not started. **Who may call it (FS §20 EE, `FS:309`; settles OQ-16):** only the panel role `mj_panel` (§2.1). `mj_app`, the acting viewer's role, holds no EXECUTE on it and cannot become `mj_panel`. The same holds for `clock_jump_to_next_unlock()` (EE names it) and `set_option()` (§3). `clock_start()` is not named in EE and does not move `app_now()` (§2.3), but under the strictest reading no acting viewer calls it either: only `mj_owner`, its owner, calls it, from the reset script; neither `mj_app` nor `mj_panel` holds EXECUTE on it. `app_now()` is read-only and stays executable by both. Postgres grants EXECUTE on every new function to PUBLIC by default, so the migrations revoke it (`ALTER DEFAULT PRIVILEGES FOR ROLE mj_owner REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC`) and grant each function explicitly.
- **Panel controls.** These are built on the primitive:
  - unchanged from P1:195: +1 day, +1 month, +1 year, +5 years, jump to the next unlock, reset
  - **added under §20 V:** +1 minute and +1 hour. §20 V allows small jumps but names none; these sizes are the provisional default (`PROVISIONAL: B20`, settles OQ-1)
  - "+1 month" uses the same UTC month arithmetic as journeys, so it is clamped under B16. For example, 01-31 + 1 month gives 02-28
- **Jump to the next unlock** stays as P1:195 defines it: the global next `unlocks_at` after `app_now()`. DN C17 is still open and has no default. `clock_jump_to_next_unlock()` (SECURITY DEFINER, `mj_panel` only) jumps there and returns nothing; with no later unlock it refuses. To apply the §1.5 order the panel needs the target `t1` before it moves, so its transaction probes first: `SAVEPOINT probe; SELECT clock_jump_to_next_unlock(); SELECT app_now();` (this is `t1`) `ROLLBACK TO SAVEPOINT probe;`, then runs §1.5 to `t1` (tested, §1 evidence). The probe tells the panel nothing that the date it shows after the jump does not (C17 unchanged), and adds no function.
- **Reset** is in §2.

**1.4 How tests reach exact instants.** Each test case runs in **one transaction** on a connection logged in as `mj_panel` (FS §20 EE, II, `FS:313`). It jumps as `mj_panel`, and acts as a viewer with `SET LOCAL ROLE mj_app` plus the acting-user setting, then `RESET ROLE` before the next jump. The switch goes one way only: `mj_panel` may become `mj_app`, `mj_app` is never a member of `mj_panel`, and while the role is `mj_app` a jump is refused (tested, §1 evidence). Inside the transaction, `clock_jump(target - app_now())` lands exactly on `target`, and later jumps are exact offsets. For example: capture, then `clock_jump('15 minutes')`, then add the note. That puts the note at capture + 15:00.000 exactly (B16: refused).

| Rubric need | How it is reached |
|---|---|
| R-001: 2026-12-31 23:59:59, then 2027-01-01 00:00:00 | `clock_jump('2026-12-31 23:59:59+00' - app_now())`, assert, `clock_jump('1 second')`, assert |
| R-040: highlight + 23:59 and + 24:01; start 2 h before unlock | `clock_jump('23 hours 59 minutes')`, then `clock_jump('2 minutes')`. Or jump to `unlocks_at - 2 hours` |
| R-046: capture + 14:59, 15:00.000, 15:01 | Exact offsets from the capture, in one transaction each |
| R-116: a date far from the real one | `clock_jump('5 years')` or more. The rules run as of the app clock |
| R-121: 2023-12-31 and 2024-01-01 | Exact jumps |

**1.5 Jump order under a running clock** (P1:196–200). A jump from `t0` to `t1` runs as follows:

1. Unlocks need nothing to run (unchanged).
2. Each scripted action (P1 §3.8) that has not been applied yet and is dated at or before `t1` is applied, in date order. For each one, the clock first jumps to the action's instant, if that instant is still ahead. The action then runs **through the same functions the app uses, as the acting fixture user**, so its rows carry the scripted times. **How, under FS §20 EE and II:** the whole jump is one transaction on the panel's `mj_panel` connection. For each action: `clock_jump(action_at - app_now())` as `mj_panel`; `SET LOCAL ROLE mj_app`; set the acting user to the action's fixture user (`set_config(…, true)`, transaction-local); call the app functions; `RESET ROLE`. The action therefore has exactly a viewer's rights and no more, and `app_now()` is exactly `action_at` inside it. The script itself lives in the panel's fixture source, not in a table. Whether an action has been applied is read from the data (for example, Wind #6's `journey_reveal` row exists). No table records it.
3. Layers are computed when a reveal is finished, inside the finish function (P1:154). This satisfies P1:199 as well (GC NB-11).
4. Announcements are emitted by the same function, after the layer rows.
5. The clock jumps to `t1`, as `mj_panel`. If the last action was at `t1` itself, the clock is already there and no jump is made (`clock_jump` refuses a zero interval).

If real-time running has already carried the clock past an action's instant, the action is applied at `app_now()` at the start of the next jump, which is late. The clock cannot go back. This is the provisional default (`PROVISIONAL: B26`, settles OQ-2).

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

**Evidence for FS §20 EE (throwaway database `mj_scratch_r5` on the local Postgres 16.15, 2026-10-30, since dropped; roles dropped, cluster stopped).** Roles as in §2.1: `GRANT mj_app TO mj_panel WITH INHERIT FALSE, SET TRUE`; EXECUTE revoked from PUBLIC by default privileges.

```
has_function_privilege: mj_app   clock_jump / clock_jump_to_next_unlock / set_option / clock_start -> f f f f ; finish_reveal -> t
                        mj_panel clock_jump / clock_jump_to_next_unlock / set_option / clock_start -> t t t f ; finish_reveal -> f
as mj_app:   clock_jump('1 day')                     -> ERROR: permission denied for function clock_jump
             clock_jump_to_next_unlock()             -> ERROR: permission denied for function clock_jump_to_next_unlock
             set_option('b2','after_reveal_finished') -> ERROR: permission denied for function set_option
             clock_start()                           -> ERROR: permission denied for function clock_start
             SET ROLE mj_panel                       -> ERROR: permission denied to set role "mj_panel"
             afterwards: app_now(), b2               -> 2026-10-25 00:00:00+00 | from_unlock (unchanged)
as mj_panel, no SET ROLE: SELECT FROM photo_read -> ERROR: permission denied for view photo_read
                          finish_reveal(4)        -> ERROR: permission denied for function finish_reveal
one txn as mj_panel, clock running: clock_jump to 2027-04-25 12:00; SET LOCAL ROLE mj_app; acting user 4;
             current_user, finish_reveal(4), app_now() -> mj_app | accepted | 2027-04-25 12:00:00+00
             clock_jump('1 minute') while mj_app        -> ERROR: permission denied for function clock_jump
             RESET ROLE; current_user                   -> mj_panel ; pg_sleep(1.2) ; app_now() -> 2027-04-25 12:00:00+00
             stored journey_reveal.finished_at          -> 2027-04-25 12:00:00+00 (exact) ; next txn app_now() -> 12:00:01.2
next-unlock probe as mj_panel: app_now() 2026-10-25 00:00; SAVEPOINT; clock_jump_to_next_unlock(); app_now()
             -> 2027-01-01 00:00:00+00 ; ROLLBACK TO SAVEPOINT ; app_now() -> 2026-10-25 00:00:00+00
as mj_panel: set_option('b2','after_reveal_finished'); SELECT b2 -> after_reveal_finished (rolled back)
```

---

## 2. O2: loading the 2021–2026 fixture, and reset

### Problem

GC:64: `capture()` sets `captured_at = app_now()` (P1:90). Triggers refuse inserts after a reveal is finished (P1:46). The clock is forward-only from 2026-10-25 (P1:195, 201). So history cannot be inserted through the guarded path at baseline. A bulk insert by a role that bypasses the rules would create exactly what P1:40 says must not be needed. Reset (R-117) depends on the answer.

### Amendment: replay, with no bypass role

**2.1 Three roles** (two until 2026-10-30; `mj_panel` added to carry FS §20 EE, `FS:309`).

| Role | Used by | May do |
|---|---|---|
| `mj_owner` | Migrations and the reset script only. Never the app, never the loader, never the panel's jumps | Owns the schema, functions and databases. Never writes a product row. The only caller of `clock_start()` (§2.3) |
| `mj_app` | The app's viewer connections: every acting viewer, the C16 viewer switcher included | Exactly the grants in P1 §2.1 (`P1:44` "the app role"). No UPDATE, DELETE or TRUNCATE anywhere. Every rule applies to it. **No EXECUTE on `clock_jump()`, `clock_jump_to_next_unlock()`, `set_option()` or `clock_start()`, and not a member of `mj_panel`** (FS §20 EE) |
| `mj_panel` | The prototype panel's control process (time control and switches, DN C16), the fixture loader (§2.2) and the schema tests (§1.4) (FS §20 II, `FS:313`). LOGIN; its credentials never reach a product screen or route (R-153) | EXECUTE on `clock_jump()`, `clock_jump_to_next_unlock()`, `set_option()` and `app_now()`; SELECT on `prototype_option` (it holds no user data, §3). No other grant: on its own it reads and writes no product row. Membership `GRANT mj_app TO mj_panel WITH INHERIT FALSE, SET TRUE` (Postgres 16), so it gains a viewer's rights only after `SET ROLE mj_app`, and only for that span |

The acting user is set per transaction (a session setting read by `viewer()`). The loader and the scripted actions act as each fixture user in the same way the C16 viewer switcher does, after `SET LOCAL ROLE mj_app` (§1.5). Acting as a user gives that user's rights and nothing more. A deployed build would need real authentication instead; OQ-12 records this, and it does not block Phase 3.

**2.2 Building the baseline.**

1. Create a fresh database from the migrations. `sim_clock` starts **stopped** at **2021-01-01 00:00:00 UTC**, the earliest fixture instant (Lantern's `joined_at` and first commit; the other users join at their first commit, P1 §3.2 as amended 2026-10-30 by user ruling).
2. The loader, connected as `mj_panel` (**FS §20 II, `FS:313`, approved 2026-10-30**; first a lead-tech proposal derived from FS §20 EE and O2's "no role bypasses the rules"), walks every fixture event in time order. For each, in one transaction: `clock_jump(event_at - app_now())` as `mj_panel`, then `SET LOCAL ROLE mj_app`, set the acting user, and call the function the app would call, as that user, then `RESET ROLE`. This is the same path as a scripted action on a panel jump (§1.5):
   - join (each user before their first action, P1 §3.2, P1:213). Each of the four users with a journey joins at the instant of their first commit, and the join comes before the commit: Steady Lantern 2021-01-01, Second Wind 2021-03-15, Long Way Round 2022-09-01, Open Hands 2023-06-01, all 00:00:00 UTC. First Light joins at 2026-10-01 00:00:00 UTC and commits nothing (P1:211)
   - `commit()`
   - `start_highlight()`, `capture()` (placeholder image) and the note within 15 minutes
   - after unlock: the visibility, person-tag, chapter and feeling-tag inserts
   - finishing the reveal, which computes layers and emits announcements (P1 §2.3)
   - reflections and overviews in their slots
3. Stop with `clock_jump` to the **baseline instant, 2026-10-25 00:00:00 UTC** (P1:201; the time of day is the provisional default, `PROVISIONAL: B21`, settles OQ-4). The clock stays stopped. Mark the database as a template (`myjourney_baseline`, no connections allowed).

The clock stays stopped during the load so that every fixture timestamp is exact (for example, commits at 00:00:00, NB-6). The prototype never runs on a stopped clock. §20 V governs from `clock_start()` on.

This answers the rest of GC:64:

- **Blobs of sealed journeys** are encrypted by `capture()` itself under the journey key, the same way as live captures. There is no load-only path (R-002).
- **Historical layers and announcements** are produced by the replay of each finished reveal. They are not inserted.
- **The fixture passes the guards as designed**, given the §20 U order (§6). Highlight photos must be captured inside their windows (P1 §3.3). Lantern #5 fills its highlight to 12. Hands #2's 48 normal photos fit its cadence. Round's 2026-09-10 reflection, made before any reveal is finished, is allowed by P1:117.

**2.3 Reset** (P1:195, R-117). The reset script runs as `mj_owner`:

1. Drop the working database.
2. `CREATE DATABASE … TEMPLATE myjourney_baseline`.
3. Call `clock_start()`. This sets `real_at` from NULL to now. `app_now()` reads exactly the baseline both before and after, so it is not a backward move. The clone also carries the template's `prototype_option` row, so every switch is back at its default (`PROVISIONAL: B22`, settles OQ-6).

No DELETE or TRUNCATE path exists on any product table. The panel's reset control reaches this script through the prototype's control process. Neither `mj_app` nor `mj_panel` can call it or `clock_start()` (§1.3).

**2.4 New check (proposed, for the rules-guardian to number).** These fail the build:

- the fixture loader or a schema test opens a connection as anything other than `mj_panel` (it never connects as `mj_owner` or directly as `mj_app`; FS §20 II)
- a product function call by the loader runs with `current_user` other than `mj_app`. The database enforces this: `mj_panel` holds no EXECUTE on any product function, so such a call fails (tested: `finish_reveal(4)` as `mj_panel` is refused, §1 evidence). The check is a test that calls one product function as `mj_panel` without `SET ROLE` and expects the refusal
- the loader's source contains an INSERT, UPDATE, DELETE, COPY or TRUNCATE statement against a product table
- after load, the baseline differs from the P1 §3 expectations: the counts per journey, the §3.4 rings and the §3.6 matrix

**Rubric served:** R-117 (reset equals the baseline load), R-120 (stored times come from the app clock, including during the load), R-002 and R-003 (sealed at load), R-119, P1:40.

**Model change:** none. There is no new table or field. The roles follow P1:44's "app role"; `mj_panel` is the separate panel role FS §20 EE requires. The template and reset script are infrastructure.

**Needs from the fixture-designer** (P1 §3, not this file):

- the exact instant of every event (NB-4, NB-6, generated with a fixed seed)
- the time of day of the scripted actions: 12:00 UTC (FS §20 BB)
- the journey of Wind's 2027-04-25 overview: journey #6 (user ruling 2026-10-30, P1 §3.8)

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

### Amendment: **APPROVED 2026-10-30**

Add one supporting record to P1 §2.4:

**`prototype_option`**: exactly one row (a boolean primary key fixed to `true`). The settings are the ones in DN's "Provisional defaults in force" table. Each column is NOT NULL, checked to exactly its two settings (R-141: no "both", "auto" or free value), and defaults to the provisional default. Each carries a `PROVISIONAL: <ID>` comment (R-149).

| Column | Settings (first = default) | Who reads it |
|---|---|---|
| `b2` | `from_unlock` / `after_reveal_finished` | RLS on photo and on what follows a photo: photo_visibility, reflection, note and person_tag, all through `photo_readable()` (§4 item 5), and on `journey_overview` through `overview_readable()` (FS §20 HH, `FS:312`; §5). Not on journey, chapter or feeling-tag rows: the network reads those from unlock under both settings (FS §20 X, settles OQ-10). Before 2026-10-30 this cell said "photo, photo_visibility and reflection only" |
| `b4` | `per_finished_reveal` / `per_year_with_app` | App (the circle is derived) |
| `b5` | `owner_only` / `viewer_visible` | App (the activity graph) |
| `b11` | `named` / `unnamed` | The announcement read function (under `unnamed`, readers get no subject, R-146) |
| `b12` | `shown` / `hidden` | App (Walking a path) |
| `c6` | `hidden` / `shown` | RLS on `person_tag` for non-owners (strictest reading, R-148: absent from the data, not only the UI) |

- **Grants.** `mj_app` and `mj_panel` have SELECT on the row. Changes go only through `set_option(id, setting)` (SECURITY DEFINER). There is no INSERT, DELETE or TRUNCATE path. **Only `mj_panel` holds EXECUTE on `set_option()`; `mj_app` does not** (FS §20 EE, `FS:309`; settles OQ-16; §2.1, tested in §1).
- **Settings hold no user data,** so reading them leaks nothing (R-141 treats the panel as a data path under R-014).
- **One row for the whole prototype,** like the one clock (P1:194; one options panel, DN C16, R-141). The settings are not per viewer (`PROVISIONAL: B23`, settles OQ-7).
- **The B2 term in the photo read policy, for non-owners of an unlocked journey.** The policy reads the B2 setting from `prototype_option`:
  - when the setting is `after_reveal_finished`, the read is allowed only if a `journey_reveal` row exists for the journey (FS §20 R: Public photos included)
  - when it is `from_unlock`, the B2 term allows the read
  - the visibility, network and seal terms of P1:48 still apply in both cases
  - the term is evaluated only inside the SECURITY DEFINER predicates `photo_readable()` (§4 item 5) and `overview_readable()` (§5, FS §20 HH). `mj_app` holds no EXECUTE on any helper they call and no grant on `journey_reveal` for this purpose, so no direct call tells a stranger whether a journey's reveal is finished (tested, §5)
- **B4, B5 and B12** are enforced by the app, which reads the same row. They change no database grant.

**Alternative considered and rejected:** a per-session setting (`SET mj.b2 = …`). Any client can override it, so the database would not be enforcing B2.

**Rubric served:** R-141 (exactly two settings, starts on the default), R-142 and R-068 (B2 under both settings), R-144, R-146, R-147, R-148, R-149.

**Model change: yes**, one supporting record in §2.4. **APPROVED 2026-10-30 (FS §20 Z).**

**Evidence (feasibility):** `set_option_b2('both')` gives `ERROR: … violates check constraint "prototype_option_b2_check"`. `DELETE FROM prototype_option` as `mj_app` gives `ERROR: permission denied`. The row reads `from_unlock`.

---

## 4. O4: highlight rows sealed

### Problem

GC:66 and RR G-13 (`RR:1240` at `7f20c3d`; it was `RR:1185` when first cited): P1:48 seals photo, note, tag and reflection rows, but not highlight rows. A readable `highlight` row exposes `started_at` and `ends_at`. DN B6 (`DN:25`) and FS §20 S (`FS:292`) allow the owner only the plain fact that "a highlight is open", with no end time and no countdown, and allow everyone else nothing (R-008, `RR:97–103`).

### Amendment: **APPROVED 2026-10-30**

1. **Add `highlight` to P1:48 (a).** Highlight rows are readable only once `app_now() >= unlocks_at` of their journey, **the owner included**, so `count(*)` returns 0 before unlock. The RLS is FORCEd so that the table owner's connections are covered too. After unlock, the readers are the owner only (`PROVISIONAL: B24`, settles OQ-8).
   **How FORCE and the SECURITY DEFINER readers fit together (resolved 2026-10-30).** `capture()`, `start_highlight()` and `highlight_open()` are owned by `mj_owner`, the table owner, and run as it, so FORCE applies to them too: with only a viewer policy they read no highlight row and cannot insert one (tested below: `start_highlight()` fails, `highlight_open()` answers `f` for an open highlight). The arrangement, with no new role, table or field:
   - `highlight_read`, `FOR SELECT TO mj_app`: the seal rule above (the journey's owner, from unlock).
   - `highlight_rules`, `FOR ALL TO mj_owner USING (session_user IN ('mj_app', 'mj_panel')) WITH CHECK (`the same`)`. Inside a SECURITY DEFINER function `current_user` is `mj_owner` but `session_user` stays the login role: `mj_app`, or `mj_panel` after `SET LOCAL ROLE mj_app` (§1.4). So the definer functions read and write every highlight row, and a connection logged in as `mj_owner` (migrations, reset) matches no policy and reads 0 rows. Neither `mj_app` nor `mj_panel` can change `session_user` (`SET SESSION AUTHORIZATION` needs a superuser) or become `mj_owner`.
   - `mj_app` holds SELECT only on `highlight`; no INSERT, UPDATE, DELETE or TRUNCATE. `start_highlight()` is the only writer.
   - Because `highlight_rules` opens the table to any `mj_owner` definer function called from an app or panel session, only these three may name `highlight`. Proposed check (for the rules-guardian to number): list every function whose body names `highlight`; it fails on any other than `capture`, `start_highlight` and `highlight_open`.
   - Limit: `mj_owner` owns the table and could ALTER it, so against `mj_owner` itself the guard is that no product connection uses that role (§2.1). The same arrangement serves `layer` if it is FORCEd (§5).
2. **One new callable: `highlight_open(journey_id) → boolean`.** SECURITY DEFINER:
   - It returns whether `started_at <= app_now() < ends_at` for some highlight of that journey.
   - **For the owner only.** For anyone else, and for a journey id that does not exist, it raises the same refusal. A non-owner therefore cannot tell another user's journey from no journey (R-008's comparison against First Light).
   - It returns no time, no count and no id.
3. `capture()` and `start_highlight()` read highlight rows internally (SECURITY DEFINER) and still return only `accepted` or `refused` (P1:49).
4. **`photo.highlight_id` is readable by the owner only, also after unlock (FS §20 DD).** Before unlock the whole row is sealed (P1:48 a). Row-level security works per row and every viewer runs as `mj_app`, so neither RLS nor a plain column grant can tell the owner from another reader of the same row. It is enforced with no table or field change, in three parts: (i) `mj_app` has a column grant on `photo` that leaves `highlight_id` out, and since FS §20 GG also `captured_at` (`GRANT SELECT (id, journey_id, image)`; item 5), so any statement that names the column, filters or sorts on it, or uses `SELECT *` on `photo` fails for every viewer; (ii) one SECURITY DEFINER function, `photo_highlight_id(photo_id)`, returns the id only when the viewer owns the photo's journey and `app_now() >= unlocks_at`, and NULL otherwise, including for an id that does not exist, so a non-owner gets the same NULL for a highlight photo, a normal photo and no photo; (iii) every reader, the owner included, reads photos through one view, `photo_read` (`security_invoker = true`, so P1:48's RLS applies unchanged), which returns the granted columns, the two capture columns of item 5, and `photo_highlight_id(id) AS highlight_id`. Any other function that returns photo data returns `highlight_id` only through (ii). Highlight rows follow item 1 (B24). Residual, not covered by any ruling: many photos on one capture date can still suggest a highlight (R-151; narrowed by FS §20 GG from times to dates, not closed).
5. **A photo's capture time is readable by the owner only; everyone else gets the UTC date (FS §20 GG, `FS:311`; R-154).** Same pattern as item 4, no table or field change: (i) the column grants leave out `photo.captured_at` (item 4 (i)) and `note.written_at` (`GRANT SELECT (id, photo_id, image) ON note`), so naming, filtering or sorting on either fails for every viewer, the owner included; (ii) `photo_captured_at(photo_id) → timestamptz`, SECURITY DEFINER, returns the full time only when the viewer owns the photo's journey and `app_now() >= unlocks_at`, else NULL (also for an id that does not exist); (iii) `photo_captured_on(photo_id) → date`, SECURITY DEFINER, returns `(captured_at AT TIME ZONE 'UTC')::date` (B16: UTC) only when `photo_readable(photo_id)` is true, else NULL, so it is no oracle for sealed, private or missing photos; (iv) `photo_readable(photo_id) → boolean`, SECURITY DEFINER, is P1:48's photo read rule written once (seal, visibility, network, public, and the B2 term of §3). The photo SELECT policy is `USING (photo_readable(id))`, and the photo_visibility, reflection, note and person_tag policies use `photo_readable(photo_id)` (person_tag also C6, R-148), so the date function and the policies cannot drift. A direct call answers only what `SELECT … FROM photo_read WHERE id = …` already answers (the FS §20 FF reasoning). (v) `photo_read` returns `photo_captured_on(id) AS captured_on` and `photo_captured_at(id) AS captured_at` (NULL for anyone but the owner). (vi) **The note's written time goes to the owner only, and to no one else in any form, not even its date.** It is at most 15 minutes after capture (P1:108), so its time pins the capture time, and its date differs from the capture date when a photo is taken after 23:45 UTC, which pins that too. Notes are read through `note_read` (`security_invoker = true`): `id, photo_id, image, note_written_at(id) AS written_at`, where `note_written_at(note_id)` is SECURITY DEFINER and owner-only after unlock, like (ii). Screen-Inventory already shows no note written time or date to a non-owner (SI:54, :687). **This carries FS §20 LL (`FS:316`) as ruled: a non-owner never sees when a note was written, not even the date; the owner sees the full time.** The note's `id` is a random uuid (item 6), so no id order bounds it either. (vii) **Activity graph (B5, `PROVISIONAL: B5`).** Under `owner_only` only the owner sees it, built from the full time. Under `viewer_visible` it is built from the photos the viewer can read, through `photo_read`, so a non-owner's data has `captured_on` only: **no bucket finer than one UTC day** is possible from the data. Whether the graph shows days or something coarser is a Phase 4 display choice, not set here. The order within one day for a non-owner is item 6 (FS §20 JJ, was OQ-18); time in image metadata is §6 (FS §20 KK, was OQ-19).

6. **Ids, and same-day order for a non-owner (FS §20 JJ, `FS:314`; settles OQ-18).** No table or field change: P1 lists `id` with no type (P1:60, 70, 89, 104, 113, 122, 131), so this fills a blank and does not change the approved model.
   - **Every surrogate `id`** (user, journey, photo, note, reflection, journey_overview, highlight, announcement, and any other product table that has one) is `uuid DEFAULT gen_random_uuid()`, a random version-4 uuid. No product table has a sequence, `serial` or identity column. A time-ordered id (uuid v1 or v7, Postgres 18's `uuidv7()`, ULID, snowflake) is banned, since it carries its creation time. Proposed check (for the rules-guardian to number): `pg_sequences` in the product schemas is empty, no column is identity or defaults to `nextval`, and every stored `id` has version nibble `4`. `journey.seq` (P1:71) is a per-user field, not an id, and stays.
   - **The fixed order.** `photo_read` ends `ORDER BY photo_captured_on(id), id`: UTC capture date, then the random id. It is the same for every reader and every read, and carries no time within the day. Every other function or route that returns photos to a non-owner uses the same order; none relies on the table's physical order. `note_read` follows the photo order. Whether the owner's own screens re-sort by full time is a Phase 4 display choice: the owner already reads the time (FS §20 GG).
   - **What else could carry time, and what is closed.** `xmin` and `ctid` are refused on `photo` and `note` (they need table-level SELECT; `mj_app` has column grants only) and do not exist on the views (tested).

   | Id | Matters under GG / JJ / LL? | Why |
   |---|---|---|
   | `photo.id` | **Yes** (JJ, GG) | A non-owner reads it; a shared sequence orders a day's photos and bounds another user's capture time between two of the reader's own |
   | `note.id` | **Yes** (GG, LL) | A non-owner reads it through `note_read`; a note is written within 15 minutes of capture, so its id order bounds the capture time and the note time |
   | `journey.id` | Not under GG/JJ; **yes under §20 T** | A public reader sees `photo.journey_id`; a shared sequence would bound the commit date, which §20 T keeps from the public |
   | `highlight.id` | No | Its rows and `photo.highlight_id` reach the owner only (B24, FS §20 DD) |
   | `reflection.id`, `journey_overview.id` | No | Their readers already read `written_at`, so id order adds nothing |
   | `announcement.id` | No | Each carries `at` for its readers |
   | `person_tag`, `layer`, `photo_visibility` | No | P1 gives them no `id` (P1:148, 165, 166); none is added. Tag order reflects the reveal, not capture |
   | `user.id` | Not under GG/JJ | A shared sequence would give join order; no ruling covers it. The one rule (random uuid everywhere) closes it anyway |

The window is half-open, `[started_at, ends_at)`, matching the journey interval at P1:47. At exactly `ends_at` the highlight is closed (`PROVISIONAL: B25`, settles OQ-9).

**Rubric served:**

- G-13, R-151 (FS §20 DD)
- R-008 (others learn nothing)
- R-009 (owner: type, dates and the bare "open")
- R-010 (a capture changes nothing that can be read)
- R-014 (every path)
- R-138 (the one DOM difference B6 allows)
- R-040, R-041 (the window, and one at a time)

**Model change: yes.** It changes the §2.1 sealing row (P1:48) and adds one function. Item 1's two-policy arrangement (2026-10-30) and item 6 (FS §20 JJ) change no table or field. **APPROVED 2026-10-30 (FS §20 AA).** There is no new table or field. Item 4 (FS §20 DD) adds a column grant, one view and one function, and changes no table or field. Item 5 (FS §20 GG, a decided ruling) narrows two column grants and adds one view (`note_read`) and four functions (`photo_captured_at`, `photo_captured_on`, `photo_readable`, `note_written_at`), and changes no table or field.

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

**Evidence for item 4 (FS §20 DD), throwaway database `mj_scratch_dd` on the local Postgres 16, 2026-10-30, since dropped; roles dropped, cluster stopped.** Viewer 1 owns J1 (unlocked; photo 100 in highlight 10, photo 101 normal) and J6 (sealed; photo 600 in highlight 60). Viewer 2 stands for a network reader, viewer 3 for a public reader; the simplified photo policy lets all three read J1.

```
as owner (1):   SELECT id, highlight_id FROM photo_read  -> 100 | 10 ; 101 | NULL ; highlight rows = 1
as network (2): SELECT id, highlight_id FROM photo_read  -> 100 | NULL ; 101 | NULL ; highlight rows = 0
                photo_highlight_id(100), photo_highlight_id(999) -> NULL, NULL
as public (3):  SELECT id, highlight_id FROM photo_read  -> 100 | NULL ; 101 | NULL
                count(*) FILTER (WHERE highlight_id IS NOT NULL) FROM photo_read -> 0
any viewer:     SELECT highlight_id FROM photo           -> ERROR: permission denied for table photo
                SELECT * FROM photo                      -> ERROR: permission denied for table photo
                ... WHERE highlight_id IS NOT NULL       -> ERROR: permission denied for table photo
                ... ORDER BY highlight_id                -> ERROR: permission denied for table photo
                SELECT id, captured_at FROM photo        -> 2 rows (granted columns still readable; before item 5. Since FS §20 GG: refused, below)
as owner (1), sealed J6: count(*) FROM photo_read        -> 0 ; photo_highlight_id(600) -> NULL
```

**Evidence for item 5 (FS §20 GG), throwaway database `mj_scratch_r5` on the local Postgres 16.15, 2026-10-30, since dropped; roles dropped, cluster stopped.** Viewer 1 owns J1 (unlocked, revealed): photos 100 (09:12, in highlight 10) and 101 (17:40), both 2025-08-09; 102 (2025-03-02 23:55, public, note written 2025-03-03 00:05); 103 (private). J6 is sealed (photo 600). Viewer 2 is on 1's map; viewer 3 is a public reader.

```
as owner (1):   SELECT id, captured_on, captured_at, highlight_id FROM photo_read
                -> 100 | 2025-08-09 | 2025-08-09 09:12:00+00 | 10 ; 101 | 2025-08-09 | 2025-08-09 17:40:00+00 | NULL
                   102 | 2025-03-02 | 2025-03-02 23:55:00+00 | NULL ; 103 | 2025-04-01 | 2025-04-01 08:00:00+00 | NULL   (600 absent: sealed)
                note_read: 1 | 102 | 2025-03-03 00:05:00+00
as network (2): photo_read -> 100 | 2025-08-09 | NULL | NULL ; 101 | 2025-08-09 | NULL | NULL ; 102 | 2025-03-02 | NULL | NULL
                photo_captured_on(100), (103 private), (600 sealed), (999 none) -> 2025-08-09, NULL, NULL, NULL
                photo_captured_at(100) -> NULL ; note_read: 1 | 102 | NULL
                photos dated 2025-08-09: count(DISTINCT captured_on) = 1, count(DISTINCT captured_at) = 0
as public (3):  photo_read -> 102 | 2025-03-02 | NULL | NULL ; photo_captured_on(100) -> NULL ; note_read: 1 | 102 | NULL
any viewer:     SELECT captured_at FROM photo / SELECT * FROM photo / ORDER BY captured_at / WHERE captured_at > now()
                -> ERROR: permission denied for table photo
                SELECT written_at FROM note -> ERROR: permission denied for table note
                SELECT id, journey_id FROM photo -> rows (granted columns still readable)
```

**Evidence for item 1's policy arrangement and item 6 (FS §20 JJ), throwaway database `mj_scratch_jj` on the local Postgres 16.15, 2026-10-30, since dropped; roles dropped, cluster stopped.** Roles as §2.1; `highlight` ENABLE + FORCE with the two policies of item 1; every `id` `uuid DEFAULT gen_random_uuid()`. Users A, B, C; A and B commit 2026-01-01. (Earlier evidence blocks show small integer ids; those were scratch stand-ins.)

```
panel txn, SET LOCAL ROLE mj_app, viewer A, 2026-08-09 09:00:
  session_user, current_user                     -> mj_panel | mj_app
  start_highlight(A) ; again                     -> accepted ; refused   (one at a time: the definer read the row)
  capture(A) ; highlight_open(A)                 -> accepted ; t         (photo stored with its highlight_id)
  count(*) FROM highlight (sealed, owner)        -> 0
mj_app login, viewer A: highlight_open(A) ; count(*) FROM highlight -> t ; 0
  INSERT INTO highlight ...                      -> ERROR: permission denied for table highlight
  SET ROLE mj_owner                              -> ERROR: permission denied to set role "mj_owner"
mj_owner connection: count(*) FROM highlight     -> 0 ; highlight_open(A) -> f ; INSERT -> ERROR: new row violates row-level security policy
counterfactual, highlight_rules dropped (FORCE, viewer policy only):
  start_highlight(B)                             -> ERROR: new row violates row-level security policy for table "highlight"
  highlight_open(A), highlight open in fact      -> f   (wrong: this is the defect item 1 now closes)
after unlock (2027-01-01): count(*) FROM highlight as A ; as C -> 1 ; 0
JJ: 30 captures each by A and B on 2026-08-09, alternating 09:01-09:40, through capture() as the panel acting as mj_app
  photos 61 ; every id version 4                 -> t ; sequences in schema 0 ; identity or nextval columns 0
  as C (non-owner): photo_read rows, distinct dates, rows with a time -> 61 | 1 | 0
  C's order = ORDER BY (captured_on, id)         -> t ; owner changes between neighbours 22 of 60
  corr(C's position, true capture rank)          -> 0.141 (n = 61; a shared sequence would give 1.000 by construction)
  as C: SELECT xmin FROM photo ; ctid FROM photo ; xmin FROM note -> ERROR: permission denied for table photo / photo / note
        SELECT xmin FROM photo_read              -> ERROR: column "xmin" does not exist
        SELECT id FROM photo ORDER BY captured_at -> ERROR: permission denied for table photo
```

---

## 5. FS §20 T: who reads a journey's type, dates, chapter and feeling tags

Ruling (`FS:296`): after unlock, the owner and the owner's network, never public, the same as the overview (P1:126). Before unlock, P1:84 and B19 (`DN:38`) are unchanged.

| Row | Sealed (`now < unlocks_at`) | Unlocked |
|---|---|---|
| `journey` (type, `committed_at`, `unlocks_at`) | Owner: these three fields only (P1:84, B19). Others: only `has_journey_underway(user)` (D17) | Owner and network. Never anyone else |
| `journey_chapter` | None exist: it is insert-only during the reveal (P1:143). It is sealed by RLS anyway | Owner and network |
| `journey_feeling_tag` | Same as `journey_chapter` | Owner and network |
| `journey_overview` | (unchanged, P1:126) | Owner and network. **Under B2's `after_reveal_finished`, the network only once the reveal is finished** (FS §20 HH, `FS:312`); the owner from unlock. Policy `USING (overview_readable(journey_id))`: SECURITY DEFINER, true when `app_now() >= unlocks_at` and either the viewer owns the journey or `viewer_in_network(owner)` and the B2 term of §3 holds; false for a missing id |

- **"Network"** means the users on the owner's current map (reading R2, P1 §3.8 / §2.3).
- **Layer rows are readable only by their owner** (P1:51). So the policy uses a SECURITY DEFINER predicate, `viewer_in_network(owner_id)`. It answers only for the current viewer, returns a boolean, and never takes a member to return an owner (P1:51). **It cannot be made callable only inside policies:** Postgres checks EXECUTE (and USAGE, and SELECT on any view a policy reads) as the querying role, so `mj_app` must hold EXECUTE and a client can call it directly (tested, below). A direct call answers exactly what the policy already answers: whether the viewer can read that owner's unlocked journey rows (§20 T); an owner with a map always has one, since layers are written only when a reveal is finished. **Settled 2026-10-30, FS §20 FF (`FS:310`): it may stay directly callable** (was OQ-17). No route exposes it. `overview_readable(journey_id)` (row above) is callable for the same reason and adds no fact: for a stranger it is always false, as for a missing id; for a network member it adds only whether the reveal is finished, which the network already learns from "journey launched" (FS §20 J, M). Its owning role must not fall under the layer table's owner-only policy (that policy applies `TO mj_app`), or under FORCE it reads no row and every answer is false (tested, below).
- **A reader of a Public photo who is not in the network** reads the photo row but no journey, chapter or tag row. `photo.journey_id` leads nowhere for them.
- **Under B2's `after_reveal_finished` setting,** FS §20 R (`FS:291`) and DN B2 (`DN:21`) say "no one but the owner reads it until the reveal is finished". **Settled 2026-10-30, FS §20 X:** the journey, chapter and feeling-tag rows are readable by the network from unlock under both settings. The `b2` switch does not govern them (§3). **The overview is the exception: FS §20 HH (`FS:312`) puts it under `b2`** (table above).
- **Conflict, not picked:** DN B9 (d) (`DN:28`) gives the Positivity Feed, which public readers use, a chapter filter. FS §20 T (`FS:296`) says chapters are never public. **Settled 2026-10-30, FS §20 Y:** no chapter filter.

**Evidence (throwaway database `mj_scratch_n6` on the local Postgres 16, 2026-10-30, since dropped; roles dropped, cluster stopped):**

```
policy calls priv.viewer_in_network(); mj_app: no USAGE, no EXECUTE  -> SELECT journey: ERROR: permission denied for function viewer_in_network
same, USAGE on schema, no EXECUTE                                    -> SELECT journey: ERROR: permission denied for function viewer_in_network
policy reads a definer view instead; mj_app has no SELECT on it      -> SELECT journey: ERROR: permission denied for view network_of_viewer
USAGE + EXECUTE; layer FORCEd, policy for all roles                   -> SELECT journey as Wind: 0 rows; direct call viewer_in_network(1) = f
```

**Notes and person tags under `b2` (gate r4 CF-20, rules r5 V2 "same line").** Both follow the photo, so `b2` governs them through `photo_readable()` (§4 item 5): FS:15 lists the handwritten note and the people tagged as parts of the Photo; FS §20 R (`FS:291`) says no one but the owner reads the journey until the reveal is finished; FS §20 X (`FS:301`) says photos "and what follows them" wait. Person tags are also hidden from non-owners under C6's default (`PROVISIONAL: C6`); under `shown`, only on photos the reader can read (R-148). Nothing here is unsettled.

**Evidence for FS §20 HH (throwaway database `mj_scratch_r5`, as in §4 item 5, since dropped).** Viewer 4 owns J4 (unlocked, reveal not finished; one photo, its note, one person tag, one overview). Viewer 2 is on 4's map and on 1's; viewer 3 is a stranger. C6 set to `shown` so tags can be counted.

```
viewer | b2                    | J4 journey row | photos | notes | tags | overview | J1 overview (revealed)
4      | from_unlock           | 1 | 1 | 1 | 1 | 1 | 0
2      | from_unlock           | 1 | 1 | 1 | 1 | 1 | 1
3      | from_unlock           | 0 | 0 | 0 | 0 | 0 | 0
4      | after_reveal_finished | 1 | 1 | 1 | 1 | 1 | 0
2      | after_reveal_finished | 1 | 0 | 0 | 0 | 0 | 1      <- journey row from unlock (§20 X); overview waits (§20 HH)
3      | after_reveal_finished | 0 | 0 | 0 | 0 | 0 | 0
panel jump to 12:00; SET LOCAL ROLE mj_app; acting user 4; finish_reveal(4) -> accepted
2      | after_reveal_finished | 1 | 1 | 1 | 1 | 1 | 1
direct calls: overview_readable(1, 4, 6 sealed, 999) as stranger 3 -> f f f f ; as network 2 -> t t f f
              the B2 helper inside the predicates, called by mj_app -> ERROR: permission denied for function
```

**Model change:** none. This records a decided ruling. P1 needs matching lines at P1:48, 84 and 143 (§7). FS §20 HH adds one function (`overview_readable`) and no table or field.

---

## 6. FS §20 U: the capture order

Ruling (`FS:297`): the open highlight first. Once it is full, a normal frame if one is left, otherwise refuse. `capture(journey_id, image)` runs as follows:

1. **Refuse** unless the caller owns the journey and `committed_at <= app_now() < unlocks_at` (P1:99).
2. **Lock the journey** for the transaction (`pg_advisory_xact_lock`), so that two concurrent captures cannot both pass a count.
3. **Highlight.** If a highlight of this journey is open (`started_at <= app_now() < ends_at`) and holds fewer photos than the type's yearly quota (48, 24 or 12), insert the photo with that `highlight_id`. Return `accepted`.
4. **Normal frame.** Otherwise, if the journey's photos with `highlight_id IS NULL` number fewer than `cadence × m`, insert the photo with `highlight_id` NULL. Return `accepted`. Here `m` is the current journey month (1–12).
   - Month *k* starts at `committed_at + (k − 1) months`, computed from `committed_at` each time (not chained), in UTC, clamped under B16. This gives the R-123 case: commit 2026-01-31, month 2 starts 2026-02-28, month 3 starts 2026-03-31.
5. **Otherwise** return `refused`. No number is returned or stored (P1:49, R-038, R-039).

**Image metadata (FS §20 KK, `FS:315`; settles OQ-19).** The capture path strips time and location metadata (EXIF, XMP, GPS, PNG text chunks) from the photo before `capture()` encrypts it, and from the note's image before the note step stores it, so the stored file keeps none, for the owner too. The prototype's fixture placeholders are generated with none (P1:256). Real-device capture is Phase 4 or later.

Effects on the rubric:

- **R-040.** "+24:01 (treated as normal frame or refused)" (`RR:314`) is now settled by state: a normal frame if one is left, else refused.
- **R-043.** A 13th photo in a full Contemplator highlight goes to a normal frame if one is left. It is refused as a highlight photo either way, which matches `RR:333`.
- **Wording.** Updating R-040's wording is for the rules-guardian.

**Model change:** none. P1:94–99 needs a line that gives the order (§7).

---

## 7. Matching lines P1 needs (applied by the supervisor 2026-10-30, commit 080ccfd)

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
| 3, 48 (e), 92, 133, 170, 195, 196, 198, 201 | Applied 2026-10-30 by lead-tech, each inside its existing line so no P1 citation moves: status note; owner-only `highlight_id` and highlight rows; the `[started_at, ends_at)` window; one global options row; reset restores switches; pointer to §1.5; late actions at the next jump and 12:00 UTC; baseline 00:00:00 UTC | FS §20 DD, BB; B24, B25, B23, B22, B26, B21 (rules r4 V2, V3; gate r3 B-2, CF-19) |
| 3, 48 (c), 48 (g), 89, 91, 104, 106, 195 | Applied 2026-10-30 (third round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–LL; FORCEd highlight read by the definer functions; random uuid ids and the same-day order; photo and note ids; metadata stripped at capture; LL cited on the note time; loader as `mj_panel` approved | FS §20 II, JJ, KK, LL; §4 item 1 |
| 3, 48 (e), 50, 90, 106, 108, 126, 169, 170, 181, 195 | Applied 2026-10-30 (second round) by lead-tech, each inside its existing line, so P1 stays at 408 lines and no P1 citation moves: status note to §20 Q–HH; capture date only for non-owners, owner-only note written time; graph no finer than a day; note readers follow the photo; overview under `b2`; clock and switches moved by `mj_panel` only; check 6 token scan; load and jumps by `mj_panel` acting as `mj_app` | FS §20 EE, GG, HH (gate r4 B-3, B-4, CF-20, NB-10; rules r5 V1–V3) |

§3 is being edited by another agent at the time of writing. The §3 lines go through the supervisor.

---

## 8. Open questions (stopped, not guessed)

| # | Question | Blocks |
|---|---|---|
| OQ-1 | Panel small jump sizes. §20 V allows small jumps but names none. Proposed: +1 minute and +1 hour. Tests use `clock_jump(interval)` directly. **Settled 2026-10-30 as a provisional default: DN B20 (+1 minute, +1 hour).** | Nothing now (was: the panel only, not the schema) |
| OQ-2 | A scripted action whose instant the running clock has already passed is applied late, at the next jump's starting `app_now()`. Accept? **Settled 2026-10-30 as a provisional default: DN B26 (applied at the next jump).** | Nothing now (was: time control) |
| OQ-3 | R-119 expects announcements "with times after the map entry". Both are written at the same instant inside the finish function. Read "after" as "not before"? | R-119 test wording (rules-guardian) |
| OQ-4 | Baseline time of day: 2026-10-25 **00:00:00 UTC**? P1:201 gives only the date. **Settled 2026-10-30 as a provisional default: DN B21 (00:00:00 UTC; P1:201 now carries it).** | Nothing now (was: fixture load, R-117) |
| OQ-5 | How is `joined_at` set: `app_now()` at join, or given? P1:63 is blank. The replay works either way: it jumps to 2021-01-01 and joins | Schema default |
| OQ-6 | Does reset put the option switches back to their defaults? The template clone does that. Keeping them means the reset script copies the row across. **Settled 2026-10-30 as a provisional default: DN B22 (reset restores every default).** | Nothing now (was: O3 behaviour) |
| OQ-7 | Options are one global row, not per viewer. Confirm. **Settled 2026-10-30 as a provisional default: DN B23 (one global setting).** | Nothing now (was: O3) |
| OQ-8 | After unlock, who reads highlight rows (proposed: owner only), and may a photo's reader see that it was a highlight photo (`highlight_id`)? Nothing in the docs said. **Settled 2026-10-30: owner only. Highlight rows: DN B24 (provisional). `photo.highlight_id`: FS §20 DD (decided), enforced as in §4 item 4.** | Nothing now (was: O4 policy) |
| OQ-9 | At exactly `ends_at` the highlight is closed (half-open, like P1:47). Confirm (B16 settles only the note's 15:00 edge). **Settled 2026-10-30 as a provisional default: DN B25 (closed at exactly the end time).** | Nothing now (was: capture(), R-040) |
| OQ-10 | Under B2 `after_reveal_finished`, does "no one but the owner reads it" (`FS:291`, `DN:21`) also cover the journey, chapter and feeling-tag rows that §20 T opens to the network at unlock? **Settled 2026-10-30, FS §20 X: no. The network reads them from unlock under both settings; `b2` does not govern them (§3).** | Nothing now (was: RLS on 3 tables under one switch setting) |
| OQ-11 | **Conflict:** DN B9 (d) (`DN:28`, a chapter filter on the Positivity Feed, which public readers use) against FS §20 T (`FS:296`, chapters never public). Related: B9 (c) selects feed entries by feeling tag, so a public reader learns that a journey carries one of the four working tags. **Settled 2026-10-30: FS §20 Y (no chapter filter) and FS §20 CC (the feed may select by feeling tag but never shows the tag to a public reader).** | Nothing now (was: Positivity Feed query, Phase 4) |
| OQ-12 | The prototype's viewer identity is a per-transaction setting, so anyone with the app role can act as any user (C11, C16). Acceptable for the local prototype. Real authentication is needed before any deploy | Deploy (host still open) |
| OQ-13 | DN C17 (the next-unlock jump and other users' dates) is still open, with no default. Built as P1:195 says | Panel acceptance |
| OQ-14 | GC O6: **settled**, journey #6 (user ruling 2026-10-30) | Fixture load |
| OQ-15 | The time of day of each scripted action in P1 §3.8 is not given (fixture-designer). **Settled 2026-10-30, FS §20 BB: 12:00 UTC.** | Nothing now (was: fixture load, OQ-2) |
| OQ-16 | Who may EXECUTE `clock_jump()` (and `clock_jump_to_next_unlock()`) and `set_option()` in the running prototype? The docs give a panel (C16) and say the switches change only through `set_option()` (FS §20 Z), but not which role calls them. Today the loader needs `clock_jump()` as `mj_app` (§2.2), so as written any acting viewer can jump the clock and flip a switch. The other reading is a separate panel role that the app's viewer connection lacks. Not picked. Reset already runs only as `mj_owner` (§2.3). **Settled 2026-10-30, FS §20 EE (`FS:309`): a separate panel role only.** Carried as `mj_panel` (§2.1, §1.3, §3). How the loader, the scripted actions and the tests use it (connect as `mj_panel`, act through `SET LOCAL ROLE mj_app`, §1.4, §1.5, §2.2) was a lead-tech proposal derived from EE and O2; **approved 2026-10-30, FS §20 II (`FS:313`)**. Before this round the cell also said "the loader runs as that role for clock_jump", which was not in the ruling | Nothing now (was: grants on three functions, Phase 3; panel acceptance) |
| OQ-17 | `viewer_in_network(owner_id)` cannot be limited to policies (§5, tested): any viewer can call it directly and, by looping over users, list whose maps they are on. R-070 forbids a call that takes a member and returns owners; this one takes an owner. The same answer already follows from reading each owner's journey rows under §20 T, so it adds no fact. Accept, or does the rules-guardian or the user want a different reading of R-070? **Settled 2026-10-30, FS §20 FF: accepted.** | R-070 test wording; nothing in the schema |
| OQ-18 | **Order within one capture date, for a non-owner (FS §20 GG).** Non-owners get the date only (§4 item 5). Photo ids are sequential, so ordering a day's photos by id gives capture order; the docs do not say whether order counts as "time" (gate r4 NB-22, SI OQ-46). A sharper case: if ids come from one sequence shared by all users, a non-owner who knows the full times of their own photos can bound another user's capture time between two of their own ids. Not picked: neither the order rule nor the id type (P1 gives `id` no type) **Settled 2026-10-30, FS §20 JJ (order) and LL (note time). Carried: §4 item 6 (random uuid ids, order `(captured_on, id)`) and §4 item 5 (vi).** | Phase 4 path order (S-06, S-17); the id type of `photo` and `note` before Phase 3 if the shared-sequence case is to be closed |
| OQ-19 | **Time in image metadata.** A device photo or a photographed note can carry its capture time inside the image file (for example EXIF). FS §20 GG gives non-owners no time. The fixture's generated placeholders carry none (P1:256), so the prototype's data does not leak. Whether real captures strip it at capture or when served to a non-owner is not settled; either satisfies GG, and they differ only in what the owner's stored file keeps **Settled 2026-10-30, FS §20 KK: stripped at capture. Carried: §6, P1:91.** | Real capture (Phase 4 or later); nothing in the Phase 3 schema |
| OQ-20 | **Catalog statistics show sealed activity** (found 2026-10-30 while testing JJ, `mj_scratch_jj`). Any role can read `pg_stat_user_tables` and `pg_class.reltuples`. As user A, `n_tup_ins` on `photo` went 61 → 62 when C captured into a sealed journey, so A learned that someone captured, and when, and the table's total (A could read 61 photos). Revoking EXECUTE on `pg_stat_get_*` from PUBLIC closed `pg_stat_user_tables` (tested: `permission denied for function pg_stat_get_tuples_inserted`); `pg_class.reltuples` still read 62 after ANALYZE. No doc covers catalog side channels; random ids do not close it. How far to go (revoke statistics functions, restrict `pg_class` columns, or accept for the local prototype as with OQ-12) is not picked | Phase 3 schema grants; R-002, R-010 test wording |

---

## 9. §2.5 check 6 as a token scan (gate r4 NB-10)

**Problem.** Check 6 (`P1:181`; R-100 `RR:772–776`) bans "view" among other words. A substring scan of the approved schema fails on `journey_overview`, `viewer()` and `viewer_in_network()` (tested below), and a scan of object kinds would fail on the SQL view `photo_read`, whose name has no banned word. A pure whole-token match misses names Postgres folds to lower case, such as an unquoted `viewCount` stored as `viewcount` (tested below).

**Amendment (wording of the check; no schema change).** The scan reads every identifier in the catalog outside `pg_*` and `information_schema`: schemas, relations (tables, views, sequences, indexes, types), columns, functions and their argument names, types, enum labels, constraints, non-internal triggers and policies. It splits each into lower-case tokens at non-letters (`_`, digits) and at lower-to-upper case changes. A token fails if it **contains** one of check 6's words (`comment`, `repl(y|ie)`, `like`, `reaction`, `caption`, `score`, `rank`, `streak`, `badge`, `view`, `follower`), **unless the whole token is on a closed allow-list**: today `viewer` (`viewer()`, `viewer_in_network()`) and `overview` (`journey_overview`). Adding a token to the allow-list is a schema change reviewed by the rules-guardian. A SQL `VIEW` object is not itself a banned word; only names are scanned. R-100's extra words (`heart`, `impression`) are the rules-guardian's to add to the list.

```sql
WITH ids(kind, name) AS (
  SELECT 'schema', nspname FROM pg_namespace WHERE nspname NOT LIKE 'pg\_%' AND nspname <> 'information_schema'
  UNION ALL SELECT 'relation', c.relname FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE n.nspname NOT LIKE 'pg\_%' AND n.nspname <> 'information_schema'
  UNION ALL SELECT 'column', c.relname || '.' || a.attname FROM pg_attribute a JOIN pg_class c ON c.oid = a.attrelid
    JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE a.attnum > 0 AND NOT a.attisdropped AND n.nspname NOT LIKE 'pg\_%' AND n.nspname <> 'information_schema'
  UNION ALL SELECT 'function', p.proname FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
    WHERE n.nspname NOT LIKE 'pg\_%' AND n.nspname <> 'information_schema'
  UNION ALL SELECT 'argument', p.proname || '(' || a || ')' FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace,
    unnest(p.proargnames) a WHERE n.nspname NOT LIKE 'pg\_%' AND n.nspname <> 'information_schema'
  UNION ALL SELECT 'type', t.typname FROM pg_type t JOIN pg_namespace n ON n.oid = t.typnamespace
    WHERE n.nspname NOT LIKE 'pg\_%' AND n.nspname <> 'information_schema'
  UNION ALL SELECT 'enum label', enumlabel FROM pg_enum
  UNION ALL SELECT 'constraint', c.conname FROM pg_constraint c JOIN pg_namespace n ON n.oid = c.connamespace
    WHERE n.nspname NOT LIKE 'pg\_%' AND n.nspname <> 'information_schema'
  UNION ALL SELECT 'trigger', tgname FROM pg_trigger WHERE NOT tgisinternal
  UNION ALL SELECT 'policy', polname FROM pg_policy
), tokens AS (
  SELECT kind, name, lower(tok) AS tok FROM ids,
    regexp_split_to_table(regexp_replace(name, '([a-z0-9])([A-Z])', '\1_\2', 'g'), '[^A-Za-z]+') AS tok
  WHERE tok <> ''
)
SELECT kind, name, tok FROM tokens
WHERE tok ~ '(comment|repl(y|ie)|like|reaction|caption|score|rank|streak|badge|view|follower)'
  AND tok NOT IN ('viewer', 'overview')
ORDER BY 1, 2;   -- the check passes when this returns no row
```

**Evidence (throwaway database `mj_scratch_r5`, as in §4 item 5, since dropped).**

```
schema with photo_read (view), note_read (view), viewer(), viewer_in_network(), overview_readable(),
  journey_overview, photo_visibility                                    -> 0 rows (pass)
substring scan of the same schema for 'view'                            -> journey_overview, journey_overview_pkey,
                                                                           viewer, viewer_in_network (4 false failures)
planted in one rolled-back transaction: table photo_like (viewCount, reply_to, "viewedAt"), table "Comments",
  enum reaction_kind ('heart','liked'), function rank_users(), view photo_views, columns users.follower_ids, users.reviewer
                                                                        -> every planted name fails, including viewcount
                                                                           (folded), viewedAt, liked, photo_views; and
                                                                           reviewer, which needs an allow-list review
```
