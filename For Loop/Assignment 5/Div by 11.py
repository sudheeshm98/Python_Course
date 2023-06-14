#4. Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.
for i in range(100,501):
    if(i%11==0) and (i%2!=0):
        print(i)
