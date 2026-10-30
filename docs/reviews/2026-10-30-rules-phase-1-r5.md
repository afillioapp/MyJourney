# Rules audit: Phase 1 docs, round 5 (changes since 5d95aa7)

Date: 2026-10-30. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-154 after this audit).

**Target:** `git diff 5d95aa7..HEAD -- docs` (commits 751b9a1, aa6953a, 45a79bb, c3a99c0). The diff covers:

- `Screen-Inventory.md`, fixed by ux
- `Phase-1-Amendments.md` and `Phase-1-Proposal.md`, fixed by lead-tech
- `Functional-Spec.md` §20 EE–HH, new user rulings
- `Rules-Rubric.md` G-13 and the R-151 implementation line
- `Status.md`

Previous audit: `docs/reviews/2026-10-30-rules-phase-1-r4.md` (FAIL: V1–V3, N1–N8).

**Context:** no code exists, and `graphify-out/` is absent, so no graph queries were run. FS §20 EE–HH (`Functional-Spec.md:309–312`) are dated user rulings recorded in c3a99c0, after the Amendments and Proposal fixes in 45a79bb.

**Verdict: FAIL.** There are 3 confirmed violations. All three are new rulings that the build docs do not carry:

- §20 EE: the viewer role can still move the clock.
- §20 HH: the overview is not held back under B2's option.
- §20 GG: non-owners receive the capture time.

r4's V1–V3 are resolved.

---

## Auto checks run

```
$ git diff --stat 5d95aa7..HEAD -- docs
 Functional-Spec.md 4, Phase-1-Amendments.md 92, Phase-1-Proposal.md 18, Rules-Rubric.md 4,
 Screen-Inventory.md 86, Status.md 2

$ git diff 5d95aa7..HEAD -- docs | grep '^+' | grep -inE "streak|badge|counter|progress|remind|notif|retake|comment|\blike\b|rank|countdown|ends in|unread|time left|timer|leaderboard|level"
  14 hits; every one is a refusal ("Must never show", "never: a comment, reply or like", "No countdown",
  "A timer, time left or countdown ... even though the clock now runs"), the word "like" as a comparison,
  or "row-level"/"Row-level security". No banned element added.

$ grep -nE "no default|[Ss]till open, no ID|not settled|Not picked" docs/Phase-1-Amendments.md
  55:  ... whether any acting viewer may call it in the running prototype is not settled (OQ-16).
  193: ... Who may EXECUTE `set_option()` is not settled (OQ-16).
  360: OQ-16 ... Not picked. ... **Settled 2026-10-30, FS §20 EE ...**
  (60, 357: C17, correctly still open)

$ grep -nE "captured_at|capture time|capture date|GG|§20 (EE|FF|GG|HH)" docs/Screen-Inventory.md docs/Phase-1-Amendments.md docs/Phase-1-Proposal.md
  §20 EE, FF, GG, HH: cited nowhere in Amendments or Proposal; GG only at Screen-Inventory.md:681 (OQ-45 status)
  Screen-Inventory.md:409  S-16 Reads "Photo (`captured_at` after unlock ...)" for network and public viewers
  Phase-1-Amendments.md:226 (iii) photo_read "returns the granted columns" (captured_at among them) to every reader
  Phase-1-Amendments.md:266 evidence: "SELECT id, captured_at FROM photo -> 2 rows" as any viewer

$ grep -nE "journey_overview\` \||^\| \`b2\`" docs/Phase-1-Amendments.md
  186: | `b2` | ... | RLS on photo, photo_visibility and reflection only. Not on journey, chapter or feeling-tag rows ...
  281: | `journey_overview` | (unchanged, P1:126) | Owner and network |

R-150 step 1 on Phase-1-Amendments.md (table IDs not labelled): B1–B19, C1–C16. None of these is touched by
the Amendments' questions except through P1, which carries them. No finding.

Citation checks: Amendments:216 `RR:97–103` = R-008 (RR:97–104), correct. Amendments:216 `RR:1185` for G-13:
G-13 is now RR:1219 (before this audit's additions), stale (N3 below).
```

---

## Status of r4 findings

