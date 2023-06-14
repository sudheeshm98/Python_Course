#2. Write a program to display product of the digits of a number accepted from the user.

N = int(input("Enter a Number : "))
Num = str(N)

prod = 1
for i in Num:
    prod = prod * int(i)
    print(i)

print("Product:", prod)

