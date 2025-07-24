# Simple calculator using if else concept

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

user_input = input("Enter a symbol: (+,-,%,*,/): ")

# Sum of two numbers

if(user_input == "+"):
    total = num1 + num2
    print("sum of two numbers is: ",total)

# Subtraction of two numbers

elif(user_input == "-"):
    subtraction = num1 - num2
    print("sub of two numbers is: ",subtraction)
# Multiplication of two numbers

elif(user_input == "*"):
    multiplication = num1 * num2
    print("multi of two numbers is: ",multiplication)
# Modulus of two numbers    

elif(user_input == "%"):
    modulus = num1 % num2
    print("module of two numbers is: ",modulus)
# Division of two numbers

elif(user_input == "*"):
    division = num1 / num2
    print("div of two numbers is: ",division)
