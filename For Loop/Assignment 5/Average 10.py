#3. Accept 10 numbers from the user and display their average
sum = 0
for i in range(0,10):
    n = int(input("Enter a Number : "))
    sum = sum + n
    avg = sum/10
print("Average = ",avg)
