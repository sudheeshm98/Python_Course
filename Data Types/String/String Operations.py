#String Operations

str = "hello world"

print(str.upper())
print(str.lower())
print(str.capitalize())

x = str.count("l")        # Return the number of times the value appears in the string
print(x)

y = str.find("world")     # The find() method finds the first occurrence of the specified value
print(y)

print(str.isalpha())
print(str.isalnum())
print(str.isupper())
print(str.islower())
print(str.isdigit())

print(str.index("world"))  # The index() method is almost the same as the find() method,
                           # the only difference is that the find() method returns -1 if the value is not found
#Replace
print(str.replace("world","SUDHI"))
print(str.replace("l","0",3))

#Join
list = ["cat","rat","dog"]
x = ",".join(list)
print(x)

#Split
str1 = "hello world"
str2 = str.split(" ")
print(str2)

print(sorted(str1))
