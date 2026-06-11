"""
__repr__ and __str__
====================

- __repr__ : unambiguous, developer-facing. Ideally valid Python that could
  recreate the object. Used by repr(), the REPL, and containers.
- __str__  : readable, user-facing. Used by str() and print().

If you define only one, define __repr__ -- Python falls back to __repr__ when
__str__ is missing (but not the other way round).

Key idea:
    __repr__ for debugging/logs; __str__ for display. repr is the safety net.
"""


class Employee:
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def __repr__(self) -> str:
        # Aim for "eval-able": Employee('Subham', 'Bhattacharya', 50000)
        return f"Employee({self.first!r}, {self.last!r}, {self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname()} - ${self.pay}"


if __name__ == "__main__":
    emp = Employee("Subham", "Bhattacharya", 50000)

    print(str(emp))     # __str__
    print(repr(emp))    # __repr__
    print(emp)          # print() uses __str__

    # Containers use __repr__ for their elements, not __str__:
    print([emp])        # [Employee('Subham', 'Bhattacharya', 50000)]

    # Expected output:
    #   Subham Bhattacharya - $50000
    #   Employee('Subham', 'Bhattacharya', 50000)
    #   Subham Bhattacharya - $50000
    #   [Employee('Subham', 'Bhattacharya', 50000)]
