"""
p
p y
p y t
p y t h
p y t h o
p y t h o n
"""

word = input("Enter a String : ")
char = len(word)
for i in range(1,char+1):
    for j in range(i):
        print(word[j],end=" ")   #word[j] p=0,y=1,t=2......
    print()