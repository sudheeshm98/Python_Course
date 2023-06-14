"""
Overriding
----------
Method Overriding is a type of Run-time Polymorphism. A child class method
overrides (or provides its implementation) the parent class method of the same name, parameters,
and return type. It is used to over-write (redefine) a parent class method in the derived class
"""
# Parent Class
class A:
    def first(self):
        print("First function of class A")

    def second(self):
        print('Second function of class A')


# Derived Class
class B(A):
    # Overriden Function
    def first(self):
        print("Redefined function of class A in class B")

    def display(self):
        print('Display Function of Child class')


# Driver Code
if (__name__ == "__main__"):
    # Creating child class object
    child_obj = B()

    # Calling the overridden method
    print("Method Overriding\n")
    child_obj.first()

    # Calling the original Parent class method
    # Using parent class object.
    A().first()
