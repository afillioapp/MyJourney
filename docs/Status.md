# My Journey — Build Status

The blackboard. Every worker reads this before starting and every finished step is recorded here with its evidence. The phases, deliverables and gates come from `Build-Plan.md`; this file only tracks where they stand.

Last updated: 2026-11-12

Status values: `todo` · `in progress` · `in review` · `done` · `blocked`

---

## Where we are

**Current phase:** 2 — Look, started at the user's request (2026-11-04). The Phase 1 gate has not been passed; see the Log.
**Next step:** the user passes the Phase 1 and Phase 2 gates. Everything open was decided by the user or, at the user's "anything open, you decide" (2026-11-10), set as labelled defaults (DN B70–B85, E10 parked). Audit `reviews/2026-11-10-rules-supervisor-carriage.md` FAIL (9) fixed by the supervisor; re-audit r2 to confirm. Then Phase 3 (needs Postgres).
**Waiting on you:** passing the Phase 1 and Phase 2 gates. Later, when you want: E2 (what close friends get), E10 (a position mark on a journey under way), AD-18 (on B41/B42). Every other open item runs on a labelled default (Decisions-Needed B70–B85). Parked: the system closing the app during the note window.

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
| Rules list as testable statements | rules-guardian | done | `Rules-Rubric.md`: R-001–R-173, every check has a how-to-check; all banned-list rows and §2.5 checks mapped (`docs/reviews/2026-10-30-gate-1.md`) |
| Screen inventory | ux | done | `Screen-Inventory.md`; rules audit PASS `docs/reviews/2026-10-30-rules-screen-inventory-r3.md` |

**Gate:** a developer can read the data model and the fixture design and know exactly what to build, with no questions left.

## Phase 2 — Look

| Deliverable | Owner | Status | Evidence |
|---|---|---|---|
| Art direction | art-director | done, pending the gate | `Art-Direction.md`. Audits r1 FAIL (12), r2 FAIL (5), r3 FAIL (2); round 3 of 3 fixed and checked by the supervisor, not re-audited. Waits on the user: AD-1 to AD-19, defaults B27 to B42 |
| Flows on paper | ux | done, pending the gate | `Flows.md`. Audits r1 FAIL (13), r2 FAIL (6), r3 FAIL (1: C2 label, `reviews/2026-11-05-rules-flows-r3.md`). Cap reached. Waits on the user: C2, FQ-1 to FQ-13, DC-1 to DC-14 |
| Microcopy for the weighted moments | copywriter | done, pending the gate | `Microcopy.md`. Audit r3 **PASS** (`reviews/2026-11-05-rules-art-microcopy-r3.md`). Waits on the user: MQ-1 to MQ-11 |

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

