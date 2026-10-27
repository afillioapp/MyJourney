# Rules audit: Screen Inventory

- **Target:** `docs/Screen-Inventory.md` (534 lines, UX agent, 2026-10-27)
- **Against:** `docs/Rules-Rubric.md` version 1 (R-001 to R-137), plus R-138 to R-140 added by this audit
- **Auditor:** Rules Guardian, 2026-10-27
- **Verdict:** **FAIL**: 16 findings: 1 violation, 11 risks, 4 weak points

Line numbers are `Screen-Inventory.md` lines unless another file is named. Short source names follow the rubric's key: FS = `Functional-Spec.md`, P1 = `Phase-1-Proposal.md`, CL = `CLAUDE.md`, MP = `Master-Prompt.md`, BP = `Build-Plan.md`, MJC = `My-Journey-Concept.md`, RG = `.claude/agents/rules-guardian.md`. `docs/Overview.md` is not cited.

---

## 1. Automated checks

No code exists, so the auto checks that apply to copy and UI were run as text scans over the inventory. The shell's `grep` is ugrep, which rejected the context patterns, so the first scan uses a small Python scanner (reproduced in Appendix A). The second uses `/usr/bin/grep` with each rubric check's own grep aid. Full output is in Appendix B.

### 1.1 Commands

```
# Scan 1: banned words, each hit tagged by where it sits
python3 -I scan.py docs/Screen-Inventory.md
#   NEVER = inside a "Must never show" cell, an "On every state, never:" paragraph, or the line-38 list
#   OQ    = inside Open questions
#   HOLDS = inside a "Holds" cell, i.e. the inventory lets it appear
#   PROSE = anything else

# Scan 2: each rubric grep aid, run as written
F=docs/Screen-Inventory.md; G=/usr/bin/grep
run(){ echo "=== $1  /$2/"; $G -n -i -E -o ".{0,50}($2).{0,50}" $F || echo "(no hits)"; }
run R-006 'moments? captured|[0-9]+ *(photos?|moments?|frames?|shots?|pictures?)\b|\bof [0-9]+\b|frames? (left|used|remaining)|so far'
run R-013 'days? (left|to go|until|remaining)|unlocks? in|countdown|time left|[0-9]+ *d *[0-9]+ *h|in [0-9]+ days|ends in'
run R-098 'left this month|remaining|of (12|24|48)|[0-9]+ (more|to go)'
run R-099 '%|complete|[0-9]+ of [0-9]+|completion'
run R-095 "don't forget|remember to|you haven't|come back|we miss|still have|waiting for you|ending soon|last chance|nudge"
run R-096 'unread|badge|isNew|\bnew\b|seen_at|read_at|\bdots?\b|marker'
run R-071 'inner circle|inner ring|closest|close friend|your ring|moved (in|out|closer|further)|where you appear|appear'
run R-083 'lost|dropped|demoted|unfriend|fading|drift'
run R-102 '\btop\b|ahead|behind|veteran|elite|achievement'
run R-028 'abandon|cancel|quit|pause|end early|restart|start over'
run R-031 'retake|re-take|try again|redo|discard|undo|use photo|re-photograph'
run R-016/019 '\bedit|delete|remove|replace|trash'
run R-104 'autoplay|endless|infinite|more like this|refresh|scroll'
run R-124-extra 'level up|points|trending|followers|new!|days to go|frames left'

# Scan 3: banned items deferred rather than banned
/usr/bin/grep -n -i -o -E ".{0,70}(later|optional|phase 2|future|for now|not yet|v2|eventually|may now|may show|may appear|may be shown).{0,70}" docs/Screen-Inventory.md

# Graph
graphify query "unlock date shown to owner countdown"
graphify query "where you appear walking a path layer"
```

### 1.2 How the hits sort

| Word or pattern | Hits (line) | Sorted |
|---|---|---|
| streak | 38, 125, 143 NEVER · 528 OQ | Fine |
| badge | 38, 142, 188, 354 NEVER | Fine |
| level | 38, 142, 188, 354, 422 NEVER · 19 "User-level" | Fine. 422 is the banned "close friends" access level |
| rank, leaderboard, score | 38, 142, 145, 188, 354 NEVER | Fine |
| counter | 38, 105, 125 NEVER · 519, 528 OQ | 519 is OQ-27, see **finding 2** |
| progress | 38, 105, 125 NEVER | Fine |
| remaining, countdown, trending, recommended, timer, dot | none | The **absence** of "countdown" and "timer" from every never list is **findings 2 and 3** |
| left | 70, 71, 72, 105, 106, 293 NEVER · 197, 205–208, 305, 364, 514 the announcement name "reflection left" (FS:280) · 7, 462 prose · 518 OQ | 71 "Whether the time left in the window may show is OQ-26" sits in a never cell but treats a timer as open: **finding 3** |
| "n moments", "n of" | 105 NEVER · 502 OQ ("24–48" range) | Fine |
| notify / notification | 38, 210 NEVER · 507 OQ | Fine |
| remind | 38, 54, 105, 125, 313, 332, 438 NEVER · 507 OQ | Fine |
| unread | 105, 123 ("unreadable") NEVER · 516 OQ | No hit bans an unread marker anywhere: **finding 11** |
| new | 145, 207, 330, 351 HOLDS ("a new ring", "new slot reflections", "a new overview") · 19, 150, 222, 258, 434 prose · 499, 526 OQ | None is a "new" marker. The "new ring" at 145/351 is **finding 8** on other grounds |
| like, reaction, view | 38, 210, 231, 332, 354, 373 NEVER · 101, 112 "look like", "like many other good things" · 320 "their views changed" | Fine |
| comment, reply | 38, 166, 210, 228, 313, 373 NEVER · 427, 534 copy "readable, not commentable" | Fine. The scanner tagged 166 PROSE; it is an "On every state, for every viewer, never:" paragraph |
| follower | 38, 354 NEVER · rest are "follow", "follow-up" | Fine |
| popular(ity) | 210, 228 NEVER · 522 OQ | 210 cites P1:180 for popularity, which P1:180 does not contain: **finding 15** |
| face | 38, 125, 388 NEVER | Fine |
| thumbnail, preview | 70, 105, 143, 161, 349 NEVER | Fine |
| last capture | 105 NEVER | But line 107 lets a "last capture" affordance appear: **finding 1** |
| R-006 count patterns | 70, 105, 293 NEVER · 502 OQ | Fine |
| R-013 countdown patterns | 71 never cell (left open) · 519 OQ-27 | **Findings 2 and 3** |
| R-099 completion | 125 NEVER | See **finding 9** |
| R-031 retake | 38, 70, 77, 439 NEVER or the approved line · 282, 516 OQ-24 "re-photographed" | **Finding 4** |
| R-016/019 edit, delete | all NEVER, or the purpose line "never edited" (302) | Fine |
| R-104 scroll | 166 NEVER (S-06 only) | Nothing equivalent on S-09: **finding 12** |
| Scan 3, deferral words | only the `later-years` state name, "optional" for the note and overview (both decided, FS:257, FS:285), and "may show / may be shown" at 71, 93, 106 | No banned item is parked as "later" or "optional". The three "may show" lines are **findings 2 and 3** |

**Auto-scan result:** no banned word is in a Holds cell as a banned thing. Every literal hit is a ban, an open question or an innocent use. The violation and risks below come from reading, not from the word scan.

**Graph:** both queries returned only spec nodes. `Screen-Inventory.md` is not in the graph yet (written today, L-006), so the graph added nothing that a citation could rest on.

---

## 2. Findings

### Finding 1: VIOLATION. The sealed-year screen shows a trace of the last capture

