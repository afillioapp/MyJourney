# Phase 1 Amendments: gate-1 items O1–O4, and rulings T and U

Status: **2026-10-30: O1, O2 accepted (no model change). O3 APPROVED by the user (Spec §20 Z). O4 APPROVED by the user (Spec §20 AA).** OQ-10 → Spec §20 X; OQ-11 → §20 Y and CC; OQ-16 → §20 EE, carried by the panel role (§2.1, §1.3; gate r4 B-3, rules r5 V1); OQ-17 → §20 FF (§5); OQ-1, 2, 4, 6, 7, 8, 9 → Decisions-Needed B20, B26, B21, B22, B23, B24, B25 (provisional); OQ-8's `photo.highlight_id` half → §20 DD, enforced in §4 item 4 (rules r4 V2, gate r3 B-2). §20 GG carried in §4 item 5 (gate r4 B-4, rules r5 V3); §20 HH in §3 and §5 (gate r4 CF-20, rules r5 V2). **§20 II–LL (user rulings 2026-10-30):** II, the loader and tests as `mj_panel`, approved (§1.4, §1.5, §2.1, §2.2); JJ in §4 item 6; KK in §6; LL in §4 item 5 (vi). FORCEd `highlight` RLS reconciled with the SECURITY DEFINER readers in §4 item 1. **§20 MM, NN (user rulings 2026-10-30):** MM in §10 (closes OQ-20), carried also in §2.1, §2.3, §4 items 1, 4, 5; NN in §6. **§20 OO–RR (user rulings 2026-10-30 on OQ-21–OQ-24):** OO in §11 (every user-content table behind a definer reader), carried also in §2.1; PP and QQ in §6; RR in §10 and §8 OQ-24. New for the user: OQ-25, OQ-26 (§8). Owner: lead-tech.

This file amends `Phase-1-Proposal.md` (P1, approved 2026-10-25) without editing it. Where P1 needs a matching line, §7 lists it for the supervisor to apply once the amendments are approved. Every amendment is the smallest change that closes its gate item. Nothing here redesigns §2.

Sources: `docs/reviews/2026-10-30-gate-1.md` (GC), P1 §2–§3, `Functional-Spec.md` (FS) §20 Q–RR (`FS:290–322`), `Decisions-Needed.md` (DN) provisional defaults, `Rules-Rubric.md` (RR). Stack: local Postgres 16 (decided 2026-10-30, DN D1). No deploy host is assumed.

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
| §20 KK | `capture()` and the note step strip time and location metadata before encrypting (§6); the database refuses any image that still carries it, as the second guard of FS §20 NN (§6) | R-154 | No |
| §20 LL | Already carried: `note_read` gives `written_at` to the owner only, no date to anyone else (§4 item 5 (vi)) | R-154 | No |
| §20 MM | The app role holds no privilege on `photo`, `note` or `highlight`; it reads them only through SECURITY DEFINER readers that start from rows it may read. Catalog statistics, row estimates, sizes, transaction and WAL counters, locks and other sessions are closed to it, and it can connect to no other database (§10) | R-002, R-010, R-154 | No table or field. Grants, three reader functions, one catalog hardening step run by the cluster superuser |
| §20 NN | `capture()` and the note step refuse, as their first step and before encryption, an image whose container is not fully walkable or carries any metadata segment (§6) | R-154 | No |
| §20 OO | The app role holds no privilege on any table with user content; each is read through one SECURITY DEFINER reader with a fixed `ROWS 1000`, journey first, applying exactly the table's current read rule, and written only through definer functions (§11) | R-002, R-010, R-154 | No table or field. Ten readers now, one waiting (`journey_reveal`, whose read rule two lines disagree on); grants. Two carried rules need the user's confirmation (OQ-25) |
| §20 PP | A guard refusal is a bug, never shown to the user; the build proves the strip step's output always passes; one press is one photo, never a retake (§6) | R-154 | No |
| §20 QQ | The strip step re-encodes every photo and note image to baseline JPEG; the guard accepts baseline JPEG only. **PNG is no longer accepted** (§6) | R-154 | No |
| §20 RR | Query timing that depends on rows the viewer cannot read is an accepted residual, revisited before real users (§10, OQ-24) | R-002, R-010 | No |

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
| `mj_app` | The app's viewer connections: every acting viewer, the C16 viewer switcher included | Exactly the grants in P1 §2.1 (`P1:44` "the app role"). No UPDATE, DELETE or TRUNCATE anywhere. Every rule applies to it. **No EXECUTE on `clock_jump()`, `clock_jump_to_next_unlock()`, `set_option()` or `clock_start()`, and not a member of `mj_panel`** (FS §20 EE). **No privilege of any kind on `photo`, `note` or `highlight`, no catalog statistics, row estimates or sizes, and CONNECT on the working database only** (FS §20 MM, §10). **Since FS §20 OO, no privilege on any table with user content: it reads through the §11 readers and writes through definer functions** (§11) |
| `mj_panel` | The prototype panel's control process (time control and switches, DN C16), the fixture loader (§2.2) and the schema tests (§1.4) (FS §20 II, `FS:313`). LOGIN; its credentials never reach a product screen or route (R-153) | EXECUTE on `clock_jump()`, `clock_jump_to_next_unlock()`, `set_option()` and `app_now()`; SELECT on `prototype_option` (it holds no user data, §3). The §10 catalog closures apply to it as to `mj_app` (both lose them through PUBLIC; tested natively and after `SET ROLE mj_app`). No other grant: on its own it reads and writes no product row. Membership `GRANT mj_app TO mj_panel WITH INHERIT FALSE, SET TRUE` (Postgres 16), so it gains a viewer's rights only after `SET ROLE mj_app`, and only for that span |

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
2. `CREATE DATABASE … TEMPLATE myjourney_baseline`, then `REVOKE ALL ON DATABASE … FROM PUBLIC; GRANT CONNECT ON DATABASE … TO mj_app, mj_panel`. A clone keeps every grant stored inside the database (the §10 catalog closures included) but not the database's own ACL, which starts again at the default that lets PUBLIC connect (tested, §10). The reset test checks the clone's ACL (FS §20 MM).
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
   - `mj_app` holds no privilege on `highlight` at all (FS §20 MM, §10; until 2026-10-30 it held SELECT, which let `EXPLAIN` show the table's row estimate). `start_highlight()` is the only writer. After unlock the owner reads highlight rows only through `highlight_rows()` (§10), which applies the seal rule above in its body, since `highlight_rules` lets every definer function from an app session see every row. `highlight_read` stays as a second guard should a grant ever be added.
   - Because `highlight_rules` opens the table to any `mj_owner` definer function called from an app or panel session, only these may name `highlight`. Proposed check (for the rules-guardian to number): list every function whose body names `highlight`; it fails on any other than `capture`, `start_highlight`, `highlight_open` and `highlight_rows` (the last added for FS §20 MM, §10).
   - Limit: `mj_owner` owns the table and could ALTER it, so against `mj_owner` itself the guard is that no product connection uses that role (§2.1). The same arrangement serves `layer` if it is FORCEd (§5).
2. **One new callable: `highlight_open(journey_id) → boolean`.** SECURITY DEFINER:
   - It returns whether `started_at <= app_now() < ends_at` for some highlight of that journey.
   - **For the owner only.** For anyone else, and for a journey id that does not exist, it raises the same refusal. A non-owner therefore cannot tell another user's journey from no journey (R-008's comparison against First Light).
   - It returns no time, no count and no id.
