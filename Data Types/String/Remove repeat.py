"""
Write a python code to remove all the repeating letters from each words of a given sentence.
 Eg: i/p: Let’s google the pineapple  --- o/p: Let’s gole the pineal
"""

str3 = "Let’s google the pineapple"
str1 = str3.split(' ')
print(str1)
str2 = []
for i in str1:
    l = ""
    for j in i:
        if j in l:
            continue
        else:
            l = l + j
    str2.append(l)
print(' '.join(str2))

