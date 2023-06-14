"""
A B C D
E F G H
I J K L
M N O P
"""
rows = int(input("Enter the rows : "))
A = 65
for i in range(rows):
    for j in range(rows):
        print(chr(A), end=" ")
        A = A+1
    print()
