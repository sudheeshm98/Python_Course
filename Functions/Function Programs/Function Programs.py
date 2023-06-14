#Sum of n natural numbers
def sum_natural(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
n = int(input("Enter the Range : "))
print(sum_natural(n))


#to find max of 3 numbers 3 6 5
def maxx(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f'{n1} is max')
    elif n2>n1 and n2>n3:
        print(f'{n2} is max')
    else:
        print(f'{n3} is max')
maxx(3,6,5)

"""OR"""

def num_max(n):
    print(max(n))
list1 = [3,6,5]
num_max(list1)


