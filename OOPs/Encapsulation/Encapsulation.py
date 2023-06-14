"""
Encapsulation
-------------

"""

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self._salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self._salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()
