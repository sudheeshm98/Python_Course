class car:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def __str__(self):
        return f'{self.name}({self.model})'

    def test(self):
        print("Hi Dears!!!")

car1 = car('Lamborgini', 2020)
car1.model = 2023                     #to change the model attribute
#del car1.name                        #to delete an attribute
print(car1)
car1.test()
print(f'{car1.name} is {car1.model} model car')
