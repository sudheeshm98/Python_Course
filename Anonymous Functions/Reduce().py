"""
Reduce()
--------
The reduce() function applies a provided function to ‘iterables’
and returns a single value, as the name implies.
"""
from functools import reduce

num = [1,2,3,4,5]
res = reduce(lambda x,y:x+y, num)
print(res)
