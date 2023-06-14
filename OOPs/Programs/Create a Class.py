class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        print("Vehicle Make is",self.make)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year


class Car(Vehicle):
    def __init__(self, make, model, year, color, mileage):
        super().__init__(make, model, year)
        self.color = color
        self.mileage = mileage

    def get_color(self):
        return self.color

    def get_mileage(self):
        return self.mileage

my_car = Car("Honda", "Civic", 2021, "Red", 10000)


my_car.get_make()
print(my_car.get_model())
print(my_car.get_year())
print(my_car.get_color())
print(my_car.get_mileage())
