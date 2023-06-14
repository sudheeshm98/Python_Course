#3.To reverse a string using recursion

def reverse(str1):
    if len(str1) == 0:
        return str1
    else:
        return reverse(str1[1:]) + str1[0]
x = str(input("Enter the string : "))
print(reverse(x))
