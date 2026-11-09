# Rules audit: carrying FS §20 KKKK (network by friend request, map by tags)

Date: 2026-11-09. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md`, R-001 to R-187 before this audit and R-196 after it.

**Targets**

- `docs/Phase-1-Amendments.md` (Am):
  - §12 (lead-tech) and §13 (fixture-designer);
  - their §0 rows (Am:65–66);
  - the §2.2 pointer (Am:230) and the §5 pointer (Am:479).
- `docs/Phase-1-Proposal.md` (P1) lines carrying §12 or §13: 29, 51, 246, 260, 270, 280, 291, 312, 316–320, 385, 392, 394, 396. Also 405, reading R2.
- `docs/Decisions-Needed.md` (DN):
  - E1 to E4 (DN:212–228);
  - B43 to B53, the "Instagram reference" rows (DN:78–88);
  - B54, the supervisor's row (DN:89).
- The supervisor's carriage:
  - `Functional-Spec.md` (FS) 146, 150, §20 H (FS:278) and KKKK (FS:378);
  - `My-Journey-Concept.md` (MJC) 372 and 864;
  - `CLAUDE.md` (CL) "Network and friends" (CL:114) and rule zero step 5 (CL:25).

**Context.** Everything in §12 and §13 is on paper. There is no Postgres on this machine, so no query was run, and none was attempted. The graph (`graphify query "friend request network mutual"`) predates KKKK and returned only the old visibility nodes. Every finding below cites the files.

**Verdict: FAIL.** There are 4 violations, all fixable on paper, and 4 notes.

**What holds up.** The model work is careful and honest.

- **Status.** §12 and §13 each open with "Untested", and every query is marked *not yet run*. Each K-check is stated as behaviour before it names Postgres (L-004).
- **Leak review, §12.6.** It is thorough, and I could not find a leak path it misses:
  - into a sealed year;
  - a layer through access;
  - a decline;
  - a third party learning who removed whom;
  - the close-friends list;
  - a count.
- **B52's newest-first order** is keyed on the request's own `sent_at` only. It returns no time, and it touches no journey.
- **The fixture arithmetic checks out:**
  - 16 "journey launched" and 10 "path crossed" at baseline;
  - per viewer 17, 9, 9, 9 and 0;
  - 31 at 2027-06-21;
  - Q-F1's 20 and 22 rows;
  - every act after both users' `joined_at`.
- **The amended access matrix** matches §12.

**What fails**

- One Instagram-reference row decides a My Journey visibility question that rule zero step 5 sends to the user.
- §20 H is left half-standing against KKKK.
- The audience rule still reads "the map" in P1's reading R2 and in §11's reader table.
- The requests list has a marker gap that the reference product would fill.

**For the prototype**, none of the four puts a banned item on screen as written:

- **V1** changes what a user learns by accepting one friend request.
- **V4** is the one a builder could turn into a visible marker.
- **V2 and V3** are paper risks for Phase 3.

The rubric is updated:

- dated `Updated` lines on the 17 rows and G-3 that KKKK made stale. This includes R-053, R-142 and R-162, which OQ-53 missed;
- nine new checks, R-188 to R-196.

---

## Checks run

```
# Status marking (R-134; the brief's "marked not yet run")
$ grep -c 'not yet run' docs/Phase-1-Amendments.md        -> every §12.7 K-check, the §12.1 sketch, Q-F1 to Q-F15
Am:1282  "Status: written on paper 2026-11-09. Untested … no query in this section has been run"
Am:1551  "Status: written on paper 2026-11-09. Untested … nothing here counts as evidence"
Am:65, :66 (§0 rows)  "On paper, untested: no Postgres on this machine; testing is due in Phase 3"   -> pass

