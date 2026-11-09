# Rules audit: Phase 1 docs, round 4 (changes since f781223)

Date: 2026-10-30. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-152 after this audit).

**Target:** `git diff f781223..HEAD -- docs/Screen-Inventory.md docs/Phase-1-Proposal.md docs/Phase-1-Amendments.md docs/Decisions-Needed.md docs/Functional-Spec.md` (commits 5f92cb0 to 7c00352). Previous audit: `docs/reviews/2026-10-30-rules-screen-inventory-r3.md` (PASS, at f781223).

**Context:** no code exists; `graphify-out/` is absent, so no graph queries were run. FS §20 Q–DD are dated user rulings. Decisions-Needed B20–B26 are provisional defaults.

**Verdict: FAIL.** There are 3 confirmed violations. Two are decided rulings that the build docs do not carry, and both would let a non-owner read something a ruling withholds. The third is an R-150 breach.

---

## Auto checks run

```
$ git diff --stat f781223..HEAD -- <5 files>
 Decisions-Needed.md 19, Functional-Spec.md 18, Phase-1-Amendments.md 333 (new), Phase-1-Proposal.md 109, Screen-Inventory.md 122

$ grep -nE "chapter|feeling|highlight_id|§20 (T|X|CC|DD)|C17|C18|B2[0-6]" docs/Screen-Inventory.md
  -> no hit for §20 T, X, CC, DD, highlight_id, B20–B26, C17 or C18 anywhere in Screen-Inventory.md
  -> 201: S-06 `reveal-finished` Holds "... Chapter and feeling tags" (no reader limit)

$ grep -noE "(Spec|FS):(29[3-9]|3[0-9][0-9])" (SI, RR, Amendments, DN, P1)
  SI:40, SI:507, SI:512 Spec:299   (now §20 W; §21 is Spec:317–327)
  RR:860 FS:299                    (same; corrected in the rubric)
  SI:560 Spec:290, SI:561 Spec:291 (now §20 Q and R; "Export" and "Age gating" are Spec:312–313)
```

Banned-term scan of the added lines (streak, badge, counter, progress, remind, notification, retake, comment, like, rank, "n moments", countdown, "ends in", unread, "new"): no hit outside refusals ("no count column", "No countdown").

**Citation spot-check:** 25 of the 118 remapped `P1:`/`Proposal:` citations were checked against the current `Phase-1-Proposal.md`.

- SI:17 223–228
- SI:23 16, 210–211
- SI:27 81
- SI:29 82, 164
- SI:30 392
- SI:200 29
- SI:220 291
- SI:234/254 168, 181, 184
- SI:523 389
- SI:524 390
- SI:525 391
- SI:526 392–396
- SI:596 299
- SI:639 227
- RR:427 246
- RR:898 308
- RR:1177 46, 143, 165–166, 408
- Amendments:77 154, 199
- Amendments:263 143
- DN:21 318

