# Decisions Needed

Every open question raised in Phase 1, merged and with duplicates removed. Sources:
- `Screen-Inventory.md` "Open questions" (Inv 1–36)
- `Rules-Rubric.md` "Gaps" (G-1–G-22) and "Questions for the user" (Q1–Q5)
- `Learnings/index.md` "Open questions" (LQ1–LQ7)

Only the user decides these. Where the docs lean one way, the lean is noted, but a lean is not a decision. Record each answer here with its date. The supervisor then writes it into `Functional-Spec.md` §20 and fixes every restatement (L-002).

Last updated: 2026-10-30

---

## Provisional defaults in force

Approved approach (user, 2026-10-27): build the prototype with these defaults and decide by playing. Each default is the way the docs lean or, where they don't lean, the strictest reading of the banned list. **Switchable** defaults get a toggle in the prototype options panel, next to the time control. Every default is labelled in code as `PROVISIONAL: <ID>`. None of these is a decision until the user says so.

| ID | Provisional default | Switchable |
|---|---|---|
| B1 | "Publish" means "reveal finished". Docs use only "reveal finished" and "journey launched" | no |
| B2 | The network can read an unlocked journey from unlock, as D12 and `Phase-1-Proposal.md:311` say. Under the option, no one but the owner reads it until the reveal is finished, Public photos included (**decided 2026-10-30**, Spec §20 R) | **yes**: from unlock / only after reveal finished |
| B3 | Each reveal choice takes effect when made. A reveal can be finished at any later time | no |
| B4 | One ring per finished reveal (`Phase-1-Proposal.md:65`) | **yes**: per finished reveal / per year with the app |
| B5 | Activity line twists in at reveal finished. The activity graph is visible to the owner only | **yes**: owner only / built from the photos the viewer can see |
| B6 | Others learn nothing about highlights. The owner sees only "a highlight is open", with no end time and no countdown. The owner part holds over B19 (**decided 2026-10-30**, Spec §20 S) | no |
| B7 | Frames left are never shown. A refused capture says so with no number (copy in Phase 2) | no |
| B8 | Counters and progress bars are banned at all times, not only while sealed | no |
| B9 | Positivity Feed: (a) reflection text only, with the photo shown when opened; (b) per-photo visibility; (c) drafted tag list only; (d) chapter filter available; (e) newest first; (f) only after reveal finished. (c) list **decided 2026-10-30**: the four working tags (Spec §20 W) | (a) **decided 2026-10-30: text only**, no longer switchable (Spec §20 Q). (b)–(f) provisional, no |
| B10 | "Reflection left" reaches only the owner's network members who can see the photo, even when it is public | no |
| B11 | "Path crossed" names both people and reaches the owner's network. It never says which ring | **yes**: named / unnamed |
| B12 | Walking a path shows the photos where the reader appears, in journey order, with no total and no grouping | **yes**: shown / hidden |
| B13 | The slot 1 overview can be written after the reveal is finished, within the slot. Readable by the network only | no |
| B14 | "Public" means signed-in users only | no |
| B15 | No usage analytics or telemetry of any kind | no |
| B16 | A commit on the 29th–31st uses the last day of shorter months. One time zone for the prototype (UTC). Exactly 15:00 is out. A highlight lasts 24 hours of elapsed time | no |
| B17 | Feeling tags are free text on the journey, with no category, as in the approved model (`Phase-1-Proposal.md:141`). Raised as Screen-Inventory OQ-37 and rubric G-14 | no |
| B18 | Tags never "surface" by popularity. No suggestions and no counts (`Functional-Spec.md:202` over `:131`). Raised as OQ-38 and G-14 | no |
| B19 | The owner of a sealed journey sees its type, commit date and unlock date and nothing else (`Phase-1-Proposal.md:84`; `Functional-Spec.md:74` read as covering the contents). Raised as OQ-39 and G-17. Exception: B6's "a highlight is open" (**decided 2026-10-30**, Spec §20 S) | no |
| C1 | "Your Journey is ready" appears on next open, never as a notification | no |
| C2 | The unlock date is shown as a plain date, never relative ("in 64 days") | no |
| C3 | The sealed-year screen does not point to earlier journeys. Their open reflection slots are reached from the owner's profile | no |
| C4 | The note step is offered only inside the capture flow, straight after the photo, for up to 15 minutes. Leaving capture ends it, so there is no way back from the sealed screen (this resolves audit finding 1). The page is taken live, once, with no re-shoot | no |
| C5 | Nothing is required before finishing a reveal. Each set-once choice shows a one-line "this can't be changed" before it is saved | no |
| C6 | People tags are not shown to readers | **yes**: hidden / shown |
| C7 | No profile picture is shown anywhere. The profile shows the name in the circle. Announcements carry no image | no |
| C8 | The map shows current rings only: no counts, no history, no drift | no |
| C9 | Empty states are a plain statement; copy in Phase 2 | no |
| C10 | People are found by name search, plus typed names for non-users | no |
| C11 | No sign-up or onboarding in the prototype. Fixture users are picked from the prototype panel | no |
| C12 | The app opens on the Profile, "the destination" (`CLAUDE.md`) | no |
| C13 | A photo's "follow-up" is its reflection stack | no |
| C14 | Feed is newest first | no |
| C15 | The app never asks for notification permission | no |
| C16 | The prototype panel has a viewer switcher (fixture users) and shows the simulated date | no |

