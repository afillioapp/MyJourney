# Rules audit: Phase 1 docs, round 9 (changes since 084890c)

Date: 2026-10-31. Auditor: rules-guardian. Rubric: `docs/Rules-Rubric.md` (R-001 to R-173 after this audit).

**Target:** `git diff 084890c..HEAD -- docs`, six commits from ce64f9e to 8c7e2e2:

- `Functional-Spec.md` §20 QQQ–XXX: new user rulings at FS:352–360, with the date line now at FS:362
- `Phase-1-Amendments.md` and `Phase-1-Proposal.md`: lead-tech carried PPP–RRR and r8 N1, N3, N4 and N6, with tests (35b7cf7)
- `Screen-Inventory.md`: ux carried LLL–RRR (ce248c7) and UUU, VVV (638204c) to S-02 and S-12, and switched §20 citations to ruling letters
- **Supervisor edits:**
  - b9c2958: SSS–VVV recorded; Amendments `:3`, `:7`, `:762`, `:795`, OQ-36/37 cells `:840–841`, and Before-real-users rows 7–8 `:855–856`; P1:3
  - 8c7e2e2: WWW and XXX recorded; DN C7 `:45`; SI labels `:181`, `:229`, `:417`, OQ-24 `:652`, OQ-49 `:718–719`, log `:857`; Amendments `:7`, `:795`; P1:3

Previous audit: `docs/reviews/2026-10-31-rules-phase-1-r8.md` (FAIL: V1–V3; N1–N7).

**Context:** no code exists and `graphify-out/` is absent, so no graph queries were run.

**Verdict: FAIL.** There are 3 confirmed violations:

- **V1:** WWW has not reached S-12. S-12 still calls "skip ends it" the strictest reading of C4, and Amendments still cites only C4 for it.
- **V2:** the status lines are stale or wrong again. Amendments `:3` reads "Open for the user: OQ-36 and OQ-37 … settled", `:7` cites the date line at FS:355, which is now SSS, and P1:3 calls PPP–RRR "the last three".
- **V3:** the supervisor rewrote two history lines in place to cite later rulings. One of them now says, in one sentence, that a decided label is not picked and still open.

All three r8 violations are resolved, and so are r8 N1, N2, N3, N4 and N6. All three new violations sit in the supervisor's direct edits.

One new note blocks Phase 3: G-26, a note window that crosses the journey's unlock.

---

## Auto checks run

