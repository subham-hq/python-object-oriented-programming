"""
Dataclasses
===========

@dataclass auto-generates __init__, __repr__, and __eq__ from annotated fields,
removing boilerplate for data-holding classes. Options: order=True adds
comparisons; frozen=True makes instances immutable (and hashable). Use
field(default_factory=...) for mutable defaults like lists.

Key idea:
    For "mostly data" classes, reach for @dataclass instead of hand-writing
    __init__/__repr__/__eq__.
"""

from dataclasses import dataclass, field


@dataclass(order=True)        # order=True -> <, >, etc. derived from field order
class Point:
    x: int
    y: int


@dataclass
class Cart:
    owner: str
    # A mutable default MUST use default_factory, never `items: list = []`,
    # otherwise every instance would share one list.
    items: list = field(default_factory=list)


@dataclass(frozen=True)       # immutable + hashable
class Config:
    debug: bool = False


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)                 # auto __repr__ -> Point(x=1, y=2)
    print(p1 == p2)           # auto __eq__ -> True
    print(p1 < Point(2, 0))   # auto ordering -> True (compares (1,2) < (2,0))

    c = Cart("Subham")
    c.items.append("book")
    print(c)                  # Cart(owner='Subham', items=['book'])
    print(Cart("X").items)    # [] (independent list, thanks to default_factory)

    cfg = Config()
    print(isinstance(hash(cfg), int))  # True (frozen -> hashable)
    try:
        cfg.debug = True               # frozen -> assignment blocked
    except Exception as e:
        print(type(e).__name__)        # FrozenInstanceError

    # Expected output:
    #   Point(x=1, y=2)
    #   True
    #   True
    #   Cart(owner='Subham', items=['book'])
    #   []
    #   True
    #   FrozenInstanceError
