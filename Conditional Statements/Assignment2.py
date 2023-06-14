#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years
# Ask user for their salary and year of service and print the net bonus amount

Salary = int(input("Enter your Current Salary : "))
Service = int(input("Enter your Year of Service : "))

if Service > 5:
    Bonus = Salary*(5/100)
    print("Your Bonus Amount is : ", Bonus)

else:
    print("You are not Eligible for the Bonus")



