#4.Write a Python function that takes a number as a parameter and check  the number is prime or not.

def prime(num):
    if num == 1:
        print(num, "is not a prime number")
    else:
        for i in range(2,num):
            if num % i == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                break
prime(7)



