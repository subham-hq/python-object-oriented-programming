"""
Encapsulation: Conventions and Name Mangling
============================================

Python has no truly private members. Instead:
    name   -> public.
    _name  -> "internal" by convention (please don't touch from outside).
    __name -> name-mangled to _ClassName__name; mainly to avoid accidental
              clashes in subclasses, NOT a security feature.

Key idea:
    Single underscore = "internal, hands off" (convention). Double underscore =
    mangled to dodge subclass name collisions, still reachable if you insist.
"""


class Account:
    def __init__(self, balance: int) -> None:
        self._balance = balance       # internal by convention
        self.__pin = "0000"           # name-mangled

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def get_balance(self) -> int:
        return self._balance


if __name__ == "__main__":
    acc = Account(100)
    acc.deposit(50)
    print(acc.get_balance())     # 150

    # _balance is reachable (nothing stops you) -- it is only a convention:
    print(acc._balance)          # 150

    # __pin is mangled: this attribute name does not exist as written...
    print(hasattr(acc, "__pin"))            # False
    # ...it was renamed to _Account__pin:
    print(acc._Account__pin)                # 0000
    print("_Account__pin" in acc.__dict__)  # True

    # Expected output:
    #   150
    #   150
    #   False
    #   0000
    #   True
