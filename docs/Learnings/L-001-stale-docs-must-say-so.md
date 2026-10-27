# L-001: A doc that is not kept current says so in its first lines, and no agent builds or audits from it

| Date | Phase | Labels | Status |
|---|---|---|---|
| 2026-10-27 | 0 | docs, briefs | open |

## What happened

The 2026-10-25 decisions were written into `docs/My-Journey-Concept.md` §29, `docs/Functional-Spec.md` §20 and `docs/Phase-1-Proposal.md` §1. `docs/Overview.md` was not touched. It is dated before them and still states the old behaviour:

| Overview.md says | Decided 2026-10-25 |
|---|---|
| `Overview.md:125`: layers "Requires both people to have uploaded" | A tag puts the tagged user on the tagger's map only, and any user counts (`Functional-Spec.md` §20 G, line 277) |
| `Overview.md:133`: "Close friends can be given access to everything" | Close friends see nothing beyond the rest of the network (§20 H, line 278) |
| `Overview.md:210`: "The name could change each year" | One name, chosen once and kept (§20 item 8, line 268) |
| `Overview.md:70`: reflections dated per photo ("Photo 7 Jan 2019 → reflection 7 Jan 2020"), and "the window stays open until the next anniversary" | All photos of a journey move to their next slot together, on the journey's unlock anniversary (§20 D, line 274) |
| `Overview.md:63`: "24–48 per year" | Three types: 48, 24, 12 (`Functional-Spec.md` §3, lines 38–42) |
| `Overview.md:257–259`: the upload/sealed fork is "unresolved" | See L-002 |

Nothing marks the file as out of date:

- `Overview.md:3` calls it an "Export of the live doc ... (21 Oct 2026)". It does not say the export is frozen, or which file wins when they disagree
- `README.md:16` lists it as "Readable overview of the whole concept", with no warning
- The knowledge graph treats it as a hub. `graphify-out/GRAPH_REPORT.md:113` asks why Overview "connects `Founder Story and Positioning` to `Product Ritual and Concept`", and line 102 links `Build Decisions 2026-10-25` to it as AMBIGUOUS. Since `/phase` builds briefs with `graphify query` (`.claude/skills/phase/SKILL.md:37`), a query can send a worker to Overview.md as readily as to the spec

The stale lines were found by a knowledge-graph build on 2026-10-27, not by any step in the build process. No agent has built from them yet. That makes this a near-miss.

`My-Journey-Concept.md` shows the practice that would have prevented it. Its body sections carry inline markers such as "*(Superseded 2026-10-25: ... See §29.)*" at lines 99, 195, 381, 418, 596 and 677. Overview.md got no such marker, and no file-level marker exists anywhere.

## Root cause

The Phase 0 gate checked that the decisions were written down (`Build-Plan.md:51`: "every blocking item answered in writing, in `My-Journey-Concept.md`"). It did not check that every doc restating the old behaviour was updated or marked. No list says which docs are authoritative and which are historical. `CLAUDE.md` names the source of truth for behaviour, but agents also reach docs through the README and the graph, and neither tells them to skip Overview.md.

## The rule going forward

Every file in `docs/` either is maintained, or carries a "Historical" banner in its first five lines saying what supersedes it. Workers build and audit only from the files `CLAUDE.md` lists as authoritative.

## Where it is enforced

Not yet. Proposed:

1. **`docs/Overview.md`**, insert after line 1 (before Phase 1 continues):
   > **Historical. Not maintained since 2026-10-21.** Where it disagrees with `Functional-Spec.md` §20 or `My-Journey-Concept.md` §29, those win. Known stale lines: 63, 70, 125, 133, 210, 257–259. Do not build or audit from this file.
2. **`README.md:16`**: change "Readable overview of the whole concept" to "Historical overview, 21 Oct 2026. Not maintained; see the banner".
3. **`CLAUDE.md`**, under "What this is", add a short "Which docs to trust" list (before Phase 1 continues):
   > Authoritative, in this order: `Functional-Spec.md` §20 and `My-Journey-Concept.md` §29 (dated decisions), then the rest of `Functional-Spec.md`, then `Phase-1-Proposal.md` for the data model. `Master-Prompt.md` and `Build-Plan.md` are process. `Overview.md` is historical: never build or audit from it.
4. **`.claude/skills/phase/SKILL.md`**, step 2, add a brief bullet: "- Never cite `docs/Overview.md` or any file with a Historical banner as a source. If `graphify query` returns one, follow it to the authoritative section instead."
5. After 1–3, run `/graphify . --update` so the banner reaches the graph.

Status changes to `enforced` once items 1, 3 and 4 are in place.

## Related

- L-002, the same failure inside the maintained docs
- L-006: the graph only reflects a banner after a refresh
- `CLAUDE.md` "Rule zero"; `Functional-Spec.md` §20
