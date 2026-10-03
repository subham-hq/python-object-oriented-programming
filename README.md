# Python Object Oriented Programming

Clean, corrected, runnable reference notes for Object-Oriented Programming in
Python. Built from my own study, then rewritten for correctness, type hints, and idiomatic modern Python.

This is a personal revision repo, not a tutorial course. Each file is a focused,
self-contained reference for **one** concept. The workflow is: open a file, read
the top docstring, run it, then read the inline comments at the decision points.

## How to run

Every file runs independently and prints a short demonstration. The expected
output is written at the bottom of each file as comments, so you can verify
behaviour without guessing.

```bash
python 01_classes_and_instances.py
```

Requires **Python 3.10+** (a couple of files use `X | None` annotations, and the
advanced-dataclasses file uses `kw_only`/`slots`). Standard library only — no
dependencies to install.

## Recommended order

Work top to bottom; later files lean on earlier ones. Files 25–32 are the
intermediate/advanced tier — do them after the core (01–24) is solid.

1. **Foundations (01–04)** — classes, methods, class vs instance variables, class/static methods
1. **Inheritance (05–09)** — single & multiple inheritance, MRO, mixins, isinstance vs issubclass
1. **Dunder methods (10–15)** — repr/str, operators, container/iterator/context-manager protocols, eq/hash
1. **Encapsulation & properties (16–18)** — name mangling, properties, descriptors
1. **Abstraction & typing (19–20)** — abstract base classes, protocols & duck typing
1. **Composition (21)** — composition vs inheritance
1. **Modern Python (22–24)** — dataclasses, slots, enums
1. **Advanced dunders (25–26)** — callable objects, dynamic attribute access
1. **Applied OOP (27–29)** — custom exceptions, cached_property, advanced dataclasses
1. **Object model (30–32)** — `__new__` vs `__init__`, `__init_subclass__`, copy semantics

## Concept index

| # | File | One-line takeaway |
|---|------|-------------------|
| 01 | [`01_classes_and_instances.py`](<01_classes_and_instances.py>) | A class is a blueprint; each instance holds its own data. |
| 02 | [`02_instance_methods_and_self.py`](<02_instance_methods_and_self.py>) | Methods receive the instance as `self`; `obj.m()` == `Class.m(obj)`. |
| 03 | [`03_class_variables.py`](<03_class_variables.py>) | Class vars are shared; `self.x = ...` shadows with an instance var. |
| 04 | [`04_classmethods_and_staticmethods.py`](<04_classmethods_and_staticmethods.py>) | `cls` methods (incl. alternate constructors) vs no-arg utilities. |
| 05 | [`05_single_inheritance_and_super.py`](<05_single_inheritance_and_super.py>) | Subclass reuses the parent; chain `__init__` via `super()`. |
| 06 | [`06_method_overriding.py`](<06_method_overriding.py>) | Subclass redefines a method; extend it with `super()`. |
| 07 | [`07_multiple_inheritance_and_mro.py`](<07_multiple_inheritance_and_mro.py>) | C3 MRO; `super()` = next in MRO; the diamond is handled. |
| 08 | [`08_mixins.py`](<08_mixins.py>) | Small behaviour-only classes mixed in via multiple inheritance. |
| 09 | [`09_isinstance_vs_issubclass.py`](<09_isinstance_vs_issubclass.py>) | Object-vs-class vs class-vs-class; the classic always-False bug. |
| 10 | [`10_repr_and_str.py`](<10_repr_and_str.py>) | `__repr__` for devs (eval-able), `__str__` for users; repr is the fallback. |
| 11 | [`11_ arithmetic_and_comparison.py`](<11_ arithmetic_and_comparison.py>) | Operators incl. reflected (`__rmul__`); `total_ordering`; `NotImplemented`. |
| 12 | [`12_container_protocol.py`](<12_container_protocol.py>) | `__len__/__getitem__/__setitem__/__contains__` → behaves like a container. |
| 13 | [`13_iterator_protocol.py`](<13_iterator_protocol.py>) | `__iter__/__next__` + the generator (`yield`) form of `__iter__`. |
| 14 | [`14_context_manager_protocol.py`](<14_context_manager_protocol.py>) | `__enter__/__exit__` guarantee teardown via `with`. |
| 15 | [`15_hash_and_eq.py`](<15_hash_and_eq.py>) | Custom `__eq__` needs a matching `__hash__` over the same fields. |
| 16 | [`16_encapsulation_and_name_mangling.py`](<16_encapsulation_and_name_mangling.py>) | `_x` is convention, `__x` is mangled; no true privacy. |
| 17 | [`17_property_decorators.py`](<17_property_decorators.py>) | Expose computed/validated attributes without changing call sites. |
| 18 | [`18_descriptors.py`](<18_descriptors.py>) | Reusable `__get__/__set__` logic; the machinery behind `property`. |
| 19 | [`19_abstract_base_classes.py`](<19_abstract_base_classes.py>) | Enforce an interface; an abstract class can't be instantiated. |
| 20 | [`20_protocols_and_duck_typing.py`](<20_protocols_and_duck_typing.py>) | Structural typing — conform by shape, not by inheritance. |
| 21 | [`21_composition_vs_inheritance.py`](<21_composition_vs_inheritance.py>) | IS-A (inherit) vs HAS-A (compose & delegate). |
| 22 | [`22_dataclasses.py`](<22_dataclasses.py>) | Auto `__init__/__repr__/__eq__`; `default_factory`; `frozen`/`order`. |
| 23 | [`23_slots.py`](<23_slots.py>) | A fixed attribute layout saves memory and removes `__dict__`. |
| 24 | [`24_enums.py`](<24_enums.py>) | Named constant singletons instead of magic strings/ints. |
| 25 | [`25_callable_objects.py`](<25_callable_objects.py>) | `__call__` makes instances callable; basis for class-based decorators. |
| 26 | [`25_dynamic_attribute_access.py`](<25_dynamic_attribute_access.py>) | `__getattr__`/`__setattr__` intercept attribute reads/writes. |
| 27 | [`27_custom_exceptions.py`](<27_custom_exceptions.py>) | One base error + subclasses; carry context; chain with `raise ... from`. |
| 28 | [`28_cached_property.py`](<28_cached_property.py>) | Compute an expensive derived value once, then cache it on the instance. |
| 29 | [`29_dataclasses_advanced.py`](<29_dataclasses_advanced.py>) | `__post_init__`, `field` options, `kw_only`, `slots`. |
| 30 | [`30_new_vs_init.py`](<30_new_vs_init.py>) | `__new__` creates the instance, `__init__` initialises it. |
| 31 | [`31_init_subclass.py`](<31_init_subclass.py>) | `__init_subclass__` auto-registers/validates subclasses (no metaclass). |
| 32 | [`32_copy_vs_deepcopy.py`](<32_copy_vs_deepcopy.py>) | Shallow copy shares nested objects; deep copy duplicates them. |

