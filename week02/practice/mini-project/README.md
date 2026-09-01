# Playlist mini-project

A small playlist package with a pytest suite and one open bug. This is the
codebase used for the Week 2 course practice: the issue in
[`PRACTICE-ISSUES.md`](PRACTICE-ISSUES.md) is driven from framing to a fix in
class, and you can re-run the same loop yourself afterwards to experiment.

Standard library plus pytest only: no network, no accounts, no API keys.

## What's here

| Path | Purpose |
|---|---|
| `playlist/tracks.py` | Track storage and input validation |
| `playlist/stats.py` | Runtime totals and the longest track |
| `tests/` | The pytest suite; it defines the expected behavior |
| `PRACTICE-ISSUES.md` | The open issue, with the test that covers it |

## Run the tests

This project uses [uv](https://docs.astral.sh/uv/) to run Python.
`uv run --with pytest` installs pytest on the fly into an isolated environment:
no venv to create, no activation step, nothing installed globally. Install uv
once:

```
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then run the whole suite from **this** folder, the one holding `playlist/` and
`tests/`:

```
uv run --with pytest pytest -q
```

**One test fails on purpose.** That is the starting state of the project, not a
broken setup. A fresh copy reports:

```
1 failed, 10 passed
```

That single failure is the issue in `PRACTICE-ISSUES.md`. Everything else
passes, so a red run with any *other* test failing means something changed that
broke a behavior which used to work.

## Run one test by name

Give pytest the file and the test name, separated by `::`:

```
uv run --with pytest pytest tests/test_tracks.py::test_remove_track_removes_it_and_returns_the_record -q
```
