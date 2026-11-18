"""Lesson 5 - Special ("magic" / "dunder") methods.

Dunder methods (double underscore, e.g. ``__init__``) let a class hook into
Python's built-in behaviour:

* ``__repr__``: unambiguous representation for developers (debugging,
  logging). Ideally it is valid Python that recreates the object.
* ``__str__``: readable representation for end users. ``str()`` and
  ``print()`` fall back to ``__repr__`` if ``__str__`` is missing, so always
  define at least ``__repr__``.
* ``__add__``, ``__len__``, ...: operator overloading (``a + b``, ``len(a)``).
"""


class Employee:
    """An employee that knows how to print and add itself."""

    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self) -> str:
        """Return the employee's full name."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """Increase pay by ``raise_amount``."""
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self) -> str:
        # Copy-pasting this output into Python recreates the same object.
        return f"Employee({self.first!r}, {self.last!r}, {self.pay!r})"

    def __str__(self) -> str:
        # Human-friendly version.
        return f"{self.fullname()} - {self.pay}"

    def __add__(self, other: "Employee") -> int:
        """``emp1 + emp2`` returns their combined pay."""
        return self.pay + other.pay


def main() -> None:
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Elvis", "Blitti", 60000)

    print(emp1)  # print() uses __str__

    # repr()/str() simply call the dunder methods.
    print(repr(emp1), "==", emp1.__repr__())
    print(str(emp1), "==", emp1.__str__())

    # Built-in types use the same mechanism: 1 + 1 calls int.__add__(1, 1).
    print("\n1 + 1 =", 1 + 1, "| int.__add__(1, 1) =", int.__add__(1, 1))

    print("\nOperator overloading (all three are equivalent):")
    print("emp1 + emp2                 =", emp1 + emp2)
    print("emp1.__add__(emp2)          =", emp1.__add__(emp2))
    print("Employee.__add__(emp1, emp2) =", Employee.__add__(emp1, emp2))


if __name__ == "__main__":
    main()
