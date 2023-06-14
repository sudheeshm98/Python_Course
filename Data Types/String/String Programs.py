#1.Create a string made of 1st , middle and last charectors

str1 = "MALAYALAM"
first = str1[0]
l = len(str1)
mid = int(l/2)
last = str1[-1]
concatenate = first+str1[mid]+last
print(concatenate)

#2.To append the new string into the middle of first string

str1 = "hello"
str2 = "world"
l = len(str1)
mid = int(l/2)
print(str1[0:mid] + str2 + str1[mid:])

#3.Arrange string characters such that lowercase letters should come first

str3 = "HeLloWoRLd"
lower = ""
upper = ""
for char in str3:
    if char.islower():
        lower+=char
    else:
        upper+=char
print(lower+upper)

#4.Count allletters,digits and special charectors from a given string

str4 = "py45%$gg&HGGJ4&"
alpha = ""
digits = ""
special = ""
for char in str4:
    if char.isalpha():
        alpha+=char
    elif char.isdigit():
        digits+=char
    else:
        special+=char

print("Alphapets :",len(alpha))
print("Digits :",len(digits))
print("Special Charectors :",len(special))