3. `capture()` and `start_highlight()` read highlight rows internally (SECURITY DEFINER) and still return only `accepted` or `refused` (P1:49).
4. **`photo.highlight_id` is readable by the owner only, also after unlock (FS §20 DD).** Before unlock the whole row is sealed (P1:48 a). Row-level security works per row and every viewer runs as `mj_app`, so neither RLS nor a plain column grant can tell the owner from another reader of the same row. It is enforced with no table or field change, in three parts: (i) `mj_app` has no SELECT on `photo.highlight_id` (since FS §20 MM no privilege on `photo` at all, §10; before that a column grant `(id, journey_id, image)` that left it and `captured_at` out), so any statement that names the table fails for every viewer; (ii) one SECURITY DEFINER function, `photo_highlight_id(photo_id)`, returns the id only when the viewer owns the photo's journey and `app_now() >= unlocks_at`, and NULL otherwise, including for an id that does not exist, so a non-owner gets the same NULL for a highlight photo, a normal photo and no photo; (iii) every reader, the owner included, reads photos through one view, `photo_read`, over the SECURITY DEFINER reader `photo_rows()` (FS §20 MM, §10; it was `security_invoker = true` over the table), which returns only rows for which `photo_readable(id)`, the same function as the photo policy, is true, and the granted columns, the two capture columns of item 5, and `photo_highlight_id(id) AS highlight_id`. Any other function that returns photo data returns `highlight_id` only through (ii). Highlight rows follow item 1 (B24). Residual, not covered by any ruling: many photos on one capture date can still suggest a highlight (R-151; narrowed by FS §20 GG from times to dates, not closed).
5. **A photo's capture time is readable by the owner only; everyone else gets the UTC date (FS §20 GG, `FS:311`; R-154).** Same pattern as item 4, no table or field change: (i) `mj_app` cannot read `photo.captured_at` (item 4 (i)) or `note.written_at` (since FS §20 MM it holds no privilege on `photo` or `note`, §10; before that, column grants that left both out), so naming, filtering or sorting on either fails for every viewer, the owner included; (ii) `photo_captured_at(photo_id) → timestamptz`, SECURITY DEFINER, returns the full time only when the viewer owns the photo's journey and `app_now() >= unlocks_at`, else NULL (also for an id that does not exist); (iii) `photo_captured_on(photo_id) → date`, SECURITY DEFINER, returns `(captured_at AT TIME ZONE 'UTC')::date` (B16: UTC) only when `photo_readable(photo_id)` is true, else NULL, so it is no oracle for sealed, private or missing photos; (iv) `photo_readable(photo_id) → boolean`, SECURITY DEFINER, is P1:48's photo read rule written once (seal, visibility, network, public, and the B2 term of §3). The photo SELECT policy is `USING (photo_readable(id))`, and the photo_visibility, reflection, note and person_tag policies use `photo_readable(photo_id)` (person_tag also C6, R-148), so the date function and the policies cannot drift. A direct call answers only what `SELECT … FROM photo_read WHERE id = …` already answers (the FS §20 FF reasoning). (v) `photo_read` returns `photo_captured_on(id) AS captured_on` and `photo_captured_at(id) AS captured_at` (NULL for anyone but the owner). (vi) **The note's written time goes to the owner only, and to no one else in any form, not even its date.** It is at most 15 minutes after capture (P1:108), so its time pins the capture time, and its date differs from the capture date when a photo is taken after 23:45 UTC, which pins that too. Notes are read through `note_read`, over the SECURITY DEFINER reader `note_rows()` (FS §20 MM, §10; it was `security_invoker = true` over the table), which returns only notes for which `photo_readable(photo_id)` is true: `id, photo_id, image, note_written_at(id) AS written_at`, where `note_written_at(note_id)` is SECURITY DEFINER and owner-only after unlock, like (ii). Screen-Inventory already shows no note written time or date to a non-owner (SI:54, :687). **This carries FS §20 LL (`FS:316`) as ruled: a non-owner never sees when a note was written, not even the date; the owner sees the full time.** The note's `id` is a random uuid (item 6), so no id order bounds it either. (vii) **Activity graph (B5, `PROVISIONAL: B5`).** Under `owner_only` only the owner sees it, built from the full time. Under `viewer_visible` it is built from the photos the viewer can read, through `photo_read`, so a non-owner's data has `captured_on` only: **no bucket finer than one UTC day** is possible from the data. Whether the graph shows days or something coarser is a Phase 4 display choice, not set here. The order within one day for a non-owner is item 6 (FS §20 JJ, was OQ-18); time in image metadata is §6 (FS §20 KK, was OQ-19).

