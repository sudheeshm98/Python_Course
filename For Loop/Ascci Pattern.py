"""
   A
  B C
 D E F
G H I J
"""
rows = int(input("Enter the rows : "))
A = 65
for i in range(rows):
    for space in range(rows-i):
        print(" ", end="")
    for j in range(i+1):
        print(chr(A), end=" ")
        A = A+1
    print()


