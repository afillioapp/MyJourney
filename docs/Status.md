# My Journey — Build Status

The blackboard. Every worker reads this before starting and every finished step is recorded here with its evidence. The phases, deliverables and gates come from `Build-Plan.md`; this file only tracks where they stand.

Last updated: 2026-10-30

Status values: `todo` · `in progress` · `in review` · `done` · `blocked`

---

## Where we are

**Current phase:** 1 — Define (all deliverables done; gate re-check pending)
**Next step:** Phase 1 gate re-check (qa), then you pass or hold the gate
**Waiting on you:** passing the Phase 1 gate; C17, C18 (not blocking)

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
| Rules list as testable statements | rules-guardian | done | `Rules-Rubric.md`: R-001–R-154, every check has a how-to-check; all banned-list rows and §2.5 checks mapped (`docs/reviews/2026-10-30-gate-1.md`) |
| Screen inventory | ux | done | `Screen-Inventory.md`; rules audit PASS `docs/reviews/2026-10-30-rules-screen-inventory-r3.md` |

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
| Stack decision | You | done | Local Postgres first, in the cloud session (`Phase-1-Proposal.md` §2.1). Deploy choice later. User, 2026-10-30 |
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

1. **Where the app deploys.** Phase 3 builds on local Postgres (decided 2026-10-30). A hosted Postgres and web framework for the Vercel project (`myjourney`) are still to choose. Does not block Phase 3.

## Log

- 2026-10-25 — Phase 0 gate passed. Phase 1 data model and fixtures approved.
- 2026-10-27 — Agent team and `/phase` workflow set up.
- 2026-10-27 — Holding page (`site/index.html`) deployed to Vercel production at `myjourney-afillio.vercel.app`, at the user's request. It uses only lines already approved in `CLAUDE.md` and the README: no form, no tracking. It is a placeholder, not the Phase 5 site. Public access is pending a change to Vercel Authentication.
- 2026-10-27 — Learner agent added. Phase 0 retrospective written (L-001 to L-006). The supervisor applied the process fixes to `CLAUDE.md`, the `phase` skill, rules-guardian, qa and developer. Product-doc fixes and commits are waiting on the user.
- 2026-10-27 — Phase 1 started: Rules Rubric and Screen Inventory dispatched.
- 2026-10-30 — Screen Inventory re-audit after round 1: FAIL, 3 confirmed (N1–N3), R-150 added. Round 2 fixed N1, N4, N11. N2, N3 (G-8), N7 and N8 wait for the user. Not yet re-audited.
- 2026-10-30 — Re-audit after round 2: FAIL on N2 and N3 only (both wait for the user). Follow-up fixed N12, N13, N14.
- 2026-10-30 — User rulings: G-8 text only (Spec §20 Q), Public waits under B2's option (§20 R), B6 over B19 (§20 S), stack local Postgres. Restatements fixed in Decisions-Needed, Screen-Inventory, Rules-Rubric.
- 2026-10-30 — Screen Inventory round 3 audit: PASS (0 violations). Leftovers N16–N18, N20 fixed; N5 and N8 raised as C18 and C17.
- 2026-10-30 — Phase 1 gate check (qa): FAIL. 4 questions for the user (U1–U4), 6 for owner agents (O1–O6), fixture inconsistency CF-1. Stale stack lines fixed (CF-2–CF-4). `docs/reviews/2026-10-30-gate-1.md`.
- 2026-10-30 — User rulings on gate-1 U1–U4 recorded as Spec §20 T–W.
- 2026-10-30 — Amendments: O3 approved (Spec §20 Z); OQ-10 → §20 X; chapter filter dropped (§20 Y); small items B20–B26 provisional. O4 and fixture O6 waiting on the user.
- 2026-10-30 — Fixtures: D14 'no journey' case moved to a scripted Hands → First Light tag (2027-06-20); pre-join captures allowed; generator leaves the six feed photos alone. Restatements fixed in Rubric R-075 area and Screen-Inventory.
- 2026-10-30 — User approved O4 (Spec §20 AA) and ruled O6 (Wind #6). Gate re-check r2: FAIL on scripted-action time; user ruled 12:00 UTC (§20 BB), feed may select by tag but never shows it (§20 CC), `highlight_id` owner only (§20 DD). Restatements CF-6–CF-9, CF-11–CF-13 fixed.
- 2026-10-30 — Rules audit r4 (FAIL: V1–V3) and gate r3 (FAIL: B-2) fixed by ux (Screen-Inventory) and lead-tech (Amendments, Proposal): §20 T/CC/DD carried to screens; `highlight_id` owner-only via column grant + view + function, tested on Postgres 16. Open for the user: Amendments OQ-16, OQ-17; Inventory OQ-43–45.
- 2026-10-30 — User rulings §20 EE (panel role), FF (viewer_in_network callable), GG (readers see capture date only), HH (overview waits under B2 option).
- 2026-10-30 — Lead-tech carried §20 EE (panel role mj_panel), GG (capture date only, via grants + views + functions), HH (overview under b2) and NB-10 (token scan) into Amendments and Proposal; tested on Postgres 16. ux carried EE/GG/HH to screens. Open: Inventory OQ-46 / Amendments OQ-18 (same-day order), OQ-19 (image metadata), loader-as-panel proposal.
- 2026-10-30 — User rulings §20 II (loader as panel role, approved), JJ (no time order same-day; ids not sequential), KK (strip image metadata at capture), LL (note time never to non-owners).
- 2026-10-30 — Lead-tech carried §20 II–LL: random uuid ids, fixed non-time order, metadata stripped at capture, highlight RLS/definer arrangement; tested on Postgres 16. New: Amendments OQ-20 (database statistics show sealed activity) for the user.
- 2026-10-30 — User rulings §20 MM (close database statistics leak fully), NN (database refuses images with metadata).
- 2026-10-30 — Lead-tech carried §20 MM (definer readers, catalog closures, one-database connect) and NN (metadata guard in capture()), tested on Postgres 16. Open for the user: Amendments OQ-21–OQ-24.
- 2026-10-30 — User rulings §20 OO (definer readers for all content tables), PP (refusal never reaches the user; no retake), QQ (baseline JPEG), RR (timing residual accepted for now).
- 2026-10-30 — Lead-tech carried §20 OO–RR: definer readers on all 15 user-content tables (264/264 rows identical to policies), baseline JPEG only, timing residual recorded. Open: Amendments OQ-25 (a–c), OQ-26.
