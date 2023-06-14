#Normal Method
list_items = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in list_items:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#List Comprehension method
list_items2 = [11,12,13,14,15,16,17,18,19,20,21]
obj = [(i,'even' if i%2==0 else 'odd') for i in list_items2]
print(obj)

#prime Numbers
prime_num = [x for x in list_items2 if all(x%y != 0 for y in range(2,x))]
print(prime_num)

#Divisible by 3
div_by_3 = [x for x in list_items2 if x%3 == 0]
print(div_by_3)
