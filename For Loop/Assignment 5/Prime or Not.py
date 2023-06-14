#1. Write a program to check whether a number is prime or not ..?
Num = int(input("Enter a Number : "))
if Num>1:
    for i in range(2,Num):
        if Num%i == 0:
            print(Num,"Is not a Prime Number")
            break
    else:
        print(Num, "Is a Prime Number")
else:
    print(Num, "Is not a Prime Number")

