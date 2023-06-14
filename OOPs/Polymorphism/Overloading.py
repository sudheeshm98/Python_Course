"""
Overloading
----------
Method Overloading in Python is a type of Compile-time Polymorphism using which we can define
two or more methods in the same class with the same name but with a different parameter list.
"""
# Function to take multiple arguments
def sum_number(*args):
    # variable to store the sum of numbers
    result = 0

    # accessing the arguments
    for num in args:
        result += num

    # Output
    print("Sum : ", result)


# Driver Code
if (__name__ == "__main__"):
    print("Similar to Method Overloading\n")
    print("Single Argument    ->", end=" ")
    sum_number(10)

    print("Two Arguments      ->", end=" ")
    sum_number(30, 2)

    print("Multiple Arguments ->", end=" ")
    sum_number(1, 2, 3, 4, 5)