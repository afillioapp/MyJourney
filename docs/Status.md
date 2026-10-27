# My Journey — Build Status

The blackboard. Every worker reads this before starting and every finished step is recorded here with its evidence. The phases, deliverables and gates come from `Build-Plan.md`; this file only tracks where they stand.

Last updated: 2026-10-27

Status values: `todo` · `in progress` · `in review` · `done` · `blocked`

---

## Where we are

**Current phase:** 1 — Define (two deliverables left)
**Next step:** Rules Rubric (rules-guardian) and Screen Inventory (ux), running in parallel
**Waiting on you:** the stack decision below, before Phase 3 can start

---

## Phase 0 — Decide

| Deliverable | Owner | Status | Evidence |
|---|---|---|---|
| Blocking and schema decisions | You | done | `My-Journey-Concept.md` §29, `Functional-Spec.md` §20 |
| Export and data ownership | You | todo | Can wait. Not needed before Phase 6 |
| Age gating | You | todo | Can wait. Not needed before Phase 6 |

**Gate:** passed 2026-10-25.
**Retrospective:** done 2026-10-27. Six learnings, L-001 to L-006, in `Learnings/index.md`.

## Phase 1 — Define

| Deliverable | Owner | Status | Evidence |
|---|---|---|---|
| Data model | lead-tech | done | `Phase-1-Proposal.md` §2, approved 2026-10-25 |
| Fixture design | fixture-designer | done | `Phase-1-Proposal.md` §3, approved 2026-10-25 |
| Rules list as testable statements | rules-guardian | in progress | Target: `Rules-Rubric.md`. Starts from `Phase-1-Proposal.md` §2.5 (11 data-layer checks); the banned list's screen-level rules are not yet written as checks |
| Screen inventory | ux | in progress | Target: `Screen-Inventory.md` |

**Gate:** a developer can read the data model and the fixture design and know exactly what to build, with no questions left.

## Phase 2 — Look

| Deliverable | Owner | Status | Evidence |
|---|---|---|---|
| Art direction | art-director | todo | Target: `Art-Direction.md` |
| Flows on paper | ux | todo | Target: `Flows.md` |
| Microcopy for the weighted moments | copywriter | todo | Target: `Microcopy.md` |

**Gate:** someone who has never heard of the product can follow the flows and understand the ritual.

## Phase 3 — Foundation

| Deliverable | Owner | Status | Evidence |
|---|---|---|---|
| Stack decision | You | blocked | See "Open decisions" |
| Schema, append-only where required | developer | todo | |
| Time control | lead-tech | todo | |
| Fixture data loaded | fixture-designer + developer | todo | |
| The 11 schema checks run as tests | lead-tech | todo | |

**Gate:** the fake data can be queried at any point in simulated time and gives a sensible answer. Reveal works. Layers recompute. Paths cross.

## Phase 4 — Build the app

| Screen | Status | Evidence |
|---|---|---|
| 1. Commit | todo | |
| 2. Capture | todo | |
| 3. The sealed year | todo | |
| 4. Reveal | todo | |
| 5. Profile | todo | |
| 6. Walking a path | todo | |
| 7. Layers | todo | |
| 8. Feed | todo | |
| 9. Positivity Feed | todo | |

**Gate after each screen:** it works against fixture data at several points in simulated time, and a rules audit on it returns zero findings.

## Phase 5 — Build the site

Can start any time after Phase 2.

| Deliverable | Owner | Status | Evidence |
|---|---|---|---|
| Site content | copywriter | todo | |
| Content organisation and tone check | content-manager | todo | |
| Build | developer | todo | |

**Gate:** the four non-negotiable statements appear above the fold or close to it.

## Phase 6 — Review

| Pass | Owner | Status | Evidence |
|---|---|---|---|
| Rules audit | rules-guardian | todo | |
| Functional QA | qa | todo | |
| Content QC | content-manager | todo | |
| Art review | art-director | todo | |

**Gate:** a rules audit with zero findings.

---

## Open decisions

1. **Stack, and where the database runs.** `Phase-1-Proposal.md` §2.1 says Postgres, local. A Vercel project (`myjourney`) also exists. Deploying there needs a hosted Postgres and a choice of web framework. Blocks Phase 3.

## Log

- 2026-10-25 — Phase 0 gate passed. Phase 1 data model and fixtures approved.
- 2026-10-27 — Agent team and `/phase` workflow set up.
- 2026-10-27 — Holding page (`site/index.html`) deployed to Vercel production at `myjourney-afillio.vercel.app`, at the user's request. It uses only lines already approved in `CLAUDE.md` and the README: no form, no tracking. It is a placeholder, not the Phase 5 site. Public access is pending a change to Vercel Authentication.
- 2026-10-27 — Learner agent added. Phase 0 retrospective written (L-001 to L-006). The supervisor applied the process fixes to `CLAUDE.md`, the `phase` skill, rules-guardian, qa and developer. Product-doc fixes and commits are waiting on the user.
- 2026-10-27 — Phase 1 started: Rules Rubric and Screen Inventory dispatched.
