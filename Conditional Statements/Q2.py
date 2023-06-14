#Greatest amoung 3 Numbers
A = int(input("Enter 1St Number : "))
B = int(input("Enter 2nd Number : "))
C = int(input("Enter 3rd Number : "))

if A > B and A > C:
  print(A, "is greater")
elif B > A and B > C:
  print(B, "is greater")
elif C > A and C > B:
  print(C, "is greater")
elif A == B and A > C:
  print(A,B, "are greater")
elif B == C and B > A:
  print(B,C, "are greater")
elif C == A and A > B:
  print(C,A, "are greater")
else:
  print("All are Equal")




