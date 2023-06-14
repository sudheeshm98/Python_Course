#Q.A function that accepts different values as parameters and returns a list

def food_items(*food):
    return list(food)
print(food_items("alfarm","shawai","chilli"))


#Q.A function that accepts dict as parameters

def my_function(**kid):
    return dict(kid)
print(my_function(fname = "Tobias", lname = "Refsnes"))