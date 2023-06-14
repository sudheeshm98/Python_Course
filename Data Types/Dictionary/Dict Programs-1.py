#1.Convert 2 lists into Dict
keys = ["one","two","three"]
values = [1,2,3]

dictt = dict(zip(keys,values))
print(dictt)

#2.Merge 2 dicts
dict1 = {"name":"sudhi","age":"25"}
dict2 = {"place":"vpz","cource":"python"}
dict1.update(dict2)
print(dict1)

#3.print the value of key 'history' from the below dict
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
print(sampleDict["class"]["student"]["marks"]["history"])

#4.initialize dict with default values
keys = ["dict3","dict4"]
defaults = {"name":"sudhi","age":"25"}

result = dict.fromkeys(keys,defaults)
print(result)

#5.create a dict by extracting the keys from a given dict
dict3 = {"name":"sudhi","age":25,"place":"kochi","course":"python"}
print(dict1.keys())