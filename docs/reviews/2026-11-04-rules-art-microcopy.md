# Rules audit: Art-Direction.md and Microcopy.md

Date: 2026-11-04. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (not edited in this run, by instruction). Targets: `docs/Art-Direction.md` (AD), `docs/Microcopy.md` (MC), both uncommitted Phase 2 deliverables. `docs/Flows.md` is audited separately and was read for context only.

**Verdicts.** `Art-Direction.md`: **FAIL**. `Microcopy.md`: **FAIL**.

**The three that matter most**

1. **ART-1.** Under B5's option, the flat graph positions each rise by days since the commit date, and a public viewer gets that graph. With one capture date, which they may read, they can work out the commit and unlock dates, which they may never read. The same graph ending at finish tells them the reveal state.
2. **ART-3.** `Art-Direction.md` §12 creates ten "drawn until answered" behaviours outside `Decisions-Needed.md`. A builder cannot label them: `PROVISIONAL: AD-1` fails R-149.
3. **COPY-2.** The capture screen shows "One press, one photo." and "No photo was taken." together.

The envelope rules (§5), the layer map and the six approved lines all held up. See "Tested and clean".

Short names: **FS** Functional-Spec, **SI** Screen-Inventory, **DN** Decisions-Needed, **P1** Phase-1-Proposal, **CL** CLAUDE.md, **MJC** My-Journey-Concept.

---

## Checks run

No automated script exists for paper deliverables. These are the rubric's own greps, run by hand from the repo root. Long lines are cut. Every hit was then read.

Graph first, as the rule requires. `graphify query` ran on "rings progress level score achievement", "activity line who sees non-owner", "sealed envelope leak", "layer shown to person", "microcopy refusal lost press" and "no relative time unlock date". It was used only to find sections. It does not yet hold either target beyond the agent-brief references, so nothing below rests on it.

```
# R-131: six lines, exact string (grep -cF)
It's not about attention. It's about intention.    | AD:1 MC:2
You've come further than you think.                | AD:1 MC:2
Strict at capture. Generous at reflect.            | AD:1 MC:2
No retakes. That moment is gone.                   | AD:1 MC:2
This app takes time, like many other good things.  | AD:1 MC:3
We want you here less, not more.                   | AD:1 MC:5

# R-006 (a)
$ grep -nE 'moments? captured|[0-9]+\s*(photos?|moments?|frames?|shots?|pictures?)\b|\bof [0-9]+\b|frames? (left|used|remaining)|so far' docs/Microcopy.md
46: M-01 (type descriptions)          -> reviewed: tested below, allowed on S-01
134: M-22 source note ("No 'yet' or 'so far'") -> not product copy
$ (same) docs/Art-Direction.md
262: "clear of 3 and 9 o'clock"       -> false positive

# R-013 with C2's additions, plus 'today', 'next year', 'yet'
$ grep -nEi 'days? (left|to go|until|remaining)|unlocks? in|countdown|time left|next month|\bsoon\b|in a few weeks|this winter|from today|\btoday\b|tomorrow|next year|\byet\b' docs/Microcopy.md
47, 51, 52: M-02 and both alternatives, "12 months from today"   -> COPY-1
3, 61, 99, 119, 134, 159, 217: source notes or prose, not product copy
$ (same, without 'yet') docs/Art-Direction.md
549: the "Do not" column               -> fine

# R-095, R-097
$ grep -nEi "don't forget|remember to|you haven't|come back|we miss|still have|waiting for you|ending soon|last chance|streak|in a row|chain|consecutive" docs/Microcopy.md
86: M-10 source note ("'Waiting for you' and 'safe' are avoided") -> not product copy
$ (same) docs/Art-Direction.md
(no output)

# R-102, R-124
$ grep -nEiw 'level|rank|top|ahead|behind|veteran|elite|achievement|earned?|earn|congrat[a-z]*|well done|score|badge|points|tier|reward' docs/Microcopy.md
133: M-21 "Your map is earned, not chosen"  -> COPY-4
142: M-23 source note ("behind")            -> not product copy
$ (same, plus tiers|established) docs/Art-Direction.md   (25 lines)
193-195: state names Young / Established / Many -> ART-6
96: "Never a jump between tiers"                -> ART-6
245: "cannot read as a status badge"            -> ART-5
the rest: bans in "Do not" columns, or unrelated ("not established", line 526)

# R-083, R-124 remainder
$ grep -nEi 'lost|dropped|demoted|unfriend|fading|retake|try again|comment|delete|unread|new!|trending|popular|likes|followers|publish' docs/Microcopy.md
34, 60: "No retakes"      -> approved line, placed by SI:104 and CL:134
103: M-15 "commentable"   -> FS §11's words, a refusal
38, 77, 78, 176, 208, 209: source notes or prose

# R-136
$ grep -nE 'Overview\.md' docs/Art-Direction.md docs/Microcopy.md
AD:610 "Not used", MC:5 "never cited"     -> pass

# Carriage of WW and TT (R-165, R-161)
$ grep -nE '\bWW\b|TT\b' docs/Art-Direction.md
598: named only as one side of a disagreement  -> ART-2

# R-150 step 1, table IDs with no label in the file
AD: B1 B10 B11 B12 B13 B14 B17 B18 B19 B2 B20 B21 B22 B23 B24 B25 B26 B6 B7 B9 C1 C10 C11 C12 C13 C14 C15 C16 C2 C3 C4 C5 C6 C7 C8 C9
MC: B10 B11 B15 B18 B2 B20 B21 B22 B23 B24 B25 B26 B4 B5 B8 C12 C13 C14 C15 C16 C2 C3 C6 C7
    (MC's B4, B10, B11, B18, C2 are false hits: the label column writes a second ID in bare form.)
    Read against each file: AD touches B7, B8, C1, C2, C8, C9 without the label (ART-10). MC touches B2 and C12 without it (COPY-5, COPY-6).

# R-149 step 1, malformed labels
AD:8 and MC:7 only: each legend's `PROVISIONAL: <ID>`   -> pass

# Contrast in the rubric or plan
$ grep -nEi 'WCAG|contrast|aria-hidden|accessib' docs/Rules-Rubric.md docs/Build-Plan.md
Rules-Rubric.md:1508, unrelated. No rubric check covers contrast.

# Recomputed AD §3.2 and §8 by script
ink/page 13.08, 14.51 (AD:416, 432 agree). 32% band 1.93, 2.60 (AD:461 agrees).
 n  pitch  stroke  tone(w/p)  outer R  day-mark height  stroke at 240 px display
 1  7.00   1.25    17.9%       95      1.90             0.94
 5  7.00   1.25    17.9%      123      1.90             0.94
 9  7.00   1.25    17.9%      151      1.90             0.94
10  6.40   1.25    19.5%      152      1.79             0.94
16  4.00   1.25    31.2%      152      1.12             0.94
17  3.76   1.20    32.0%      152      1.05             0.90
25  2.56   0.82    32.0%      152      0.72             0.61
40  1.60   0.51    32.0%      152      0.45             0.38
80  0.80   0.26    32.0%      152      0.22             0.19

# MC's count table
30 tags in Flows, less the legend = 29 markers. 39 recommended strings: recounted by hand, correct.
```

