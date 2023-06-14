"""
String is a set of charectors
Eg: str = "Hello"

"""
str1 = "Hello World"

#String Indexing
print(str1[1])
print(str1[-1])    #Reverse

#String slicing
print(str1[1:5])
print(str1[-3:])   #Reverse
print(str1[2:])
print(str1[::-1])         #to reverse the whole string
print(str1[-2:-5:-1])      #Reverse order

#String concatenate
x = "Hello"
y = "World"
print(x," "+y)

fruit = 'banana'
for i in range(len(fruit)):
    print(i,fruit[i])

