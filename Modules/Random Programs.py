"""
Write a python program to generate a random colour hex,
a random alphapetical string, random value between 2 integers
and a random multiple of 7 between 0&7.
"""

import random

random_numb = random.randint(0,16777215)
hex_num = str(hex(random_numb))
print(hex_num)
hex_num = "3"+hex_num[2:]
print("hex color code is ",hex_num)

s = "python"
str1 = " "
for i in s*2:
    str1 = str1+random.choice(s)
print(str1)

print(random.randint(1,100))

print(random.randrange(0,70,7))




