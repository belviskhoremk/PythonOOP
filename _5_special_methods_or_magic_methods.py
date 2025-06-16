# __init__ is also called dunder init
# we should have at least the repr method, because if we call the str method and it does not exist, it falls back directly to the repr method
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        # this method is an unambiguous representation of the object. used for debugging, logging by other developers
        # Try to display something you can copy-paste back in the python code to recreate that same object
        return "Employee('{}', '{}',  '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        # Dunder string method
        # readable representation of an object. meant to be display to the end-user
        return "{}-{}".format(self.fullname(), self.pay)

    # Let's create a dunder method to overload the addition operator
    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Elvis', 'Blitti', 60000)
print(emp1)

# Doing this
print(repr(emp1))
print(str(emp1))
# is same as doing this
print(emp1.__repr__())
print(emp1.__str__())

# Notice that we can do operator overloading using dunder methods
print(1+1)
print(int.__add__(1, 1))

print("\nOperator overloading")
# These will call the __add__ method and are the same thing
print("Doing emp1+emp2", emp1+emp2)
print("Doing emp1.__add__(emp2)", emp1.__add__(emp2))
print("Doing Employee.__add__(emp1, emp2)", Employee.__add__(emp1, emp2))
