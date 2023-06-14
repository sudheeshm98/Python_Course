class bank:
    def __init__(self,name,transaction):
        self.name = name                             #public
        self._trans = transaction                    #_protected

bank = bank('SBI',12345678)
print(bank._trans)


