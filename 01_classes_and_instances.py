"""Lesson 1 - Classes and instances.

A *class* is a blueprint; an *instance* is a concrete object built from it.
This lesson shows:

* attaching attributes to instances by hand (and why that is tedious);
* using ``__init__`` (the constructor) to set instance attributes;
* defining methods, and how ``instance.method()`` is just
  ``Class.method(instance)`` under the hood.
"""


class Employee:
    """An empty class: instances get their attributes assigned manually."""


class Student:
    """A student with a first name, last name and age."""

    def __init__(self, first: str, last: str, age: int):
        # ``self`` is the instance being created; these are instance variables.
        self.first = first
        self.last = last
        self.age = age

    def fullname(self) -> str:
        """Return the student's full name."""
        return f"{self.first} {self.last}"


def main() -> None:
    # --- Instances of an empty class -------------------------------------
    emp1 = Employee()
    emp2 = Employee()
    # Each instance is a distinct object with its own memory address.
    print(emp1)
    print(emp2)

    # Instance variables can be attached manually, but this is repetitive
    # and error-prone: that's what __init__ is for.
    emp1.first_name = "John"
    emp1.last_name = "Doe"
    emp1.email = "John.Doe@company.com"

    emp2.first_name = "Elvis"
    emp2.last_name = "Blitti"
    emp2.email = "Elvis.Blitti@company.com"

    print(emp1.first_name)
    print(emp2.first_name)

    # --- Instances created through __init__ ------------------------------
    student_1 = Student("John", "Doe", 22)
    student_2 = Student("Elvis", "Blitti", 22)

    print("\nStudent class")
    print(student_1.first)
    print(student_2.first)

    print("\nFull name built manually")
    print(f"{student_1.first} {student_1.last}")

    print("\nFull name via a method on the instance")
    print(student_1.fullname())
    print(student_2.fullname())

    # instance.method() is syntactic sugar for Class.method(instance).
    print("\nFull name via the method called on the class itself")
    print(Student.fullname(student_2))


if __name__ == "__main__":
    main()
