"""
Context Manager Protocol: __enter__ and __exit__
================================================

The `with` statement uses these dunders to guarantee setup/teardown even when
an exception occurs:
    __enter__ -> runs on entry; its return value is bound by `as`.
    __exit__  -> runs on exit (always); return True to SUPPRESS an exception,
                 falsey to let it propagate.

Key idea:
    Use a context manager whenever something must be released/closed reliably
    (files, locks, connections, timers).
"""


class ManagedResource:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self) -> "ManagedResource":
        print(f"open {self.name}")
        return self                       # bound to the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        # Runs even on error. exc_* are None on a clean exit.
        print(f"close {self.name}")
        return False                      # do not suppress exceptions


if __name__ == "__main__":
    with ManagedResource("db") as res:
        print(f"using {res.name}")

    # Teardown still runs when the block raises:
    try:
        with ManagedResource("file"):
            raise ValueError("boom")
    except ValueError as e:
        print(f"caught: {e}")

    # Expected output:
    #   open db
    #   using db
    #   close db
    #   open file
    #   close file
    #   caught: boom
