# L-005: Before any deploy, check who will be able to reach it, at which URL, and what only the user can change, and tell the user before you start

| Date | Phase | Labels | Status |
|---|---|---|---|
| 2026-10-27 | 1 (setup) | deploy, process, tooling | open |

## What happened

On 2026-10-27 the user asked for a holding page on Vercel. `site/index.html` was built from approved lines only and deployed to production (`Status.md:111`). The content was fine. Three things about the deploy were not checked before it happened:

1. **The page is not public.** The project has Vercel Authentication switched on, which blocks public access to its `.vercel.app` URLs. `Status.md:111` records "Public access is pending a change to Vercel Authentication"
2. **The obvious URL is someone else's.** `myjourney.vercel.app` belongs to a different account and serves another site. The project's real production URL is `myjourney-afillio.vercel.app`. If anyone had shared the obvious URL, people would have landed on a stranger's site under this product's name
3. **The fix needs the user's hands.** The supervisor tried to relax the protection, and Claude Code's permission check blocked it. That was the right outcome: loosening access to an outward-facing system is the user's call. But it meant the user learned after the deploy that the page was not public, and that they had to change a setting by hand

**What went right.** The page went live before Phase 5, out of plan order. The user chose this explicitly after being told it skips the plan's order. The Log records it as a placeholder, "not the Phase 5 site" (`Status.md:111`), and the Phase 5 rows stay `todo` (`Status.md:84–86`). This is the right way to handle an exception, and it is worth keeping as the pattern.

## Root cause

The deploy happened outside `/phase`, so none of its steps ran: no brief, and no "check the evidence, not the claim" (`.claude/skills/phase/SKILL.md:28`). The only deploy rule is a hard stop, "Anything irreversible or outward-facing: deploying ... ask the user" (`SKILL.md:58`). That rule makes sure the user approves an action. It does not make sure anyone has checked what the action will produce. So the user approved a deploy whose result, a private page at a non-obvious URL, nobody had predicted. No step lists the settings that only the user can change.

## The rule going forward

No deploy without a preflight, reported to the user before the deploy. The preflight covers: project and team IDs taken from `CLAUDE.md` Names and IDs; protection settings read; the URL that will serve it, and who owns that hostname; whether the public can reach it; and each step only the user can do. After the deploy, fetch the URL logged out and log the result.

An exception to the plan's order is allowed only when the user chooses it after being told which order it skips. It is logged as an exception and never marks a deliverable done.

## Where it is enforced

Partly. The exception pattern is already followed in `Status.md:111`, but no skill writes it down. Proposed:

1. **`.claude/skills/phase/SKILL.md`**, new section before "Hard stops" (before the next deploy; it does not block Phase 1):
   ```
   ## Outward-facing actions (deploys, domains, access settings)

   These apply inside and outside `/phase next`.

   1. Take the team and project IDs from `CLAUDE.md` Names and IDs. Never pick a project by name match alone
   2. Read the project's protection settings (Vercel Authentication, password protection) and say whether the result will be public
   3. List the domains and aliases that will serve it. Name the exact URL the public will use. Never assume `<project>.vercel.app` is ours
   4. List every step only the user can do: dashboard settings, anything the permission check blocks
   5. Put 1–4 in front of the user and get a yes. Then deploy
   6. Afterwards, fetch the public URL logged out and record the status code and the URL in the Status.md Log

   A step out of plan order needs the user's explicit choice after you have told them which order it skips. Log it as an exception. It never marks a deliverable `done`.
   ```
2. **`.claude/agents/developer.md`**, "What you do not do", add: "No deploy, domain or access-setting change. You build. The supervisor deploys through the outward-facing checklist in `/phase`."

## Related

- L-003: the IDs and the "not ours" URL belong in the register
- L-004: this deploy exposed the hosting conflict
- `Status.md:111`; `.claude/skills/phase/SKILL.md` "Hard stops"; `Build-Plan.md` §7 "Human gates on anything irreversible"
