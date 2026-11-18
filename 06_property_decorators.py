"""Lesson 6 - Property decorators: getters, setters and deleters.

``@property`` lets you define a method but access it like an attribute
(``emp.email`` instead of ``emp.email()``). This keeps derived values such as
``email`` in sync with the data they come from, without breaking code that
already reads them as attributes.

``@<name>.setter`` and ``@<name>.deleter`` define what happens on assignment
(``emp.fullname = "..."``) and deletion (``del emp.fullname``).
"""


class Employee:
    """An employee whose email and full name are derived from first/last."""

    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last
        # Storing the email here would go stale when `first` changes:
        # self.email = f"{first}.{last}@email.com"

    @property
    def email(self) -> str:
        """Email address, always computed from the current name."""
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self) -> str:
        """Getter: ``emp.fullname``."""
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        """Setter: ``emp.fullname = "First Last"`` updates first and last."""
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self) -> None:
        """Deleter: ``del emp.fullname`` clears first and last."""
        print("Deleting name...")
        self.first = None
        self.last = None


def main() -> None:
    emp1 = Employee("John", "Smith")
    print(emp1.fullname, "|", emp1.email)

    # Because email is a property, it follows changes to `first`.
    emp1.first = "Jim"
    print(emp1.fullname, "|", emp1.email)

    # Without the setter this line would raise AttributeError.
    emp1.fullname = "Elvis Blitti"
    print(emp1.fullname, "|", emp1.email)

    del emp1.fullname
    print(emp1.fullname, "|", emp1.email)


if __name__ == "__main__":
    main()
