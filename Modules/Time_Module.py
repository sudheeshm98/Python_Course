"""
Time Module
-----------
This module has many time related functions

"""
import time

print(time.ctime())

for i in range(5):
    time.sleep(1)
    print(i)