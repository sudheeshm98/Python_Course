#Arithmetic Operators
A = 5
B = 7
print(A+B)
print(A-B)

#Assingment Operators
X = 10
X += 5    #X=X+5
print(X)

#Comparisson Operators  --  True/False
x = 5
Y = 7
print(x == Y)    # returns False because X is not equal to Y
print(X > Y)

#Logical Operators
X = 5
print(X > 6 and X < 10)      # Returns True if both statements are true
print(X > 6 or X < 10)       # Returns True if one of the statements is true
print(not(X > 6 or X < 10))  # Reverse the result, returns False if the result is true

#Identity Operators
x = ["black", "red"]
y = ["black", "red"]
z = x
print(x is z)         # returns True because z is the same object as x
print(x is not z)     # returns False because x is not the same object as y, even if they have the same content

#Membership Operators
x = ["apple", "banana"]
print("banana" in x)       # returns True because a sequence with the value "banana" is in the list
print("banana" not in x)




