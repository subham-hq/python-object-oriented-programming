"""
Class Variables vs Instance Variables
=====================================

A class variable is shared by every instance. An instance variable belongs to
one instance. Reading an attribute checks the instance first, then the class;
writing `self.x = ...` always creates/overwrites an INSTANCE variable, which
shadows the class variable for that one instance only.

Key idea:
    Shared state  -> class variable (a counter, a default rate).
    Per-object state -> instance variable (set in __init__).
"""


class Employee:
    # Class variables: one copy shared across all instances.
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        # Increment on the CLASS so all instances see the same count.
        Employee.num_of_emps += 1

    def apply_raise(self) -> None:
        # self.raise_amount reads the instance value if present, else the class
        # value. Using self (not Employee) lets a subclass override the rate.
        self.pay = int(self.pay * self.raise_amount)


if __name__ == "__main__":
    print(Employee.num_of_emps)         # 0

    emp_1 = Employee("Subham", "Bhattacharya", 50000)
    emp_2 = Employee("Test", "User", 60000)
    print(Employee.num_of_emps)         # 2

    # Changing it on the class affects everyone:
    Employee.raise_amount = 1.05
    print(emp_1.raise_amount, emp_2.raise_amount)  # 1.05 1.05

    # Assigning via the instance creates an INSTANCE variable that shadows the
    # class one -- for emp_1 only:
    emp_1.raise_amount = 1.10
    print(emp_1.raise_amount)                # 1.1  (instance value)
    print(emp_2.raise_amount)                # 1.05 (still the class value)
    print("raise_amount" in emp_1.__dict__)  # True  (now lives on the instance)
    print("raise_amount" in emp_2.__dict__)  # False (still only on the class)

    # Expected output:
    #   0
    #   2
    #   1.05 1.05
    #   1.1
    #   1.05
    #   True
    #   False
