"""
4.Hierarchical Inheritance :-
more than one child class is derived from a single parents class
"""


class vehicle:
    def info(self):
        print('This is vehicle')


class car(vehicle):
    def car_info(self, name):
        print(f'Car name is : {name}')


class bike(vehicle):
    def bike_info(self, name):
        print(f'Bike name is : {name}')


obj1 = car()
obj1.car_info('BMW')
obj1.info()

obj2 = bike()
obj2.bike_info('Mateor 350')
obj2.info()