- **Check:** R-010 (also R-003, R-134)
- **Where:** `Screen-Inventory.md:107`, against `:105` and `:22`
- **What is wrong:** The S-03 `sealed · note window` row puts "the way back to the note step for the photo just taken" in the **Holds** column. That state is defined at line 22 as "within 15 minutes of a photo's capture, while that photo has no note". So for 15 minutes after each capture the sealed-year screen looks different, and the difference exists only because a photo was just taken and has no note yet.
- **Why it breaks the rule:** R-010: "A capture changes nothing that any reader can observe, the owner included: no 'last captured' … recent-activity mark". The same screen's own never list at line 105 bans "Anything derived from `captured_at`, such as the last capture". Working out the state needs `captured_at` and the note's existence, and both are sealed rows (P1:48; R-003). No source puts a re-entry point on the sealed-year screen. FS:257 and FS:281 say only that the note is offered after capture and can be added up to 15 minutes later. OQ-24 (line 516) asks *how* the user gets back. It presupposes *that* they get back, and line 107 already places the route on S-03. Per the audit rule, a raised question does not excuse a thing the inventory also lets appear.
- **Severity:** violation
- **Raised by the inventory:** partly (OQ-24 asks how, not whether)

### Finding 2: RISK. The unlock date is left open to being shown as a countdown

- **Check:** R-013 (also R-135, G-17)
- **Where:** `Screen-Inventory.md:93`, `:90`, `:105`, `:519`
- **What is wrong:** Element 4 of S-03 is "The unlock date. Whether it may be shown relative to today is OQ-27", and OQ-27 asks "Is 'in 64 days' a counter under Spec:233?". The sealed never list at 105 names counters, progress bars and reminders, but no countdown, timer or relative date. Elements 1–4 trace only to P1:84. FS:74 ("Nothing in a sealed journey is visible: not to the user") is not set against it. FS ranks above P1 in `CLAUDE.md:25–30`.
- **Why it breaks the rule:** R-013 already bans this: "no 'n days to go', 'unlocks in', timer or ticking display. The owner may see the unlock date as a date." "In 64 days" is that countdown, and FS:233 bans visible counters during the sealed year with no conflict to resolve. Treating a decided ban as open invites a designer to draw it. Citing only P1:84 picks one side of G-17 without citing the other (R-135).
- **Severity:** risk
- **Raised by the inventory:** yes (OQ-27), but framed as open when the rubric has decided it

### Finding 3: RISK. No ban on a timer for the highlight window or the note window

- **Check:** R-140 (new), R-095, CL:60
- **Where:** `Screen-Inventory.md:71`, `:106`, `:294`, `:518` (highlight); `:277`, `:22` (note)
- **What is wrong:** Line 71 says "Whether the time left in the window may show is OQ-26", in the never column, treating "time left" as possibly allowed. The S-12 never list (277) bans the photo, a typed field, holding up capture and a second note. It has nothing on a 15-minute timer, the most reflexive element a designer would put on a time-limited step.
- **Why it breaks the rule:** A "time left" display on either window is a counter that ticks down. CL:60 and MP:42 ban counters outright. FS:233 bans them during the sealed year, and both windows exist only while a journey is sealed, so G-4's time-limit dispute does not reach them. RG:28 names "timers" by name. The rubric's own R-013 covers only the unlock countdown, so this gap is new: **R-140 added**. G-13 still leaves open whether a plain open-or-closed highlight state may show. That part of OQ-26 stays open.
- **Severity:** risk
- **Raised by the inventory:** yes for the highlight (OQ-26), no for the note window

### Finding 4: RISK. The note step leaves room for a review or re-shoot of the page

- **Check:** R-005, R-020, R-031
- **Where:** `Screen-Inventory.md:277`, `:282`, `:516`
- **What is wrong:** S-12's never list bans showing "The photo it belongs to", but not the **note page just photographed**. Line 282 and OQ-24 ask "Whether the page can be re-photographed before saving". A re-shoot before saving needs a review-before-save of a sealed image.
- **Why it breaks the rule:** R-005: after the shutter, nothing of the captured frame is shown, and "Same after the note photo is taken". R-020: "No UI control re-takes or removes a note". FS:228: "no review-before-save". The note is sealed like the photo (P1:48, P1:105). The inventory raises it as a question, so it is not counted as a violation.
- **Severity:** risk
- **Raised by the inventory:** yes (OQ-24)

### Finding 5: WEAK POINT. Capture and highlight controls may reveal availability before the attempt

- **Check:** R-138 (new), R-038, R-098
- **Where:** `Screen-Inventory.md:94–95`, `:72`, `:293`, `:517`
- **What is wrong:** S-03 elements 5 and 6 are "The way to Capture" and "The way to start a highlight". Nothing says whether these look the same when no frame or no highlight is left. OQ-25 asks "Is the camera offered at all?". A greyed-out camera or a hidden highlight button is a disabled-but-visible state. Shown each day, it tells the owner whether frames are left and when they come back. It also needs a pre-flight call that works out availability outside capture.
- **Why it is a weak point:** P1:49 says frames used, frames left and highlights left "are counted inside" `capture()` and `start_highlight()` "and never stored or returned". RG:28 names disabled-but-visible states as leaks. The rubric's R-038 covers only the two calls' replies, not a third call or a control state, so **R-138 is added** (Provisional on G-5 and Question 5).
- **Severity:** weak point
- **Raised by the inventory:** in part (OQ-25)

### Finding 6: RISK. The journey type on the sealed screen can carry the quota as a target

- **Check:** R-098 (also R-009)
- **Where:** `Screen-Inventory.md:91`, against `:53` and `:105`
- **What is wrong:** S-03 element 2 is "The journey's type". At Commit (line 53) the type is shown "with difficulty, cadence, photos per year and highlights". A designer reusing that type card on the sealed screen shows "48 photos a year · 4 highlights" all year. The sealed never list bans frames used and left, but not the quota itself.
- **Why it breaks the rule:** R-098: "No count of the quota is shown in a way that reads as a target". FS:243 bans the same. A yearly total shown beside a running year is the target. Before Commit it describes a choice; after Commit it is a goal.
- **Severity:** risk
- **Raised by the inventory:** no

### Finding 7: RISK. The profile can draw the current sealed year as a filling ring

- **Check:** R-012 (also R-011)
- **Where:** `Screen-Inventory.md:143`
- **What is wrong:** S-05 `sealed` holds "The current journey as existing, with type, commit date and unlock date only", on the screen whose whole identity is a circle of rings. The never column bans the activity graph and thumbnails or counts. It does not ban a partial, growing or dated arc for the current year, which is the reflex way to place "a journey with a start and end date" on a ring diagram.
- **Why it breaks the rule:** R-012: "no progress ring or arc on the circle for the current year, no elapsed-time bar". FS:187 bans "A visible grid being filled". A ring being filled is the same mechanic. The generic line 38 says "progress bars", which a designer may not read as covering an arc.
- **Severity:** risk
- **Raised by the inventory:** no

### Finding 8: RISK. Rings are tied to finishing the reveal, stated as settled

- **Check:** R-102, R-135 (G-7)
- **Where:** `Screen-Inventory.md:145`, `:351`, `:431`, `:434`, against `:142` and `:495`
- **What is wrong:** OQ-6 (495) correctly records that FS:185 ("One ring per year with the app") and P1:65 ("one ring per journey whose reveal is finished") disagree. But the Holds column at 145 states "A new ring" at `reveal-finished` citing P1:65 alone. S-21's purpose (431) says finishing makes "the year become a ring", and its Leads-to (434) is "Profile (own) S-05 (the new ring)". The flow is now written as: do the task, get the ring.
- **Why it breaks the rule:** R-135: where docs disagree the deliverable cites both and does not pick. The higher-trust doc (FS, `CLAUDE.md:28`) is the one not followed here. And a ring awarded for completing a step reads as an achievement, which R-102 bans ("treats more rings as better"; FS:185 "A record, not a rank"). The line 145 never cell bans "A ring presented as an achievement", but the flow at 434 presents exactly that.
- **Severity:** risk
- **Raised by the inventory:** yes (OQ-6), but the screens follow one side anyway

