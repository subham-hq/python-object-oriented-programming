"""
Multiple Inheritance, MRO, and the Diamond Problem
==================================================

A class can inherit from several parents. Python resolves attribute/method
lookups using the MRO (Method Resolution Order), computed by the C3
linearisation. The "diamond" (two parents sharing a common base) is handled
correctly because each class appears exactly once in the MRO, and cooperative
super() calls walk that order.

Key idea:
    super() does NOT mean "the parent" -- it means "the next class in the MRO".
    Inspect the order with ClassName.__mro__ (or help(ClassName)).
"""

from __future__ import annotations


class Base:
    def greet(self) -> list[str]:
        return ["Base"]


class A(Base):
    def greet(self) -> list[str]:
        # super() here resolves against the FINAL instance's MRO, not just A.
        return ["A"] + super().greet()


class B(Base):
    def greet(self) -> list[str]:
        return ["B"] + super().greet()


class D(A, B):  # diamond: D -> A -> B -> Base
    def greet(self) -> list[str]:
        return ["D"] + super().greet()


if __name__ == "__main__":
    d = D()

    # Cooperative chain follows the MRO, hitting each class exactly once:
    print(d.greet())  # ['D', 'A', 'B', 'Base']

    # The resolution order itself:
    print([cls.__name__ for cls in D.__mro__])
    # ['D', 'A', 'B', 'Base', 'object']

    # Expected output:
    #   ['D', 'A', 'B', 'Base']
    #   ['D', 'A', 'B', 'Base', 'object']
