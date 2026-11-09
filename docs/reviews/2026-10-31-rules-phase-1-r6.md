# Rules audit: Phase 1 docs, round 6 (changes since 62c66b3)

Date: 2026-10-31. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-165 after this audit).

**Target:** `git diff 62c66b3..HEAD -- docs`, eleven commits from fd99657 to 04e4105. The diff covers:

- `Functional-Spec.md` §20 II–VV: new user rulings, at FS:313–326
- `Phase-1-Amendments.md` and `Phase-1-Proposal.md`: lead-tech's carriage of §20 EE–RR, with new sections §9, §10 and §11
- `Screen-Inventory.md`: ux carried EE, GG and HH, and the OQ-46 line
- `Decisions-Needed.md` B2, `Rules-Rubric.md` (R-151 and R-116 wording) and `Status.md`

Previous audit: `docs/reviews/2026-10-30-rules-phase-1-r5.md` (FAIL: V1–V3, N1–N6).

**Context:**

- No code exists, and `graphify-out/` is absent, so no graph queries were run.
- The §20 SS–VV rulings were recorded in 04e4105. That commit changed only the OQ-25 and OQ-26 cells of the Amendments' §8 table. No body section, no Proposal line and no screen was touched, so those rulings are carried in a table cell only.

**Verdict: FAIL.** There are 4 confirmed violations:

- **TT:** the join date still goes to every viewer.
- **SS:** no reader exists for the reveal state.
- **B10:** the default is dropped from the announcement reader.
- **VV:** the body still calls the question unsettled.

All r5 violations (V1–V3) are resolved.

---

## Auto checks run

```
$ git diff --stat 62c66b3..HEAD -- docs
 Decisions-Needed 2, Functional-Spec 14, Phase-1-Amendments 456, Phase-1-Proposal 42, Rules-Rubric 6,
 Screen-Inventory 64, Status 10, reviews/gate-1-r4 128

$ git show --stat per commit
 04e4105 (SS-VV): Functional-Spec 4, Phase-1-Amendments 4 (OQ-25, OQ-26 cells only), Status 1
 Screen-Inventory last changed in 9c6b32e (one OQ-46 line); nothing for MM-VV

$ git diff 62c66b3..HEAD -- docs ':!docs/reviews' | grep '^+' | grep -ioE "streak|badge|counter|progress|remind|notif|
  \blike\b|rank|leaderboard|level|unread|retake|try again|press again|countdown|timer|thumbnail"
  Every hit is one of four things:
   - a refusal ("never a retake", "no countdown", "nothing invites a second press")
   - a SQL token (NOT LIKE, row-level, progressive JPEG, WAL counters)
   - check 6's own word list
   - "corr(... capture rank)" in test evidence
  No banned element is added.

$ R-150 step 1 (labels), F = Phase-1-Amendments.md:
  B1 B10 B11 B12 ... unlabelled. Two of these are touched by lines new in this diff:
   - B10, by the announcement reader at :691 (V3)
   - B11, by `b11 = unnamed` at :691
  B2 is labelled in P1:126, not in the Amendments' §3/§11 lines
$ R-150 step 1, F = Phase-1-Proposal.md: B10 unlabelled (P1:168 announcement line)

$ R-165 open-word scan (new this round; command in the rubric), F = Phase-1-Amendments.md:
  30:  §20 OO row: "Ten readers now, one waiting (journey_reveal ...)"; "need the user's confirmation (OQ-25)"
  445: "What the app does with that press's image when the bug occurs is not settled (OQ-26)"
  679: user_rows() "Every viewer, every row ... (confirm: OQ-25 (a))"
  691: announcement_rows() "(confirm the actor's own: OQ-25 (c))"
  692: journey_reveal "None yet | Not picked: two lines disagree (OQ-25 (b))"
  711: "journey_reveal: P1:45 against this file's §3 (OQ-25 (b)). Not picked."
  (542-544 are other OQ rows citing OQ-21/22/24/26 as history: pass)
$ grep -n "waits on|not settled|Not picked|confirm" Phase-1-Proposal.md
  48: "(the journey_reveal reader waits on Phase-1-Amendments.md OQ-25)"

$ grep -n "joined_at" Phase-1-Proposal.md
  63: "| joined_at | |" (no reader rule)
  213: "Each user's joined_at is the date of their first Commit: Steady Lantern 2021-01-01 (#1) ..."

$ grep -n "B10" Phase-1-Amendments.md Phase-1-Proposal.md   -> no match
$ grep -n "^| B10" Decisions-Needed.md
  29: "Reflection left" reaches only the owner's network members who can see the photo, even when it is public

$ grep -n "count(\*)" CLAUDE.md                              -> no match (Amendments:710 cites CLAUDE.md for it)

$ grep -n "^## 21\|A time control" Functional-Spec.md         -> 335, 339
$ grep -noE "(FS|Spec):3[23][0-9]" docs/*.md
  Screen-Inventory 40, 510, 515: "Spec:321–331 (§21)"
  Rules-Rubric 894: "FS:325 ... heading at FS:321"
  These are stale: §20 grew by 14 lines. FS:321 is now §20 QQ.
```

