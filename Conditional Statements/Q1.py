#The Number is div by 7 and mult of 5 ?

x = int(input("Enter a Number: "))

if (x%7 == 0) and (x%5 == 0):
    print("The given Number is Divisible by 7 and Multiple of 5")

else:
    print("The Condition is False")

#Find a person can vote or not ?

Age = int(input("Enter the person Age: "))
if Age >= 18:
    print("The Person can Vote")
else:
    print("The Person cannot vote")


