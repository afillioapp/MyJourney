# My Journey — Build Framework

How to get from the concept to a working website and web app with dummy data. Seven phases, 0 to 6, each with a gate that must pass before the next one starts.

Last updated: 2026-10-27

---

## The shape of it

```
Phase 0  Decide        →  unblock the contradictions
Phase 1  Define        →  data model, rules list, fixture design
Phase 2  Look          →  art direction + flows, on paper
Phase 3  Foundation    →  schema, fixtures, TIME CONTROL
Phase 4  Build app     →  screens, in ritual order
Phase 5  Build site    →  marketing site (can start any time after Phase 2)
Phase 6  Review        →  rules audit, QA, polish
```

The one rule of sequencing: **fixtures and the time control come before any screen.** Nothing in this product is visible until a year has passed, so without them there is nothing to build against and nothing to look at.

---

## Phase 0 — Decide

Nothing starts until these are answered. They are in `Functional-Spec.md` section 20.

**Blocking:**

- [x] Unlock: **the whole journey unlocks once a year.** Resolved 2026-10-25
- [x] Handwritten note: **optional second step after capture.** Resolved 2026-10-25

**Needed before the schema is written:**

- [x] Do unused frames roll over or lapse? **They carry forward to later months of the same journey, and lapse when it ends.** Resolved 2026-10-25
- [x] Is cadence enforced per month or as an annual total? **Per month of the journey, counted from the commit date.** Resolved 2026-10-25
- [x] How is a highlight triggered, how long does it last, and is it capped? **The user starts it, it lasts 24 hours, and it's capped at the type's yearly quota.** Resolved 2026-10-25
- [x] Can a photo ever be deleted? **Never.** Resolved 2026-10-25
- [x] Can a journey be abandoned mid-year? **No.** Resolved 2026-10-25
- [x] Who can be tagged — users only, or contacts? **Users, or a typed name that never counts towards layers.** Resolved 2026-10-25

**Can wait, but not forever:**

- [ ] Age gating, if teenagers are a target
- [ ] Export and data ownership
- [x] Does the user name change yearly? **No. One name, kept.** Resolved 2026-10-25

All answers are recorded in `My-Journey-Concept.md` §29, together with the other decisions made during Phase 1.

**Gate:** every blocking item answered in writing, in `My-Journey-Concept.md`.
**Owner:** you.

---

## Phase 1 — Define

Turn decisions into things a builder can work from.

| Deliverable | Owner |
|---|---|
| Data model: the nine objects, their fields and relationships | Lead Tech |
| The rules list as testable statements, one line each | Rules Guardian |
| Fixture design: who the fake users are, which years, whose paths cross when | Fixture Designer |
| Screen inventory: every screen the app needs, named, nothing designed yet | UX |

**Gate:** a developer can read the data model and the fixture design and know exactly what to build, with no questions left.

---

## Phase 2 — Look

Still no code.

| Deliverable | Owner |
|---|---|
| Art direction: the circle system, rings, the nostalgic register, colour, type | Art Director |
| Flows on paper: Commit, capture, sealed state, reveal, reflect, layers, profile | UX |
| Microcopy for the moments that carry weight: Commit, sealed, reveal, "Your Journey is ready" | Copywriter |

**Gate:** someone who has never heard of the product can follow the flows and understand the ritual.

---

## Phase 3 — Foundation

The first code. No user-facing screens yet.

| Deliverable | Owner |
|---|---|
| Schema implemented, append-only where the rules demand it | Developer |
| **Time control** — jump the clock forward a year or five | Lead Tech |
| Fixture data loaded: five-year users, crossing paths, all three journey types, mixed visibility, reflection stacks of varying depth, one sealed year in progress | Fixture Designer + Developer |

**Gate:** you can query the fake data at any point in simulated time and get a sensible answer. Reveal works. Layers recompute. Paths cross.

This gate is the whole project's pivot. Everything after it is comparatively easy; nothing before it can be skipped.

---

## Phase 4 — Build the app

Screens in the order of the ritual, each one usable before the next starts.

1. Commit — pick a type, press the button
2. Capture — three taps, no retake
3. The sealed year — the empty state, and what a user does instead
4. Reveal — the annual moment: reflections, tagging, tags, overview, visibility
5. Profile — the circle, the rings, the activity line twisted into it
6. Walking a path — reading someone's journey start to now
7. Layers — the concentric navigation
8. Feed — announcements only
9. Positivity Feed — tag filtering

**Gate after each screen:** it works against fixture data at several points in simulated time.

---

## Phase 5 — Build the site

Can start any time after Phase 2. Static, no app logic.

| Deliverable | Owner |
|---|---|
| The founder story, attention versus intention, the ritual, the reveal, the album, the relationships | Content Manager + Copywriter |
| "We are not trying to get you onto the app" stated plainly and early | Content Manager |
| The three journey types explained | Content Manager |
| Build | Developer |

