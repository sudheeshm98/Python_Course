"""
Python f-string
---------------

"""

name = "SUDHI"
age = 25

print('%s is %d years old' %(name,age))
print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')              # f-string method (Most used)

bags = 5
apples_in_bag  = 10

print(f'There are total of {bags * apples_in_bag} apples')