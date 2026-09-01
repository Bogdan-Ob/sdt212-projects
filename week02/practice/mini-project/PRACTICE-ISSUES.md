# Open issues · playlist mini-project

One open issue. It has a test in `tests/` that **fails today** and must pass
once the issue is fixed. Run that test to check the work, then run the whole
suite to confirm nothing else broke.

Run one test by name, from the folder holding `playlist/` and `tests/`:

```
uv run --with pytest pytest tests/<file>::<test name> -q
```

---

## Issue P1 · Removing a track leaves it in the playlist

**Module:** `playlist/tracks.py`

**What happens:** `remove_track(playlist, "t1")` returns the requested track,
but `t1` is still present afterwards. Code that trusts the function name sees
the returned record and assumes the playlist changed when it did not.

**Expected behavior:** The requested track is returned and removed. Every other
track stays unchanged, and an unknown track id still raises `KeyError`.

**Covering test:**
`tests/test_tracks.py::test_remove_track_removes_it_and_returns_the_record`