```
$ git log --format='%h %s' 084890c..HEAD -- docs
 8c7e2e2 WWW, XXX (supervisor)       638204c UUU, VVV to S-12 (ux)       b9c2958 SSS-VVV (supervisor)
 35b7cf7 PPP-RRR carried (lead-tech) ce248c7 LLL-RRR to S-02/S-12 (ux)   ce64f9e QQQ, RRR ruled

$ grep -nE '^- \*\*[A-Z]+\.' docs/Functional-Spec.md (tail)
 PPP 350, QQQ 352, RRR 353, SSS 355, TTT 356, UUU 357, VVV 358, WWW 359, XXX 360
 date line 362 "*AAA–XXX above were ruled on 2026-10-31.*"; "## 21" 371; "A time control" 375

$ grep -noE "§20 (QQQ|RRR|SSS|TTT|UUU|VVV|WWW|XXX)" docs/*.md | cut -d: -f1,3 | sort | uniq -c
 Amendments  QQQ 13, RRR 4, SSS 4, TTT 2, UUU 0, VVV 0, WWW 0, XXX 0
 Proposal    QQQ 3,  RRR 1, (none of SSS-XXX)
 SI          QQQ 13, RRR 9, SSS 1, UUU 11, VVV 10, WWW 2 (OQ-24 arrow :652, log :857 only), XXX 7
 DN          XXX 1 (C7 :45)                                                              -> V1

$ awk 'NR<587' docs/Screen-Inventory.md | grep -niE "strictest reading|still open|not picked|waits on"
 :340 '(2) the user skips ("skip ends it" is the strictest reading of C4, see OQ-24)'      -> V1
 (other hits: state names "is open", "still open" of a reveal, the "How Spec is cited" note: pass)

$ R-165 (1), F = Phase-1-Amendments.md, words + "open for"
 :3 hits for every settled OQ: one phrase, "Open for the user: OQ-36 and OQ-37 (§8), settled 2026-10-31 by FS §20 SSS and TTT"  -> V2
 :824-:837: each is another OQ row's own question text: pass
$ same on Phase-1-Proposal.md -> none

$ grep -noE "FS:3[5-9][0-9]|FS:2[0-9][0-9]–3[5-9][0-9]" docs/Phase-1-Amendments.md
 :7 "FS:290–360" (correct: XXX is FS:360) and "dated at FS:328 and FS:355"  -> FS:355 is SSS; the date line is FS:362  -> V2
 :52, :552, :762, :816, :839, :853 FS:350 (PPP) ; :53, :515, :539, :762, :836, :840 FS:352 (QQQ) ;
 :54, :554, :762, :816, :839, :853 FS:353 (RRR): all correct
$ same scan on Screen-Inventory.md: only :835 (the revision log, history): pass

$ git show b9c2958 8c7e2e2 -- docs/Phase-1-Amendments.md | grep '^[-+]| 3, 91, 105'
 -… (tenth round) by lead-tech … status note to §20 Q–RRR
 +… (tenth round) by lead-tech … status note to §20 Q–VVV       (b9c2958)
 -… status note to §20 Q–VVV
 +… status note to §20 Q–XXX                                      (8c7e2e2)          -> V3
$ git show 8c7e2e2 -- docs/Screen-Inventory.md | grep -A1 '^-.*Not picked.*profile-picture'
 -"… 'shown by name' keep `PROVISIONAL: C7`. Still open on 2026-10-31 …"
 +"… 'shown by name' keep Spec §20 XXX. Still open on 2026-10-31 …"                  -> V3

$ grep -n "still ahead\|zero interval" docs/Phase-1-Amendments.md docs/Phase-1-Proposal.md
 Amendments :110, :113, :179 ("only if the event's instant is still ahead"), :51 ; P1:213     -> r8 N1 resolved
$ grep -n "R-001–R-1" docs/Status.md
 :36 "R-001–R-171"  (r8 N5 resolved; R-173 after this audit)

$ grep -noiE "while the journey is sealed" docs/*.md
 Amendments:551 only, citing "(P1:104, :108)"; P1:104 is the id row, P1:108 says "within 15 minutes of
 the photo's captured_at (D8)". No FS, DN, P1 or SI line covers a note window that crosses unlock  -> N1 (G-26)

$ git diff 084890c..HEAD -- docs ':!docs/reviews' | grep '^+' | grep -ioE "streak|badge|counter|progress|remind|notif|
  rank|leaderboard|level|unread|retake|re-shoot|try again|countdown|timer|thumbnail|preview|minutes left|face|comment|
  avatar|profile picture|confirmation|tick"
 Every hit is a refusal inside a never-list ("no 'saved' … no tick or check mark", "No message, no timer"), a quoted
 ruling, a SQL or log term ("saved" as a route answer body, "a press saved by the retry"), or "a padded wait is a
 timer in the route. Not built" (OQ-37). No banned element is added.
```

---

## Status of r8 findings

