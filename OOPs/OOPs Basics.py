"""
OOPs
----
Concepts :
1.Class            4.Encapsulation
2.Object           5.Abstraction
3.Inheritance      6.Polymorphism
"""
# class myclass:
#     x = 10
#
# obj = myclass()
# print(obj.x)


class car:
    name = ''
    model = 2020

car1 = car()
car1.name = 'Swift'
car1.model = 2010

car2 = car()
car2.name = 'polo'
car2.model = 2015

print(f'{car1.name} is {car1.model} model car')
print(f'{car2.name} is {car2.model} model car')


#Using constructor  -- to initialise objects
class car:
    def __init__(self,name,model):          #__init__ is the constructor
        self.name = name                    #self is the reference keyword
        self.model = model

car3 = car('Lamborgini',2020)
print(f'{car3.name} is {car3.model} model car')
