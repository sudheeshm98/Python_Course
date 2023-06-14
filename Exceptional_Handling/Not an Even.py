try:
    num = int(input("Enter a Number : "))
    assert num % 2 == 0
except:
    print("Not an Even Number")
else:
    x = 1 / num
    print(x)
