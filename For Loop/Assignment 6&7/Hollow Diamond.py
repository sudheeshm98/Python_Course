#Hollow Diomand
rows = int(input("Enter the rows : "))
for i in range(rows):
    for a in range(rows-i-1):
        print(" ", end="")
    for b in range(i+1):
        if b==0 or b==i:
           print("* ", end="")
        else:
           print("  ", end="")
    print()

for i in range(rows-1):
    for x in range(i+1):
        print(" ", end="")
    for y in range(rows-i):
        if y==0 or y==rows-i-2:
           print("* ", end="")
        else:
            print("  ", end="")
    print()

