"""
Operator Overloading: Arithmetic, Reflected, and Comparison
===========================================================

Dunder methods let your objects respond to operators:
    +  __add__     -  __sub__     *  __mul__   (and reflected: __radd__/__rmul__)
    == __eq__      <  __lt__      <= __le__    (etc.)

Reflected methods handle "other OP self" when the left operand doesn't know how
to combine with yours (e.g. `2 * money`). functools.total_ordering fills in the
remaining comparisons from __eq__ plus one of __lt__/__le__/__gt__/__ge__.

Key idea:
    Implement the operator that makes domain sense; return NotImplemented for
    unsupported types so Python tries the reflected op or raises a clean error.
"""

from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money({self.cents})"

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented        # let Python handle/raise correctly
        return Money(self.cents + other.cents)

    def __mul__(self, factor: int) -> "Money":
        # Money * int  (scale an amount).
        if not isinstance(factor, int):
            return NotImplemented
        return Money(self.cents * factor)

    # int * Money: Python first tries int.__mul__(2, money) -> NotImplemented,
    # then falls back to money.__rmul__(2). Same logic, so reuse __mul__.
    __rmul__ = __mul__

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents

    def __lt__(self, other: "Money") -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents < other.cents


if __name__ == "__main__":
    a = Money(500)
    b = Money(150)

    print(a + b)             # Money(650)
    print(a * 3)             # Money(1500)  -- __mul__
    print(2 * b)             # Money(300)   -- reflected via __rmul__
    print(a == Money(500))   # True
    print(a < b)             # False
    print(a > b)             # True  (derived by total_ordering)
    print(sorted([a, b]))    # [Money(150), Money(500)]

    # Expected output:
    #   Money(650)
    #   Money(1500)
    #   Money(300)
    #   True
    #   False
    #   True
    #   [Money(150), Money(500)]
