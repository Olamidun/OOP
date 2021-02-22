# SECTION THREE ----- INHERITANCE

'''
Inheritance is the process by which one class takes on the attributes and methods of another class. This newly formed class is called the CHILD class while the other class is called the PARENT/BASE class. Let's illustrate it by creating two classes namely: SoftwareEngineer and Designer. They are both employees in a company.

'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''
It it usually generic for an employee to have a name and an age. Software Engineers and Designers alsoo have names and ages; instead of creating a name and age attribute in each of SoftwareEngineer and Designer class, we can just set that attribute in the Employee class and have our SoftwareEngineer and Designer class inherit from it.
So to make our SoftwareEngineer and Designer class inherit the Employee class; we put our Base class in a paretheses like this: NameOfChildClass(ParentClass).
Note that apart from inheriting; we can extend it(add more functionalities), override it(change what the function in the base class does)
'''

class SoftwareEngineer(Employee):
    pass


class Designer(Employee):
    pass