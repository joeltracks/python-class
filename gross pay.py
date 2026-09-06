import math
hours = input("Enter number of hours worked: ")

hours_worked = int(hours)

rate = input("Enter hourly rate: ")

hourly_rate = int(rate)
gross_pay = hours_worked * hourly_rate
print(gross_pay)

def calculate_gross_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

pay = calculate_gross_pay(40, 15)
print(pay)