**Phase 2 triage (supervisor, 2026-11-10, at the user's request).** To close the Phase 2 gate in one or two sittings:

- **A. Needed for the gate** (they shape the ritual as a new reader meets it; no default, or the default is a product call): FQ-1 (which three taps); FQ-4 (how the reveal opens); FQ-2 with FQ-8 (lines and confirmations before set-once presses); FQ-12/MQ-1 with FQ-13/MQ-2 (whether the app states the 15-minute note window, the 24-hour highlight and its cap); FQ-5 (the "small deliberate act"); FQ-7 (an unwritten year in a reflection stack); MQ-8 (is the owner told what goes out at finish).
- **B. Stay on their default, decided by playing:** AD-1 to AD-18 (defaults B27–B42; AD-5 and AD-10's arrangement need none in the prototype), DC-1 to DC-7, DC-9 to DC-14, DC-16 (flows already follow §20 or a labelled default), MQ-4, MQ-6, MQ-7, MQ-10, E6 (B69). **No default yet, supervisor to propose labelled defaults for the user's one-go OK:** FQ-3, FQ-10 (unlock-instant edges, with parked SI OQ-51, OQ-52), FQ-6 (empty paths), FQ-9 (where a path opens).
- **C. Closed or housekeeping:** FQ-11 (JJJJ), AD-19 (IIII), DC-8 (NNNN), DC-15 (B61), MQ-5 (HHHH), MQ-9 (closed 2026-11-05); MQ-3 and MQ-11 are process (markers for the copywriter, ux), for the supervisor.

0. **Carry §20 KKKK (network by friend request) before Phase 3.** *Done on paper 2026-11-10: friend-screens audit V1 and V2 fixed (`542b705`); not re-audited.* Data model (`Phase-1-Amendments.md` §12) and fixtures (§13) done on paper, 2026-11-09; rules audit r2 fixed (`reviews/2026-11-09-rules-kkkk-r2.md`). Untested until Phase 3 (no Postgres here). **Still to do:** a ux pass on Flows and Screen-Inventory for the friend screens (the requests list, sending, removing, the close-friends list) and for "network" read as the map.

0c. **Carry §20 NNNN (no one can tell they are on someone's rings).** *Done on paper 2026-11-10 by the supervisor:* Phase-1-Amendments §14 (three switches left, tags owner-only, "path crossed" never named), Proposal:170, Spec §20 Z and :196, Flows, Screen-Inventory, Microcopy (M-18 one line, M-25 retired), Decisions B11/B12/C6, Rubric `Updated` lines, preview regenerated. Not audited by the rules-guardian; untested until Phase 3. **For the user:** Concept §16 "you see where you were in their journey" now rests on recognising yourself in a photo, with no mark.

0b. **Carry §20 MMMM (blocking).** *Done on paper 2026-11-10 by the supervisor:* Phase-1-Amendments §15 (two insert-only records, one block term in the readers; untested), Decisions B62–B69 (Instagram reference; B68 settles SI OQ-55 (b)), Screen-Inventory S-16 block, S-05 way in, new S-25 Blocked, Flow 10 parts F and G. No fixture change. **With the user: E6** (does a block touch the rings; built as B69, no). Lead-tech review and a rules audit still to run; copy markers for the copywriter.

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
- 2026-10-30 — Lead-tech carried §20 OO–RR: definer readers on all 14 user-content tables (264/264 rows identical to policies), baseline JPEG only, timing residual recorded. Open: Amendments OQ-25 (a–c), OQ-26.
- 2026-10-31 — User rulings §20 SS (reveal state: owner + network after unlock), TT (joined_at own row only), UU (own announcements as R2), VV (guard bug: strip again, save once).
- 2026-10-31 — Rules audit r6 FAIL and gate r5 FAIL: SS, TT, VV were only noted in the OQ table, not carried (supervisor shortcut). User rulings §20 WW–ZZ. Sent to lead-tech and ux.
- 2026-10-31 — Lead-tech carried SS–ZZ and B10 into readers and P1 lines with rule-oracle tests (48/48; planted faults caught). ux carried them to screens. Open for the user: AM OQ-27–29, SI OQ-47–49.
- 2026-10-31 — User rulings §20 AAA (press instant wins over VV), BBB (feed sort: reflection written time), CCC (public ring count only), DDD (double strip failure: press lost, logged, nothing shown). UU wording fixed.
- 2026-10-31 — Lead-tech carried §20 AAA–DDD (feed order reader, ring_count(), double-failure path with id-free log line), tested. B9 (e) marked decided. Open: AM OQ-30–32, SI OQ-50.
- 2026-10-31 — User rulings §20 EEE (date inference allowed), FFF (log gap accepted), GGG (lost press: camera returns, no note offer, no frame used), HHH (note step retries like capture). Carried into Amendments §6 and Screen-Inventory S-02 (HHH belongs to S-12; carried there 2026-10-31 by ux) by the supervisor.
- 2026-10-31 — Rules audit r7 FAIL (V1, V2: supervisor's EEE–HHH edits incomplete). User rulings §20 III (lost note ends the step), JJJ (lost press looks normal, note offer included; GGG's no-offer retired), KKK (public path order allowed). Fixes sent to lead-tech and ux.
- 2026-10-31 — Lead-tech carried EEE–KKK into Amendments/Proposal body with note-step tests (14:59 edge, JJJ discard). New: AM OQ-33 (how the note step knows its photo, Phase 3), OQ-34, OQ-5.
- 2026-10-31 — User rulings §20 LLL (note step uses a server-side handle), MMM (III route-only, accepted), NNN (note window 15 min after a lost press), OOO (joined_at = app_now() at join).
- 2026-10-31 — Lead-tech carried LLL–OOO (note handle via transaction-local setting, join_user() with app_now(), tests and planted faults). New: AM OQ-35 (handles lost on server restart).
- 2026-10-31 — User ruling §20 PPP (note handles lost on restart accepted for the prototype).
- 2026-10-31 — Rules audit r8 FAIL (S-12 not carrying LLL/PPP; stale lines; loader zero-jump). User rulings §20 QQQ (lost press looks like the normal press it would have been), RRR (note closed after restart looks like window ended). Sent to lead-tech and ux.
- 2026-10-31 — Lead-tech carried PPP–RRR and r8 N1 (loader only-if-ahead), N3, N4, N6 (Before real users list), tested. Open: AM OQ-36, OQ-37; SI OQ-24 residual, saved-page confirmation.
- 2026-10-31 — User rulings §20 SSS, TTT (OQ-36/37 accepted, Before real users 7–8), UUU (note window end: nothing changes on screen), VVV (no saved confirmation). Supervisor updated Amendments status lines and the list; S-12 sent to ux.
- 2026-10-31 — User rulings §20 WWW (skip ends the note step), XXX (C7 decided in full). Carried by the supervisor into Decisions-Needed, Screen-Inventory labels and OQ-24/49, Amendments/Proposal status ranges.
- 2026-10-31 — User rulings §20 YYY (note window ends at unlock), ZZZ (lost note answer identical to saved). Decisions-Needed C4 marked for WWW, YYY. Fixes for gate r8 and rules r9 sent to lead-tech and ux; the supervisor no longer edits their files.
- 2026-10-31 — Lead-tech carried WWW (skip request), YYY (window ends at unlock), ZZZ (same answer), N3 press timing; restored history row; tested. Open: AM OQ-38, OQ-39. S-12 skip already carried by ux.
- 2026-10-31 — User rulings §20 AAAA (retry timing gap accepted), BBBB (skip bypass accepted with OQ-12; refusal answers 'closed').
- 2026-10-31 — Lead-tech carried AAAA, BBBB (Before real users 9–10; one 'closed' answer tested).
- 2026-10-31 — Rules audit r10 FAIL (S-12 leave-capture send, AAAA/BBBB not on screens). User rulings: YYY reworded; §20 CCCC (at unlock: quiet end, app goes to 'ready'), DDDD (leaving capture = in-app navigation only). Sent to ux and lead-tech.
- 2026-10-31 — Lead-tech carried CF-46 (notes before unlock), r10 N3–N6, CCCC, DDDD; no behaviour change. Open: SI OQ-51, OQ-52; system closing the app; BBBB (b) timing as its own item.
- 2026-10-31 — ON HOLD at the user's request. All work committed and pushed. Not re-audited after the r10/r9 fixes. Four questions parked (above).
- 2026-10-31 — Quick clickable prototype built for the user's review (`prototype/index.html`, private artifact link). Browser-only, fixture data, not the Phase 4 build; not rules-audited. Work stays on hold until the user's review.
- 2026-11-04 — Hold lifted by the user, who asked for the next phase to be completed and then made live to preview. Exception to plan order, chosen by the user: Phase 2 starts with the Phase 1 gate not passed and the r10/r9 fixes not re-audited. Phase 1 gate stays open. Deploy preflight (L-005), read from Vercel: project and team IDs from the register; Vercel Authentication on for all except custom domains, no password protection, no custom domain, so every `.vercel.app` URL needs a team login; project is connected to GitHub (`afillioapp/MyJourney`), so a branch push makes a preview deployment. Only the user can switch the authentication off.
- 2026-11-04 — Phase 2 drafts written: `Flows.md` (ux), `Art-Direction.md` (art-director), `Microcopy.md` (copywriter). Rules audits: Flows r1 FAIL (13), fixed; r2 FAIL (6). Art direction FAIL (12) and microcopy FAIL (9), in one report. Rubric R-176 to R-178 added by the guardian. Preview page (`preview/`) part built by developer. All workers stopped at 22:30 on the account's 5-hour usage limit.
- 2026-11-05 — Resumed. Supervisor added R-179 to R-186 (guardian's P-1 to P-8). Fixes sent: Flows round 3 of 3, art direction and microcopy round 1. Cross-doc: "12 months from today" removed from Flows:156 and M-02 by the strictest reading (CL:24, C2); Microcopy Q-n renamed MQ-n (R-177). Learner not yet dispatched for the failed audits; batched to the end of the phase to save usage.
- 2026-11-05 — Flows round 3 of 3 done; re-audit r3 FAIL on one labelling violation (V1: the plain unlock date marked `PROVISIONAL: C2` though C2's other option is a countdown R-013 bars). Cap reached: to the user, not to another round. Microcopy round 1 fixes and two syncs with the final flows done.
- 2026-11-05 — Art direction round 1 fixed (new ring geometry, tier names removed, AD-11 to AD-18). Supervisor added provisional defaults B27 to B41 to `Decisions-Needed.md` from the art director's proposals (B28 marked as an invented rule) and linked them in `Art-Direction.md`. Art and microcopy re-audit r2 running.
- 2026-11-05 — Art and microcopy re-audit r2: both FAIL (art 5, copy 3; none leaks, shows a layer or ranks), all 21 r1 findings fixed (`reviews/2026-11-05-rules-art-microcopy-r2.md`); guardian added R-187. Three art findings traced to the supervisor's new rows: B41 revised (plain way to Reveal while open, does not answer C18), B28 revised (activity line kept under both B4 settings), B42 added (sealed-year and Commit ways per SI:170). Round 2 of 3 sent to art-director and copywriter. Preview page built (`preview/`, `python3 preview/build.py`); checkpoint commit a618960, not pushed.
- 2026-11-05 — Art and microcopy final audit r3 (`reviews/2026-11-05-rules-art-microcopy-r3.md`): **Microcopy PASS**. Art FAIL on 2 (ART-R3-1 medium: B28 left a gap under B4's option; ART-R3-2: a range missing B42). Run stopped on the 5-hour usage limit after writing the report.
- 2026-11-09 — Resumed. Supervisor revised B28 (flat graph stays under B4's option until the year's ring exists) and B31 (points to the exception). Art round 3 of 3 sent for the matching edits.
- 2026-11-09 — Art round 3 of 3 fixed (B28 carried, B42 range). Checked by the supervisor against ART-R3-1 and ART-R3-2; no further audit run, to save usage. All three Phase 2 deliverables are `in review`, waiting on the user's answers. Preview regenerated.
- 2026-11-09 — Pushed `2b2079e` to `claude/wizardly-planck-77eo2h`; Vercel preview `dpl_256FnLoD9w7WcQf2N6qsk7sE77W1` READY at `myjourney-dkv21qbhn-afillio.vercel.app/preview/`. Logged out it returns 302 to Vercel login, the same at the branch alias, so it is private. Production untouched. Not checked behind the login (that needs a share link).
- 2026-11-09 — Project moved from `~/Documents/Business/Retro-Gram` to `~/Projects/Retro-Gram` at the user's choice, out of Google Drive's backup of `~/Documents`. Git, graph root and Claude memory carried. Markdown files updated for the new location and current status: `CLAUDE.md`, `README.md`, `Learnings/index.md`, `Decisions-Needed.md`; B36 carried into `Screen-Inventory.md` S-16.
- 2026-11-09 — User rulings: §20 EEEE (unlock date always plain; clears Flows r3 V1), FFFF ("Your Journey is ready" once), GGGG (B28 timing kept), HHHH ("We want you here less, not more." on the website; R-130 met by the site). Carried by the supervisor into Flows, Microcopy, Art-Direction, Screen-Inventory, Rubric and Decisions-Needed (L-002). AD-18: user not sure, stays open under B41 and B42. B11 "no" and AD-19 "yes" need a follow-up; FQ-11 to be re-asked. Preview regenerated.
- 2026-11-09 — User rulings §20 IIII (newest ring thinnest and brightest; AD-19) and JJJJ (Start a highlight leads back to S-03; FQ-11), carried into Flows, Microcopy, Screen-Inventory and Art-Direction. The tone for IIII is still to be specified by art-director. User direction on B11: network by friend request, map by tags (Decisions-Needed E1), to be confirmed before the data model is touched.
- 2026-11-09 — User ruling §20 KKKK: the network is made by mutual friend requests (in-app only, no notification, count or suggestions); the map by tags only, anyone taggable by typed name; non-friends on the map see Public only; announcements go to friends; close friends are a chosen list (what they get is E2). Carried into Functional-Spec 146, 150, §20 H, Concept §372 and §864, Proposal D16 and CLAUDE.md. The data model amendment is queued (Open decisions 0). User rule for questions: product-specific questions go to the user; generic app behaviour takes Instagram as the reference within the banned list (CLAUDE.md rule zero step 5).
- 2026-11-09 — E2: user leans yes, close friends get something extra, what is undecided. The prototype keeps "nothing extra" until then.
- 2026-11-09 — Carrying §20 KKKK started (Open decisions 0). Supervisor added Instagram-reference provisional defaults B43 to B47 (send, answer, remove, no limit or count, close-friends list). Lead-tech dispatched for a Phase-1-Amendments section on paper: no Postgres on this Mac, so it is untested until Phase 3. Fixture-designer and the rules audit follow.
- 2026-11-09 — Lead-tech wrote `Phase-1-Amendments.md` §12 (KKKK on paper; untested, no Postgres). Its open questions: generic ones became Instagram-reference defaults B48 to B53 (B52 changes §12's request order, for lead-tech to carry); E3 (what still gives a map place away) and E4 (friend lists) go to the user; OQ-49 (rubric rows KKKK replaced) goes to the rules audit.
- 2026-11-09 — KKKK carriage: rules audit r1 FAIL (4) fixed: B43 way in, B48 event-time audience, B55, B56, E3 (c), E5, §20 H half reopened, P1 notes, lead-tech §11/§12 (K13, K14), fixture audiences at event time (13/9/5/2/0, matched three ways). Re-audit r2 FAIL on one low item (K8) plus a K14 gap, both fixed by lead-tech. Guardian added R-188 to R-197. Not re-audited after the last two-line fix.
- 2026-11-09 — ux pass for KKKK: Screen-Inventory S-22 (requests), S-23 (friends), S-24 (close friends), S-16 request element, S-05 way in; Flows Flow 10 Friends; "network as map" lines restated in both. Generic questions SI OQ-55 to OQ-57 settled by the supervisor as Instagram-reference defaults B57 to B61 (B61 strictest over Instagram's "follow back"). Rules audit next.
- 2026-11-09 — Friend screens rules audit (`reviews/2026-11-09-rules-friend-screens.md`): FAIL (2): V1, SI and Flows do not carry B57–B61; V2, Flows prototype row for Second Wind after 2026-11-14 drops her outgoing request to Long Way Round. B58, B59 tightened. Not yet fixed.
- 2026-11-10 — User rulings: E4 no (§20 LLLL, B56 decided); E5 yes, blocking (§20 MMMM, to carry: Open decisions 0b); E2 deferred, B55 stands. E3 explained to the user, answer awaited.
- 2026-11-10 — User ruling §20 NNNN (E3): no one can tell they are on someone else's rings. B11 unnamed, B12 and C6 hidden, all three no longer switches; B48 confirmed. To carry (Open decisions 0c).
- 2026-11-10 — Friend screens audit V1 (B57–B61 carried into SI and Flows) and V2 (Second Wind's request to Long Way Round) fixed by the supervisor (`542b705`). Not re-audited.
- 2026-11-10 — §20 NNNN carried on paper by the supervisor (Open decisions 0c). Rules-guardian re-audit still to run. Next: §20 MMMM, blocking (0b).
- 2026-11-10 — §20 MMMM (blocking) carried on paper by the supervisor (Open decisions 0b): Amendments §15, DN B62–B69 and E6, SI S-16 and S-25, Flow 10 parts F and G. Preview regenerated. Not audited; lead-tech review due before Phase 3.
- 2026-11-10 — Phase 2 triage pile A answered by the user: §20 OOOO (three taps), PPPP (photos first), QQQQ (one line per step; highlight grace), RRRR (feed to profile), SSSS (no gap), TTTT (finish line), UUUU (limits stated); then E7–E9 as §20 VVVV (reflections by capture anniversary), WWWW (dismiss a highlight within 3 hours, before any photo), XXXX (fixed circle). Carried by the supervisor into Spec, Proposal (fixture dates, 18 fixed reflections), Amendments §16, Flows, Screen-Inventory, Microcopy (draft lines for the copywriter), Art-Direction §7.x, Rubric, CLAUDE.md; defaults B70–B78; preview regenerated (`2822ab3`, `7ad6990`). Rules audit started.
- 2026-11-10 — Rules audit of the supervisor's carriage: FAIL (9: V1 sealed journey type/dates under B74; V2 reflection before unlock; V3 Reflect way as marker; V4 path-crossed subject; V5–V7 block and dismiss gaps; V8, V9 carriage). Fixed by the supervisor; re-audit r2 FAIL (6 partly fixed, 3 new: R2-1 to R2-3), then fixed again (r2 fixes, below); user rulings §20 YYYY (B72–B74), ZZZZ (block removes from blocker's rings); defaults B79–B85 (timelines, Reflect way, subject never receives, blocked side, repeat dismiss), E10 parked. Phase 2 deliverables marked done, pending the gate.
- 2026-11-10 — Re-audit r2 (`reviews/2026-11-10-rules-supervisor-carriage-r2.md`): FAIL; V1, V2, V5 fixed, V3, V4, V6–V9 partly, new R2-1 (owner's dates at the line's ends), R2-2 (a spark per photo counts a day), R2-3 (public timelines show unfinished reveals). All addressed by the supervisor: one identical spark per day, no timelines for public viewers, the owner's dates beside the words, B83 counts 8 / 6 / 4 / 2 / 0, `reflect_state()`, `dismiss_highlight` in the fixed set. Not re-audited a third time.
- 2026-11-10 — User direction for the visual identity: the dotted circle (one ring per journey, 52 weekly dots, bigger dot for a week with a photo, biggest for a highlight, oldest ring outermost). Logged in `Art-Direction.md` §0 with a reference image and a mock in `docs/visual-identity/`; questions AD-20 to AD-25 for the user. Not a §20 ruling yet; nothing built.
- 2026-11-12 — User confirmed the dotted circle: §20 AAAAA (one ring per journey, 52 weekly dots, three sizes, newest ring next to the name, older rings move out a step finer; replaces IIII's tree order and "newest thinnest", keeps "brightest"). Carried by the supervisor into Functional-Spec §14 and §20, Art-Direction §0, §2, §3.2, §3.3, §3.5, §3.6, §4, §8, §10, §11, §12, Decisions-Needed B27, B34 and new defaults B86 (weeks), B87 (highlight dot), B88 (sizes owner only), B89 (many rings), and CLAUDE.md. Then drawn in the preview (`39e7f96`; dots 1:2:3, each ring's dots halfway between the next ring's, 3 units clear of the frame) and the prototype (`1177709`; fixture highlights hold their photos), with tests: `python3 -m unittest discover -s preview` (18) and `node --test prototype/test_prototype.mjs` (10). Pushed at the user's "make the final changes live": preview deployment `dpl_9ksPBvN5N2qxkBmg1VWz5EdgH99h`, READY, private (302 to the Vercel login logged out); production untouched.
- 2026-11-12 — Rules audit `reviews/2026-11-12-rules-dotted-circle.md`: FAIL (7; no sealed-year leak, no counter). All seven checked and confirmed by the supervisor, then fixed: V1 `PROVISIONAL: B4`, `B89` labels in code; V2 the prototype's same-day photos ordered by a hashed key, not capture order (new test); V3 raised to the user as Decisions-Needed **E11** (rings by journey or by year), per-year readings marked not built; V4 §3.6 rows carry B80 and B31 as changed 2026-11-10; V5 AAAAA carried into Screen-Inventory S-05, S-16 and Flows, status lines; V6 the tone measure stated place by place, with the one rise from one ring to two recorded; V7 week 52 holds 8 to 10 days. Guardian added R-211 to R-213 and G-29. Residuals R1, R2 for the user. Not re-audited.
- 2026-11-12 — User ruling §20 BBBBB (E11): keep B4's "one ring per year with the app" option. Its dotted drawing set as default B90 (year rings follow B28; weeks from each journey's commit date; two journeys merge by the larger size; a year with no finished journey is 52 small dots; newest year next to the name). Carried into Art-Direction §3.2, Decisions-Needed, CLAUDE.md. Answers the guardian's G-29 for the rubric's owner. Not built: the prototype has no options panel.
