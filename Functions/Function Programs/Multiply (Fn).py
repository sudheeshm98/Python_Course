#1.Multiply all the numbers in a list using function

def mult(list1):
    x = 1
    for i in list1:
        x *= i
    return x
list1 = [2,5,4,8,7,9,6]
print(mult(list1))