Section A was approved by the user on 2026-10-27 and is being applied.

---

## A. Text corrections: the decision already exists

The docs already decided these, in `Functional-Spec.md` §20 or `Phase-1-Proposal.md`. Older lines still say otherwise. **One yes approves all of them.**

| # | Stale text | Correct per | Raised as |
|---|---|---|---|
| A1 | The reflection example uses per-photo dates (`Functional-Spec.md:104–111`, `My-Journey-Concept.md:200, 203–210`) | §20 D: all photos of a journey move to their next slot on the unlock anniversary (`Functional-Spec.md:101, 274`) | Inv 1, G-1 |
| A2 | "Written a year or more after the moment" (`Functional-Spec.md:98`) | §20 D slot rule | Inv 2 |
| A3 | Close friends "get everything" (`My-Journey-Concept.md:807, 383`) | §20 H: they see nothing extra | Inv 4, G-3 |
| A4 | Layers calculated on "upload" (`My-Journey-Concept.md:401`) | Calculated at reveal finished (`Functional-Spec.md:162`) | Inv 5, G-2 |
| A5 | Journey stores "frames used", "highlights used" and a "committed" state (`Functional-Spec.md:14–15`) | Proposal: counts never stored, state derived (`Phase-1-Proposal.md:49, 76–84`) | Inv 8, G-6 |
| A6 | Overview "written at reveal" (`Functional-Spec.md:118`, `My-Journey-Concept.md:218`) | §20 E: a new one every year (`Functional-Spec.md:275`) | Inv 14, G-15 |
| A7 | "Frame range 24–48" and the arithmetic built on it (`My-Journey-Concept.md:99, 128, 799`, `Functional-Spec.md:47`) | Types are 12, 24 and 48 (`Functional-Spec.md:38–42`) | Inv 13, G-22 |
| A8 | The streak ban points to "section 4" (`My-Journey-Concept.md:714`) | §7 (line 244) and `Functional-Spec.md` §18 | G-22, LQ3 |
| A9 | The upload vs sealed fork is still open (`My-Journey-Concept.md` §28) | Sealing is automatic at capture (`Functional-Spec.md` §4) | LQ1 |
| A10 | "Six phases" (`Build-Plan.md:3`, `README.md:14`), and the Phase 5 start is given three ways | Seven phases, 0 to 6. Phase 5 starts after Phase 2 (`Build-Plan.md:121`) | L-002 |
| A11 | "Phase 2" also names the business's printing stage (`Functional-Spec.md` §17) | Rename it "the album phase" | L-003 |
| A12 | `Overview.md` is out of date | Add a "Historical, not maintained since 2026-10-21" banner, and mark it so in `README.md` | LQ4 |

**Decision:** ☐ Apply all · ☐ Apply except: ____

---

## B. Blocks the Phase 1 gate: these change the data model or the rules

The Phase 1 gate asks that a developer can build the data model "with no questions left". Each question below changes a table, an access rule or a check.

**B1. "Publish".** Does "published" (`Functional-Spec.md:141`, Concept 365–367, 424, 440) mean "the reveal is finished"? *Lean:* yes. Use only "reveal finished" and "journey launched". (Inv 3, G-2, LQ2)

**B2. Reading a journey before its reveal is finished.** From unlock until the owner finishes, every photo is Network by default (`Functional-Spec.md:151, 269`, `Phase-1-Proposal.md:311`). Concept:362 says sharing happens "only … as a finished story". Can the network read an unlocked journey before its reveal is finished? (Inv 9)

**B3. A reveal that is never finished.** Can the owner still finish it in later years? If they set a photo to Private and never finish, does that choice take effect? *Lean:* each choice takes effect when made (set-once, `Functional-Spec.md:286`), and the photos default to Network. (Inv 16, G-11)

**B4. What adds a ring to the circle.** One per year with the app (`Functional-Spec.md:185`, Concept:687), or one per finished reveal (`Phase-1-Proposal.md:65`, approved)? (Inv 6, G-7)

**B5. The activity graph and line.** When does the line twist into the circle: at unlock, or at reveal finished? Who sees the graph: owner only, or built only from the photos the viewer can see? Captured times of private photos must not leak (`Functional-Spec.md:145`). (Inv 7, 28)

**B6. Highlights in the sealed year.** Highlight records are not sealed in the approved model (`Phase-1-Proposal.md:48`). May the owner see that a highlight is open, and when it ends? *Lean:* others see nothing (§20 I). For the owner, open or closed with no countdown. (Inv 26, G-13)

**B7. Frames left.** May the owner ever see frames left (`Functional-Spec.md:243` leaves room; `Phase-1-Proposal.md:49` says never)? What does a refused capture say? (Inv 25, G-5, Q5)