---

## Status of r5 findings

| r5 item | Status | Evidence |
|---|---|---|
| V1: FS §20 EE not carried | **Resolved** | Amendments `:68` (§1.3), `:150–151` (§2.1 role table), `:231` (§3 grants), evidence `:112–133`, OQ-16 `:538`. P1 `:169–170`, `:195`. SI `:40`, `:516`, `:518`, `:535`, `:553` |
| V2: FS §20 HH not in the data layer | **Resolved** | Amendments `:224` (`b2` governs the overview through `overview_readable()`), `:387`, `:392`, evidence `:406–420`; P1 `:126`; SI S-15 `:373–374`. The "same line" point on notes and person tags is resolved at `:404` |
| V3: FS §20 GG not carried | **Resolved** | Amendments `:272` (§4 item 5 (i)–(vii)), evidence `:332–348`; P1 `:48` (f), `:50`, `:90`, `:106`; SI `:54`, S-16 `:396`, `:404`, `:410`; S-17 `:433` |
| N1: loader as panel role was a silent addition | **Resolved by the user** | FS §20 II (`FS:313`); Amendments `:158`, `:538` |
| N2: FF body called open | **Resolved** | Amendments `:390` ("Settled 2026-10-30, FS §20 FF") |
| N3: stale `RR:1185` | **Resolved** | Amendments `:255` gives `RR:1240` and the old value. G-13 is at RR:1240 before this audit's insertions |
| N4: S-15 should cite HH | **Resolved** | SI `:373` (source list), `:374` |
| N5: R-151 implementation wording | **Resolved** | b88ba1c, `Rules-Rubric.md:155` |
| N6: weakest points | **Partly resolved** | Activity graph resolution: resolved (Amendments `:272` (vii), P1 `:50`). C17 is still open (Amendments `:73`, `:535`). Highlight inference by date stays as the R-151 residual (Amendments `:271`) |

---

## Coverage of FS §20 EE–VV in the build docs

| Ruling | Amendments | Proposal | Screen-Inventory | Carried? |
|---|---|---|---|---|
| EE panel role | §1.3, §2.1, §3 | 169, 170, 195 | 40, 516, 518, 535, 553 | Yes |
| FF | §5 :390 | (none needed) | (none needed) | Yes |
| GG | §4 item 5 | 48 (f), 50, 90, 106 | 54, S-16, S-17 | Yes |
| HH | §3 :224, §5 :387 | 126 | 373–374 | Yes |
| II | §1.4, §1.5, §2.1, §2.2 | 195 | (none needed) | Yes. Its check is now R-163 |
| JJ | §4 item 6 | 48 (g), 89, 104 | 687 | Mostly. SI `:54` still says "not settled (OQ-46)" (N4) |
| KK | §6 :437 | 91 | (none needed) | Yes |
| LL | §4 item 5 (vi) | 106 | 687 | Mostly. SI `:54`, S-06 `:209` and S-17 `:433` say "written time", not "not even the date" (N4). Data layer correct |
| MM | §10 | 48 (h), 179, 195 | (none needed) | Yes |
| NN | §6 :441–446 | 91, 105, 180 | (none needed) | Yes |
| OO | §11 | 44, 45, 48 (h), 51, 168, 179 | (none needed) | Yes, except three rows, which are V1–V3 |
| PP | §6 :445 | 91 | **No** (S-02 `:84–95`) | Data side yes; screen side no (inside V4) |
| QQ | §6 :439, :444 | 91, 105 | (none needed) | Yes |
| RR | §10 :665 | 48 (h) | (none needed) | Yes |
| SS | **No** (`:692`, `:711`, `:30`, `:761`) | **No** (48 (h)) | (none needed) | **No: V2** |
| TT | **No** (`:679`) | **No** (63) | S-16 `:410` reads "User (name)"; S-06 `:209` "User" | **No: V1** |
| UU | OQ-25 cell only; `:691` still says "confirm" | **No** | (none needed) | The behaviour matches, but the B10 half is wrong: V3 |
| VV | **No** (`:445` "not settled") | **No** | **No** (S-02) | **No: V4** |

