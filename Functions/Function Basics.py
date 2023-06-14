"""
Functions
---------
* A function is a block of code which only runs when it is called.
* You can pass data, known as parameters, into a function.
* A function can return data as a result.
* A function is defined using the def keyword.

1.Builtin
2.User Defined
3.Lambda
"""
def test_fun():
    print("hi dears")
test_fun()


def sum():
    a = 5
    b = 10
    c = a+b
    print(c)
sum()


def sum(x,y):
    z = x+y
    return z
print(sum(10,20))


#Arbitory Arguments  --  If the number of arguments is unknown, add a * before the parameter name
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("jack","Emil", "Tobias", "Linus")


#keyword Argument  --  arguments with the key = value syntax
def my_function1(child3, child2, child1):
  print("The youngest child is " + child3)
my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitory Keyword Arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")


#Default value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function()
my_function("Sweden")
my_function("India")


#Passing a list as argument
def food_items(food):
    for x in food:
        print(x)
food = ["Alfarm","Shawai","Shawarma"]
food_items(food)
