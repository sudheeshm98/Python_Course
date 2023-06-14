"""
Define a class , which have a class parameter and have a same instance parameter
"""


class Person:
    name = 'Person'                    #class parameter

    def __init__(self,name):           #instance parameter
        self.name = name

obj = Person('Sachin')
print("%s Name is %s "%(Person.name,obj.name))

obj2 = Person('Tendulkar')
print("%s Name is %s "%(Person.name,obj2.name))