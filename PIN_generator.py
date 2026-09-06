import random

#generate a random PIN of 4 digits
num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
num_3 = random.randint(0, 9)
num_4 = random.randint(0, 9)


#combine the 4 digits to make a PIN
PIN = str(num_1) + str(num_2) + str(num_3) + str(num_4)
print("Your PIN is: " + PIN)