# Learnings

The project's learning space. It records mistakes, near-misses and what changed so they do not happen twice. The learner agent keeps it. Each learning is a page, `L-NNN-slug.md`, numbered in order. Pages are never renumbered and never deleted.

Last updated: 2026-10-27, after the Phase 0 retrospective, which covers Phase 0 and the setup on 2026-10-25 to 2026-10-27.

---

## Read before you start

Every brief carries this list. Each line is the rule; the page has the evidence.

1. **[L-001](L-001-stale-docs-must-say-so.md):** Build and audit only from the authoritative docs. `docs/Overview.md` is out of date (lines 63, 70, 125, 133, 210, 257–259 contradict the 2026-10-25 decisions). Never cite it.
2. **[L-002](L-002-decisions-propagate-everywhere.md):** When two docs disagree, do not pick. `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29 win. Cite both lines under Open questions. Known traps: the reflection example at `Functional-Spec.md:104–111` uses per-photo dates (wrong, see §20 D); "publish" names no real step; `My-Journey-Concept.md:807` says close friends "get everything" (wrong, see §20 H).
3. **[L-003](L-003-names-and-ids-register.md):** The product is My Journey, formerly Retrogram, in folder `Retro-Gram/myjourney`. "Phase n" means a build phase, never the business's printing stage. Take external IDs only from the register, never by name match.
4. **[L-004](L-004-environment-is-a-decision.md):** The stack and database host are undecided (`Status.md` Open decisions 1). Treat "Postgres, local" as an assumption. State every check as behaviour, not as a database feature.
5. **[L-006](L-006-history-and-graph-freshness.md):** The graph may be stale, so read the cited section itself. Edit nothing while a graph build runs.

Also carry, when the labels match:

- `deploy`, or anything outward-facing: [L-005](L-005-preflight-before-deploy.md), the deploy preflight
- `data` (lead-tech, developer, rules-guardian): L-004 in full

---

## All learnings

Newest first.

| ID | Title | Phase | Labels | Status | Where it is enforced |
|---|---|---|---|---|---|
| [L-006](L-006-history-and-graph-freshness.md) | Every change to the shared files is committed and reaches the graph, and nothing is edited while the graph is being built | 1 (setup) | tooling, process | open | Partly: a git repo exists since 2026-10-27 16:07. Proposed: `phase` SKILL step 9, `CLAUDE.md` graphify section |
| [L-005](L-005-preflight-before-deploy.md) | Before any deploy, check who will be able to reach it, at which URL, and what only the user can change, and tell the user before you start | 1 (setup) | deploy, process, tooling | open | Partly: the exception pattern is followed in `Status.md:111`. Proposed: new "Outward-facing actions" section in `phase` SKILL, `developer.md` |
| [L-004](L-004-environment-is-a-decision.md) | Where the app runs and where its data lives is a decision for the user, raised before anything is designed on top of it | 0 | process, data, deploy | open | Proposed: `rules-guardian.md`, `phase` SKILL step 2, `lead-tech.md`, `developer.md`, `Build-Plan.md` Phase 3 |
| [L-003](L-003-names-and-ids-register.md) | Every name the project goes by, and every external ID, is written down in one place, and searches use all of them | 1 (setup) | docs, deploy, tooling | open | Proposed: `CLAUDE.md` "Names and IDs", `phase` SKILL hard stops |
| [L-002](L-002-decisions-propagate-everywhere.md) | A decision is recorded only when every restatement, summary, count and cross-reference it touches matches it | 0 | docs, rules, process | open | Proposed: `CLAUDE.md` rule zero, `phase` SKILL step 8, `qa.md` gate control, listed doc fixes |
| [L-001](L-001-stale-docs-must-say-so.md) | A doc that is not kept current says so in its first lines, and no agent builds or audits from it | 0 | docs, briefs | open | Proposed: banner on `Overview.md`, `README.md:16`, `CLAUDE.md` "Which docs to trust", `phase` SKILL step 2 |

---

## Labels

The fixed set. Add a new label only when none fits, and add it here.

`docs` · `rules` · `data` · `time` · `fixtures` · `ux` · `copy` · `art` · `process` · `briefs` · `deploy` · `tooling` · `cost`

---

## Open questions for the user

Raised by the learnings above. Only the user can settle these.

1. **The upload vs sealed fork** (`My-Journey-Concept.md` §28, `Overview.md:257–259`). Can it be closed with this text? "*Closed 2026-10-25: sealing is automatic at capture (`Functional-Spec.md` §4), so there is no upload step. Other people's past years are read through their profile and Walking a path (§6, §15), as a deliberate act, never as a feed (§13).*" (L-002)
2. **"Published".** In `My-Journey-Concept.md:365–367, 424, 440` and `Functional-Spec.md:141`, does "published" mean "the reveal is finished"? If so, should the docs use only "reveal finished" or "journey launched"? (L-002)
3. **`My-Journey-Concept.md:714`** says streaks are banned by "section 4", which does not ban them. Point it at §7 (line 244) and `Functional-Spec.md` §18? (L-002)
4. **`docs/Overview.md`.** Mark it historical, update it to match, or move it out of `docs/`? Is the live doc it was exported from (line 3) still being edited, and if so, which copy wins? (L-001)
5. **Stack and database host.** Already open as `Status.md` Open decisions 1. It blocks Phase 3, not Phase 1. (L-004)
6. **Vercel Authentication** on project `myjourney`. Switch it off so the holding page is public, or keep the page private for now? This has to be done by hand in the Vercel dashboard. (L-005)
7. **Commits.** May the supervisor commit after each recorded step, as L-006 proposes? (L-006)
