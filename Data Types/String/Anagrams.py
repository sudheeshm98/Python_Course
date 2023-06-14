"""
To find if two strings are Anagrams or not.
"""
str1 = input("Enter the first string : ")
str2 = input("Enter the second string :")
str3 = str1.lower()
str4 = str2.lower()
if sorted(str3) == sorted(str4):
    print(str1, "and", str2, "are Anagrams")
else:
    print(str1, "and", str2, "are not Anagrams")