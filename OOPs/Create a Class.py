"""
Create a class with instance attributes
"""
class player:
    def __init__(self,name,country,rank):
        self.name = name
        self.country = country
        self.rank = rank


player1 = player("Rohit","india",1)
player2 = player("Babar","Pakistan",2)

print(f"{player1.name} from {player1.country} Ranked {player1.rank}")
print(f"{player2.name} from {player2.country} Ranked {player2.rank}")

