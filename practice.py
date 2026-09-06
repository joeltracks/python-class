
def add_two_numbers(num1, num2):
    print (num1 + num2)

result = add_two_numbers(5, 10)
print(result)

add = lambda x, y: x + y
print(add(1, 10))
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet('hamster', 'Harry')

import math
radius = 21
area = math.pi * (radius ** 2)
print(area)

import random

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#pick what fruit to consume

tunda = random.choice(fruits)
print(tunda)

def greet():
    print("Hello Friday!")

greet()

def calculate_gross_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

hours = input("Enter number of hours worked: ")
hours_worked = int(hours)

rate = input("Enter hourly rate: ")
hourly_rate = float(rate)

pay = calculate_gross_pay(hours_worked, hourly_rate)
print("Gross pay:", pay)

# The Definition
def display_menu():
    print("--- Game Menu ---")
    print("1. Start Game")
    print("2. Load Save")
    print("3. Exit")

display_menu()

def add_two_numbers(num1, num2):
    print(num1 + num2)

add_two_numbers(5, 10)