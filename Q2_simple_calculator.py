# Q2 Create a program that: 
#1. Asks user for two numbers 
#2. Performs and displays: Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation

a = int(input("Enter first number: "))  #taken first number input
b = int(input("Enter second number: ")) #second number taken as a input

#perform Arithmetic operations
Addition = a+b
Subtraction = a-b
Multiplication = a*b
Division = a/b
Modulus = a%b
Exponentiation = a**b

#print all the results of performed operations 
print("\nResults:")
print(f"{a} + {b} = {Addition}")
print(f"{a} - {b} = {Subtraction}")
print(f"{a} * {b} = {Multiplication}")
print(f"{a} / {b} = {Division}")
print(f"{a} % {b} = {Modulus}")
print(f"{a} ^ {b} = {Exponentiation}")