### Finding 9: RISK. Showing "which choices are already set" invites a completion meter

- **Check:** R-099 (Provisional, G-4), R-135
- **Where:** `Screen-Inventory.md:125`
- **What is wrong:** S-04 `reveal-open` holds "Which choices are already set, and that they are now fixed", across up to 48 photos and five steps. The plain way to draw that is a checklist or a tick per photo, which is a completion meter ("12 of 24 tagged"). The never cell bans "A completion bar" citing Brief:42 only.
- **Why it breaks the rule:** R-099 bans any completion meter, including for the reveal. It is Provisional because FS:233 limits the ban to the sealed year while CL:60 and MP:42 do not (G-4). The inventory follows MP:42 without citing FS:233. That is the safe side, but it still picks without citing both (R-135), and "which choices are set" is the opening a designer will use.
- **Severity:** risk
- **Raised by the inventory:** no

### Finding 10: RISK. Readers can total up tags and read rings off someone else's map

- **Check:** R-071, R-139 (new), G-12
- **Where:** `Screen-Inventory.md:35`, `:156`, `:166`, `:342`, `:373`, `:511`, `:512`
- **What is wrong:** "tagged" is a viewer class (35) and a viewer of S-06 (156). That implies a distinct view for a person tagged in the journey, and "How the tagged reader's appearances are shown, given layer invisibility, is OQ-19" (166). Separately, S-16 is "Reached from … S-17 (via a person tag, OQ-20)" (342), which assumes person tags are shown to readers and link to profiles while OQ-20 (512) is still open. If tags are shown, any network reader can count how often B appears in A's journey and read B's ring on A's map. Rings are exactly that count (FS:161).
- **Why it breaks the rule:** FS:164: "Each user sees only their own map". CL:65 and MP:47: no layer is shown to the person on it. R-071 covers only the person on the ring. Nothing in the rubric covered a third party reconstructing someone else's map from visible tags, so **R-139 is added** (Provisional for the tagged reader's own case, G-12). OQ-19 and OQ-20 raise the issue, so this is not a violation. But the navigation at 342 already wires in the route that depends on the open answer.
- **Severity:** risk
- **Raised by the inventory:** yes (OQ-19, OQ-20)

### Finding 11: RISK. The feed bans images and popularity but not unread markers, and its order is never raised

- **Check:** R-096, R-104 (Rubric Question 1)
- **Where:** `Screen-Inventory.md:210`, `:38`
- **What is wrong:** S-08's "never" paragraph (210) bans images, a fourth event type, counts, likes, replies, popularity and push. It does not ban an unread dot, a "new" marker, a "since your last visit" divider or a badge on the feed's entry point. Line 38 says the tables quote "only the banned items most at risk on that screen". By that rule, leaving unread markers off the feed reads as "not at risk here", on the one screen where they are most at risk. The feed's order is not raised as an open question anywhere, though the Positivity Feed's order is (OQ-30c).
- **Why it breaks the rule:** R-096: "no unread dot, badge count, 'new' marker or app-icon badge anywhere". Read state is also the base of every "come back, there's more" pattern (R-104). The announcement feed's order is Question 1 in the rubric's list of things no source covers. A designer will fill it with newest-first-since-last-seen.
- **Severity:** risk
- **Raised by the inventory:** no

### Finding 12: RISK. The Positivity Feed's Holds column says "Public photos", and it has no limit on endless content

- **Check:** R-086 and CL:63 under G-8; R-104
- **Where:** `Screen-Inventory.md:228`, `:231`
- **What is wrong:** The `reveal-finished` Holds cell reads "Public photos and their reflections … Whether the photo image itself appears is OQ-11". The first words a designer reads in the Holds column are "Public photos". Line 231's never list has no counterpart to S-06's "not … as effortless as scrolling" (166). That leaves a public, endlessly filtered stream with nothing against infinite scroll, "more like this" or autoplay.
- **Why it breaks the rule:** CL:63 and MP:45 ban a photo feed ("never images"). P1:317 fills the Positivity Feed with public photos. The docs disagree (rubric G-8), and OQ-11 cites both sides correctly, so this is not a violation. But the Holds wording leans to one side. R-104: no surface designed to make a visit longer. The Positivity Feed is the screen most shaped like a scroll feed.
- **Severity:** risk
- **Raised by the inventory:** yes for the image (OQ-11), no for endless content

### Finding 13: WEAK POINT. Nothing stops an in-app "reflections are open" marker on the anniversary

- **Check:** R-095, R-096
- **Where:** `Screen-Inventory.md:311`, `:313`, `:146`
- **What is wrong:** At every unlock anniversary all photos of every past journey open a new slot together (311). S-14 bans a push and a requirement to write (313). Neither S-14, S-05 (146) nor S-17 bans an **in-app** banner, dot or "Year 3 reflections are open" marker. Because every photo opens at once, a designer will reflexively announce it.
- **Why it is a weak point:** R-095 bans any in-app nudge to reflect, "no banner, toast, modal". FS:102: "never pushed or reminded to write one". The inventory bans the push but not the in-app form.
- **Severity:** weak point
- **Raised by the inventory:** no

### Finding 14: RISK. Feeling tags follow one doc, and "popular ones surface" is not raised

- **Check:** R-135, R-103 (G-14)
- **Where:** `Screen-Inventory.md:405`
- **What is wrong:** S-19 holds "Feeling tags as free text inside the category (Spec:131)". P1:141 stores feeling tags as (journey, free text) with no category. The inventory does not cite it. FS:131 also says "Popular ones surface over time and the best get promoted into official categories", against FS:202 "never by popularity". Neither tension appears in the 36 open questions (scan: "popular" occurs only at 210, 228, 522).
- **Why it breaks the rule:** R-135: cite both, do not pick (G-14). A tag field that suggests or sorts by popular tags is a popularity mechanic shown to the user, the kind R-103 keeps out of the Positivity Feed.
- **Severity:** risk
- **Raised by the inventory:** no

### Finding 15: WEAK POINT. Citations that point at the wrong line

- **Check:** R-134
- **Where:** `Screen-Inventory.md:197`, `:208`, `:305`, `:514` (Spec:282); `:210` (Proposal:180)
- **What is wrong:** "Reflection left reaches only people who can see that photo" is §20 J at `Functional-Spec.md:280`. The inventory cites `Spec:282` four times, and that line is §20 L, ring changes. Line 210 cites "Likes, replies or popularity (Proposal:180)". P1:180 lists likes and replies but not popularity (that is FS:202, which is about the Positivity Feed).
- **Why it is a weak point:** R-134: every behaviour traces to a source line. Phase 2 will follow these citations. A wrong line means the reader checks the wrong rule, and the popularity ban on the announcement feed has no source of its own. CL:62 (ranking) is the nearest one.
- **Severity:** weak point
- **Raised by the inventory:** no

### Finding 16: WEAK POINT. The time control is outside the product in name, but not shown to be under the seal

- **Check:** R-014, R-008, R-117
- **Where:** `Screen-Inventory.md:450–467`
- **What is wrong:** T-01 is "not part of the product and is never shown as a product feature" (454). It is not stated to apply the seal. On each jump it applies scripted actions, layers and announcements (455). A panel that reports what it applied ("Wind captured 3 photos"), or labels "jump to the next unlock" with whose journey and when, leaks sealed counts and other users' unlock dates. OQ-35 leaves the viewer switcher and the simulated-date display open. "Never shown as a product feature" does not say where it sits (inside the app's own navigation, or apart from it).
- **Why it is a weak point:** R-014 lists "the time-control panel" among the paths that must apply the seal. R-008 lets others learn only that a sealed journey exists. The inventory's T-01 entry has a never line for backward jumps only. The forward-only rule is held correctly (R-117).
- **Severity:** weak point
- **Raised by the inventory:** in part (OQ-35)

