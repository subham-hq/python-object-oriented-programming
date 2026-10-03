"""
functools.cached_property
=========================

@cached_property turns a method into an attribute that is computed once, on
first access, then cached on the instance. Later accesses return the stored
value without recomputing -- useful for expensive derived data.

Caveats:
- The instance needs a writable __dict__, so it does NOT work with __slots__
  unless you add "__dict__" to the slots.
- The cache lasts for the object's lifetime; clear it with `del obj.attr`.
- Use a plain @property when the value is cheap or must always be fresh.

Key idea:
    Expensive, derived, and stable for the object's life -> @cached_property.
    Cheap or must stay live -> @property.
"""

from functools import cached_property


class Dataset:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers
        self.compute_count = 0      # proves the body runs only once

    @cached_property
    def total(self) -> int:
        # Pretend this is expensive. It should run only on first access.
        self.compute_count += 1
        return sum(self.numbers)


if __name__ == "__main__":
    ds = Dataset([1, 2, 3, 4])

    print(ds.total)                # 10  (computed now)
    print(ds.total)                # 10  (served from cache)
    print(ds.compute_count)        # 1   (body ran only once)

    # The cached value now lives on the instance, shadowing the descriptor:
    print("total" in ds.__dict__)  # True

    # Clear the cache to force recompute on next access:
    del ds.total
    print(ds.total)                # 10  (recomputed)
    print(ds.compute_count)        # 2

    # Expected output:
    #   10
    #   10
    #   1
    #   True
    #   10
    #   2
