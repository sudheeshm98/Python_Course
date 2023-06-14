"""
Dictionary
----------
Used to store data values are in key:value pairs

1.mutable
2.indexed
3.ordered
4.no duplicates

"""
dict1 = {"name":"sudhi","age":25,"place":"kochi","course":"python"}
print(dict1)
print(len(dict1))

print(dict1["name"])      #key method
x = dict1.get("name")     #get() method
print(x)

print(dict1.keys())       #Returns a list containing the dictionary's keys
print(dict1.values())     #Returns a list of all the values in the dictionary

print(dict1.copy())       #prints the whole dict

y = dict1.items()
print(y)

dict1.pop("place")        #Removes the element with the specified key
print(dict1)

dict1.popitem()           #Removes the last inserted key-value pair
print(dict1)

dict1.update({"batch":"Feb 2023"})     #to add new key-value pairs
print(dict1)

dict1["age"] = "26"        #update the existing pair
print(dict1)
dict1["sex"] = "male"      #add new pair
print(dict1)


#fromkeys()   ---   returns a dictionary with the specified keys and the specified value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)

#setdefault()
z = dict1.setdefault("model","Bronco")        #to add new key-value pairs
print(dict1)
