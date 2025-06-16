# A class variable is a variable that is shared between all the instances of the class
# A instance variable is a variable that is most of the time unique to each instance

class Employee:
    #Class variable
    # we can access the class variable using self or using the class name
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        #These are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1      # access using class name. This variable does not belong to any instance and does not need to.

    def fullname(self):
        return '{}, {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)        # access using self. we can change the raise_amount for a particular instance


emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Elvis", "Blitti", 60000)

print(emp1.pay)
emp1.apply_raise()
print("\n After raise")
print(emp1.pay)

# we can access a class variable from both the class and the instance
print("\nPrinting the raise_amount for class, emp1, and emp2")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# We can modify the raise amount for a particular employee
emp1.raise_amount = 1.05
print("\nPrinting the raise_amount for class, emp1, and emp2 after modification of amount of emp1")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)


# Now when we check the namespaces, we see that emp1 has raise_amount in its namespace
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

# we print the number of employees
print("\n",Employee.num_of_employees)