---

## Findings: Art-Direction.md

### ART-1. The public flat graph gives the commit date, and its ending gives the reveal state
- **Checks:** R-152, R-162, R-144. FS §20 T (`FS:296`), SS (`FS:323`), EEE (`FS:338`), ZZ (`FS:333`).
- **Where:** `Art-Direction.md:137`, `:158`, `:162`, `:180`, `:585` (AD-6).
- **What is wrong, part 1.** AD:137 sets day 0 to the commit date. AD:158 places each rise at `x = 10 + 300·(d + 0.5)/N`, with `d` counted from that day. AD:180 gives this graph to a public viewer under B5's option, from photos they can read. They can read a photo's capture date (FS §20 GG). So `commit date = capture date − d`, and the unlock date follows.
- **Why it breaks the rule.** A public reader never reads either date (R-152). EEE allows narrowing journey dates from dates the reader already holds, but R-152's EEE line still fails "a screen or reader that adds a new date field for a public reader, or computes the bracket for them". This graph does more than narrow: one rise gives the exact day. To draw it, the reader must also return `d` or `committed_at` to a public viewer. SI:412 asks for a graph "no finer than one day" and names no anchor. The anchor is this file's choice, and it is the leak. The network row (AD:178) is fine, because the network reads dates (§20 T).
- **What is wrong, part 2.** AD:162 and AD-6 (AD:585) draw the flat graph "from unlock until finish, then the ring alone", "as SI's rows read". On S-16 the graph is listed only in the `unlock-day`, `reveal-open` row (SI:420). So a public viewer sees a graph on an unfinished journey and none on a finished one.
- **Why it breaks the rule.** ZZ lists what a public reader may infer the reveal state from: the Positivity Feed, rings and photos appearing. R-162 says "the paths in G-23 may differ between #3 and #4, and nothing else may". A graph that disappears is not on that list. AD:574 says each drawn state is "always the strictest reading". Here it is not.

