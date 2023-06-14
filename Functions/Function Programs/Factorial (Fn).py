#3.Write a Python function to calculate the factorial of a number (a non-negative integer).
#The function accepts the number as an argument.

def factorial(n):
    if n<0:
        return f'Number should be less than zero!!!'
    else:
        prod = 1
        for i in range(1,n+1):
            prod *= i
        return prod
print(factorial(10))

