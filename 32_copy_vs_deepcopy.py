"""
Shallow vs Deep Copy: copy.copy, copy.deepcopy, __copy__, __deepcopy__
======================================================================

copy.copy()     -> SHALLOW: a new outer object, but nested objects are SHARED.
copy.deepcopy() -> DEEP: recursively copies nested objects too, so nothing is
                   shared between original and copy.

Customise the behaviour with __copy__ / __deepcopy__ when the defaults are wrong
(e.g. you must reset a cache or avoid copying a file handle). Most classes need
neither.

Key idea:
    Shallow copy duplicates the container but shares its contents; deep copy
    duplicates all the way down. Mutating shared contents affects both copies.
"""

import copy


class Team:
    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members


if __name__ == "__main__":
    original = Team("A", ["Subham", "Aamir"])

    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    # Shallow copy shares the SAME inner list; deep copy gets its own:
    print(shallow.members is original.members)  # True
    print(deep.members is original.members)     # False

    # Mutating the shared list shows up in the shallow copy, not the deep one:
    original.members.append("Riya")
    print(shallow.members)   # ['Subham', 'Aamir', 'Riya'] (shared -> changed)
    print(deep.members)      # ['Subham', 'Aamir']         (independent)

    # Expected output:
    #   True
    #   False
    #   ['Subham', 'Aamir', 'Riya']
    #   ['Subham', 'Aamir']