# Map-based membership left anywhere a builder reads
$ grep -n 'layer(member_id)\|takes the viewer, a member\|actor.s network (R2' docs/Phase-1-Amendments.md
Am:1107, :1118, :1119, :1149   §11 reader table: no pointer to §12.3                    -> V3
Am:479                          §5: "Superseded 2026-11-09 by FS §20 KKKK … see §12"      -> pass
P1:405   R2: "the owner's network, meaning everyone on the owner's map" (no note)          -> V3
P1:168   announcement audience "worked out from visibility (see reading R2)"             -> V3

# FS §20 H against KKKK
FS:278  H: "(ring part superseded …) They see nothing beyond the rest of the network"     (unmarked)
FS:378  KKKK (f): "Whether close friends see anything more than other friends is still open (E2)"
FS:150, CL:114, DN E2 (DN:214): open; user 2026-11-09: "yes, close friends should get something extra"  -> V2

# Rule zero step 5 rows (B43–B53): what each decides
B43 send · B44 answer · B45 remove · B46 no number · B47 close-friends list mechanics · B49 list across removal
B50 answer final · B51 resend · B52 order · B53 crossed       -> generic mechanics, banned items dropped
B48 "Who sees an announcement is worked out when it is read. A new friend sees the owner's earlier announcements"
                                                              -> an audience (visibility): V1

# Fixture arithmetic, recomputed from P1 §3.3–3.4 and Am §13.1
journey launched 5+5+3+3 = 16 ; path crossed 3+1+3+2+1 = 10 ; Q-F9 baseline 26, 2027-06-21 26+2+3 = 31
Lantern 8+5+4 = 17 ; Wind 5+4 = 9 ; Hands 9 ; Round 9 ; First Light 0
Q-F1: 11 sends + 4 accepts + 1 decline + 1 withdrawn + 1 removal + 2 entries = 20 ; +accept +befriended = 22
every act after both joins (Am:1595) ; no act on a P1 fixed instant (Am:1597)                     -> pass

