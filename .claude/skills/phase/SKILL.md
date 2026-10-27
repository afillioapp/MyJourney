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
8. **Record.** When the work is audited and clean, set the row to `done`, add the evidence path, and add a dated line to the Log.
9. **Refresh the graph.** Run `/graphify . --update` so the new deliverable joins the knowledge graph. Then tell the user what was produced and what comes next.

When writing a brief, use `graphify query "<topic>"` to find every doc section that bears on the deliverable, and list those sections in the brief. The worker reads the sections themselves; the graph only finds them.

Independent deliverables in the same phase may run in parallel, for example art direction and microcopy once the flows exist. Never parallelise a deliverable with its own inputs.

## `/phase gate <n>`

1. Dispatch the **qa** agent (quality gate control) with a brief to check the gate for phase n. The supervisor does not grade its own workers' output.
2. qa checks every deliverable's evidence, runs the gate's test as written and writes `docs/reviews/<date>-gate-<n>.md`. A gate that cannot be checked as written is not passed on judgement.
3. For gates after Phase 2, a rules audit with zero violations is part of every gate.
4. Open the gate report and spot-check its evidence yourself.
5. Report PASS or FAIL with reasons. **Only the user passes a gate.** On their explicit yes, record it in `docs/Status.md` and move "Current phase" forward.

## Hard stops: ask the user

- Any change to a locked rule, the banned list or the approved data model
- Anything in the "still undecided" or "Open decisions" lists
- Anything irreversible or outward-facing: deploying, pushing, deleting
- A worker or audit that hits the three-round cap