---

## Findings

### Confirmed violations

**V1. FS §20 TT is not carried. Every viewer, public readers included, reads every user's join date. In the fixture that is each user's first Commit date.** Rubric: R-161 (new), R-152, R-008, R-165 (new).

- **Where:**
  - `Phase-1-Amendments.md:679`: `user_rows()`, "Every viewer, every row: the P1:44–45 grant with no row rule (confirm: OQ-25 (a))". The `user` table holds `name`, `profile_picture` and `joined_at` (`:547`).
  - `Phase-1-Proposal.md:63`: `joined_at` has no reader rule.
  - `Phase-1-Proposal.md:48` (h) lists `user` among the reader-only tables with no row rule.
  - Only the OQ-25 cell (`:547`) records TT.
- **What is wrong:** FS §20 TT (`FS:324`) rules that "A user's join date (`joined_at`) is readable by that user only; everyone reads names". The reader as specified gives it to everyone.
- **Why it breaks the rule:**
  - `Phase-1-Proposal.md:213`: "Each user's `joined_at` is the date of their first Commit: Steady Lantern 2021-01-01 (#1) ...". First Light, a public reader on no one's map, therefore reads Lantern #1's commit date through `user_rows()`. FS §20 T and R-152 keep that date from public readers.
  - The product joins and commits as separate steps, but nothing stops a first Commit on the join day. For a user whose first journey is still sealed, the join date then gives the commit date of a sealed journey to anyone, which R-008 bans.
  - A decided ruling is contradicted in the build source (R-134; now R-165).

**V2. FS §20 SS is not carried. The reveal-state record has no reader, and the build docs still call its read rule "not picked".** Rubric: R-162 (new), R-165 (new), R-134.

- **Where:**
  - `Phase-1-Amendments.md:692`: `journey_reveal`, "**None yet** | **Not picked: two lines disagree (OQ-25 (b))**".
  - `:711`: "Not picked."
  - `:30`: "Ten readers now, one waiting (`journey_reveal` ...). Two carried rules need the user's confirmation (OQ-25)".
  - `:761`: "one waiting on OQ-25 (b)".
  - `:547`, Blocks column: "(b) blocks the Phase 3 `journey_reveal` reader", still present after the cell records the settlement.
  - `Phase-1-Proposal.md:48` (h): "the `journey_reveal` reader waits on `Phase-1-Amendments.md` OQ-25".
- **What is wrong:** FS §20 SS (`FS:323`) rules that whether a reveal is finished "is readable by the owner and the owner's network after unlock, never public, as §20 T". No body line specifies that reader.
- **Why it breaks the rule:**
  - As written, after OO no product role reads any reveal state (`:547` (b)). The owner cannot see that their own reveal is finished, which S-04 and the finish screen need (SI:153, :503).
  - A Phase 3 builder has two options: invent a read rule, or keep the stale P1:45 "same grant", which would open the record to every viewer, the public included. Inventing a rule breaks rule zero, and the P1:45 grant breaks SS.
  - Either path contradicts a decided ruling in the build source.

