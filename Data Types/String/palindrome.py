"""
To check if a string is palindrome or not
"""
str1 = input("Enter the string : ")
if str1 == str1[::-1]:
    print(str1, "is Palindrome")
else:
    print(str1, "is not Palindrome")