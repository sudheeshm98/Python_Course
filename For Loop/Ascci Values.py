#Ascci value
"""
A is 65    ,   a is 97
Z is 90    ,   z is 122
"""
#To find ascci value
x = ord("A")
print(x)

#To print alphapets

for i in range(65,91):
    print(chr(i), end=" ")

for i in range(97,123):
    print(chr(i), end=" ")

""" OR """

import string

for i in string.ascii_uppercase:
    print(i,end=" ")

for i in string.ascii_lowercase:
    print(i,end=" ")