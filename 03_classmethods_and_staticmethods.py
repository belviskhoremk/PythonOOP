"""Lesson 3 - Class methods and static methods.

* A regular method receives the **instance** (``self``).
* A ``@classmethod`` receives the **class** (``cls``). It is used to change
  class-wide state or as an *alternative constructor*.
* A ``@staticmethod`` receives neither. It is a plain function that lives in
  the class because it is logically related to it.
"""

import datetime


class Employee:
    """An employee, with class-level helpers."""

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1

    def fullname(self) -> str:
        """Return the employee's full name."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """Increase pay by ``raise_amount``."""
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        """Change the raise for every employee (same as ``cls.raise_amount = amount``)."""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        """Alternative constructor: build an employee from ``"First-Last-Pay"``.

        Using ``cls`` instead of ``Employee`` means subclasses get an instance
        of the subclass.
        """
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        """Return True if ``day`` is Monday to Friday.

        Static: it needs neither an instance nor the class.
        """
        return day.weekday() < 5  # 5 = Saturday, 6 = Sunday


def main() -> None:
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Elvis", "Blitti", 60000)

    print("raise_amount:", Employee.raise_amount, emp1.raise_amount, emp2.raise_amount)
    Employee.set_raise_amount(1.05)  # affects the class and every instance
    print("after set_raise_amount(1.05):",
          Employee.raise_amount, emp1.raise_amount, emp2.raise_amount)

    # Without an alternative constructor, every caller has to parse the string.
    first, last, pay = "Do-Re-70000".split("-")
    print("\nManual parsing:", Employee(first, last, int(pay)).fullname())

    # With one, the parsing logic lives in the class.
    new_emp = Employee.from_string("Fa-Sol-90000")
    print("Alternative constructor:", new_emp.fullname(), new_emp.pay)

    my_date = datetime.date(2016, 7, 10)  # a Sunday
    print(f"\nIs {my_date} a workday?", Employee.is_workday(my_date))


if __name__ == "__main__":
    main()
