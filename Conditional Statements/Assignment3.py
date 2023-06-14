X = int(input("Enter Your Marks out of 100 : "))

if X >= 80:
    print("Your Grade is A")
elif 60 <= X < 80:
    print("Your Grade is B")
elif 50 <= X < 60:
    print("Your Grade is C")
elif 45 <= X < 50:
    print("Your Grade is D")
elif 25 <= X < 45:
    print("Your Grade is E")
else:
    print("You are Failed!!!")
