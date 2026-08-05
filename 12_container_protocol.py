"""
Container Protocol: __len__, __getitem__, __setitem__, __contains__
===================================================================

Implementing these dunders makes your object behave like a built-in container:
    len(obj)        -> __len__
    obj[key]        -> __getitem__   (also enables slicing)
    obj[key] = val  -> __setitem__
    x in obj        -> __contains__  (falls back to iteration if absent)

Key idea:
    Implement the container dunders and your object supports [], len(), and `in`
    with normal Python syntax -- no special method call needed.
"""

from __future__ import annotations


class Playlist:
    def __init__(self, songs: list[str] | None = None) -> None:
        self._songs = list(songs) if songs else []

    def __len__(self) -> int:
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]            # enables playlist[0] and slicing

    def __setitem__(self, index: int, value: str) -> None:
        self._songs[index] = value

    def __contains__(self, song: str) -> bool:
        return song in self._songs


if __name__ == "__main__":
    pl = Playlist(["Intro", "Verse", "Outro"])

    print(len(pl))            # 3
    print(pl[0])              # Intro
    pl[1] = "Chorus"
    print(pl[1])              # Chorus
    print("Outro" in pl)      # True
    print(pl[:2])             # ['Intro', 'Chorus']  (slicing via __getitem__)

    # Expected output:
    #   3
    #   Intro
    #   Chorus
    #   True
    #   ['Intro', 'Chorus']
