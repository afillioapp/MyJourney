# L-006: Every change to the shared files is committed and reaches the graph, and nothing is edited while the graph is being built

| Date | Phase | Labels | Status |
|---|---|---|---|
| 2026-10-27 | 1 (setup) | tooling, process | open |

## What happened

**No version history until 2026-10-27 16:07.** From 2026-10-25 to the afternoon of 2026-10-27, the project folder was not a git repository. All the decision work went into the docs with nothing to diff and nothing to roll back to: Concept §29, Spec §20, the approved proposal, and the agent team. A repository now exists. `git log` shows two commits on 2026-10-27, `3ef0cbb` "Project docs and rules" at 16:07:20 and `c37a298` "Ignore graphify output" at 16:07:50. So the history starts after all of Phase 0. Consequences:

- The broken cross-reference at `My-Journey-Concept.md:714` (L-002) cannot be traced to the edit that broke it
- At the time of this retrospective, the working tree already has uncommitted work again. `git status` shows `.claude/skills/phase/SKILL.md` and `.gitignore` modified, and `.claude/agents/learner.md` untracked. No rule says when to commit
- A sibling folder `../_archive-2026-10-25` exists outside the project. It looks like a manual snapshot. Its contents were not checked, and it is not a substitute for history

**Edits during a graph read.** On 2026-10-27, a knowledge-graph extraction was running while the supervisor edited `docs/Status.md`. Afterwards the file was recorded as only partly read. The graph's files agree. `graphify-out/cost.json` records 20 files in the 19:50:39 UTC run, but `graphify-out/manifest.json` has 19 entries, and `docs/Status.md` is not one of them, even though `graph.json` holds nodes from it. Without a manifest entry, an incremental update has no record of what it saw.

**The graph is already stale.** Comparing `manifest.json` modification times with the files on disk: `CLAUDE.md` (15:51), `.claude/agents/rules-guardian.md` (15:51) and `.claude/skills/phase/SKILL.md` (17:28) all changed after the 15:50 build. The phase skill refreshes the graph only after a deliverable (`.claude/skills/phase/SKILL.md:33`), so supervisor edits made outside `/phase next` never reach it. Briefs are built from `graphify query` (`SKILL.md:37`), so a stale graph can leave a new rule out of a brief.

## Root cause

Tooling state was not part of the workflow. The `/phase` loop has steps to record (step 8) and refresh the graph (step 9) for deliverables, but none to commit, and nothing covers the supervisor's own edits between deliverables: setup, fixes, learnings. Nothing says the graph build must be left alone while it runs, or that edits wait until it finishes. A smaller drift: `CLAUDE.md` says "A committed graphify-out/graph.json is rewritten whole", but `c37a298` and `.gitignore` now keep `graphify-out/` out of git.

## The rule going forward

Every recorded step ends with a commit, and with a graph refresh if any doc changed, whether the step is a `/phase` deliverable or not. No file is edited while a graph build or update is running.

## Where it is enforced

Partly. A git repository now exists. Proposed:

1. **Now, before Phase 1 continues:** commit the current working tree, including `docs/Learnings/` (needs the user's go-ahead, see Open questions), then run `/graphify . --update` so `Status.md`, `CLAUDE.md`, `rules-guardian.md`, the phase skill and this space are all in the graph
2. **`.claude/skills/phase/SKILL.md`**, step 9, replace with:
   > 9. **Refresh and commit.** Run `/graphify . --update` and wait for it to finish. Edit nothing while it runs. Then commit the deliverable, `docs/Status.md` and any doc fixes together, with the message `Phase <n>: <deliverable>`. Then tell the user what was produced and what comes next.
3. **`.claude/skills/phase/SKILL.md`**, add under "Learning outside gates":
   > The same applies to any change the supervisor makes outside `/phase next`: setup, doc fixes, applied learnings. Refresh the graph, then commit.
4. **`CLAUDE.md`**, graphify section: delete the bullet beginning "A committed graphify-out/graph.json ..." or reword it to match `.gitignore`. As it stands it describes a setup that is no longer true

## Related

- L-002: history would have shown when the line-714 cross-reference broke
- L-001: a banner on Overview.md only reaches the graph after a refresh
- `.claude/skills/phase/SKILL.md` steps 8–9; `CLAUDE.md` "graphify"
