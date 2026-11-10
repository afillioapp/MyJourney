# My Journey — project memory

Read this before doing anything in this repo.

## What this is

A photo app where every picture is sealed the moment it is taken and the whole year unlocks exactly one year later. The product is not about photographs. It is about what happens when time becomes part of the product.

Positioning: **not attention, intention.** Tone: self-recognition, self-progression, self-awareness.

Full detail is in `docs/`. `docs/Functional-Spec.md` is the source of truth for behaviour. `docs/Master-Prompt.md` is the brief. `docs/My-Journey-Concept.md` is the decision record, with dates.

**What we are building:** a playable prototype on dummy data. The user explores it to find bugs, discover features and decide on options. Getting to something playable comes before settling every question on paper.

## Rule zero

**Never decide a behaviour silently.** Almost every sensible default in this category is something this product has deliberately banned, so a quiet guess is worse than a blocked task.

When the docs do not settle something (rule as of 2026-10-27):

1. Look in `docs/Decisions-Needed.md`. If the item has a **provisional default**, build that, and nothing else
2. If it is not listed, stop and ask the supervisor. Do not pick
3. Every provisional default is labelled in the code (`// PROVISIONAL: Decisions-Needed B4`) so it can be found and changed. The ones marked "switchable" are wired to the prototype options panel, so the user can compare options in the app
4. A provisional default may never break the banned list. When unsure, the strictest reading wins
5. **Which questions reach the user** (user, 2026-11-09). Questions about what makes My Journey itself, such as the ritual, sealing, the reveal, rings, layers, visibility and the product's voice, go to the user. Generic app questions, such as notification settings, account basics, search or how a friend request is accepted, are not asked: the supervisor takes Instagram's behaviour as the reference, labels it `PROVISIONAL` in `docs/Decisions-Needed.md` as "Instagram reference", and tells the user afterwards. The banned list and steps 1 to 4 still win: where Instagram does something the banned list rules out, such as push notifications, counts, suggestions or streaks, the reference is dropped

`docs/Functional-Spec.md` section 20 records what was decided. A provisional default becomes a decision only when the user says so, and then it moves into §20.

The approved data model and fixture design are in `docs/Phase-1-Proposal.md` (approved 2026-10-25). Build against it; do not redesign it.

**When two docs disagree, do not pick.** `docs/Functional-Spec.md` §20 and `docs/My-Journey-Concept.md` §29 win. Cite both lines and raise it as an open question. Known conflicts are listed in `docs/Learnings/index.md` under "Read before you start".

## Which docs to trust

In this order:

1. `docs/Functional-Spec.md` §20 and `docs/My-Journey-Concept.md` §29: the dated decisions
2. The rest of `docs/Functional-Spec.md`
3. `docs/Phase-1-Proposal.md`
4. `docs/Master-Prompt.md`, `docs/Build-Plan.md`, and the rest of the Concept doc

`docs/Overview.md` is historical (2026-10-21, before the decisions). Never build or audit from it.

The Phase 2 drafts, `docs/Flows.md`, `docs/Art-Direction.md` and `docs/Microcopy.md`, are in review (2026-11-09) and wait on the user's answers. They are not decisions. Where they rest on a provisional default, the default in `docs/Decisions-Needed.md` is what to build.

## Names and IDs

The only place to take these from. Never find an external resource by matching a name.

| What | Value |
|---|---|
| Product | My Journey (formerly Retrogram) |
| Folder | `Retro-Gram/myjourney`, at `~/Projects/Retro-Gram/myjourney`. Moved out of `~/Documents/Business/` on 2026-11-09 so Google Drive no longer backs it up. Keep it out of `~/Documents` and `~/Desktop` |
| Vercel team | `team_eD0tvc1w4vZhmrNBOUb5F8Q0` (slug `afillio`) |
| Vercel project | `myjourney`, `prj_5Cw4kvcC5aCVNQJPlf1irWVJb2b8` |
| Production URL | `myjourney-afillio.vercel.app`. `myjourney.vercel.app` is **not ours** |
| Phase 2 preview | `/preview/` on preview deployments of branch `claude/wizardly-planck-77eo2h`; stable alias `myjourney-git-claude-wizardly-planck-77eo2h-afillio.vercel.app/preview/`. Private: Vercel team login. Regenerate with `python3 preview/build.py` |
| Storage | Local and GitHub only. Never Google Drive, its connector or its folders (user, 2026-11-04) |
| Search terms | my journey, myjourney, retrogram, retro-gram |

"Phase n" always means a build phase from `docs/Build-Plan.md`. The business's printing stage is "the album phase".

## The banned list

Breaking one of these is a build failure, not a style disagreement.

| Never | Why |
|---|---|
| No retakes | The moment is gone. However imperfect, that is the photo |
| No edits to reflections | You never rewrite your past self. You add a new one |
| No comments from anyone else | The only voice on a photo is the owner's |
| No face recognition | People are tagged by hand, deliberately |
| No ads anywhere | Ads need attention, which the product rejects |
| No streaks, counters, progress bars, reminders | Engagement mechanics are banned outright |
| No re-engagement notifications | We are not trying to get users onto the app |
| No ranking, levels, badges, leaderboards | The circle is a record, not a rank |
| No photo feed | The feed carries announcements only, never images |
| Nothing leaks from a sealed year | Not thumbnails, not counts, not "3 moments captured" |
| No layer is ever shown to the person on it | Each user sees only their own map |

