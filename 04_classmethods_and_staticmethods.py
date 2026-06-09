"""
Class Methods and Static Methods
================================

- A regular method receives the instance as `self`.
- A @classmethod receives the CLASS as `cls`. Use it for behaviour about the
  class itself, and for alternate constructors.
- A @staticmethod receives nothing automatic. Use it for a utility that
  logically belongs with the class but needs neither instance nor class state.

Key idea:
    Need `self`? regular method. Need `cls` (class state / alternate
    constructor)? classmethod. Need neither? staticmethod.
"""

import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        # Sets the class variable. Called on a subclass, it sets it on that
        # subclass, because `cls` is whatever class invoked the method.
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        # Alternate constructor: parse a string, then build via cls(...).
        # Using cls (not Employee) means a subclass gets an instance of
        # itself, not of Employee.
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        # No self, no cls -- pure utility. weekday(): Mon=0 ... Sun=6.
        return day.weekday() not in (5, 6)


if __name__ == "__main__":
    Employee.set_raise_amount(1.05)
    print(Employee.raise_amount)              # 1.05

    # Alternate constructor in action:
    new_emp = Employee.from_string("John-Doe-70000")
    print(new_emp.first, new_emp.pay)         # John 70000

    # Static utility (no instance involved):
    print(Employee.is_workday(datetime.date(2026, 5, 7)))  # True  (Thursday)
    print(Employee.is_workday(datetime.date(2026, 5, 9)))  # False (Saturday)

    # Expected output:
    #   1.05
    #   John 70000
    #   True
    #   False
