---
name: rules-audit
description: Audit a My Journey doc, screen or code change against the banned list and docs/Rules-Rubric.md, using the rules-guardian agent. `/rules-audit <target>` where target is a file, folder, screen name, or "all". Use after every build step and before every gate.
---

# /rules-audit

1. **Identify the target.** It is a file, a folder, a screen or `all`. With no target, use whatever changed in the last `/phase next` step.
2. **Run the automated checks first.** If `docs/Rules-Rubric.md` lists an automated check script or test command, run it and keep the output. A deterministic check beats an opinion.
3. **Dispatch rules-guardian** with a self-contained brief: the target paths, the automated check output from step 2, and the instruction to audit against every check in `docs/Rules-Rubric.md` and write the report to `docs/reviews/<YYYY-MM-DD>-rules-<target>.md`.
   - If `docs/Rules-Rubric.md` does not exist yet, the brief is to create it first (Phase 1 deliverable), then audit.
4. **Verify the report.** Open it. For each finding, look at the file:line yourself. Drop findings that do not hold up, and say that you dropped them and why.
5. **Make every finding permanent.** If a confirmed finding is not covered by an existing check, make sure rules-guardian added it to the rubric. If a new check can be automated, note it in the report so the developer can turn it into a test.
6. **Return the result:** PASS (zero confirmed violations) or FAIL, the findings list, and any rubric additions.

The guardian must report at least one finding, even if it is only "the weakest point". That does not count as a violation. Only confirmed violations fail the audit.
