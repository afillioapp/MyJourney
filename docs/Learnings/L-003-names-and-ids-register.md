# L-003: Every name the project goes by, and every external ID, is written down in one place, and searches use all of them

| Date | Phase | Labels | Status |
|---|---|---|---|
| 2026-10-27 | 1 (setup) | docs, deploy, tooling | open |

## What happened

- The product has had three names. `My-Journey-Concept.md:721` gives the original name, "Retrogram ... Set aside". Line 720 says the working name, "My Journey", is "Not final". The workspace folder is still `Retro-Gram`, the project folder is `myjourney`, and the Vercel project is `myjourney`
- On 2026-10-27 the user said "I already created a vercel for it". A search for "retro" found nothing. The project was found only by matching the folder name
- No doc records the Vercel identifiers. `Status.md:105` and `Status.md:111` give the project name and production URL, but not its ID, team or team slug. They are:
  - Team: `afillio` (`team_eD0tvc1w4vZhmrNBOUb5F8Q0`)
  - Project: `myjourney` (`prj_5Cw4kvcC5aCVNQJPlf1irWVJb2b8`)
  - Production URL: `myjourney-afillio.vercel.app`
  - **Not ours:** `myjourney.vercel.app` belongs to a different account and serves someone else's site (see L-005)
- "Phase 2" means two things. In the build it is Look (`Build-Plan.md:14`). In the business it is the physical album and printing: `Functional-Spec.md` §17 "Album and print — phase 2", `Functional-Spec.md:89` "(phase 2)", `Overview.md:171`, and `My-Journey-Concept.md:818`. `Build-Plan.md:228` has to say "phase 2 of the business, not of this build" to tell them apart

## Root cause

The rename happened in the docs (`My-Journey-Concept.md` §22) but not in the folder, and the user created external resources outside the docs. No file lists the project's names, aliases and external IDs, so every search for an external resource has to guess which name was used. The Vercel tools need exact team and project IDs, and the only way to get them was to list everything and match by eye. The "phase 2" clash has the same cause: a term was reused, and no glossary says which meaning wins.

## The rule going forward

`CLAUDE.md` holds a "Names and IDs" section. Any search for an external resource tries every name listed there, and any new account, project, domain or ID is added to it the same day it is created or found.

## Where it is enforced

Not yet. Proposed:

1. **`CLAUDE.md`**, new section after "What this is" (before Phase 1 continues):
   ```
   ## Names and IDs

   | Thing | Name | ID / URL |
   |---|---|---|
   | Product (working name, not final) | My Journey | Formerly "Retrogram" (Concept §22) |
   | Workspace folder | Retro-Gram | Old name, not renamed |
   | Project folder | myjourney | |
   | Vercel team | afillio | team_eD0tvc1w4vZhmrNBOUb5F8Q0 |
   | Vercel project | myjourney | prj_5Cw4kvcC5aCVNQJPlf1irWVJb2b8 |
   | Production URL | | https://myjourney-afillio.vercel.app |
   | NOT ours | | myjourney.vercel.app belongs to another account. Never link to it |

   When looking for an external resource, search every name above (my journey, myjourney, retrogram, retro-gram, afillio). Add any new account, project, domain or ID here the day it appears.

   "Phase n" always means a build phase in `Build-Plan.md`. The business's printing stage is "the album phase", never "phase 2".
   ```
2. **Doc wording, for the supervisor:** where "phase 2" means printing (`Functional-Spec.md` §17 heading and line 89, `My-Journey-Concept.md:818`), change it to "the album phase". `Build-Plan.md:228` can then drop its disambiguation. This is a wording change, not a product change
3. **`.claude/skills/phase/SKILL.md`**, "Hard stops", add: "Before acting on any external resource (Vercel, a domain, a database host), take its ID from `CLAUDE.md` Names and IDs. If it is not there, find it, confirm it with the user and add it before acting."

## Related

- L-005: the deploy surprises started with a URL nobody had checked
- L-004: the Vercel project existed before any doc knew about it
- `My-Journey-Concept.md` §22 Naming
