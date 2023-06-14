#6.delete a list of keys from a dict

#7.check if a value exist in a dict
dict1 = {"name":"sudhi","age":25,"place":"kochi","course":"python"}
x = dict1.values()
print(x)
if "sudhi" in dict1.values():
    print("sudhi exist in the dict")

#8.rename key of a dict
dict2 = {"name":"sudhi","age":25,"place":"kochi","course":"python"}
dict2['from']=dict2.pop('place')
print(dict2)

#9.get the key of min value from the dicts
dict3 = {"name":"sudhi","age":25,"place":"kochi","course":"python"}
a = dict3.values()
b = []
for i in a:
    a = str(i)
    b.append(a)
print(min(b))

#10.change the value of a key in the nested dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
sampleDict["class"]["student"]["marks"]["physics"] = 80
print(sampleDict)