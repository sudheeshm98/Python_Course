"""
Map()
-----
This function accepts another function and a sequence of ‘iterables’
as parameters and provides output after applying the function to each
iterable in the sequence.

"""
#Example 1
def add(n):
    return n+n

num = [1,2,3,4,5]
res = map(add,num)
print(list(res))

#Example 2
num1 = [1, 2, 3, 4]
num2 = [4, 5, 6, 7]
ress = map(lambda x, y: x + y, num1, num2)
print(list(ress))
