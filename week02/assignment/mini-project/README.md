# Gradebook mini-project

A small gradebook package with a pytest suite and three open bugs. It is the
codebase you work in for the Week 2 assignment: pick one issue from
[`ISSUES.md`](ISSUES.md) and drive your coding agent until the test that covers
that issue passes.

Standard library plus pytest only: no network, no accounts, no API keys.

## What's here

| Path | Purpose |
|---|---|
| `gradebook/students.py` | Roster storage and input validation |
| `gradebook/grading.py` | Score averages and letter grades |
| `gradebook/reports.py` | Top-students and grade-distribution reports |
| `tests/` | The pytest suite; it defines the expected behavior |
| `ISSUES.md` | The three open issues, each with the test that covers it |

## Run the tests

This project uses [uv](https://docs.astral.sh/uv/) to run Python. `uv run --with pytest`
installs pytest on the fly into an isolated environment: no venv to create, no
activation step, nothing installed globally. Install uv once:

```
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then run the whole suite from **this** folder, the one holding `gradebook/` and
`tests/`:

```
uv run --with pytest pytest -q
```

**Three tests fail on purpose.** That is the starting state of the project, not
a broken setup. A fresh checkout reports:

```
3 failed, 18 passed
```

The three failures are the three issues in `ISSUES.md`. Everything else passes,
so a red run with any *other* test failing means something you changed broke a
behavior that used to work.

## Run one test by name

Give pytest the file and the test name, separated by `::`:

```
uv run --with pytest pytest tests/test_students.py::test_add_student_rejects_whitespace_only_name -q
```

Or match on part of the name with `-k`:

```
uv run --with pytest pytest -q -k whitespace_only_name
```

Each issue in `ISSUES.md` lists its covering test in exactly this
`tests/<file>::<test name>` form, ready to paste.