| r8 item | Status | Evidence |
|---|---|---|
| V1: LLL not on S-12 | **Resolved** | S-12 Reads `Screen-Inventory.md:348`: "Nothing of the Photo, not even its id". The main row `:340` and its never-list ban the id on the device (R-169). The source line `:334` cites LLL and NNN |
| V2: PPP's early end had no screen row | **Resolved** | FS §20 RRR (`FS:353`). S-12 end (6) `:340`, the restart row `:344`, the lost-press row `:343` and `:345`. The never-list at `:344` bans "couldn't save your note", "your 15 minutes are up" and "try again". UUU (`FS:357`) settles what follows, at `:340` and `:344` |
| V3: stale status lines | **Resolved, then stale again** | §0 now has PPP, QQQ and RRR rows (`Phase-1-Amendments.md:52–54`). The OQ-12 cell `:816` is split and cites `FS:350`. `:3` reaches RRR. The supervisor's SSS–XXX edits made `:3`, `:7` and P1:3 stale again: V2 |
| N1: loader zero jump | **Resolved** | `Phase-1-Amendments.md:179` ("only if the event's instant is still ahead", `event_at > app_now()`), `:51`, `:110`, `:113`. P1:213 says the same |
| N2: G-25 | **Resolved by the user** | FS §20 QQQ (`FS:352`). Amendments §6 `:515`, `:535`, `:539`, `:550`, `:552`. Evidence `:713–739` covers six states against a rolled-back oracle, with the planted guard-first `capture()` caught (`:736`). SI `:89`, `:94`, `:96`, `:336`. G-25 is closed in the rubric |
| N3: the note timing gap | **Resolved, residual accepted** | Every note press runs one route shape, and a lost press's note now strips its page (`:540`, `:554`). The remaining gap is measured at 5.3 ms (`:555`, evidence `:754–759`) and accepted by FS §20 TTT (`FS:356`; OQ-37 `:841`; Before real users item 8). R-170 (3) is updated |
| N4: route logs | **Resolved** | `:553`: no access or request log line, and no handle, press instant, real time or user id in any output. Evidence `:748–753` scans four text forms and epoch, and a planted route that logs its entry is caught. P1:108 and P1:180 carry it |
| N5: stale citations | **Resolved** | SI cites §20 by letter (`:11`; log `:845`), "Spec §21" (`:40`), and "Spec §20 Still open 1/2" (`:580–581`). `Status.md:36` reads R-171. The evidence edited in place was disclosed. The same kind of edit, without disclosure, recurs: V3 |
| N6: no pre-deploy list | **Resolved** | "Before real users" `Phase-1-Amendments.md:843–858`, items 1–8, each with its ruling and where it is carried |
| N7: the rubric held a retired behaviour | **Done in r8**, and the same kind of thing again here | Lead-tech flagged R-170 (3) and R-170's `Open` line. Both are superseded in this audit (N6 below) |

---

## Coverage of FS §20 QQQ–XXX in the build docs

| Ruling | Amendments | Proposal | Screen-Inventory | Other | Carried? |
|---|---|---|---|---|---|
| QQQ | §0 `:53`; §6 `:515`, `:523`, `:535`, `:539`, `:550`, `:552`; tests `:558`; evidence `:713–739`; OQ-32 `:836` | 91, 105, 180 | S-02 `:87`, `:89`, `:94`, `:96`; S-12 `:336`, `:343`; state `:28`; OQ-50 `:726` | Rubric G-25 closed | Yes |
| RRR | §0 `:54`; §6 `:552`, `:554`; tests `:558`; evidence `:740–747`; OQ-12 `:816`, OQ-35 `:839` | 108, 180 | S-12 `:340`, `:343–345`, `:348–349`; state `:28` | | Yes |
| SSS | OQ-36 `:840`; Before real users 7 `:855` | (no line needed: P1:91 states the order) | log `:854` ("no screen change") | | Yes. The status line `:3` labels it "Open for the user": V2 |
| TTT | OQ-37 `:841`; Before real users 8 `:856` | (none needed) | log `:854` | | Yes. S-12 has no line on waiting for the note answer (R-170 (3), N3 below) |
| UUU | (none needed; the route already answers `closed`) | (none needed) | S-12 `:340`, `:343–345`, `:349`; state `:28`; OQ-24 `:651` | | Yes |
| VVV | (none needed) | (none needed) | S-12 `:340–345`, `:349` | | Yes |
| WWW | **None.** `:552` cites only `C4` ("When the route learns that the user skipped …") | None; P1:3 does not say it does not bear | **OQ-24 arrow `:652` and the log `:857` only. S-12 end (2) `:340` still reads "the strictest reading of C4, see OQ-24"; source line `:334` lacks WWW** | DN C4 `:42` not annotated | **No: V1** |
| XXX | (none needed: YY is already carried in `user_rows()`, `:989`) | (P1:62 cites YY and C7: enough) | `:181`, `:229`, `:417`; OQ-49 `:719`. Source lines `:167`, `:225`, `:247`, `:407` still say "Decisions C7" | DN C7 `:45` | Yes, in the state rows. The OQ-49 history line was rewritten: V3 |

---

## Findings

### Confirmed violations

