"""
5.Hybrid Inheritance :-
combination of different inheritance
"""


class Vehicle:
    def info(self):
        print('This is vehicle')


class car(Vehicle):
    def car_info(self, name):
        print(f'Car name is : {name}')


class bike(Vehicle):
    def bike_info(self, name):
        print(f'Bike name is : {name}')


class sportscar(car, Vehicle):
    def sports_car_info(self):
        print('inside the sports car class')


obj1 = car()
obj1.car_info('BMW')
obj1.info()

s_car = sportscar()
s_car.car_info('BMW')
s_car.info()
