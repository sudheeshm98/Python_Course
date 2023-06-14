"""
The circle class models a circle with a radius and color
"""

class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

    def get_radius(self):
        print('Radius : ',self.radius)

    def get_color(self):
        print('Color : ',self.color)

    def get_area(self):
        print('Area : ',3.14 * self.radius**2)

    def get_circumference(self):
        print('Circumference : ',2 * 3.14 * self.radius)


obj = Circle(5,'Red')

obj.get_radius()
obj.get_color()
obj.get_area()
obj.get_circumference()


