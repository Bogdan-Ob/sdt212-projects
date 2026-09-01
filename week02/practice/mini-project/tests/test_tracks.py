import pytest

from playlist.tracks import add_track, new_playlist, remove_track


def test_add_track_stores_the_track():
    playlist = new_playlist()
    add_track(playlist, "t1", "Blue Line", 210)
    assert playlist["t1"] == {"title": "Blue Line", "seconds": 210}


def test_remove_track_rejects_an_unknown_track_id():
    playlist = new_playlist()
    with pytest.raises(KeyError):
        remove_track(playlist, "missing")


def test_add_track_rejects_an_empty_title():
    playlist = new_playlist()
    with pytest.raises(ValueError):
        add_track(playlist, "t1", "", 210)
    assert playlist == {}


def test_add_track_rejects_a_duplicate_track_id():
    playlist = new_playlist()
    add_track(playlist, "t1", "Blue Line", 210)
    with pytest.raises(ValueError):
        add_track(playlist, "t1", "Second Wind", 180)
    assert playlist["t1"]["title"] == "Blue Line"


def test_add_track_rejects_a_non_integer_duration():
    playlist = new_playlist()
    with pytest.raises(ValueError):
        add_track(playlist, "t1", "Blue Line", "210")
    assert playlist == {}


def test_add_track_rejects_a_negative_duration():
    playlist = new_playlist()
    with pytest.raises(ValueError):
        add_track(playlist, "t1", "Blue Line", -30)
    assert playlist == {}


def test_remove_track_removes_it_and_returns_the_record():
    playlist = new_playlist()
    add_track(playlist, "t1", "Blue Line", 210)
    add_track(playlist, "t2", "Second Wind", 180)
    removed = remove_track(playlist, "t1")
    assert removed == {"title": "Blue Line", "seconds": 210}
    assert "t1" not in playlist
    assert playlist["t2"] == {"title": "Second Wind", "seconds": 180}
