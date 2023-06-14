"""
Random Module
"""

import random

print(random.randint(1,100))

print(random.randrange(40,50))

list_items = [1,3,5,7,9,11,13,15]

print(random.choice(list_items))

random.shuffle(list_items)
print(list_items)


