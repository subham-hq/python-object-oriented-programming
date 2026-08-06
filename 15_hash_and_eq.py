"""
__eq__ and __hash__ (and why they travel together)
==================================================

- __eq__ defines value equality (==).
- __hash__ lets an object be used in sets and as a dict key.

Rule: if a == b, then hash(a) == hash(b). Defining __eq__ sets __hash__ to None
(the object becomes unhashable) UNLESS you also define __hash__. Hash on the
same immutable fields you compare in __eq__.

Key idea:
    Custom __eq__ -> provide a matching __hash__ over the same fields, or your
    objects break in sets/dicts.
"""


class Color:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Color):
            return NotImplemented
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def __hash__(self) -> int:
        # Hash the SAME fields used in __eq__.
        return hash((self.r, self.g, self.b))

    def __repr__(self) -> str:
        return f"Color({self.r}, {self.g}, {self.b})"


if __name__ == "__main__":
    red_1 = Color(255, 0, 0)
    red_2 = Color(255, 0, 0)

    print(red_1 == red_2)              # True  (value equality)
    print(red_1 is red_2)              # False (different objects)
    print(hash(red_1) == hash(red_2))  # True  (equal -> same hash)

    # Because eq and hash agree, duplicates collapse in a set:
    print(len({red_1, red_2}))         # 1
    palette = {red_1: "primary"}
    print(palette[red_2])              # 'primary' (red_2 finds red_1's entry)

    # Expected output:
    #   True
    #   False
    #   True
    #   1
    #   primary
