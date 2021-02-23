# SECTION FOUR ---- ENCAPSULATION AND ABSTRACTION

'''
Encapsulation is the mechanism of hiding data implementation. This means that instance variables are kept internal. Instance methods can also be kept internal. 
Continuing with our SoftwareEngineer class, The Software Engineer has an overall salary he is being paid at the end of the month, but we do not want to set the overall salary when instantiating the class, instead we want to set the base salary(because the HR knows what the base salary is but doesn't know the number of bugs the developer will solve in a month), as that with other things will be used to calculate the overall salary, this is a good situation for us to set our overall salary as an internal method i.e we do not want to call it like we call a public instance variable because it is not something we know before hand, rather it's calculated based on the base salary and other factors.

'''

class SoftwareEngineer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # internal instance variable(One which we want only the HR and Software Engineer to access)

        self._salary = None # By convention, the internal instance variable is set by preceeding the name of the variable with an underscore. It is set to None initially, because the HR "will come in" to set it to the appropriate amount

        self._num_of_bugs_solved = 0 # We set this to be a internal instance variable because it is only going to be used by an instance method named "code" inside the class, there is no need for it to be increased after we might have instantiated our class. In essence, the number of bugs that will be solved by the developer isn't something that is readily known like age or name.

    def code(self):
        self._num_of_bugs_solved += 1


    # This function is called a getter
    @property
    def salary(self):
        return self._salary

    # This function is called a setter
    @salary.setter
    def salary(self, base_salary):
        '''
        We are setting a base salary here because other compensations are baased on the number of bugs solved by a developer, the only thing that's known is the base salary, there is no way to know the number of bugs a developer will solve in a month, to then calculate the overall salary of an Engineer, an internal instance method called "_calculate_overall salary" is created because the variables to be used to calculate it are internal variables.

        '''
        self._salary = self._calculate_overall_salary(base_salary)

    '''To create an internal instance method, an underscore is used to start the function name like this'''
    def _calculate_overall_salary(self, base_salary):
        if self._num_of_bugs_solved < 10:
            return base_salary
        if self._num_of_bugs_solved < 100:
            return f"NGN {base_salary * 2}"
        return base_salary * 3

se = SoftwareEngineer('Max', 20)

# We can print out the name and age of the Software Engineer because they are not private instance variables
print(se.age, se.name)

for i in range(70):
    se.code()

se.salary = 6000 # We are setting our base salary and then calculating the overall salary based on the number of bugs the Engineer solved in a month. 
print(se.salary)



# ------- ABSTRACTION

'''
 
Abstraction simply means each object should only expose a high level mechanism for using it, it should hide internal implementation details. What this means that if we take a look at line 54 which calls the "get_salary" function, we only exposed a way to make use of our internal instance methods and variables without actually having to worry about how they are implemented, we simply call a function and it does all the "heavy lifting" for us.
So, using the analogy of HR, all the HR simply needs to do is set the salary using the set_salary function and then call get_salary to get the salary without having to worry about the internal implementations of "_calculate_overall_salary".

'''

 
