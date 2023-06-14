#5.Generate a Python list of all the even numbers between 4 to 30

def even(x,y):
    z = []
    for i in range(x,y):
        if i%2 == 0:
            z.append(i)
    print(z)

even(4,31)

