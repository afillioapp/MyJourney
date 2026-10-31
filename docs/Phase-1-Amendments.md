# Phase 1 Amendments: gate-1 items O1–O4, and rulings T and U

Status: **2026-10-30: O1, O2 accepted (no model change). O3 APPROVED by the user (Spec §20 Z). O4 APPROVED by the user (Spec §20 AA).** OQ-10 → Spec §20 X; OQ-11 → §20 Y and CC; OQ-16 → §20 EE, carried by the panel role (§2.1, §1.3; gate r4 B-3, rules r5 V1); OQ-17 → §20 FF (§5); OQ-1, 2, 4, 6, 7, 8, 9 → Decisions-Needed B20, B26, B21, B22, B23, B24, B25 (provisional); OQ-8's `photo.highlight_id` half → §20 DD, enforced in §4 item 4 (rules r4 V2, gate r3 B-2). §20 GG carried in §4 item 5 (gate r4 B-4, rules r5 V3); §20 HH in §3 and §5 (gate r4 CF-20, rules r5 V2). **§20 II–LL (user rulings 2026-10-30):** II, the loader and tests as `mj_panel`, approved (§1.4, §1.5, §2.1, §2.2); JJ in §4 item 6; KK in §6; LL in §4 item 5 (vi). FORCEd `highlight` RLS reconciled with the SECURITY DEFINER readers in §4 item 1. **§20 MM, NN (user rulings 2026-10-30):** MM in §10 (closes OQ-20), carried also in §2.1, §2.3, §4 items 1, 4, 5; NN in §6. **§20 OO–RR (user rulings 2026-10-30 on OQ-21–OQ-24):** OO in §11 (every user-content table behind a definer reader), carried also in §2.1; PP and QQ in §6; RR in §10 and §8 OQ-24. **§20 SS–ZZ (user rulings 2026-10-31; OQ-25 → SS, TT, UU; OQ-26 → VV, XX; gate r5 NB-24 → WW, NB-26 → YY, rules r6 G-23 → ZZ):** SS and ZZ in §11 (`journey_reveal_rows()`, policy changed); TT in §11 (`user_rows()` column mask) and check 3 now tests column masks; UU with DN B10 in §11 (`announcement_rows()`, `PROVISIONAL: B10`); VV and XX in §6 (the retry runs inside the press transaction); WW in §3 (`b4`); YY in §11 (`user_rows()` returns no `profile_picture`). Also r6 N5 (§4 item 1, the R-156 scan) and N6 (§4 item 1, highlight rows insert-only; §11, the Positivity Feed order, OQ-28). **§20 AAA–DDD (user rulings 2026-10-31 on OQ-27, OQ-28, OQ-29 and Screen-Inventory OQ-48):** AAA in §6 (a retried press is stored at the press instant; VV's line on the stored time is retired); BBB in §11 (`positivity_feed_rows()` ends `ORDER BY written_at DESC, id` and returns no time); CCC in §11 and §3 `b4` (`ring_count(profile_id uuid) → integer`, the count only, for every viewer); DDD in §6 (a second refusal rolls the press back, stores no photo, and is logged in the server log, which no product role can read and which carries no image). OQ-27, OQ-28 and OQ-29 settled; P1 lines 3, 65, 91, 117, 164, 179, 180 carry them (§7). **§20 EEE–KKK (user rulings 2026-10-31 on OQ-30, OQ-31, OQ-32, gate r6 NB-27, rules r7 G-24 and Screen-Inventory OQ-44):** EEE and KKK need no change (§11); FFF accepts the log residual with OQ-12 (§6); GGG, whose "no note offer" part JJJ retires, and HHH, III and JJJ in §6 (the note step's retry inside its own transaction, its double refusal ending the step, and the note offered after a lost press and discarded), tested under §6 (`mj_scratch_r8`). OQ-30, OQ-31 and OQ-32 settled; P1 lines 3, 105, 180 carry them (§7). §11's table count corrected to 14 (gate r6 CF-36). **§20 LLL–OOO (user rulings 2026-10-31 on OQ-33, OQ-34, OQ-5):** LLL and NNN in §6 (the note handle: `capture()` hands the route the new photo's id in a transaction-local setting, the route keeps it per device session and acting user for one note transaction or until press + 15 minutes, and a lost press gets a handle that leads to "discard"); MMM in §6 and §8 OQ-12 (III held by the route only, an accepted residual); OOO in §2.2 (`join_user(name)` sets `joined_at = app_now()`; the loader joins each user at the P1 §3.2 instant). Tested under §6 and §2 (`mj_scratch_r9`). OQ-5, OQ-33 and OQ-34 settled; P1 lines 3, 49, 63, 105, 108, 176, 180, 213 carry them (§7). No model change. **§20 PPP–RRR (user rulings 2026-10-31 on OQ-35, rules r8 G-25 and rules r8 V2), with rules r8 N1, N3, N4 and N6:** PPP in §6 and §8 OQ-12 (a restart drops the route's handles: an accepted residual, the next note press is answered as a closed window); QQQ in §6 (`capture()` judges the §20 U order first and runs the image guard only on a press judged accepted, so a lost press is judged at the press instant and one that a normal press would refuse is answered `refused`; the "never computed" reading is retired); RRR in §6 (every "closed" note answer is one answer, the same as an ended window); N1 in §1.5 and §2.2 (the loader and the panel jump only to an instant still ahead); N3 in §6 (every note press runs one route shape; the residual is measured); N4 in §6 (the route writes no handle, press time or acting user); N6 in §8 ("Before real users"). Tested under §2 and §6 (`mj_scratch_r10`). OQ-35 and G-25 settled; P1 lines 3, 91, 105, 108, 180, 213 carry them (§7). No model change. **§20 SSS–ZZZ (user rulings 2026-10-31 on OQ-36, OQ-37, Screen-Inventory OQ-24, S-12 and OQ-49, rules r9 G-26 and gate r8 NB-31), with rules r9 V1–V3 and N1–N3 and gate r8 CF-41, CF-42 and CF-44:** SSS and TTT settle OQ-36 and OQ-37 as accepted residuals ("Before real users" items 7 and 8); UUU and VVV are screen rulings that the route already meets with its one `closed` answer and its `saved` answer (§6); WWW in §6 (the device's skip request: the route drops the entry when the user skips or leaves capture, so no later note press for that press is taken; rules r9 N2, R-173); XXX needs no change here (§11 `user_rows()` returns no `profile_picture`; P1:62); YYY in §6 (`add_note()` and the `note` trigger refuse once the journey is unlocked, and the route's window read is bounded by both press + 15 minutes and `unlocks_at`, so a note press after unlock gets the one `closed` answer; rules r9 N1, G-26); ZZZ in §6 (a note lost twice is answered `saved`, byte for byte as a saved note; gate r8 NB-31). Rules r9 N3 in §6 (the press's own timing, measured). Tested under §6 (`mj_scratch_r11`). P1 lines 3, 105, 108, 180 carry them (§7). The §7 tenth-round row is restored to the range lead-tech applied (rules r9 V3). No model change. **§20 AAAA, BBBB (user rulings 2026-10-31 on OQ-38, OQ-39):** AAAA accepts the extra strip's timing gap after a guard refusal for the prototype (§6 "The press's own timing"; "Before real users" item 9); BBBB accepts OQ-39 (a), a client that never sends the skip, with OQ-12 ("Before real users" item 10), and settles (b): a note-step refusal after the route read the window as open gets the one `closed` answer (§6 "The note press"), tested (`mj_scratch_r12`). OQ-38 and OQ-39 settled; P1 line 3 carries them (§7). No model change. Owner: lead-tech.

This file amends `Phase-1-Proposal.md` (P1, approved 2026-10-25) without editing it. Where P1 needs a matching line, §7 lists it for the supervisor to apply once the amendments are approved. Every amendment is the smallest change that closes its gate item. Nothing here redesigns §2.

Sources: `docs/reviews/2026-10-30-gate-1.md` (GC), P1 §2–§3, `Functional-Spec.md` (FS) §20 Q–BBBB (`FS:290–364`; dated at `FS:328` and `FS:366`, "*AAA–BBBB above were ruled on 2026-10-31.*"), `Decisions-Needed.md` (DN) provisional defaults, `Rules-Rubric.md` (RR). Stack: local Postgres 16 (decided 2026-10-30, DN D1). No deploy host is assumed.

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
| §20 NN | `capture()` and the note step refuse, before encryption and before any write, an image whose container is not fully walkable or carries any metadata segment. The note step runs the guard as its first step; `capture()`, since FS §20 QQQ, once the press is judged accepted (§6) | R-154 | No |
| §20 OO | The app role holds no privilege on any table with user content; each is read through one SECURITY DEFINER reader with a fixed `ROWS 1000`, journey first, applying exactly the table's current read rule, and written only through definer functions (§11) | R-002, R-010, R-154, R-158 | No table or field. Eleven readers, `journey_reveal_rows()` included since FS §20 SS (2026-10-31); grants. Before 2026-10-31 this cell gave ten readers and left `journey_reveal` without one (OQ-25, now settled by SS, TT, UU) |
| §20 PP | A guard refusal is a bug, never shown to the user; the build proves the strip step's output always passes; one press is one photo, never a retake (§6) | R-154 | No |
| §20 QQ | The strip step re-encodes every photo and note image to baseline JPEG; the guard accepts baseline JPEG only. **PNG is no longer accepted** (§6) | R-154 | No |
| §20 RR | Query timing that depends on rows the viewer cannot read is an accepted residual, revisited before real users (§10, OQ-24) | R-002, R-010 | No |
| §20 SS, ZZ | `journey_reveal_rows()` returns (`journey_id`, `finished_at`) to the owner and, after unlock, the owner's network, journey first; never to a public reader, and no other reader returns the reveal state to one as a field. The `journey_reveal` policy changes from "every row" to the same rule (§11) | R-162, R-152, R-158 | No table or field. One reader, one internal predicate, one policy |
| §20 TT | `user_rows()` returns `joined_at` on the viewer's own row only, NULL on every other row; §11 check 3 compares whole tuples, so it tests the mask (§11) | R-161, R-158 | No |
| §20 UU, DN B10 | `announcement_rows()`: the actor reads their own "reflection left"; everyone else reads it only as a member of the owner's network who can read the photo, even when the photo is public (`PROVISIONAL: B10`). "Journey launched" and "path crossed": the actor's network (R2) (§11) | R-088, R-089, R-158 | No. One internal predicate, one policy |
| §20 VV, XX, AAA | A guard refusal is retried once inside the press's own transaction, so the retry is judged and stamped at the press instant, and the stored `captured_at` is that instant (AAA retires VV's line on the stored time); `capture()` takes no time argument (§6) | R-160, R-031 | No |
| §20 WW | Under `b4 = per_year_with_app`, per-year rings are drawn only on the viewer's own profile, from the one `joined_at` `user_rows()` gives them (§3) | R-161, R-141 | No |
| §20 YY | `profile_picture` stays in the table, unused: no writer sets it and `user_rows()` does not return it (§11) | R-161 | No |
| §20 BBB | The Positivity Feed reader, `positivity_feed_rows()` → (`reflection_id`, `photo_id`, `text`), ends `ORDER BY r.written_at DESC, r.id`: newest reflection first by its written time, ties by the random id. It returns no time-typed column, and no capture, note or journey time (§11) | R-103, R-155, R-162 | No. One definer reader (OQ-28 named it "another definer reader of the same kind") |
| §20 CCC | `ring_count(profile_id uuid) → integer`, SECURITY DEFINER, EXECUTE for `mj_app` only: the number of that user's finished reveals, the same for every viewer, and nothing else. It moves only when a reveal is finished, exactly when the network reads "journey launched" (§11, §3 `b4`) | R-161, R-162, R-158 | No table or field. One scalar definer reader |
| §20 DDD | A second guard refusal in one press: `ROLLBACK TO SAVEPOINT press`, `COMMIT`, no photo, nothing shown. The two refusals are the bug log: two `ERROR` lines with one virtual transaction id in the Postgres server log, which carries no image, no id and no statement text, and which no product role can read (§6) | R-160, R-031 | No table or field. Role settings and the log line prefix, in the cluster script |
| §20 EEE | Journey dates are never returned as fields to a public reader. Narrowing them from capture and reflection dates the reader already reads is allowed, so `reflection_rows()` keeps `written_at` and `year_index` for every reader of the photo (§11; settles OQ-30) | R-152 | No. No change |
| §20 FFF | The guard-bug log stays id-free. The user-settable `log_parameter_max_length_on_error` is an accepted residual alongside OQ-12, to be fixed before real users (§6; settles OQ-31) | R-167 | No. No change |
| §20 GGG, JJJ | A lost press (§20 DDD) uses no frame or highlight place. The screen after it looks exactly like the screen after a normal press, note offer included. JJJ retires GGG's "no note offer". A note written for a lost press is discarded: the route calls no note step, and nothing is stored or logged (§6; settles OQ-32 (a), rules r7 G-24). Under FS §20 QQQ (below) only a press judged accepted can be lost | R-160, R-168 | No. How the note step names its photo: FS §20 LLL (below) |
| §20 HHH, III | The note step retries as `capture()` does: one transaction, strip, savepoint, one retry. Both calls are judged and stamped at the note press's frozen `app_now()`, so a note pressed at capture + 14:59 whose retry ends after 15:00 is accepted. If both strips fail: roll back, commit, nothing stored, two id-free log lines. That ends the note step, as a page taken does, and nothing offers it again (§6; settles OQ-32 (b), gate r6 NB-27) | R-160 (4), R-031, R-020 | No. III is held by the route only: FS §20 MMM (below) |
| §20 KKK | A public reader may see the order of the journeys on a path. No reader returns a journey date to them as a field. Their photos are ordered by `(captured_on, id)` (§4 item 6), so EEE covers it (settles Screen-Inventory OQ-44) | R-152 | No. No change |
| §20 LLL | An accepted `capture()` sets the transaction-local setting `mj.note_handle` to the new photo's id; its result stays `accepted` or `refused`. The route reads the setting before `COMMIT` and keeps the handle in its own memory, keyed by device session and acting user; the device never receives it. The note step, `add_note(handle uuid, img bytea)`, finds its photo by it. One note transaction per handle (§6; settles OQ-33) | R-160, R-168, R-020 | No table or field. One session setting, set inside `capture()`; route memory. A stored token was not needed (§6) |
| §20 MMM | III is held by the route only: the handle is dropped when its first note transaction ends, saved or lost, and the database stores nothing about a lost note. An accepted residual alongside OQ-12, revisited before real users (§6, §8 OQ-12; settles OQ-34) | R-020, R-160 (4) | No. No change |
| §20 NNN | A lost press's handle carries the press instant and no photo. The note step it leads to closes at press + 15 minutes (exactly 15:00 out, `PROVISIONAL: B16`), judged by `app_now()` in the note transaction, as for a real photo, whose press instant is its `captured_at` (FS §20 AAA) (§6) | R-046, R-160, R-168 | No |
| §20 OOO | `join_user(name text) → uuid` (SECURITY DEFINER, EXECUTE for `mj_app` only) inserts the user with `joined_at = app_now()`. It takes no time argument, and a `BEFORE INSERT` trigger refuses any `joined_at` other than `app_now()`. The loader jumps to each P1 §3.2 instant and joins there, jumping only when that instant is still ahead (rules r8 N1) (§2.2; settles OQ-5) | R-120, R-161 | No table or field. One function, one trigger |
| §20 PPP | The route's note handles live in its process memory, so a route restart drops every entry. Nothing wrong is stored and no note can attach to the wrong photo; the next note press finds no entry and is answered `closed`, as after an ended window (RRR). An accepted residual for the local prototype, next to OQ-12, solved before real users (`FS:350`; §6, §8 OQ-12, "Before real users"; settles OQ-35) | R-169, R-171 | No. No change |
| §20 QQQ | A press is judged first, at the press instant: `capture()` runs steps 1–5 (owner and seal, lock, open highlight, normal frame, refuse), and only a press judged accepted reaches the image guard, still before encryption and the insert. A press a normal press would refuse is answered `refused` whatever its image, stores nothing and leaves no entry. A lost press is therefore always one judged accepted, and looks accepted, note offer included (JJJ). The judgment is the normal press's own code, so it reads nothing a normal press does not read (`FS:352`; §6; settles rules r8 G-25 and OQ-32 (a)'s "or from what that press would have given") | R-160, R-170, R-138 | No table or field. One step moved inside `capture()` |
| §20 RRR | Every note press the route answers `closed` gets one answer, the one an ended window gets: after a restart (PPP), after a skip or leaving capture (since 2026-10-31 also FS §20 WWW, below), after a refused press, with a handle already used, and with the window over (since 2026-10-31 also the journey's unlock, FS §20 YYY, below). Nothing else is sent: no reason, no time, no message (`FS:353`; §6) | R-169, R-170, R-171 | No |
| §20 SSS | Judging a press first leaves three gaps, all accepted for the prototype: a strip fault on a press judged refused is not logged, trusted code can learn whether a press would be accepted without using a frame, and the server log holds refusal lines only for presses judged accepted (`FS:355`; §6 "Judged first"; settles OQ-36; "Before real users" item 7) | R-138, R-160 | No. No change |
| §20 TTT | The note step's own database time (about 5 ms at the median), which only a saved note spends, is accepted for the prototype (`FS:356`; §6 "Timing"; settles OQ-37; "Before real users" item 8) | R-170 | No. No change |
| §20 UUU | When the note window ends while S-12 is open, nothing on screen changes on its own. The route already meets it: it sends nothing unasked, and the next note press is answered `closed` (`FS:357`; §6 "The note press") | R-160, R-171 | No. No change (screen: S-12, ux) |
| §20 VVV | A saved page shows no confirmation. The route's `saved` answer carries no reason, time or message, so a lost press's note, answered the same way (JJJ), and a note lost twice (ZZZ, below) look identical (`FS:358`; §6) | R-160, R-170 | No. No change (screen: S-12, ux) |
| §20 WWW | Skipping the note step ends it for good. The device sends one **skip request** when the user skips or leaves capture (`PROVISIONAL: C4` for leaving capture); the route drops the entry for that device session and acting user, does no database work, and always answers the one `closed`, so no later note press for that press is taken, inside the 15 minutes or after (`FS:359`; §6 "The skip request"; rules r9 N2, R-173) | R-173, R-169, R-170, R-020 | No table or field. One route request |
| §20 XXX | C7 is decided in full: no profile picture anywhere. Already carried: `profile_picture` stays unused and `user_rows()` does not return it (YY, §11; P1:62) (`FS:360`) | R-086, R-126, R-161 | No. No change |
| §20 YYY | The note window ends at unlock. `add_note()` refuses once `app_now() >= unlocks_at`, and the `note` trigger refuses the same as its second guard. The route's window read is open only while `app_now() < press_instant + 15 minutes` **and** `app_now() < unlocks_at` (read through `journey_rows()`, the owner's own dates, P1:84), so after unlock no note step is called and the note press gets the one `closed` answer, for a photo and a lost press alike. A press at or after `unlocks_at` is judged refused by step 1 and leaves no entry (`FS:361`; §6 "Unlock"; rules r9 N1, G-26) | R-171, R-170, R-046 | No table or field. One condition in `add_note()` and in the `note` trigger; one bound in the route's window read |
| §20 ZZZ | A note lost twice (HHH, III) is answered `saved`, byte for byte as a saved note, a note saved by the retry and a lost press's discarded note (`FS:362`; §6 "A note lost twice"; gate r8 NB-31) | R-170, R-160 | No |
| §20 AAAA | The extra strip after a guard refusal is accepted for the prototype: at the median a lost press answers 16.7 ms and a press saved by the retry 21.1 ms later than a saved press, and a note lost twice 10.8 ms and a note saved by the retry 14.4 ms later than a saved note. No padded wait is built and the retry stays (`FS:363`; §6 "The press's own timing"; settles OQ-38; "Before real users" item 9) | R-170 | No. No change |
| §20 BBBB | (a) A client that never sends the skip request can still have a note taken inside the 15 minutes: accepted with OQ-12 until real users ("Before real users" item 10). (b) If `add_note()` refuses after the route read the window as open, the device gets the one `closed` answer, byte for byte as RRR's; the test stand-in's "scaffolding only" wording is retired (`FS:364`; §6 "The note press", "The skip request"; settles OQ-39) | R-171, R-173 | No. No change |

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
2. Each scripted action (P1 §3.8) that has not been applied yet and is dated at or before `t1` is applied, in date order. For each one, the clock first jumps to the action's instant, if that instant is still ahead. The action then runs **through the same functions the app uses, as the acting fixture user**, so its rows carry the scripted times. **How, under FS §20 EE and II:** the whole jump is one transaction on the panel's `mj_panel` connection. For each action: only if `action_at > app_now()`, `clock_jump(action_at - app_now())` as `mj_panel` (two actions at one instant make one jump; rules r8 N1, as §2.2 step 2); `SET LOCAL ROLE mj_app`; set the acting user to the action's fixture user (`set_config(…, true)`, transaction-local); call the app functions; `RESET ROLE`. The action therefore has exactly a viewer's rights and no more, and `app_now()` is exactly `action_at` inside it. The script itself lives in the panel's fixture source, not in a table. Whether an action has been applied is read from the data (for example, Wind #6's `journey_reveal` row exists). No table records it.
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
2. The loader, connected as `mj_panel` (**FS §20 II, `FS:313`, approved 2026-10-30**; first a lead-tech proposal derived from FS §20 EE and O2's "no role bypasses the rules"), walks every fixture event in time order. For each, in one transaction: **only if the event's instant is still ahead** (`event_at > app_now()`, read in that transaction), `clock_jump(event_at - app_now())` as `mj_panel`; if `event_at = app_now()` no jump is made, and `clock_jump`'s refusal of `d <= 0` (§1.3) is never loosened; if `event_at < app_now()` the loader stops with an error and applies nothing in that transaction, since on the stopped clock with events in time order that can only be a fault in the fixture (rules r8 N1; tested below). Five events of the load land on the instant the clock already reads: Lantern's join at the starting instant (step 1) and each of the four commits that follow their user's join at the same instant (P1:213). Then `SET LOCAL ROLE mj_app`, set the acting user, and call the function the app would call, as that user, then `RESET ROLE`. This is the same path as a scripted action on a panel jump (§1.5):
   - join (each user before their first action, P1 §3.2, P1:213). Each of the four users with a journey joins at the instant of their first commit, and the join comes before the commit: Steady Lantern 2021-01-01, Second Wind 2021-03-15, Long Way Round 2022-09-01, Open Hands 2023-06-01, all 00:00:00 UTC. First Light joins at 2026-10-01 00:00:00 UTC and commits nothing (P1:211). **How the join sets `joined_at` (FS §20 OOO, `FS:348`; settles OQ-5):** the join is `join_user(name text) → uuid`, SECURITY DEFINER, EXECUTE for `mj_app` only. It inserts the `user` row with a random id, the name (set once, D19) and `joined_at = app_now()`, and returns the new id, which the loader then sets as the acting user. It takes no time argument, so no caller can pass a date. As a second guard, a `BEFORE INSERT` trigger on `user` refuses any `joined_at` other than `app_now()`, as the note table's trigger does for `written_at` (§6). `mj_app` holds no privilege on `user` (§11), and the statement-level append-only trigger refuses UPDATE, DELETE and TRUNCATE (P1:45). So the loader never passes a join date: it jumps the clock to the join instant (the clock is stopped during the load, §2.2 step 3, so the instant is exact) and calls `join_user()` there. Lantern's join is the first event of the load, at the clock's starting instant 2021-01-01 00:00:00 UTC (step 1), before her #1 commit at the same instant. `commit()` refuses an acting user who has not joined, so a loader that commits before it joins fails (tested below). This leaves P1:215 unchanged: the person-tag writer still compares a tag's time with the tagged user's `joined_at`
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

**Evidence under FS §20 OOO** (throwaway `mj_scratch_r9`, local Postgres 16.15, 2026-10-31; database and roles dropped, cluster stopped). Roles as §2.1. A real `mj_panel` login (host connection) jumps the stopped clock and acts through `SET LOCAL ROLE mj_app`, one transaction per event, as §2.2 step 2. `user` carries the `BEFORE INSERT` trigger above and the statement-level append-only trigger.

```
join_user(name text) -> uuid ; arguments of a time type 0
replay, clock stopped, app_now at start 2021-01-01 00:00:00+00:
  Steady Lantern | joined_at 2021-01-01 00:00:00+00 | first commit 2021-01-01 00:00:00+00 | equal t
  Second Wind    | joined_at 2021-03-15 00:00:00+00 | first commit 2021-03-15 00:00:00+00 | equal t
  Long Way Round | joined_at 2022-09-01 00:00:00+00 | first commit 2022-09-01 00:00:00+00 | equal t
  Open Hands     | joined_at 2023-06-01 00:00:00+00 | first commit 2023-06-01 00:00:00+00 | equal t
  First Light    | joined_at 2026-10-01 00:00:00+00 | first commit none
as mj_app: join_user('Back Dated', '2020-01-01'::timestamptz)        -> ERROR: function mj.join_user(unknown, timestamp with time zone) does not exist
           join_user(name => 'Back Dated', joined_at => '2020-01-01') -> ERROR: function ... (name => unknown, joined_at => ...) does not exist
           INSERT INTO user (name, joined_at) ... '2020-01-01'        -> ERROR: permission denied for table user
           UPDATE user SET joined_at = '2020-01-01'                   -> ERROR: permission denied for table user
as the table owner: INSERT ... joined_at '2020-01-01'                 -> ERROR: joined_at is app_now() at join
                    UPDATE user SET joined_at ...                     -> ERROR: user is append-only
planted: join_user_planted(name text, at timestamptz), granted to mj_app
  signature scan (a join function with a time-typed argument)         -> found, caught
  join_user_planted('Back Dated', '2020-01-01')                       -> ERROR: joined_at is app_now() at join (the trigger holds too)
commit before join: commit_journey() as a user id that never joined   -> ERROR: commit: no such user
```

**Evidence for rules r8 N1** (throwaway `mj_scratch_r10`, local Postgres 16.15, 2026-10-31; database and roles dropped, `log_line_prefix` reset, cluster stopped). Roles, clock, `join_user()` and its trigger as above. The loader stand-in is a separate process; each event is one transaction on a real `mj_panel` login (host connection), acting through `SET LOCAL ROLE mj_app`. The nine events are the five joins and four first commits at the P1 §3.2 instants, join before commit.

```
clock_jump(interval '0') / clock_jump(interval '-1 second') as mj_panel  -> ERROR: clock_jump: forward only (both; the guard is unchanged)
step 2 as written before (clock_jump(event_at - app_now()) for every event), clock stopped at 2021-01-01 00:00:00+00:
  event 1, join Steady Lantern at 2021-01-01 00:00:00+00 -> ERROR: clock_jump: forward only ; rows (users/journeys) 0/0 -> 0/0
step 2 with "only if ahead" (event_at > app_now() read in the event's transaction):
  9 events applied ; app_now at the end 2026-10-01 00:00:00+00
  (from the event list, not printed by the run: 4 jumps, 5 events at the instant the clock already read)
  Steady Lantern | joined_at 2021-01-01 00:00:00 | first commit 2021-01-01 00:00:00 | equal true
  Second Wind    | joined_at 2021-03-15 00:00:00 | first commit 2021-03-15 00:00:00 | equal true
  Long Way Round | joined_at 2022-09-01 00:00:00 | first commit 2022-09-01 00:00:00 | equal true
  Open Hands     | joined_at 2023-06-01 00:00:00 | first commit 2023-06-01 00:00:00 | equal true
  First Light    | joined_at 2026-10-01 00:00:00 | first commit none
an event behind the clock (a join at 2026-09-30 00:00:00+00 after the load) -> loader stops (out of order) ; rows 5/4 -> 5/4
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
| `b4` | `per_finished_reveal` / `per_year_with_app` | App (the circle is derived; `PROVISIONAL: B4`). **Under `per_year_with_app`, the per-year rings are computed only for the viewer's own profile**, from the viewer's own `joined_at`, the only one `user_rows()` returns (FS §20 TT, §11). Every other profile is drawn with one ring per finished reveal under both settings (FS §20 WW, `FS:330`). That count comes from `ring_count(profile_id)` for every viewer, public included (FS §20 CCC, `FS:336`; §11), so the app has one path for every other profile; for a network viewer it equals the owner's rows in `journey_reveal_rows()` (tested, §11). It carries no date, so a ring drawn for another profile carries no year or date label from the data. Under `per_finished_reveal` the own profile uses the same count. Before 2026-10-31 (CCC) this cell read "for a public viewer no reader gives it (OQ-29)" |
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
  - the term is evaluated only inside the SECURITY DEFINER predicates `photo_readable()` (§4 item 5) and `overview_readable()` (§5, FS §20 HH). `mj_app` holds no EXECUTE on any helper they call and no grant on `journey_reveal` for this purpose, so no direct call tells a stranger whether a journey's reveal is finished (tested, §5). The owner and, after unlock, the owner's network read the reveal state through `journey_reveal_rows()` (FS §20 SS, §11); its predicate is internal too
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
   - Because `highlight_rules` opens the table to any `mj_owner` definer function called from an app or panel session, only these may name `highlight`. **The check is Rubric R-156** (until 2026-10-31 this line proposed a scan of function bodies only, which missed views, policies, rules and dynamic SQL, and as a substring scan would have caught `photo_highlight_id`; rules r6 N5). Run as the superuser in the test, it lists every object whose definition names the relation `highlight` as a whole identifier: a token match, so `highlight_id`, `photo_highlight_id`, `highlight_open`, `start_highlight` and the trigger name do not match, while `mj.highlight` and a quoted `"highlight"` do. Its sources: `pg_get_functiondef()` for every function in the product schemas (trigger functions included); `pg_get_viewdef()` for every view and materialised view; `qual` and `with_check` of every policy on any table other than `highlight`; `pg_get_ruledef()` for every rule other than a view's `_RETURN`; and every `pg_proc` row in `pg_depend` on `'highlight'::regclass`, for SQL-standard bodies. The set must equal {`capture`, `start_highlight`, `highlight_open`, `highlight_rows`}. A name scan cannot see a table named at run time, so the check also fails on any function owned by `mj_owner` whose body builds SQL at run time (PL/pgSQL `EXECUTE`, `format(`, `query_to_xml`, `dblink`) unless the rules-guardian has reviewed it onto a closed list (today empty). Tested, with planted failures (evidence below).
   - **Highlight rows are insert-only (rules r6 N6, 2026-10-31).** No definer function needs to UPDATE or DELETE one. `start_highlight()` fixes `ends_at` at insert (`started_at` + 24 hours, cut off at `unlocks_at`, P1:133), and `capture()` and `highlight_open()` only read. So `highlight` joins the immutability list (P1:45, §2.5 check 1). A trigger refuses UPDATE, DELETE and TRUNCATE for every product path: the table owner's connections and every definer function. It is a **statement-level** trigger, because under FORCE a connection that matches no policy updates 0 rows and a row-level trigger would never fire (tested). Without it, `highlight_rules` (`FOR ALL`) would let a future definer function lengthen an open highlight (tested as a counterfactual).
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

**Evidence for item 1's R-156 scan and the insert-only highlight (rules r6 N5, N6), throwaway database `mj_scratch_r6` on the local Postgres 16.15, 2026-10-31; database and roles dropped, cluster stopped.** Roles as §2.1; `highlight` ENABLE + FORCE with the two policies of item 1; `capture`, `start_highlight`, `highlight_open`, `highlight_rows` and `photo_highlight_id` as specified; one planted definer function `extend_highlight_planted()` that runs `UPDATE highlight SET ends_at = ends_at + 1 day`.

```
R-156 scan, schema as built      -> capture(uuid,bytea), extend_highlight_planted(uuid), highlight_open(uuid),
                                    highlight_rows(), start_highlight(uuid)      (photo_highlight_id not listed: token match;
                                    extend_highlight_planted is the planted N6 function, so the check fails, as it must)
planted in one rolled-back txn: view over highlight; policy on photo with EXISTS (... FROM mj.highlight ...);
  plpgsql EXECUTE format('... %I', 'high'||'light'); BEGIN ATOMIC body; quoted mj."highlight"; rule on another table
                                 -> every one listed: view, policy, dynamic SQL, function (x2), function (pg_depend), rule
statement trigger refuse_change() on highlight (BEFORE UPDATE OR DELETE OR TRUNCATE, FOR EACH STATEMENT):
  panel txn, SET LOCAL ROLE mj_app, viewer L: start_highlight(L6) -> accepted ; extend_highlight_planted(L6)
                                 -> ERROR: UPDATE on highlight refused: insert-only ; highlight_open(L6) -> t
  as mj_owner (matches no policy): UPDATE / DELETE / TRUNCATE ... CASCADE
                                 -> ERROR: UPDATE / DELETE / TRUNCATE on highlight refused: insert-only
counterfactual, trigger dropped (rolled back): extend_highlight_planted(L6) runs ; ends_at - started_at -> 2 days
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

**Judged first (FS §20 QQQ, `FS:352`, 2026-10-31; settles rules r8 G-25).** Steps 1–5 decide the press before anything reads the image. Steps 3 and 4 choose the place (the open highlight, a normal frame) and only then insert. Between the choice and the insert, `capture()` runs the image guard (below), so the guard reads the image only of a press judged accepted. A press judged refused at step 1 or 5 returns `refused` whatever its image: the guard does not run, nothing is encrypted, stored or logged, and no handle is set. The decision is the normal press's own code in the same call, at the same frozen `app_now()`. So the judgment reads nothing a normal press does not read, and it gives the device nothing a normal press does not give (tested below, `mj_scratch_r10`). Until 2026-10-31 the guard was the first step, before step 1.

**Image metadata (FS §20 KK, `FS:315`; settles OQ-19).** The capture path strips time and location metadata (EXIF, XMP, GPS, PNG text chunks) from the photo before `capture()` encrypts it, and from the note's image before the note step stores it, so the stored file keeps none, for the owner too. The prototype's fixture placeholders are generated with none (P1:256). Real-device capture is Phase 4 or later.

**Stored format (FS §20 QQ, `FS:321`; settles OQ-23).** The strip step re-encodes every photo, and every note image, to a baseline JPEG: it decodes the image, keeps the pixels only, and writes a new file with an APP0 JFIF header, SOF0 at 8-bit precision, one scan, nothing after EOI, and no other segment (no EXIF, XMP, ICC, IPTC or comment, and never progressive). Re-encoding rather than cutting segments out means no unknown segment can survive. The fixture placeholders are generated as baseline JPEG too (P1:256).

**The database's second guard (FS §20 NN, `FS:318`, user ruling 2026-10-30).** Stripping (KK) runs before the database. As a second guard, the database itself refuses an image that still carries time or location metadata:

- **Where.** One function, `image_metadata_free(bytea) → boolean` (IMMUTABLE, no table access), called in `capture()` **once steps 1–4 above have judged the press accepted** (FS §20 QQQ; until 2026-10-31 it was called as the first step, before step 1, the journey lock and any count). It still runs **before encryption** and before the insert, on the plaintext bytes. It is also called as the first step of the note step (unchanged), before the note's image is sealed under the journey key (P1:105). It cannot run later: after encryption the bytes are ciphertext, so no trigger on `photo` or `note` could read them. It therefore holds only if those two functions are the only writers, which §10 makes so: `mj_app` holds no INSERT on `photo` or `note` (FS §20 MM). A refusal raises an error (`check_violation`), so nothing is stored and no frame or highlight place is used.
- **What it accepts: an allow-list, not a deny-list, baseline JPEG only (FS §20 QQ).** It walks the whole container and returns true only for a **baseline JPEG**: SOI; then only DQT, SOF0 with 8-bit sample precision, DHT, DRI and an APP0 segment that begins `JFIF\0`; one SOS; entropy-coded data containing no marker other than RST0–7; and EOI as the last two bytes. Everything else is refused: APP1 (EXIF, which holds the date and GPS IFDs, and XMP), APP13 (IPTC), APP2 (ICC, whose header holds a date), any other APPn, COM, SOF1 (extended sequential) and SOF0 at 12-bit precision (neither is baseline), progressive JPEG (SOF2), bytes after EOI, and every other format (HEIC, WebP, …). **PNG acceptance is removed** (it was case (b) until 2026-10-30): the capture path never stores PNG under QQ, so the guard no longer accepts it, clean or not, for photos and notes alike. None of the allowed parts can hold a time or a place.
- **A refusal never reaches the user (FS §20 PP, `FS:320`; settles OQ-22).** The strip step runs before saving, so a refusal means the strip step is broken: it is a bug, not a state the product has. The capture screen therefore has no refusal message, and nothing invites a second press: one press is one photo, never a retake (CLAUDE.md banned list). The database side is unchanged: `capture()` and the note step raise `check_violation`, store nothing and use no frame or highlight place, so a bug can never be "fixed" by the user pressing again. If the bug occurs anyway, the app strips that press's image again and saves it once, with no action from the user (FS §20 VV, `FS:326`). The retry is judged and stamped at the original press instant, so the press gives the photo it would have given (FS §20 XX, `FS:331`), and the stored time is the press instant (FS §20 AAA, `FS:334`). If the second strip fails too, that press gives no photo, nothing is shown and the bug is logged (FS §20 DDD, `FS:337`). Under FS §20 QQQ this can happen only to a press judged accepted (above). The next two bullets give the mechanism. The build makes the bug unreachable for every sample: the check below requires the strip step's output for every sample to pass.
- **The retry runs inside the press's own transaction (FS §20 VV, XX, AAA; settles OQ-26, rules r6 V4, gate r5 NB-25; AAA settles Screen-Inventory OQ-48).** The capture route opens one database transaction when the press request reaches the server. It opens it before the strip step, so the strip step runs on the server, inside that transaction. Every step for that press then runs in it:
  1. strip, then `SAVEPOINT press`, then `capture(journey, image)`
  2. only if `capture()` raised the guard's `check_violation`: `ROLLBACK TO SAVEPOINT press`, strip the same bytes again, and call `capture()` once more. This is one retry, never a loop
  3. `COMMIT`
  - `app_now()` is frozen for the transaction (§1.2), so both calls are judged at the same instant: the seal, the open highlight and the frames left, in the §20 U order. Both are also stamped at that instant. If the highlight closes, the month turns or the journey unlocks while the retry runs, the press still lands where it would have landed. `captured_at` is the press instant (FS §20 XX). **FS §20 AAA (`FS:334`) settles the wording: the press instant wins, and VV's line on the stored time is retired** (Screen-Inventory OQ-48). The note window therefore runs from the press instant too (P1:108). The one-transaction design is unchanged. The rolled-back first call stored nothing and used no frame or highlight place. Nothing is shown and nothing is asked (PP).
  - **The client cannot back-date a capture.** `capture()` takes no time argument; its arguments are the journey and the image. The instant is `app_now()`, read from `sim_clock`, which `mj_app` cannot write (§1.1) and no session setting overrides (tested). The device sends only the image and never holds the transaction, so it cannot choose the instant: the press instant is when the press reached the server. A server-issued press token stamped by `app_now()` was considered and not used. Carrying an instant across two transactions needs either a stored token, which is a new table, or a signing key, which is a new secret. One transaction needs neither.
  - **Residual.** Code that holds an `mj_app` connection could keep a transaction open and capture later at the earlier instant. That code can already act as any user (OQ-12), and the same point, real authentication before any deploy, closes both. The Phase 4 route test checks that the transaction opens after the request body is read and before the strip step, that no other code path calls `capture(`, and that there is no retry loop.
- **If the second strip also fails (FS §20 DDD, `FS:337`; settles OQ-27; Screen-Inventory OQ-47 for the screen).** The press gives no photo, the user sees nothing different, and the bug is logged. No error, no "try again". In the same press transaction, after step 2:
  4. only if the second `capture()` also raised the guard's `check_violation`: `ROLLBACK TO SAVEPOINT press`, then `COMMIT`. Both calls are rolled back, so nothing is stored and no frame or highlight place is used. There is no third call and no loop, and the user is not asked to press again (PP). R-160 (3) holds: no row, no prompt
  - **Only a press judged accepted gets here (FS §20 QQQ).** Both calls judge the press first (steps 1–5). A press judged refused returns `refused` from the first call, never reaches steps 2 or 4, and the route answers `refused`, exactly as for a normal press at that instant. Its image is never read, so a strip fault on it is neither detected nor logged (OQ-36 (a)). If a retry is judged refused although the first call was judged accepted, which is possible only if another transaction changed the journey's counts in between, it returns `refused` and the route answers `refused`, the answer a normal press gives in that state
  - **What is logged, and where: the Postgres server log, nothing in the database.** Each guard refusal is one server-log line, `ERROR:  image carries metadata`, written by the server when `capture()` raises. Its CONTEXT names only the function (`PL/pgSQL function capture(uuid,bytea) line N at RAISE`). The message is fixed text: `capture()`'s RAISE takes no format argument, DETAIL or HINT, so the line holds no user, journey, photo or `app_now()`. The line prefix holds the real time, the process id, the **virtual transaction id (`%v`)**, and the login role and database. A press lost under DDD shows as two refusal lines with the same virtual transaction id. A press saved by the retry (step 2) shows as one. No row is written anywhere: there is no log table, so no object is added
  - **It carries no image and no statement text.** The route sends the image as a bind parameter, never inline (the Phase 4 route test checks this). The cluster script, run by the superuser like §10 (b), sets these on `mj_app` and `mj_panel` (`ALTER ROLE … SET`): `log_min_error_statement = panic`, `log_statement = none`, `log_min_duration_statement = -1`, `log_min_duration_sample = -1` and `log_parameter_max_length = 0`. All five are superuser-only settings, so neither role can lift them (tested: `SET log_min_error_statement` is refused for both). It also sets `log_parameter_max_length_on_error = 0`, which is user-settable. That is a residual, accepted alongside OQ-12 and to be fixed before real users (FS §20 FFF, `FS:339`; was OQ-31). It adds `%v` to `log_line_prefix` (`ALTER SYSTEM`). Role settings are cluster-wide, so a template clone (§2.3) keeps them. `auto_explain` stays unloaded (§10 (d))
  - **No product role can read it.** The log is a file outside the database, owned by the server's operating-system user (here `/var/log/postgresql/…`, mode 0640). Under the logging collector it is the `log_file_mode` default, 0600. Neither `mj_app` nor `mj_panel` is a member of `pg_read_server_files` or `pg_monitor`. So `pg_read_file()`, `pg_read_binary_file()`, `pg_stat_file()`, `pg_ls_logdir()`, `pg_current_logfile()`, server-side `lo_import()` and `COPY … FROM` a file are all refused, natively and after `SET ROLE mj_app` (tested). The route receives only the `ERROR` of its own call, which it never shows (PP). The note step's refusals land in the same log in the same form, since logging is the server's and not `capture()`'s. Their CONTEXT line names the note step's function instead (tested, `mj_scratch_r8` below). The note step retries as `capture()` does (FS §20 HHH, `FS:341`; below)
  - **What the screen then shows (FS §20 GGG, `FS:340`, and JJJ, `FS:343`, 2026-10-31; settles OQ-32 a and rules r7 G-24).** No frame or highlight place is used, since step 4 rolled both calls back (GGG). The screen looks exactly as after a normal press, **note offer included** (JJJ, under which DDD's "the user sees nothing different" wins). **GGG's "with no note offer" is retired by JJJ** and is not built. **FS §20 QQQ (`FS:352`) settles which normal press:** the press it would have been. The earlier line here, "whether the lost press would have been accepted is never computed", is **retired by QQQ**. Every press is judged at the press instant before the guard reads its image (steps 1–5 above), so a press a normal press would refuse is never lost: it is answered `refused`, and S-02 shows the normal refusal (`PROVISIONAL: B7`). A lost press is always one judged accepted, so it answers `accepted` and S-12 is offered as after a saved press. The judgment stores nothing: no row, no handle, no log line, and no frame or highlight place.
  - **A note written for a lost press is discarded (FS §20 JJJ).** The lost press stored no photo, so the note has nothing to attach to. The route calls no note step for it. It strips the page as for any note press, so that the route does the same work (rules r8 N3, "The note press" below), and then drops the bytes from memory. Nothing is stored or sealed, no row is written, and no log line is added beyond the two refusals of the lost press. (Until 2026-10-31 this line read "nothing is stripped".) The user sees exactly what a saved note shows, and nothing invites a second press (PP). The note is never attached to another photo. An earlier photo of the same journey still inside its 15 minutes, with no note, gets none (tested below). The route names the note's photo through the handle below (FS §20 LLL), and a lost press's handle names none.
- **The note step retries the same way (FS §20 HHH, `FS:341`, 2026-10-31; settles OQ-32 b).** The note route opens one database transaction when the note press reaches the server, after the request body is read and before the strip step. In it:
  1. strip, then `SAVEPOINT press`, then the note step for the photo
  2. only if the note step raised the guard's `check_violation`: `ROLLBACK TO SAVEPOINT press`, strip the same bytes again, and call the note step once more. This is one retry, never a loop
  3. only if the second call also raised it: `ROLLBACK TO SAVEPOINT press`. There is no third call
  4. `COMMIT`
  - **One instant.** `app_now()` is frozen for the transaction (§1.2), so both calls are judged and stamped at the note press instant. The stored `written_at` is that instant, and the 15-minute window (FS §20 K, `FS:281`; D8, P1:108; exactly 15:00 is out, `PROVISIONAL: B16`) is judged once, by the note step and again by the table's trigger, at that instant. **A note pressed at capture + 14:59 whose retry finishes after 15:00 in real time is accepted**, and is stored at capture + 14:59 (tested below). The note step takes no time argument; its arguments name the photo and carry the image.
  - **Two refusals (HHH).** Nothing is stored and nothing is shown. The two refusals are two `ERROR:  image carries metadata` lines with one virtual transaction id, as for a lost photo press, with a CONTEXT line that names the note step's function and no id.
  - **The step then ends (FS §20 III, `FS:342`; gate r6 NB-27).** A note lost twice ends the note step, exactly as a page taken does (S-12). No route offers it again for that photo, so there is no re-shoot (`PROVISIONAL: C4`; R-020). The photo stays without a note, which is the same as a skipped note. **What the device receives (FS §20 ZZZ, `FS:362`; gate r8 NB-31):** the note press is answered `saved`, byte for byte as a saved note, so nothing differs (VVV); see "A note lost twice" below. **The database cannot enforce III.** A lost note leaves no trace, by HHH and PP, so a later note-step call for the same photo inside its 15 minutes would be accepted (tested below). III is held by the route, and the Phase 4 route test checks it: no photo gets a second note transaction after its first one has ended, whether saved or lost. The two calls inside one note transaction are steps 1 and 2 above, not a second note press. **FS §20 MMM (`FS:346`; settles OQ-34): III is enforced by the server route only, and the database stores nothing about a lost note.** The route holds it by dropping the note handle when its first note transaction ends (below). The database side is an accepted residual, alongside OQ-12 and FFF: code that holds an `mj_app` connection and a photo's handle can call the note step again inside the 15 minutes, and that code can already act as any user. Revisit before real users, with OQ-12.
- **The note handle (FS §20 LLL, `FS:345`, and NNN, `FS:347`, 2026-10-31; settles OQ-33).** The note step finds its photo through a server-side handle that the device never holds. No table or field is added, and `capture()`'s result stays `accepted` or `refused` (P1:49).
  - **What the handle is.** It is the new photo's `id`, a random version-4 uuid (FS §20 JJ). `capture()` first clears the transaction-local setting `mj.note_handle` (`set_config(…, true)`, the same mechanism as the acting-user setting, §2.1), then sets it to the new id right after the insert, and returns `accepted`. The route reads it with `current_setting('mj.note_handle', true)` in the press transaction, before `COMMIT`. Because the setting is transaction-local, it is gone at `COMMIT`. Because it is set inside the savepoint, a call rolled back by `ROLLBACK TO SAVEPOINT press` takes it back too. So a press saved by the retry (step 2) gives the handle of the one stored photo, and a lost press (step 4) gives an empty setting. The function's `SET search_path` clause does not reset it, since that clause covers only its own variable (tested). A refused press (no frame left, step 5) also leaves it empty, and under FS §20 QQQ that holds whatever its image.
  - **Why the photo id and not a separate token.** The handle has to live from the press transaction to the note transaction, up to 15 minutes later. A token that is not the photo id would need a stored map from token to photo, which is a new table and a model change, or a signing key, which is a new secret. This is the same reason the press instant is not carried in a token (above). The photo id needs neither. It is unguessable (122 random bits), and it opens nothing on its own: before unlock no reader returns a row for it, also to the owner (P1:48 (a)), and the note step accepts it only from the photo's owner (§2.1), inside the 15 minutes (D8, P1:108), before the journey's unlock (FS §20 YYY, `FS:361`, 2026-10-31; P1:108 carries it since then; "Unlock" below), and only while the photo has no note (P1:104). Until 2026-10-31 this sentence said "while the journey is sealed" and cited P1:104 and :108, neither of which said it (rules r9 N1, G-26); YYY now rules it. The device never receives it, so to the device it is not a photo id at all.
  - **Where the route keeps it.** In the route's own process memory, never in the database and never on the device: one entry per **device session and acting user** (C16, OQ-12), holding the handle (or none), what kind of entry it is (a photo, or a lost press), the press instant, read as `app_now()` in the press transaction, and the id of the journey the press was into, which the route already passed to `capture()` (since 2026-10-31, for the unlock bound of FS §20 YYY; the device does not receive it from the route). For a saved press that instant is the photo's `captured_at` (FS §20 AAA). The device receives exactly what it received before LLL: the press's `accepted` or `refused`, and the note press's outcome. **A lost press answers `accepted`, as a saved one does** (FS §20 JJJ), and its entry is of kind "lost press" with no handle. Under FS §20 QQQ a press is lost only when it was judged accepted. **A press answered `refused`, by a normal refusal or because a lost press's judgment was refused, leaves no entry** (it replaces any earlier one with none), since S-12 never follows a refusal. A new press on the same session and user replaces the entry. S-12 is reached only straight after a press and has ended before the camera returns (`Screen-Inventory.md` S-12; `PROVISIONAL: C4`), so the entry it replaces belongs to a note step that has already ended. **When the user skips or leaves capture, the device tells the route with the skip request, and the route drops the entry** ("The skip request" below). Skipping ends the note step for good, and no note can be added later in the 15 minutes (FS §20 WWW, `FS:359`, decided 2026-10-31; no longer a strictest reading of C4). Leaving capture ends it under `PROVISIONAL: C4`, which WWW does not change. Until 2026-10-31 this sentence read "When the route learns that the user skipped or left capture, it drops the entry (C4)", and no line said how the route learns (rules r9 N2, R-173). Reset (§2.3) clears every entry, since the presses they name no longer exist in the clone. **A route restart clears every entry too (FS §20 PPP, `FS:350`).** The memory is the route process's own, so a restart inside a note window drops that press's entry. Nothing wrong is stored and no note can attach to the wrong photo. The next note press finds no entry and is answered `closed`, as after an ended window (RRR, below), so that note step ends before its 15 minutes. This is an accepted residual for the local prototype (one route process), next to OQ-12, solved before real users (§8, "Before real users"). Keeping entries across a restart would need a stored map (a new table) or a session store outside the database, and neither is built.
  - **What the route writes (rules r8 N4; R-169 (2)).** The capture and note routes write no access-log or request-log line. Nothing the route writes to stdout, stderr, a log file, an error trace or a crash report holds a handle or any photo id, a press instant (the `app_now()` read at the press, in any format or precision, epoch included), the real time a press reached it, or the acting user's id. The route never logs its memory or an entry. The only text it may write for these routes is the driver's error for its own call: the guard's `ERROR:  image carries metadata` and its `CONTEXT` line. Those hold none of the above (§6, DDD), and the route writes them as received, without the parameters or the entry. A framework's default request logging is turned off for these two routes. The build check below scans everything the route writes.
  - **The note press.** The note route looks up the entry for the device session and acting user and drops it at once, so a handle serves one note transaction. **Every note press then runs one shape (rules r8 N3)**: the route reads the request body, strips the page, opens the note transaction, sets the role and the acting user, reads the window, takes `SAVEPOINT press` and commits. Only an entry that holds a photo, inside the window, calls the note step between the savepoint and the commit. **With no entry** (after a restart, PPP; after a skip, FS §20 WWW, or leaving capture, `PROVISIONAL: C4`, both dropped by the skip request; after a refused press, a press at or after unlock included; with a handle already used) the window check has no press instant and reads closed, so no note step is called and the answer is `closed`. **That is the one answer for every closed case (FS §20 RRR, `FS:353`):** after a restart, with no entry of any other kind, and with the window over, the device receives the same `closed` response, byte for byte, as when the window has ended. It carries no reason, no time and no message, and nothing in it invites another photo (S-12 is ux's; R-171). With an entry, in the note transaction (steps 1–4 above), the route first reads `coalesce(app_now() < press_instant + interval '15 minutes' AND app_now() < (SELECT unlocks_at FROM journey_rows() WHERE id = journey), false)`. Until 2026-10-31 it read only the first bound; the second is FS §20 YYY ("Unlock" below). With no entry both arguments are NULL and the same statement reads closed, so every note press runs the same read. That is the note window: exactly 15:00 is out (`PROVISIONAL: B16`), it is judged at the note press's frozen instant like everything else in that transaction (so HHH's 14:59 edge holds here too), and it reads `app_now()`, never the system clock (§2.5 check 10). If the window is open and the entry holds a photo, the route runs steps 1–4 with `add_note(handle, image)`, and the note step and the `note` trigger judge the window and the seal again. It answers `saved` when the note step accepts, at the first call or after the retry, and `saved` when both strips fail (FS §20 ZZZ, "A note lost twice" below). **If `add_note()` returns `refused` here, the device gets the one `closed` answer**, byte for byte as RRR's (FS §20 BBBB, `FS:364`, 2026-10-31; settles OQ-39 (b)). Through the route this happens only when other code holding an `mj_app` connection and the handle has already added the note (MMM, OQ-12). Until 2026-10-31 this sentence read "If `add_note()` returns `refused` here, see OQ-39 (b)", and the test's route stand-in sent `closed` there "as scaffolding only"; that answer is now the design. Tested (`mj_scratch_r12`, below): the window read open, `add_note()` refused, the answer byte-identical to every other `closed`, and a planted route that answers otherwise is caught. If the window is open and the entry is a lost press, it calls no note step and stores nothing. It has stripped the page as for any note and drops the bytes, and it answers exactly as for a saved note (FS §20 JJJ). If the window is closed, whether by press + 15 minutes or by the journey's unlock, it calls no note step and answers `closed`, for a photo and a lost press alike (FS §20 NNN: "exactly as after a real photo"; RRR; YYY). **The entry has been dropped whatever happened**, so a handle serves one note transaction. That is how the route holds III (MMM).
  - **Timing (rules r8 N3; R-170 (3)), what remains.** A lost press's note and a saved note now share every step the route takes: the body read, the strip step (the largest share, 11.9 ms median in the test for a 1240×1754 page of 261 KB), the transaction, the role and acting user, the window read, the savepoint and the commit. What remains is the note step's own database work, which only a saved note does: the guard's walk, encryption under the journey key, the insert, the `note` trigger, and the WAL flush at commit. On the local Postgres 16 that came to 5.3 ms at the median (5.86 ms against 0.58 ms, n = 200 each; p95 8.76 ms against 0.87 ms). Of that, `add_note()` took 4.5 ms, including the stand-in's hex decode, and the commit 0.85 ms against 0.05 ms. Before this round the gap was the whole of it, about 18 ms here (11.9 + 5.86, summed, not measured as one), since a lost press's note did no strip and opened no transaction. Closing the remaining gap would need the note step's encryption and a write without a row, or a padded wait. No ruling gives either, so neither is built. The residual is recorded as OQ-37. A closed answer has the same shape with no note step, so every `closed` answer is in one timing class.
  - **The skip request (FS §20 WWW, `FS:359`, 2026-10-31; rules r9 N2, R-173).** "Skipping the note step ends it for good; no note can be added later in the 15 minutes." The screen alone cannot hold that, since a note press sent after a skip would find the entry still alive (CLAUDE.md, "Enforce rules in code"). So S-12 sends one request when the user skips, and the same request when it leaves capture without a page taken (`PROVISIONAL: C4`). The request carries nothing: no handle, no id, no time, no body. The route keys it like a note press, by device session and acting user. It drops that entry, if there is one, and answers the one `closed` response, byte for byte as RRR's. It opens no transaction and runs no database statement, in every case: an entry for a photo, an entry for a lost press, no entry, after a restart, after the window has ended. **No new leak:** the device sends the route nothing it does not already have. The answer is a constant, and the work is the same in every case (2.7–3.1 µs at the median in the test, below). The route writes no log line for it (rules r8 N4 applies unchanged). A skip on another session, or as another user, leaves this entry alone. The device does not need the answer, because S-12 has already ended on screen (UUU, VVV; the screen row is ux's, R-173 (2)). Since the answer is constant and the work is the same, waiting for it would show nothing either. A new press on the same session and user replaces the entry anyway, as before. **What it does not cover:** a client that never sends the skip and then sends a note press inside the 15 minutes. The product's S-12 never sends a note press after a skip, so only code outside the product's client reaches this. That is OQ-39 (a), accepted with OQ-12 until real users (FS §20 BBBB, `FS:364`, 2026-10-31; "Before real users" item 10). Until 2026-10-31 this read "That is OQ-39 (a), not picked."
  - **Unlock (FS §20 YYY, `FS:361`, 2026-10-31; rules r9 N1, G-26).** "The note window ends at unlock. Nothing is added to a journey once it unlocks; the note step ends then, and looks exactly like the window ending (UUU, RRR)." This is enforced in three places:
    - `add_note()` refuses once `app_now() >= unlocks_at` of the photo's journey, inside the 15 minutes too.
    - The `note` trigger refuses the same as its second guard (`note after unlock`), so a writer that drops the check is still refused (tested with a planted `add_note()` without it).
    - The route's window read takes both bounds (above), for an entry of either kind. A note press after unlock therefore calls no note step and gets the one `closed` answer, byte-identical to a window that has ended (RRR).

    The edge is half-open, as the seal is (`committed_at <= app_now() < unlocks_at`, P1:99). At exactly `unlocks_at` the journey is unlocked and the window has ended. The route reads `unlocks_at` through `journey_rows()`, which already gives the owner the type and dates of their own journey in the sealed year (P1:84), so the read tells the route nothing new. Nothing of it reaches the device. **A lost press at that instant (R-170):**
    - A lost press captured before unlock whose note press comes after unlock is answered `closed`, exactly as the photo's. Without the bound it would have been answered `saved` while the photo's was not (G-26 (b)). That difference is caught as planted fault (e).
    - A press at or after `unlocks_at` is refused at step 1 before the guard reads its image (FS §20 QQQ). A lost press there is answered `refused`, byte for byte as a normal press, and the guard does not run. It leaves no entry, and its next note press is `closed`.

    The prototype reaches this case when the demoer jumps to the next unlock while S-12 is open (R-153). Nothing on screen changes on its own (UUU), and the next note press is not taken.
  - **A note lost twice (FS §20 ZZZ, `FS:362`, 2026-10-31; gate r8 NB-31).** It is answered `saved`. The whole response, meaning status line, headers and body, is byte-identical to the one sent for a saved note, a note saved by the retry, and a lost press's discarded note (JJJ). That gives one `saved` response and one `closed` response, and a note press gets nothing else. The step then ends (III), and the next note press for it is `closed`.
  - **The press's own timing (rules r9 N3; R-170 (4)), measured and accepted (FS §20 AAAA, `FS:363`, 2026-10-31).** The device's next screen after a press depends on its answer: `accepted` leads to the note offer (S-12), `refused` to the normal refusal (S-02). So S-02 waits for the answer, and the time the answer takes depends on how the server handled the press:
    - A saved press strips once, then encrypts and inserts.
    - A press saved by the retry strips twice, then encrypts and inserts.
    - A lost press strips twice and stores nothing.

    Measured through the route stand-in for a 2016×1512 photo of 384 KB, n = 100 each, alternating (evidence below; strip step 28.7 ms at the median):

    | Press | Median | p95 |
    |---|---|---|
    | Saved | 34.9 ms | 44.9 ms |
    | Saved by the retry | 56.0 ms | 66.4 ms |
    | Lost | 51.6 ms | 65.8 ms |

    So a lost press answers 16.7 ms later than a saved press at the median, and a press saved by the retry answers 21.1 ms later. The notes, for a 1240×1754 page of 276 KB, alternating and n = 100 each (strip step 12.4 ms at the median):

    | Note press | Median | p95 |
    |---|---|---|
    | Saved | 27.7 ms | 35.5 ms |
    | Saved by the retry | 42.1 ms | 55.6 ms |
    | Lost twice | 38.5 ms | 46.0 ms |
    | Lost press's note, discarded | 21.3 ms | 28.9 ms |

    The discarded note's 6.4 ms gap to a saved note is TTT's accepted gap. **The extra strip after a guard refusal is not covered by TTT:** it makes a note lost twice 10.8 ms slower than a saved note, and a note saved by the retry 14.4 ms slower. The extra strip is the larger cost, and it occurs only when the strip step has a bug, which the build check makes unreachable for every sample (PP). Closing it would need a padded wait (a timer in the route, as for OQ-37) or one strip per press with no retry, which VV and HHH rule out. Neither is built. The residual is OQ-38, accepted for the prototype by FS §20 AAAA ("Before real users" item 9); until 2026-10-31 this read "The residual is OQ-38, not picked." The S-02 review in R-170 (4) stays: no transition into S-12 shows the wait in a way that would tell the user.
  - **The loader** (§2.2) uses the same handle in the same way: it reads `mj.note_handle` inside each capture transaction, keeps it in its own process memory, and passes it to the note step in the note's own transaction, inside the 15 minutes (P1:310). It never reads a photo id from a table.
  - **The note step's arguments** are `(handle uuid, img bytea)`: the handle and the image, and no time (HHH). Its value is stored as `note.photo_id` (P1:104).
- **What the build runs** (proposed check, for the rules-guardian to number; fails the build): a fixed set of sample images generated by the test with a fixed seed is passed to `image_metadata_free()` and through `capture()` as the owner of a sealed journey with a frame left (under FS §20 QQQ a press judged refused never reaches the guard), and through the note step as the owner of a photo captured less than 15 minutes earlier (D8; until 2026-10-31 this read "an unlocked photo", which the 15-minute rule refuses). Clean baseline JPEG → `true`, `accepted`. JPEG with EXIF date, EXIF GPS only, XMP date, IPTC date, ICC, COM text, bytes after EOI, progressive scan, SOF1, 12-bit SOF0; PNG clean or with `tIME`, `tEXt`, `iTXt`, `eXIf`; WebP → `false`, and both functions raise and store no row (counts unchanged). **PP:** every decodable sample, after the QQ strip step → `true`, `accepted` by both; any `false` fails the build. Every fixture placeholder → `true` (P1:256). **VV, XX:** with the clock running, in one panel transaction acting as the owner of a sealed journey whose highlight closes one second after the press: `capture()` with a refused image raises, `ROLLBACK TO SAVEPOINT`, wait past the highlight's end, `capture()` with the stripped image → `accepted`; exactly one new photo, `captured_at` equal to the `app_now()` read at the press, inside the highlight. `capture()` has no argument of a time type. **DDD:** in one press transaction the strip step is forced to fail twice, with the image carrying a fixed marker byte sequence and sent as a bind parameter. The check requires: both calls raise; no new photo (counts unchanged); exactly two `image carries metadata` lines with one virtual transaction id in the server log, and one such line for a press saved by the retry; no `STATEMENT` line; the marker, in hex or as text, nowhere in the log; no uuid in the refusal lines. The log-reading functions above must be refused for `mj_app` and `mj_panel`, natively and after `SET ROLE mj_app`, and `SET log_min_error_statement` must be refused for both. **HHH, the note step (R-160 (4)):** with the clock running, each note press is one panel transaction acting as the photo's owner, with the refused image sent as a bind parameter. (i) The retry is saved: refused, `ROLLBACK TO SAVEPOINT`, then the stripped image → `accepted`. Exactly one note, with `written_at` equal to the `app_now()` read at the note press. (ii) **The edge:** the clock is jumped to capture + 14:59 and the note pressed. The first call is refused, the route waits past capture + 15:00 in real time, and the retry → `accepted`. `app_now()` still equals the press instant, the next transaction's `app_now()` is past capture + 15:00, and `written_at` is capture + 14:59.x. The counterfactual must hold too: the same retry in a new transaction after 15:00 is refused and stores nothing. (iii) Two refusals in one note press: both raise, no note row, and every table's row count is unchanged. The log holds two refusal lines with one virtual transaction id, their CONTEXT names the note step's function, and there is no `STATEMENT` line, no marker and no uuid. The note step has no argument of a time type. **JJJ:** an accepted photo P with no note, then a lost press (two `capture()` refusals), then the note press for the lost press. Every table's row count is unchanged after the lost press and after its note, and P still has no note. The planted fault must be caught: a route that names the note's photo as the owner's latest photo without a note inside 15 minutes attaches the discarded note to P. **III** is a Phase 4 route test (above). The database side is an accepted residual (FS §20 MMM): a later note-step call after a lost note is accepted. **LLL, the handle:** `capture()` returns `text` and has no argument of a time type; after an accepted press `mj.note_handle` equals the id of the one new photo, and it is unset in the next transaction on the same connection; after `ROLLBACK TO SAVEPOINT` it is empty; after a lost press it is empty, also when the same connection's previous transaction saved a photo. `mj_app` is refused on `photo`. Against a route stand-in that holds the handle per device session and acting user: a note press 10 minutes after a press saved by the retry stores one note on that photo at the note press instant; a second note press for the same handle calls no note step; a note press from another session, or as another user on the same session, calls none; the note step called with the owner's handle as another user → `refused`. Every response the device receives is scanned for a uuid: none. **NNN**, on the stopped clock so the instants are exact: photo, note at press + 14:59 → saved; photo, note at press + 15:00.000 → closed, no note step called, and the note step called directly at that instant → `refused`; lost press, note at + 14:59 → the same answer as the photo's, no note step called, every row count unchanged; lost press, note at + 15:00.000 → the same answer as the photo's. With the clock running: jump to press + 14:59.5, wait 0.8 s in real time, note press → closed, for a photo and a lost press alike. **JJJ** again through the handle: photo P with no note, a lost press 1 minute later, its note press 1 minute after that → saved to the device, every row count unchanged, P has no note. **III through the handle:** a note press whose two strips fail, then a later note press for the same photo inside 15 minutes → no note step called, no note. **Planted faults, each must be caught:** (a) the route puts the handle in the press response (the uuid scan finds it); (b) the route keeps the entry after a lost note (the second note is stored); (c) the route skips the window check for a lost press (at + 15:00.000 its answer differs from the photo's); (d) a `capture()` that sets the handle at session level (a lost press on the same connection reads the previous photo's handle, so its note would attach there). **QQQ, both branches** (stopped clock; the strip step forced to fail twice; the oracle is a normal press with a clean image at the same instant in a rolled-back transaction). Six states: a frame left; no frame left; a highlight open and not full with no frame left; a highlight full with no frame left; the journey unlocked; a press into another user's journey. In each state the lost press's device answer equals the oracle's. When the oracle says `refused`, the device gets `refused`, byte-identical to a normal refused press, with zero refusal lines in the server log and no entry, and the next note press is answered `closed`. When the oracle says `accepted`, the device gets `accepted` with two refusal lines under one virtual transaction id, an entry of kind "lost press", and a note press 1 minute later answered `saved`. Every row count is unchanged in every case. **Reads:** the per-table read counters of the transaction (`pg_stat_xact_user_tables`: sequential and index scans, and tuples read) are identical for a lost press and a normal press in every state judged refused. In every state judged accepted, the lost press's reads are the normal press's minus those of the insert (the journey key and the foreign-key checks). Planted fault: a `capture()` with the guard first, the order before QQQ, answers `accepted` where the oracle says `refused` (caught). **RRR:** on the stopped clock, a photo whose note press comes 5 minutes after a route restart; a photo whose note press comes at press + 15:00.000; a photo skipped (since 2026-10-31, through the skip request, WWW) and then note-pressed; a lost press whose note press comes after a restart. Each calls no note step and gets one `closed` response, byte-identical across all four. The controls (photo + 1 minute, lost press + 1 minute) get `saved`. **N3:** every note press runs the one route shape above, and a lost press's note strips its page. Timing is a Phase 4 review (R-170 (3)), with the residual of OQ-37. **N4 (R-169 (2)):** everything the route writes (stdout, stderr, log, driver error text) is scanned for every handle it held, every press instant in four text forms and as epoch seconds, and every acting user's id: no hit, and no uuid at all. The planted fault must be caught: a route that logs its entry (handle and press instant). **WWW (R-173), on the stopped clock:** a photo, then the skip request, then a note press at press + 1 minute sent straight to the route → `closed`, no note step called, no note row. The same for a lost press, after leaving capture (the same request), after a page taken, and after a page lost twice. The skip answer is byte-identical to RRR's `closed` for a photo entry, a lost-press entry, no entry, after a restart, and on another session, and it runs no database statement in any case. A skip sent on another session leaves this session's entry, and its note press is `saved`. Planted fault (g): a route that ignores the skip stores the note (caught). **YYY (G-26)**, journey unlocking at U, on the stopped clock: a photo and a lost press at U − 5:00; note presses at U − 1:00 → `saved` (controls), at U + 0:00.000 and at U + 1:00 → `closed` for both, byte-identical, no note step called, no note row. At U + 1:00, `add_note()` called straight as the owner → `refused`. A planted `add_note()` without the seal check → the `note` trigger raises `note after unlock`, and so does a direct INSERT as the superuser. A normal press and a lost press at U + 0:00.000 → `refused`, byte-identical; the guard does not run, no entry is left, and the next note press is `closed`. With the clock running: a photo and a lost press at U − 1 s, a 1.5 s real wait, then note presses → `closed` for both, no note. Planted fault (e): a route whose window read lacks the unlock bound answers a lost press's note `saved` and the photo's `closed` (caught; the database still stores no note). **ZZZ (NB-31):** the full responses (status line, headers, body) for a saved note, a note saved by the retry, a note lost twice and a lost press's note are byte-identical. Planted fault (h): a route that answers a note lost twice `closed` (caught). **One `closed`:** every `closed` the run sends (RRR's restart, + 15:00.000 and no-entry cases, every skip, and every YYY case) is one byte string. **N3 (R-170 (4)):** the press and note-press timings of saved, retried and lost cases are measured and recorded as OQ-38. It is a review, not a pass or fail.
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

- **Evidence under FS §20 VV and XX** (throwaway `mj_scratch_r6`, local Postgres 16.15, 2026-10-31; database and roles dropped, cluster stopped). The guard stand-in accepts `\x00` and refuses `\xff`; `capture()` runs the §20 U order; the clock runs at real speed (§1.2). A highlight on Lantern #6 ends one second after the press.

```
mj_panel login; BEGIN; SET LOCAL ROLE mj_app; viewer Lantern; press_instant := app_now()
  SAVEPOINT press; capture(L6, '\xff')            -> ERROR: image carries metadata   (the bug)
  ROLLBACK TO SAVEPOINT press; pg_sleep(1.5)       (the highlight has now closed in real time)
  capture(L6, '\x00')                              -> accepted ; app_now() = press_instant -> t ; COMMIT
new photos from the press: 1 ; captured_at = press_instant: t ; in the highlight: t ; highlight closed by now: t
  (press 2026-10-25 00:00:00.001046+00, highlight end 00:00:01.000411+00)
counterfactual, retry in a new transaction after the highlight closed -> accepted, stamped later: t, normal frame: t
capture() arguments                                -> jid uuid, img bytea
as mj_app: UPDATE sim_clock                        -> ERROR: permission denied for table sim_clock
           SET mj.sim_at = '2020-01-01'; app_now() -> unchanged
```

- **Evidence under FS §20 AAA and DDD** (throwaway `mj_scratch_r7`, local Postgres 16.15, 2026-10-31; database and roles dropped, `log_line_prefix` reset, cluster stopped). Roles as §2.1, with the role settings above; `%v` added to `log_line_prefix`. The guard stand-in accepts `\x00` and refuses anything else. The refused image is `\xff` followed by the marker `MJMARKER-7Q` (hex `4d4a4d41524b4552…`). Each press is one transaction on a real `mj_panel` login (host connection), acting through `SET LOCAL ROLE mj_app` as Lantern, owner of a sealed journey. The image is sent with psql `\bind`, so it travels as a bind parameter.

```
role settings seen by the session      -> log_min_error_statement panic ; log_parameter_max_length_on_error 0
AAA, clock running: press_instant := app_now(); SAVEPOINT press; capture(L7, refused) -> ERROR: image carries metadata
  ROLLBACK TO SAVEPOINT press; pg_sleep(1.2); capture(L7, '\x00') -> accepted ; app_now() = press_instant -> t ; COMMIT
  next transaction: app_now() > press_instant + 1 s -> t ; stored captured_at -> 2027-11-02 12:00:00.048857+00 = press_instant
DDD case 1, two refusals in one press: SAVEPOINT press; capture -> ERROR ; ROLLBACK TO SAVEPOINT press; capture -> ERROR ;
  ROLLBACK TO SAVEPOINT press; COMMIT
DDD case 2, contrast: capture -> ERROR ; ROLLBACK TO SAVEPOINT press; capture('\x00') -> accepted ; COMMIT
photos in the database: before both cases 11 ; after 12 (the one new photo is case 2's; case 1 stored none)
server log, every line from the two cases (verbatim):
  2026-10-31 02:37:02.836 UTC [768] 3/101 mj_panel@mj_scratch_r7 ERROR:  image carries metadata
  2026-10-31 02:37:02.836 UTC [768] 3/101 mj_panel@mj_scratch_r7 CONTEXT:  PL/pgSQL function capture(uuid,bytea) line 4 at RAISE
  2026-10-31 02:37:02.836 UTC [768] 3/101 mj_panel@mj_scratch_r7 ERROR:  image carries metadata
  2026-10-31 02:37:02.836 UTC [768] 3/101 mj_panel@mj_scratch_r7 CONTEXT:  PL/pgSQL function capture(uuid,bytea) line 4 at RAISE
  2026-10-31 02:37:02.837 UTC [768] 3/102 mj_panel@mj_scratch_r7 ERROR:  image carries metadata
  2026-10-31 02:37:02.837 UTC [768] 3/102 mj_panel@mj_scratch_r7 CONTEXT:  PL/pgSQL function capture(uuid,bytea) line 4 at RAISE
refusal lines per virtual transaction id -> 3/101: 2 (case 1, press lost) ; 3/102: 1 (case 2, press saved)
STATEMENT lines 0 ; marker (hex or text) in the log 0 ; uuids in the refusal lines 0
as mj_panel, and after SET ROLE mj_app: pg_read_file, pg_read_binary_file, pg_stat_file, pg_ls_logdir, pg_current_logfile, lo_import
  -> ERROR: permission denied for function ... ; COPY t.poll FROM '<log file>' -> ERROR: permission denied to COPY from a file
  member of pg_read_server_files / pg_monitor -> mj_panel f f ; mj_app f f
  SET log_min_error_statement = 'error' -> ERROR: permission denied to set parameter (mj_panel and mj_app logins)
counterfactual 1, mj_panel's log_min_error_statement reset to the default and the image sent inline:
  ... 3/130 mj_panel@mj_scratch_r7 STATEMENT:  SELECT mj.capture('42647d88-…'::uuid,  E'\\xff4d4a4d41524b45522d3751'::bytea);
  (the journey id and the image are in the log: why the role setting is needed)
counterfactual 2 (residual, OQ-31), the session itself runs SET log_parameter_max_length_on_error = -1, image as a bind parameter:
  ... 3/122 mj_panel@mj_scratch_r7 CONTEXT: ... unnamed portal with parameters: $1 = '42647d88-…', $2 = '\xff4d4a4d41524b45522d3751'
```

- **Evidence under FS §20 HHH, III and JJJ** (throwaway `mj_scratch_r8`, local Postgres 16.15, 2026-10-31; database and roles dropped, `log_line_prefix` reset, cluster stopped). Roles as §2.1, with the DDD role settings above and `%v` in `log_line_prefix`. `app_now()` and `clock_jump()` are as §1.2 and §1.3, and the clock is running. The guard stand-in accepts an image whose first byte is `0x00` and refuses anything else. The refused image is `\xff` followed by the marker `MJMARKER-8Q`. `capture()` and the note step (stand-in name `add_note(pid uuid, img bytea)`) run the guard first, then the owner and window checks. The `note` table carries the insert-only trigger and the 15-minute trigger (`written_at = app_now()` and `app_now() < captured_at + 15 min`). Each press is one transaction on a real `mj_panel` login (host connection), acting through `SET LOCAL ROLE mj_app` as Lantern, who owns a journey that is sealed at 2027-11-02. Images are sent with psql `\bind`. **The test names each note's photo by reading it as the superuser, since how the route names it was then OQ-33** (settled by FS §20 LLL; the `mj_scratch_r9` run below uses the handle).

```
note step arguments -> pid uuid, img bytea ; prosecdef t ; arguments of a time type 0
HHH (i), 10 min after capture: press := app_now(); SAVEPOINT press; add_note(P1, refused) -> ERROR: image carries metadata
  ROLLBACK TO SAVEPOINT press; add_note(P1, '\x00') -> accepted ; app_now() = press -> true ; COMMIT
  photos 1, notes 0 -> photos 1, notes 1 ; written_at 2027-11-02 12:10:01.167026+00 = press ; = capture + 00:10:00.167522
HHH (ii), the edge: clock_jump(capture + 14:59 - app_now()); next transaction press = capture + 00:14:59.043757
  SAVEPOINT press; add_note(P2, refused) -> ERROR ; ROLLBACK TO SAVEPOINT press; pg_sleep(1.5)
  clock_timestamp() - transaction_timestamp() > 1.5 s -> true ; add_note(P2, '\x00') -> accepted ; app_now() = press -> true ; COMMIT
  next transaction: app_now() >= capture + 15:00 -> true
  stored written_at = capture + 00:14:59.043757 ; inside 15:00 -> true
  counterfactual: P3 at capture + 14:59, refused, ROLLBACK; 1.5 s later, new transaction add_note(P3, '\x00') -> refused ; notes for P3 0
                  the table's own trigger, direct INSERT as the table owner after 15:00 -> ERROR: note outside its 15 minutes
HHH (iii) and III, two refusals in one note press on P4 (capture + 2 min):
  SAVEPOINT press; add_note -> ERROR ; ROLLBACK TO SAVEPOINT press; add_note -> ERROR ; ROLLBACK TO SAVEPOINT press; COMMIT
  row count of each of the 19 tables, before and after -> identical ; notes for P4 0
  III residual, rolled back: a later add_note(P4, '\x00') inside 15 min -> accepted   (the database cannot tell; OQ-34, accepted by FS §20 MMM)
JJJ: P5 accepted, no note; 1 min later a lost press: SAVEPOINT; capture -> ERROR ; ROLLBACK TO; capture -> ERROR ; ROLLBACK TO; COMMIT
  row counts after the lost press -> identical ; the note press for it: no photo from its press, so no note step is called
  row counts after the discarded note -> identical ; notes for P5 0
  planted: route names the note's photo as the latest unnoted photo inside 15 min -> add_note accepted, attached to P5 (caught)
server log, refusal lines from the run (verbatim, the product-role lines):
  2026-10-31 03:08:11.897 UTC [1022] 3/243 mj_panel@mj_scratch_r8 ERROR:  image carries metadata
  2026-10-31 03:08:11.897 UTC [1022] 3/243 mj_panel@mj_scratch_r8 CONTEXT:  PL/pgSQL function add_note(uuid,bytea) line 3 at RAISE
  ... (3/255, 3/267 the same: HHH (ii) and its counterfactual)
  2026-10-31 03:08:15.794 UTC [1092] 3/283 mj_panel@mj_scratch_r8 ERROR:  image carries metadata
  2026-10-31 03:08:15.794 UTC [1092] 3/283 mj_panel@mj_scratch_r8 CONTEXT:  PL/pgSQL function add_note(uuid,bytea) line 3 at RAISE
  2026-10-31 03:08:15.795 UTC [1092] 3/283 mj_panel@mj_scratch_r8 ERROR:  image carries metadata
  2026-10-31 03:08:15.795 UTC [1092] 3/283 mj_panel@mj_scratch_r8 CONTEXT:  PL/pgSQL function add_note(uuid,bytea) line 3 at RAISE
  2026-10-31 03:08:16.143 UTC [1118] 3/299 mj_panel@mj_scratch_r8 ERROR:  image carries metadata    (x2, capture(uuid,bytea): JJJ's lost press)
refusal lines per virtual transaction id -> 3/243 1 ; 3/255 1 ; 3/267 1 (notes saved or rolled back) ; 3/283 2 (note lost) ; 3/299 2 (press lost)
STATEMENT lines from mj_panel or mj_app 0 (the one STATEMENT line is the superuser's direct trigger INSERT) ; marker hex 0 ; marker text 0 ; uuids in refusal lines 0
```

- **Evidence under FS §20 LLL, MMM and NNN** (throwaway `mj_scratch_r9`, local Postgres 16.15, 2026-10-31; database and roles dropped, cluster stopped). Roles as §2.1. `app_now()`, `clock_jump()` and `clock_start()` as §1.2 and §1.3. The guard stand-in accepts an image whose first byte is `0x00` and refuses anything else. `capture(jid uuid, img bytea)` and `add_note(handle uuid, img bytea)` are as above, the `note` table carries the insert-only and 15-minute triggers, and `mj_app` holds no privilege on `photo` or `note`. The route stand-in is a shell process: every press and note press is one transaction on a real `mj_panel` login (host connection) through `SET LOCAL ROLE mj_app`, with the savepoint steps above; its memory is one entry per (device session, acting user); everything it sends the device is written to a file, which the test scans. The test reads photo ids as the superuser only to check results.

```
capture(jid uuid, img bytea) -> text ; add_note(handle uuid, img bytea) -> text ; time-typed arguments 0, 0
press, first strip refused, retry saved -> device: accepted ; handle = id of the one new photo: t ; photos 1 -> 2
next transaction, same login: mj.note_handle -> <unset>
SAVEPOINT a; capture(..) -> accepted, handle set t ; ROLLBACK TO SAVEPOINT a -> handle ''
as mj_app: SELECT id FROM photo -> ERROR: permission denied for table photo
note press at + 10 min -> saved ; notes for P1 1 ; written_at = press + 10 min t
second note press, same handle -> closed (no note step called) ; notes for P1 1
stopped clock, exact:
  photo P2, note at + 14:59        -> saved  ; notes for P2 1
  photo P3, note at + 15:00.000    -> closed ; notes for P3 0 ; add_note(P3) directly at that instant -> refused
  lost press L1 -> device: accepted ; handle the route got '' ; note at + 14:59     -> saved  ; note step called: no
  lost press L2 -> device: accepted ;                           note at + 15:00.000 -> closed ; note step called: no
  row counts before L1 and after L2's note -> identical
JJJ: photo P5, lost press 1 min later, its note 1 min after -> saved ; row counts identical ; notes for P5 0
III: P6, note press with both strips refused -> saved (note step: lost) ; later note press -> closed, no note step ; notes for P6 0
  residual (MMM): add_note(P6) called directly inside 15 min, rolled back -> accepted
keyed: P7 pressed on session A as Lantern; note press on session B as Wind -> closed ; B as Lantern -> closed ; A as Wind -> closed
  add_note(Lantern's handle) as Wind -> refused ; session A as Lantern -> saved ; notes for P7 1
device responses: press accepted (10, saved and lost alike) ; note saved / closed ; uuids in them 0
planted (a) handle sent with the press response          -> uuids in device responses 1 : caught
planted (b) route keeps the entry after a lost note      -> second note step accepted, notes for P10 1 : caught
planted (c) no window check for a lost press, + 15:00.000 -> lost: saved, photo: closed : caught
planted (d) capture() sets the handle at session level   -> lost press on the same connection reads the earlier photo's handle t : caught
        the real capture(), same case                     -> lost press reads ''
clock running: photo P8, jump + 14:58, note at once -> saved ; lost press, same -> saved
               photo P9, jump + 14:59.5, 0.8 s real wait -> closed ; notes for P9 0 ; lost press, same -> closed
system-clock calls outside the clock module: functions 0 ; route stand-in 0
```

- **Evidence under FS §20 PPP, QQQ and RRR, and rules r8 N3 and N4** (throwaway `mj_scratch_r10`, local Postgres 16.15, 2026-10-31; database and roles dropped, `log_line_prefix` reset, cluster stopped). Roles as §2.1, with the DDD role settings and `%v` in `log_line_prefix`. The schema is as in `mj_scratch_r9`, except that `capture(jid uuid, img bytea)` judges steps 1–5 first and runs the guard stand-in (first byte `0x00` is clean) only on a press judged accepted. The planted `capture_guard_first()` keeps the old order. The route stand-in is a separate process. Every press and note press is one transaction on a real `mj_panel` login (host connection) through `SET LOCAL ROLE mj_app`, with the savepoint steps above, and the retry runs only on SQLSTATE 23514. Its memory is one entry per (device session, acting user). What it sends the device and everything it writes go to files, which the test scans. The clock is stopped at 2027-11-02 01:00:00+00. The five users come from the N1 load (§2). Each state's journey is a stand-in Contemplator (1 frame a month, highlight quota 12). R's highlight holds 12 photos. The test reads ids and counts as the superuser only to check results.

```
QQQ, lost press (both strips fail) | normal press, clean image, same instant (rolled back) | device | rows u/j/h/p/n | refusal lines | entry
  S1 frame left                                 accepted | {"press": "accepted"} | 5/9/2/15/0 -> same | 2 (vxid 3/555) | lost
  S2 no frame left                              refused  | {"press": "refused"}  | same               | 0              | none
  S3 highlight open, not full, no frame left    accepted | {"press": "accepted"} | same               | 2 (vxid 3/579) | lost
  S4 highlight full (12), no frame left         refused  | {"press": "refused"}  | same               | 0              | none
  S5 journey unlocked (Lantern's 2021 journey)  refused  | {"press": "refused"}  | same               | 0              | none
  S6 Wind presses into First Light's journey    refused  | {"press": "refused"}  | same               | 0              | none
  normal clean presses through the route in S2, S4, S5, S6 -> {"body": {"press": "refused"}, "status": 200} (byte-identical to the lost press's) ; rows unchanged
  saved press, device -> {"body": {"press": "accepted"}, "status": 200} (byte-identical to S1's and S3's lost press)
reads in the press transaction, pg_stat_xact_user_tables (table:seq_scan,seq_tup_read,idx_scan,idx_tup_fetch):
  S2 clean  highlight:0,0,1,0 journey:0,0,1,1 photo:0,0,2,1 sim_clock:1,1,0,0     S2 lost  identical
  S4 clean  highlight:0,0,1,1 journey:0,0,1,1 photo:0,0,3,13 sim_clock:1,1,0,0    S4 lost  identical
  S5, S6 clean  journey:0,0,1,1 sim_clock:1,1,0,0                                  S5, S6 lost  identical
  S1 clean  highlight:0,0,1,0 journey:0,0,2,2 journey_key:0,0,1,1 photo:0,0,2,0 sim_clock:1,1,0,0
  S1 lost   highlight:0,0,1,0 journey:0,0,1,1                     photo:0,0,2,0 sim_clock:1,1,0,0   (minus the key read and the insert's FK check)
  S3 clean  highlight:0,0,2,2 journey:0,0,2,2 journey_key:0,0,1,1 photo:0,0,1,0 sim_clock:1,1,0,0
  S3 lost   highlight:0,0,1,1 journey:0,0,1,1                     photo:0,0,1,0 sim_clock:1,1,0,0   (the same)
server log, S1 (verbatim):
  2026-10-31 04:43:28.961 UTC [2452] 3/555 mj_panel@mj_scratch_r10 ERROR:  image carries metadata
  2026-10-31 04:43:28.961 UTC [2452] 3/555 mj_panel@mj_scratch_r10 CONTEXT:  PL/pgSQL function capture(uuid,bytea) line 23 at RAISE
  2026-10-31 04:43:28.962 UTC [2452] 3/555 mj_panel@mj_scratch_r10 ERROR:  image carries metadata
  2026-10-31 04:43:28.962 UTC [2452] 3/555 mj_panel@mj_scratch_r10 CONTEXT:  PL/pgSQL function capture(uuid,bytea) line 23 at RAISE
  whole run: STATEMENT lines 0 ; marker (hex or text) 0 ; uuids in refusal lines 0
planted capture_guard_first(), lost press: S2 -> {"press": "accepted"} vs normal refused : caught ; S4 -> the same : caught
note press 1 minute later: S1, S3 -> no note step (discard), {"note": "saved"} ; S2, S4, S5, S6 -> no entry, {"note": "closed"} ; rows unchanged
residual (OQ-36 (b)), capture(journey, '\xff4d4a') straight from mj_app, no route:
  S1 -> ERROR 23514 image carries metadata ; S2 -> refused ; rows 5/11/2/420/402 -> same (later in the run)
RRR, stopped clock from 2027-11-02 02:00:00+00, Lantern, session A:
  a photo, route restart, + 5 min, note press      -> no note step ; {"body": {"note": "closed"}, "status": 200}
  b photo, + 15:00.000, note press                 -> no note step ; {"body": {"note": "closed"}, "status": 200}
  c photo, skipped, note press                     -> no note step ; {"body": {"note": "closed"}, "status": 200}
  e lost press, route restart, + 1 min, note press -> no note step ; {"body": {"note": "closed"}, "status": 200}
  a, b, c, e byte-identical -> True
  d control: photo, + 1 min -> note step accepted, {"note": "saved"} ; f control: lost press, + 1 min -> discard, {"note": "saved"}
  rows 5/9/2/15/0 -> 5/9/2/19/1 (four photos, d's one note) ; notes on that journey 1
N4, everything the route wrote (log, stderr with the driver's error text) scanned for each handle it held, each press instant
  as printed, without the zone, with 'T', its time of day, and as epoch seconds, and each user id:
  route-setup 15 handles, 2 instants -> hits 0, uuids 0 ; route-qqq -> 0, 0 ; route-planted-guard-first -> 0, 0 ; route-rrr 4 handles, 5 instants -> 0, 0
  driver error text the route wrote (route-qqq, all of it): 4 x "ERROR:  image carries metadata", 4 x "CONTEXT:  PL/pgSQL function capture(uuid,bytea) line 23 at RAISE"
  device responses: uuids 0 ; bodies {"press": "accepted"}, {"press": "refused"}, {"note": "saved"}, {"note": "closed"} only
  planted: a route that logs its entry -> hits 4 (handle and press instant), uuids 1 : caught
N3, one mj_panel session, alternating, n = 200 each; page 1240x1754 baseline JPEG 260,874 B:
  strip step (Pillow 12.3.0 decode and baseline re-encode) median 11.9 ms over 20 : now run in both shapes
  saved note  (txn, role, viewer, window, savepoint, add_note, commit)  median 5.857 ms  p95 8.764 ms ; notes stored 200
  lost press  (txn, role, viewer, window, savepoint, commit)            median 0.579 ms  p95 0.874 ms
  of the saved note: add_note statement median 4.544 ms ; COMMIT 0.851 ms (lost press's COMMIT 0.049 ms) ; the rest 0.426 vs 0.522 ms
  first run, a 1,477,692 B noise image (no compression): saved 32.944 ms median, p95 105.155 ms ; lost press 0.730 ms, p95 1.116 ms
```

- **Evidence under FS §20 WWW, YYY and ZZZ, and rules r9 N1–N3** (throwaway `mj_scratch_r11`, local Postgres 16.15, 2026-10-31; built twice, once for the run below and once for the note timing, and each time the database and roles were dropped and the cluster stopped). Roles as in §2.1 (`mj_owner`, `mj_app`, and `mj_panel` with `INHERIT FALSE, SET TRUE`), plus a superuser login used only to check results. EXECUTE is revoked from PUBLIC by default privileges, and `mj_app` holds no table privilege. `app_now()`, `clock_jump()` and `clock_start()` are as in §1.2 and §1.3. The `journey` table's `unlocks_at` is generated in UTC. `capture(jid uuid, img bytea)` judges steps 1, 2, 4 and 5 first, as in `mj_scratch_r10`. The stand-in has no highlight, which this round does not test. Encryption is pgcrypto `pgp_sym_encrypt_bytea` under the journey key. `add_note(handle uuid, img bytea)` runs the guard first, then checks the owner, the window, `app_now() < unlocks_at` (YYY) and that the photo has no note. The `note` trigger refuses a `written_at` other than `app_now()`, a note at or after 15 minutes, and a note at or after unlock. The guard stand-in accepts a JFIF APP0 header followed directly by DQT. The strip step is a real Pillow 13.0.0 decode and baseline re-encode. A forced failure does the same work and then prefixes `\xffMJMARKER-11`. The route stand-in is a separate Python 3.13 process (psycopg 3.3.6). Every press and note press is one transaction on a real `mj_panel` login (host connection) through `SET LOCAL ROLE mj_app`, with the savepoint steps above. Its memory holds one entry per (device session, acting user): kind, handle, press instant and journey. Its device responses are full HTTP byte strings, which the test compares and scans. Scripts were kept outside the repo and deleted after the run.

```
journey A (Lantern) unlocks U = 2027-11-02 00:00:00+00 ; stopped clock
photo 384,459 B with an EXIF date ; guard(raw) -> f ; guard(strip output) -> t ; page 276,409 B
closed = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nCache-Control: no-store\r\nContent-Length: 17\r\n\r\n{"note":"closed"}'
saved  = '... Content-Length: 16\r\n\r\n{"note":"saved"}'
YYY, journey A:
  presses at U-5:00, three photos and three lost presses -> {"press":"accepted"} x6 ; kinds photo, lost
  note at U-1:00 (controls)    photo -> saved ; lost press -> saved (discarded) ; note step called 1
  note at U+0:00.000           photo -> closed ; lost press -> closed ; note step called 0
  press at U+0:00.000          normal -> {"press":"refused"} ; lost -> {"press":"refused"} ; byte-identical True ; guard raised 0 ; entries none
  note at U+1:00               photo -> closed ; lost press -> closed ; note step called 0 ; notes on that photo 0
  add_note(handle) as the owner at U+1:00 -> refused
  planted add_note() without the seal check, U+1:00 -> ERROR: note after unlock (the note trigger) : caught
  direct INSERT as the superuser at U+1:00      -> ERROR: note after unlock
  rows user/journey/photo/note (4, 4, 0, 0) -> (4, 4, 3, 1) : the one note is the U-1:00 photo control
  planted (e) window read without the unlock bound, journey D, note at U_D+1:00:
              photo -> closed (note step called 1, refused) ; lost press -> saved ; identical False : caught ; notes stored 0
  clock running, journey E unlocking 00:55:00: photo and lost press at 00:54:59.145 ; 1.5 s real wait ;
              note presses at 00:55:00.686 -> closed, closed ; identical True ; note step called 0 ; notes 0
WWW, journey B (sealed to 2028-03-15):
  skip answer for: photo entry, lost-press entry, leave capture, no entry, after restart, other session
              -> byte-identical True ; equal to closed True ; database statements 0
  note press at +1:00 after: skip, lost press + skip, leave capture, page taken, page lost twice
              -> closed x5 ; note step called 0 ; rows (4, 4, 10, 2) -> (4, 4, 10, 2)
  skip sent on session S8x ; S8's note press -> saved
  planted (g) route ignores the skip -> note after skip saved, note step called 1 : caught
ZZZ, journey B, note presses at +1:00:
  saved / saved by the retry / lost twice / lost press (discarded) -> one 112-byte string, {"note":"saved"} ; byte-identical True
  planted (h) lost twice answered closed -> saved vs closed, identical False : caught
one closed: 14 closed responses in the run (RRR restart, + 15:00.000, no entry; WWW x5; YYY x6) -> distinct 1
device responses 650 ; uuids in them 0 ; bodies {"note":"closed"}, {"note":"saved"}, {"press":"accepted"}, {"press":"refused"} only
route writes 0 lines ; system-clock calls in the route 0
N3, presses, journey C (stand-in cadence 100), stopped clock, one mj_panel session, alternating, n = 100 each:
  strip step, photo: median 28.7 ms over 30
  saved     median 34.89 ms  p95 44.88 ms
  retried   median 55.97 ms  p95 66.41 ms
  lost      median 51.59 ms  p95 65.75 ms   ; photos stored 200 ; device answers {"press":"accepted"} only
  at the median: lost - saved +16.70 ms ; retried - lost +4.38 ms ; retried - saved +21.07 ms
  skip request: median 3.1 us (photo entry), 2.9 us (lost press), 2.7 us (no entry)
N3, note presses (second build), journey C, at each press's own instant, alternating, n = 100 each after 5 warm-up rounds:
  strip step, page: median 12.4 ms over 30
  saved        median 27.65 ms  p95 35.49 ms
  retried      median 42.08 ms  p95 55.58 ms
  lost twice   median 38.47 ms  p95 46.01 ms
  lost press   median 21.25 ms  p95 28.94 ms   ; answers {"note":"saved"} only ; notes stored 210
```

- **Evidence under FS §20 BBBB (b)** (throwaway `mj_scratch_r12`, local Postgres 16, 2026-10-31; database and roles dropped, cluster stopped, scripts kept outside the repo and deleted). In `mj_scratch_r11` this branch was reached only by planted fault (e) (`photo -> closed (note step called 1, refused)`), and that `closed` was not among the 14 compared. This run reaches it by its one real cause and compares it. Roles `mj_owner`, `mj_app`, and `mj_panel` (NOINHERIT, member of `mj_app` with `INHERIT FALSE, SET TRUE`); EXECUTE revoked from PUBLIC by default privileges; `mj_app` holds no table privilege. A stopped clock read by `app_now()`, moved by `clock_jump()` (EXECUTE for `mj_panel` only). `capture()` checks the owner and the seal, runs the guard stand-in, inserts at `app_now()` and sets `mj.note_handle`. `add_note(handle, img)` runs the guard, then refuses on a wrong owner, the window, `unlocks_at`, or a note already on the photo. The `note` trigger guards the time, the window and unlock. The route stand-in (Python, one `psql` transaction per press on a host `mj_panel` login through `SET LOCAL ROLE mj_app`) keeps one entry per (session, user), runs the window read of "The note press" above, takes `SAVEPOINT press`, and calls `add_note()` only when the read is open and the entry holds a photo. No strip or retry: this run tests the answer, not the image path.

```
press P1 -> accepted
other code add_note(handle P1) at +0:30 -> saved        (mj_app connection holding the handle: MMM, OQ-12)
route note press P1 at +1:00: window read open True ; add_note -> refused ; answer closed True
next note press P1 (entry dropped) -> closed ; window read open False
P2 note at +15:00.000 -> closed ; open False
no entry -> closed
control P3 note at +1:00 -> saved ; add_note saved
closed responses 4 -> distinct 1 ; equal to the one closed True
planted (i) refusal answered {"note":"refused"}: open True ; add_note refused ; identical to closed False : caught
note step called 3 ; photos 4 ; notes 3 ; photos with more than one note 0
```

- **Settled 2026-10-30.** OQ-22 by FS §20 PP (`FS:320`), OQ-23 by FS §20 QQ (`FS:321`). **Settled 2026-10-31:** OQ-26 by FS §20 VV (`FS:326`) and XX (`FS:331`), carried above. **Settled 2026-10-31 (later rulings):** the stored time by FS §20 AAA (`FS:334`; Screen-Inventory OQ-48), and OQ-27 by FS §20 DDD (`FS:337`), both carried above. **Settled 2026-10-31 (rulings on the questions DDD raised):** OQ-31 by FS §20 FFF (`FS:339`), and OQ-32 by GGG (`FS:340`) and HHH (`FS:341`). III (`FS:342`) and JJJ (`FS:343`) then ruled what follows a lost note and a lost press, and JJJ retires GGG's "no note offer". All are carried and tested above. Raised while carrying them: OQ-33 and OQ-34 (§8). **Settled 2026-10-31 (rulings on those):** OQ-33 by FS §20 LLL (`FS:345`) and NNN (`FS:347`), OQ-34 by MMM (`FS:346`), carried and tested above (`mj_scratch_r9`). Raised while carrying them: OQ-35 (§8). **Settled 2026-10-31 (rulings on those and on rules r8):** OQ-35 by FS §20 PPP (`FS:350`), with RRR (`FS:353`) for the answer a note press then gets; rules r8 G-25 by QQQ (`FS:352`). Carried and tested above (`mj_scratch_r10`), with rules r8 N3 and N4. Raised while carrying them: OQ-36 and OQ-37 (§8), settled 2026-10-31 by FS §20 SSS and TTT. **Settled 2026-10-31 (rulings on those, on Screen-Inventory, on rules r9 G-26 and on gate r8 NB-31):** OQ-36 by FS §20 SSS (`FS:355`) and OQ-37 by TTT (`FS:356`), accepted ("Before real users" items 7 and 8). The skip by WWW (`FS:359`), the note window at unlock by YYY (`FS:361`), and the answer to a note lost twice by ZZZ (`FS:362`). All three are carried above, with the skip request, the unlock bound and one `saved` answer, and tested (`mj_scratch_r11`). Rules r9 N3 (the press's own timing) is measured above. Raised while carrying them: OQ-38 and OQ-39 (§8). **Settled 2026-10-31 (rulings on those):** OQ-38 by FS §20 AAAA (`FS:363`) and OQ-39 by BBBB (`FS:364`), accepted ("Before real users" items 9 and 10); BBBB's `closed` answer to a note-step refusal is carried in "The note press" and tested (`mj_scratch_r12`).

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
| 3, 45, 48 (a), 48 (h), 62, 63, 65, 91, 164, 168, 176, 180 | Applied 2026-10-31 (sixth round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–ZZ; highlight rows insert-only; the 0 is read through the readers; the `journey_reveal` and `user` read rules; `profile_picture` unused; per-year rings on the own profile only; the guard-bug retry in the press transaction; "reflection left" under B10 and UU; check 1 gains highlight; check 5 gains the retry | FS §20 SS–ZZ; DN B10 (rules r6 V1–V4, N4, N6; gate r5 B-5, B-6, CF-29) |
| 3, 65, 91, 117, 164, 179, 180 | Applied 2026-10-31 (seventh round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–DDD; other profiles' rings through `ring_count()`; the press instant stored, and the second refusal (no photo, the server log); the Positivity Feed order; `journey_reveal` counted by `ring_count()`; check 4 gains `ring_count()` in the differential test; check 5 gains the double refusal | FS §20 AAA, BBB, CCC, DDD (OQ-27, OQ-28, OQ-29; Screen-Inventory OQ-48) |
| 3, 105, 180 | Applied 2026-10-31 (eighth round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–KKK; the note image gains the retry in the note press's own transaction at its frozen instant, the double refusal, III's end of the step and JJJ's discarded note; check 5 gains the note-step retry, the 14:59 edge, the note's double refusal and the lost press's note | FS §20 HHH, III, JJJ (rules r7 V1, V2, N5; gate r6 CF-33) |
| 3, 49, 63, 105, 108, 176, 180, 213 | Applied 2026-10-31 (ninth round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–OOO; `capture()` hands the route, and only the route, the note handle; `joined_at` is `app_now()` at `join_user()`, with no time argument; III held by the route only, and the lost press's note window closing 15 minutes after the press; the note step finds its photo through the route's handle, one note transaction, no table or field; check 1 gains the join's arguments and trigger; check 5 gains the handle tests and planted faults; the loader joins at each P1 §3.2 instant | FS §20 LLL, MMM, NNN, OOO (OQ-33, OQ-34, OQ-5) |
| 3, 91, 105, 108, 180, 213 | Applied 2026-10-31 (tenth round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–RRR; `capture()` judges the §20 U order before the image guard, which reads only a press judged accepted; a lost press is the press it would have been, refused or accepted with the note offer; one `closed` answer for a restart, a missing entry and an ended window; every note press runs one route shape; the route writes no handle, press time or acting user; check 5 gains QQQ's two branches, RRR, the route-output scan and its planted faults; the loader jumps only to an instant still ahead | FS §20 PPP, QQQ, RRR (OQ-35, rules r8 G-25, V2); rules r8 N1, N3, N4 |
| 3, 105, 108, 180 | Applied 2026-10-31 (eleventh round) by lead-tech, each inside its existing line, so P1 stays at 408 lines: status note to §20 Q–ZZZ, with which rulings bear on which lines; a note lost twice answered as a saved note; the note window ends at unlock, in the note step, its trigger and the route's window read; the device's skip request drops the handle; check 5 gains the skip, the unlock edge with a lost press, the byte-identical `saved` and their planted faults. **Correction, dated 2026-10-31 (rules r9 V3):** the supervisor changed the tenth-round row above from "Q–RRR" to "Q–VVV" (b9c2958) and then to "Q–XXX" (8c7e2e2), and P1:3 the same way. The tenth round applied Q–RRR, so the row is restored to that. SSS–XXX reached P1:3 only as a range, by the supervisor, and this round gives them their line account | FS §20 SSS–ZZZ (OQ-36, OQ-37, rules r9 G-26, gate r8 NB-31); rules r9 V2, V3, N1–N3; gate r8 CF-41, CF-42, CF-44 |
| 3 | Applied 2026-10-31 (twelfth round) by lead-tech, inside its existing line, so P1 stays at 408 lines: status note to §20 Q–BBBB; AAAA and BBBB accept residuals, and BBBB's `closed` answer is a route answer, so neither changes any other P1 line. P1:180 (check 5) does not yet name the BBBB (b) case; it is tested here (§6, `mj_scratch_r12`) | FS §20 AAAA, BBBB (OQ-38, OQ-39) |

§3 is being edited by another agent at the time of writing. The §3 lines go through the supervisor.

---

## 8. Open questions (stopped, not guessed)

| # | Question | Blocks |
|---|---|---|
| OQ-1 | Panel small jump sizes. §20 V allows small jumps but names none. Proposed: +1 minute and +1 hour. Tests use `clock_jump(interval)` directly. **Settled 2026-10-30 as a provisional default: DN B20 (+1 minute, +1 hour).** | Nothing now (was: the panel only, not the schema) |
| OQ-2 | A scripted action whose instant the running clock has already passed is applied late, at the next jump's starting `app_now()`. Accept? **Settled 2026-10-30 as a provisional default: DN B26 (applied at the next jump).** | Nothing now (was: time control) |
| OQ-3 | R-119 expects announcements "with times after the map entry". Both are written at the same instant inside the finish function. Read "after" as "not before"? | R-119 test wording (rules-guardian) |
| OQ-4 | Baseline time of day: 2026-10-25 **00:00:00 UTC**? P1:201 gives only the date. **Settled 2026-10-30 as a provisional default: DN B21 (00:00:00 UTC; P1:201 now carries it).** | Nothing now (was: fixture load, R-117) |
| OQ-5 | **How is `joined_at` set: `app_now()` inside the join, or a value the caller (the loader) gives?** Still not settled by any doc (re-checked 2026-10-31 for gate r6 NB-28). P1:63 gives only the read rule (FS §20 TT). P1:213 gives the fixture's values and calls them "a fixture choice, not product behaviour". R-120 (`RR:1038`) names capture, reflection, overview, highlight and Commit times as app-clock times, and not the join. P1:73 sets `committed_at` from `app_now()`, but no line says the same of the join. Both readings give the same fixture: the replay jumps to each join instant and then joins (§2.2 step 2), so the loader would pass exactly `app_now()`. They differ only in what the join function accepts. Under the first it takes no time argument, as `capture()` and the note step do not. Under the second the caller can back-date a join, and with it the earliest date a tag of that user is allowed (P1:215). Not picked **Settled 2026-10-31, FS §20 OOO (`FS:348`): `app_now()` at join; nobody can back-date it; the loader joins each user at the right simulated time. Carried: §2.2 (`join_user(name text) → uuid`, no time argument, plus a `BEFORE INSERT` trigger on `user`), P1:63, P1:176, P1:213; tested (§2 evidence, `mj_scratch_r9`)** | Nothing now (was: the join function's arguments, Phase 3). Fixture data: none |
| OQ-6 | Does reset put the option switches back to their defaults? The template clone does that. Keeping them means the reset script copies the row across. **Settled 2026-10-30 as a provisional default: DN B22 (reset restores every default).** | Nothing now (was: O3 behaviour) |
| OQ-7 | Options are one global row, not per viewer. Confirm. **Settled 2026-10-30 as a provisional default: DN B23 (one global setting).** | Nothing now (was: O3) |
| OQ-8 | After unlock, who reads highlight rows (proposed: owner only), and may a photo's reader see that it was a highlight photo (`highlight_id`)? Nothing in the docs said. **Settled 2026-10-30: owner only. Highlight rows: DN B24 (provisional). `photo.highlight_id`: FS §20 DD (decided), enforced as in §4 item 4.** | Nothing now (was: O4 policy) |
| OQ-9 | At exactly `ends_at` the highlight is closed (half-open, like P1:47). Confirm (B16 settles only the note's 15:00 edge). **Settled 2026-10-30 as a provisional default: DN B25 (closed at exactly the end time).** | Nothing now (was: capture(), R-040) |
| OQ-10 | Under B2 `after_reveal_finished`, does "no one but the owner reads it" (`FS:291`, `DN:21`) also cover the journey, chapter and feeling-tag rows that §20 T opens to the network at unlock? **Settled 2026-10-30, FS §20 X: no. The network reads them from unlock under both settings; `b2` does not govern them (§3).** | Nothing now (was: RLS on 3 tables under one switch setting) |
| OQ-11 | **Conflict:** DN B9 (d) (`DN:28`, a chapter filter on the Positivity Feed, which public readers use) against FS §20 T (`FS:296`, chapters never public). Related: B9 (c) selects feed entries by feeling tag, so a public reader learns that a journey carries one of the four working tags. **Settled 2026-10-30: FS §20 Y (no chapter filter) and FS §20 CC (the feed may select by feeling tag but never shows the tag to a public reader).** | Nothing now (was: Positivity Feed query, Phase 4) |
| OQ-12 | The prototype's viewer identity is a per-transaction setting, so anyone with the app role can act as any user (C11, C16). Acceptable for the local prototype. Real authentication is needed before any deploy. **Accepted alongside it, to be revisited at the same point:** the user-settable `log_parameter_max_length_on_error` (FS §20 FFF, §6), and III held by the route only, so code holding an `mj_app` connection and a photo's note handle can call the note step again after a lost note (FS §20 MMM, `FS:346`; §6). Also recorded here (FS §20 PPP, `FS:350`): note handles live in route memory and are lost on a server restart; that note step then ends early, the note press is answered `closed` as after an ended window (FS §20 RRR, `FS:353`), and nothing wrong is stored (§6 "Where the route keeps it"). Also accepted here (FS §20 BBBB, `FS:364`, 2026-10-31): a client that never sends the skip request can have a note taken inside the 15 minutes (OQ-39 (a); §6 "The skip request"). Every residual to close at this point is listed in "Before real users", below the table | Deploy (host still open) |
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
| OQ-25 | **Read rules no doc decided, found while carrying FS §20 OO** (§11). OO moves each table's current read rule into a reader unchanged. For three tables the current rule was never decided, only implied. (a) **`user`** (`name`, `profile_picture`, `joined_at`): P1:45 gives it "the same grant" as P1:44 (SELECT) and P1 states no row rule, so today every viewer reads every user row, `joined_at` included. §11 carries exactly that in `user_rows()` (no behaviour change). Confirm, or rule a narrower set. (b) **`journey_reveal`: two lines disagree.** P1:45 gives the app role the same SELECT, with no row rule, so any viewer would read whether any journey's reveal is finished. This file, §3 (B2 term), says the app role holds no grant on `journey_reveal` for that purpose, "so no direct call tells a stranger whether a journey's reveal is finished". The owner certainly reads it (Screen-Inventory S-04 and the finish screen are the owner's, SI:153, :503). Not picked: §11 writes no `journey_reveal` reader until this is ruled, so after OO the app role reads no reveal row at all (state "revealing" or "revealed" is not readable through the app role meanwhile). (c) **`announcement`, the actor's own**: R2 as written shows "journey launched" and "path crossed" to the actor's network, which never contains the actor (tags exclude oneself, P1:156), and "reflection left" to readers of the photo, which includes the actor. So the actor reads their own reflection-left announcements but not their own launched or crossed ones. §11 carries that unchanged; confirm it is intended **Settled 2026-10-31:** (a) FS §20 TT — the `user` reader returns `joined_at` only for the viewer's own row; (b) FS §20 SS — `journey_reveal` gets a definer reader with the §20 T rule (owner and network, after unlock); (c) FS §20 UU — carried as written. **Carried 2026-10-31 (§11):** (a) `user_rows()` returns `joined_at` on the viewer's own row only, NULL on every other, and no `profile_picture` (FS §20 YY); the person-tag writer still reads the tagged user's `joined_at` inside its definer body (P1:215), and returns nothing of it. (b) `journey_reveal_rows()`, with the policy changed to the same rule, and FS §20 ZZ. (c) The actor's own "reflection left" per UU; for every other reader DN B10 narrows "readers of the photo" to the owner's network members who can read it, even when the photo is public (`PROVISIONAL: B10`; rules r6 V3). | Nothing now (was: (b) blocked the Phase 3 `journey_reveal` reader; gate r5 B-5, B-6) |
| OQ-26 | **What happens to the pressed image when the guard refuses it** (FS §20 PP leaves it). PP rules that the user never sees a refusal and that one press is one photo. If the bug occurs anyway, either (a) that press yields no photo, silently, which breaks "one press is one photo"; or (b) the app strips the same bytes again and resubmits them as the same press, which keeps one photo per press but stores a `captured_at` a moment later than the press. Not picked **Settled 2026-10-31, FS §20 VV:** strip again and save once; **and FS §20 XX:** the retry is judged and stamped at the original press instant. **Carried: §6** (one retry inside the press's transaction; `capture()` takes no time argument). The edge rules r6 N3 and gate r5 NB-25 raised (the retry at a later instant) is closed by XX. Option (b)'s later stored time is retired by FS §20 AAA (`FS:334`): the press instant is stored. The double failure is FS §20 DDD (OQ-27). | Nothing in Phase 3. The Phase 4 capture route follows §6 |
| OQ-27 | **The strip step fails twice for one press** (rules r6 N3 remainder; R-160 (3)). VV and XX give one retry. If the retried image is refused too, R-160 (3) requires at most one row and no prompt, so that press gives no photo, which "one press is still one photo" (VV) does not cover. A second retry, or any other step, is not in any doc. Not picked **Settled 2026-10-31, FS §20 DDD (`FS:337`): the user sees nothing different; that press gives no photo and the bug is logged; no error, no "try again". Carried: §6 (step 4: roll back and commit, no third call; the log is the server log, two refusal lines with one virtual transaction id, no image, no id, no statement text, unreadable by `mj_app` and `mj_panel`; tested). Raised from it: OQ-31 and OQ-32, both settled 2026-10-31 (FS §20 FFF, GGG, HHH; then III, JJJ)** | Nothing in Phase 3 (was: Phase 4 capture route). Unreachable by every sample (§6 check) |
| OQ-28 | **The Positivity Feed's sort key** (rules r6 N6; R-155 (d)). DN B9 (e) gives "newest first" (`PROVISIONAL: B9`), and FS §20 Q makes each entry a reflection's text. Which time "newest" sorts by is not stated: the reflection's `written_at`, or the journey's reveal or unlock. Any answer must meet FS §20 GG, JJ and ZZ: never `captured_at`, a note's `written_at`, `ctid` or `xmin` (R-155 (d)); never `journey_reveal.finished_at` or `unlocks_at` for a public reader, since ZZ and §20 T keep both from them and a sort by either gives their order; ties by the random `id` (JJ). The only time in the docs that a feed reader already reads is the reflection's `written_at` (P1:114; §4 item 6 table). Not picked **Settled 2026-10-31, FS §20 BBB (`FS:335`): newest reflection first, by the reflection's written time. Carried: §11 (`positivity_feed_rows()` ends `ORDER BY r.written_at DESC, r.id`; it returns `reflection_id`, `photo_id` and `text`, no time-typed column; tested against a plain-SQL oracle, with a planted `captured_at` sort caught). Found while confirming it: OQ-30** | Nothing now (was: Phase 4 Positivity Feed query, S-09) |
| OQ-29 | **A public viewer's count of another user's rings** (FS §20 WW, ZZ; SI OQ-44). WW: others see one ring per finished reveal. ZZ: a public reader may infer reveal state from rings. A network viewer can count `journey_reveal_rows()` for that owner, but SS gives a public viewer no reveal record, so no reader gives the app that count for a public viewer. Options include a count-only definer function, or no rings on S-16 for a public viewer. A count that a public viewer can poll would show when each reveal finished, which goes further than "infer". Not picked **Settled 2026-10-31, FS §20 CCC (`FS:336`): public viewers get a ring count only; one reader returns the number of finished reveals for a profile and nothing else, no dates. Carried: §11 (`ring_count(profile_id uuid) → integer`, EXECUTE for `mj_app` only, the same number for every viewer) and §3 `b4`. Tested: no date in its result, and polled by a public viewer it changes only when, and by as much as, a network member's "journey launched" count changes; two planted faults caught** | Nothing now (was: Phase 4 S-16 for a public viewer) |
| OQ-30 | **A public reader can bracket a journey's unlock date** (found while confirming FS §20 BBB). `positivity_feed_rows()` returns no time. But a public reader who opens an entry reads the photo's `captured_on` (FS §20 GG) and, through `reflection_rows()`, the reflection's `written_at` and `year_index` (P1:114–115; reflections follow the photo, D11). A photo is captured before unlock and a reflection in slot *k* is written in [unlock + (k−1) years, unlock + k years) (FS §20 D). So `captured_on` < `unlocks_at` ≤ `written_at` − (k−1) years, and a slot-1 reflection written soon after a late capture pins the unlock date within days. FS §20 T says a journey's dates are never public. This is not new with BBB: it follows from P1:114 as approved, and BBB's sort adds nothing to it. Options include masking `written_at` and `year_index` for non-network readers (as TT masks `joined_at`), giving them a coarser time, or accepting it as an inference as ZZ does for the reveal state. Not picked **Settled 2026-10-31, FS §20 EEE (`FS:338`):** inference allowed; no change. `reflection_rows()` keeps `written_at` and `year_index` for every reader of the photo, and no reader returns a journey date to a public reader as a field (§11). KKK (`FS:344`) applies the same to the order of journeys on a path (Screen-Inventory OQ-44). | Nothing now (was: `reflection_rows()` columns for a public reader, Phase 3; S-17 and the Positivity Feed's opened entry, Phase 4) |
| OQ-31 | **Two limits on DDD's "the log carries no image"** (§6). (a) `log_parameter_max_length_on_error` is user-settable in Postgres 16, so code holding an `mj_app` or `mj_panel` connection can run `SET log_parameter_max_length_on_error = -1` and get its own image and journey id written into the server log on a refusal (tested, counterfactual 2). No grant can stop a user-settable parameter. The route never sets it (Phase 4 route test), and such code can already act as any user (OQ-12). Accept with OQ-12 until real authentication, or require more? (b) **What the line holds was built on the strictest reading**: fixed text, no user, journey or photo id and no `app_now()`. The real time and the virtual transaction id come from the line prefix. A developer chasing the bug may want the journey or the strip step's version in the line. Not added, since a sealed journey's id beside a real time records that its owner pressed then. Confirm or widen **Settled 2026-10-31, FS §20 FFF (`FS:339`):** both accepted; no change. (a) is recorded in §6 as an accepted residual, to be fixed before real users with OQ-12. | (a) Deploy (with OQ-12). (b) Nothing in Phase 3 |
| OQ-32 | **After a double refusal (DDD), two points the rulings do not reach.** (a) The guard runs before the §20 U order (§6), so the route cannot tell whether the lost press would have been accepted or refused (no frame left). "The user sees nothing different" then has no single answer: different from an accepted press, or from what that press would have given? What follows on screen is also open: an accepted press goes on to the note offer (S-12), and here no photo exists to attach a note to (Screen-Inventory OQ-47). (b) VV, XX and DDD speak of the press. The note step's guard refusal is logged the same way (§6), but whether the note step strips again and retries once is not ruled **Settled 2026-10-31: (a) FS §20 GGG (`FS:340`), its "no note offer" part retired by JJJ (`FS:343`): the screen looks exactly as after a normal press, note offer included, and a note written for a lost press is discarded; (b) FS §20 HHH (`FS:341`), with III (`FS:342`): a note lost twice ends the note step. Carried in §6 (the note route's transaction and the discarded note) and tested (`mj_scratch_r8`).** Raised while carrying them: OQ-33 and OQ-34. **(a)'s "or from what that press would have given" settled 2026-10-31 by FS §20 QQQ (`FS:352`; rules r8 G-25): the press it would have been. `capture()` now judges the §20 U order before the guard, so the route can tell. Carried in §6 ("Judged first") and tested (`mj_scratch_r10`). The opening sentence of (a) describes the order before QQQ.** | Nothing in Phase 3 beyond OQ-33. Phase 4: the capture and note routes follow §6, and S-02 and S-12 follow JJJ and III (ux) |
| OQ-33 | **How the note step names the photo it is for** (found 2026-10-31 while carrying FS §20 JJJ). `capture()` returns only `accepted` or `refused` (P1:49, §4 item 3, §6 step 5). Before unlock no reader returns a sealed photo, including to its owner (P1:48 (a)). Yet the note step needs its photo (P1:104, `photo_id`), and S-12 reads "Photo (id only)" (`Screen-Inventory.md` S-12). No doc says how the route learns which photo a note press is for. JJJ makes the answer matter. After a lost press there is no photo, and the note must be discarded, never attached elsewhere. A route that picked "the owner's latest photo without a note inside 15 minutes" would attach it to an earlier photo (tested, §6: the planted fault is caught). Any answer must also keep a lost press looking exactly like a saved one to the user (DDD, JJJ). Options include `capture()` returning the new photo's id to the route alone, or the capture and note presses sharing one route-held handle. The first changes P1:49's "only `accepted` or `refused`", and the second is a route design. Not picked **Settled 2026-10-31, FS §20 LLL (`FS:345`): a server-side handle, given by `capture()` to the server route only, one-time, valid for the note window, never exposed to the device as a photo id; and NNN (`FS:347`): after a lost press the note step closes 15 minutes after the press. Carried: §6 "The note handle" (the new photo's id in the transaction-local `mj.note_handle`; route memory per device session and acting user; one note transaction; a lost press's entry leads to "discard"; window judged by `app_now()`), P1:49, P1:105, P1:108, P1:180; no table or field; tested (`mj_scratch_r9`, four planted faults caught). Raised: OQ-35** | Nothing in Phase 3 (was: the note step's arguments and the loader's note calls). Phase 4: the capture and note routes follow §6 |
| OQ-34 | **III is held by the route only** (FS §20 III, `FS:342`). A note lost twice leaves no trace, since HHH and PP store nothing. So the database cannot tell a lost note from no note, and a later note-step call for that photo inside its 15 minutes would be accepted (tested, §6). Enforcing III in the database would need a stored trace of the lost note, which is a new field and would contradict "nothing stored". As carried: the route never makes a second note transaction for a photo (the Phase 4 route test, §6). This is the same kind of residual as OQ-12: code that holds an `mj_app` connection can already act as any user. Accept with OQ-12, or require more? **Settled 2026-10-31, FS §20 MMM (`FS:346`): III is enforced by the server route only; the database stores nothing about a lost note; accepted alongside OQ-12, revisit before real users. Carried: §6 (the route drops the note handle when its first note transaction ends), §8 OQ-12, P1:105; tested (`mj_scratch_r9`: a later note press after a lost note calls no note step; planted route that keeps the handle caught)** | Nothing in Phase 3. Phase 4 note route test; deploy (with OQ-12) |
| OQ-35 | **The route's note handles do not survive a server restart** (found 2026-10-31 while carrying FS §20 LLL). LLL keeps the handle on the server, not on the device, and without a new table it can live only in the route's process memory (§6). If the route process restarts inside a note window, its entries are gone. A note press after that finds no entry, so no note step is called. Nothing wrong is stored and no note can attach to the wrong photo, but for an accepted photo the note step then ends earlier than its 15 minutes, which S-12 does not list as one of its ends (`Screen-Inventory.md` S-12). Keeping handles across a restart would need them stored, which is a new table (a model change) or a session store outside the database (a new piece of infrastructure). As written: a restart drops the entries, and the note press answers as after a closed window. Accept for the local prototype (one route process), or require handles to survive a restart? Not picked **Settled 2026-10-31, FS §20 PPP (`FS:350`): accepted for the local prototype; residual next to OQ-12, solved before real users. The S-12 part is answered by FS §20 RRR (`FS:353`): a note press answered `closed` after a restart looks exactly as when the window has ended. Carried: §6 ("Where the route keeps it", "The note press"), §0, §8 OQ-12 and "Before real users"; tested (`mj_scratch_r10`: restart, ended window, skip and lost press after a restart give one byte-identical `closed`).** The screen row is ux's (rules r8 V2, R-171) | Nothing now. Before real users (with OQ-12) |
| OQ-36 | **What QQQ's judgment leaves** (found 2026-10-31 while carrying FS §20 QQQ, `FS:352`). To judge a press first without storing anything, `capture()` now runs steps 1–5 before the image guard (§6, "Judged first"). The judgment is the normal press's own code, so it reads nothing a normal press does not, and the device gets nothing a normal press does not (tested). Three effects are not covered by a ruling. (a) **DDD's "the bug is logged" on a press judged refused.** The guard does not read a refused press's image, so a strip fault on that press is neither detected nor logged. The press is answered `refused` and stores nothing, as QQQ requires. Logging it would mean running the guard on a refused press too, which needs either a second error the route must tell apart from the guard's (a new result) or a log line that does not abort (a new log form). Built: not logged. (b) **A judgment without a press.** Code that holds an `mj_app` connection can call `capture(journey, image)` with an image that fails the guard. It answers `refused` or raises and stores nothing either way, so that code learns whether a press would be accepted without using a frame (tested). Before QQQ the guard ran first and always raised. This cannot be avoided: the route holds only `mj_app`, so anything that lets the route tell the two branches apart lets any `mj_app` holder do the same. The device cannot reach it, because the server strips every image (PP). It is the same class as OQ-12. (c) **The server log** now holds refusal lines only for presses judged accepted. So the log, which no product role reads and which carries no id, also records that a press at that real time would have been accepted. Accept (a)–(c) with OQ-12, or require more? Not picked **Settled 2026-10-31, FS §20 SSS (`FS:355`): accepted; Before real users item 7.** | Nothing now |
| OQ-37 | **The remaining timing gap between a lost press's note and a saved note** (rules r8 N3; R-170 (3)). Every note press now runs one route shape, so the strip step, which is the largest cost, is the same in both (§6, "Timing"). What remains is the note step's database work, which only a saved note does: guard walk, encryption, insert, trigger and WAL flush. Measured on the local Postgres 16: 5.3 ms at the median, 7.9 ms at p95, for a 261 KB page (§6 evidence). Closing it would need the note step's encryption and a write that stores no row, or a padded wait. Neither is in any ruling, and a padded wait is a timer in the route. Not built. Accept the residual (S-12 then must not wait on the note answer in a way that shows it, R-170 (3)), or require more? Not picked **Settled 2026-10-31, FS §20 TTT (`FS:356`): accepted; Before real users item 8.** | Nothing now |
| OQ-38 | **The timing of a press or note press that meets the guard bug** (rules r9 N3; R-170 (4); found 2026-10-31 while measuring it). S-02 waits for the press answer, since `accepted` leads to S-12 and `refused` does not, so the press's own time reaches the screen. After a guard refusal the route strips again (FS §20 VV, HHH), so the presses that meet the bug answer later than a saved one. Measured at the median for a 384 KB photo (§6, "The press's own timing"): a lost press is 16.7 ms later and a press saved by the retry 21.1 ms later. For a 276 KB page, a note lost twice is 10.8 ms later and a note saved by the retry 14.4 ms later. TTT accepts only the note step's database time (about 5 ms), which is the discarded note's 6.4 ms here. The extra strip is not covered by any ruling. It occurs only when the strip step has a bug, which the build check makes unreachable for every sample (PP). Closing it would need a padded wait, which is a timer in the route (as for OQ-37), or no retry, which VV and HHH rule out. Accept the residual for the prototype (S-02 must then not show the wait, R-170 (4)), or require more? Not picked. **Settled 2026-10-31: FS §20 AAAA (`FS:363`), accepted for the prototype ("Before real users" item 9; §6 "The press's own timing").** | Nothing in Phase 3. Phase 4 S-02 and S-12 review |
| OQ-39 | **Two route cases that no ruling covers, found while carrying WWW and YYY** (§6). (a) **A client that never sends the skip.** WWW is held by the skip request: S-12 sends it on skip and on leaving capture, and the route drops the entry. A client that does not send it, and then sends a note press inside the 15 minutes, has that note taken. The product's S-12 never does this, so only code outside the product's client reaches it. That is the same class as OQ-12 and MMM. Holding WWW without the device's word would need the route to end the entry on some other signal, and none is ruled. Accept with OQ-12 until real users, or require more? (b) **`add_note()` refusing inside a window the route read as open.** The route's window read and `add_note()` judge the same two bounds at the same frozen instant, the entry is keyed to the acting user, and a handle serves one note transaction. So through the route, `add_note()` can refuse only if other code has already added a note to that photo (the MMM residual). No ruling says what the device then receives. RRR's "closed" covers a closed window, and ZZZ's "saved" covers a note lost twice. The test's route stand-in sends `closed` there, as scaffolding only, so that planted fault (e) runs. That is not a design. Not picked. **Settled 2026-10-31: FS §20 BBBB (`FS:364`). (a) Accepted with OQ-12 ("Before real users" item 10). (b) The device gets the one `closed` answer, now the design (§6 "The note press"; tested, `mj_scratch_r12`).** | (a) Deploy (with OQ-12). (b) Phase 4 note route |

### Before real users (rules r8 N6)

Every residual that a ruling or this file accepts only until real users, in one place. None blocks the local prototype. Each must be closed, or ruled on again, before any real user's data enters the system or any deploy. The deploy host is still open (OQ-12). Each row names where the residual is carried.

| # | Residual | Accepted by | Carried in |
|---|---|---|---|
| 1 | Viewer identity is a per-transaction setting, so any holder of the app role can act as any user. Needs real authentication | OQ-12 (C11, C16) | §2.1, §8 OQ-12 |
| 2 | A holder of an `mj_app` connection can keep a press transaction open and capture later at the earlier instant | Closed by item 1 (§6) | §6 "Residual" under VV, XX |
| 3 | `log_parameter_max_length_on_error` is user-settable, so a product connection can put its own image and ids into the server log on a refusal | FS §20 FFF (`FS:339`; OQ-31 (a)) | §6 DDD |
| 4 | III is held by the route only. A holder of a product connection and a handle can call the note step again after a lost note | FS §20 MMM (`FS:346`; OQ-34) | §6 III; R-169 |
| 5 | Note handles live in route memory and are lost on a restart. That note step ends early and is answered `closed` | FS §20 PPP (`FS:350`), RRR (`FS:353`; OQ-35) | §6 "Where the route keeps it" |
| 6 | Query timing can still depend on rows the viewer cannot read (B-tree depth, cache) | FS §20 RR (`FS:322`; OQ-24) | §10, §11 |
| 7 | Accepted: a judgment without a press, the unlogged strip fault on a refused press, and the accepted-only log lines (QQQ) | FS §20 SSS (`FS:355`; OQ-36) | §6 "Judged first" |
| 8 | Accepted: the note step's database time, which only a saved note spends (about 5 ms) | FS §20 TTT (`FS:356`; OQ-37) | §6 "Timing" |
| 9 | Accepted: the extra strip after a guard refusal, so a press or note press that meets the guard bug answers 10–21 ms later than a saved one at the median | FS §20 AAAA (`FS:363`; OQ-38) | §6 "The press's own timing" |
| 10 | Accepted with OQ-12: a client that never sends the skip request can still have a note taken inside the 15 minutes | FS §20 BBBB (`FS:364`; OQ-39 (a)), with OQ-12 | §6 "The skip request"; §8 OQ-12 |

Not on this list, because no ruling ties them to real users: C17 (OQ-13), OQ-3, and the highlight-by-date residual (§4, R-151). Each stays open where it is recorded. Until 2026-10-31 this paragraph also read "OQ-38 and OQ-39 are open too, and are not on this list unless the user accepts them until real users"; FS §20 AAAA and BBBB accepted them, as items 9 and 10.

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

Ruling (`FS:319`, user 2026-10-30): every table with user content, not only sealed content, is read only through definer readers with fixed row estimates. This is §10's mechanism (a) applied to every such table. No table or field changes. Each reader applies exactly its table's read rule, and the policy states the same rule. Three read rules changed on 2026-10-31, each by a ruling: `user` (FS §20 TT), `journey_reveal` (SS, ZZ) and `announcement` (UU, with DN B10 now carried; rules r6 V1–V3, gate r5 B-5, B-6). The readers and policies changed with them (below).

**The tables, and their readers.** Every object of P1 §2.2 and every record of P1 §2.4 that holds something a user made or did:

| Table | Reader (SECURITY DEFINER, `ROWS 1000`) | Read rule, unchanged | Rule from | Starts from |
|---|---|---|---|---|
| `user` | `user_rows()` → (`id`, `name`, `joined_at`) | Rows: every viewer, every row (names to everyone). **Column mask: `joined_at` only on the viewer's own row, NULL on every other** (FS §20 TT, `FS:324`). **No `profile_picture` column:** the field stays unused, and no writer sets it (FS §20 YY, `FS:332`; DN C7) | FS §20 TT, YY; P1:45 | The table: this rule reads every row |
| `journey` | `journey_rows()` | The owner, always (sealed: type and dates only, P1:84); the owner's network from unlock (FS §20 T, X) | P1:84, §5 | The viewer's journeys by `user_id`; network owners by `layer(member_id)`, then `journey(user_id)` |
| `photo` | `photo_rows()`, view `photo_read` | `photo_readable(id)` | §4 items 4–6, §10 | Readable photos (below) |
| `note` | `note_rows()`, view `note_read` | `photo_readable(photo_id)` | §4 item 5 (vi) | Readable photos |
| `highlight` | `highlight_rows()` | The owner, from unlock (`PROVISIONAL: B24`) | §4 item 1 | The viewer's journeys |
| `reflection` | `reflection_rows()` | `photo_readable(photo_id)` (D11) | P1:117, §4 item 5 (iv) | Readable photos |
| `journey_overview` | `journey_overview_rows()` | `overview_readable(journey_id)` (FS §20 HH), whose B2 term is `PROVISIONAL: B2` | §5 | Readable journeys |
| `journey_chapter` | `journey_chapter_rows()` | From unlock, the owner and the network (FS §20 T, X) | §5 | Readable journeys |
| `journey_feeling_tag` | `journey_feeling_tag_rows()` | The same | §5 | Readable journeys |
| `person_tag` | `person_tag_rows()` | `photo_readable(photo_id)`, and the photo's owner only unless `c6 = shown` (`PROVISIONAL: C6`, R-148) | §3, §4 item 5 (iv) | Readable photos |
| `photo_visibility` | `photo_visibility_rows()` | `photo_readable(photo_id)` | §4 item 5 (iv) | Readable photos |
| `layer` | `layer_rows()` | `owner_id = viewer()` | P1:51 | `layer(owner_id)` |
| `announcement` | `announcement_rows()`, §3's "announcement read function" (no subject under `b11 = unnamed`, `PROVISIONAL: B11`, R-146) | "Journey launched" and "path crossed": the actor's network (R2, FS §20 M); never the actor, whose map never holds them (FS §20 UU). "Reflection left": the actor, who is the photo's owner (FS §20 UU); otherwise **only a member of the owner's network who can read the photo, even when it is public** (`PROVISIONAL: B10`, narrowing D18 / FS §20 J "people who can see that photo"). Before 2026-10-31 this cell read "readers of the photo", which sent public photos' announcements to strangers (rules r6 V3) | P1:168, P1:405, §3; DN B10; FS §20 UU | Network owners by `layer(member_id)`, plus the viewer as actor; then `announcement(actor)` |
| `journey_reveal` | `journey_reveal_rows()` → (`journey_id`, `finished_at`) | **After unlock, the owner and the owner's network; never a public reader or a stranger** (FS §20 SS, `FS:323`, the §20 T rule). No other reader returns the reveal state to a public reader as a field (FS §20 ZZ, `FS:333`). The network learns nothing new from `finished_at`: "journey launched" already carries that instant (`at`). **Also counted, never listed, by `ring_count(profile_id)`** for every viewer: the number of a user's finished reveals and nothing else (FS §20 CCC, `FS:336`; below) | FS §20 SS, T, ZZ, CCC | The viewer's journeys by `user_id`; network owners by `layer(member_id)`, then `journey(user_id)`; then `journey_reveal` by its key. `ring_count()`: `journey(user_id)` for the profile, then `journey_reveal` by its key |

"Readable journeys" are the viewer's own and those of owners whose map holds the viewer. "Readable photos" are the photos of those journeys, by the `journey_id` index, plus public photos through a partial index on `photo_visibility` where the setting is public; both then filtered by `photo_readable()`. The starting set always contains every row the predicate allows, so the start only decides how much is read, never what is returned (tested below).

**The three rules of 2026-10-31, as built.**

- **`user`, a column rule (FS §20 TT).** Row-level security works per row, and every viewer reads every user row, so a policy cannot carry TT. The same pattern as `photo_captured_at()` does (§4 item 5): `user_rows()` returns `CASE WHEN id = viewer() THEN joined_at END`. The policy stays `USING (true)` for rows. It is a second guard only, and the mask lives in the reader. Definer writers that need another user's `joined_at` read it internally and return nothing of it. The person-tag writer is one: a tag must come after the tagged user's `joined_at` (P1:215).
- **`journey_reveal` (FS §20 SS, ZZ).** The policy changes from P1:45's "same grant", which allowed every row, to `USING (journey_reveal_readable(journey_id))`. That internal predicate (SECURITY DEFINER; no EXECUTE for `mj_app` or `mj_panel`) is true when `app_now() >= unlocks_at` and the viewer owns the journey or `viewer_in_network(owner)`. Before unlock no row exists, since the reveal is finished only after unlock (P1:164), so the owner reads one exactly when the reveal is finished: S-04 and the finish screen (SI:153, :503) have their state. **ZZ: nothing returns the reveal state to a public reader as a field.** `journey_reveal_rows()` returns no row to them. `journey_rows()`, chapter and feeling-tag rows and "journey launched" are network-only (§20 T, R2). The Positivity Feed reader returns reflection text only (FS §20 Q) and selects by reveal state without returning it (DN B9 (f)). `ring_count()` returns how many of a user's reveals are finished, never which journey's, and no time (FS §20 CCC). What a public reader may still infer (the feed, rings, photos appearing under `b2`) is the inference ZZ allows (Rubric G-23). A direct `photo_readable()` call under `after_reveal_finished` answers only what the photo appearing already answers (FS §20 FF reasoning).
- **`announcement` (FS §20 UU, DN B10).** The policy changes to `USING (announcement_receivable(type, actor, subject))`. That internal predicate (SECURITY DEFINER; no EXECUTE for `mj_app` or `mj_panel`) gives "reflection left" to the actor, or to a viewer who is in the actor's network and for whom `photo_readable(subject photo)` is true. It gives every other type to the actor's network. The reader starts from the network owners, not from readable photos, since B10 requires the network.
- **The names are the developer's**, as for the writers. The predicates' grants are not: neither product role may call them.

**The two readers of FS §20 BBB and CCC (user rulings 2026-10-31), as built.**

- **The Positivity Feed, `positivity_feed_rows()` → (`reflection_id uuid`, `photo_id uuid`, `text text`)** (FS §20 BBB, `FS:335`; settles OQ-28). SECURITY DEFINER, fixed `search_path`, `ROWS 1000`, EXECUTE for `mj_app` only. Its selection is unchanged: reflections on photos set Public (B9 (b)), in journeys whose reveal is finished (B9 (f)) and that carry one of the four working tags (FS §20 W, CC), and for which `photo_readable()` is true. It starts from public photos through the partial index on `photo_visibility`. **Its body ends `ORDER BY r.written_at DESC, r.id`**: newest reflection first by the reflection's written time (BBB), ties by the random id (FS §20 JJ). `B9 (e)` "newest first" is now decided by BBB, so its sort key carries no `PROVISIONAL` label. The app shows rows in the order returned and re-sorts by nothing. **What it reveals to a public reader:**
  - **No capture or note time.** The order is by `reflection.written_at` only. No `captured_at`, `captured_on`, note `written_at`, `ctid` or `xmin` appears in the body's `ORDER BY` (R-155 (d)), and none is returned
  - **No journey date or reveal state.** The result has no time-typed column (tested: 0), and no `journey_id`, type, chapter or tag, so §20 T, CC and ZZ hold for the list. The order tells a reader only how the reflections' written times compare. The reader can already read those times through `reflection_rows()` on each opened photo (P1:114), so the order adds nothing
  - **Polling it.** A reflection appears when it is written. A reflection written before the reveal finished appears when the reveal finishes. This is the inference FS §20 ZZ allows ("from the Positivity Feed"). What `reflection_rows()` itself lets a public reader infer about unlock dates was OQ-30, not BBB. FS §20 EEE (`FS:338`) settles it: the inference is allowed, and there is no change
- **The ring count, `ring_count(profile_id uuid) → integer`** (FS §20 CCC, `FS:336`; settles OQ-29). SECURITY DEFINER, STABLE, fixed `search_path`, owned by `mj_owner`.
  - **What it returns.** The number of journeys of `profile_id` with a `journey_reveal` row and `app_now() >= unlocks_at`. The second term is a guard: a reveal finishes only after unlock, P1:164. It returns 0 for a user with none, for an id that matches no user, and for NULL. It is a scalar, not a set, and has no OUT column: it returns no date, no journey id and no per-journey state
  - **Who may call it.** EXECUTE for `mj_app` only: not `mj_panel` (which calls no product function, §2.1) and not PUBLIC. Any acting viewer may call it for any profile, their own included. It returns the same number to every viewer, owner, network, public and stranger alike, so it is no oracle for the caller's place on anyone's map. Limiting it to public viewers would add one
  - **Rows and estimate, as OO.** It is SECURITY DEFINER, so the planner cannot inline it. A scalar call plans as `Result (rows=1)` whatever the tables hold (tested before and after 200 other finished reveals), so it has the constant estimate that `ROWS 1000` gives the set-returning readers. Its body is journey-first: `journey(user_id)` for that profile, then `journey_reveal` by its primary key. It never scans `journey_reveal` (tested with `enable_seqscan = off`). The timing residual is RR's, as for every reader
  - **How it composes with WW and ZZ.** WW (`FS:330`): every other profile is drawn with this count, under both settings of `b4` (§3). The viewer's own profile under `per_year_with_app` is drawn from the viewer's own `joined_at` (TT), and under `per_finished_reveal` from this count. For a network viewer the count equals that owner's rows in `journey_reveal_rows()` (tested). ZZ (`FS:333`): the count is how many reveals are finished, never a field saying that a given journey's reveal is finished. A public reader who polls it learns that a reveal finished, and roughly when, the inference ZZ allows from rings. That is no more than the owner's network learns from "journey launched" at the same instant (FS §20 J, M), and no more than CCC grants. A count also implies a lower bound on time with the app (one journey at a time, each 12 months). WW already accepts that alongside TT
  - **What it never moves on.** Nothing about a sealed journey (a capture, a highlight or a commit), an unlock, a reflection, or a reveal choice made before finish. Only `finish_reveal()` moves it, by one (tested by polling, below)

Not user content, unchanged: `journey_type` and `chapter` (constants and catalogue), `prototype_option` (settings, §3), `sim_clock` (§1.1), `journey_key` (no privilege and no reader; only the key-release function, P1:48 (b)).

**Mechanism.**

- **Privileges.** `REVOKE ALL` on every table above from `mj_app`, `mj_panel` and PUBLIC. `SELECT`, `count(*)`, `EXPLAIN`, `xmin` and `ctid` on any of them are refused.
- **Readers.** As §10 (a): owned by `mj_owner`, SECURITY DEFINER, fixed `search_path`, `ROWS 1000`, EXECUTE for `mj_app` only. `EXPLAIN` on any of them shows `rows=1000` whatever the tables hold.
- **Internal helpers** (the network owners of the viewer, the readable journeys, the readable photo ids): no EXECUTE for `mj_app` or `mj_panel` (tested). One of them takes the viewer, a member, and returns owners. Neither role can call it, so P1:51 ("Nothing callable takes a member and returns an owner") holds. The readers that use it return only rows the policies already returned (FS §20 FF).
- **Writers.** The app role holds no INSERT either. Every insert goes through a SECURITY DEFINER function: `capture()`, the note step, `start_highlight()`, `commit()`, the join, `finish_reveal()` (which writes `journey_reveal`, `layer` and `announcement`, P1 §2.3), the reflection insert function (P1:52), and one function for each reveal-choice insert (visibility, person tag, chapter, feeling tag) and for the overview. Each carries in its body the check its insert policy carried. The insert-only triggers (P1:44–46, the 15-minute note rule, the slot uniqueness) stay on the tables and fire for every writer. No UPDATE, DELETE or TRUNCATE path exists, as before. The function names are the developer's.
- **Policies stay** on every table as a second guard, should a grant ever be added. The Positivity Feed query is another definer reader of the same kind, `positivity_feed_rows()`; its selection rules are unchanged (FS §20 W, Y, CC; DN B9). **It ends `ORDER BY r.written_at DESC, r.id`: newest reflection first, by the reflection's written time (FS §20 BBB, `FS:335`; settles OQ-28; above).** The key is never `captured_at`, a note's `written_at`, `ctid` or `xmin` (FS §20 GG, JJ, LL; R-155 (d)), and never the reveal's or the journey's dates (FS §20 T, ZZ). Ties go by the random `id` (JJ). Before 2026-10-31 (BBB) this line left the key open.
- **FS §20 FF unchanged.** `viewer_in_network()`, `overview_readable()` and `photo_readable()` stay executable by `mj_app`. §5's reason for that (a policy's functions are checked as the querying role) no longer applies once no policy is evaluated for `mj_app`. The grants stay because FF allows them and no ruling asks to remove them.

**Where OO meets an existing rule.**

1. **P1:44** "The app role has INSERT and SELECT only" (reflections, overviews), and P1:45's "same grant": superseded. The app role holds neither. Append-only is unchanged and stronger, since no direct write exists at all. P1:44–45 amended in line.
2. **P1:48 (a) and `.claude/agents/lead-tech.md:30`, "`count(*)` returns 0"** (until 2026-10-31 this item cited `CLAUDE.md`, which has no such line; rules r6 N4): on every user-content table `count(*)` is now refused, not 0. The 0 is read through the readers, as MM already did for photo and note (check 4). Rubric tests that query a table directly (R-002, R-010, and any test of tag, reflection or layer rows by table name) need rewording, which is for the rules-guardian.
3. **`journey_reveal`**: P1:45 gave it the same grant with no row rule, and this file's §3 gave the app role no grant. FS §20 SS (2026-10-31) settles it: `journey_reveal_rows()`, with the policy changed to match (above; was OQ-25 (b)).
4. **§2.5 check 7** ("no layer row with owner ≠ B is readable") now reads through `layer_rows()`; the table refuses.
5. **`user.joined_at`** (FS §20 TT) is a column rule. It lives in the reader's mask, and the row policy is unchanged (above).
6. **"Reflection left"**: the reader and the policy carried D18 without DN B10, so the equivalence test passed against a policy with the same gap (rules r6 V3). Both now carry B10 and UU, and check 3 compares against the rule as well as the policy.

No other conflict was found. The equivalence test below shows every reader returning exactly what its policy returned, under both settings of `b2` and of `c6`. The r6 test after it adds the rule oracle and the column mask.

**Checks (proposed, for the rules-guardian to number; each fails the build):**

1. **No privilege.** For `mj_app`, `mj_panel` and PUBLIC, no table or column privilege of any kind on any table in the product schema, other than SELECT on `journey_type`, `chapter` and `prototype_option`. A new table fails the build until it is added to that short list or given a reader.
2. **Fixed estimate, journey first.** Every set-returning function `mj_app` may EXECUTE is SECURITY DEFINER with `prorows = 1000`. `EXPLAIN SELECT * FROM` each reader shows `rows=1000` before and after the activity of §10 check 1. With `enable_seqscan = off`, the plan of each reader's body, run as `mj_owner` with a fixture viewer set, has no sequential scan on a user-content table other than `user` (whose rule reads every row). **The one scalar reader, `ring_count()` (FS §20 CCC):** SECURITY DEFINER, not a set, no OUT column, result type `integer`, and `EXPLAIN SELECT ring_count(…)` shows `Result … rows=1` before and after that activity. Any other function `mj_app` may EXECUTE that returns a scalar from a user-content table fails the build until it is reviewed onto this clause.
3. **Same rows and values as the policy and as the rule** (Rubric R-158 (3); extended 2026-10-31 for FS §20 TT and rules r6 V3). For each fixture viewer, at several clock points, under every setting of `b2` and `c6`, each reader is checked three ways:
   - **Against the policy.** It returns exactly the table rows for which the table's policy expression is true. The test evaluates the policy with that viewer set, either as the table owner or through a test-only role that holds SELECT and falls under the policies.
   - **Values too, through each column mask.** The comparison is over whole tuples, every returned column included, not over row ids. Each column equals the table's value, except a masked column, which equals its mask: `user.joined_at` only on the viewer's own row (TT); `photo.captured_at`, `photo.highlight_id` and `note.written_at` as §4 items 4 and 5. A reader that returns the right rows with an unmasked column fails.
   - **Against the rule.** The same tuples are also compared with an oracle the test writes from the rubric's read rule and the provisional defaults in force: R-152, R-158, R-161, R-162, R-088 with B10, R-089 with UU. The oracle is plain SQL that calls none of the schema's predicates, so a policy that shares the reader's gap cannot make the check pass.
   - **The feed and the ring count (FS §20 BBB, CCC), which have no table policy of their own,** are compared with their oracles only. `positivity_feed_rows()` is read `WITH ORDINALITY`, so the comparison covers the order as well as the tuples, against plain SQL sorted by `written_at DESC, id`. `ring_count(p)` must equal the plain count of `p`'s finished reveals, for every viewer and every profile, a missing id included. For a network viewer it must also equal that owner's rows in `journey_reveal_rows()`.
4. **Differential catalog test** of §10 check 1, with its targets extended to every user-content table and its primary key.
5. **The ring count by polling** (FS §20 CCC, ZZ; proposed, for the rules-guardian to number). The panel walks the clock through the fixture's later events, each step one transaction acting as `mj_app`: a capture into a sealed journey, a commit, an unlock, a reflection, finished reveals. At each step, First Light (public, on no map) reads `ring_count()` for each profile, and a member of each owner's network counts that owner's "journey launched" rows in `announcement_rows()`. Between every two steps, the change in the public count must equal the change in the network's count. A change the network did not see fails the build. The result type must be `integer`, with no set and no OUT column. Planted faults must be caught: a count from unlock, a count from commit, and a variant that returns a date.

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

AFTER OO (REVOKE ALL on the 14 tables from mj_app, mj_panel, PUBLIC; this block read "15" until 2026-10-31, see the note below it):
  table grants left 0; column grants left 0
  SELECT count(*) FROM reflection; SELECT xmin FROM journey; INSERT INTO reflection; UPDATE journey_overview;
  DELETE FROM person_tag; TRUNCATE layer                    -> ERROR: permission denied for table ...
  EXPLAIN on each of the 14 tables                          -> ERROR: permission denied for table ...
  EXPLAIN on the 10 readers, the journey_reveal stand-in, photo_read, note_read -> rows=1000; after a second 40-user batch: identical
  network_owner_ids(), candidate_journey_ids(), readable_photo_ids() -> ERROR: permission denied for function ...
  as A through readers: journey 3, reflection 20, person_tag 4, layer 1, announcement 14, overview 2
  reflection writer on A's own photo -> accepted (reader count 20 -> 21); on another user's readable photo -> refused
  mj_panel without SET ROLE: SELECT reflection / EXPLAIN journey / reflection_rows() -> ERROR: permission denied
  differential catalog test (§10 check 1, targets extended to the 14 tables and reflection_pkey), one session,
  around a third batch and VACUUM ANALYZE:
    mj_app: 1,090 probes answered; changed only clock_timestamp() gen_random_uuid() now() random()
            statement_timestamp() timeofday() transaction_timestamp()
    mj_panel native, and after SET ROLE mj_app: the same 1,090; the same 7
  timing (RR): reflection_rows() 2.9 ms -> 4.7 ms after 200,000 reflections A cannot read;
               scan-and-filter reader 58 ms -> 17,746 ms
```

The reflection written by the writer test was removed afterwards by the cluster superuser, in the scratch database only.

**The table count is 14 (gate r6 CF-36, corrected 2026-10-31).** The table above lists 14 user-content tables: the 10 of P1 §2.2's nine objects (`user`, `journey`, `photo`, `note`, `reflection`, `journey_overview`, `highlight`, `journey_chapter`, `journey_feeling_tag`, `layer`) and 4 of P1 §2.4 (`journey_reveal`, `person_tag`, `photo_visibility`, `announcement`). P1:48 (h) lists the same 14 (3 + 11), and the "BEFORE" line above has photo, note and highlight plus "the other 11". The other five tables are not user content (above): `journey_type`, `chapter`, `prototype_option`, `sim_clock`, `journey_key`. The "15" in the evidence block was wrong. `mj_scratch_oo` has been dropped, so whether that scratch held a fifteenth table cannot be checked now. Its block names no table outside these 19, and its "x 11 tables" row matches 14. Re-checked in `mj_scratch_r8` (2026-10-31, local Postgres 16.15, since dropped), with all 19 tables of P1 §2.2 and §2.4 as stand-ins: tables in the product schema 19; user-content 14; table privileges left for `mj_app` and `mj_panel` on anything but `journey_type`, `chapter` and `prototype_option` 0 and 0; column grants on the 14 for `mj_app`, `mj_panel` and PUBLIC 0; `EXPLAIN SELECT * FROM` each of the 14 as `mj_app` → `permission denied for table` 14 of 14. §11 check 1 is written over the schema, not a count, so the build is unchanged. `Status.md:132` now says 14 (re-checked 2026-10-31; until then this sentence said it still read "15"). "The 10 of P1 §2.2's nine objects" means 10 tables for nine objects: the Tag object is stored as two tables, `journey_chapter` and `journey_feeling_tag` (gate r7 observation).

**Evidence for the 2026-10-31 rules (FS §20 SS, TT, UU, ZZ; DN B10), throwaway `mj_scratch_r6`, local Postgres 16.15; database and roles dropped, cluster stopped.** Roles as §2.1, plus a test-only role `mj_policy_probe`. It holds SELECT on `journey_reveal` and `announcement`, and on `user` without `joined_at`, and falls under the policies, so the test evaluates the real policies with a viewer set. The users are the fixture's five plus a stranger on no map. The journeys are Lantern #1 (revealed) and #6 (sealed), Wind #1, Hands #1 and Round #3 (revealed), and Round #4 (unlocked, never finished). Maps follow P1 §3.4. The photos are private, network and public, and the announcements cover all three types. There are 4 clock points (2021-12-31 23:59:59, 2022-01-01 00:00, baseline, 2027-01-01) and both `b2` settings.

```
reader (as mj_app) = policy (probe role, mask applied) = rule oracle (plain SQL), md5 of whole sorted tuples:
  user            48 cases: 48 identical, 0 differing
  journey_reveal  48 cases: 48 identical, 0 differing
  announcement    48 cases: 48 identical, 0 differing
at baseline, b2 from_unlock (rows): journey_reveal  Lantern 3, Wind 2, Hands 3, Round 1, First Light 0, stranger 0
                                    announcement    Lantern 7, Wind 6, Hands 8, Round 2, First Light 0, stranger 0
                                    user            6 rows each; joined_at non-NULL on the viewer's own row only
mutants, each in a rolled-back transaction (reader = policy / reader = rule / caught):
  pre-r6 announcement rule, reader and policy both "readers of the photo"   48 / 14 / 34   <- r6 V3: policy-only test passes
  user_rows() returning joined_at to everyone                             0 / 0 / 48
  journey_reveal: every row (P1:45), reader and policy                    48 / 0 / 48    <- policy-only test passes
  journey_reveal: owner-only stand-in (the 2026-10-30 scratch)            22 / 22 / 26
ZZ, as First Light: journey_reveal_rows() for Round #3 (finished) and #4 (not) -> 0 and 0 rows; user_rows(): own joined_at only
as Round (owner): journey_reveal_rows() -> R3 2025-09-21 12:00:00+00 ; R4 absent (never finished)
as mj_app: SELECT count(*) FROM journey_reveal ; SELECT joined_at FROM user -> ERROR: permission denied for table ...
           journey_reveal_readable(R3)                                      -> ERROR: permission denied for function ...
has_function_privilege, journey_reveal_readable() / announcement_receivable(): mj_app f f ; mj_panel f f
EXPLAIN SELECT * FROM journey_reveal_rows() / user_rows() / announcement_rows() -> Function Scan ... rows=1000 (each)
enable_seqscan = off, bodies of journey_reveal_rows() and announcement_rows() -> index and bitmap scans only, no Seq Scan
UPDATE journey_reveal / UPDATE user, as the table owner -> ERROR: UPDATE on ... refused: insert-only
```

**Evidence for FS §20 BBB and CCC, throwaway `mj_scratch_r7`, local Postgres 16.15, 2026-10-31; database and roles dropped, cluster stopped.** Roles as §2.1. The users are the fixture's five plus a stranger. The journeys are Lantern #1, #2 (`thankful`) and #6 (sealed); Wind #1, #4 (`it eventually pays off`) and #6 (sealed); Hands #1 and #2 (`thankful`); and Round #2 (`it eventually pays off`), #3 (`worried for nothing`) and #4 (unlocked, never finished, given `thankful` and a public photo here, to test B9 (f)). Maps follow P1 §3.4. There are 11 reflections, inserted out of date order, two sharing one `written_at`. The polling run is on a real `mj_panel` login, each step one transaction acting through `SET LOCAL ROLE mj_app`.

```
BBB  positivity_feed_rows() result -> TABLE(reflection_id uuid, photo_id uuid, text text) ; time-typed columns 0 ; prosecdef t ; prorows 1000
     as First Light, Stranger, Second Wind (network), Lantern (owner), Round (owner): 7 rows each ;
       returned order (WITH ORDINALITY) and tuples = oracle (plain SQL, ORDER BY written_at DESC, id) -> t t t t t
     First Light's order -> h2 2025-06-29 ; w4 2025-04-26 ; r2 and l2b 2025-03-03 (tie, by id) ; l2a 2025-02-01 ; r2 2024-09-22 ; l2a 2023-01-21
     absent: Round #4 (reveal never finished) 0 ; network photo in a qualifying journey 0 ; non-working tags (Lantern #1, Round #3) 0
     EXPLAIN SELECT * FROM positivity_feed_rows() -> Function Scan on positivity_feed_rows (rows=1000)
     planted: the same feed sorted by captured_at DESC -> order = oracle: f (caught)
CCC  ring_count: args profile_id uuid ; result integer ; proretset f ; prosecdef t ; STABLE ; search_path=mj ;
       EXECUTE mj_app t, mj_panel f, PUBLIC f
     every viewer (L, W, H, R, F, S) x every profile, = oracle -> all t ; F 0, H 2, L 2, R 2 (R4 not counted), S 0, W 2 ;
       missing id 0 ; NULL 0
     network and owners, ring_count vs that owner's rows in journey_reveal_rows(): W->L 2/2, H->L 2/2, L->W 2/2, L->H 2/2,
       H->R 2/2, L->L 2/2, R->R 2/2 ; public F->L 2/0, F->R 2/0 (CCC: the count only; SS: no reveal rows)
     as First Light: journey_reveal_rows() 0 ; journey_rows() 0 ; ring_count(Round) 2 ; SELECT count(*) FROM journey_reveal -> permission denied
     EXPLAIN SELECT ring_count(...) -> Result (rows=1) ; after 200 more users with a finished reveal, ANALYZE -> Result (rows=1) ; Lantern still 2
     body, enable_seqscan off -> Bitmap Index Scan on journey_user_id_idx ; Index Only Scan using journey_reveal_pkey (no Seq Scan)
     polling, as First Light (public); "net" = a network member's count of that owner's "journey launched":
       0 baseline 2026-10-25                  F=0  L=2/net 2  R=2/net 2  W=2/net 2
       1 Lantern captures into sealed #6      F=0  L=2/net 2  R=2/net 2  W=2/net 2
       2 First Light commits                  F=0  L=2/net 2  R=2/net 2  W=2/net 2
       3 Lantern #6 unlocks 2027-01-01        F=0  L=2/net 2  R=2/net 2  W=2/net 2
       4 Lantern reflects                     F=0  L=2/net 2  R=2/net 2  W=2/net 2
       5 Lantern finishes #6 2027-01-10 12:00 F=0  L=3/net 3  R=2/net 2  W=2/net 2
       6 Wind #6 unlocks 2027-04-12           F=0  L=3/net 3  R=2/net 2  W=2/net 2
       7 Wind finishes #6 2027-04-25 12:00    F=0  L=3/net 3  R=2/net 2  W=3/net 3
       8 First Light #1 unlocks 2027-11-02    F=0  L=3/net 3  R=2/net 2  W=3/net 3
     changes between polls not matched by the network's count (32 intervals each):
       ring_count 0 of 2 (pass) ; planted count-from-unlock 3 of 3 (caught: L@3, W@6, F@8) ; planted count-from-commit 1 of 1 (caught: F@2)
     result-type check: ring_count integer t ; planted variant returning max(finished_at) -> timestamp with time zone (caught)
```

**Model change:** none. No table or field. Eleven reader functions (`journey_reveal_rows()` added 2026-10-31 for FS §20 SS; until then this line read "ten, and one" for OQ-25 (b)), plus the Positivity Feed reader `positivity_feed_rows()` (its order fixed by FS §20 BBB) and the scalar `ring_count()` (FS §20 CCC), both 2026-10-31, internal helpers (two internal predicates added 2026-10-31, for `journey_reveal` and `announcement`, neither executable by a product role), writer functions for the inserts the app role made directly, and grants. It changes the read path of every user-content table, and the write path of the tables the app role used to insert into directly.
