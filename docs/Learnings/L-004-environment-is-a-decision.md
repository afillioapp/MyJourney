# L-004: Where the app runs and where its data lives is a decision for the user, raised before anything is designed on top of it

| Date | Phase | Labels | Status |
|---|---|---|---|
| 2026-10-27 | 0 | process, data, deploy | open |

## What happened

- `Phase-1-Proposal.md:40` (§2.1), approved 2026-10-25, opens with "Postgres, local." Every rule mechanism in its table (lines 42–53) is a Postgres feature: grants, triggers, row-level security, an exclusion constraint, and a function that releases an encryption key
- The user had already created a Vercel project, `myjourney` (L-003). Nobody in the build knew about it, and no doc mentioned it
- The two assumptions met only on 2026-10-27, when the user asked for a deploy. The result is `Status.md:105`, Open decision 1: "Stack, and where the database runs ... Deploying there needs a hosted Postgres and a choice of web framework. Blocks Phase 3." `Status.md:54` marks the Phase 3 stack row `blocked`
- Phase 0 never raised it. The Phase 0 list (`Build-Plan.md:29–47`) is drawn only from product contradictions and mechanics in `Functional-Spec.md` §20. `Build-Plan.md` Phase 3 (lines 89–93) has no stack row; it was added later in `Status.md:54`. "What is deliberately not in this plan" (`Build-Plan.md:226–230`) rules out real auth, storage and mobile, but says nothing about hosting
- No damage yet. No code exists (`Phase-1-Proposal.md:3`: "No code written yet")

## Root cause

Phase 0 was scoped as "unblock the contradictions" (`Build-Plan.md:12`), which means product questions only. Questions about the environment had no slot in it, so the Phase 1 data-model proposal filled the gap with a default ("local") and stated it as a fact, not as an assumption to confirm. Approving the proposal then approved the assumption without anyone noticing it was one. Separately, the user's own setup work (creating a Vercel project) had no place to be recorded, so it could not be checked against the proposal. This is the same kind of failure rule zero exists to stop, a plausible default standing in for a decision, but applied to infrastructure rather than product behaviour.

## The rule going forward

Every proposal and brief lists its assumptions about the environment (where it runs, where the data lives, which accounts and services already exist) as named assumptions. The supervisor checks each one against `CLAUDE.md` "Names and IDs" (L-003) and asks the user about any that are not recorded decisions. Rubric checks describe behaviour, not the database feature that currently implements it.

## Where it is enforced

Not yet. Proposed:

1. **`.claude/agents/rules-guardian.md`**, under "What you own", add (before Phase 1 continues, because the Rules Rubric is the next deliverable):
   > Write each check as the behaviour it guarantees ("a reflection, once written, cannot be changed or removed"). Where `Phase-1-Proposal.md` §2.1 names a Postgres mechanism, record it under the check as the current implementation, not as the check itself. The stack and database host are still open (`Status.md`, Open decisions 1).
2. **`.claude/skills/phase/SKILL.md`**, step 2 "Write the brief", add a bullet:
   > - The environment it assumes (where it runs, where data lives, which external accounts or projects exist), each either a recorded decision or flagged to the user before dispatch
3. **`.claude/agents/lead-tech.md`** and **`.claude/agents/developer.md`**, "Read first", add (before Phase 3):
   > Before any schema or code: confirm `Status.md` Open decision 1 (stack and database host) is closed. "Postgres, local" in `Phase-1-Proposal.md` §2.1 is an assumption until then.
4. **`docs/Build-Plan.md`** Phase 3 table (lines 89–93), add the row "Stack decision: web framework, database host, deploy target | You" so the plan matches `Status.md:54` (before Phase 3).

## Related

- L-003: the Vercel project was invisible because no register existed
- L-005: the deploy that brought the conflict to light
- `Status.md` Open decisions 1; `Phase-1-Proposal.md` §2.1; `CLAUDE.md` "Rule zero"