**V3. DN B10 is dropped from the announcement reader. As written, a public reader outside the owner's network receives "reflection left".** Rubric: R-088 (its B10 case), R-150, R-158 (new; see its item 3).

- **Where:** `Phase-1-Amendments.md:691`. `announcement_rows()` reads "reflection left: readers of the photo (D18, R2)", and its starting set is "readable photos, then `announcement(subject photo)`". B10 is labelled nowhere in the Amendments or the Proposal (R-150 step 1 output above). `Phase-1-Proposal.md:168` says only "worked out from visibility (see reading R2)".
- **What is wrong:** DN B10 (`DN:29`, provisional, in force) says: "'Reflection left' reaches only the owner's network members who can see the photo, even when it is public". "Readers of the photo" includes every public reader of a public photo.
  - Example: First Light reads Lantern #5's public photos (P1:314–319), so under §11 First Light gets Lantern's "reflection left" on them.
  - R-088's B10 case fails as built: "Lantern reflects on a Lantern #5 public photo: First Light and Long Way Round (not on Lantern's map) get no announcement".
- **Why it breaks the rule:**
  - A provisional default is replaced by a wider reading, without its label. R-150: "never extends a default ... to cases its row does not name".
  - Sending announcements to strangers puts more into a feed the product wants read less (`CLAUDE.md` "Low usage is the goal").
  - §11's proof cannot catch it. The equivalence test (`:735–736`, "264 identical, 0 differing") compares each reader with the existing policy, and the policy has the same gap. R-158 item 3 now requires the read rule to be checked against the rubric, not only against the policy.
- **Note:** the drift is older than this diff, since P1:168 never carried B10. §11 is the first place that states the rule in full, and this diff added it, so it is confirmed here.

**V4. FS §20 VV is not carried. The build source still calls the guard-bug case "not settled", on the path the no-retake ban protects.** Rubric: R-160 (new), R-031, R-165 (new).

- **Where:**
  - `Phase-1-Amendments.md:445`: "What the app does with that press's image when the bug occurs is not settled (OQ-26)." Only the OQ-26 cell (`:548`) records VV.
  - `Screen-Inventory.md` S-02 (`:84–95`) has no line for PP or VV. Its only refusal state is the no-frame refusal (`:89`), which shows copy. Nothing stops a builder sending a guard error to that same refusal copy, which PP bans.
- **What is wrong:** FS §20 VV (`FS:326`) rules: "the app strips again and saves that moment once ... One press is still one photo". The other reading, still open in the body, is OQ-26 (a): "that press yields no photo, silently". VV rejected it.
- **Why it breaks the rule:**
  - A decided ruling is contradicted on a banned-list path (no retakes, `CLAUDE.md:64`).
  - The capture screen is Phase 4, but the screen doc is the Phase 4 build source, and it is silent.
- **Edge VV leaves open:** see N3.

### Notes (not violations)

**N1. Conflict, raised and not picked: SS "never public" against three lines that let a public reader infer that a reveal is finished.** Added as Gap G-23. R-161 and R-162 run on the strictest reading.

- DN B9 (f) (`DN:28`): the Positivity Feed carries only journeys whose reveal is finished. First Light learns that Round #2 is finished.
- DN B4's default ring per finished reveal, shown to public viewers on S-16 (`Screen-Inventory.md:405`). SI OQ-44 is still open on rings for public viewers.
- FS §20 R (`FS:291`), under B2's option: Public photos appear only once the reveal is finished.
- Also under TT: B4's second setting, "per year with the app", shows others a ring per year since joining, which gives the join year. A switchable default must pass under both settings (R-141).

**N2. UU against B10, for the actor.** FS §20 UU (`FS:325`) gives the actor their own "reflection left". B10 (`DN:29`) sends it only to network members, and the owner is never on their own map (R-074).

- FS §20 outranks a provisional default (CL:30), so UU holds for the actor. B10 still holds for everyone else, which is V3.
- This is recorded as a `Decided` line on R-088 and R-089.
- UU's citation "As written in R2" is loose. R2 (`P1:405`) covers only "journey launched" and "path crossed". The reflection-left rule is FS §20 J and D18, narrowed by B10. OQ-25 (c) (`:547`) carries the same paraphrase.

