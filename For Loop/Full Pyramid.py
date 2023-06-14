#Full Pyramid

rows = int(input("Enter the rows : "))      # 5
for i in range(0,rows):                    # 0,1,2,3,...
    for space in range(0,rows-i):              # 5-0=5
        print(" ", end="")
    for star in range(0,i+1):                  # 0, 0+1, 1+1,
        print("* ", end="")

    print()

#Reverse Pyramid

rows = int(input("Enter the rows : "))
for i in range(rows):
    for s in range(i+1):
        print(" ", end="")
    for j in range(rows-i):
        print(" *", end="")

    print()