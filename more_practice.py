eng2sp = {"hello": "hola", "goodbye": "adiós", "thank you": "gracias"}
print(eng2sp["thank you"])
celsius_to_fahrenheit = lambda c : (c * 9/5) + 32
print(celsius_to_fahrenheit(35))

calculate_tax = lambda price : price * 1.15
is_expensive = lambda price : True if price > 100 else False
print(calculate_tax(55))
print(is_expensive(120))

try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")

except:
    print("Error: Please enter a valid number for age.")
# recursive functions
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(6))

def count_down(n):
    if n == 0:
        print("Blastoff") # base case

    else:
        print(n)
        count_down(n-1)

count_down(5)
    
def factorial(n):
    # 1. Base Case: If n is 1, we finally have an answer!
    if n == 1:
        return 1
    
    # 2. Recursive Case: n * (n - 1)
    else:
        # The function PAUSES here until factorial(n-1) returns a value
        return n * factorial(n - 1)

print(factorial(4)) 

def safe_divide(a, b):
    try:
        ans = a / b
        return ans
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Calling the function
print(safe_divide(10, 2)) 
print(safe_divide(10, 0)) 