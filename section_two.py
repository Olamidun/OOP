# SECTION TWO ---- FUNCTIONS IN CLASSES

'''
WHY USE FUNCTIONS IN CLASS?

Well, This approach is useful if we want to tie some kind of functionality to a particular data type we are working with; say for example, we want only our software engineer to be able to write code, we could create a function named "write_code" in our class instead of declaring it globally...that way the functionality is only peculiar to our SoftwareEngineer class. A UiUxDesigner class cannot make use of that functionality since it isn't globally created and we can just tie functions or functionalities peculiar to Ui/Ux Designers to its class. 

'''

class SoftwareEngineer:
    '''
    So to implement the peculiarities or atrributes of a software engineer in a class in python, the "__init__" function is used, which basically just initializes or prepares our object to run

    '''

    # Class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # self.argument_name is what is called instance attributes.
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

        '''
        The arguments set in the "__init__" function are the arguments that are taken in when creating an instance of the object.....The instance attributes being set to those attributes tells python that the arguments should be used inside that class whose objects we are creating.

        The difference between a class attribute and instance attribute is that an instance attribute is only tied to one instance of a class and cannot be used on the whole class, while a class attribute can be access without necessarily creating an instance of the class

        '''
    # functions created in a class are called Instance methods; they take in self as a compulsory argument...you can then add more arguments if your function requires it.
    def write_code(self):
        print(f"{self.name} is writing code")

    # You can also give an instance method n argument as you would a normal function e.g:
    def write_code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    
    '''
    SPECIAL METHODS(DUNDER METHOD) IN PYTHON
    Each data type in python has a special method, which is what is executed when an object is converted to the corresponding data type.
    For example, if you have a function in a class that returns a string, you can take advantage of a special method called "__str__" to return the string for you instead of creating that function. For example:
    '''

    def info(self):
        information = f"{self.name}, {self.age}, {self.level}"
        return information

    '''Can be written using a the __str__ special method like this: '''

    def __str__(self):
        information = f"{self.name}, {self.age}, {self.level}"
        return information

    # Another example of dunder method is the "__eq__" method
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

se1 = SoftwareEngineer('max', 20 , 'Junior', 5000)
se2 = SoftwareEngineer('max', 20 , 'Junior', 5000)
# This is the syntax for calling the instance method("write_code") that we create.
se1.write_code_in_language('PYTHON')
print(se1.info())

print(se1 == se2) #This goes into our class and execute the special method; we don't need to append ".__str__()" to execute it.