---

## 3. What held

Recorded so the next audit does not re-open it:

- Every screen carries an explicit never column, and line 38 applies the whole banned list and the P1:180 schema words to every screen
- S-02 bans preview, thumbnail, review-before-save, retake, import, quality checks and video (70)
- S-03's allowed list is closed ("Exactly this list", 86) and P1:84-bound. It bans counts, "3 moments captured", activity, notes, reminders and low-point prompts (105)
- Others see "exists only" for a sealed journey on S-06 (161) and S-16 (349)
- S-07 is owner-only and bans another user's map, a list and extra inner-ring access (175, 188)
- S-08 bans every image, including any not a photograph (210), which is stricter than FS:171 and on the safe side of G-9
- "Your Journey is ready" is placed as in-app text on S-04 (124), not as a notification, with OQ-15 raised (G-16, R-094)
- Close friends get no level (422). Face suggestion is banned at reveal and tagging (125, 388)
- T-01 is forward only (456)
- No banned item is parked as "later" or "optional" in any states table
- `Overview.md` is not cited (line 9)

---

## 4. Rubric additions

Added to `docs/Rules-Rubric.md` under their area headings:

| ID | Area | Statement (short) | From |
|---|---|---|---|
| R-138 | 3. Capture and cadence | Availability of a frame or highlight is learned only by trying: no control changes with it, and no other call reports it. Provisional on G-5 and Question 5 | Finding 5 |
| R-139 | 6. Layers | No screen lets anyone see or work out a ring on a map not their own: no per-person tag totals or groupings. Provisional for the tagged reader's own case (G-12) | Finding 10 |
| R-140 | 8. Engagement mechanics | No timer or time-left display on the note window or an open highlight | Finding 3 |

The rubric's banned-list coverage table was not edited, since this audit may only add R-IDs. R-138 and R-140 belong in the "streaks, counters" row and R-139 in the "No layer is ever shown" row. That table update is for the rubric owner's next revision.

---

## Appendix A: scanner

`/private/tmp/claude-501/-Users-alireza-Documents-Business-Retro-Gram/b40adc49-9189-4dde-b59d-25ba1ef5a572/scratchpad/scan.py` (scratchpad, not in the repo). Patterns, each case-insensitive:

```
streak · badge · \blevels?\b · \brank(s|ing)?\b · leaderboard · \bscores?\b · \bcounters?\b · \bcounts?\b|count\(
progress · remaining · \bleft\b · countdown|count down|counts down
\d+\s*(moments?|frames?|photos?|shots?)\b|\bof \d+\b|moments captured
\bin \d+ days\b|days? (left|to go|until|remaining)|unlocks? in\b|time left|ends in
notif · remind · unread · \bnew\b · \blikes?\b · reaction · \bviews?\b · comment · \brepl(y|ies)\b
follow(er)?s?\b · trending · popular · recommend · \bfaces?\b · thumbnail · preview
last (shot|capture|photo) · \bdots?\b · \btimer|ticking
```

A hit is tagged by the table column it falls in (by the header row containing "Must never show"), or by section (Open questions), or by line prefix ("On every state, never", "**Applies to every screen.**", "- **Must never show:**").

## Appendix B: raw output

### B.1 Scan 1 (scanner)

