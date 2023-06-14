num = int(input("Enter a Number : "))
rev = 0
while num > 0:
    dig = num % 10          #dig = 3 , 2 , 1
    rev = rev*10 + dig      #0*10 + 3 = 3
    num = num//10           #num = 123 , 12 , 1 , 0
print("Reverse of the given Number is : ",rev)
