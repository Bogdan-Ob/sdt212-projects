# Open issues · gradebook mini-project

Three open issues. Each one has a test in `tests/` that **fails today** and must
pass once the issue is fixed. Run that test to check your work, then run the
whole suite to confirm nothing else broke.

Run one test by name, from the folder holding `gradebook/` and `tests/`:

```
uv run --with pytest pytest tests/<file>::<test name> -q
```

---

## Issue 1 · Whitespace-only student names are accepted

**Module:** `gradebook/students.py`

**What happens:** `add_student(roster, "s1", "   ")` succeeds and stores a
student whose name is nothing but spaces. Every report then shows a blank name,
and the record cannot be told apart from another blank-named student.

**Expected behavior:** A name made only of whitespace is rejected exactly like
an empty name: `add_student` raises `ValueError` and the roster is left
unchanged.

**Covering test:**
`tests/test_students.py::test_add_student_rejects_whitespace_only_name`

---

## Issue 2 · `top_students` returns one student too few

**Module:** `gradebook/reports.py`

**What happens:** Asking for the top 3 students on a four-student roster returns
only 2 pairs. Asking for the top 1 returns an empty list. The students that do
come back are in the right order.

**Expected behavior:** `top_students(roster, count)` returns `count`
`(name, average)` pairs, highest average first, ties broken by name A–Z. If
fewer than `count` students have recorded scores, it returns all of them.

**Covering test:**
`tests/test_reports.py::test_top_students_returns_the_requested_number_in_rank_order`

---

## Issue 3 · Averages crash for a student with no recorded scores

**Module:** `gradebook/grading.py`

**What happens:** A student who has been added but never scored raises
`ZeroDivisionError`. `student_average(student)` divides by zero, and
`class_average(roster)` fails as soon as one such student is on the roster. An
empty roster raises the same error.

**Expected behavior:**

- `student_average(student)` returns `None` when the student has no recorded
  scores.
- `class_average(roster)` averages the students who **do** have scores; a
  student with no scores must not change that number.
- `class_average(roster)` returns `None` when no student on the roster has any
  recorded score, including an empty roster.

**Covering test:**
`tests/test_grading.py::test_averages_handle_students_with_no_recorded_scores`
