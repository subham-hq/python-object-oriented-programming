"""
Classes and Instances
======================

A class is a blueprint. An instance is a concrete object built from that
blueprint. Each instance carries its own data (instance attributes) while
sharing the behaviour (methods) defined on the class.

Key idea:
    Defining a class creates a type; calling the class (Employee(...)) creates
    an instance and runs __init__ to set that instance's own attributes.
"""


class Employee:
    """A minimal example class representing a company employee."""

    def __init__(self, first: str, last: str, pay: int) -> None:
        # __init__ runs automatically when you call Employee(...).
        # `self` is the instance being created; each assignment below stores
        # data ON that specific instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"


if __name__ == "__main__":
    emp_1 = Employee("Subham", "Bhattacharya", 50000)
    emp_2 = Employee("Test", "User", 60000)

    # emp_1 and emp_2 are distinct objects, each with its own attribute values.
    print(emp_1.email, emp_1.pay)
    print(emp_2.email, emp_2.pay)

    print(emp_1 is emp_2)               # False  (different objects)
    print(type(emp_1))                  # <class '__main__.Employee'>
    print(isinstance(emp_1, Employee))  # True

    # Expected output:
    #   Subham.Bhattacharya@company.com 50000
    #   Test.User@company.com 60000
    #   False
    #   <class '__main__.Employee'>
    #   True
