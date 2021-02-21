# SECTION ONE ----- WHAT IS A CLASS AND HOW TO CREATE ONE
'''
Classes are needed when we want to represent complex data types as objects; say for example, a software engineer objects. A software engineer could have the following things peculiar to them:
- A name
- Position
- Level
- Salary, etc.

Now, all these could be represented in any of the primitive data types in python like lists, dictionary, or tuple.....but what happens if we want to create multiple objects of software engineers, representing each objects as a primitive data type is not only efficient, it is also not flexible...like if we want to add more peculiar things to software engineers. It is also error prone.

A more efficient approach is to leverage the concept of CLASS in python. A CLASS is created this way:

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

 
se1 = SoftwareEngineer('max', 20 , 'Junior', 5000)
print(SoftwareEngineer.alias)