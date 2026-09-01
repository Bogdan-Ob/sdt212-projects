"""Runtime statistics over a playlist."""


def total_runtime(playlist):
    """Return the combined duration of every track, in whole seconds."""
    return sum(track["seconds"] for track in playlist.values())


def longest_track(playlist):
    """Return the title of the longest track, or None for an empty playlist."""
    if not playlist:
        return None
    longest = max(playlist.values(), key=lambda track: track["seconds"])
    return longest["title"]