### ART-2. "Same ring geometry for every viewer" drops §20 WW, which protects the join date
- **Checks:** R-161, R-165 (3), R-143, R-166. FS §20 WW (`FS:330`), TT (`FS:324`). SI:174, SI:412.
- **Where:** `Art-Direction.md:172`, `:90`, `:174–180`, `:598`.
- **What is wrong.** AD:172 says "Every viewer gets the same frame, the same name and the same ring geometry." AD:90 says "The drawing does not change with the setting, except as AD-2 says." Under B4's "per year with the app", the owner sees per-year rings on S-05 and everyone else sees one ring per finished reveal. The geometry therefore differs by viewer. The §3.6 table has no B4 column. WW appears only at AD:598, as one side of a doc disagreement, and it is a ruling limiting the option.
- **Why it breaks the rule.** A build following AD:172 with the switch flipped draws per-year rings on S-16, and that hands every viewer the join year, which TT and R-161 forbid.

### ART-3. §12's "drawn until answered" is a second list of defaults, outside Decisions-Needed
- **Checks:** Rule zero (`CL:19–24`), R-134, R-149, R-150.
- **Where:** `Art-Direction.md:9`, `:574`, `:580–589`. Stated flat in the body at `:129`, `:162`, `:168`, `:172`, `:177–182`, `:264`.
- **What is wrong.** CL:20–21 gives a builder two options: build a provisional default from `Decisions-Needed.md`, or stop and ask. AD-1 to AD-10 are not in that table, yet each has a state the build draws. CL:23 requires a label in the code, and R-149 step 1 rejects anything but `[BC]n`, so `PROVISIONAL: AD-1` fails. AD:574 says these are "not a decision", but the body reads as settled: AD:182 "two people with the same number of rings have identical rings", AD:129 "so a ring is only ever added outside", and §11 check 3 tests AD-1's state.
- **Also wrong.** AD:574 says the drawn state is "always the strictest reading". AD-9's "Outermost" (AD:588) is a geometry convenience. AD-6's state is worse than the alternative (ART-1). AD-5 draws nothing for a long name.
- **Why it breaks the rule.** Raising a question is right. Attaching a buildable behaviour to it, with no ID the build can carry, is what rule zero stops. AD-1's own strict state may well be right. The route to it is the violation.

### ART-4. `[AD]` is used to settle behaviours
- **Checks:** R-134, CL:17. AD:7 and AD:9 state the file's own rule.
- **Where and what:**
  - `:44`, `:50`: on which screens rings appear, "and nowhere else". The label admits it rests on lines that do not say so (Spec:185 and Concept:692 ban comparison, not a display size).
  - `:127`: rings are never labelled "for anyone else" (owner and network). This settles what an owner can learn from their own circle. The network reads journey dates under §20 T, so it is not a sealing need. No AD-n covers it.
  - `:243`, `:245`: whether and where a sealed journey is drawn on S-16 and S-06 ("where it needs a drawing", "sits where that journey would sit"). This is screen structure, which AD:3 disclaims, and S-16's `sealed` row (SI:419) names no such place. See ART-5.
  - `:269`: an empty layer ring is not drawn on a partly filled map. Flows:455 says "three rings around them". When the last person drifts off a ring, that ring vanishes, which is a visible event in a map that "shows no drift" (C8). No AD-n covers it. AD-7 asks only about names and busy maps.
- **Why it breaks the rule.** The label is allowed for colour, type and geometry. These decide who sees what, on which screen and when.

### ART-5. "It cannot read as a status badge" is not true and is not tested
- **Checks:** R-126, R-008, FS §20 I (`FS:279`), R-134.
- **Where:** `Art-Direction.md:243`, `:245`.
- **What is wrong.** A 56 × 39 picture beside a person's name, present for those with a journey under way and absent for those without, is what a status badge looks like. Moving it "where that journey would sit" does not change that for a profile with no earlier journeys, because nothing else is there. §11 has no check for the claim. "Where it needs a drawing" also leaves the choice of drawing or words to the builder.
- **Why it breaks the rule.** The fact itself is allowed (§20 I). What is not allowed is a stated guarantee with nothing behind it, on a profile where "nothing signals how well they are doing". The drawing adds no information beyond the flag, so this is not a leak. A watcher can read the commit and unlock days from when the flag flips, but that comes from the flag and not from this file (R-008 weakest point).
- **Also.** AD:224's "one fixed image" and AD:243's smaller variant without the mark are two images. Neither varies by content, so this is wording only.

