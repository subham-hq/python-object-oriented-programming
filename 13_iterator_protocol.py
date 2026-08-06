"""
The Iterator Protocol: __iter__ and __next__ (and the generator shortcut)
=========================================================================

- An ITERABLE implements __iter__, returning an iterator.
- An ITERATOR implements __next__ (and returns itself from __iter__),
  raising StopIteration when exhausted.

This is what `for x in obj:` uses under the hood. The manual two-class form
shows the mechanism; in practice you implement __iter__ as a GENERATOR (using
`yield`), which gives you __next__ and StopIteration for free.

Key idea:
    __iter__ hands back something with __next__. Writing __iter__ as a
    generator (`yield`) is the concise, idiomatic way to do it.
"""


# --- Form 1: the explicit mechanism (separate iterator class) ---
class Countdown:
    """An iterable that counts from `start` down to 1."""

    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> "CountdownIterator":
        # Return a FRESH iterator so the object can be looped multiple times.
        return CountdownIterator(self.start)


class CountdownIterator:
    def __init__(self, current: int) -> None:
        self.current = current

    def __iter__(self) -> "CountdownIterator":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# --- Form 2: the same behaviour as a generator (what you'd actually write) ---
class CountdownGen:
    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self):
        # `yield` turns this method into a generator: it automatically provides
        # __next__ and raises StopIteration when the function returns. No
        # separate iterator class, no manual state-tracking.
        n = self.start
        while n > 0:
            yield n
            n -= 1


if __name__ == "__main__":
    cd = Countdown(3)
    print(list(cd))               # [3, 2, 1]
    print([n for n in cd])        # [3, 2, 1]  (works again: fresh iterator)

    it = iter(cd)
    print(next(it), next(it))     # 3 2

    print(list(CountdownGen(3)))  # [3, 2, 1]  (generator form, same result)

    # Expected output:
    #   [3, 2, 1]
    #   [3, 2, 1]
    #   3 2
    #   [3, 2, 1]
