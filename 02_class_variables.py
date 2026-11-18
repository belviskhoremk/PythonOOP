"""Lesson 2 - Class variables vs instance variables.

* An **instance variable** belongs to one object (``self.pay``).
* A **class variable** is shared by every instance (``Employee.raise_amount``).

Attribute lookup checks the instance first, then the class. That is why
assigning ``emp.raise_amount = ...`` creates an instance-level override
without touching the other employees.
"""


class Employee:
    """An employee whose pay can be raised by a shared percentage."""

    # Class variables: shared by all instances.
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first: str, last: str, pay: int):
        # Instance variables: unique to each employee.
        self.first = first
        self.last = last
        self.pay = pay
        # Use the class name here: the counter is not per-instance, and
        # ``self.num_of_employees += 1`` would create an instance attribute.
        Employee.num_of_employees += 1

    def fullname(self) -> str:
        """Return the employee's full name."""
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        """Increase pay by ``raise_amount``.

        Uses ``self.raise_amount`` (not ``Employee.raise_amount``) so that a
        subclass or a single instance can override the percentage.
        """
        self.pay = int(self.pay * self.raise_amount)


def main() -> None:
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Elvis", "Blitti", 60000)

    print("Pay before raise:", emp1.pay)
    emp1.apply_raise()
    print("Pay after raise: ", emp1.pay)

    # A class variable is reachable from the class and from every instance.
    print("\nraise_amount for class, emp1, emp2")
    print(Employee.raise_amount, emp1.raise_amount, emp2.raise_amount)

    # Assigning on an instance creates an instance variable that shadows
    # the class variable for that instance only.
    emp1.raise_amount = 1.05
    print("\nraise_amount after setting emp1.raise_amount = 1.05")
    print(Employee.raise_amount, emp1.raise_amount, emp2.raise_amount)

    # The namespaces confirm it: only emp1 has its own raise_amount.
    print("\nemp1.__dict__:", emp1.__dict__)
    print("emp2.__dict__:", emp2.__dict__)

    print("\nNumber of employees:", Employee.num_of_employees)


if __name__ == "__main__":
    main()