**V1. FS §20 WWW has not reached S-12 or the Amendments body. S-12 still presents "skip ends the step" as a strictest reading of a provisional default.** Rubric: R-165 (3), R-171 (updated). It blocks the S-12 flow (Phase 2) and screen (Phase 4). It does not block Phase 3.

- **Where:**
  - `Screen-Inventory.md:340`, S-12's list of ends: "(2) the user skips ("skip ends it" is the strictest reading of C4, see OQ-24)".
  - S-12's source line `:334` cites UUU and VVV but not WWW.
  - WWW appears in SI only at the OQ-24 arrow (`:652`) and the supervisor's log line (`:857`).
  - `Phase-1-Amendments.md:552`: "When the route learns that the user skipped or left capture, it drops the entry (C4)". WWW is not cited anywhere in Amendments. The RRR test (`:558`, "a photo skipped and then note-pressed") does test it, but against C4.
  - `Status.md:147` says the supervisor carried WWW "into … Screen-Inventory labels and OQ-24/49". That is true, and it is also all that was done.
- **What is wrong:** WWW (`FS:359`) is a decision: "Skipping the note step ends it for good; no note can be added later in the 15 minutes". The S-12 row still calls it an inventory reading of `PROVISIONAL: C4`, so a builder or the options panel would treat it as provisional. C4 is "not switchable", so nothing is switched today. But R-150 and R-149 track provisional labels, and this one is no longer provisional.
- **Why it breaks the rule:** R-165 (3): each §20 item recorded since a doc's last edit is carried "with its letter cited". This is the same supervisor shortcut that r6, r7 and r8 found: the ruling goes into the OQ record and not into the row it bears on.

**V2. The status lines are stale or wrong after the supervisor's SSS–XXX edits.** Rubric: R-165 (1), (2) and (6). This blocks nothing in Phase 3 behaviour, but the Amendments are the Phase 3 build source.

- **Where:**
  - `Phase-1-Amendments.md:3` ends "Open for the user: OQ-36 and OQ-37 (§8), settled 2026-10-31 by FS §20 SSS and TTT. Owner: lead-tech." The supervisor appended "settled …" to lead-tech's "Open for the user" instead of replacing it. One clause now calls the same two questions both open and settled. The R-165 (1) scan hits it.
  - `:3` gives no account of UUU–XXX, whether as "do not bear" or otherwise.
  - `:7`: "FS §20 Q–XXX (`FS:290–360`, SSS–XXX added 2026-10-31; dated at `FS:328` and `FS:355`)". The range was extended twice, but the date-line citation was never moved. FS:355 is now SSS, and the date line is FS:362. This is R-165 (6) exactly: whoever edits §20 re-checks the citations at or after the edit.
  - `Phase-1-Proposal.md:3`: "§20 Q–XXX … PPP, QQQ and RRR (the last three) bear on lines 91, 105, 108 and 180". They are no longer the last three, and nothing says SSS–XXX do not bear on P1. Of those, only XXX touches a P1 line (P1:62, which cites YY and C7 and is still correct).
- **Why it breaks the rule:** R-165 (1): "No build doc calls a decided question open". R-165 (2): the status line reaches the latest letter, or says why the later letters do not bear. A Phase 3 builder who reads `:3` sees "Open for the user" first.

**V3. Two history lines were rewritten in place to cite later rulings. One of them now contradicts itself.** Rubric: R-172 (new), R-134. No behaviour changes. The record of what was open when is falsified.

- **Where:**
  - `Phase-1-Amendments.md:795`, the §7 row "Applied 2026-10-31 (tenth round) by lead-tech … status note to §20 Q–RRR". The supervisor changed it to "Q–VVV" (b9c2958) and then to "Q–XXX" (8c7e2e2). Lead-tech applied Q–RRR. VVV, WWW and XXX did not exist when the row was written, and the row still credits lead-tech with them.
  - `Screen-Inventory.md:718`, the first OQ-49 arrow. ux wrote: "**Not picked.** … 'The name in the circle' and 'shown by name' keep `PROVISIONAL: C7`. Still open on 2026-10-31 …". In 8c7e2e2 a blanket `PROVISIONAL: C7` → `Spec §20 XXX` replacement reached this history line too. It now reads "**Not picked.** … keep Spec §20 XXX. Still open on 2026-10-31". That is a decided ruling, labelled "not picked" and "still open" in one sentence. The supervisor's log line (`:857`) says "the four `PROVISIONAL: C7` labels". Only three of the four were state rows (`:181`, `:229`, `:417`); the fourth was this history line.