**N3. A silent-decision risk inside VV.** The re-save is a second `capture()` call at a later `app_now()`. If the highlight closes, the month's frames lapse or the journey unlocks between the two calls, the re-save is refused or lands as a normal frame. Neither VV nor PP says what happens then, and "one press is still one photo" cannot hold as worded. This is recorded as `Open` on R-160 and goes to the supervisor. It must not be filled in by a builder.

**N4. Stale lines that do not change behaviour.** Each one should be fixed by its owner.

- **Status and source lines:**
  - `Phase-1-Proposal.md:3` reads "§20 Q–RR".
  - `Phase-1-Amendments.md:3` (status) lacks SS–VV, and `:7` reads "§20 Q–RR (`FS:290–322`)".
  - The OQ-25 and OQ-26 cells say "Settled 2026-10-30", but `Status.md:133` records those rulings on 2026-10-31.
- **Spec citations:** `Screen-Inventory.md:40`, `:510` and `:515` cite "Spec:321–331 (§21)". §21 is now FS:335–345, and FS:321 is §20 QQ. Rubric R-116 had the same problem; it now carries an `Updated` line.
- **Screen lines behind the rulings:**
  - `Screen-Inventory.md:54`: "The order of photos within one day, for a non-owner, is not settled (OQ-46)". JJ settled it, and `:687` already says so.
  - `:54`, S-06 `:209` and S-17 `:433` say "written time", where LL is "not even the date". S-06 `:209` reads "User", not "User (name)", which matters under TT.
  - The data layer is right in each case (`note_read`, Amendments `:272` (vi)), so nothing leaks.
- **`count(*)` lines:**
  - `Phase-1-Proposal.md:48` (a) still ends "so `count(*)` returns 0", while (h) refuses the table to the app role.
  - `Phase-1-Amendments.md:710` cites `CLAUDE.md` for "`count(*)` returns 0". `CLAUDE.md` has no such text (grep above).
- **Status.md rubric range:** `Status.md` gives the rubric range as R-001–R-154. It is now R-001–R-165. That is the supervisor's line, not edited here.
- **Unlabelled defaults in new lines:** B2 and B11 are touched without a `PROVISIONAL:` label at Amendments `:685` (overview reader, B2 term) and `:691` (`b11`) (R-150, labels).

**N5. The proposed highlight-name check, as worded, would not hold.**

- `Phase-1-Amendments.md:264`: "list every function whose body names `highlight`".
- Under `highlight_rules` (`:262`), every definer function and every view owned by the table owner, called from an app session, sees every row. A name scan of function bodies alone misses three things:
  - views, policies on other tables, rules and triggers
  - a table named at run time through dynamic SQL
- A substring reading would also catch `photo_highlight_id`.
- R-156 states the full check: whole-identifier match over functions, views, policies, rules and trigger functions, `pg_depend` for SQL-standard bodies, and a ban on dynamic SQL in table-owner functions unless reviewed. Its list now includes `highlight_rows`.

**N6. Weakest points carried forward:**

- **C17** (Amendments `:73`, `:535`): the next-unlock jump is built with no default and shows another user's unlock date to the demoer.
- **Highlight inference by date** (R-151 residual):
  - Narrowed by GG and JJ, not closed.
  - Under B5's `viewer_visible` setting, a per-day graph shows 19 Lantern #1 photos on one date (Amendments `:272` (vii)).
- **Query timing** (FS §20 RR, Amendments `:665`): accepted until real users. This is now recorded on R-157.
- **The Positivity Feed's sort key under JJ** (Amendments `:704`, DN B9 (e)): it is not stated. "Newest first" must not sort by `captured_at`. Added to R-155 (d).
- **Highlight rows are not on the immutability list** (P1:45 lists photo, note, journey and user name). `highlight_rules` is `FOR ALL` (`:262`), so a future definer function could UPDATE `ends_at` with no trigger to stop it. Today no ruling covers this; it is reported only.
- **OQ-3** (R-119 "after the map entry") and **OQ-12** (viewer identity before deploy) are unchanged.