All are correct except one: SI:639 (N3). Separately, Amendments:216 cites `RR:89–95` for R-008, but R-008 now starts at RR:95 (before this audit's additions) (N3).

---

## Findings

### Confirmed violations

**V1. The rulings in FS §20 T and §20 CC are not applied to reader screens. A public reader sees chapter and feeling tags.** Rubric: R-152 (new). Also R-134 and R-150.

- **Where:**
  - `Screen-Inventory.md:201`. S-06 `reveal-finished` "Holds" lists "Chapter and feeling tags" for every reader. `Screen-Inventory.md:184` lists "public (signed-in)" among S-06's viewers.
  - The same unrestricted reads appear in S-16 (`:390` viewer "network or public", `:407` reads Journey), S-17 (`:414` public, `:430` reads Tag) and S-09 (`:280` reads Tag and Journey for any signed-in reader, and `:264` leads to S-06 and S-16).
- **What is wrong:** FS §20 T (`Functional-Spec.md:296`) rules that a journey's type, dates, chapter and feeling tags are read after unlock by "the owner and the owner's network, never public". FS §20 CC (`:307`) rules that a feeling tag "never shows ... to a public reader".
  - P1 carries T (`Phase-1-Proposal.md:48` (d), `:84`, `:143`). Screen-Inventory, the doc Phase 2 and Phase 4 build screens from, carries neither ruling.
  - A public reader can follow a Positivity Feed entry into S-06 and be shown the chapter and feeling tags.
  - No S-06, S-16, S-17 or S-09 "Must never show" cell bans type, dates, chapter or tags to a non-network reader.
- **Why it breaks the rule:** a decided ruling is contradicted in a build source (R-134, CL:30). No rubric check covered T or CC, so R-152 is added.

**V2. FS §20 DD is contradicted. `photo.highlight_id` is "as readable as the photo itself".** Rubric: R-151 (new). Also R-008's B6 line and R-150.

- **Where:**
  - `Phase-1-Amendments.md:226`: "`photo.highlight_id` is a column of the photo row ... After unlock it is as readable as the photo itself (OQ-8)."
  - The amendments header (`:3`) and the OQ-8 row (`:326`) say OQ-8 is settled, but `:226` was left unchanged. It sits inside O4, which the user approved and which the builder implements.
  - `Phase-1-Proposal.md:92` (`highlight_id | Nullable`) and `:48` (a) carry no owner-only rule after unlock. Neither DD nor B24 appears in P1.
  - Screen-Inventory S-06 and S-17 (`:204`, `:428`) ban no highlight marker after unlock. S-16 `:400` bans it only while sealed.
- **What is wrong:** FS §20 DD (`Functional-Spec.md:308`) rules that `photo.highlight_id` is "readable by the owner only, also after unlock". DN B24 (`Decisions-Needed.md:59`) does the same for highlight rows, and DN B6 (`:25`) says "Others learn nothing about highlights", with no time limit.
- **Why it breaks the rule:**
  - A builder following the approved O4 text gives every network and public reader of Lantern #1 a field that marks the 19 graduation-party highlight photos.
  - Row-level security cannot hide one column of a readable row, and no doc says how DD is enforced (column grant or owner-aware view).
  - R-008 covers only the sealed year, so R-151 is added.

**V3. Questions that B20–B26 answer are still described as open, or left without their label.** Rubric: R-150 (existing check, steps 1, 3 and 4).

- **Where:**
  - `Phase-1-Amendments.md`:
    - `:58`: "Proposed sizes ... (OQ-1)". B20 answers it.
    - `:81`: "**Not specified; OQ-2.**". B26 answers it.
    - `:128`: "the time of day is OQ-4". B21 answers it.
    - `:228`: "OQ-9 asks for confirmation". B25 answers it.
    - OQ table `:319–331`: OQ-1, 2, 4, 6, 7 and 9 are not marked settled, while OQ-8 and OQ-15 are. OQ-10 and OQ-11 (`:328–329`) are not marked settled by §20 X and Y either.
  - `Screen-Inventory.md:514`: T-01 "Holds" lists only "+1 day, +1 month, +1 year, +5 years". It is missing +1 minute and +1 hour (`PROVISIONAL: B20`) and the running clock (FS §20 V). T-02 (`:528–549`) does not carry B22 (reset restores switches) or B23 (one global setting), and its "Reads" (`:549`) omits `prototype_option` (FS §20 Z).
  - `Phase-1-Proposal.md`: `:201` gives no baseline time and no `PROVISIONAL: B21` label. `:195` reset has no `B22` label. `:196–200` jump order has no `B26` label. `:133` has no `B25` label. `:48` (a) has no `B24` label.
- **Why it breaks the rule:** R-150 says that a deliverable "never calls such a question open" and labels every default it touches with `PROVISIONAL: <ID>`. The Amendments header (`:3`) maps the OQs to B20–B26, but the body still tells a reader to stop on them. Severity is low: none of these lets a banned item in.

### Notes (not violations)

**N1. FS §20 X is not carried where B2's option is described.** It is stricter, so nothing leaks.

- `Screen-Inventory.md:200` says "Under B2's option: others, nothing yet". X (`Functional-Spec.md:301`) gives the network type, dates, chapter and feeling tags from unlock under that setting.
- DN B2 row (`Decisions-Needed.md:21`) and FS §20 R (`:291`) still read "no one but the owner reads it", with no pointer to X.
- `Phase-1-Amendments.md:186` still has `b2` driving RLS on "journey, chapter and feeling tags, subject to OQ-10". X settled that it does not, as `:270` itself records.
- Rubric R-068 and R-142 now carry a `Decided (FS §20 X)` line.

**N2. Rubric R-103 had a stale reading** ("may be filtered by chapter (d)") after FS §20 Y. This was the rubric's own error. It is corrected, and the old wording is kept in the line.

**N3. Citation spot-check: 1 wrong of 25.** Two other references are stale as well:

- `Screen-Inventory.md:639` cites "Proposal:330 'tests a tag that isn't on the drafted list'". P1:330 is now "Derivation, every journey in §3.3". The quoted sentence no longer exists. Its successor is `Phase-1-Proposal.md:364` ("What the exclusions test: Steady Lantern #5's free-text tag is not on the list").
- `Phase-1-Amendments.md:216` cites `RR:89–95` for R-008. That is R-007; R-008 starts at RR:95 (before this audit's additions).
- Outside the remap, Spec citations past §20 are stale: SI:40, 507 and 512 cite `Spec:299` (now §20 W; §21 is Spec:317–327), and SI:560–561 cite `Spec:290–291` (now §20 Q and R; the items are Spec:312–313). The same problem in `RR:860` is corrected in the rubric.

**N4. Two open questions say "Still open, no ID", but both now have IDs.** `Screen-Inventory.md:665` (OQ-41) and `:667` (OQ-42) are now DN C17 and C18 (`Decisions-Needed.md:178`, `:180`). They are still open with no default, but they do have an ID (R-150 step 3).

**N5. C17 is still open, and the control it concerns is still built.** `Phase-1-Amendments.md:60` and OQ-13 (`:331`) build "jump to the next unlock" as P1:195 defines it, and C17 has no default. After the jump, the simulated date shown in T-02 equals another user's sealed `unlocks_at`, which is a field from a sealed journey shown through the panel (R-141, R-014). OQ-13 marks panel acceptance as blocked, which is correct. This is not a new violation, but it stays a weakest point until the user answers C17.

**N6. `viewer_in_network(owner_id)` (`Phase-1-Amendments.md:268`), if callable directly, lets a viewer enumerate whose maps they are on.** R-070 forbids a call that takes a member and returns owners. Looping this boolean over every user does the same. FS §20 T already lets a network member infer membership by reading a journey row, so this adds nothing the ruling does not already give. Still, the predicate should exist only inside policies: no EXECUTE for `mj_app` and no route. EXECUTE grants for `set_option()` and `clock_jump()` are likewise unstated (OQ-12 accepts this for the local prototype).

**N7. Two items are passed to the supervisor and not decided here.**

- Amendments §2.4 proposes a check: the loader connects only as `mj_app` and contains no direct INSERT, UPDATE, DELETE, COPY or TRUNCATE. It was not numbered, because it comes from no finding. It should be added when the supervisor accepts it.
- OQ-3 (R-119's "times after the map entry" against a same-instant write) is recorded on R-119 as open. The check is not softened.

**N8. Weakest point: highlights can be inferred after unlock.** Under DD, B24 and R-151, a reader who sees `captured_at` on many photos from one day (Lantern #1: 19 in 24 hours) can still infer a highlight. No ruling covers it. R-151 records it as a residual risk.

### Checked and clean

- FS §20 Q–W, Y–BB are applied consistently in the P1 amendments and in the DN B9 row:
  - P1:48 (c) and P1:84 give the owner's highlight view as a bare boolean.
  - P1:99 gives the capture order.
  - The P1 §3.7 derivation matches §3.3: 6 journeys, 23 public photos, and the slot 1 dates of the six fixed reflections fall inside their slots after each reveal finished.
  - The P1 §3.8 times are at 12:00.
- `highlight_open()` (Amendments:221–224) returns no time, count or id. It gives the same refusal to non-owners and to unknown ids, which keeps R-008's comparison against First Light intact.
- The Hands → First Light tag (P1:391, :394) puts First Light only on Hands' map and changes no baseline ring or matrix cell.
- B20–B26 add no counter, timer, reminder or leak.
- `joined_at` (P1:213) is a fixture value, and no screen shows it.

---

## Rubric changes

- **Added R-151:** after unlock, highlight facts reach the owner only (FS §20 DD, DN B24, B6).
- **Added R-152:** type, dates, chapter and feeling tags reach the owner and network only; never public (FS §20 T, CC).
- **Lines added to existing checks:**
  - `Decided` lines for FS §20 U (R-040, R-043), X (R-068, R-142), Z (R-141) and BB (R-119).
  - `Provisional default` lines for B20, B22, B23 (R-141), B21, B22 (R-117), B25 (R-040) and B26 (R-119).
  - OQ-3 recorded as open on R-119.
- **Corrections:** R-103's B9 (d) reading, and R-116's source (`FS:299` → `FS:321`). No check was removed or renumbered.
