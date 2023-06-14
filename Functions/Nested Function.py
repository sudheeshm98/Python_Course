"""
Nested Function  -- Fn inside a fn
"""
#Ex - 1
def outer_func():
    def inner_func():
        print("HI SUDHI")

    inner_func()
outer_func()

#Ex - 2
def increment(number):
    def inner_increment():
        return number+1
    return inner_increment()

print(increment(10))

#Ex - 3
def function1():
    p = "Hello World"
    def function2():
        print(p)
    function2()
function1()