### ART-6. Rings get bigger and darker with count, and the state table names tiers
- **Checks:** R-102, R-143, MJC:693 ("no tier name"), art-director brief ("Rings must never read as a progress bar").
- **Where:** `Art-Direction.md:96`, `:98`, `:123`, `:124`, `:193–195`, `:367`, `:404`, `:538`, `:540`.
- **Tier names.** AD:193–195 divide ring count into **Young** (1–3), **Established** (4–9) and **Many** (10+), and the geometry changes at the same boundary. "Established" is a status word. These names will reach code and fixtures from this table. AD:96 uses "tiers" itself.
- **Size.** AD:540's heading "Age is not size" is false for 1 to 9 rings: outer radius goes 95, 102, … 151, in equal steps. AD:123 says "size stops saying anything early on", but the fixtures hold at most 5 revealed journeys (`P1:207–208`), so every fixture circle differs by size alone.
- **Weight.** AD:538 says "One weight and one colour for every ring and every number of rings". The stroke falls from 1.25 to 0.26 by formula. AD:98 concedes the rest: "from 17 rings on, the tone stays constant". Below 17, tone rises from 17.9% to 32%, so more rings do read as heavier, which AD:195 denies.
- **Meter.** AD:124 says "A meter needs a container, and without one there is nothing to fill." The fixed 320 box and the 64-unit band, with its own token `--mj-ring-band` at AD:367, are a capacity reached in equal steps at exactly 9 rings. AD:404 says no meter tokens exist.
- **Why it breaks the rule.** Growth itself has a source (MJC:687, MJC:700), so a growing circle is not the violation. The violation is the tier vocabulary, and §10 stating as rules things its own formulas contradict. Those are the rules Phase 6 will audit against.

### ART-7. "The type never shows" is false once marks are drawn, and density reads as a score
- **Checks:** R-102, `CL:89–93`, the file's own AD:148, AD:151, AD:541.
- **Where:** `Art-Direction.md:139–151`.
- **What is wrong.** Each rise spans about 8 days. An Explorer's 48 normal photos, evenly spread, sit 7.6 days apart and merge into a nearly unbroken raised line. A Contemplator's 12 sit 30 days apart as separate bumps, and a Contemplator cannot have more than 13 such days. So the ring shows the type, and the harder type looks sparser. "No peak to be proud of" (AD:148) holds, but fullness replaces peaks, which is what a contribution graph is read for. A clean ring beside a busy one (AD:150) visibly marks an empty year.
- **Why it matters.** This is owner-only and after unlock under the default, so it does not break the banned list today. It contradicts two stated rules, and it becomes exposure if AD-1 is answered yes for the network. The user should see it before answering AD-1.

### ART-8. The navigation marks add a way to Capture that no doc names, and skip ways that do exist
- **Checks:** R-134, R-095, R-104, R-138, R-168.
- **Where:** `Art-Direction.md:285–290`, `:295`, `:296`, `:548`.
- **What is wrong.**
  - AD:289 gives Capture a navigation mark. Flows:509 does not list it, and S-02 is reached from S-03 and S-13 only (SI:89, SI:170). A standing camera mark is the "+" of every other photo app, and it is an invitation to capture.
  - In `no-journey`, S-02 is "not available" (SI:100). The mark then has to be hidden, or lead nowhere, or be disabled, which AD:404 rules out and AD:296 does not allow ("two appearances and no more").
  - AD:285–290 have no mark for S-01, S-04, S-06 or S-15, which Flows:509 does list. AD:295 discusses Commit and Reveal as ways with no mark given.
  - Flows:509's S-04 way appears "when one is open". A way that appears on the day a reveal opens is a marker, whatever it looks like. AD:548 says "A way looks the same every day" and does not address appearing. AD-10 does not raise this.

### ART-9. The contrast shortfall is "accepted" with a false reason, and is not listed as a question
- **Checks:** R-134, the file's own AD:9. No rubric check covers contrast (grep above), so the number itself is not a rule violation.
- **Where:** `Art-Direction.md:461`.
- **What is wrong.**
  - It says "accepted as [AD] for the user to review", but §12 does not list it. The user cannot review what is not on the list, and "accepted" is not the art director's word to use for something below the file's own 3:1 line (AD:410).
  - "Nothing can be read or operated through telling those rings apart" is false for the owner. Their day marks live on those rings (AD:176). At 40 rings the mark height (0.45) is less than the stroke (0.51), so the owner's activity record is lost in the blur.
  - "From about 40 rings" is measured at 320 px, but AD:56 allows 240 px, where the stroke falls to 0.6 px by 25 rings.
- **What holds.** The figures 1.93 and 2.60 are right. Decades of rings is true of any real user.

### ART-10. Provisional defaults cited without the label
- **Checks:** R-150, `CL:23`, the file's own AD:8.
- **Where:** B7 `:404`. C2 `:496`, `:549`. C8 `:270`, `:545`. C9 `:192`, `:201`. B8 `:148`, `:541`. C1 `:406` ("Your Journey is ready", no ID). B4's default stated as fact at `:198` and `:199`.
- **What is wrong.** Each rests on a default and reads as settled. AD:48 is correct to write "DN C7, decided", which is why "DN C9" alongside it reads as if it were decided too.

