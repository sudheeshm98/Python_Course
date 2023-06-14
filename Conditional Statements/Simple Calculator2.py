A = int(input("Enter 1st Number :"))
B = int(input("Enter 2nd Number :"))
C = input("Enter the Choice (+,-,*,/) = ")

if C == '+':
    print("The Sum is ", A+B)
elif C == '-':
    print("The Difference is ", A-B)
elif C == '*':
    print("The Product is ", A*B)
elif C == '/':
    print("The Quotient is ", A/B)
else:
    print("Invalid Operation")


