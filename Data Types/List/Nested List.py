list1 = ["cat","dog","pig","fox",["lion","tiger","deer"],"rat"]

print(list1[4])
print(list1[4][1])                    #list[4] = ["lion","tiger","deer"]

list1.insert(5,"rabbit")
print(list1)
x = list1[4].insert(2,"monkey")       #insert an item inside list
print(list1)

list1[4].remove("lion")               #remove an item inside list
print(list1)

list1[4].pop(1)                       #pop an item inside list
print(list1)

list1[4].reverse()                    #reverse the inside list
print(list1)

#Adding a sublist to a main list
list2 = ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
list3 = ["h","i","j"]
# list2[2][1][2].extend(list3)
# print(list2)
list2[2][1].insert(3,list3)
print(list2)

