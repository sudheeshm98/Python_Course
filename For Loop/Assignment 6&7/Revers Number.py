"""
54321
4321
321
21
1
"""
N = int(input("Enter the Number : "))
for i in range(N):
    for j in range(N-i,0,-1):
        print(j, end=" ")
    print()