```
   7  left                     PROSE  ...f, the gap is listed under **Open questions** and left open....
  19  level                    PROSE  ...| `no-journey` | User-level. The user has no sealed journey. Two cases: **nev...
  19  new                      PROSE  ... journeys** (the last journey has unlocked and no new Commit yet, as Long Way Round). Commit is open. I...
  38  streak                   NEVER  ... "No face recognition" · "No ads, anywhere" · "No streaks, counters, progress bars, reminders" · "No re-en...
  38  streak                   NEVER  ...ent, reply, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:180). The tab...
  38  badge                    NEVER  ...-engagement notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed" · "Nothing le...
  38  badge                    NEVER  ...ly, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:180). The tables bel...
  38  level                    NEVER  ...· "No re-engagement notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed" · "Not...
  38  rank                     NEVER  ...minders" · "No re-engagement notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed...
  38  rank                     NEVER  ... "comment, reply, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:180)....
  38  leaderboard              NEVER  ...t notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed" · "Nothing leaks from a seale...
  38  score                    NEVER  ...ts too: "comment, reply, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal...
  38  counter                  NEVER  ... recognition" · "No ads, anywhere" · "No streaks, counters, progress bars, reminders" · "No re-engagement no...
  38  progress                 NEVER  ...on" · "No ads, anywhere" · "No streaks, counters, progress bars, reminders" · "No re-engagement notification...
  38  notify                   NEVER  ...rs, progress bars, reminders" · "No re-engagement notifications" · "No ranking, levels, badges or leaderb...
  38  remind                   NEVER  ...anywhere" · "No streaks, counters, progress bars, reminders" · "No re-engagement notifications" · "No rank...
  38  like                     NEVER  ...e banned as screen elements too: "comment, reply, like, reaction, caption, score, rank, streak, badge, v...
  38  reaction                 NEVER  ...ed as screen elements too: "comment, reply, like, reaction, caption, score, rank, streak, badge, view or fol...
  38  view count               NEVER  ...e, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:180). The tables below quo...
  38  comment                  NEVER  ...): "No retakes" · "No edits to reflections" · "No comments from anyone else" · "No face recognition" · "No ...
  38  comment                  NEVER  ...ma scan words are banned as screen elements too: "comment, reply, like, reaction, caption, score, rank, str...
  38  reply                    NEVER  ...ords are banned as screen elements too: "comment, reply, like, reaction, caption, score, rank, streak, ba...
  38  follower                 NEVER  ...ion, caption, score, rank, streak, badge, view or follower" (Proposal:180). The tables below quote only the ...
  38  face                     NEVER  ...flections" · "No comments from anyone else" · "No face recognition" · "No ads, anywhere" · "No streaks, ...
  54  remind                   NEVER  ...one has unlocked") | Any prompt to commit again: "Remind a user to capture, reflect, or return" (Spec:242)...
  70  count (any)              NEVER  ...aken, as a preview or thumbnail: "No previews, no counts of what is inside, no thumbnails" (Spec:75). "No ...
  70  left                     NEVER  ...to not taken in the app (Spec:53). Frames used or left (Proposal:49; Spec:243) |...
  70  thumbnail                NEVER  ...(Spec:228). The photo just taken, as a preview or thumbnail: "No previews, no counts of what is inside, no th...
  70  thumbnail                NEVER  ...il: "No previews, no counts of what is inside, no thumbnails" (Spec:75). "No tagging, no writing, no choices"...
  70  preview                  NEVER  ...fore-save" (Spec:228). The photo just taken, as a preview or thumbnail: "No previews, no counts of what is ...
  70  preview                  NEVER  ... photo just taken, as a preview or thumbnail: "No previews, no counts of what is inside, no thumbnails" (Sp...
  71  left                     NEVER  ...pec:65, Spec:265, Proposal:96) | Highlight photos left, highlights left (Proposal:49). Whether the time ...
  71  left                     NEVER  ... Proposal:96) | Highlight photos left, highlights left (Proposal:49). Whether the time left in the windo...
  71  left                     NEVER  ..., highlights left (Proposal:49). Whether the time left in the window may show is OQ-26 |...
  71  days to go / in n days   NEVER  ... left, highlights left (Proposal:49). Whether the time left in the window may show is OQ-26 |...
  72  count (any)              NEVER  ... What the user sees is not specified: OQ-25 | Any count or target: "Show a count of how much of their quo...
  72  count (any)              NEVER  ...t specified: OQ-25 | Any count or target: "Show a count of how much of their quota is left in a way that ...
  72  left                     NEVER  ...rget: "Show a count of how much of their quota is left in a way that reads as a target" (Spec:243) |...
 101  count (any)              PROSE  ...ing at all: as the owner, "photos return 0 rows, `count(*)` returns 0" (Proposal:178). So any empty-list ...
 101  like                     PROSE  ...ny empty-list or still-loading pattern would look like a fault. The emptiness is the product (Brief:130;...
 105  counter                  NEVER  ...50). Any note (sealed, Proposal:105). "No visible counters, no progress bars, no reminders during the sealed...
 105  count (any)              NEVER  ... `sealed` | Elements 1–8 above | "No previews, no counts of what is inside, no thumbnails" (Spec:75). "Not...
 105  count (any)              NEVER  ...e, no thumbnails" (Spec:75). "Not thumbnails, not counts, not '3 moments captured'" (Brief:46). Frames use...
 105  progress                 NEVER  ... (sealed, Proposal:105). "No visible counters, no progress bars, no reminders during the sealed year" (Spec:...
 105  left                     NEVER  ...oments captured'" (Brief:46). Frames used, frames left, highlights left (Proposal:49). The year's activi...
 105  left                     NEVER  ... (Brief:46). Frames used, frames left, highlights left (Proposal:49). The year's activity graph or line:...
 105  n moments / n of         NEVER  ...ils" (Spec:75). "Not thumbnails, not counts, not '3 moments captured'" (Brief:46). Frames used, frames left, ...
 105  remind                   NEVER  ...:105). "No visible counters, no progress bars, no reminders during the sealed year" (Spec:233). A reminder...
 105  remind                   NEVER  ...o reminders during the sealed year" (Spec:233). A reminder to capture (Spec:242). A prompt to photograph a...
 105  unread                   NEVER  ... capture or which months have photos, since it is unreadable (Proposal:48, 50). Any note (sealed, Proposal...
 105  thumbnail                NEVER  ...e | "No previews, no counts of what is inside, no thumbnails" (Spec:75). "Not thumbnails, not counts, not '3 ...
 105  thumbnail                NEVER  ...of what is inside, no thumbnails" (Spec:75). "Not thumbnails, not counts, not '3 moments captured'" (Brief:46...
 105  preview                  NEVER  ...| `sealed` | Elements 1–8 above | "No previews, no counts of what is inside, no thumbnails" (Sp...
 105  last shot / last capture NEVER  ... Anything derived from `captured_at`, such as the last capture or which months have photos, since it is unreadab...
 106  left                     NEVER  ...6 | As in `sealed`, and highlight photos taken or left (Proposal:49) |...
 112  like                     PROSE  ...(Brief:115–122, for example "This app takes time, like many other good things."). Where each goes is the...
 123  unread                   NEVER  ...d` | Not reachable | Anything: "Sealed content is unreadable by the owner, not merely hidden in the UI" (S...
 125  streak                   NEVER  ...inder to finish (Spec:242). A completion bar: "No streaks, counters, progress bars, reminders" (Brief:42)....
 125  counter                  NEVER  ...finish (Spec:242). A completion bar: "No streaks, counters, progress bars, reminders" (Brief:42). The album ...
 125  progress                 NEVER  ...ec:242). A completion bar: "No streaks, counters, progress bars, reminders" (Brief:42). The album order step...
 125  remind                   NEVER  ... faces: "No face recognition, ever" (Spec:127). A reminder to finish (Spec:242). A completion bar: "No str...
 125  remind                   NEVER  ...letion bar: "No streaks, counters, progress bars, reminders" (Brief:42). The album order step: "Optionally...
 125  face                     NEVER  ...photo can never be deleted" (Spec:266). Suggested faces: "No face recognition, ever" (Spec:127). A remind...
 125  face                     NEVER  ...ever be deleted" (Spec:266). Suggested faces: "No face recognition, ever" (Spec:127). A reminder to fini...
 142  badge                    NEVER  ...:694) | "no scores, no levels, no leaderboard, no badges, no comparison between users" (Spec:185). Anythi...
 142  level                    NEVER  ...is simply younger" (Concept:694) | "no scores, no levels, no leaderboard, no badges, no comparison between...
 142  leaderboard              NEVER  ...ounger" (Concept:694) | "no scores, no levels, no leaderboard, no badges, no comparison between users" (Spec:18...
 142  score                    NEVER  ...eir circle is simply younger" (Concept:694) | "no scores, no levels, no leaderboard, no badges, no compari...
 142  count (any)              HOLDS  ...picture, the circle with no rings (whether a ring counts years with the app or finished reveals is OQ-6). ...
 143  streak                   NEVER  ...the sealed year. A visible grid being filled is a streak mechanic and is banned" (Spec:187). Any thumbnail...
 143  count (any)              NEVER  ...hanic and is banned" (Spec:187). Any thumbnail or count from the sealed journey (Spec:75) |...
 143  thumbnail                NEVER  ... a streak mechanic and is banned" (Spec:187). Any thumbnail or count from the sealed journey (Spec:75) |...
 145  rank                     NEVER  ...ing presented as an achievement: "A record, not a rank" (Spec:185) |...
 145  new                      HOLDS  ...| `reveal-finished` | A new ring: "one ring per journey whose reveal is finis...
 150  new                      PROSE  ...- **Copy:** the young circle of a new user `[copy: copywriter]`...
 161  count (any)              NEVER  ...g its existence in detail" (Spec:246). Any photo, count, thumbnail or capture date (Spec:75) |...
 161  thumbnail                NEVER  ...xistence in detail" (Spec:246). Any photo, count, thumbnail or capture date (Spec:75) |...
 163  follower                 HOLDS  ... | Photos by their locked visibility. Reflections follow their photo (Spec:276). The overview, to the owne...
 166  comment                  PROSE  ... not be as effortless as scrolling" (Spec:177). A comment or reply: "Others may read; only the owner writes...
 166  reply                    PROSE  ...effortless as scrolling" (Spec:177). A comment or reply: "Others may read; only the owner writes" (Spec:1...
 178  follower                 PROSE  ...ly when the owner finishes a reveal. So the table follows the **owner's** journey states....
 185  count (any)              HOLDS  ...urney at tight (5+), middle (2–4) or outer (1) by count, straight to that ring (Spec:161, Spec:282). Unta...
 185  count (any)              NEVER  ... map" (Spec:165). Typed names: "Typed names never count" (Spec:163) |...
 188  badge                    NEVER  ...twork" (Spec:150; see OQ-4). "No ranking, levels, badges or leaderboards" (Brief:44). Whether past rings,...
 188  level                    NEVER  ...f the network" (Spec:150; see OQ-4). "No ranking, levels, badges or leaderboards" (Brief:44). Whether past...
 188  rank                     NEVER  ...he rest of the network" (Spec:150; see OQ-4). "No ranking, levels, badges or leaderboards" (Brief:44). Whet...
 188  leaderboard              NEVER  ...ec:150; see OQ-4). "No ranking, levels, badges or leaderboards" (Brief:44). Whether past rings, drift history o...
 188  count (any)              NEVER  ...Whether past rings, drift history or shared-photo counts appear is OQ-36....
 197  left                     PROSE  ...d" to the owner's network (Spec:283); "reflection left" only to people who can see that photo (Spec:282)...
 200  follower                 PROSE  ...The table follows the state of the **announced** journey....
 205  left                     HOLDS  ...| `unlock-day`, `reveal-open` | "Reflection left", if the owner writes one (Proposal:117), to thos...
 206  left                     HOLDS  ...rossed", one per crossing (Spec:280). "Reflection left" | Who is named in "path crossed", and whether it...
 207  left                     HOLDS  ...| `later-years` | "Reflection left" for new slot reflections | |...
 207  new                      HOLDS  ...| `later-years` | "Reflection left" for new slot reflections | |...
 208  left                     HOLDS  ...(viewer with an empty network) | Only "reflection left" on public photos would reach them (Spec:282 with...
 210  count (any)              NEVER  ...fourth event type (Proposal:168, Proposal:183). A count: "no count column" (Proposal:168). Likes, replies...
 210  count (any)              NEVER  ...t type (Proposal:168, Proposal:183). A count: "no count column" (Proposal:168). Likes, replies or popular...
 210  notify                   NEVER  ...roposal:180). A push to return: "No re-engagement notifications of any kind" (Spec:236)....
 210  like                     NEVER  ...:183). A count: "no count column" (Proposal:168). Likes, replies or popularity (Proposal:180). A push to ...
 210  reply                    NEVER  ...A count: "no count column" (Proposal:168). Likes, replies or popularity (Proposal:180). A push to return: "...
 210  popular                  NEVER  ...o count column" (Proposal:168). Likes, replies or popularity (Proposal:180). A push to return: "No re-engag...
 222  new                      PROSE  ...own state changes nothing: the same feed serves a new user (Spec:30) and a user in a sealed year (Conce...
 222  follower                 PROSE  ...The table follows the state of the **source** journey. The reader's...
 228  comment                  NEVER  ...pularity" (Spec:202). "Public means readable, not commentable" (Spec:152) |...
 228  popular                  NEVER  ...photo image itself appears is OQ-11 | Ordering by popularity: "never by popularity" (Spec:202). "Public mea...
 228  popular                  NEVER  ...ears is OQ-11 | Ordering by popularity: "never by popularity" (Spec:202). "Public means readable, not comme...
 231  count (any)              NEVER  ...er nudged" (Spec:209). Likes, reactions, views or counts (Proposal:180). Which tags qualify, chapter filte...
 231  like                     NEVER  ... a low point: "invited, never nudged" (Spec:209). Likes, reactions, views or counts (Proposal:180). Which...
 231  reaction                 NEVER  ...point: "invited, never nudged" (Spec:209). Likes, reactions, views or counts (Proposal:180). Which tags qual...
 231  view count               NEVER  ...ited, never nudged" (Spec:209). Likes, reactions, views or counts (Proposal:180). Which tags qualify, cha...
 258  new                      PROSE  ...- **Viewer:** owner (new user)...
 293  left                     NEVER  ...rs, cut off at unlock (Proposal:133) | Highlights left or used: "Frames used, frames left and highlights...
 293  left                     NEVER  ...) | Highlights left or used: "Frames used, frames left and highlights left are counted inside them and n...
 293  left                     NEVER  ...or used: "Frames used, frames left and highlights left are counted inside them and never stored or retur...
 305  left                     PROSE  ...where it came from. Writing one emits "reflection left" (Spec:282), seen in S-08...
 313  remind                   NEVER  ... (Spec:100). A push: "The user is never pushed or reminded to write one" (Spec:102). A requirement to writ...
 313  comment                  NEVER  ... edits, ever" (Spec:99). Anyone else writing: "No comments from others" (Spec:100). A push: "The user is ne...
 320  view count               PROSE  ...- **Purpose:** the owner writes how their views changed across the year, once per journey per yea...
 330  new                      HOLDS  ...| `later-years` | A new overview for slot *k*. The stack, readable back t...
 332  remind                   NEVER  ...: "Immutable, like everything else" (Spec:120). A reminder. A public reader....
 332  like                     NEVER  ...On every state, never: an edit: "Immutable, like everything else" (Spec:120). A reminder. A public...
 344  follower                 PROSE  ...The table follows the state of the **profile owner's** journeys....
 349  count (any)              NEVER  ...w only that one exists" (Spec:279) | Type, dates, counts, thumbnails, the year's activity: "Others see onl...
 349  thumbnail                NEVER  ...hat one exists" (Spec:279) | Type, dates, counts, thumbnails, the year's activity: "Others see only `has_jour...
 351  new                      HOLDS  ...| `reveal-finished` | The new ring. The journey by locked visibility | As above...
 354  badge                    NEVER  ...0, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). Follower or view counts (Proposal:1...
 354  level                    NEVER  ...r the inner ring (Spec:150, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). Follower or...
 354  leaderboard              NEVER  ...r ring (Spec:150, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). Follower or view counts (P...
 354  score                    NEVER  ... access for the inner ring (Spec:150, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). F...
 354  count (any)              NEVER  ...aderboard, … badges" (Spec:185). Follower or view counts (Proposal:180). Anything that "signals how the pe...
 354  view count               NEVER  ... … leaderboard, … badges" (Spec:185). Follower or view counts (Proposal:180). Anything that "signals how...
 354  follower                 NEVER  ...s, … levels, … leaderboard, … badges" (Spec:185). Follower or view counts (Proposal:180). Anything that "sig...
 364  left                     PROSE  ...-06, Positivity Feed S-09, Feed S-08 ("reflection left"). **Leads to:** Reflect S-14 (owner), Walking a ...
 373  like                     NEVER  ...On every state, never: a comment, reply or like (Spec:230, Proposal:180). A caption: "There's no ...
 373  comment                  NEVER  ...On every state, never: a comment, reply or like (Spec:230, Proposal:180). A captio...
 373  reply                    NEVER  ...On every state, never: a comment, reply or like (Spec:230, Proposal:180). A caption: "The...
 373  follower                 NEVER  ...ple tags are shown to readers is OQ-20. What "the follow-up" is is OQ-29....
 388  face                     NEVER  ...ec:286). How a user is found is OQ-33 | Suggested faces: "No face recognition, ever" (Spec:127), "No face...
 388  face                     NEVER  ...w a user is found is OQ-33 | Suggested faces: "No face recognition, ever" (Spec:127), "No face detection...
 388  face                     NEVER  ...aces: "No face recognition, ever" (Spec:127), "No face detection anywhere in the pipeline" (Spec:231). A...
 422  level                    NEVER  ...51). Each set once (Spec:286) | A "close friends" level: they "see nothing beyond the rest of the network...
 427  comment                  PROSE  ...- **Copy:** "Public means readable, not commentable" (Spec:152) `[copy: copywriter]`; that each c...
 434  new                      PROSE  ...eveal S-04. **Leads to:** Profile (own) S-05 (the new ring)...
 438  remind                   NEVER  ... overview (Spec:285) or reflections (Spec:102). A reminder to finish (Spec:242) |...
 462  left                     PROSE  ... Lantern #6 unlocks: `unlock-day`. "The reveal is left for whoever is demoing" | Proposal:200, Proposal:...
 495  count (any)              OQ     ...6. **What a ring counts.** Spec:185 says "One ring per year with the app"...
 497  follower                 OQ     ...§1 was not updated. Confirm the time states above follow the Proposal....
 499  new                      OQ     ...ots open on the owner's earlier journeys during a new sealed year (Proposal:294: lantern-1 slot 5 on 20...
 502  n moments / n of         OQ     ... floor". 12 is outside that range, and the middle of 24–48 is 36. Concept:799 still says "Frame range 24–...
 507  notify                   OQ     ...ey has unlocked, when there are "No re-engagement notifications of any kind" (Spec:236) and the app must ...
 507  notify                   OQ     ... Concept:156 contrasts the reveal with "an unlock notification with nothing to do". Where does "Your Jour...
 507  remind                   OQ     ...s of any kind" (Spec:236) and the app must never "Remind a user … to return" (Spec:242)? Concept:156 contr...
 511  count (any)              OQ     ...wing a reader the photos they appear in lets them count them and infer their ring (5+ tight, Spec:161). O...
 514  left                     OQ     ...22. **"Reflection left" on a public photo reaches everyone.** It goes to...
 516  unread                   OQ     ...5 minutes after capture" (Spec:281). The photo is unreadable at once, even to the owner (Spec:234, Proposa...
 517  count (any)              OQ     ... the camera offered at all? Spec:243 bans a quota count "in a way that reads as a target", which leaves r...
 517  count (any)              OQ     ...target", which leaves room for some other kind of count. Proposal:49 returns no number at all. Affects S-...
 518  left                     OQ     ...it ends? Proposal:49 forbids returning highlights left. The window itself is not addressed. Affects S-02...
 519  counter                  OQ     ... the unlock date (Proposal:84). Is "in 64 days" a counter under Spec:233? Affects S-03....
 519  days to go / in n days   OQ     ... owner may see the unlock date (Proposal:84). Is "in 64 days" a counter under Spec:233? Affects S-03....
 521  follower                 OQ     ...29. **The "follow-up".** Spec:195: "the original moment, then the f...
 521  follower                 OQ     ...w-up".** Spec:195: "the original moment, then the follow-up". Concept:569: "the follow-up photo or memory ...
 521  follower                 OQ     ...al moment, then the follow-up". Concept:569: "the follow-up photo or memory that came later". The data mod...
 521  follower                 OQ     ...s no link between photos (Proposal:86–99). Is the follow-up only the reflection stack? Affects S-17....
 522  popular                  OQ     ...ratitude tags? (c) In what order, since "never by popularity" (Spec:202) names no other? (d) Does a photo s...
 526  new                      OQ     ...screen opens the app in each time state? Only the new user's day one is stated (Spec:30). Concept:438–4...
 528  streak                   OQ     ... reflecting on drift)? A count may fall under "No streaks, counters" (Brief:42). Affects S-07....
 528  counter                  OQ     ...ng on drift)? A count may fall under "No streaks, counters" (Brief:42). Affects S-07....
 528  count (any)              OQ     ...r member"; Concept:407 on reflecting on drift)? A count may fall under "No streaks, counters" (Brief:42)....
 534  comment                  PROSE  ...-18). The tone of chapters (S-19). "Readable, not commentable" and final choices (S-20). Finishing the reve...
```

