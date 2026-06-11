"""
isinstance() vs issubclass()
============================

- isinstance(obj, Cls)  -> is this OBJECT an instance of Cls (or a subclass)?
- issubclass(Sub, Cls)  -> is this CLASS derived from Cls?

A very common mistake is passing a class as the first argument to isinstance.
A class is not an instance of your class -- it is an instance of `type` -- so
isinstance(Manager, Employee) is always False. The question you actually meant
is issubclass(Manager, Employee).

Key idea:
    First arg is an object -> isinstance.
    First arg is a class   -> issubclass.
"""


class Employee:
    pass


class Manager(Employee):
    pass


class Developer(Employee):
    pass


if __name__ == "__main__":
    mgr = Manager()

    # Correct: object vs class.
    print(isinstance(mgr, Manager))     # True
    print(isinstance(mgr, Employee))    # True  (a subclass instance counts)
    print(isinstance(mgr, Developer))   # False (sibling, unrelated)

    # The classic bug: passing a CLASS to isinstance -> always False, because
    # Manager is an instance of `type`, not of Employee.
    print(isinstance(Manager, Employee))   # False (wrong question)

    # What you actually meant: class-vs-class derivation.
    print(issubclass(Manager, Employee))   # True
    print(issubclass(Manager, Developer))  # False
    print(issubclass(Manager, Manager))    # True (a class is its own subclass)
    print(type(Manager) is type)           # True (classes are instances of type)

    # Expected output:
    #   True
    #   True
    #   False
    #   False
    #   True
    #   False
    #   True
    #   True
