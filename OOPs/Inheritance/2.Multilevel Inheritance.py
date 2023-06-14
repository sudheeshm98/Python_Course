"""
2.Multilevel Inheritance
"""
class Grandfather:
    def ownhouse(self):
        print('Grandpa house')

class Father(Grandfather):
    def ownbike(self):
        print('Fathers bike')

class Son(Father):
    def ownbook(self):
        print('Son have a book')

A = Grandfather()
B = Son()

B.ownhouse()
B.ownbike()
B.ownbook()
