# Cloud / iPhone sessions — token cap

James, 2026-09-20. Standing rule for Claude Code cloud sessions and sessions started from the Claude iOS app.

- Do not watch a pull request.
- Do not run /autofix-pr.
- Do not enable Auto-fix.
- Do not poll GitHub Checks, Actions, or `gh run`.
- Do not keep running tests, linters, or builds until they pass.
- If the user asked for a code change, you may run the project test command once. Then stop and wait.
- If tests fail, report the failure and wait. Do not start another fix-and-retest loop unless the user says to.
- Prefer a short plan and a small diff over unattended iteration.

This rule exists because an unattended iPhone session burned a full weekly usage pool looping CI-style checks.
