from playlist.stats import longest_track, total_runtime
from playlist.tracks import add_track, new_playlist


def _sample():
    playlist = new_playlist()
    add_track(playlist, "t1", "Blue Line", 210)
    add_track(playlist, "t2", "Second Wind", 185)
    add_track(playlist, "t3", "Nightshift", 240)
    return playlist


def test_total_runtime_sums_every_track():
    assert total_runtime(_sample()) == 635


def test_total_runtime_of_an_empty_playlist_is_zero():
    assert total_runtime(new_playlist()) == 0


def test_longest_track_returns_its_title():
    assert longest_track(_sample()) == "Nightshift"


def test_longest_track_of_an_empty_playlist_is_none():
    assert longest_track(new_playlist()) is None
