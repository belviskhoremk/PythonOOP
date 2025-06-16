#Inheritance allows to inherit attributes and methods from a parent class

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

"""
class Developer(Employee):
    pass

class Manager(Employee):
    pass
# we see that we can initialize te developer instance even tough the class is empty
dev1 = Developer("John", "Doe", 50000)
emp1 = Employee("Elvis", "Blitti", 60000)
print(dev1.fullname())
print(emp1.fullname())
"""

class Developer(Employee):
    raise_amount = 1.10     # we can modify the class variables values and make them specific to this class

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

# Create a developer instance
dev1 = Developer("John", "Doe", 50000, prog_language="Python")

print("\nDev 1 before raise", dev1.pay)
dev1.apply_raise()
print("Dev 1 before raise", dev1.pay)

# Create an employee instance
emp1 = Employee("John", "Doe", 50000)

print("\nEmployee 1 before raise", emp1.pay)
emp1.apply_raise()
print("Employee 1 after raise", emp1.pay)

emp2 = Employee("Elvis", "Blitti", 60000)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("Employee {} already exists".format(emp))

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("Employee {} doesn't exist".format(emp))

    def list_employees(self):
        for emp in self.employees:
            print("-->", emp.fullname())

manager = Manager("Will", "Smith", 50000, [dev1])
print("\nEmployees under the manager")
manager.list_employees()

print("\nLets add one employee")
manager.add_employee(emp2)
manager.list_employees()

# We can check if an object is an instance of a class
print(isinstance(manager, Manager))
print(isinstance(manager, Developer))

# We can check if a class is a subclass of another class
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))


