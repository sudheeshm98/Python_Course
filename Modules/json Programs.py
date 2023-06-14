#1.json data - python objects
import json

json_data = '{ "Name":"Sudhi","Age":6,"Course":"Python"}'
python_obj = json.loads(json_data)

print("Name: ", python_obj["Name"])
print("Age: ", python_obj["Age"])
print("Course: ", python_obj["Course"])

#2.python objects - json data
import json

python_obj = {"Name":"Sudhi","Age":6,"Course":"Python"}
json_data = json.dumps(python_obj)
print(json_data)

#3.python objects - json strings
import json
dict1 = {"Name":"Sudhi","Age":6,"Course":"Python"}
list1 = ["Sudhi",25,"Python"]
json_dict = json.dumps(list1)
print(json_dict)
print(type(json_dict))

#4.To convert python dict object(sort by key) to json data. Print the object members with indent level 4
import json

dict2 = {"Name":"Sudhi","Age":6,"Course":"Python"}
print(json.dumps(dict2, sort_keys=True, indent=4))

#5.json encoded data - python objects
import json

json_data = '{"Name":"Sudhi","Age":6,"Course":"Python"}'
python_dict = json.loads(json_data)
print(python_dict)

