#union()
set1 = {"a","b","c"}
set2 = {1,2,3,"a"}
set3 = set1.union(set2)
print(set3)

#intersection()
x = set1.intersection(set2)
print(x)

#difference()
y = set1.difference(set2)
print(y)

#symmetric_difference()
z = set1.symmetric_difference(set2)
print(z)

set3 = {"a","b","c"}
set4 = {1,2,3,"a"}

#update()
set3.update(set4)
print(set3)

#intersection_update()
set3.intersection_update(set4)
print(set3)

#difference_update()
set3.difference_update(set4)
print(set3)

#symmetric_difference_update()
set3.symmetric_difference_update(set4)
print(set3)

set5 = {"a","b","c"}
set6 = {1,2,3,"a","b","c"}

#isdisjoint()
a = set5.isdisjoint(set6)
print(a)

#issubset()
b = set5.issubset(set6)
print(b)

#issuperset()
c = set5.issuperset(set6)
print(c)
