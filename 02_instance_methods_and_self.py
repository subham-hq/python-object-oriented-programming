"""
Instance Methods and `self`
===========================

An instance method is a function defined inside a class whose first parameter
is `self` -- a reference to the instance it is called on. Python passes the
instance automatically:  emp.fullname()  is sugar for  Employee.fullname(emp).

Key idea:
    `self` is not a keyword; it is just the conventional name for the first
    parameter. The method receives the instance so it can read/modify its data.
"""


class Employee:
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self) -> str:
        # Uses the calling instance's own first/last values.
        return f"{self.first} {self.last}"

    def give_raise(self, amount: int) -> None:
        # Methods can mutate instance state.
        self.pay += amount


if __name__ == "__main__":
    emp_1 = Employee("Subham", "Bhattacharya", 50000)

    # These two calls are exactly equivalent:
    print(emp_1.fullname())          # bound method: self = emp_1
    print(Employee.fullname(emp_1))  # explicit: we pass the instance ourselves

    emp_1.give_raise(5000)
    print(emp_1.pay)

    # Expected output:
    #   Subham Bhattacharya
    #   Subham Bhattacharya
    #   55000
