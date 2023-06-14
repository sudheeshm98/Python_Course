#Number Pyramid

rows = int(input("Enter the rows : "))
for i in range(1,rows+1):
    for s in range(0,rows-i):
        print(" ", end="")
    for n in range(1,i+1):
        print(n, end=" ")

    print()
