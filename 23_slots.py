"""
__slots__
=========

By default each instance stores attributes in a per-instance __dict__, which is
flexible but memory-hungry. Declaring __slots__ tells Python the fixed set of
attributes, replacing __dict__ with a compact, fixed layout. This saves memory
(significant at large object counts) and blocks accidental new attributes.

Key idea:
    Many small objects of a fixed shape -> __slots__ for memory savings; the
    tradeoff is that you can no longer add arbitrary attributes.
"""


class Slotted:
    __slots__ = ("x", "y")        # only these attributes are allowed

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Unslotted:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    s = Slotted(1, 2)
    print(s.x, s.y)                 # 1 2

    # No __dict__ on a slotted instance:
    print(hasattr(s, "__dict__"))   # False

    # Adding an undeclared attribute is rejected:
    try:
        s.z = 3
    except AttributeError as e:
        print(f"blocked: {type(e).__name__}")

    # A normal instance allows it freely (and has a __dict__):
    u = Unslotted(1, 2)
    u.z = 3
    print(u.z, hasattr(u, "__dict__"))  # 3 True

    # Expected output:
    #   1 2
    #   False
    #   blocked: AttributeError
    #   3 True