## Common gotchas (the traps worth memorising)

- **`isinstance` vs `issubclass`** — `isinstance` takes an *object*; `issubclass` takes a *class*. `isinstance(SomeClass, Base)` is always `False`, because a class is an instance of `type`. (File 09.)
- **Mutable default arguments** — never `def f(x=[])`. The list is created once and shared across every call. Use `None` + create inside, or `field(default_factory=list)` in dataclasses. (Files 06, 22.)
- **Class vs instance variables** — `self.x = ...` always creates an *instance* variable that shadows the class one, for that object only. (File 03.)
- **`__eq__` without `__hash__`** — defining `__eq__` makes the object unhashable unless you also define `__hash__`; hash the same fields you compare. (File 15.)
- **`super()` is not "the parent"** — it is "the next class in the MRO". Under multiple inheritance that may be a sibling, not a base. (File 07.)
- **`__slots__` removes `__dict__`** — saves memory but blocks adding undeclared attributes, and breaks `cached_property` unless you add `"__dict__"` to the slots. (Files 23, 28.)
- **`__setattr__` recursion** — `__setattr__` fires on *every* assignment, so `self.x = v` inside it recurses forever; delegate to `super().__setattr__` or write to `self.__dict__`. (File 26.)
- **Subclass `Exception`, not `BaseException`** — `BaseException` also catches `KeyboardInterrupt`/`SystemExit`, which you almost never want to swallow. (File 27.)
- **`__new__` must return the instance** — forget the `return`, or return the wrong object, and `__init__` is skipped (or runs on the wrong thing). (File 30.)
- **Shallow copy shares nested state** — `copy.copy` duplicates only the outer object; mutating a shared inner list/dict affects both. Use `copy.deepcopy` when you need full independence. (File 32.)

## Attribution

Foundational examples adapted from Corey Schafer's Python OOP series, then
rewritten and extended (type hints, reflected operators, generator-based
iterators, descriptors, ABCs, protocols, dataclasses, slots, enums, callable
objects, dynamic attributes, custom exceptions, cached properties, `__new__`,
`__init_subclass__`, and copy semantics). Standard library only.

## License

MIT — see `LICENSE`.