### B.2 Scan 2 (rubric grep aids)

```
=== R-006  /moments? captured|[0-9]+ *(photos?|moments?|frames?|shots?|pictures?)|of [0-9]+|frames? (left|used|remaining)|so far/
70:Import of a photo not taken in the app (Spec:53). Frames used or left (Proposal:49; Spec:243) |
105:ils" (Spec:75). "Not thumbnails, not counts, not '3 moments captured'" (Brief:46). Frames used, frames left, 
293:unlock (Proposal:133) | Highlights left or used: "Frames used, frames left and highlights left are counted insi
502: floor". 12 is outside that range, and the middle of 24–48 is 36. Concept:799 still says "Frame range 24–
=== R-013  /days? (left|to go|until|remaining)|unlocks? in|countdown|time left|[0-9]+ *d *[0-9]+ *h|in [0-9]+ days|ends in/
71: left, highlights left (Proposal:49). Whether the time left in the window may show is OQ-26 |
519: owner may see the unlock date (Proposal:84). Is "in 64 days" a counter under Spec:233? Affects S-03.
=== R-098  /left this month|remaining|of (12|24|48)|[0-9]+ (more|to go)/
502: floor". 12 is outside that range, and the middle of 24–48 is 36. Concept:799 still says "Frame range 24–
=== R-099  /%|complete|[0-9]+ of [0-9]+|completion/
125:r" (Spec:127). A reminder to finish (Spec:242). A completion bar: "No streaks, counters, progress bars, remind
=== R-095  /don't forget|remember to|you haven't|come back|we miss|still have|waiting for you|ending soon|last chance|nudge/
231: a prompt to capture a low point: "invited, never nudged" (Spec:209). Likes, reactions, views or counts (
=== R-096  /unread|badge|isNew|new|seen_at|read_at|dots?|marker/
19: journeys** (the last journey has unlocked and no new Commit yet, as Long Way Round). Commit is open. I
38:-engagement notifications" · "No ranking, levels, badges or leaderboards" · "No photo feed" · "Nothing le
38:ly, like, reaction, caption, score, rank, streak, badge, view or follower" (Proposal:180). The tables bel
105: capture or which months have photos, since it is unreadable (Proposal:48, 50). Any note (sealed, Proposal
123:d` | Not reachable | Anything: "Sealed content is unreadable by the owner, not merely hidden in the UI" (S
142::694) | "no scores, no levels, no leaderboard, no badges, no comparison between users" (Spec:185). Anythi
145:| `reveal-finished` | A new ring: "one ring per journey whose reveal is finis
150:- **Copy:** the young circle of a new user `[copy: copywriter]`
188:twork" (Spec:150; see OQ-4). "No ranking, levels, badges or leaderboards" (Brief:44). Whether past rings,
207:| `later-years` | "Reflection left" for new slot reflections | |
222:own state changes nothing: the same feed serves a new user (Spec:30) and a user in a sealed year (Conce
258:- **Viewer:** owner (new user)
330:| `later-years` | A new overview for slot *k*. The stack, readable back t
351:| `reveal-finished` | The new ring. The journey by locked visibility | As above
354:0, Spec:278). "scores, … levels, … leaderboard, … badges" (Spec:185). Follower or view counts (Proposal:1
434:eveal S-04. **Leads to:** Profile (own) S-05 (the new ring)
499:ots open on the owner's earlier journeys during a new sealed year (Proposal:294: lantern-1 slot 5 on 20
516:5 minutes after capture" (Spec:281). The photo is unreadable at once, even to the owner (Spec:234, Proposa
526:screen opens the app in each time state? Only the new user's day one is stated (Spec:30). Concept:438–4
=== R-071  /inner circle|inner ring|closest|close friend|your ring|moved (in|out|closer|further)|where you appear|appear/
38:**Applies to every screen.** None of these ever appears, in any state, for any viewer (Brief:37–47, Spec
144:`reveal-open` | The year's activity graph may now appear: "only after the year unlocks" (Spec:187). Whethe
144:r its ring and twisted line appear now or at finish is OQ-6 and OQ-7. The way into R
166:e access" (Proposal:288). How the tagged reader's appearances are shown, given layer invisibility, is OQ-1
188:enu, not a list" (Spec:159). Extra access for the inner ring: close friends "see nothing beyond the rest of th
188: past rings, drift history or shared-photo counts appear is OQ-36.
228:gs (Proposal:317). Whether the photo image itself appears is OQ-11 | Ordering by popularity: "never by pop
354:at all (Spec:164, Spec:235). Extra access for the inner ring (Spec:150, Spec:278). "scores, … levels, … leader
422:chooses (Spec:151). Each set once (Spec:286) | A "close friends" level: they "see nothing beyond the rest of the
493:4. **Close friends.** Concept:807 says "close friends get everything"; Concept:381–383 says close frie
496:e activity line is twisted in, and when the graph appears.** Spec:186 says "at the end of the journey", Sp
507:es "Your Journey is ready" (Plan:79, Concept:740) appear? Is `unlock-day` a distinct state at all, given t
511:19. **"Where you appear" and layer invisibility.** Spec:196 and Concept:5
511:70 say the reader sees where they appear in someone's journey. Spec:164 and Spec:235 say n
511:rns their layer. Showing a reader the photos they appear in lets them count them and infer their ring (5+ 
=== R-083  /lost|dropped|demoted|unfriend|fading|drift/
188: or leaderboards" (Brief:44). Whether past rings, drift history or shared-photo counts appear is OQ-36.
191:- **Copy:** drift outward, framed as expected: "treated as a featur
528:** Does the owner's map show past years' rings or drift, or the number of shared photos (Proposal:150: "T
528:t entry per member"; Concept:407 on reflecting on drift)? A count may fall under "No streaks, counters" (
534:. Finding yourself in someone's hard year (S-06). Drift, and the empty map (S-07). The three announcement
=== R-102  /top|ahead|behind|veteran|elite|achievement/
142:s is OQ-6). "A person who joined this year is not behind; their circle is simply younger" (Concept:694) | 
145:to the circle (Spec:186) | A ring presented as an achievement: "A record, not a rank" (Spec:185) |
=== R-028  /abandon|cancel|quit|pause|end early|restart|start over/
55:k 3) | A second Commit. Any way to change type or abandon: "It cannot be changed for that year" (Spec:44), 
55:"No abandoning" (Spec:263) |
105:a bad moment" (Spec:209). A way to change type or abandon (Spec:44, Spec:263). A second Commit (Spec:273) |
=== R-031  /retake|re-take|try again|redo|discard|undo|use photo|re-photograph/
38:, for any viewer (Brief:37–47, Spec:226–247): "No retakes" · "No edits to reflections" · "No comments from
46:journey types and presses Commit, which cannot be undone.
70:e only result is accepted (Proposal:49, 97) | "No retakes" (Spec:55). "no review-before-save" (Spec:228). 
77: the capture refusal `[copy: copywriter]`. The no-retake line "No retakes. That moment is gone." (Brief:12
282:kip `[copy: copywriter]`. Whether the page can be re-photographed before saving is OQ-24
439: Done. It cannot happen twice (Proposal:164) | An undo |
516: photo inside the 15 minutes? And can the page be re-photographed before it is saved ("written once", Spec:16; "N
516:o retakes", Spec:55)? Affects S-12, S-03.
534:and button (S-01). The capture refusal and the no-retake line (S-02). The sealed state (S-03). "Your Journ
=== R-016/019  /edit|delete|remove|replace|trash/
38:r (Brief:37–47, Spec:226–247): "No retakes" · "No edits to reflections" · "No comments from anyone else"
125:fore the reveal is finished" (Spec:286). A way to edit or delete a photo: "A photo can never be deleted"
302:or the current slot, added to the stack and never edited.
313:On every state, never: an edit or delete: "Immutable. No edits, ever" (Spec:99). Anyone el
332:On every state, never: an edit: "Immutable, like everything else" (Spec:120). A 
373:). A caption: "There's no caption" (Proposal:94). Edit or delete (Spec:266). Access through being tagged
388:on anywhere in the pipeline" (Spec:231). A way to remove a set tag (Spec:286). Any hint of where the tagge
=== R-104  /autoplay|endless|infinite|more like this|refresh|scroll/
166:n order, not as a grid" (Spec:193). An effortless scroll into it: "It must not be as effortless as scrolli
=== R-124-extra  /level up|points|trending|followers|new!|days to go|frames left/
105:ot '3 moments captured'" (Brief:46). Frames used, frames left, highlights left (Proposal:49). The year's activi
293:sal:133) | Highlights left or used: "Frames used, frames left and highlights left are counted inside them and n
```

### B.3 Scan 3 (deferral words)

```
3:lan.md:65`): every screen the app needs, named, nothing designed yet. Phase 2 writes the flows from this list and Phase 4 builds the screens from i
15:shows each in its own state: at baseline Steady Lantern has #1–#5 in `later-years` and #6 `sealed` (Proposal:218–223).
19:the last journey's `unlock-day`, `reveal-open`, `reveal-finished` or `later-years` | Spec:30, Spec:273 (§20 C), Proposal:16 (D3), Proposal:209–21
26:| `later-years` | `now ≥ unlock + 1 year`: reflection and overview slot *k* ≥ 
26:2. Two variants: `later-years · finished` and `later-years · never finished` (Long Way Round #4 from 2027-09-06) | Spec:27
56:| `unlock-day`, `reveal-open`, `reveal-finished`, `later-years` | Only through `no-journey` · between journeys (above) | As ab
71:t, highlights left (Proposal:49). Whether the time left in the window may show is OQ-26 |
93:| 4 | The unlock date. Whether it may be shown relative to today is OQ-27 | Proposal:84 |
101:k like a fault. The emptiness is the product (Brief:130; `ux.md:21`). Phase 2 and the copywriter make it read that way. This file does not.
106:| `sealed · highlight open` | Elements 1–8. Whether the open window may show is OQ-26 | As in `sealed`, and highlight photos taken or left (Propos
125:ounters, progress bars, reminders" (Brief:42). The album order step: "Optionally orders the physical album (phase 2)" (Spec:89) is the album phase, 
127:| `later-years · finished` | As `reveal-finished`, with slot *k* open for Refl
128:| `later-years · never finished` | Photos still Network, no chapter, no tags (
144:| `unlock-day`, `reveal-open` | The year's activity graph may now appear: "only after the year unlocks" (Spec:187). Whether its ring an
146:| `later-years` | Rings accumulate. The overview stack, readable back to back 
147:journey` · between journeys | As `reveal-open`, `reveal-finished` or `later-years` for the last journey, plus the way to Commit S-01 | As above |
154:ing to now, in order, with the hard times and the reflections written later.
162:unlock-day`, `reveal-open` | Owner: every photo. Network: every photo not yet set Private, because Network is the default (Spec:151, Proposal:311: 
164:| `later-years` | As `reveal-finished`, with deeper reflection stacks and an o
186:| `later-years` | Unchanged until the next finished reveal | |
207:| `later-years` | "Reflection left" for new slot reflections | |
217:- **Purpose:** reflections written years later on other people's hard moments, filtered by tags of endurance and gra
229:| `later-years` | The same, with reflections written years after the moment, w
263:(Spec:13); when and how it is set is OQ-31 | A way to change the name later: "Set once, immutable" (Proposal:61). A yearly name: "Decided 2026-10
270:- **Purpose:** straight after capture, an optional, skippable offer to photograph a handwritten A4 page, which becomes t
311:| `later-years` (either variant) | Slot *k* open. Earlier reflections read-onl
328:| `unlock-day`, `reveal-open` | Slot 1 overview may be written. Optional (Spec:285) | A requirement to write one before finishing: "A reveal c
330:| `later-years` | A new overview for slot *k*. The stack, readable back to bac
352:| `later-years` | Rings, and the overview stack for network viewers | As above
371:| `later-years` | The reflection stack grows by at most one per slot (Spec:97)
389:| `reveal-finished`, `later-years · finished` | Tags, read-only (Spec:276) | Any change |
390:| `later-years · never finished` | OQ-16 | |
406:| `reveal-finished`, `later-years · finished` | The tags, read-only | Any change (Spec:276) |
407:| `later-years · never finished` | None: "There's no chapter, no tags" (Spec:2
423:| `reveal-finished`, `later-years · finished` | Visibility, read-only (Spec:276) | Any change |
424:| `later-years · never finished` | Every photo stays Network (Spec:269). Wheth
439:| `reveal-finished`, `later-years · finished` | Done. It cannot happen twice (Proposal:164) | An 
441:| `later-years · never finished` | OQ-16 | |
477:ring, the physical album, print-shop ritual. Spec §7 step 6 calls it "phase 2"; that is the business stage, not a build phase | Spec:89, Spec:213–2
508: is still possible. Can visibility, tags and chapter still be set in `later-years · never finished`? Affects S-04, S-18–S-21.
509:17. **What must be done before finishing.** Overviews are optional (Spec:285) and reflections are optional (Spec:102). Is a chapter requ
521:the follow-up". Concept:569: "the follow-up photo or memory that came later". The data model has no link between photos (Proposal:86–99). Is the 
```
