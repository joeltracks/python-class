import math
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
operation = int(input("Enter operation (1/2/3/4/5): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if(operation == 1):
    print(num1 + num2)
elif(operation == 2):
    print(num1 - num2)
elif(operation == 3):
    print(num1 * num2)
elif(operation == 4):
    print(num1 / num2)
elif(operation == 5):
    print("Square root of", num1, "is", math.sqrt(num1))

else:
    print("Invalid input")