### ART-11. "It adds no colour change to the image" is false
- **Checks:** R-134. AD:30, AD:32.
- **Where:** `Art-Direction.md:520`, `:331`.
- **What is wrong.** `--mj-film-sheen` lays white at up to 10% over the photograph, which lifts every pixel it touches. AD:32 says "Photos keep their own colours" and no filter is applied, and AD:30 says no gradients as decoration. The plastic sheet has a source (MJC:309). The claim that it changes nothing does not. Low severity. Stated so the user can decide with the facts.

### ART-12. The status line names no §20 range
- **Check:** R-165 (2).
- **Where:** `Art-Direction.md:3`. AD:608 says §20 was read, with no letter range and no statement of why later letters do not bear. Low severity. The same is true of `Microcopy.md:3` (COPY-9).

### Weakest points in this file (not violations)
- **The activity line and R-154, R-151.** Same-height rises hide a highlight in the graph, but the residual stays: 19 same-dated photos still suggest one, to anyone reading dates.
- **AD-2 blocks a switch that must work.** B4's option has no ring date (AD:581), and R-143 sends that to the supervisor. Correctly raised, but it means the switch cannot be flipped in full.

---

## Findings: Microcopy.md

### COPY-1. M-02's "12 months from today" is a relative form of the unlock date, and the note argues it away
- **Checks:** R-013 (Rubric:157), C2 (`DN:40`), SI:52 ("No countdown or relative date to any unlock", on every screen), R-135, CL:24.
- **Where:** `Microcopy.md:47`, `:51`, `:52`.
- **What is wrong.** R-013 under C2 says "any relative form of the unlock date fails". MC:47's note says "C2 governs the date of a running year". C2's row and SI:52 do not say that: the limit is the copywriter's. The wording comes from the marker (Flows:156), so the two sources disagree, and CL:30 says cite both and raise it. It is not in the Open questions, and no `PROVISIONAL: C2` label sits on the entry.
- **Fairness.** It does not tick and it is the same on every date, so it is not a countdown. Length can be said without "today" ("A journey runs 12 months", CL:87). CL:24 says the strictest reading wins when unsure. Flows:156 needs the same ruling, and it is outside this audit's target.

### COPY-2. "One press, one photo." and "No photo was taken." show together
- **Checks:** R-168, R-134. SI:94. FS §20 U, QQQ.
- **Where:** `Microcopy.md:60`, `:61`.
- **What is wrong.** M-03 sits on the camera "unchanged in every state". M-04 shows on the same camera after a refusal (Flows:200: "back to the camera"). So the screen says "One press, one photo. No retakes. That moment is gone." beside "No photo was taken." Both claims are about the same press and only one is true. M-03's note also contradicts itself: "unchanged in every state", then "never after a press". The camera returns after every note step, so M-03 is on screen after a press every time. The approved half, "No retakes. That moment is gone.", is not at fault. "One press, one photo." is the addition, taken from Flows:190.

### COPY-3. M-10's "Nothing has gone wrong and nothing is missing" makes a claim about the contents of a sealed year
- **Checks:** R-009 and B19 (`DN:38`: the owner sees type and dates "and nothing else"), R-134, FS §20 DDD, HHH.
- **Where:** `Microcopy.md:86`, and alternative `:90` is clean.
- **What is wrong.** The note says the line "says nothing of photos", and that "safe" and "waiting for you" were avoided "since each implies contents". "Nothing is missing" implies contents in the same way. It is also not always true. After a lost press (DDD) or a lost page (HHH) something has gone wrong and something is missing, and the app cannot check this. A rejected "safe" with an accepted "nothing is missing" does not hold together.
- **What holds.** The line is the same for everyone at all times, so it is not a leak by variation. Alternative 1 meets the same need without the claim.

### COPY-4. "Your map is earned" turns a description of the map into an achievement
- **Checks:** R-102, CL:71, SI:176 and AD:551 (both ban "you earned" for rings).
- **Where:** `Microcopy.md:133`, read with `:134`.
- **What is wrong.** Spec:160's "Earned, not chosen" describes how layers are computed, and Flows:455 has "closeness is earned". M-21 changes the subject to "**Your map** is earned", which reads as something the owner achieved, and a bigger map as more earned. M-22 follows with "Your map is young. It holds just you.", which puts a stage in front of it. The doc set treats "you earned" as banned reward language for the owner's rings, and the same owner sees both kinds of ring. It names no level, so this is a strict-reading finding (CL:24), but the fix costs nothing: keep the subject Flows:455 gives. The rest of M-21 is sound ("Moving outward is expected" is what SI:243 asks for, and R-083 passes).

