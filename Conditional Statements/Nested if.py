#Greatest amoung 3 Numbers
A = int(input("Enter 1St Number : "))
B = int(input("Enter 2nd Number : "))
C = int(input("Enter 3rd Number : "))

if A >= B:
  if A >= C:
    print(A)
elif B >= A:
  if B >= C:
    print(B)
else:
  print(C)