- **What is wrong:**
  - r8 N5 found evidence edited in place, but that edit was disclosed. These two edits are not disclosed.
  - A reader can no longer tell what was open on what date. On SI:718, the line now holds a decided label next to open words, which R-165 is meant to stop.
- **Why it breaks the rule:** the docs are a decision record with dates (`CLAUDE.md:9`, "the decision record, with dates"). A later ruling is added as a new line, as the next arrow (`:719`) correctly does. R-172 makes this a numbered check.

### Notes blocking Phase 3

**N1. A note window that crosses the journey's unlock: the note step's refusal condition has no source, and its route answer has no row (G-26, new).** Rubric: R-171, R-170 (1), R-165. Not picked.

- **Where:**
  - `Phase-1-Amendments.md:551`: the note step "accepts it only from the photo's owner, inside the 15 minutes, while the journey is sealed, and only while the photo has no note (P1:104, :108)".
  - P1:104 is the `id, photo_id` row. P1:108 says only "within 15 minutes of the photo's `captured_at` (D8)". FS §20 K (`FS:281`) says "up to 15 minutes after capture, never after".
  - The evidence stand-in for `add_note` checks "the owner and window" only (`:643`). No test has a note window that crosses `unlocks_at`.
  - `Screen-Inventory.md:346` makes `unlock-day` onward "Not a writing step".
  - The route's window check (`:554`) reads only `press_instant + 15 minutes`. Its answers are `saved` and `closed` (`:552`, `:554`, evidence `:752`).
- **The gap:** take a photo captured at `unlocks_at` − 5 minutes, with its note pressed at `unlocks_at` + 1 minute.
  - **(a)** If the note may be added, a note appears on a photo that is already readable. That writing happens after unlock, against SI:346.
  - **(b)** If it may not, as `:551` asserts, the route's window check passes and `add_note()` refuses. No route answer covers that refusal. A lost press at the same instant is answered `saved` (JJJ), so the two device answers would differ (R-170 (1)). Whatever the route sends is a behaviour nobody ruled on.
  - The prototype reaches this case whenever the demoer jumps to the next unlock while S-12 is open (T-01; R-153).
- **Why it blocks Phase 3:** `add_note()`'s refusal conditions are part of the Phase 3 schema. "While the journey is sealed" is stated once, in a rationale paragraph, against sources that do not say it, and no test covers it. That is a condition a builder will either build or drop by choice. Raise it for the user.

### Notes for Phase 4+ (and the Phase 2 flows)

**N2. WWW is held only by the screen: no line says how a skip reaches the route.** Rubric: R-173 (new), R-169.

- `Phase-1-Amendments.md:552` drops the entry "when the route learns that the user skipped or left capture". But S-12 "sends the page and receives only the route's answer to the note press" (`Screen-Inventory.md:348`), and R-171's list of route answers names no skip request.
- If the device never tells the route, the entry stays alive until the next press or press + 15 minutes. A note press sent after a skip is then accepted. WWW says "no note can be added later in the 15 minutes", and `CLAUDE.md:78–83` requires rules to be enforced in code, not by convention.
- This is a Phase 4 route item. R-173 makes it a test. Whether the device sends a skip, or the route ends the entry another way, is lead-tech's to design within the rulings. It is not picked here.

**N3. A press's own timing is not reviewed.** Rubric: R-170 (4) (new).

- R-170 (3) and OQ-37 cover the note press.
- At the press itself, the paths differ. A lost press strips twice and walks the guard twice, then rolls back. A saved press strips once, encrypts and inserts. A press saved by the retry strips twice and inserts.
- If S-02's hand-off to S-12 waits on the press answer, the hand-off timing differs. No evidence measures it.
- This is a Phase 4 review, not a violation.

**N4. FS §20 SSS (b) is a probe of a frame's availability.** Rubric: R-138 (new `Accepted residual` line).

