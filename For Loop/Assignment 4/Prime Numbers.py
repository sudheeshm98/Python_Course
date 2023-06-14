#5.Write a program to display all prime numbers within a range

a = int(input("Enter starting Range : "))
b = int(input("Enter Ending Range : "))

print("Prime numbers between", a, "and", b, "are:")

for num in range(a, b + 1):

   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)