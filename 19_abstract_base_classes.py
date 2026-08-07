"""
Abstract Base Classes (ABCs)
============================

An ABC defines an interface: methods that subclasses MUST implement. Inherit
from abc.ABC and mark required methods with @abstractmethod. You cannot
instantiate a class that still has unimplemented abstract methods.

Key idea:
    Use an ABC to guarantee "every subclass provides method X" and to fail
    loudly (at instantiation) when one doesn't.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        # No body needed; subclasses must supply one.
        ...

    def describe(self) -> str:
        # Concrete methods can call abstract ones -- they will be implemented.
        return f"{type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


if __name__ == "__main__":
    shapes: list[Shape] = [Circle(1), Rectangle(2, 3)]
    for s in shapes:
        print(s.describe())

    # Instantiating the abstract class itself fails:
    try:
        Shape()
    except TypeError as e:
        print(f"cannot instantiate: {type(e).__name__}")

    # Expected output:
    #   Circle with area 3.14
    #   Rectangle with area 6.00
    #   cannot instantiate: TypeError
