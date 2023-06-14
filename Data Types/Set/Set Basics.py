"""
Set
---
1.immutable
2.unordered
3.unindexed
4.no duplicates
"""
set1 = {1,2,3,5,"cat"}
print(5 in set1)

for i in set1:
    print(i)

#add()
set1.add("dog")
print(set1)

#update()      ---   any datatype can update to a set
list1 = ["crow","parrot","peacock"]
set1.update(list1)
print(set1)

#remove()
set1.remove("crow")
print(set1)

#discard()  ---          #remove() method will raise an error if the specified item does not exist
                         #and the discard() method will not
set1.discard("python")
print(set1)

#pop()   ---  The pop() method removes a random item from the set
x = set1.pop()
print(set1)

#clear()
set1.clear()
print(set1)

#delete
del set1
