---
name: phase
description: Run the My Journey build one step at a time. `/phase` or `/phase status` shows where the build stands; `/phase next` runs the next deliverable through its owner agent and the rules audit; `/phase gate <n>` checks whether phase n can close. Use whenever the user wants to move the build forward, see progress, or pass a gate.
---

# /phase: the supervisor loop

You are the supervisor. The workers are the agents in `.claude/agents/`. They report to you, never to each other. The shared state is the files in `docs/`, with `docs/Status.md` as the board.

Read `CLAUDE.md`, `docs/Build-Plan.md` and `docs/Status.md` before anything else.

## `/phase` or `/phase status`

Summarise `docs/Status.md` in a few lines: the current phase, what is done, the next step and its owner, and anything waiting on the user. Change nothing.

## `/phase next`

Run **one** deliverable, the first `todo` in the current phase whose inputs exist. Then stop.

1. **Check the inputs.** If the deliverable depends on a doc that does not exist, or on an open decision, stop and tell the user what is missing. Do not start a worker on a guess.
   - Never cite `docs/Overview.md`, or any file marked historical (L-001)
   - Name every environment assumption the deliverable makes: stack, database host, URL, access. If one is an open decision, state it in the brief as an assumption (L-004)
2. **Write the brief.** The worker never sees this conversation, so the brief must stand on its own:
   - The deliverable, and the target file path
   - The doc sections it must trace to
   - What is explicitly out of scope
   - The output that proves it is finished
   - "If something is not specified, stop and list it under Open questions. Do not guess."
3. **Dispatch** to the owner agent named in `docs/Status.md`. Set the row to `in progress`.
4. **Check the evidence, not the claim.** Open the files the worker lists. Confirm each piece of evidence yourself.
5. **Audit.** Run `/rules-audit` on what changed. Set the row to `in review`.
6. **Revise.** If the audit fails, send the findings back to the same worker with the original brief. **At most three rounds.** After the third, stop and bring the best attempt to the user, with the remaining findings flagged.
7. **Open questions go to the user,** never to another worker and never filled in by you. A deliverable with open questions stays `in review`.
8. **Record.** When the work is audited and clean, set the row to `done`, add the evidence path, and add a dated line to the Log. If the step recorded a decision, grep `docs/` for the old wording and every restatement of it. Fix or flag each hit before closing the step (L-002).
9. **Refresh and commit.** Run `/graphify . --update`, and edit nothing until it finishes. Then commit the step if the user has allowed commits; otherwise list the uncommitted files. Tell the user what was produced and what comes next (L-006).

Every brief also carries the learnings that apply. Include the "Read before you start" list from `docs/Learnings/index.md`, plus any learning whose labels match the deliverable.

When writing a brief, use `graphify query "<topic>"` to find every doc section that bears on the deliverable, and list those sections in the brief. The worker reads the sections themselves; the graph only finds them.

Independent deliverables in the same phase may run in parallel, for example art direction and microcopy once the flows exist. Never parallelise a deliverable with its own inputs.

## `/phase gate <n>`

1. Dispatch the **qa** agent (quality gate control) with a brief to check the gate for phase n. The supervisor does not grade its own workers' output.
2. qa checks every deliverable's evidence, runs the gate's test as written and writes `docs/reviews/<date>-gate-<n>.md`. A gate that cannot be checked as written is not passed on judgement.
3. For gates after Phase 2, a rules audit with zero violations is part of every gate.
4. Open the gate report and spot-check its evidence yourself.
5. Report PASS or FAIL with reasons. **Only the user passes a gate.** On their explicit yes, record it in `docs/Status.md` and move "Current phase" forward.
6. **Retrospective.** Dispatch the **learner** with the phase's log, review reports, audit findings and anything the user corrected. Apply its proposed enforcement changes to agent briefs, skills and the rubric. Bring any change to a product rule to the user.

## Learning outside gates

Also dispatch the **learner** whenever an audit fails, a deliverable hits its revision cap, or the user corrects the build. Do it straight away, not at the next gate.

## Outward-facing actions (L-005)

Before any deploy, publish, domain change or access-setting change:

1. Take the target's IDs from "Names and IDs" in `CLAUDE.md`, never by name match
2. Check who will be able to reach it: the protection settings, and whether the URL is ours
3. Name anything only the user can change, such as dashboard settings or permission-gated actions
4. Tell the user all of this **before** acting, and get their yes
5. If it skips the plan's order, say so, and log it as a user-approved exception in `docs/Status.md`
6. After acting, verify from outside: fetch the public URL as an anonymous visitor

## Hard stops: ask the user

- Any external ID not in the "Names and IDs" register (L-003)

- Any change to a locked rule, the banned list or the approved data model
- Anything in the "still undecided" or "Open decisions" lists
- Anything irreversible or outward-facing: deploying, pushing, deleting
- A worker or audit that hits the three-round cap
