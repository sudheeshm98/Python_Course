"""
1. is y div by 2 or not
2. is y div by 5 or not

if y satisfies both conditions y is appended to new_list
"""

my_list = [10,15,20,25,30,35,40,45,50]
new_list = [y for y in my_list if y%2 == 0 and y%5 == 0]
print(new_list)
