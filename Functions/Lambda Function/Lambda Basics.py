"""
Lambda function
---------------
* A lambda function is a small anonymous function.
* A lambda function can take any number of arguments, but can only have one expression.
* The power of lambda is better shown when you use them as an anonymous function inside another function.
  Say you have a function definition that takes one argument, and that argument will be multiplied with
  an unknown number

syntax
lambda arguments(): expression
"""
x = lambda a,b,c: a+b+c
print(x(6,8,9))

# n = 5
# x = lambda a : a * n
# print(x(11))

def myfunc(n):
  return lambda a : a * n
x = myfunc(5)
print(x(11))


