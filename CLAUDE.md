# CLAUDE.md — Hispania

Iron Age Iberia RPG. Individual soldier view. James 2026-09-19 direction: keep the individual Iberian soldier view; prioritize non-Celtic Iberians first; Celtiberians later in this repo; short-term fixed sequence of events is the nearer build.

Designer notes are James-only. Agent-written research is input, not canon.

Do not merge the open iPhone PRs from an agent session.

## Cloud / iPhone sessions — token cap

James, 2026-09-20. Also in `.claude/rules/iphone-cloud-sessions.md`.

- Do not watch a pull request.
- Do not run /autofix-pr.
- Do not enable Auto-fix.
- Do not poll GitHub Checks, Actions, or `gh run`.
- Do not keep running tests, linters, or builds until they pass.
- If the user asked for a code change, you may run the project test command once. Then stop and wait.
- If tests fail, report the failure and wait. Do not start another fix-and-retest loop unless the user says to.
- Prefer a short plan and a small diff over unattended iteration.
