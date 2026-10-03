"""
__init_subclass__: Hooking Subclass Creation
============================================

__init_subclass__ is a hook called automatically whenever a class is SUBCLASSED
-- not when instances are created. It is the modern, lightweight way (PEP 487)
to register, validate, or configure subclasses without writing a metaclass.

(A class decorator can do similar work, but it must be applied to each class by
hand. __init_subclass__ fires for every subclass automatically.)

Key idea:
    Need "do something every time someone subclasses this"? Use
    __init_subclass__ instead of reaching for a metaclass.
"""


class Plugin:
    registry: dict = {}

    # Implicitly a classmethod. `cls` is the NEW subclass being defined; extra
    # keyword args come from the subclass's class header (see below).
    def __init_subclass__(cls, *, key: str, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        Plugin.registry[key] = cls          # auto-register under the given key


# `key=...` in the header is passed straight to __init_subclass__:
class JsonPlugin(Plugin, key="json"):
    pass


class CsvPlugin(Plugin, key="csv"):
    pass


if __name__ == "__main__":
    # Both subclasses registered themselves at definition time -- no manual
    # registry calls and no decorator on each class.
    print(sorted(Plugin.registry))                 # ['csv', 'json']
    print(Plugin.registry["json"] is JsonPlugin)   # True

    # Look up by key and instantiate:
    obj = Plugin.registry["csv"]()
    print(type(obj).__name__)                       # CsvPlugin

    # Expected output:
    #   ['csv', 'json']
    #   True
    #   CsvPlugin
