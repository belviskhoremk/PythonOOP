# Python OOP: Object-Oriented Programming in Python

Six small, runnable lessons covering the core of object-oriented programming in
Python. I wrote them while following Corey Schafer's
[Python OOP tutorial series](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc),
then documented each concept in the code.

Every file runs on its own, with no dependencies (Python 3.10+). Read the
module docstring at the top for the theory, then run it to see the output.

## Lessons

| # | File | Concepts |
|---|------|----------|
| 1 | [`01_classes_and_instances.py`](01_classes_and_instances.py) | Classes vs instances, `__init__`, instance variables, methods, `Class.method(instance)` |
| 2 | [`02_class_variables.py`](02_class_variables.py) | Class vs instance variables, attribute lookup order, `__dict__` |
| 3 | [`03_classmethods_and_staticmethods.py`](03_classmethods_and_staticmethods.py) | `@classmethod`, alternative constructors (`from_string`), `@staticmethod` |
| 4 | [`04_inheritance.py`](04_inheritance.py) | Subclasses, `super()`, overriding, mutable-default pitfall, `isinstance` / `issubclass` |
| 5 | [`05_magic_methods.py`](05_magic_methods.py) | `__repr__` vs `__str__`, operator overloading with `__add__` |
| 6 | [`06_property_decorators.py`](06_property_decorators.py) | `@property`, setters and deleters |

## Usage

```bash
git clone https://github.com/belviskhoremk/PythonOOP.git
cd PythonOOP
python 01_classes_and_instances.py
```

## Key takeaways

- `self` is the instance. `instance.method()` is just `Class.method(instance)`.
- Attribute lookup goes **instance → class → parent classes**, which is what
  makes per-instance overrides and inheritance work.
- Use `@classmethod` for alternative constructors, and `@staticmethod` for
  helpers that need neither the instance nor the class.
- Always define `__repr__`; add `__str__` when end users need a friendlier format.
- Prefer `@property` over storing derived values, so they never go stale.

## Credits

The lesson structure follows [Corey Schafer](https://www.youtube.com/@coreyms)'s
excellent OOP series. Comments and refactoring are my own.