- Since QQQ, code that holds a product connection can learn whether a press would be accepted without using a frame (`Phase-1-Amendments.md:840`, evidence `:738–739`).
- The device cannot reach it, and the user accepted it until real users (Before real users item 7).
- R-138's "learned only by trying" now has an exception for trusted code, which is recorded on the check.

**N5. Minor carriage gaps.** No behaviour changes.

- **XXX in source lines:** the S-05, S-07, S-08 and S-16 source lines (`Screen-Inventory.md:167`, `:225`, `:247`, `:407`) still list "Decisions C7" and not Spec §20 XXX. The states cite XXX.
- **Stale pointer:** the OQ-31 arrow `:666` still says "Whether YY also settles C7's other two parts is OQ-49". That is history, with no forward pointer to XXX.
- **C4 not annotated:** DN C4 (`Decisions-Needed.md:42`) is not annotated with WWW, nor with III, JJJ or LLL, which each settle a residual of it. C7 (`:45`) is annotated.
- **Rubric range:** `Status.md:36` says R-001–R-171, but the rubric is R-001–R-173 after this audit.

**N6. The rubric itself held lines that QQQ and r8 N3's carriage retired.** These were found and fixed in this audit, as superseding lines. Nothing was deleted.

- **R-170 (3)** read "a lost press, which does no strip, seal or write". The strip is now done on every note press (lead-tech flag).
- **R-170 `Open` and G-25** called the refused-state lost press open. QQQ decided it (lead-tech flag).
- **R-159's current implementation** read "`image_metadata_free()` runs as the first step of `capture()`". Since QQQ it runs after the press is judged.
- **R-116** gave §21 at FS:361. It is now FS:371, and "A time control" is at FS:375.
- **R-086, R-126, G-9 and G-10** still read C7 as provisional.
- **R-171's ends list** still had skip as a reading of C4.

**N7. Weakest points carried forward.** None is a violation today.

- **C17** (`Phase-1-Amendments.md:817`): still no default.
- **Unchanged:** OQ-3 (`:807`) and the highlight-by-date residual (`:858`).
- **Review-only checks** that wait for Phase 4 code:
  - R-169 (5), R-170 (3) and (4), R-171, R-172 (2) and R-173 (2)
  - UUU's "nothing changes on its own". A builder's natural reflex here is to grey out the offer at minute 15, and only a UI test at press + 15:00 with the user idle catches it (R-160, new `Decided` line).

### Checked and clean

- **QQQ mechanism** (`:515`, `:535`, `:550`, `:552`; evidence `:713–739`):
  - The judgment is the normal press's own code at the same frozen instant.
  - Device answers are byte-identical to a normal press in all six states.
  - Per-table reads are identical in the refused states.
  - A refused press leaves zero log lines and no entry.
  - A press into another user's journey is refused with the same reads. It is no probe of someone else's seal.
- **RRR:** four closed cases, byte-identical (`:740–747`). The closed answer carries no reason, time or message (`:554`).
- **N4 carriage:** no route output holds a handle, a press instant in any of five forms, or a user id. A planted logging route is caught (`:748–753`).
- **UUU and VVV on S-12:**
  - The never-lists ban a confirmation in any form, and anything that changes on its own at minute 15.
  - They also ban "too late", "try again" and "time's up".
  - Every lost or discarded case now ends identically to a saved page (`:340–345`).
  - These are refusals, not new elements.
- **XXX state rows** (`:181`, `:229`, `:417`) and DN C7 (`:45`) are correct. `user_rows()` still returns no `profile_picture` (`:989`).
- **No banned element** was added in any changed line (scan above).
- **No silent decision** was found in the lead-tech or ux carriage, apart from N1, where `:551` states an unsourced condition. Lead-tech raised OQ-36 and OQ-37 instead of picking, and both were then ruled.

---

## Rubric changes

**Added:**

| Check | What it covers | Comes from |
|---|---|---|
| R-172 | A dated record (revision-log row, OQ arrow, applied row, status-log line, evidence) is appended to, never rewritten to cite a later ruling | V3; r8 N5 |
| R-173 | A note step that has ended on screen has ended at the server: after a skip, leaving capture, a page taken or a page lost twice, no later note press for that press is taken, whatever the device sends | FS §20 WWW, III; CL:78–83; N2 |
| G-26 | A note window that crosses the journey's unlock: may a note be added after unlock, and if not, what does the route answer? | N1 |