**B8. Counters after unlock.** The spec bans counters and progress bars "during the sealed year" (`Functional-Spec.md:233`), while `CLAUDE.md` bans them outright. Is "12 of 24 reflected" allowed during the reveal? *Lean:* banned at all times. (G-4)

**B9. Positivity Feed.**
- (a) Does it show photographs? "No photo feed, never images" covers the announcement feed. Is the Positivity Feed exempt?
- (b) Visibility is per photo, not per journey.
- (c) Which tags qualify: only the drafted list, or free text too?
- (d) Can it be filtered by chapter?
- (e) In what order?
- (f) Can a photo enter before its reveal is finished?

(Inv 11, 12, 30, G-8, G-14)

**B10. "Reflection left" on a public photo.** It goes to everyone who can see the photo, so every user receives it. Intended? (Inv 22)

**B11. "Path crossed" names the crossed person.** That tells them they are on the owner's map (`Functional-Spec.md:164`). Does it name them, and does it reach them? (Inv 21)

**B12. "Where you appear" in Walking a path.** Showing a reader the photos they appear in lets them count those photos and estimate their ring. Show them without a total? Or not at all? (Inv 19, G-12)

**B13. Overviews.** Can slot 1 be written after the reveal is finished? Can anyone outside the network read it? (Inv 14, G-19)

**B14. "Public".** Does "anyone" include signed-out visitors? (G-20)

**B15. Analytics.** May the app or site collect any usage analytics? *Lean:* no, since low usage is the goal. (Q2)

**B16. Calendar edges.**
- A commit on the 29th–31st or on 29 February: when do its months and its unlock fall?
- Whose time zone defines a day?
- Is a note added at exactly 15:00 minutes in or out?
- Does a 24-hour highlight stay 24 hours across a daylight-saving change?

(G-18)

---

## C. Needed in Phase 2: these shape flows and screens, not data

**C1. Unlock day.** How does the owner learn the journey has unlocked, with no notifications? Is "Your Journey is ready" text shown on next open, or a notification? *Lean:* text on next open only. (Inv 15, G-16)

**C2. The unlock date.** May the owner see it? As a date only, or as "in 64 days" (a countdown)? *Lean:* a plain date, no relative time. (Inv 27, G-17)

**C3. The sealed-year screen and earlier journeys.** May the sealed-year screen point the owner to reflection slots still open on their earlier journeys? (Inv 10)

**C4. The note step.** How does the user return to it within the 15 minutes, when the photo is already sealed? Can the page be re-photographed before saving? Must it be taken live in the app, or can it come from the gallery? (Inv 24, Q3)

**C5. Finishing a reveal.** Is anything required before finishing, such as a chapter? Is the owner asked to confirm each set-once choice? (Inv 17, 18)

**C6. People tags for readers.** Can a reader see who else is tagged? Can a tag lead to that person's profile? (Inv 20)

**C7. Profile picture.** What may it show, given "nothing signals how the person looks"? When is it set, and can it change? May announcements show it? (Inv 31, G-9, G-10)

**C8. The map's detail.** Does the owner's map show past rings, drift, or shared-photo counts? (Inv 36)

**C9. Empty states.** What do an empty map, an empty feed and an empty circle hold? (Inv 23)

**C10. Finding people.** How does a user find another user to tag or visit: search, invitation, or something else? (Inv 33)

**C11. Invitation and onboarding.** Invitation is "the main arrival path" (`Functional-Spec.md:28`) but no step is described. (Inv 32)

**C12. Opening the app.** Which screen opens the app in each state? (Inv 34)

**C13. "The follow-up".** Is a photo's follow-up only its reflection stack? (Inv 29)

**C14. Feed order.** *Lean:* newest first. (Q1)

**C15. Notification permission.** If no notification is ever sent, should the app ask for notification permission at all? *Lean:* never ask. (Q4)

**C16. The prototype viewer.** How does the demoer switch between fixture users? Does the time control show the simulated date? (Inv 35)

---

**C17. Time-control jump and another user's unlock date.** "Jump to the next unlock" plus the shown date tells the demoer when another user's journey unlocks. Is the demoer exempt, or does the jump go to the chosen viewer's own next unlock? (Inv OQ-41; re-audit N8.) No default.

**C18. How long "Your Journey is ready" stays.** Once, on the next open, or on every open until the reveal is finished? (Inv OQ-42; re-audit N5.) C1 says "next open". No default.

## D. Already open elsewhere

| # | Decision | Blocks |
|---|---|---|
| D1 | Stack: **decided 2026-10-30, local Postgres first**. Deploy host still open (`Status.md` Open decisions 1) | Before deploy |
| D2 | Vercel Authentication on `myjourney`: make the holding page public or keep it private (a dashboard change) | The holding page |
| D3 | May the supervisor commit after each recorded step? (LQ7) | Nothing; the working tree stays uncommitted until then |
| D4 | Export and data ownership | Phase 6 |
| D5 | Age gating | Phase 6 |
