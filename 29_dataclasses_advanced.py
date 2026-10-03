"""
Dataclasses, Advanced: __post_init__, field options, kw_only, slots
===================================================================

Beyond the basics (file 22), dataclasses support:
- __post_init__ : runs after the generated __init__; use it to validate or
                  compute derived fields.
- field(...)    : per-field control -- repr=False, compare=False, init=False,
                  default / default_factory.
- kw_only=True  : force keyword-only construction (Python 3.10+).
- slots=True    : generate __slots__ for memory savings (Python 3.10+).

Key idea:
    Reach for these when a dataclass needs validation, derived fields, or a
    memory-efficient / keyword-only construction contract.
"""

from dataclasses import dataclass, field


@dataclass(kw_only=True, slots=True)   # keyword-only construction + __slots__
class Account:
    owner: str
    balance: float = 0.0
    # Derived in __post_init__, so it is NOT a constructor argument:
    is_overdrawn: bool = field(init=False)
    # Kept out of repr (e.g. a secret or noisy field):
    token: str = field(default="xxxx", repr=False)

    def __post_init__(self) -> None:
        # Validation/derivation belongs here -- __init__ is auto-generated.
        self.is_overdrawn = self.balance < 0


if __name__ == "__main__":
    # kw_only=True -> must use keywords; Account("Subham") would be a TypeError.
    a = Account(owner="Subham", balance=100.0)
    print(a)                       # token hidden by repr=False
    print(a.is_overdrawn)          # False (set in __post_init__)

    b = Account(owner="Test", balance=-50.0)
    print(b.is_overdrawn)          # True

    # slots=True -> no __dict__, and undeclared attributes are rejected:
    print(hasattr(a, "__dict__"))  # False
    try:
        a.note = "hi"
    except AttributeError as e:
        print(f"blocked: {type(e).__name__}")

    # Expected output:
    #   Account(owner='Subham', balance=100.0, is_overdrawn=False)
    #   False
    #   True
    #   False
    #   blocked: AttributeError
