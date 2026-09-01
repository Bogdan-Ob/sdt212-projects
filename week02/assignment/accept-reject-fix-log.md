# Week 2 · Accept / reject / fix log

**Name:** <your name>
**Date:** <YYYY-MM-DD>

## Issue
- **Issue claimed:** 1 <#number, title from the seeded repo>
- **What the fix should change:** Reject whitespace-only student names with ValueError in add_student <one line>
- **Existing test that confirms it:** tests/test_students.py <test name / file>
- **Branch:** week02-issue1 <branch name>

---

## Log entries (one per agent action)

### Action 1
- **Agent action:** Ran `python -m pytest -q -k test_add_student_rejects_whitespace_only_name` to confirm bug failure
- **Files changed:** none
- **Your explanation (teach-back):** Confirmed initial failure state before making code edits
- **Evidence / test result:** 1 failed, 20 deselected
- **Decision:** accept
- **Follow-up prompt:** none

### Action 2
- **Agent action:** Updated `add_student` in `gradebook/students.py` to validate `not name.strip()` and re-ran tests
- **Files changed:** week02/assignment/mini-project/gradebook/students.py
- **Your explanation (teach-back):** Replaced `if not name:` with `if not name or not name.strip():`. Method `.strip()` removes outer whitespace; whitespace-only strings evaluate to `""`, triggering `ValueError`
- **Evidence / test result:** 1 passed, 20 deselected (full suite: 2 failed, 19 passed)
- **Decision:** accept
- **Follow-up prompt:** none

---

## Pull request
- **Pull request URL:** https://github.com/Bogdan-Ob/sdt212-projects/pull/1 <paste the URL>
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