**Low usage is the goal, and the product says so publicly.** If a change would increase time in app, it is probably wrong.

## Enforce rules in code, not by convention

- Reflections and journey overviews are **append-only at the data layer**. No update path exists
- Sealed content is **unreadable**, not merely hidden in the UI
- No endpoint returns which layer a viewer occupies in someone else's map
- No comment object exists on a photo

## How the product works

**Commit** — on any day, the user picks one of three types and presses Commit. It cannot be changed afterwards. The journey runs 12 months from that date. One journey at a time: the next Commit opens only once the current one has unlocked. No abandoning.

| Type | Difficulty | Cadence | Photos/year | Highlights |
|---|---|---|---|---|
| Explorer | Easy | 4 monthly | 48 | 4 |
| Wanderer | Normal | 2 monthly | 24 | 2 |
| Contemplator | Hard | 1 monthly | 12 | 1 |

Each month of the journey has its own limit. Unused frames carry forward to later months and lapse when the journey ends.

A highlight is a limited window where the frame limit does not apply. The user starts it, it lasts 24 hours, only one can be open at a time, and it holds up to the type's yearly quota.

**Capture** — inside the app, at the moment, three taps: from opening the app, to the sealed year, to the camera, the shutter (§20 OOOO). No retakes, no quality bar, photos only. Sealed instantly. Photos are never deleted. An optional second step offers a handwritten A4 note, photographed, which becomes the writing on the back. It can be added up to 15 minutes after capture, never after; the app says so with a fixed circle drawing, never a countdown (§20 UUUU, XXXX).

**The sealed year** — nothing is visible to anyone, including the owner. Others may know only that a sealed journey exists.

**Reveal** — the whole journey unlocks 12 months after Commit, as one event. The single engagement moment of the year: meeting the photos first, one at a time in the order taken (§20 PPPP), then tagging people by hand (users, or a typed name), chapter and feeling tags, the year overview, visibility. Visibility is Network until the owner chooses. Each choice is set once, and everything locks when the reveal is finished.

**Reflect** — one per photo per year, immutable, stacking forever. Each photo's slot opens on the anniversary of the day it was taken and stays open a year, so reflecting is not part of the reveal (§20 VVVV, 2026-11-10). The overview stacks the same way, one per journey per year, readable by the network. Both are optional.

**Layers** — concentric rings with the user at the core: tight (5+ shared photos), middle (2–4), outer (1). A tag puts the tagged user on the tagger's map only. A journey with no crossing moves someone out one ring, and nobody drops off. A layer is never shown to the person on it.

**Network and friends** (decided 2026-11-09, `docs/Functional-Spec.md` §20 KKKK) — the network is your friends: people who accepted a friend request, which both must agree to. Requests arrive inside the app only, with no notification, no friend count and no "people you may know". The map comes only from tags, so being someone's friend says nothing about being on their map. Someone on your map who is not a friend sees only your Public photos. Close friends are a list you choose from among your friends; whether they see anything extra is still open (`docs/Decisions-Needed.md` E2). The data model amendment is written on paper (`docs/Phase-1-Amendments.md` §12), untested until Phase 3. Blocking: §20 MMMM, Amendments §15. No one can tell they are on someone else's rings: §20 NNNN.

**The feed** — announcements only, on three events: journey launched (when the reveal is finished), reflection left (only to people who can see that photo), path crossed (every crossing).

**The profile** — the destination. The circle frames the picture, one ring per year, a record not a rank. The year's activity line twists into that circle, and the activity graph appears only after the year unlocks.

## How the build runs

Phases and gates are in `docs/Build-Plan.md`. Where each one stands is in `docs/Status.md`. Update it after every step.

- `/phase` shows status. `/phase next` runs one deliverable through its owner agent and a rules audit. `/phase gate <n>` checks a gate. Only the user passes a gate
- `/rules-audit <target>` runs the rules-guardian against `docs/Rules-Rubric.md`
- One agent per role, in `.claude/agents/`. Workers report evidence to the supervisor and never to each other

## Building anything visual

Nothing in this product is visible until a year has passed. **Fixtures and a time control come before any screen.** See `docs/Functional-Spec.md` section 21 for the required dataset.

## Voice

Nostalgic, 1970s to 90s family album. The circle is the identity system. "Circling back" is the product's phrase. Nothing asks the user to perform.

Lines that belong in the product, stated plainly:

- "It's not about attention. It's about intention."
- "You've come further than you think."
- "Strict at capture. Generous at reflect."
- "No retakes. That moment is gone."
- "This app takes time, like many other good things."
- "We want you here less, not more."

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- `graphify-out/` is in `.gitignore`. The graph is local and is not committed
- Edit nothing while a graph build is running. A file changed mid-read is recorded as only partly read (L-006)
- **The graph is a map, not a source.** Use it to find which doc sections cover a topic, then read those sections and cite them. Never act on an INFERRED or AMBIGUOUS edge as if it were a decision; that would be inventing a behaviour (rule zero)
- `graphify update .` only re-reads code. After a doc changes, run `/graphify . --update` so the change reaches the graph. `/phase` does this after each deliverable