6. **Ids, and same-day order for a non-owner (FS §20 JJ, `FS:314`; settles OQ-18).** No table or field change: P1 lists `id` with no type (P1:60, 70, 89, 104, 113, 122, 131), so this fills a blank and does not change the approved model.
   - **Every surrogate `id`** (user, journey, photo, note, reflection, journey_overview, highlight, announcement, and any other product table that has one) is `uuid DEFAULT gen_random_uuid()`, a random version-4 uuid. No product table has a sequence, `serial` or identity column. A time-ordered id (uuid v1 or v7, Postgres 18's `uuidv7()`, ULID, snowflake) is banned, since it carries its creation time. Proposed check (for the rules-guardian to number): `pg_sequences` in the product schemas is empty, no column is identity or defaults to `nextval`, and every stored `id` has version nibble `4`. `journey.seq` (P1:71) is a per-user field, not an id, and stays.
   - **The fixed order.** `photo_read` ends `ORDER BY photo_captured_on(id), id`: UTC capture date, then the random id. It is the same for every reader and every read, and carries no time within the day. Every other function or route that returns photos to a non-owner uses the same order; none relies on the table's physical order. `note_read` follows the photo order. Whether the owner's own screens re-sort by full time is a Phase 4 display choice: the owner already reads the time (FS §20 GG).
   - **What else could carry time, and what is closed.** `xmin` and `ctid` are refused on `photo` and `note` (they need table-level SELECT; since FS §20 MM `mj_app` holds no privilege on either, §10) and do not exist on the views (tested). Transaction-id and WAL counters, which move on every capture, are closed by §10.

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

**Stored format (FS §20 QQ, `FS:321`; settles OQ-23).** The strip step re-encodes every photo, and every note image, to a baseline JPEG: it decodes the image, keeps the pixels only, and writes a new file with an APP0 JFIF header, SOF0 at 8-bit precision, one scan, nothing after EOI, and no other segment (no EXIF, XMP, ICC, IPTC or comment, and never progressive). Re-encoding rather than cutting segments out means no unknown segment can survive. The fixture placeholders are generated as baseline JPEG too (P1:256).

**The database's second guard (FS §20 NN, `FS:318`, user ruling 2026-10-30).** Stripping (KK) runs before the database. As a second guard, the database itself refuses an image that still carries time or location metadata:

- **Where.** One function, `image_metadata_free(bytea) → boolean` (IMMUTABLE, no table access), called as the **first step of `capture()`**, before step 1 above, before the journey lock, before any count and **before encryption**, on the plaintext bytes; and as the first step of the note step, before the note's image is sealed under the journey key (P1:105). It cannot run later: after encryption the bytes are ciphertext, so no trigger on `photo` or `note` could read them. It therefore holds only if those two functions are the only writers, which §10 makes so: `mj_app` holds no INSERT on `photo` or `note` (FS §20 MM). A refusal raises an error (`check_violation`), so nothing is stored and no frame or highlight place is used.
- **What it accepts: an allow-list, not a deny-list, baseline JPEG only (FS §20 QQ).** It walks the whole container and returns true only for a **baseline JPEG**: SOI; then only DQT, SOF0 with 8-bit sample precision, DHT, DRI and an APP0 segment that begins `JFIF\0`; one SOS; entropy-coded data containing no marker other than RST0–7; and EOI as the last two bytes. Everything else is refused: APP1 (EXIF, which holds the date and GPS IFDs, and XMP), APP13 (IPTC), APP2 (ICC, whose header holds a date), any other APPn, COM, SOF1 (extended sequential) and SOF0 at 12-bit precision (neither is baseline), progressive JPEG (SOF2), bytes after EOI, and every other format (HEIC, WebP, …). **PNG acceptance is removed** (it was case (b) until 2026-10-30): the capture path never stores PNG under QQ, so the guard no longer accepts it, clean or not, for photos and notes alike. None of the allowed parts can hold a time or a place.
- **A refusal never reaches the user (FS §20 PP, `FS:320`; settles OQ-22).** The strip step runs before saving, so a refusal means the strip step is broken: it is a bug, not a state the product has. The capture screen therefore has no refusal message, and nothing invites a second press: one press is one photo, never a retake (CLAUDE.md banned list). The database side is unchanged: `capture()` and the note step raise `check_violation`, store nothing and use no frame or highlight place, so a bug can never be "fixed" by the user pressing again. What the app does with that press's image when the bug occurs is not settled (OQ-26). The build makes the bug unreachable for every sample: the check below requires the strip step's output for every sample to pass.
- **What the build runs** (proposed check, for the rules-guardian to number; fails the build): a fixed set of sample images generated by the test with a fixed seed is passed to `image_metadata_free()` and through `capture()` as the owner of a sealed journey, and through the note step as the owner of an unlocked photo. Clean baseline JPEG → `true`, `accepted`. JPEG with EXIF date, EXIF GPS only, XMP date, IPTC date, ICC, COM text, bytes after EOI, progressive scan, SOF1, 12-bit SOF0; PNG clean or with `tIME`, `tEXt`, `iTXt`, `eXIf`; WebP → `false`, and both functions raise and store no row (counts unchanged). **PP:** every decodable sample, after the QQ strip step → `true`, `accepted` by both; any `false` fails the build. Every fixture placeholder → `true` (P1:256).
- **Evidence, before FS §20 QQ** (throwaway `mj_scratch_mm`, local Postgres 16.15, 2026-10-30, since dropped; images made with Pillow 12.3.0, 64×48; PNG was still accepted then):

```
image                        size   image_metadata_free   capture() as owner of a sealed journey
jpeg_clean.jpg               677 B  t                     accepted
jpeg_exif_time_stripped.jpg  677 B  t                     accepted   (EXIF {306: '2026:05:01 23:47:12', ...} -> {})
png_clean.png                140 B  t                     accepted
jpeg_exif_time.jpg           783 B  f                     ERROR: image carries metadata (no row stored)
jpeg_exif_gps.jpg            767 B  f                     ERROR: image carries metadata
jpeg_xmp.jpg                 930 B  f                     ERROR: image carries metadata
jpeg_iptc.jpg                720 B  f                     ERROR: image carries metadata
jpeg_com.jpg                 703 B  f                     ERROR: image carries metadata
jpeg_trailer.jpg             697 B  f                     ERROR: image carries metadata
jpeg_progressive.jpg         539 B  f                     ERROR: image carries metadata
png_time.png                 159 B  f                     ERROR: image carries metadata
png_text.png                 182 B  f                     ERROR: image carries metadata
png_itxt.png                 394 B  f                     ERROR: image carries metadata
png_exif.png                 248 B  f                     ERROR: image carries metadata
other_webp.webp               82 B  f                     ERROR: image carries metadata
12-megapixel random-noise JPEG, 10.8 MB (worst case for the entropy scan): image_metadata_free -> t in 2.7 s
```

- **Evidence under FS §20 PP and QQ** (throwaway `mj_scratch_oo`, local Postgres 16.15, 2026-10-30, since dropped; roles dropped, cluster stopped). The same samples plus three new ones (ICC in APP2, SOF1, SOF0 at 12-bit, the last two made by patching the clean file's frame header). "Strip" is the QQ step: decode, keep pixels only, re-encode to baseline JPEG (Pillow 12.3.0, `progressive=False`). The guard runs first in `capture()` (owner of a sealed journey) and in the note step (owner of an unlocked photo); each accepted call is rolled back.

```
input                       guard  capture()                        note step
jpeg_clean.jpg              t      accepted                         accepted
jpeg_exif_time_stripped     t      accepted                         accepted
png_clean.png               f      ERROR: image carries metadata    ERROR: image carries metadata   <- PNG no longer accepted
jpeg_sof1 / jpeg_12bit      f f    ERROR (both)                     ERROR (both)
jpeg_icc                    f      ERROR                            ERROR
jpeg_exif_time, _exif_gps, _xmp, _iptc, _com, _trailer, _progressive; png_time, _text, _itxt, _exif; other_webp
                            f      ERROR (all 12)                   ERROR (all 12)
after the strip step: all 17 decodable inputs (every row above but jpeg_12bit, which no decoder opens)
                            t      accepted (17 of 17)              accepted (17 of 17)
photo and note rows before the run 201,136 and 20; after 201,136 and 20 (refusals stored nothing)
```

- **Settled 2026-10-30.** OQ-22 by FS §20 PP (`FS:320`), OQ-23 by FS §20 QQ (`FS:321`). Open from PP: OQ-26 (§8).

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
| 3, 45, 48 (h), 91, 105, 179, 180, 195 | Applied 2026-10-30 (fourth round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–NN; no app-role privilege on photo and note; sealed tables read only through definer readers, catalog statistics closed; image guard before encryption; check 4 through the read views plus the differential catalog test; check 5 gains the image samples; reset re-applies the database ACL | FS §20 MM, NN (§6, §10) |
| 3, 44, 45, 48 (h), 51, 91, 105, 168, 179, 180 | Applied 2026-10-30 (fifth round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–RR; append-only tables now hold no app-role privilege; every user-content table read only through definer readers with a fixed estimate, journey first; layer and announcement readers named; timing residual accepted until real users; baseline JPEG only, PNG removed, refusal is a bug and never a retake; check 4 on every user-content table; check 5 samples and the strip-step output | FS §20 OO, PP, QQ, RR (§6, §10, §11) |

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
| OQ-20 | **Catalog statistics show sealed activity** (found 2026-10-30 while testing JJ, `mj_scratch_jj`). Any role can read `pg_stat_user_tables` and `pg_class.reltuples`. As user A, `n_tup_ins` on `photo` went 61 → 62 when C captured into a sealed journey, so A learned that someone captured, and when, and the table's total (A could read 61 photos). Revoking EXECUTE on `pg_stat_get_*` from PUBLIC closed `pg_stat_user_tables` (tested: `permission denied for function pg_stat_get_tuples_inserted`); `pg_class.reltuples` still read 62 after ANALYZE. No doc covers catalog side channels; random ids do not close it. How far to go (revoke statistics functions, restrict `pg_class` columns, or accept for the local prototype as with OQ-12) is not picked **Settled 2026-10-30, FS §20 MM (`FS:317`): closed fully. Carried: §10 (every path found, closed and tested, including `EXPLAIN` estimates, `pg_stats`, sizes, transaction and WAL counters, locks, other sessions, and other databases). Residuals outside MM's wording: OQ-21, OQ-24.** | R-002, R-010 test wording (rules-guardian: `count(*)` on the table is now refused; the 0 is read through the views, §10) |
| OQ-21 | **Row estimates of tables the app role still reads directly** (found 2026-10-30 while carrying MM). FS §20 MM covers capture into a sealed journey, and §10 closes that. The same `EXPLAIN` path remains on every table `mj_app` still SELECTs with row-level security, because the planner's estimate counts rows the viewer cannot read. Tested on `reflection`: `EXPLAIN SELECT 1 FROM reflection` as viewer A read `rows=100` with 300 rows and `rows=300` with 900, none readable by A, so A learns that reflections were left, also on photos A cannot see (FS: "reflection left" is announced only to people who can see that photo). The same holds for `person_tag`, `photo_visibility`, `journey_overview`, `journey_reveal`, `announcement`, `layer` and `journey` (on `layer` the owner filter of its policy reduced the estimate to `rows=1` in the test, so no leak was seen there). Closing it is the §10 mechanism on every product table: no table privilege for `mj_app`, every read through a definer reader. Apply it to all tables, to some, or to none beyond MM is not picked **Settled 2026-10-30, FS §20 OO (`FS:319`): every table with user content. Carried: §11 (a reader per table, every table's privileges revoked, before/after tested). Three tables' read rules were never decided, only implied: OQ-25** | Nothing now but OQ-25 (was: Phase 3 grants on the non-sealed tables) |
| OQ-22 | **What the user sees when the NN guard refuses an image** (§6). Stripping (KK) runs first, so the guard fires only on a fault. As specified, `capture()` raises, nothing is stored and no frame is used, and the moment is lost unless the user presses again. Whether pressing again is allowed after a refusal (a "retake" in the banned list's sense?) and what the screen says is not in any doc **Settled 2026-10-30, FS §20 PP (`FS:320`): a refusal never reaches the user; the app strips before saving and a refusal is a bug; one press is one photo, never a retake. Carried: §6 (no refusal message, no second press; the build proves the strip step's output always passes). Left open by PP: OQ-26** | Nothing in Phase 3; Phase 4 capture screen waits on OQ-26 only |
| OQ-23 | **Which image formats the capture path stores.** The NN guard can prove only a baseline JPEG or a PNG clean (§6), so every other format is refused. Which format the KK strip step emits (for example, always re-encode to baseline JPEG) is not in any doc. The fixture placeholders are generated, so either works for Phase 3 **Settled 2026-10-30, FS §20 QQ (`FS:321`): baseline JPEG; the strip step re-encodes to it. Carried: §6. The guard accepts baseline JPEG only (SOF0, 8-bit); PNG acceptance is removed, for photos and notes; fixture placeholders are baseline JPEG** | Nothing now (was: real capture; fixture placeholder format) |
| OQ-24 | **Timing.** No statistic or estimate is left (§10), but the time a read takes can still depend on rows the viewer cannot read. §10 requires every definer reader to start from rows the viewer may read and reach sealed rows through an index: tested, a reader that scans every photo and filters went from 3.0 ms to 3,693 ms when another user's sealed journey grew by 200,000 photos, while the journey-first reader stayed at 0.6 ms. What is left is B-tree depth and cache state, below what the test could measure. FS §20 MM speaks of statistics and estimates, not time. Accept the residual, or require more (for example a separate database per sealed journey, which would close it fully but changes the storage design) is not picked **Settled 2026-10-30, FS §20 RR (`FS:322`): accepted for now, revisited before real users. Recorded in §10 as an accepted residual, with the revisit condition. Re-measured under OO on `reflection` (§11)** | Nothing in Phase 3. **Revisit before any real user's data enters the system** (the same point as OQ-12) |
| OQ-25 | **Read rules no doc decided, found while carrying FS §20 OO** (§11). OO moves each table's current read rule into a reader unchanged. For three tables the current rule was never decided, only implied. (a) **`user`** (`name`, `profile_picture`, `joined_at`): P1:45 gives it "the same grant" as P1:44 (SELECT) and P1 states no row rule, so today every viewer reads every user row, `joined_at` included. §11 carries exactly that in `user_rows()` (no behaviour change). Confirm, or rule a narrower set. (b) **`journey_reveal`: two lines disagree.** P1:45 gives the app role the same SELECT, with no row rule, so any viewer would read whether any journey's reveal is finished. This file, §3 (B2 term), says the app role holds no grant on `journey_reveal` for that purpose, "so no direct call tells a stranger whether a journey's reveal is finished". The owner certainly reads it (Screen-Inventory S-04 and the finish screen are the owner's, SI:153, :503). Not picked: §11 writes no `journey_reveal` reader until this is ruled, so after OO the app role reads no reveal row at all (state "revealing" or "revealed" is not readable through the app role meanwhile). (c) **`announcement`, the actor's own**: R2 as written shows "journey launched" and "path crossed" to the actor's network, which never contains the actor (tags exclude oneself, P1:156), and "reflection left" to readers of the photo, which includes the actor. So the actor reads their own reflection-left announcements but not their own launched or crossed ones. §11 carries that unchanged; confirm it is intended | (b) blocks the Phase 3 `journey_reveal` reader, and the owner's reveal state behind it. (a), (c) block nothing: carried as they are |
| OQ-26 | **What happens to the pressed image when the guard refuses it** (FS §20 PP leaves it). PP rules that the user never sees a refusal and that one press is one photo. If the bug occurs anyway, either (a) that press yields no photo, silently, which breaks "one press is one photo"; or (b) the app strips the same bytes again and resubmits them as the same press, which keeps one photo per press but stores a `captured_at` a moment later than the press. Not picked | Phase 4 capture screen; not the Phase 3 schema |

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

---

## 10. FS §20 MM: database statistics never leak activity (settles OQ-20)

Ruling (`FS:317`, user 2026-10-30, the strictest option, "close it fully"): the app role cannot read catalog statistics or row estimates that would show capture into a sealed journey. This applies to `mj_app` and to `mj_panel`, natively and after `SET ROLE mj_app` (§2.1). No table or field changes.

**Paths found, all tested as `mj_app` (viewer A) while user C captured into C's sealed journey** (throwaway `mj_scratch_mm`, as approved before this section):

| Path | What A saw before | Closed by |
|---|---|---|
| `pg_stat_user_tables`, `pg_stat_all_*`, `pg_statio_*`, `pg_stat_xact_*`, `pg_stat_database`, `pg_stat_io`, `pg_stat_wal`, `pg_stat_slru`, `pg_stat_bgwriter`, `pg_stat_get_*()` | `photo` `n_tup_ins` 101; per-table live tuples, inserts since vacuum, last vacuum and analyze times, scans; per-database inserts and commits | (b) |
| `pg_stat_activity` (`pg_stat_get_activity`) | sessions in the working database; all viewers share `mj_app`, so other viewers' query text too | (b) |
| `pg_locks` (`pg_lock_status`), `pg_blocking_pids`, `pg_try_advisory_*` | the advisory lock `capture()` holds on C's journey (§6 step 2) while C captures | (b) |
| `pg_class.reltuples`, `relpages`, `relallvisible`, `relfrozenxid`, `relminmxid` (table, index, TOAST) | `photo` 101 rows, `photo_pkey` 101 | (b) |
| `pg_database.datfrozenxid`, `datminmxid` | moved after the vacuum that inserts trigger | (b) |
| `pg_relation_size`, `pg_total_relation_size`, `pg_table_size`, `pg_indexes_size`, `pg_database_size`, `pg_tablespace_size` | `photo` 49,152 bytes in total; grew with C's capture | (b) |
| `pg_stats`, `pg_stats_ext`, `pg_stats_ext_exprs` | none for `photo` (row-level security hides it), but catalog tables' statistics change after the analyze that inserts trigger | (b) |
| `EXPLAIN` row estimates | `EXPLAIN SELECT id FROM photo` → `rows=34` (101 × ⅓); `… WHERE journey_id <> <A's journey>` → `rows=13`, about C's 40 sealed photos, because `=` on uuid is leakproof, so the planner used the column statistics despite row-level security | (a) |
| `xmin`, `ctid` | refused already (column grants only) | (a) |
| `txid_current()`, `pg_current_xact_id()`, `pg_current_snapshot()`, `pg_export_snapshot()`, `age(xid)`, `mxid_age`, `txid_status`, `pg_xact_status`, commit timestamps | the transaction counter moves on every capture | (b) |
| `pg_current_wal_lsn()`, `_insert_lsn`, `_flush_lsn` | the WAL position moves on every capture | (b) |
| Another database on the cluster (`postgres`, `template1`, PUBLIC CONNECT by default) | from there, `pg_stat_get_db_tuples_inserted(<working db>)` 966 → 967, `pg_stat_activity` 1 session in the working db, `pg_locks` 1 advisory lock, during C's capture | (c) |
| `pg_stat_statements`, `pgstattuple`, `pg_buffercache`, `pg_visibility`, `pageinspect` | available on the cluster, not installed; each would count calls or rows | (d) |

**Mechanism.**

- **(a) No privilege on the tables a sealed capture writes.** `mj_app` holds no privilege of any kind on `photo`, `note` and `highlight` (no SELECT, column or table; no INSERT). `EXPLAIN` needs the privileges of the statement it explains, so it is refused on them. The writers are `capture()`, the note step and `start_highlight()` (SECURITY DEFINER, as already). The readers are three SECURITY DEFINER set-returning functions owned by `mj_owner`, `photo_rows()`, `note_rows()` and `highlight_rows()`, each declared with a fixed `ROWS 1000`, under the views `photo_read` and `note_read` (same names and columns as §4 items 4–6) and, for the owner's highlight rows after unlock (B24), `highlight_rows()` directly. A planner cannot inline a SECURITY DEFINER function, so `EXPLAIN` on a view shows `Function Scan … rows=1000`, a constant, whatever the table holds. `photo_rows()` returns only rows for which `photo_readable(id)` is true, `note_rows()` only notes for which `photo_readable(photo_id)` is true (the same function as the policies, §4 item 5 (iv)), and `highlight_rows()` applies the B24 rule of §4 item 1. **Each reader starts from the journeys the viewer may read and reaches photos through the `journey_id` index**, never by scanning every row and filtering; otherwise the time a read takes counts sealed rows (OQ-24, measured). The row-level security policies stay, as a second guard should a grant ever be added.
- **(b) Catalog closures, in every product database.** One script, run by the cluster's bootstrap superuser when the template is built (pg_catalog belongs to it; `mj_owner` cannot change it). It is the only step not run by `mj_owner`, and it touches no product row. A template clone keeps it (tested):
  - `REVOKE EXECUTE … FROM PUBLIC` on every `pg_catalog` function named `pg_stat_get_*`, `pg_stat_have_stats`; `pg_lock_status`, `pg_blocking_pids`, `pg_safe_snapshot_blocking_pids`, `pg_isolation_test_session_is_blocked`; `pg_relation_size`, `pg_total_relation_size`, `pg_table_size`, `pg_indexes_size`, `pg_database_size`, `pg_tablespace_size`; `pg_current_wal_*`, `pg_last_wal_*`; `txid_current`, `txid_current_if_assigned`, `txid_current_snapshot`, `txid_status`, `pg_current_xact_id`, `pg_current_xact_id_if_assigned`, `pg_current_snapshot`, `pg_xact_status`, `pg_export_snapshot`, `pg_xact_commit_timestamp`, `pg_xact_commit_timestamp_origin`, `pg_last_committed_xact`, `mxid_age`, `age(xid)`; `pg_advisory_*`, `pg_try_advisory_*`. Then `GRANT EXECUTE ON FUNCTION pg_advisory_xact_lock(bigint) TO mj_owner`, for `capture()`'s lock.
  - `REVOKE SELECT ON pg_stats, pg_stats_ext, pg_stats_ext_exprs FROM PUBLIC`.
  - `REVOKE SELECT ON pg_class FROM PUBLIC`, then `GRANT SELECT (<every column but reltuples, relpages, relallvisible, relfrozenxid, relminmxid>) ON pg_class TO PUBLIC`; the same on `pg_database` without `datfrozenxid`, `datminmxid`. `pg_class` stays readable by name, kind and oid, so `'photo'::regclass`, `to_regclass()` and `\dt` still work (tested); only `SELECT *` on these two catalogs fails for the app role.
- **(c) One database.** `REVOKE ALL ON DATABASE <working> FROM PUBLIC; GRANT CONNECT … TO mj_app, mj_panel`, re-applied after every clone (§2.3: a clone does not keep the database's own ACL, tested). On the cluster, `REVOKE CONNECT, TEMPORARY ON DATABASE postgres, template1 FROM PUBLIC`; the template `myjourney_baseline` already allows no connection (§2.2). Tested on a second throwaway database: after the revoke, `mj_app` and `mj_panel` get `permission denied for database`.
- **(d) Extensions.** `pg_extension` in the product database holds only `plpgsql` and the extension the encryption uses, if any (P1:48 (b); its choice is the developer's). `shared_preload_libraries` loads none of `pg_stat_statements`, `auto_explain`, `pg_buffercache`, `pgstattuple`, `pg_visibility`, `pageinspect`.

**What breaks:** nothing the app needs. Tested after (a)–(c): `capture()` → `accepted` (its advisory lock works); A sealed: `count(*)` through `photo_read`, `note_read` and `highlight_rows()` → 0, 0, 0; after unlock A reads its 62 photos through `photo_read`, B reads 0; `'photo'::regclass`, `to_regclass('photo_read')` and psql `\dt` work. What the app role loses: `count(*)` and `SELECT` on the three tables themselves (refused, not 0), the statistics views, and `SELECT *` on `pg_class` and `pg_database`.

**Checks (proposed, for the rules-guardian to number; each fails the build):**

1. **Differential catalog test.** As `mj_app` (and again as `mj_panel`, natively and after `SET ROLE mj_app`), in one session: fingerprint (md5 of the sorted rows) every `pg_catalog` and `information_schema` relation the role may SELECT, and every `pg_catalog` function it may EXECUTE that takes no argument or one `oid`/`regclass` argument, called on `photo`, its primary key, its TOAST table, `note`, `highlight` and the database. Then, as another user through `mj_panel`: start a highlight and capture into that user's sealed journey, hold a second capture open, and run `VACUUM ANALYZE` as the superuser. Fingerprint again. The check passes when only the fixed allow-list differs: `now()`, `transaction_timestamp()`, `statement_timestamp()`, `clock_timestamp()`, `timeofday()`, `random()`, `gen_random_uuid()`.
2. **Named refusals.** As `mj_app`: `SELECT`, `count(*)`, `EXPLAIN` and `xmin` on `photo`, `note`, `highlight`; `reltuples`, `relpages` from `pg_class`; `datfrozenxid`; `pg_stats`, `pg_stats_ext`; every size function above; `txid_current()`, `pg_current_xact_id()`, `pg_current_wal_lsn()`, `age(xid)`; `pg_locks`, `pg_stat_activity`, `pg_try_advisory_xact_lock()` each raise `permission denied`. `EXPLAIN SELECT * FROM photo_read` shows `rows=1000` before and after a capture.
3. **Clone.** After reset (§2.3), the working database's ACL grants CONNECT to `mj_app` and `mj_panel` only, and neither role can connect to `postgres` or `template1`.
4. **Extensions** as in (d).

**Evidence (throwaway `mj_scratch_mm`, `mj_scratch_mm_other`, `mj_scratch_mm_clone`, local Postgres 16.15, 2026-10-30; databases and roles dropped, cluster stopped).** Before: the table above. Differential test: 1,024 probes answered before (a)–(b), 480 after (the rest now refuse):

```
before (a)-(b), as mj_app:   97 probes changed, among them pg_class, pg_database, pg_locks, pg_stat_activity,
                             pg_stat_user_tables, pg_stats, pg_stat_get_tuples_inserted('photo'),
                             pg_stat_get_live_tuples('photo'), pg_total_relation_size('photo'), pg_database_size,
                             pg_current_wal_lsn(), txid_current(), pg_current_snapshot(), pg_export_snapshot()
after, as mj_app:            7 changed: clock_timestamp() gen_random_uuid() now() random() statement_timestamp()
                             timeofday() transaction_timestamp()
after, as mj_panel (native): the same 7
after, mj_panel SET ROLE:    the same 7
EXPLAIN SELECT * FROM photo_read                 -> Function Scan on photo_rows (rows=1000)
EXPLAIN SELECT * FROM photo                      -> ERROR: permission denied for table photo
SELECT reltuples FROM pg_class                   -> ERROR: permission denied for table pg_class
SELECT relname, relkind, oid FROM pg_class ...   -> photo | r | 17313
txid_current() / pg_current_wal_lsn() / age(xid) -> ERROR: permission denied for function ...
pg_locks / pg_stat_activity                      -> ERROR: permission denied for function pg_lock_status / pg_stat_get_activity
clone of the hardened database: datacl NULL (PUBLIC may connect); txid_current() and pg_class.reltuples still refused
```

**Accepted residual: query timing (FS §20 RR, `FS:322`, user ruling 2026-10-30; settles OQ-24).** With every reader journey-first (§10 (a), §11), the time a read takes can still depend slightly on rows the viewer cannot read: B-tree depth and cache state. This is accepted for the prototype on dummy data. **Revisit condition: before any real user's data enters the system**, the same point at which real authentication must replace the per-transaction viewer (OQ-12). At that point the options listed in OQ-24 (for example a separate database per sealed journey) go back to the user. The journey-first rule itself is not relaxed: a reader that scans a whole table and filters is a build failure (§11 check 2). Re-measured under OO (§11): `reflection_rows()` 2.9 ms → 4.7 ms while 200,000 reflections the viewer cannot read were added; a scan-and-filter reader over the same rule 58 ms → 17,746 ms.

**Model change:** none. No table or field. Three definer reader functions, grants, one catalog script and the database ACL. It changes the read path of §4 items 4–6 (from `security_invoker` views over the tables to views over definer readers) and §4 item 1 (`mj_app` no longer holds SELECT on `highlight`).

---

## 11. FS §20 OO: every table with user content is read only through definer readers (settles OQ-21)

Ruling (`FS:319`, user 2026-10-30): every table with user content, not only sealed content, is read only through definer readers with fixed row estimates. This is §10's mechanism (a) applied to every such table. No table, field or read rule changes: each reader applies exactly the predicate of the table's current policy.

**The tables, and their readers.** Every object of P1 §2.2 and every record of P1 §2.4 that holds something a user made or did:

| Table | Reader (SECURITY DEFINER, `ROWS 1000`) | Read rule, unchanged | Rule from | Starts from |
|---|---|---|---|---|
| `user` | `user_rows()` | Every viewer, every row: the P1:44–45 grant with no row rule (confirm: OQ-25 (a)) | P1:45 | The table: this rule reads every row |
| `journey` | `journey_rows()` | The owner, always (sealed: type and dates only, P1:84); the owner's network from unlock (FS §20 T, X) | P1:84, §5 | The viewer's journeys by `user_id`; network owners by `layer(member_id)`, then `journey(user_id)` |
| `photo` | `photo_rows()`, view `photo_read` | `photo_readable(id)` | §4 items 4–6, §10 | Readable photos (below) |
| `note` | `note_rows()`, view `note_read` | `photo_readable(photo_id)` | §4 item 5 (vi) | Readable photos |
| `highlight` | `highlight_rows()` | The owner, from unlock (`PROVISIONAL: B24`) | §4 item 1 | The viewer's journeys |
| `reflection` | `reflection_rows()` | `photo_readable(photo_id)` (D11) | P1:117, §4 item 5 (iv) | Readable photos |
| `journey_overview` | `journey_overview_rows()` | `overview_readable(journey_id)` (FS §20 HH) | §5 | Readable journeys |
| `journey_chapter` | `journey_chapter_rows()` | From unlock, the owner and the network (FS §20 T, X) | §5 | Readable journeys |
| `journey_feeling_tag` | `journey_feeling_tag_rows()` | The same | §5 | Readable journeys |
| `person_tag` | `person_tag_rows()` | `photo_readable(photo_id)`, and the photo's owner only unless `c6 = shown` (`PROVISIONAL: C6`, R-148) | §3, §4 item 5 (iv) | Readable photos |
| `photo_visibility` | `photo_visibility_rows()` | `photo_readable(photo_id)` | §4 item 5 (iv) | Readable photos |
| `layer` | `layer_rows()` | `owner_id = viewer()` | P1:51 | `layer(owner_id)` |
| `announcement` | `announcement_rows()`, §3's "announcement read function" (no subject under `b11 = unnamed`, R-146) | Launched and crossed: the actor's network; reflection left: readers of the photo (D18, R2) (confirm the actor's own: OQ-25 (c)) | P1:168, §3 | Network owners, then `announcement(actor)`; readable photos, then `announcement(subject photo)` |
| `journey_reveal` | **None yet** | **Not picked: two lines disagree (OQ-25 (b))** | P1:45 against §3 | |

"Readable journeys" are the viewer's own and those of owners whose map holds the viewer. "Readable photos" are the photos of those journeys, by the `journey_id` index, plus public photos through a partial index on `photo_visibility` where the setting is public; both then filtered by `photo_readable()`. The starting set always contains every row the predicate allows, so the start only decides how much is read, never what is returned (tested below).

Not user content, unchanged: `journey_type` and `chapter` (constants and catalogue), `prototype_option` (settings, §3), `sim_clock` (§1.1), `journey_key` (no privilege and no reader; only the key-release function, P1:48 (b)).

**Mechanism.**

- **Privileges.** `REVOKE ALL` on every table above from `mj_app`, `mj_panel` and PUBLIC. `SELECT`, `count(*)`, `EXPLAIN`, `xmin` and `ctid` on any of them are refused.
- **Readers.** As §10 (a): owned by `mj_owner`, SECURITY DEFINER, fixed `search_path`, `ROWS 1000`, EXECUTE for `mj_app` only. `EXPLAIN` on any of them shows `rows=1000` whatever the tables hold.
- **Internal helpers** (the network owners of the viewer, the readable journeys, the readable photo ids): no EXECUTE for `mj_app` or `mj_panel` (tested). One of them takes the viewer, a member, and returns owners. Neither role can call it, so P1:51 ("Nothing callable takes a member and returns an owner") holds. The readers that use it return only rows the policies already returned (FS §20 FF).
- **Writers.** The app role holds no INSERT either. Every insert goes through a SECURITY DEFINER function: `capture()`, the note step, `start_highlight()`, `commit()`, the join, `finish_reveal()` (which writes `journey_reveal`, `layer` and `announcement`, P1 §2.3), the reflection insert function (P1:52), and one function for each reveal-choice insert (visibility, person tag, chapter, feeling tag) and for the overview. Each carries in its body the check its insert policy carried. The insert-only triggers (P1:44–46, the 15-minute note rule, the slot uniqueness) stay on the tables and fire for every writer. No UPDATE, DELETE or TRUNCATE path exists, as before. The function names are the developer's.
- **Policies stay** on every table as a second guard, should a grant ever be added. The Positivity Feed query is another definer reader of the same kind; its selection rules are unchanged (FS §20 W, Y, CC; DN B9).
- **FS §20 FF unchanged.** `viewer_in_network()`, `overview_readable()` and `photo_readable()` stay executable by `mj_app`. §5's reason for that (a policy's functions are checked as the querying role) no longer applies once no policy is evaluated for `mj_app`. The grants stay because FF allows them and no ruling asks to remove them.

**Where OO meets an existing rule.**

1. **P1:44** "The app role has INSERT and SELECT only" (reflections, overviews), and P1:45's "same grant": superseded. The app role holds neither. Append-only is unchanged and stronger, since no direct write exists at all. P1:44–45 amended in line.
2. **P1:48 (a) and CLAUDE.md, "`count(*)` returns 0"**: on every user-content table `count(*)` is now refused, not 0. The 0 is read through the readers, as MM already did for photo and note (check 4). Rubric tests that query a table directly (R-002, R-010, and any test of tag, reflection or layer rows by table name) need rewording, which is for the rules-guardian.
3. **`journey_reveal`**: P1:45 against this file's §3 (OQ-25 (b)). Not picked.
4. **§2.5 check 7** ("no layer row with owner ≠ B is readable") now reads through `layer_rows()`; the table refuses.

No other conflict was found. The equivalence test below shows every reader returning exactly what its policy returned, under both settings of `b2` and of `c6`.

**Checks (proposed, for the rules-guardian to number; each fails the build):**

1. **No privilege.** For `mj_app`, `mj_panel` and PUBLIC, no table or column privilege of any kind on any table in the product schema, other than SELECT on `journey_type`, `chapter` and `prototype_option`. A new table fails the build until it is added to that short list or given a reader.
2. **Fixed estimate, journey first.** Every set-returning function `mj_app` may EXECUTE is SECURITY DEFINER with `prorows = 1000`. `EXPLAIN SELECT * FROM` each reader shows `rows=1000` before and after the activity of §10 check 1. With `enable_seqscan = off`, the plan of each reader's body, run as `mj_owner` with a fixture viewer set, has no sequential scan on a user-content table other than `user` (whose rule reads every row).
3. **Same rows as the policy.** For each fixture viewer, at several clock points, under every setting of `b2` and `c6`, each reader returns exactly the table rows for which the table's policy expression is true, evaluated by the test as the table owner with that viewer set.
4. **Differential catalog test** of §10 check 1, with its targets extended to every user-content table and its primary key.

**Evidence (throwaway `mj_scratch_oo`, local Postgres 16.15, 2026-10-30; database and roles dropped, cluster stopped).** Roles as §2.1, the §10 catalog closures applied. Users: A (the viewer), B (on A's map and on C's), C (an unlocked journey with 300 photos, 290 private), D (a stranger), E. User ids are text stand-ins. To measure estimates, the scratch used `user_rows()` as every row and a `journey_reveal` reader limited to the owner as stand-ins; neither settles OQ-25.

```
BEFORE OO: photo, note, highlight behind readers (MM); the other 11 tables SELECT under their policies.
As mj_app, viewer A: EXPLAIN SELECT * FROM <table>; then 40 new users on no map that holds A commit 20 sealed
journeys and reveal 20 journeys with private photos, reflections, tags, chapters, feeling tags, overviews, maps and
announcements, plus 200 reflections on C's private photos; ANALYZE; EXPLAIN again.
  journey 3 -> 9 (the 20 sealed commits show)   journey_reveal 1 -> 11   journey_chapter 1 -> 8
  journey_feeling_tag 1 -> 8   journey_overview 1 -> 8   photo_visibility 103 -> 170   person_tag 1 -> 24
  reflection 42 -> 172   announcement 41 -> 51   app_user 5 -> 45   layer 1 -> 1
  None of the new rows is readable by A, except the 40 user rows under the stand-in.

SAME ROWS: for viewers A, B, C, D, E, F21 x b2 (from_unlock, after_reveal_finished) x c6 (hidden, shown) x 11 tables,
  count and md5 of the sorted rows through the policy vs through the reader -> 264 identical, 0 differing
  A under b2 from_unlock / after_reveal_finished: journey 3 / 3, chapter 2 / 2 (FS §20 X), overview 2 / 1 (FS §20 HH),
  photos 20 / 14, reflections 20 / 14 (B's unfinished journey waits)

AFTER OO (REVOKE ALL on the 15 tables from mj_app, mj_panel, PUBLIC):
  table grants left 0; column grants left 0
  SELECT count(*) FROM reflection; SELECT xmin FROM journey; INSERT INTO reflection; UPDATE journey_overview;
  DELETE FROM person_tag; TRUNCATE layer                    -> ERROR: permission denied for table ...
  EXPLAIN on each of the 15 tables                          -> ERROR: permission denied for table ...
  EXPLAIN on the 10 readers, the journey_reveal stand-in, photo_read, note_read -> rows=1000; after a second 40-user batch: identical
  network_owner_ids(), candidate_journey_ids(), readable_photo_ids() -> ERROR: permission denied for function ...
  as A through readers: journey 3, reflection 20, person_tag 4, layer 1, announcement 14, overview 2
  reflection writer on A's own photo -> accepted (reader count 20 -> 21); on another user's readable photo -> refused
  mj_panel without SET ROLE: SELECT reflection / EXPLAIN journey / reflection_rows() -> ERROR: permission denied
  differential catalog test (§10 check 1, targets extended to the 15 tables and reflection_pkey), one session,
  around a third batch and VACUUM ANALYZE:
    mj_app: 1,090 probes answered; changed only clock_timestamp() gen_random_uuid() now() random()
            statement_timestamp() timeofday() transaction_timestamp()
    mj_panel native, and after SET ROLE mj_app: the same 1,090; the same 7
  timing (RR): reflection_rows() 2.9 ms -> 4.7 ms after 200,000 reflections A cannot read;
               scan-and-filter reader 58 ms -> 17,746 ms
```

The reflection written by the writer test was removed afterwards by the cluster superuser, in the scratch database only.

**Model change:** none. No table or field. Ten reader functions now and one waiting on OQ-25 (b), internal helpers, writer functions for the inserts the app role made directly, and grants. It changes the read path of every user-content table, and the write path of the tables the app role used to insert into directly.
