"""
LIST
-----
Mutable , indexed , ordered & allow duplicants

List = ["apple",123,"orange",5.6]
"""
items = ["apple",123,"red",7.5,"john"]
items1 = ["snow",50,"don"]
print(items[2])                              #indexing
print(items[-2])
print(items[1:4])                            #slicing
print(items[::-1])

items.append("grapes")                       #append
print(items)

items.extend(items1)                         #extend
print(items)

items.remove("red")                          #remove
print(items)

items.insert(1,"banana")                     #insert  --- Here 1 is index value
print(items)

items.pop(3)                                 #pop  --- to remove items
print(items)

items.reverse()                              #reverse
print(items)

# items.sort()
