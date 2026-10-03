"""
Callable Objects: __call__
==========================

Defining __call__ makes an INSTANCE callable like a function: obj(args) runs
obj.__call__(args). Use it for function-like objects that also carry state or
configuration -- strategies, partially-configured operations, and class-based
decorators.

Key idea:
    Need a "function" that remembers state or is configured at creation time?
    Make a class with __call__ instead of juggling closures/globals.
"""

from typing import Callable


class Multiplier:
    """A configurable callable: built with a factor, then called like f(x)."""

    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, value: int) -> int:
        return value * self.factor


class CallCounter:
    """A class-based decorator: wraps a function and counts how often it runs."""

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


@CallCounter
def greet(name: str) -> str:
    return f"hi {name}"


if __name__ == "__main__":
    triple = Multiplier(3)
    print(triple(10))          # 30  -- instance called like a function
    print(callable(triple))    # True

    print(greet("Subham"))     # hi Subham
    print(greet("Aamir"))      # hi Aamir
    print(greet.calls)         # 2   -- state kept on the wrapping instance

    # Expected output:
    #   30
    #   True
    #   hi Subham
    #   hi Aamir
    #   2
