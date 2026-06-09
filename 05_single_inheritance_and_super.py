"""
Single Inheritance and super()
==============================

A subclass inherits attributes and methods from its parent (base) class.
super() gives access to the parent's implementation -- most importantly to
chain __init__ so the parent can initialise the part of the object it owns.

Key idea:
    Call super().__init__(...) first, then set the subclass-specific
    attributes. Don't copy-paste the parent's __init__ body.
"""


class Employee:
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        # self.raise_amount lets subclasses override the rate (see Developer).
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    # Override the shared class variable for this subclass only.
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_language: str) -> None:
        super().__init__(first, last, pay)  # let Employee set first/last/pay
        self.prog_language = prog_language  # then add what Developer adds


if __name__ == "__main__":
    dev = Developer("Subham", "Bhattacharya", 50000, "Python")
    print(dev.fullname())        # inherited method -> Subham Bhattacharya
    print(dev.prog_language)     # Python

    dev.apply_raise()
    print(dev.pay)               # 55000 -> uses Developer.raise_amount (1.10)

    # Expected output:
    #   Subham Bhattacharya
    #   Python
    #   55000