### Checked and clean

- **The EE grants and evidence** (`:112–133`): the viewer role holds no EXECUTE on the clock, the next-unlock jump, `set_option()` or `clock_start()`, and cannot become the panel role. Matches R-153.
- **The §9 token scan:** a closed allow-list (`viewer`, `overview`), folded identifiers and planted failures all caught. It is the stronger form of R-100 to R-108.
- **The MM and OO mechanism** (§10, §11):
  - Every user-content table is refused to every product role, `EXPLAIN` included.
  - Estimates are fixed, and readers start from the journeys the viewer may read.
  - The differential catalog test shows only clock and random functions moving.
  - Internal helpers that take a member and return owners are not executable (`:702`), so R-070 holds.
- **KK, NN, QQ and PP (data side)** (§6): an allow-list guard before encryption, PNG removed, the strip output proven to pass for every sample, and "nothing invites a second press" (`:445`).
- **JJ** (§4 item 6): random v4 ids, no sequences, `(captured_on, id)` order, and evidence `:366–373` (correlation 0.141). It is now R-155.
- **`overview_readable()` callable directly** (`:390`): for network members it adds only the reveal state, which SS now gives them anyway.
- **DN B2 row** (`DN:21`) now points to §20 X and HH. This was r4 N1's last open part.

---

## Rubric changes

**Added:**

| Check | What it covers | Comes from |
|---|---|---|
| R-155 | No id or default order carries time | FS §20 JJ; the proposed check at Amendments §4 item 6 |
| R-156 | The only four ways to reach highlight rows (`capture`, `start_highlight`, `highlight_open`, `highlight_rows`) | FS §20 AA, DD, MM; the proposed check at §4 item 1; N5 |
| R-157 | No catalog statistic, estimate, size or counter shows hidden activity; the timing residual is accepted | FS §20 MM, OO, RR; Amendments §10 checks 1–4, §11 check 4 |
| R-158 | Every read goes through a reader with a fixed estimate; same rows as the rule, checked against the rubric and not only the policy | FS §20 OO; Amendments §11 checks 1–3; V3 |
| R-159 | No stored image carries time or place | FS §20 KK, NN, QQ; Amendments §6 |
| R-160 | One press is one photo; a guard refusal never reaches the user; one silent re-save | FS §20 PP, VV; V4 |
| R-161 | The join date goes to its own user only | FS §20 TT; V1 |
| R-162 | The reveal state goes to the owner and network after unlock, never public | FS §20 SS; V2 |
| R-163 | The loader and tests connect as the panel role and act one way as a viewer | FS §20 II; Amendments §2.4 |
| R-164 | A guard test must not pass on a privilege refusal alone: writer function and table-owner cases are required | Lead-tech's request at Amendments `:542`, `:710` |
| R-165 | Every §20 ruling is carried in each build doc; open-word scan | r5 V1–V3, r6 V1, V2, V4 |

**Lead-tech's rewording request is carried as dated `Updated 2026-10-31` lines.** The old wording stays, since the rubric never shrinks:

- R-001, R-002 and R-003 (the 0 is read through the readers; raw bytes are read as the table owner)
- R-010 (snapshots include the readers and the catalog fingerprint)
- R-015, R-018, R-021, R-022, R-023, R-026, R-052, R-057, R-084 and R-122 (the table-owner and writer-function cases)
- R-069, which covers R-072, R-073, R-074 and R-080 (through `layer_rows()`)
- R-151 and R-152 (through the readers)
- §2.5 mapping rows 1–5 and 7

**`Decided` lines added:**

- TT on R-008 and R-152
- SS on R-152
- LL and JJ on R-154, with its implementation now stated
- UU on R-088 and R-089
- PP and VV on R-031

**Other changes:**

- R-116's FS citation corrected by an `Updated` line.
- **Gap G-23** added (N1).
- The header note and the banned-list coverage have new paragraphs, and the "No retakes" and "Nothing leaks" coverage rows are extended.
- **Nothing was renumbered or removed.** The only changed lines are table rows, each kept whole with text added to it.
