"""
#To find sum of n natural numbers without for loop
n = int(input("Enter the Number : "))
sum = 0    # Initial value
if n>0:    # Condition
    sum = n*(n+1)/2    # Statement
    print(sum)
else:
    print("No Value")
"""
#To find sum of n natural numbers using for loop
print("Sum of n Natural Numbers")
num = int(input("Enter the Number : "))
sum = 0 # Initialize
for i in range(1,num+1):
    sum = sum + i  #1,3,6,10,15.....
print(sum)