| r4 item | Status | Evidence |
|---|---|---|
| V1: §20 T and CC not on reader screens | **Resolved** | `Screen-Inventory.md:42` (new "Journey facts after unlock"). S-06 `:187`, `:202–203`, `:206–208`; S-09 `:266`, `:277`, `:282`; S-16 `:392`, `:403–404`, `:407–409`; S-17 `:416`, `:430`, `:432` |
| V2: `highlight_id` "as readable as the photo itself" | **Resolved** | `Phase-1-Amendments.md:226` item 4 (column grant without `highlight_id`, `photo_highlight_id()`, `photo_read`), evidence `:252–266`. `Phase-1-Proposal.md:48` (e), `:92`. Screen bans at SI `:206`, `:277`, `:407`, `:430` |
| V3: B20–B26 called open or unlabelled | **Resolved** | Amendments `:23`, `:58`, `:81`, `:128`, `:143`, `:195`, `:228`. OQ table `:345–359`. P1 `:48`, `:133`, `:170`, `:195`, `:198`, `:201`. SI T-01 `:514–517`, T-02 `:550–553` |
| N1: §20 X not carried where B2's option is described | **Partly resolved** | Fixed in SI `:202` and Amendments `:186`, `:288`. Still open: DN B2 (`Decisions-Needed.md:21`) has no pointer to X or HH (DN was not in this diff) |
| N2: rubric R-103 | Closed in r4 | |
| N3: stale citations | **Resolved** for SI:639 (now OQ-30 at `:644`), Amendments R-008, and the Spec:299 and 290–291 references | New stale citation: see N3 below |
| N4: OQ-41 and OQ-42 had IDs | **Resolved** | SI `:670`, `:672` |
| N5: C17 open while the jump is built | **Still open** | Amendments `:60`, `:357`. SI `:516`, `:670`. EE now limits who can press the jump, but the jump still shows another user's unlock date to the demoer |
| N6: `viewer_in_network()` callable; EXECUTE grants unstated | **Settled by the user** in FS §20 FF (`:310`) and EE (`:309`). FF is now on R-070. EE is not carried in the Amendments body: see V1 |
| N7: loader check (Amendments §2.4); OQ-3 | **Unchanged.** The loader check was not adopted by the supervisor, so it is not numbered. OQ-3 is still open on R-119 (`RR:907`) |
| N8: highlight inferred from capture times | **Narrowed, not closed.** GG hides the time of day, but 19 Lantern #1 photos on one date still suggest a highlight. Kept as the R-151 residual |

---

## Findings

### Confirmed violations

**V1. FS §20 EE is not carried. As written, the viewer role can still jump the clock and flip switches.** Rubric: R-153 (new). Also R-141, R-014.

- **Where:**
  - `Phase-1-Amendments.md:55`: "The loader calls it as `mj_app` (§2.2), so `mj_app` holds EXECUTE on it today; whether any acting viewer may call it in the running prototype is not settled (OQ-16)."
  - `Phase-1-Amendments.md:193`: "Who may EXECUTE `set_option()` is not settled (OQ-16)."
  - `Phase-1-Amendments.md:121`: the loader runs "as `mj_app`" and calls `clock_jump` for every event.
  - Only the OQ table row `:360` records EE as settled.
- **What is wrong:** FS §20 EE (`Functional-Spec.md:309`) rules that `clock_jump()`, the jump to the next unlock and `set_option()` are "callable only by a separate panel role, never by the acting viewer". Every viewer runs as `mj_app` (`Phase-1-Amendments.md:226`: "every viewer runs as `mj_app`"). The body still gives that role EXECUTE on `clock_jump()` and calls the question open. A builder working from §1.3, §2.2 and §3 would grant the acting viewer the clock.
- **Why it breaks the rule:**
  - A decided ruling is contradicted in the build source (R-134).
  - A viewer who can move the clock can reach any sealed journey's unlock instant from inside a product screen. That turns the time control into a route round the seal (R-014, R-141).
  - No check covered who may call these functions, so R-153 is added.

**V2. FS §20 HH is not carried in the data layer. Under B2's option, the network reads the overview before the reveal is finished.** Rubric: R-142 and R-063 (both now carry a `Decided (FS §20 HH)` line).

- **Where:**
  - `Phase-1-Amendments.md:186`: the `b2` switch drives "RLS on photo, photo_visibility and reflection **only**". The overview is not on the list.
  - `Phase-1-Amendments.md:281`: `journey_overview`, unlocked: "Owner and network", with no B2 term.
  - `Phase-1-Proposal.md:126`: "Readable by the owner and the owner's network", unconditional.
  - Under B13 (`Decisions-Needed.md:32`) the slot 1 overview can be written during `reveal-open`, so the case does arise.
- **What is wrong:** FS §20 HH (`Functional-Spec.md:312`) rules that under "only after reveal finished" the network reads the overview only once the reveal is finished. The Amendments make B2 explicitly not govern the overview. That is the opposite.
- **Note:** `Screen-Inventory.md:373` (S-15) already holds the right behaviour as a "strictest reading", so the gap is in the data layer, which is where the rule must live (`CLAUDE.md`, "Enforce rules in code").
- **Same line, related:** the word "only" at `:186` also leaves notes and person tags outside `b2`. R-142's `Decided (FS §20 X)` line counts both as "what follows" a photo. Neither the Amendments nor P1 says whether their read policies inherit the photo's readability. Under C6's default, person tags are hidden from non-owners anyway (R-148). For notes, the photo policy may cover it, but no doc says so. This part is recorded as unverified, not as a separate violation.
- **Why it breaks the rule:** a decided ruling is contradicted in a build source (R-134). R-142 ("no one but the owner reads any of it") already covers it, so no new check is needed. `Decided` lines were added.

**V3. FS §20 GG is not carried. Every reader receives a photo's full capture time.** Rubric: R-154 (new). Also R-151's residual.

