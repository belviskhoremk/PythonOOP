#  a class method works on the class directly and modifies variable for all instance
# a static method is not related to any instance or even the class itself. It is just a method that does some task without involving the class and its instances

class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Let's create a class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Use the classmethod as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        #now we return the class
        return cls(first, last, pay)

    # Let's create a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Elvis", "Blitti", 60000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.set_raise_amount(1.05)     # It's the same as Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# we can use the classmethod as an alternative constructor
# suppose a case where we have to create an instance from a string

emp_str_1 = "Do-Re-70000"
first, last, pay = emp_str_1.split("-")
new_emp = Employee(first, last, pay)
print(new_emp.fullname())

# instead of having to parse the string everytime we create a new instance, we can just add a method to the class called from_string
print("\n\nAlternative constructor as class method")
emp_str_2 = "Fa-Sol-90000"
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.fullname())

# Let's try our static method
print("\n\nStatic method")
import datetime
my_date = datetime.date(2016, 7, 10)
print(my_date)
print(Employee.is_workday(my_date))