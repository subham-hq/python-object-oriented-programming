"""
Descriptors: __get__, __set__, __set_name__
===========================================

A descriptor is a class implementing __get__/__set__ (and optionally
__delete__) that is assigned as a CLASS attribute on another class. It governs
how that attribute behaves on instances. Descriptors are the machinery behind
property, classmethod, staticmethod, and functions-as-methods.

Key idea:
    Reusable, validated attribute logic shared across many fields/classes ->
    write a descriptor once, attach it wherever needed.
"""


class PositiveNumber:
    """A reusable descriptor enforcing a positive numeric value."""

    def __set_name__(self, owner, name: str) -> None:
        # Called automatically when the owning class is created. Gives us the
        # attribute name so each instance can store its own value.
        self._name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self                      # accessed on the class itself
        return getattr(instance, self._name)

    def __set__(self, instance, value) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self._name[1:]} must be a positive number")
        setattr(instance, self._name, value)


class Product:
    # Two independent fields, both validated by the same descriptor class.
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, price: float, quantity: int) -> None:
        self.price = price          # goes through PositiveNumber.__set__
        self.quantity = quantity


if __name__ == "__main__":
    p = Product(10.0, 3)
    print(p.price, p.quantity)      # 10.0 3

    p.price = 12.5                  # validated on assignment
    print(p.price)                  # 12.5

    try:
        p.quantity = -1             # rejected by the descriptor
    except ValueError as e:
        print(f"rejected: {e}")

    # Expected output:
    #   10.0 3
    #   12.5
    #   rejected: quantity must be a positive number
