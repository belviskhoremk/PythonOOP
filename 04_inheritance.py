"""Lesson 4 - Inheritance.

A subclass inherits every attribute and method of its parent and can:

* override class variables (``Developer.raise_amount``);
* extend ``__init__`` with extra attributes, delegating the rest to the
  parent through ``super().__init__(...)``;
* add new methods (``Manager.add_employee``).

``isinstance`` and ``issubclass`` let you inspect the hierarchy at runtime.
"""

from __future__ import annotations


class Employee:
    """Base class for every kind of employee."""

    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self) -> str:
        """Return the employee's full name."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """Increase pay by ``raise_amount`` (looked up on the subclass first)."""
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    """An employee who also has a main programming language."""

    raise_amount = 1.10  # overrides Employee.raise_amount for developers only

    def __init__(self, first: str, last: str, pay: int, prog_language: str):
        # Let the parent set first/last/pay, then add our own attribute.
        super().__init__(first, last, pay)
        self.prog_language = prog_language


class Manager(Employee):
    """An employee who supervises a list of other employees."""

    def __init__(self, first: str, last: str, pay: int,
                 employees: list[Employee] | None = None):
        super().__init__(first, last, pay)
        # Never use a mutable default argument (employees=[]): the same list
        # would be shared by every Manager. Use None and create a new list.
        self.employees = employees if employees is not None else []

    def add_employee(self, emp: Employee) -> None:
        """Add ``emp`` to the team if they are not already in it."""
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print(f"Employee {emp.fullname()} is already managed")

    def remove_employee(self, emp: Employee) -> None:
        """Remove ``emp`` from the team if present."""
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print(f"Employee {emp.fullname()} is not managed")

    def list_employees(self) -> None:
        """Print every managed employee."""
        for emp in self.employees:
            print("-->", emp.fullname())


def main() -> None:
    dev1 = Developer("John", "Doe", 50000, prog_language="Python")
    print("Developer pay before raise:", dev1.pay)
    dev1.apply_raise()  # uses Developer.raise_amount = 1.10
    print("Developer pay after raise: ", dev1.pay)

    emp1 = Employee("John", "Doe", 50000)
    print("\nEmployee pay before raise:", emp1.pay)
    emp1.apply_raise()  # uses Employee.raise_amount = 1.04
    print("Employee pay after raise: ", emp1.pay)

    emp2 = Employee("Elvis", "Blitti", 60000)

    manager = Manager("Will", "Smith", 50000, [dev1])
    print("\nEmployees under the manager:")
    manager.list_employees()

    print("\nAfter adding one employee:")
    manager.add_employee(emp2)
    manager.list_employees()

    print("\nisinstance(manager, Manager):  ", isinstance(manager, Manager))
    print("isinstance(manager, Developer):", isinstance(manager, Developer))
    print("issubclass(Manager, Developer):", issubclass(Manager, Developer))
    print("issubclass(Manager, Employee): ", issubclass(Manager, Employee))


if __name__ == "__main__":
    main()
