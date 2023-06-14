#Half Pyramid
rows = int(input("Enter the rows : "))
for i in range(rows):
    for star in range(i+1):
        print("* ", end="")

    print()

#Half Pyramid
rows = int(input("Enter the rows : "))
for i in range(rows):
    for star in range(rows-i):
        print("* ", end="")

    print()