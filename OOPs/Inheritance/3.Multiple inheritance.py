"""
3.Multiple Inheritance
"""
#parent class 1
class vehicle:
    def vehicle_info(self):
        print('inside vehicle class')

#parent class 2
class car:
    def car_info(self):
        print('inside car class')

#child class
class sports_car(car,vehicle):
    def sports_car_info(self):
        print('inside sports car class')

obj = sports_car()
obj.sports_car_info()