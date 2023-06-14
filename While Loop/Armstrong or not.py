"""
What is Armstrong number with example?
An Armstrong number is one whose sum of digits raised to the power three equals the number itself
371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371
"""

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
   dig = temp % 10
   sum = (dig ** 3) + sum
   temp = temp//10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")