- **Where:**
  - `Phase-1-Amendments.md:226` (iii): the read view `photo_read` "returns the granted columns" to every reader, the owner included. Part (i) grants `captured_at` to every viewer, and the evidence at `:266` shows `SELECT id, captured_at FROM photo` succeeding for any viewer.
  - `Phase-1-Proposal.md:48` (e): "every reader reads photos through one read view". `:90`: `captured_at` is a full timestamp.
  - `Phase-1-Proposal.md:106`: the note's `written_at` has no reader rule. It is at most 15 minutes after `captured_at` (`:108`), so a reader of a note learns the capture time to the quarter hour.
  - `Screen-Inventory.md:409`: S-16 "Reads" gives network and public viewers `captured_at` with no date-only limit. `:395`: under B5's option the activity graph for a non-owner is built from `captured_at`, at no stated resolution.
  - `Screen-Inventory.md:681` records GG as decided, but no screen row (S-06, S-16, S-17) carries it.
- **What is wrong:** FS §20 GG (`Functional-Spec.md:311`) rules that "readers other than the owner see a photo's capture date, never its time". The data layer hands them the time.
- **Why it breaks the rule:**
  - A decided ruling is contradicted in the build sources (R-134).
  - Under the house rule that a restriction is unreadable, not merely hidden (`CLAUDE.md`, "Enforce rules in code"), a field the API returns counts as shown. The precedent is R-152: "on any screen or in any response".
  - No check covered capture-time resolution, so R-154 is added.
- **Note:** this is drift, not defiance. GG was recorded in c3a99c0, after the Amendments and Proposal fixes in 45a79bb. It still has to be carried before Phase 3.

### Notes (not violations)

**N1. A silent addition sits in the OQ-16 settlement.**

- `Phase-1-Amendments.md:360` says "the loader runs as that role for clock_jump". FS §20 EE (`:309`) says nothing about the loader.
- It is a reasonable consequence: O2 forbids a bypass role, and the loader must move the clock. But it changes §2.2 (`:121`, "The loader (as `mj_app`)") and P1 §3.1 ("replayed ... as the app role", `Phase-1-Proposal.md:195`).
- It should be written into the body as derived from EE, with the source cited, or confirmed by the supervisor. It must not live only in a table cell. No banned item rides on it.

**N2. FF is recorded, but the body still calls it open.** `Phase-1-Amendments.md:284`: "Whether that is acceptable under R-070 is OQ-17." The OQ row `:361` says it is settled by FS §20 FF. Nothing leaks, because FF accepts exactly what is built. R-070 now carries a `Decided (FS §20 FF)` line.

**N3. A stale citation.** `Phase-1-Amendments.md:216` cites G-13 as `RR:1185`. G-13 was at RR:1219 before this audit, and is lower still after it.

**N4. S-15 should cite HH.** `Screen-Inventory.md:373` describes the overview under B2's option as a "strictest reading". It is now decided (FS §20 HH) and should cite it. The behaviour is already correct.

**N5. The rubric's R-151 implementation line reads badly.** It now says "`P1:92` does not yet say how **Updated 2026-10-30:** now stated ..." (`Rules-Rubric.md:155`). This is the rubric's own wording. It is kept, not shortened (the rubric never shrinks), and is readable as a dated update.

**N6. Weakest points carried forward:**

- **C17** (r4 N5): the jump to the next unlock is still built with no default. After a jump, the panel shows another user's unlock date.
- **Highlight inference by date** (r4 N8, R-151 residual): GG narrows this but does not close it.
- **The activity graph's resolution under B5's option**: R-154 now requires no bucket finer than a day for non-owners. No doc states it yet.

### Checked and clean

- **Banned-term scan:** every hit is a refusal or a false positive.
- **The S-09 entry ban** (`Screen-Inventory.md:277`, `:282`): it implements CC (`:307`). The feed selects by tag inside the data layer and returns reflection text only.
- **The T-01 running clock** (`:516–517`): it adds a ban on any timer or time left for note or highlight windows (R-140). There is no countdown.
- **The T-02 one global row** (`:550–553`): it shows nothing beyond fixture users' names (R-014).
- **The `highlight_id` enforcement** (Amendments:226):
  - A non-owner gets the same NULL for a highlight photo, a normal photo and a missing id, so it is not an oracle.
  - The sealed owner case returns 0 rows.
  - Filtering or sorting on the column is refused.
  - This matches R-151's check.
- **The P1 amendments** (`:3`, `:48`, `:92`, `:133`, `:170`, `:195`, `:198`, `:201`): each is tagged and edited in place, and the line count is unchanged, so P1 citations do not move. No line redesigns §2 beyond the approved O3, O4 and DD.
- **The rubric G-13 change** (751b9a1): it keeps the original question struck through. Nothing was removed.

---

## Rubric changes

- **Added R-153:** only the panel moves time or flips switches; no acting viewer can (FS §20 EE). It comes from V1.
- **Added R-154:** non-owners learn a capture date, never its time, including through a note's written time or a graph finer than a day (FS §20 GG). It comes from V3.
- **`Decided` lines added:**
  - EE on R-141
  - FF on R-070
  - GG on R-151 (the residual is narrowed, not closed)
  - HH on R-063 and R-142
- **Updated:** the header note, and the banned-list coverage note (R-151 to R-154).
- **Nothing renumbered or removed.**
