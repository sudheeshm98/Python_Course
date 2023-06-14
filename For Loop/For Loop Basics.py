"""
for loop is used for iterating over a sequence

Syntax
------
for value in sequence:
    print(value)
"""
for X in "SUDHI":
    print(X)

A = 123        #integers are cannot be iterate directly
B = str(A)     #int -- str  Then it can be iterable
for x in B:
    print(x)

#Break
for i in range(1,11):
    if i == 5:
        break    # Terminates the current loop
    print(i)

#Continue
for i in range(1,11):
    if i == 5:
        continue    # ignores the rest of the statements inside a loop, and continues with the next iteration
    print(i)

#Pass
for i in range(1,11):
    pass               # Nothing happens when pass is executed
