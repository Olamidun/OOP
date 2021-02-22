# SECTION THREE ----- INHERITANCE

'''
Inheritance is the process by which one class takes on the attributes and methods of another class. This newly formed class is called the CHILD class while the other class is called the PARENT/BASE class. Let's illustrate it by creating two classes namely: SoftwareEngineer and Designer. They are both employees in a company.

'''
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} is working")

'''
It it usually generic for an employee to have a name and an age. Software Engineers and Designers alsoo have names and ages; instead of creating a name and age attribute in each of SoftwareEngineer and Designer class, we can just set that attribute in the Employee class and have our SoftwareEngineer and Designer class inherit from it.
So to make our SoftwareEngineer and Designer class inherit the Employee class; we put our Base class in a paretheses like this: NameOfChildClass(ParentClass).
Note that apart from inheriting; we can extend it(add more functionalities), override it(change what the function in the base class does)
'''

class SoftwareEngineer(Employee):
    '''
    To extend, we can just create another instance method in the child class.
    
    '''
    def __init__(self, name, age, level, position, programming_language):
        '''
        We are overriding the init method of the parent class by passing extra arguments.

        since instance attributes for name and age has been defined in the "init function" in the base class; we do not need to create it again in the init function of the child class, what we do instead is call the initializer of the base class using the "super function" like this: 

        '''
        super().__init__(name, age) # we pass in age and name because those are the arguments in the init function of the parent class
        self.level = level
        self.position = position 
        self.programming_language = programming_language
        
   # Extending the parent class by giving the child class that is inheriting it its own instance method(s) 
    def information(self):
        print(f"{self.name} is a {self.level} software developer who develops software with {self.programming_language}")


'''
In the SoftwareEngineer class, we extended the parent class and overrode the "__init__" function, in this class we will override the Parent class' instance method

'''
class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing")
    
    '''
    We override an instance method of the parent class in a child class by creating a function in the child class and giving it the same name as the name of the instance method we want to override and then doing whatever we want with it.
    
    '''
    def work(self):
        print(f"{self.name} is designing")

'''
To create an instance of a child class, you pass in the arguments of the parent class as well aas its own argument(if any) when instantiating
'''
se = SoftwareEngineer('Olamidun', 25, 'Entry Level', 'Junior Developer', 'Python')
de = Designer('Babayega', 25)
# de.draw()
# se.information()
# de.work()