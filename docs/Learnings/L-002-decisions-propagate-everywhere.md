# L-002: A decision is recorded only when every restatement, summary, count and cross-reference it touches matches it

| Date | Phase | Labels | Status |
|---|---|---|---|
| 2026-10-27 | 0 | docs, rules, process | open |

## What happened

The maintained docs contradict themselves in places the 2026-10-25 decisions did not reach. Each item below was checked against the file on 2026-10-27.

**Summaries and lists that were not updated**

- `My-Journey-Concept.md:807`, in the §26 "Answered" summary: "close friends get everything". §29 (line 864) says they "see nothing beyond the rest of the network". The body of the same doc marks the old rule superseded at line 381, but the summary list has no marker
- `My-Journey-Concept.md:130`, §4 "Open points" item 3, still asks whether a highlight is capped. §29 (line 846) decided it: capped at the type's yearly quota. The neighbouring item 1 (line 128) is struck through as resolved, but item 3 is not

**A fork that the decisions settle but that is never closed**

- `My-Journey-Concept.md:826–832` (§28) says neither source document "says which version won", upload model or sealed model. `Overview.md:257–259` repeats it
- The maintained docs now settle the upload half. `Functional-Spec.md:58` says "Sealed automatically at capture. Never a later decision about inclusion". `My-Journey-Concept.md:868` and `Functional-Spec.md:279` (§20 I) say others may know only that a sealed journey exists
- The second half of the fork, browsing other people's past years, was not removed outright. It came back as a deliberate act through the profile and Walking a path (`Functional-Spec.md:76`, §15 lines 191–197), and never as a feed (`Functional-Spec.md:171`, "No photographs in the stream")
- The upload model's vocabulary survives. `Functional-Spec.md:141` says visibility is "chosen at publish time", and `My-Journey-Concept.md:365–367, 424, 440` speak of a journey being "published". No decided behaviour has a publish step. §20 F (line 276) places the visibility choice at reveal

**A worked example that contradicts the decision beside it**

- `Functional-Spec.md:99` says a new reflection is added "on the next anniversary". The example at lines 104–111 dates reflections from each photo's own capture date (7 Jan 2019 → 7 Jan 2020 → 7 Jan 2021). Line 101 of the same section, and §20 D (line 274), say all photos of a journey move to their next slot together, on the journey's unlock anniversary. This is in the declared source of truth, which the Rules Rubric and Screen Inventory are about to be written from

**A cross-reference that points at the wrong section**

- `My-Journey-Concept.md:714`: "streak mechanics are banned by section 4's rules". Section 4 (lines 95–133) covers journey types, highlights and Commit. It says nothing about streaks or engagement mechanics. The nearest rule in that doc is §7, line 244: "No engagement mechanics, no feed, no notification loops designed to pull people back". The explicit ban is in `Functional-Spec.md:233` ("No streaks") and `CLAUDE.md:32`. §4 was rewritten on 2026-10-25 (its heading at line 95 reads "REVISED 2026-10-25"), so its contents may once have differed. Without version history (L-006) there is no way to check

**Counts and summaries that do not match their own lists**

- `Build-Plan.md:3` says "Six phases", and `README.md:14` says "Six phases with gates". The diagram at `Build-Plan.md:12–18` lists seven, Phase 0 to Phase 6. The user asked how many phases there are and got a wrong number from the doc
- When Phase 5 may start is given three ways: "can run parallel from Phase 3" (`Build-Plan.md:17`), "Can start any time after Phase 2" (`Build-Plan.md:121`), and "Can start once Phase 2 has passed" (`Status.md:80`)
- `README.md:20` still says "Pre-build"

## Root cause

Recording a decision was treated as a single write to two decision logs (Concept §29 and Spec §20). Nothing required a search for every other place that restates the old behaviour, its vocabulary, a count, or a section number. The supersession markers in Concept's body show this was done by hand and incompletely: body sections were marked, but summary lists (§26), open-point lists (§4) and the fork (§28) were not. No gate, audit or brief checks that the docs agree with each other. The Phase 0 gate (`Build-Plan.md:51`) checks only that answers exist in writing.

## The rule going forward

When a decision is recorded, search every doc for the old wording and its key terms, and fix or mark each hit, in the same change. A gate cannot pass while two maintained docs disagree on a decided behaviour, or while a count or "see section N" does not match its target.

## Where it is enforced

Not yet. Proposed:

1. **`CLAUDE.md`**, under "Rule zero", add (before Phase 1 continues):
   > When two docs disagree, do not pick. The dated decisions in `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29 win over everything else. Cite both lines in your report under Open questions.
2. **`.claude/skills/phase/SKILL.md`**, step 8 "Record", add:
   > If the step recorded a decision, grep `docs/` for the old wording and key terms. Fix or mark each hit "Superseded YYYY-MM-DD, see §…", and list the hits in the Log line.
3. **`.claude/agents/qa.md`**, Gate control, add a step after step 3:
   > Check consistency. For each decision dated in this phase, grep the maintained docs for its key terms and confirm each hit agrees. Confirm that every count ("six phases") matches its list and every "see section N" points at a section that says it. Any mismatch fails the gate.
4. **Doc fixes for the supervisor to apply.** These restate decisions already made and need no new product input:
   - `My-Journey-Concept.md:807`: append "*(Superseded 2026-10-25: close friends see nothing extra. See §29.)*"
   - `My-Journey-Concept.md:130`: mark resolved, as line 128 is: "**Resolved 2026-10-25: capped at the type's yearly quota, 24 hours, user-started. See §29.**"
   - `Functional-Spec.md:99`: "on the next anniversary" becomes "on the journey's next unlock anniversary (§20 D)". Replace the example at lines 104–111 with one keyed to the journey's unlock date U: first reflection slot U to U+1 year, second slot U+1 to U+2, and so on. Do not keep per-photo dates
   - `Functional-Spec.md:141`: "chosen at publish time, not at capture" becomes "chosen at reveal, not at capture (§20 F)"
   - `Build-Plan.md:3` and `README.md:14`: "Six phases" becomes "Seven phases, 0 to 6"
   - `Build-Plan.md:17`: change "(can run parallel from Phase 3)" to "(can start once Phase 2 has passed)" to match line 121 and `Status.md:80`
5. **For the user, then the supervisor:** the §28 fork closing text and the line-714 cross-reference (see Open questions on `index.md`)

Items 1 and 4 come before Phase 1 continues. Rules-guardian and ux both read `Functional-Spec.md` next, and the §8 example would otherwise be turned into rubric checks or screen states.

## Related

- L-001: the same failure for a whole file
- L-006: without history, nobody can tell when a cross-reference broke
- `Build-Plan.md` §9 "Every finding becomes a permanent check"
