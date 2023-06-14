"""
Polymorphism
------------
it is the ability of an object to take many forms
"""
#Polymorphism with Inheritance
class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details',self.name,self.color,self.price)
    def max_speed(self):
        print('Max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gears')

class Car(Vehicle):
    def max_speed(self):
        print('Max speed is 250')
    def change_gear(self):
        print('Vehicle change 7 gears')

car = Car('Ford','Gray',250000)
car.show()

vehicle = Vehicle('BMW','Black',500000)
vehicle.show()



