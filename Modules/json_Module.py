"""
json Module
-----------
JSON is a syntax for storing and exchanging data
Python has a built-in package called json, which can be used to work with JSON data

"""
import json

print(dir(json))

#parsing

#dumps   python - json
x = {"name":"sudhi","age":25,"place":"vpz"}
print(type(x))
y = json.dumps(x)
print(y)
print(type(y))

#loads   json - python
X = '{"name":"sudhi","age":25,"place":"vpz"}'
Y = json.loads(X)
print(Y)
print(type(Y))
