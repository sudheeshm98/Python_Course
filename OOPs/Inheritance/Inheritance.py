"""
Inheritance
-----------
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

1.Single Inheritance
2.Multiple Inheritance
3.Multilevel Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance

"""

class university:                                             #parent
    def __init__(self):
        self.name = KTU
        print('You are in university class constructor')

    def test(self):
        print("test function")

class college(university):                                    #child
    def __init__(self):
        self.name = "KTU shool of engineering"
        print('You are in college class constructor')

    def show(self):
        print("college class instance method : ",self.name)

college = college()
college.show()
college.test()