# Rubric rows naming fixture access that KKKK changed (beyond OQ-53's list)
R-053  "As Open Hands (on Round's map) … read a Long Way Round #4 photo: allowed"         -> now refused
R-142  "As Open Hands at baseline, read a Long Way Round #4 photo: 'from unlock' allowed"; X case "As Open Hands … Round #4's type and dates: allowed"  -> now refused
R-162  "As Open Hands (network), the same"                                                -> Hands is not Round's friend
```

---

## Violations

### V1. B48 settles a visibility question under "Instagram reference"
- **Checks:** CL rule zero step 5 (CL:25: "Questions about what makes My Journey itself, such as … layers, visibility … go to the user"); R-150; new R-196.
- **Where:** `Decisions-Needed.md:83` (B48); Am:1381, Am:1537 (OQ-41, "User or supervisor"), Am:1712, Am §13.4.2 and Q-F12.
- **What is wrong.** B48: "Who sees an announcement is worked out when it is read. A new friend sees the owner's earlier announcements, and a removed friend stops seeing them."
  - This is not a generic app mechanic. It decides who reads My Journey's feed, which three §20 rulings govern (J, M, UU). It also decides how much of a person's map history each new friendship opens.
  - Under it, accepting one request gives the new friend every "path crossed" the other person has ever emitted, back to 2021, each naming who was on their map (B11 "named", the default).
  - The fixture shows it: from 2026-11-14 Wind reads Hands' two old "path crossed" naming Lantern, and Hands reads Wind's three naming Lantern (Am:1712, Q-F12).
  - E1's own history (DN:212) says the user ruled out people working out who is on someone's map. E3 (a) is already with the user for exactly this kind of exposure. B48 widens it across all past years, by default, under a label that means "not asked".
  - The alternative, the audience at the time of the event, is real and costs a stored audience or a comparison of times (Am:1537). Choosing between them is the user's call.
- **How serious for the prototype.** **Medium.** No banned item appears. A ring is never named (R-092), and nothing sealed is reached. But the user will be deciding E3 (a), whether a friend should learn they are on a map, without being told that B48 already hands every new friend the full crossing history. In the preview, one scripted accept on 2026-11-14 doubles what Wind and Hands know about each other's maps.
- **Fix belongs to:** the supervisor. Either move B48 to the user beside E3, or replace it with the strictest reading under steps 1 to 4 (audience at the time of the event) until the user rules.

### V2. FS §20 H is left half in force against KKKK
- **Checks:** CL:30 (cite both, do not pick); R-165; R-178 (no "for now" on a §20 ruling); R-064.
- **Where:**
  - `Functional-Spec.md:278` (§20 H: "*(ring part superseded …)* They see nothing beyond the rest of the network");
  - `:378` (KKKK: "Whether close friends see anything more … is still open (E2)");
  - `:150`;
  - `CLAUDE.md:114` ("still open");
  - `Decisions-Needed.md:214` (E2: "§20 H's 'nothing extra' stands as the provisional reading"; the user, the same day: "yes, close friends should get something extra");
  - `:82` (B47: "for now they get nothing extra");
  - Am:1284, :1356 ("FS §20 H's 'nothing extra' stands").
- **What is wrong.** H's second half was decided on 2026-10-25, and KKKK supersedes only its ring part. KKKK then calls the same question "still open", and the user has said the answer will be yes.
  - So the record says two things. FS:278 says it is decided. FS:150, FS:378, CL:114 and DN E2 say it is open. DN E2 calls a §20 ruling a "provisional reading", and B47 attaches "for now" to it, which R-178 bans.
  - No B-row carries "nothing extra" as a default. B47's text carries it in passing.
- **How serious for the prototype.** **Low.** Both readings build the same thing today: close friends get nothing extra.
  - It matters for Phase 3 and later. R-064 and §12's K8 test "nothing extra" as a rule, and a builder reading FS:278 alone treats it as decided.
  - When the user answers E2, nobody will know whether a §20 ruling is being reversed or an open question closed.
- **Fix belongs to:** the supervisor. Mark the second half of FS:278 as reopened by KKKK (f) and E2, and give "nothing extra" its own B-row. R-064 now runs under B47 (its `Updated` line).

### V3. The audience and reader rules still read "the map" in P1's reading R2 and in Amendments §11
- **Checks:** R-165 (a ruling is carried in each build doc it bears on); CL:30; new R-188.
- **Where:**
  - `Phase-1-Proposal.md:405` (R2: "the owner's network, meaning everyone on the owner's map", no note);
  - `:168` (the announcement audience, "see reading R2");
  - `:84`, `:126`, `:143`, `:164` ("the owner's network", no note);
  - `Phase-1-Amendments.md:1107` ("network owners by `layer(member_id)`");
  - `:1118` ("the actor's network (R2) … whose map never holds them");
  - `:1119`;
  - `:1149` (the helper that "takes the viewer, a member, and returns owners").
- **What is wrong.** §12.3 lists the before and after for every one of these. But the lines themselves carry no pointer, unlike §5 (Am:479), P1:29 and P1:51. §12.8 records that R2 "is in §4, which the supervisor did not open to this round", and lists P1:84, 126, 143, 164 and 168 as needed and not applied.
  - A developer building `announcement_rows()` from §11's table, or from P1:168 through R2, builds the old map audience.
  - Since KKKK, that is the exact thing E1 ruled out: access that tells a person they are on the map.
- **How serious for the prototype.** **None today, medium for Phase 3.** K1, K2 and K10 would catch a map-based body once tests run. They only exist on paper, and the stale lines are what the code will be written from.
- **Fix belongs to:** the supervisor (P1:405, P1 §4; the P1 lines in §12.8) and lead-tech (a status line on §11's table pointing to §12.3).

### V4. The requests list has no rule against the way to it changing, and the reference product fills that gap with a marker
- **Checks:** R-096, R-186; CL rule zero steps 4 and 5 (the banned list wins over the reference); new R-194.
- **Where:** `Decisions-Needed.md:78` (B43: "It waits in the other person's in-app requests list. No notification, badge, dot or count of requests"); FS:378 (c). There is no screen for the requests list in `Screen-Inventory.md` yet.
- **What is wrong.** B43 drops the reference product's banned parts by name: notification, badge, dot, count. It is silent on how the list is reached.
  - In the reference product the entry to follow requests appears only while requests are waiting. Built "as Instagram" for the part B43 does not state, a "Requests" row that appears when someone asks is a notification by another name.
  - R-186 bans a way that appears because of content. But B43 is the row a builder will follow, and it does not say so.
- **How serious for the prototype.** **Medium.** If built as the reference does it, the profile or feed gains an entry on the day someone sends a request. It is the one place in the friendship design where a re-engagement cue can come in quietly, and the fixture has pending requests at baseline (fr-9, fr-10, fr-11), so a previewing user would meet it at once.
- **Fix belongs to:** the supervisor (B43's wording) and ux (the screen). R-194 now states the behaviour.

---

## Notes (not violations)

- **N1. "Who removed whom" is safe from third parties, and not between the two friends.** §12.6 and K5 say nothing tells anyone who removed whom. Between the two, the one who did not remove always knows by elimination. The model adds nothing to that, which is the most it can do. R-191 states it that way. **Prototype: none.**
- **N2. A declined sender can keep returning to the top of the list.**
  - B51 sets no limit on withdrawing and sending again, and DN:86 notes "no block exists in the docs".
  - B52 puts each new request at the top of the recipient's list.
  - So a person who was declined can resend daily and always sit first.
  - The reference product has block and restrict. B51 departs from it there without saying so.
  - This is not a banned-list item, so it is a user-safety question for the supervisor. Blocking is a generic feature, so step 5 would normally settle it.
  - **Prototype: low** (fixture users do not do this).
- **N3. R-155's statement read literally bans B52.** R-155 says "no default order tells a non-owner when anything happened". B52's order tells a recipient which of their requests was sent later. §12.6 shows that this reveals nothing sealed. R-155 is now scoped by an `Updated` line, and R-192 holds the one allowed time order. **Prototype: none.**
- **N4. E4 builds a state with no B-row.** "Built for now: no one can" (DN:228) is buildable, but `PROVISIONAL: E4` fails R-149's label pattern, and no B-row carries it. The state is the strictest reading, so it is safe (R-193 tests it). It still needs a row for the code label (R-180). **Prototype: none.**

## Tested and clean

**Leaks**

- No friendship reader or writer reads a journey, photo, note or highlight row.
- A friend of a sealed journey's owner gets only `has_journey_underway()` (Am:1402).
- No path dates a sealed year: B52's key is `friend_request.sent_at` alone, in its own transaction (Am:1419).
- A decline is invisible to its sender through readers, writers, crossed requests, the order and the catalog (Am:1415–1421; K3).
- The remover is not stored (Am:1297).
- The close-friends list is owner-only, and no rule reads it (Am:1424).
- No count exists in any reader (Am:1425).

**Banned list, through the Instagram references**

- B43 drops notifications, badges, dots and counts.
- B46 drops friend counts and "people you may know".
- No reference adds a streak, a suggestion or a push. V4 is the one gap.

**Rulings**

- §12.3 carries §20 T, X, HH, SS, ZZ, M, UU, J with B10, R, CCC, GG, DD, LL and TT correctly.
- No reader is left on the map in §12 itself.
- FF's new reason is stated (Am:1358).

**Fixtures**

- §13.3's matrix matches §12's rule cell by cell.
- P1:316–320 match §13.3.
- P1:291 and P1:391 now agree with FS §20 G.
- P1:394's lapsed reason is marked.
- The B54 skip rule is prototype tooling and is labelled so.

**Concept and CLAUDE.md**

- MJC:372 and :864 carry KKKK.
- CL:114 matches FS:378.
- Rule zero step 5 keeps the banned list and steps 1 to 4 above the reference.

---

## Rubric changes made in this run

**`Updated` lines (2026-11-09, FS §20 KKKK)**

- **R-060:** network = current friends; Round now allowed; K1.
- **R-061:** K9.
- **R-063:** the HH case moves to Lantern.
- **R-064:** the list exists, owner-only, nothing extra under B47; K8.
- **R-065:** Hands tagged by Round, Public only.
- **R-066:** the tagger case is Round.
- **R-069:** K10.
- **R-070:** FF's reason.
- **R-081:** superseded in part; `follow` still banned; `friend_request` and `close_friend` allowed only for the §12.1 tables.
- **R-088:** Round now receives; First Light alone does not.
- **R-089:** friends at read time; Q-F9 counts.
- **R-142:** cases move from Hands to Lantern.
- **R-146:** Lantern and Hands.
- **R-155:** B52 scoped.
- **R-157:** K11.
- **R-162:** Lantern is the network viewer.
- **G-3:** the new H/KKKK contradiction.
- **R-053, R-142 and R-162** were missed by OQ-53.

**New checks**

- **R-188:** the map grants nothing; K2, K10.
- **R-189:** a decline never shows; K3.
- **R-190:** both must agree; K4.
- **R-191:** removal at once; no remover beyond elimination; K5.
- **R-192:** no count or time value, and one allowed order; K6.
- **R-193:** only the two people involved; K7.
- **R-194:** no marker on the requests list or its way in; from V4.
- **R-195:** friendship records are append-only and stamped by the app clock; K12.
- **R-196:** an Instagram reference settles only generic questions; from V1.

R-188, R-192, R-193 and R-194 were added to Banned-list coverage, and a log entry was added. No check renumbered or removed.

**Not edited here (other owners)**

- §11 check 5 in `Phase-1-Amendments.md` (Am:1175) still holds as OQ-53 says, since Wind, Lantern, Hands and Round each have a friend at every scripted point. Its wording "a member of each owner's network" now means a friend.
- P1:405 (reading R2) is V3, for the supervisor.

---

## Report
- Files changed:
  - `docs/reviews/2026-11-09-rules-kkkk.md`
  - `docs/Rules-Rubric.md`: R-188 to R-196 added; `Updated` lines on 17 rows and G-3; coverage rows; log entry.
- Findings: 4 violations and 4 notes.
  - **V1:** rule zero step 5, R-150, R-196, DN:83 (B48). A visibility question (a new friend reads all earlier announcements, so the full crossing history) was settled as "Instagram reference". **Medium for the prototype:** it widens E3 (a) before the user rules on it.
  - **V2:** CL:30, R-165, R-178, FS:278 against FS:378, FS:150, CL:114, DN:214, DN:82. §20 H's "see nothing beyond" is left decided while KKKK calls it open, and the user has said yes. **Low for the prototype** (the same build either way). **Medium for the record.**
  - **V3:** R-165, P1:405/168 (R2), Am:1107/1118/1119/1149 (§11). The audience and reader rules still read the map, with no pointer to §12.3. **None today, medium for Phase 3.**
  - **V4:** R-096, R-186, rule zero steps 4 and 5, DN:78 (B43). The way to the requests list is not stated, and the reference product shows it only while requests wait. **Medium for the prototype:** a marker by another name.
  - **Notes:**
    - N1: the person removed always knows who removed them, by elimination.
    - N2: under B51 and B52, a declined sender can resend to the top of the list, with no block.
    - N3: R-155 is scoped for B52.
    - N4: E4's built state has no B-row.
- Rubric additions: R-188 to R-196. `Updated` lines on R-053, R-060, R-061, R-063, R-064, R-065, R-066, R-069, R-070, R-081, R-088, R-089, R-142, R-146, R-155, R-157, R-162 and G-3.
- Verdict: FAIL.
