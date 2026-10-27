# Graph Report - myjourney  (2026-10-27)

## Corpus Check
- Corpus is ~26,611 words - fits in a single context window. You may not need a graph.

## Summary
- 253 nodes · 507 edges · 11 communities (9 shown, 2 thin omitted)
- Extraction: 78% EXTRACTED · 21% INFERRED · 1% AMBIGUOUS · INFERRED: 107 edges (avg confidence: 0.87)
- Token cost: 269,237 input · 0 output

## Community Hubs (Navigation)
- Product Ritual and Concept
- Agent Team Roles
- Banned List Enforcement
- Build Plan and Agent Patterns
- Functional Spec Mechanics
- Time Control and Fixtures (Agents)
- Foundation, Tags and Visibility
- Founder Story and Positioning
- Master Prompt and Open Questions
- Open Signup
- Journey Underway Check

## God Nodes (most connected - your core abstractions)
1. `Build Plan (Build Framework)` - 36 edges
2. `My Journey (project memory)` - 29 edges
3. `Functional Spec` - 23 edges
4. `Master Build Prompt` - 21 edges
5. `Build Status (blackboard)` - 21 edges
6. `Phase 1 Proposal: Data Model and Fixtures` - 20 edges
7. `The banned list` - 18 edges
8. `/phase skill (supervisor loop)` - 16 edges
9. `Rules Guardian agent (adversarial critic)` - 13 edges
10. `Fixtures and Time Control (§3)` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Hard stops: ask the user` --references--> `Phase 1 Proposal: Data Model and Fixtures`  [INFERRED]
  .claude/skills/phase/SKILL.md → docs/Phase-1-Proposal.md
- `Copywriter agent` --references--> `Nothing leaks from a sealed year`  [INFERRED]
  .claude/agents/copywriter.md → CLAUDE.md
- `Sealed-year empty state` --references--> `The sealed year`  [INFERRED]
  .claude/agents/ux.md → CLAUDE.md
- `Art Director agent` --references--> `My Journey — Working Concept`  [EXTRACTED]
  .claude/agents/art-director.md → docs/My-Journey-Concept.md
- `Copywriter agent` --references--> `My Journey — Working Concept`  [EXTRACTED]
  .claude/agents/copywriter.md → docs/My-Journey-Concept.md

## Hyperedges (group relationships)
- **Layers of voice on a photo (photo, handwritten note, reflections, overview)** — docs_my_journey_concept_handwritten_note, docs_my_journey_concept_reflect, docs_my_journey_concept_journey_overview, docs_my_journey_concept_reveal [EXTRACTED 1.00]
- **Network architecture: feed announces, layers navigate, profile is destination** — docs_my_journey_concept_announcement_feed, docs_my_journey_concept_layers, docs_my_journey_concept_profile, docs_my_journey_concept_visibility [EXTRACTED 1.00]
- **Circle identity system (circling back, rings, activity line)** — docs_my_journey_concept_circling_back, docs_my_journey_concept_the_circle, docs_my_journey_concept_activity_line, docs_my_journey_concept_layers [INFERRED 0.85]
- **Reveal Ritual: reflections, people tags, chapter/feeling tags, overview, visibility** — docs_functional_spec_reveal, docs_functional_spec_reflection, docs_functional_spec_chapter_tags, docs_functional_spec_feeling_tags, docs_functional_spec_journey_overview, docs_functional_spec_visibility_levels, docs_functional_spec_no_face_recognition [EXTRACTED 1.00]
- **Database-level rule enforcement for sealing and immutability** — docs_phase_1_proposal_postgres_rule_enforcement, docs_phase_1_proposal_row_level_security_sealing, docs_phase_1_proposal_journey_key, docs_phase_1_proposal_one_journey_exclusion_constraint, docs_phase_1_proposal_capture_function, docs_phase_1_proposal_schema_checks [EXTRACTED 1.00]
- **Paths cross again after years apart (demo centrepiece)** — docs_phase_1_proposal_steady_lantern, docs_phase_1_proposal_second_wind, docs_phase_1_proposal_crossing_paths_fixture, docs_phase_1_proposal_layer_computation, docs_phase_1_proposal_sim_clock [INFERRED 0.85]
- **My Journey agent team under the /phase supervisor** — claude_skills_phase_skill_phase, claude_agents_art_director_art_director, claude_agents_content_manager_content_manager, claude_agents_copywriter_copywriter, claude_agents_developer_developer, claude_agents_fixture_designer_fixture_designer, claude_agents_lead_tech_lead_tech, claude_agents_qa_qa, claude_agents_rules_guardian_rules_guardian, claude_agents_ux_ux [EXTRACTED 1.00]
- **Time control and fixtures that make the product visible before a year passes** — claude_fixtures_before_screens, claude_agents_lead_tech_sim_clock, claude_agents_lead_tech_app_now, claude_agents_fixture_designer_scripted_future, claude_agents_developer_simulated_time_testing [INFERRED 0.85]
- **Journey lifecycle: commit, capture, seal, reveal, reflect** — claude_commit, claude_capture, claude_sealed_year, claude_reveal, claude_reflect [EXTRACTED 1.00]

## Communities (11 total, 2 thin omitted)

### Community 0 - "Product Ritual and Concept"
Cohesion: 0.08
Nodes (41): Activity Line (twisted into the circle), Announcement Feed (three events), Brand Language: Yoga and Vibration, Build Decisions 2026-10-25 (Phase 1), Capturing the Low Points, Chapter Tags (fixed categories), Circling Back, Commit Button (+33 more)

### Community 1 - "Agent Team Roles"
Cohesion: 0.15
Nodes (28): Art Director agent, Content Manager agent, [copy: copywriter] markers, Copywriter agent, Developer agent, Testing screens at several simulated times, Multi-user testing via access matrix, Gate control procedure (+20 more)

### Community 2 - "Banned List Enforcement"
Cohesion: 0.10
Nodes (12): Four non-negotiables above the fold, Rules Guardian agent (adversarial critic), Sealed-year empty state, Append-only reflections and overviews at data layer, Capture (three taps, sealed instantly), The feed (announcements only), Handwritten A4 note (back of photo, 15-minute window), Layers (tight, middle, outer rings) (+4 more)

### Community 3 - "Build Plan and Agent Patterns"
Cohesion: 0.12
Nodes (30): Build Plan (Build Framework), Agentic Design Patterns (BASWE, 2026), Art Director (role), Autonomy Ladder, Briefs Are Tools, Budgets and Stopping Conditions in Code, Content Manager (role), Copywriter (role) (+22 more)

### Community 4 - "Functional Spec Mechanics"
Cohesion: 0.09
Nodes (30): Deliberately Not in This Plan, Phase 4 — Build the App, Album and Print (phase 2), Capture (three taps, no retakes), Commit, Contemplator (1/month, 12/yr, 1 highlight), Explorer (4/month, 48/yr, 4 highlights), Feed (announcements only) (+22 more)

### Community 5 - "Time Control and Fixtures (Agents)"
Cohesion: 0.12
Nodes (23): Fixture Designer agent, Scripted future (actions applied on clock jumps), app_now(), Lead Tech agent, Schema checks as build-failing tests (Phase-1-Proposal 2.5), sim_clock (single forward-only clock), /phase next (one deliverable per run), Functional Spec (+15 more)

### Community 6 - "Foundation, Tags and Visibility"
Cohesion: 0.12
Nodes (24): Fixture Designer (role), Fixtures and Time Control Before Any Screen, Lead Tech (role), Phase 3 — Foundation, Chapter Tags (ME→ME, ME→YOU, ME→IT), Demo and Fixture Requirements, Feeling Tags, Positivity Feed (+16 more)

### Community 7 - "Founder Story and Positioning"
Cohesion: 0.12
Nodes (13): My Journey — Working Concept, Founder Story (deactivated Instagram), Instagram (contrast reference), Language Bank, My Journey (product), Naming (My Journey, originally Retrogram), Pitch Deck as Family-Album Experience, The Ritual (Capture→Seal→Wait→Reveal→Reflect→Preserve→Repeat) (+5 more)

### Community 8 - "Master Prompt and Open Questions"
Cohesion: 0.16
Nodes (15): Activity Graph (after unlock only), Age Gating and Parental Consent (open), Export and Data Ownership (open), Profile Circle and Rings, Master Build Prompt, Circling Back, Core Message: People Do Not See How Far They Have Come, Definition of Done (+7 more)

## Ambiguous Edges - Review These
- `Three Journey Types` → `Activity Line (twisted into the circle)`  [AMBIGUOUS]
  docs/My-Journey-Concept.md · relation: references
- `Announcement Feed (three events)` → `Unresolved Fork: Upload Model vs Sealed Model`  [AMBIGUOUS]
  docs/My-Journey-Concept.md · relation: conceptually_related_to
- `Build Decisions 2026-10-25 (Phase 1)` → `My Journey — Product Overview`  [AMBIGUOUS]
  docs/Overview.md · relation: conceptually_related_to

## Knowledge Gaps
- **28 isolated node(s):** `Explorer (easy, 48/yr, 4 highlights)`, `Wanderer (normal, 24/yr, 2 highlights)`, `Journey Overview (Year Note)`, `Veja (independence reference)`, `Holmes–Rahe Life Stress Inventory` (+23 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 35 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `My Journey — Product Overview` connect `Founder Story and Positioning` to `Product Ritual and Concept`?**
  _High betweenness centrality (0.321) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Build Status (blackboard)` (e.g. with `The Folder Is the Blackboard` and `Age Gating and Parental Consent (open)`) actually correct?**
  _`Build Status (blackboard)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Explorer (easy, 48/yr, 4 highlights)`, `Wanderer (normal, 24/yr, 2 highlights)`, `Journey Overview (Year Note)` to the rest of the system?**
  _28 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Product Ritual and Concept` be split into smaller, more focused modules?**
  _Cohesion score 0.07560975609756097 - nodes in this community are weakly interconnected._
- **Why does `My Journey — Working Concept` connect `Founder Story and Positioning` to `Master Prompt and Open Questions`, `Agent Team Roles`, `Build Plan and Agent Patterns`, `Time Control and Fixtures (Agents)`?**
  _High betweenness centrality (0.269) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Three Journey Types` and `Activity Line (twisted into the circle)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Announcement Feed (three events)` and `Unresolved Fork: Upload Model vs Sealed Model`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._