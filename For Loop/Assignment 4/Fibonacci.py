#2.Write a Python program to get the Fibonacci series between 0 to 50.

a = 0
b = 1
print(a)
print(b)
for n in range(0,51):
    c = a + b
    if c < 50:
        print(c)
    a = b
    b = c


