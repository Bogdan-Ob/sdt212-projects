# Week 2 Assignment: Drive the agent to a pull request

**Graded:** 10 pts (classwork)

In class, one seeded issue was driven from framing to a pull request, gated with a teach-back and recorded in an accept/reject/fix log, then read back through the repository host's MCP server. That demonstration used a separate playlist package, so all three issues here are unseen. Now do **one** of them yourself. Review-bot triage is out of scope here.

**Before you start:** confirm that the single private course repository has `main` on an authenticated remote, the instructor can inspect it, and a supported CLI or web route can open a pull request. That repository is created in class, earlier in the session. See [`../../README.md`](../../README.md) for the repository policy.

Your repository host's **MCP server** must already be connected to your agent, with its tools listed. You connect it in class during the practice block, so it is ready before this task starts. Resolve all setup before you start.

## Work
1. **Pick one** issue from `mini-project/ISSUES.md`. **Issue 1 is the lighter pick**; Issue 3 is the stretch. In one line, state what the fix should change and which **existing test** confirms it.
2. From the root of the existing private course repository, **branch** off the issue with `git switch -c week02-issue<N>`. Open **agent mode** in the coding agent chosen for this run.
3. **Frame** the issue to the agent. **Authorize each command and edit at the prompt**, and **withhold** on anything outside the issue's scope or the low-risk boundary (no database writes, no deployment, no secrets, no dependency upgrades).
4. **Run the existing test.** From `mini-project/`, run `uv run --with pytest pytest -q`. That installs pytest on the fly into an isolated environment, so there is no venv to create and no activation step. If you do not have [uv](https://docs.astral.sh/uv/) yet, install it once with `curl -LsSf https://astral.sh/uv/install.sh | sh` (Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`).
   **Expect a red run: 3 tests fail on purpose** (one per issue in `ISSUES.md`). That is the starting state, not a broken setup. Your job is to turn *your* issue's test green and leave the others alone. Run just yours with `uv run --with pytest pytest -q -k <the full covering-test name from ISSUES.md>`; a short fragment can match a second test and muddies the result. Iterate with the agent until it passes.
5. **Apply the teach-back gate** to at least one change before accepting it: say **what changed**, **why it works**, and **what evidence** (passing test / run output) backs it.
6. Fill in `accept-reject-fix-log.md`: **one entry per agent action**: action, files changed, your explanation, evidence, decision (accept / reject / fix), follow-up prompt.
7. **Commit and open a pull request** in the private course repository, even if imperfect:
   `git add week02/assignment/` · `git commit -m "Fix issue <N>: <what changed>"` · `git push --set-upstream origin week02-issue<N>`
   You already created the branch in step 2, so do not create it again here.
   Use the repository host's supported CLI or web route to open a pull request into `main`. Make `Do not merge.` its first body line, and leave it open and unmerged. Paste the URL into the log, then commit and push the updated log so the branch carries the link.
8. **Read your own pull request back through the MCP server.** In agent mode, ask the agent to read pull request `<N>` in your repository using the connected server, and **authorize the call** when it asks. Record in the log the **tool name** it called and **one field** from the result (its state, title, or head branch). As of 2026-08-30 the read tool for a pull request is `pull_request_read`; if your agent reports a different name, record the name it actually used.
9. **Submit** the completed `accept-reject-fix-log.md` to the **Week 2 Canvas assignment**, with the pull-request URL filled in. Submission stays open until the **end of the day**.

## Show
Display the **private pull request** and **teach back one change** aloud: what changed, why it works, and the evidence.

## Rules
- **One issue only.** Review-bot triage is demo-only this week, so do not include it.
- **The MCP call is read-only.** Read your pull request; do not let the agent create, edit, close, or merge anything through the server.
- **Low-risk task only**: no database writes, no deployment, no secrets, no dependency upgrades.
- **Disclose** your tools and models in the `accept-reject-fix-log.md` disclosure block; the teach-back gate is how you show you own each change.
