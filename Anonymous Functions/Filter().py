"""
Filter()
--------
The filter() function is used to generate an output list
of values that return true when the function is called.
"""


def fun(val):
    letters = ['a', 'e', 'i', 'o', 'u']
    if val in letters:
        return True
    else:
        return False


str1 = ['p', 'y', 't', 'h', 'o', 'n']
filtered = filter(fun, str1)
print(list(filtered))

# for i in filtered:
#     print((s), end=' ')
