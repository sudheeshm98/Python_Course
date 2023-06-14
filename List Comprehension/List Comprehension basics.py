"""
List Comprehension
------------------
it offers a shorter syntax when you want to create a new list based on the
values of an existing list.

syntax
newlist = [expression for item in iterable if condition == True]
"""

IPL = ['MI','CSK','RR','SRH','GT','LSG','DD','KKR']
newlist = [x for x in IPL if 'S' in x]
print(newlist)
