"""
__new__ vs __init__
===================

Two distinct steps build an object:
    __new__(cls, ...)   -> CREATES and returns the new (still-empty) instance.
                           Runs first; it is implicitly a static/class method.
    __init__(self, ...) -> INITIALISES the already-created instance. Runs
                           second and returns None.

You rarely override __new__. You need it when you must control creation itself:
caching/singletons, subclassing immutable types (int, str, tuple), or returning
a different or existing object.

Key idea:
    __new__ makes the object; __init__ fills it in. Override __new__ only when
    you must influence creation; otherwise __init__ is all you need.
"""


class Logger:
    """Singleton: __new__ returns the same instance every time."""

    _instance = None

    def __new__(cls) -> "Logger":
        if cls._instance is None:
            # Create the single shared instance exactly once.
            cls._instance = super().__new__(cls)
        return cls._instance


class CelsiusInt(int):
    """Subclassing an immutable type: the value must be fixed in __new__,
    because by the time __init__ runs the int object already exists."""

    def __new__(cls, value: int) -> "CelsiusInt":
        # Clamp at absolute zero (-273). int is immutable, so set the value
        # here, during creation -- __init__ would be too late to change it.
        return super().__new__(cls, max(value, -273))


if __name__ == "__main__":
    a = Logger()
    b = Logger()
    print(a is b)              # True  (same single instance)

    t = CelsiusInt(-300)
    print(t)                   # -273  (clamped during __new__)
    print(isinstance(t, int))  # True
    print(t + 10)              # -263  (behaves like a normal int)

    # Expected output:
    #   True
    #   -273
    #   True
    #   -263