**`Decided` lines added:**

- QQQ on R-160, on R-170 (closing its `Open` line) and on G-25 (closed)
- RRR, UUU, VVV and WWW on R-160
- XXX on R-086, R-126, G-9 (closed) and G-10 (closed)

**`Accepted residual` lines added:**

- SSS on R-138 and R-160
- TTT on R-170

**`Updated` lines added:**

- R-116 (§21 now at FS:371; "A time control" at FS:375)
- R-159 (the guard runs after the press is judged)
- R-170 ((3) after r8 N3's carriage; new (4), the press's own timing)
- R-171 (the ends list after WWW and UUU; the skip request; G-26)

**Other changes:**

- R-173 is added to the "No retakes" coverage row, which is the only changed line, kept whole with text appended.
- One coverage paragraph and one header line are added.
- **Nothing was renumbered or removed.**

## Report
- Files changed: `/home/user/MyJourney/docs/Rules-Rubric.md`, `/home/user/MyJourney/docs/reviews/2026-10-31-rules-phase-1-r9.md`
- Findings: 10
  - V1 (R-165 (3), R-171): `Screen-Inventory.md:340` S-12 end (2) still calls skip "the strictest reading of C4, see OQ-24"; `:334` lacks WWW; `Phase-1-Amendments.md:552` cites only C4. WWW is carried only in the OQ-24 arrow `:652` and the log `:857`
  - V2 (R-165 (1), (2), (6)): `Phase-1-Amendments.md:3` "Open for the user: OQ-36 and OQ-37 …, settled …"; `:7` "dated at FS:355" (now SSS; the date line is FS:362); `Phase-1-Proposal.md:3` "PPP, QQQ and RRR (the last three)", no line on SSS–XXX
  - V3 (R-172, new): `Phase-1-Amendments.md:795`, lead-tech's tenth-round row, rewritten Q–RRR → Q–VVV → Q–XXX (b9c2958, 8c7e2e2); `Screen-Inventory.md:718` OQ-49 history rewritten to "Not picked … keep Spec §20 XXX. Still open"
  - N1 (G-26, R-171, R-170 (1)), blocks Phase 3: `Phase-1-Amendments.md:551` "while the journey is sealed" cites P1:104, :108, which do not say it, and the stand-in `:643` does not test it. A note window crossing unlock has no rule, and `add_note()` refused inside the window has no route answer (`:554`)
  - N2 (R-173, new): `Phase-1-Amendments.md:552` "when the route learns that the user skipped", but `Screen-Inventory.md:348` sends only the page. WWW is held by the screen only
  - N3 (R-170 (4)): a press's own timing (lost vs saved vs retried) is not reviewed or measured; `Phase-1-Amendments.md:555` covers the note only
  - N4 (R-138): `Phase-1-Amendments.md:840` SSS (b) lets trusted code learn whether a frame is available without using one. Accepted, and recorded on R-138
  - N5: `Screen-Inventory.md:167`, `:225`, `:247`, `:407` source lines cite C7, not XXX; `:666` has no pointer to XXX; `Decisions-Needed.md:42` C4 is not annotated with WWW; `Status.md:36` R-171 (now R-173)
  - N6 (fixed here): `Rules-Rubric.md` R-170 (3) "does no strip", R-170 `Open` and G-25, R-159's "first step of `capture()`", R-116 FS:361, C7 provisional lines on R-086, R-126, G-9 and G-10, and R-171's skip. All are superseded, none deleted
  - N7: C17 (`Phase-1-Amendments.md:817`), OQ-3 (`:807`), the highlight-by-date residual (`:858`) and the review-only checks (R-169 (5), R-170 (3)/(4), R-171, R-172 (2), R-173 (2), and UUU's idle-at-15:00 UI test) are unchanged
- Rubric additions: R-172, R-173, G-26; `Decided` lines on R-086, R-126, R-160, R-170, G-9, G-10, G-25; `Accepted residual` lines on R-138, R-160, R-170; `Updated` lines on R-116, R-159, R-170, R-171
- Verdict: FAIL
