"""Track storage for a playlist, with input validation.

A playlist is a plain dict keyed by track id. Each value is a dict with a
`title` and a duration in whole seconds.
"""


def new_playlist():
    """Return an empty playlist."""
    return {}


def add_track(playlist, track_id, title, seconds):
    """Add one track to the playlist and return the stored record.

    A track id must be a non-empty string and unique on the playlist. A title
    must be a non-empty string. A duration must be a non-negative whole number
    of seconds.
    """
    if not isinstance(track_id, str) or not track_id:
        raise ValueError("track_id must be a non-empty string")
    if not isinstance(title, str) or not title:
        raise ValueError("title must be a non-empty string")
    if track_id in playlist:
        raise ValueError("track_id is already on the playlist: " + track_id)
    if isinstance(seconds, bool) or not isinstance(seconds, int):
        raise ValueError("seconds must be a whole number")
    if seconds < 0:
        raise ValueError("seconds must not be negative")

    playlist[track_id] = {"title": title, "seconds": seconds}
    return playlist[track_id]


def remove_track(playlist, track_id):
    """Remove one track by id and return the record that was removed."""
    if track_id not in playlist:
        raise KeyError(track_id)
    return playlist[track_id]
