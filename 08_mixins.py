"""
Mixins
======

A mixin is a small class that supplies a focused piece of behaviour, mixed in
via multiple inheritance. A mixin is not meant to be instantiated on its own
and usually carries no __init__/state -- it just adds methods.

Key idea:
    Use mixins to share orthogonal behaviour (serialisation, comparison,
    logging) across unrelated classes without forcing a deep hierarchy.
"""


class DictReprMixin:
    """Adds a generic __repr__ built from the instance's __dict__."""

    def __repr__(self) -> str:
        # self.__dict__ holds the instance attributes as a dict.
        kwargs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({kwargs})"


class AsDictMixin:
    """Adds a to_dict() method usable by any class with instance attributes."""

    def to_dict(self) -> dict:
        return dict(self.__dict__)


class Point(DictReprMixin, AsDictMixin):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point(3, 4)
    print(repr(p))        # from DictReprMixin
    print(p.to_dict())    # from AsDictMixin

    # Expected output:
    #   Point(x=3, y=4)
    #   {'x': 3, 'y': 4}
