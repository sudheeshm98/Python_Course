#1.To find LCM of two  numbers using recurion

def highest(a, b):
    if b == 0:
        return a
    else:
        return highest(b, a % b)


def lcm(a, b):
    return (a * b) // highest(a, b)


x = int(input("Enter the First Number : "))
y = int(input("Enter the Second Number : "))

print(lcm(x,y))


