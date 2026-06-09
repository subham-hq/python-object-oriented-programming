# Python OOP — Revision Reference

Clean, corrected, runnable reference notes for Object-Oriented Programming in
Python. Built from my own study (Corey Schafer's OOP series as the starting
point), then rewritten for correctness, type hints, and idiomatic modern Python.

This is a personal revision repo, not a tutorial course. Each file is a focused,
self-contained reference for **one** concept. The workflow is: open a file, read
the top docstring, run it, then read the inline comments at the decision points.

## How to run

Every file runs independently and prints a short demonstration. The expected
output is written at the bottom of each file as comments, so you can verify
behaviour without guessing.

```bash
python 01_foundations/01_classes_and_instances.py
```

Requires **Python 3.10+** (a couple of files use `X | None` annotations, and the
advanced-dataclasses file uses `kw_only`/`slots`). Standard library only — no
dependencies to install.

## Recommended order

Work top to bottom; later sections lean on earlier ones. Sections 08–09 are the
intermediate/applied tier — do them after the core (01–07) is solid.

1. `01_foundations/` — classes, methods, class vs instance variables, class/static methods
2. `02_inheritance/` — single & multiple inheritance, MRO, mixins, isinstance vs issubclass
3. `03_dunder_methods/` — repr/str, operators, container/iterator/context-manager protocols, eq/hash
4. `04_encapsulation_and_properties/` — name mangling, properties, descriptors
5. `05_abstraction_and_typing/` — abstract base classes, protocols & duck typing
6. `06_composition/` — composition vs inheritance
7. `07_modern_python/` — dataclasses, slots, enums
8. `08_advanced_dunders/` — callable objects, dynamic attribute access
9. `09_applied_oop/` — custom exceptions, cached_property, advanced dataclasses

## Concept index

| # | File | One-line takeaway |
|---|------|-------------------|
| 01 | classes_and_instances | A class is a blueprint; each instance holds its own data. |
| 02 | instance_methods_and_self | Methods receive the instance as `self`; `obj.m()` == `Class.m(obj)`. |
| 03 | class_variables | Class vars are shared; `self.x = ...` shadows with an instance var. |
| 04 | classmethods_and_staticmethods | `cls` methods (incl. alternate constructors) vs no-arg utilities. |
| 05 | single_inheritance_and_super | Subclass reuses the parent; chain `__init__` via `super()`. |
| 06 | method_overriding | Subclass redefines a method; extend it with `super()`. |
| 07 | multiple_inheritance_and_mro | C3 MRO; `super()` = next in MRO; the diamond is handled. |
| 08 | mixins | Small behaviour-only classes mixed in via multiple inheritance. |
| 09 | isinstance_vs_issubclass | Object-vs-class vs class-vs-class; the classic always-False bug. |
| 10 | repr_and_str | `__repr__` for devs (eval-able), `__str__` for users; repr is the fallback. |
| 11 | arithmetic_and_comparison | Operator overloading; `total_ordering`; return `NotImplemented`. |
| 12 | container_protocol | `__len__/__getitem__/__setitem__/__contains__` → behaves like a container. |
| 13 | iterator_protocol | `__iter__/__next__` + `StopIteration` drive the `for` loop. |
| 14 | context_manager_protocol | `__enter__/__exit__` guarantee teardown via `with`. |
| 15 | hash_and_eq | Custom `__eq__` needs a matching `__hash__` over the same fields. |
| 16 | encapsulation_and_name_mangling | `_x` is convention, `__x` is mangled; no true privacy. |
| 17 | property_decorators | Expose computed/validated attributes without changing call sites. |
| 18 | descriptors | Reusable `__get__/__set__` logic; the machinery behind `property`. |
| 19 | abstract_base_classes | Enforce an interface; an abstract class can't be instantiated. |
| 20 | protocols_and_duck_typing | Structural typing — conform by shape, not by inheritance. |
| 21 | composition_vs_inheritance | IS-A (inherit) vs HAS-A (compose & delegate). |
| 22 | dataclasses | Auto `__init__/__repr__/__eq__`; `default_factory`; `frozen`/`order`. |
| 23 | slots | A fixed attribute layout saves memory and removes `__dict__`. |
| 24 | enums | Named constant singletons instead of magic strings/ints. |
| 25 | callable_objects | `__call__` makes instances callable; basis for class-based decorators. |
| 26 | dynamic_attribute_access | `__getattr__`/`__setattr__` intercept attribute reads/writes. |
| 27 | custom_exceptions | One base error + subclasses; carry context; chain with `raise ... from`. |
| 28 | cached_property | Compute an expensive derived value once, then cache it on the instance. |
| 29 | dataclasses_advanced | `__post_init__`, `field` options, `kw_only`, `slots`. |

## Common gotchas (the traps worth memorising)

- **`isinstance` vs `issubclass`** — `isinstance` takes an *object*; `issubclass` takes a *class*. `isinstance(SomeClass, Base)` is always `False`, because a class is an instance of `type`. (File 09.)
- **Mutable default arguments** — never `def f(x=[])`. The list is created once and shared across every call. Use `None` + create inside, or `field(default_factory=list)` in dataclasses. (Files 06, 22.)
- **Class vs instance variables** — `self.x = ...` always creates an *instance* variable that shadows the class one, for that object only. (File 03.)
- **`__eq__` without `__hash__`** — defining `__eq__` makes the object unhashable unless you also define `__hash__`; hash the same fields you compare. (File 15.)
- **`super()` is not "the parent"** — it is "the next class in the MRO". Under multiple inheritance that may be a sibling, not a base. (File 07.)
- **`__slots__` removes `__dict__`** — saves memory but blocks adding undeclared attributes, and breaks `cached_property` unless you add `"__dict__"` to the slots. (Files 23, 28.)
- **`__setattr__` recursion** — `__setattr__` fires on *every* assignment, so `self.x = v` inside it recurses forever; delegate to `super().__setattr__` or write to `self.__dict__`. (File 26.)
- **Subclass `Exception`, not `BaseException`** — `BaseException` also catches `KeyboardInterrupt`/`SystemExit`, which you almost never want to swallow. (File 27.)

## Attribution

Foundational examples adapted from Corey Schafer's Python OOP series, then
rewritten and extended (type hints, `NotImplemented` handling, descriptors,
ABCs, protocols, dataclasses, slots, enums, callable objects, dynamic
attributes, custom exceptions, cached properties). Standard library only.

## License

MIT — see `LICENSE`.
