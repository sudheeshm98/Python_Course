"""
Decorators
----------
A decorator is a design pattern that allows you to modify
the functionality of a function by wrapping it in another function.

The outer function is called the decorator, which takes the original
function as an argument and returns a modified version of it.
"""

#Method-1
def function1(func):                      # define the inner function
    def inner():                          # add some additional behavior to decorated function
        print("Hello")                    # call original function
        func()
    return inner                          # return the inner function

def function2():                          # define ordinary function
    print("Sudhiii")

decorated_func = function1(function2)     # decorate the ordinary function

decorated_func()                          # call the decorated function

#Method-2
def make_pretty(func):
    def inner():
        print("I Love")
        func()
    return inner

@make_pretty
def ordinary():
    print("You")

ordinary()

