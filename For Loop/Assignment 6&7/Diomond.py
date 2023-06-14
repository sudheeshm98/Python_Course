#Diomand
rows = int(input("Enter the rows : "))
for i in range(rows-1):
    for a in range(rows-i):
        print(" ", end="")
    for b in range(i+1):
        print("* ", end="")
    print()

for i in range(rows):
    for x in range(i):
        print(" ", end="")
    for y in range(rows-i):
        print(" *", end="")
    print()

