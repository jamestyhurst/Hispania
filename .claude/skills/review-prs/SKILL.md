---
name: review-prs
description: James's pull-request review walk. Use whenever James says "review PRs", "review pull requests", "review requests", "go through the PRs", or names a PR to judge for merging. Works oldest open PR first and decides whether merging it would break the product a user gets by installing from main today — not merely whether the diff conflicts. Repo-agnostic; copy to ~/.claude/skills/review-prs/ on any device.
---

# Review PRs

> Written 2026-09-25 from James's instruction. Portable: holds for every
> repository and device. A repo's own `AGENTS.md` / `CLAUDE.md` may add rules.

## What "review PRs" means

```pseudocode
LIST open PRs, ascending by number.
START at the lowest number. Finish its verdict before touching the next.
FOR each PR:
    READY TO MERGE only if ALL hold:
        mergeable     -- no conflicts with the base branch as it is now
        green         -- repo's tests + checks pass on the PR merged into base
        product-safe  -- someone who installs from base AFTER the merge
                         gets a product that still installs, launches, and plays/works
                         at least as well as before (see checklist)
        in-scope      -- matches the repo's design docs / ADRs; no silent decisions
    FIRST ask: does this PR move toward a destination the project has already
        committed to (ADRs, design docs, James's rulings)? If yes, the default is
        to MAKE IT MERGEABLE: merge base in, fix conflicts, and cut the unsafe
        parts (stubs, placeholder numbers, untested AI behaviour) so the
        foundation lands now and the rest follows in a later PR.
    ELSE verdict is one of:
        FIX-THEN-MERGE   fixes, including cutting unsafe parts, make it ready
                         (preferred for work toward a committed destination)
        PARK             last resort: ideas worth keeping, nothing safe to land yet
                         -> move the code somewhere unwired (e.g. a parked/ subfolder
                            with a guard test that nothing live imports it),
                            keep the full diff as a reference patch,
                            record why and how to integrate later
        CLOSE            superseded, already landed, or not wanted
    REPORT verdict + reasons to James. NEVER merge on your own initiative: James approves
        every merge. His explicit merge command, given after the review, IS that approval --
        then merge in the order he asks (lowest number first unless told otherwise), mark a
        draft ready first, retarget a stacked PR to the base once its parent lands, and pass
        the head SHA you verified so a PR that moved since review is not merged blind.
```

## Product-safety checklist

Ask each against `base + this PR`, not the PR branch alone:

1. **Install:** new dependency? Declared in requirements/lockfile? Stays inside
   the layer the repo allows it in?
2. **Launch:** does the entry point still start? Run it, don't infer it.
3. **Existing saves / data:** schema or format bump? Migration + roundtrip test?
   Does its version number collide with another open PR's?
4. **Balance / behaviour:** stub numbers, TEMP constants, or AI changes that alter
   what every player sees? Was it playtested?
5. **User-facing surface:** new menu items, commands, screens backed by
   half-finished logic?
6. **Stacking:** which open PRs does this one depend on or collide with?
7. **Already landed?** Parts of the diff may already be on base — say so.

## Authorship weighting

Weight scrutiny by who wrote it. Roles (James, 2026-09-25):

- **Claude** — general purpose; the deep, cautious thinker. Reviews on request
  and handles salvage/parking work.
- **Copilot** — the default PR-review agent where available.
- **Grok** (Grok Bot, Warp/Grok) — general purpose, but not expected to think as
  deeply or cautiously as Claude: check its architecture before trusting it.
- **OpenCode** — cheap, expendable, small tasks. Keep its PRs small; a large
  OpenCode PR is itself a warning sign.

## Output

Per PR: number, title, author/device, **verdict**, 3–6 bullet reasons tied to the
checklist, and the smallest next action. Date-stamp any written report.

## Automated mode

> Added 2026-10-24 from James's ruling (`Developer_Documents/designer_notes_2026_10_24_pr_automation.md`).
> Draft by Claude for James to edit. Holds for every repository that carries this skill.

Two runners use this skill without James present. Everything above still holds, except where
this section grants more.

```pseudocode
LIGHT REVIEW   -- GitHub Action, on each push to a PR (.github/workflows/claude-pr-review.yml)
    REVIEW only the pushed PR, against base + this PR.
    POST one comment: verdict (READY / FIX-THEN-MERGE / PARK / CLOSE), reasons tied to the
        checklist, the smallest next action. Edit your earlier comment instead of adding one.
    NEVER push, merge, close, or resolve threads. The sweep does those.

SCHEDULED SWEEP -- a fresh cloud session on a schedule, in Opus: Wednesday Teutoburg, Thursday
                   Greco, Friday Offload then every other repository, early morning Eastern
    IF this repo lacks this skill or .github/workflows/claude-pr-review.yml: copy both from
        jamestyhurst/Teutoburg main in one PR, and merge it first, by this doctrine.
    LIST open PRs, ascending by number. A stacked PR goes right after its parent.
    FOR each PR, in that order:
        REBASE onto base (James, 2026-10-24), then push with --force-with-lease. Every PR
            branch was started by James through an agent he launched, so rewriting it is safe.
        RESOLVE conflicts so the PR fits base AND the READY PRs queued before it.
            Both sides changed the same logic and either choice loses behaviour -> PARK it,
            say why in a PR comment, move on.
        FIX what makes it FIX-THEN-MERGE: missing dependency lines, stale ids, cut stubs.
        READY = the full checklist above passes on base + this PR, AND the repo's test command
            passes locally on the exact head you will merge, AND no CI check on that head has
            failed. Do not wait for CI that is still running: the local run is the proof.
        IF READY: mark it ready for review, then merge (merge commit, never squash),
            passing the head SHA you verified. Retarget its stacked children to base.
        ELSE: leave one comment with the verdict and what blocks it.
    REPORT to James once per sweep: merged, fixed, parked, blocked, each with one reason.

NEVER, in either runner:
    merge a PR whose body lists decisions for James that he has not answered
    merge a PR that settles an open question, or edits a designer note's quoted words
    merge red CI, skip or disable a test to get green, or force-push without --force-with-lease
    close a PR: James closes PRs himself, rarely (designer_notes_2026_10_24.md §5)
    wait on CI by polling: a check still running is left for the next sweep
LIMITS per sweep: at most 10 PRs worked; the test command once per PR change.
```

When a merge lands, every later PR in the queue is checked against the new base before it can
be merged in the same sweep.
