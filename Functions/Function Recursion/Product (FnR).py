#2.To find product of two numbers using recursion

def prod(x,y):
    if x==0 or y==0:
        return 0
    else:
        return x+prod(x,y-1)

x = int(input("Enter the first Number : "))
y = int(input("Enter the Second Number : "))
print(prod(x,y))

