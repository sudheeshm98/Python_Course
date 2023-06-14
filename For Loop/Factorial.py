#To find factorial of a Number
x = int(input("Enter a Number : "))
fact = 1
for i in range(1, x+1):
    fact = fact * i
print("The factorial of", x, "is", fact)

