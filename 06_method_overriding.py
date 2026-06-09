"""
Method Overriding
=================

A subclass can redefine a method it inherited. Calls on a subclass instance use
the subclass's version (dynamic dispatch). The override can fully replace the
parent's behaviour, or extend it by calling super().

Key idea:
    The subclass's method wins for subclass instances. Use super() inside the
    override when you want "parent behaviour PLUS extra".
"""

from __future__ import annotations


class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    def describe(self) -> str:
        return f"{self.first} {self.last} (employee)"


class Manager(Employee):
    def __init__(self, first: str, last: str, team: list[str] | None = None) -> None:
        super().__init__(first, last)
        # Avoid a mutable default argument ([]). One shared list would leak
        # across every Manager created without an explicit team.
        self.team = team if team is not None else []

    # Full override: replaces Employee.describe entirely.
    def describe(self) -> str:
        return f"{self.first} {self.last} (manager of {len(self.team)})"


class Lead(Manager):
    # Extend rather than replace: reuse Manager.describe via super().
    def describe(self) -> str:
        base = super().describe()
        return f"{base} [tech lead]"


if __name__ == "__main__":
    emp = Employee("Test", "User")
    mgr = Manager("Sue", "Smith", ["Aamir", "Riya"])
    lead = Lead("Lin", "Park", ["Sue"])

    print(emp.describe())    # ... (employee)
    print(mgr.describe())    # ... (manager of 2)
    print(lead.describe())   # ... (manager of 1) [tech lead]

    # Expected output:
    #   Test User (employee)
    #   Sue Smith (manager of 2)
    #   Lin Park (manager of 1) [tech lead]
