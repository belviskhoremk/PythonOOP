# the property decorator allows us to define a method but access it like an attribute

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    # like this we can do obj.email instead of obj.email(), so we dont break the code
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    #This is a getter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Creating a setter for fullname. we cant create the setter if fullname does not have the property decorator
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # The deleter works almost the same way as the setter
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


emp1 = Employee("John", "Smith")

print(emp1.fullname)
print(emp1.email)
print(emp1.first)

emp1.first='Jim'
print(emp1.fullname)
print(emp1.email)
print(emp1.first)

# Right now, we cannot do the following, even if we add the property decorator
emp1.fullname = "Elvis Blitti"

#So we need to use a setter
print(emp1.fullname)
print(emp1.email)

del emp1.fullname
print(emp1.fullname)
print(emp1.email)