# let's create an empty class then create instances with manual instance variable
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

# The print statements will basically show the location where each instance is stored
print(emp1)
print(emp2)

emp1.first_name = "John"    # this is an instance variable
emp1.last_name = "Doe"
emp1.email = 'John.Doe@company.com'

emp2.first_name = "Elvis"
emp2.last_name = "Blitti"
emp2.email = 'Elvis.Blitti@company.com'

print(emp1.first_name)
print(emp2.first_name)



# Now let's create the class with the __init__ method or constructor
class Student:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def fullname(self):
        return '{}, {}'.format(self.first, self.last)

# now we can create the instance variables directly while creating the instance

student_1 = Student("John", "Doe", 22)
student_2 = Student("Elvis", "Blitti", 22)

print("\nStudent Class")
print(student_1)
print(student_2)

print(student_1.first)
print(student_2.first)

# we can print a full name like this. But instead of writing all this everytime, we can create a method in the class
print("\nPrinting manually the full name")
print('{}, {}'.format(student_1.first, student_1.last))

print("\nPrinting the full name with a method call on the instance")
print(student_1.fullname())
print(student_2.fullname())

# We can also call a class method on the class by passing the instance as argument
print("\nPrinting the full name with a method called on the Class itself")
print(Student.fullname(student_2))