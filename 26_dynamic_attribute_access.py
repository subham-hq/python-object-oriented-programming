"""
Dynamic Attribute Access: __getattr__, __setattr__, __getattribute__
====================================================================

These dunders intercept attribute access:
    __getattr__(self, name)      -> called ONLY when normal lookup fails
                                     (the attribute was not found).
    __setattr__(self, name, val) -> called on EVERY assignment. Must delegate
                                     to super().__setattr__ (or self.__dict__)
                                     or it recurses forever.
    __getattribute__(self, name) -> called on EVERY access. Powerful but easy
                                     to break; rarely needed.

Used to build proxies, lazy/computed attributes, config objects, and ORM-like
models where the attributes are not known ahead of time.

Key idea:
    __getattr__ = fallback for missing attributes. __setattr__ = hook on all
    writes (mind the recursion). Reach for these only when static attributes
    won't do.
"""


class FlexibleConfig:
    """Reads return a default for unknown keys; writes route into a dict."""

    def __init__(self) -> None:
        # This assignment goes through __setattr__ below, which special-cases
        # "_data" and stores it normally via the base implementation.
        self._data = {}

    def __getattr__(self, name: str):
        # Reached only when `name` is NOT a real attribute. `_data` IS a real
        # attribute, so reading it here never re-enters __getattr__ (no
        # recursion).
        return self._data.get(name, f"<unset:{name}>")

    def __setattr__(self, name: str, value) -> None:
        if name == "_data":
            super().__setattr__(name, value)   # store the internal dict normally
        else:
            self._data[name] = value           # route public attrs into the dict


if __name__ == "__main__":
    cfg = FlexibleConfig()
    cfg.host = "localhost"          # intercepted by __setattr__ -> stored in _data
    cfg.port = 5432

    print(cfg.host)                 # localhost  (missing attr -> __getattr__)
    print(cfg.port)                 # 5432
    print(cfg.timeout)              # <unset:timeout>  (default from __getattr__)
    print("host" in cfg._data)      # True  (lives in the dict, not __dict__)
    print(cfg.__dict__)             # {'_data': {'host': 'localhost', 'port': 5432}}

    # Expected output:
    #   localhost
    #   5432
    #   <unset:timeout>
    #   True
    #   {'_data': {'host': 'localhost', 'port': 5432}}
