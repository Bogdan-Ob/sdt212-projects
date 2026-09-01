# Week 2 · Accept / reject / fix log

**Name:** <your name>
**Date:** <YYYY-MM-DD>

## Issue
- **Issue claimed:** <#number, title from the seeded repo>
- **What the fix should change:** <one line>
- **Existing test that confirms it:** <test name / file>
- **Branch:** <branch name>

---

## Log entries (one per agent action)

### Action 1
- **Agent action:** Ran pytest tests/test_students.py::test_add_student_rejects_whitespace_only_name -q to verify bug reproduction <what you asked the agent to do, and what it did>
- **Files changed:** none <paths touched>
- **Your explanation (teach-back):** Confirmin state of the method<what changed and why it works, in your own words>
- **Evidence / test result:** <test name + pass/fail, or run output>
- **Decision:** <accept | reject | fix>
- **Follow-up prompt:** <the re-prompt you sent if you rejected or fixed, or "none">

### Action 2
- **Agent action:** <...>
- **Files changed:** <...>
- **Your explanation (teach-back):** <...>
- **Evidence / test result:** <...>
- **Decision:** <accept | reject | fix>
- **Follow-up prompt:** <...>

### Action 3
- **Agent action:** <...>
- **Files changed:** <...>
- **Your explanation (teach-back):** <...>
- **Evidence / test result:** <...>
- **Decision:** <accept | reject | fix>
- **Follow-up prompt:** <...>

> Add more entries as needed. At least one entry must carry a full teach-back (what changed, why it works, the passing-test/run evidence).

---

## Pull request
- **Pull request URL:** <paste the URL>
- **Visible status:** <open, unmerged, first body line says "Do not merge.">
- **Existing test now passing:** <test name, confirmed pass>

---

## MCP read-back
Read your own pull request back through the connected MCP server, authorize the call, and record what happened.

- **Tool called:** <the tool name your agent reported, e.g. pull_request_read>
- **What you asked for:** <e.g. pull request #3 in my course repo>
- **One field returned:** <state, title, or head branch, copied from the result>
- **Authorized at the prompt:** <yes / no, and what you were asked to approve>

---

## AI-use disclosure
- **Tools / models used:** <coding agent + model label, e.g. <agent> / <model> ; any other tool>
- **What AI contributed:** <e.g. drafted the fix, wrote the branch edits>
- **What I verified myself:** <e.g. read the diff, ran the test, taught back Action N>