### COPY-5. M-17 goes past its marker, misreads under B2's default, and uses a word B1 does not
- **Checks:** R-150, R-134, B1, B2 (`DN:20–21`), the file's own MC:7, MC:38.
- **Where:** `Microcopy.md:105`, `:224`.
- **What is wrong.**
  - The marker (Flows:355) says "Say the choices lock". The second sentence, "The people on your map are told your journey is out", is added, and Q-8 raises only what it leaves out.
  - It reads differently under B2's two settings. Under the default the network has read the journey since unlock, so "out" at finish misleads. MC:7 says an entry gives wording for both settings where they differ. B2 is not labelled.
  - "Out" is a third word. MC:38 fixes "launched" and "finish". Its source, Concept:722, is a note on the product name.
  - "Told" suggests a message reaching someone, but a feed line is only read if they open the feed (C15, R-094).
  - It gives one of two things that go out at that moment. Q-8 says names are left out "because the setting is switchable", but an owner reading this takes it as the whole list.
- **What holds.** "Choice", "as it stands", no ring, no praise. The first sentence is good.

### COPY-6. M-23's second line fills in what Q-5 says is open, and does not do the job it was placed for
- **Checks:** R-134, R-130, R-095 under C9, R-150, the file's own MC:9.
- **Where:** `Microcopy.md:142`, `:221`, `:223`, `:9`.
- **What is wrong.**
  - No doc places "We want you here less, not more." on S-05. R-134 says raised, not filled in. Q-5 raises it and the line is written in anyway.
  - The reason does not hold. Q-5 says it gives R-130 something to read "on the Profile as first opened". M-23 shows only in the never-committed row (Q-7, Flows:520), so of the five fixture users only First Light would see it.
  - C9 says an empty state "states what is there". This line does not. The marker asks for "a plain statement".
  - MC:9 promises one line per marker, and this marker has two.
  - The placement rests on C11 and C12 (R-130's provisional line), and neither is on the label.
- **Fairness.** The line itself is approved and harmless here. M-28's placement on S-10 is sound. Dropping it from M-23 leaves R-130's app half unmet, which is a question for the user and not one to answer by placing it.

### COPY-7. "Young" is false in states the prototype can reach
- **Checks:** R-143, R-141 ("both settings"), R-102, the file's own MC:7, MC:223.
- **Where:** `Microcopy.md:142`, `:134`, `:223`.
- **What is wrong.** Q-7 says "M-23 is true in all of these". Under B4's option, First Light (`P1:211`, joined 2026-10-01, never committed) at +5 years has rings and years, and reads "Your circle is young". That is one press on the time control. M-22 has the same fault: a user with several finished reveals who tagged nobody has an empty map and reads "Your map is young". MJC:694 ties the word to a person "who joined this year". The word also means different things across the two docs: AD:192 calls no rings **Empty** and AD:193 calls 1–3 rings **Young**.

### COPY-8. Labels and citations
- **Check:** R-150.
- **Where and what:**
  - `:46`: M-01 cites R-098 for the numbers being allowed. R-098 says the reverse under B7 ("no count of the quota is shown in any form"). The allowance is SI:76 and SI:118, and the note should cite those.
  - `:102`: M-14 is labelled B17, B18, and the note says it depends on neither.
  - `:106`: "(switchable)" sits on B1, B10, B11. Only B11 is switchable.

### COPY-9. The status line names no §20 range
- **Check:** R-165 (2). **Where:** `Microcopy.md:3`. Low severity.

### The worker's own wording calls, tested

| Call | Result |
|---|---|
| M-02 "12 months from today" | **Fails.** COPY-1 |
| M-17 tells the owner the network is told | **Fails.** COPY-5 |
| Q-5, the line on S-05 | **Fails.** COPY-6 |
| M-21 "earned" | **Fails on the strict reading.** COPY-4 |
| M-01 `\d+ photos` | **Passes.** S-01 is unavailable while sealed (SI:78), SI:76 requires these numbers, and SI:118 keeps them off S-03. The citation is wrong (COPY-8) and R-006's grep has no carve-out (P-6) |
| M-19 "Each year" | **Not a violation, but the reason is wrong.** C2 covers the unlock date only, so the swap was not needed for that rule. The change also makes it worse in one way: "next year" was a fact about this photo, and "each year" is a standing annual appointment. Spec:102 says "never pushed or reminded". It is true and it appears only on a screen the owner chose to open, so it stays under R-095. Worth a look from the user |
| M-27 "later" | **Passes.** §20 D outranks Spec:204's "years later", and the note cites both. Weak point: "their own hard moments" describes every entry, but the four feed tags include "thankful" and "gratification" (§20 W). It shows no tag (§20 CC), and it comes from Spec:204 |

### Weakest points in this file (not violations)
- **M-25 "You were here." (R-139, R-147, G-12).** Reported as the rubric requires of every audit under B12's "shown". The line carries no number, but a reader can count its appearances and estimate their ring on that person's map. It also tells a public reader they are on the owner's map. C-8 and MC:210 raise it correctly. The user has not ruled.
- **M-05 "runs for 24 hours".** Untrue in the last 24 hours of a journey (P1:133, R-040) and silent on the cap. Q-2 raises it, so this is not a violation.
- **M-08 "It becomes the writing on the back of this photo."** False after a lost press or lost page (JJJ, III). The marker asks for it (Flows:240) and the spec makes the promise (SI:334). But M-09's note says "promises nothing about the page being kept", and M-08's note treats "saved" as breaking the rulings, while "becomes" says the same thing. The bug path is accepted. The notes overclaim.
- **M-01's ladder.** "The most room of the three", "Half the room", "Half again" orders the types by quantity. The next line, "None is a better year", answers it. Close to the marker's limit (Flows:154), within it.

---

## Tested and clean

These were on the brief and held up. They are listed so nobody re-audits them.

- **Sealed envelope, §5 rules 1–9.** No variation by count, date or type. No stand-ins, marks, padlock, loading signs or motion. §11 check 2 tests it. The words sit off the image. The open-highlight line is a plain body line, per §20 S.
- **Sealed year on the circle.** AD:196 adds nothing, and rings start only at finish. R-012, R-143 hold under the default.
- **Rings for non-owners.** A plain ring depends on `k` and `n` alone (AD:182). This meets §20 CCC. The join angle is a function of `k`, so no ring points at a date. No count is printed, and §11 check 5 covers screen readers.
- **Layers, §6.** Own map only. No viewer's layer on any other screen. Name angle comes from a random id (§20 JJ), so it encodes nothing. Same size, colour and weight on all rings. No drift on show. Rejecting the "bubbles that swell" is right (AD:251).
- **Palette.** No gold, green, red. No disabled colour. Rust stays off the ways in (AD:406).
- **Numbers on sealed content.** No line in MC varies with what a sealed year holds. M-04 and M-07 are one line each, no number. M-06 is one fixed line.
- **Lost-press rulings.** M-04 agrees with PP, DDD, GGG (as amended by JJJ), JJJ, QQQ and CCCC. "Deliberately no line" (MC:166–181) carries VVV, UUU, RRR, YYY, WWW, DDDD.
- **Urgency, reminders, come-back, congratulation.** None in product strings. M-11 is the C1 string alone.
- **The six approved lines.** Word for word in both files.
- **No-default questions.** No line settles C17, C18, OQ-51, OQ-52 or FQ-1 to FQ-9. The blanks in MC:198–204 are real blanks.

---

## Proposed rubric additions

Not added, by instruction. The supervisor numbers them.

- **P-1 (area 5, from ART-1).** *Statement:* No position, length or scale in a drawing shown to a public reader is computed from a journey date that reader may not read. *Type:* review, then auto. *How to check:* for each drawing a public viewer receives, take one element the viewer can date from a field they can read, and try to recover the commit or unlock date from its position. Any success fails. The reader behind the drawing returns no day index or commit date. Also: nothing a public viewer can see appears or disappears at reveal finished, other than the paths named in FS §20 ZZ.
- **P-2 (area 13, from ART-3).** *Statement:* A deliverable holds no buildable interim behaviour outside `Decisions-Needed.md`. A doc-local question ID (AD-n, Q-n, FQ-n) may raise a question, but may not carry a state the build draws, because no valid code label can name it (R-149). *Type:* review. *How to check:* list every "until answered", "for now" and "drawn as" cell. Each one names a DN ID, or is blank, or stops the build.
- **P-3 (area 13, from ART-4).** *Statement:* An art-direction or taste label covers colour, type, geometry and texture only. A line under it saying who sees something, on which screen, when it appears or disappears, or what a press does is a behaviour and goes to the open questions. *Type:* review. *How to check:* read every `[AD]` line against that list.
- **P-4 (area 12, from COPY-2).** *Statement:* Strings that can show in the same screen state do not contradict each other. *Type:* review. *How to check:* for each screen state in `Screen-Inventory.md`, list every string the copy file places there, and read them together. A string's "where it sits" note agrees with the states it shows in.
- **P-5 (area 12, from COPY-3, COPY-7).** *Statement:* A line is true in every state that reaches it: the bug paths (lost press, lost page), both settings of every switchable default it touches, and the clock's +5 years. A line about a sealed year says nothing about its contents, including reassurance that is constant for everyone. *Type:* review. *How to check:* run each weighted line against First Light at +5 years under B4's option, a lost press, a lost page, and a journey with no photos. Grep aid on S-03 copy: `missing`, `safe`, `kept`, `waiting`, `nothing has gone wrong`.
- **P-6 (area 1, from M-01).** *Statement:* A type's cadence, yearly photos and highlight numbers appear on S-01 only, and on no screen reachable while a journey is sealed. *Type:* auto. *How to check:* grep the app's copy for the M-01 strings, and fail on any file outside S-01's components. R-006 (a) hits on those strings in S-01 are expected. This keeps the R-006 grep from either failing M-01 or being waved past elsewhere.
- **P-7 (area 8, from ART-6).** *Statement:* The ring-count states have no user-facing or code-facing names that read as levels, and each "do" in the art rules holds for every value its own formulas allow. *Type:* review, then auto. *How to check:* grep code and fixtures for `established`, `veteran`, `young` as a state name keyed to ring count. Read §10 against the worked values at n = 1, 5, 9, 10, 17, 25, 40.
- **P-8 (area 8, from ART-8).** *Statement:* A navigation way exists only where a `Screen-Inventory.md` "Leads to" row names it from that screen, and no way appears, disappears or changes because of content. *Type:* review. *How to check:* compare the marks table with each screen's "Leads to" row in every state, `no-journey` included. A way appearing on the day a reveal opens is reported under R-096 until the user rules.

---

## Open for the user

Not decided here, for the supervisor to carry.

- AD-1 with ART-7: if day marks ever reach the network, the ring shows how many days a person captured.
- Whether the flat graph under B5's option should exist for a public viewer at all, or what it can be anchored to (ART-1). SI:412 also needs this, since it allows the graph without naming an anchor.
- COPY-1 reaches Flows:156. The same ruling applies to both.
- R-130's app half has nothing to read for most fixtures if M-23's second line goes (COPY-6).

---

## Report
- Files changed: `docs/reviews/2026-11-04-rules-art-microcopy.md`
- Findings: 21.
  - **Art-Direction.md: 12**
    - ART-1: R-152, R-162, AD:137/158/162/180/585: public flat graph anchored at the commit date gives the commit and unlock dates, and ending at finish gives the reveal state.
    - ART-2: R-161, R-165, AD:172/90: "same ring geometry for every viewer" drops §20 WW; under B4's option it would hand out the join year.
    - ART-3: rule zero, R-134, R-149, AD:574/580–589: "drawn until answered" is a second default list with no valid code label.
    - ART-4: R-134, AD:44/50/127/243/245/269: `[AD]` settles where rings appear, who may label them, where the envelope goes, and whether empty layer rings exist.
    - ART-5: R-126, R-008, AD:245: "cannot read as a status badge" is not true and not tested.
    - ART-6: R-102, AD:96/98/123/124/193–195/538/540: tier names; bigger and heavier with count; §10 contradicts its own formulas.
    - ART-7: R-102, AD:139–151: "the type never shows" is false; density reads as a score.
    - ART-8: R-134, R-095, R-138, AD:285–296: invents a Capture way; no marks for ways that exist; a way appearing is a marker.
    - ART-9: R-134, AD:461: contrast "accepted", not in §12, reason false for the owner's day marks.
    - ART-10: R-150, AD:148/192/201/270/404/496/541/545/549: defaults cited without the label.
    - ART-11: R-134, AD:520: "no colour change" from a white overlay is false.
    - ART-12: R-165 (2), AD:3: no §20 range.
  - **Microcopy.md: 9**
    - COPY-1: R-013, C2, SI:52, R-135, MC:47/51/52: "12 months from today" is a relative form, and the conflict is argued away instead of raised.
    - COPY-2: R-168, MC:60/61: "One press, one photo." shows beside "No photo was taken."
    - COPY-3: R-009, B19, R-134, MC:86: "Nothing has gone wrong and nothing is missing" is a claim about sealed contents, false after DDD or HHH.
    - COPY-4: R-102, MC:133: "Your map is earned" reads as an achievement.
    - COPY-5: R-150, B1, B2, R-134, MC:105: past its marker, misreads under B2's default, "out" and "told".
    - COPY-6: R-134, R-130, C9, MC:142/221: filled in what Q-5 calls open; reaches only one of five fixture users.
    - COPY-7: R-143, R-141, MC:134/142/223: "young" is false at +5 years under B4's option and for a user who tagged nobody.
    - COPY-8: R-150, MC:46/102/106: wrong citation and misapplied labels.
    - COPY-9: R-165 (2), MC:3: no §20 range.
- Rubric additions: none made, by instruction. Eight proposed, P-1 to P-8, in the report for the supervisor to number.
- Verdict: `docs/Art-Direction.md` FAIL. `docs/Microcopy.md` FAIL.
