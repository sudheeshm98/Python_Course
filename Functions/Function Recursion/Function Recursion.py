"""
Function Recursion
------------------
a defined function can call inside that function itself

"""

#Factorial
def fact(n):
    if n == 1:
        return 1
    else:
        x = n*fact(n-1)
        return x            #5!=5*4!
print(fact(5))


#SUM OF N NATURAL NUMBERS
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

# print("\n\nRecursion Example Results")
tri_recursion(5)