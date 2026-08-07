"""
Duck Typing and Protocols (Structural Typing)
=============================================

Duck typing: "if it walks like a duck and quacks like a duck, it's a duck."
Python cares whether an object HAS the needed method, not what it inherits.

typing.Protocol formalises this for type checkers: a class satisfies a Protocol
by having the right methods/attributes -- no explicit inheritance required.
@runtime_checkable additionally allows isinstance() checks at runtime.

Key idea:
    Depend on behaviour (methods present), not on a shared base class. Protocols
    document that contract without coupling implementations to a hierarchy.
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class SupportsArea(Protocol):
    def area(self) -> float: ...


# Note: neither class inherits from SupportsArea -- they just match its shape.
class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Disk:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


def total_area(items: "list[SupportsArea]") -> float:
    # Works on anything with .area() -- pure duck typing.
    return sum(item.area() for item in items)


if __name__ == "__main__":
    shapes = [Square(2), Disk(1)]
    print(round(total_area(shapes), 2))   # 7.14

    # runtime_checkable lets isinstance test structural conformance
    # (it checks method existence, not the signature):
    print(isinstance(Square(1), SupportsArea))  # True  (has area())
    print(isinstance("string", SupportsArea))   # False (no area())

    # Expected output:
    #   7.14
    #   True
    #   False
