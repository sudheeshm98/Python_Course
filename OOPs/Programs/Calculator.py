class Calculator:

    def Addition(self):
        print("Sum = ",a+b)

    def Substraction(self):
        print(a-b)

    def Multiplication(self):
        print(a*b)

    def Division(self):
        print(a/b)

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))

obj = Calculator()

choice = 1
while choice != 0:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        print(obj.Addition())
    elif choice == 2:
        print(obj.Substraction())
    elif choice == 3:
        print(obj.Multiplication())
    elif choice == 4:
        print(obj.Division())
    else:
        print("Invalid Choice!!!")
    break