**Gate:** the four non-negotiable statements appear above the fold or close to it — strict at capture, no retakes, low usage is the goal, this app takes time.

---

## Phase 6 — Review

| Pass | Who | What they check |
|---|---|---|
| Rules audit | Rules Guardian | Every screen against the enforcement table in the spec. No streaks, no comments, no ranks, nothing leaking from a sealed year |
| Functional QA | QA | Every flow at several points in simulated time |
| Content QC | Content Manager | Copy consistent with the language bank, no drift in tone |
| Art review | Art Director | The circle system applied consistently |

**Gate:** a rules audit with zero findings. That one matters more than the others, because every rule you've locked is a thing a normal product would do and this one must not.

---

## Roles

| Role | Phases | Note |
|---|---|---|
| You | 0, and every gate | The decisions are yours |
| Lead Tech | 1, 3 | Owns the data model and the time control |
| UX | 1, 2 | Flows, separate from art direction |
| Art Director | 2, 6 | The circle system and the nostalgic register |
| Fixture Designer | 1, 3 | The demo lives or dies here |
| Developer | 3, 4, 5 | Frontend and the data layer |
| Content Manager | 5, 6 | Organises and holds the tone |
| Copywriter | 2, 5 | The weighted moments |
| Rules Guardian | 1, 6 | The one role a normal project doesn't have |
| QA | 6 | Note: QA and Quality Control are the same role |

---

## How the agent team should work

Adapted from *Agentic Design Patterns* (BASWE, 2026). Only the parts that apply to this build.

### 1. Start as far left as the problem allows

The autonomy ladder runs: single call → prompt chain → workflow → agent → multi-agent. Each step right adds capability, cost and risk.

**Most of this build is a workflow, not an autonomous agent.** The phases are a fixed sequence with gates. Use agents for the parts where the number of steps is genuinely unknown; use a plain chain for the rest. Multi-agent systems use roughly fifteen times the tokens of a chat interaction, so reach for them only when a subtask is large enough to pay for the coordination.

### 2. Supervisor and workers, never workers talking to workers

You are the supervisor. Each role is a worker with its own brief, its own context and its own output.

- Workers report to you, never to each other
- Workers return **evidence, not conclusions**: the file they changed, the screen they built, the finding they hit. One worker's assumption must never become your fact
- Give every worker a **self-contained brief**. A worker never sees your reasoning, only what you hand it

### 3. The folder is the blackboard

Agents do not message each other. They read and write shared state: the files in this folder. `Master-Prompt.md` is the shared context every worker reads before starting, `Functional-Spec.md` is the source of truth, and findings get written back as files.

This is why conflicting assumptions happen in the first place: two workers starting from different context. Shared context at the start, and a synthesis step where conflicts are reconciled explicitly, is the fix.

### 4. Every step names a verifiable output

"Research the topic" is not an executable step. "Design the flow" is not either.

Every step in every brief names the tool or action it uses, and the output that proves it is finished. Each phase gate in this plan is written that way on purpose. If a gate cannot be checked, rewrite it until it can.

### 5. The Rules Guardian is a critic, and a critic needs teeth

This is the most important borrowing. A critic that is the same model with the same prompt as the builder will agree with itself.

Make it strong:

- **A written rubric with numbered checks.** The banned list in `Master-Prompt.md`, one line per rule, each phrased as a testable statement
- **A separate, adversarial brief.** Not the builder's prompt
- **Require at least one issue per review.** Sycophantic critics pass everything
- **Prefer deterministic checks.** A test that fails if a comment field exists on a photo is worth more than an opinion that comments are absent. Automate every rule you can into a real check
- **Cap revisions at three rounds**, then escalate to you with the best attempt flagged

### 6. Budgets and stopping conditions live in code, not in the prompt

Asking an agent nicely to stop is not a stopping condition. The same logic applies to this product's own rules: "append-only" must be enforced at the data layer, not by a convention everyone agrees to follow.

Set a step cap, a cost ceiling and a time limit per task. When a limit is hit, return a partial result with a clear flag, never a crash and never a silent guess.

### 7. Human gates on anything irreversible

You are the gate for: the Phase 0 decisions, any change to a locked rule, and anything in the "still undecided" list. An agent that hits one of these stops and asks. It does not decide.

### 8. Briefs are tools, and tool design is prompt design

The guide's rule for tools applies to role briefs: one job each, say what it does and what it does **not** cover, and make the wrong move hard to express. Most failures that look like a bad agent are a badly written brief.

### 9. Every finding becomes a permanent check

When the Rules Guardian finds a violation, the fix is not just repairing that screen. The check goes into the rubric so it runs on every later review. The rubric grows; it never shrinks.

---

## What is deliberately not in this plan

- Real authentication, real photo storage, real printing. All of it belongs to the album phase of the business, not to this build
- Mobile apps. The capture rule says photos are taken inside the app, which eventually means a phone, but the prototype can demonstrate the ritual on the web
- Any revenue mechanism. Phase 1 of the business has no revenue line by decision
