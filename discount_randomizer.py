import random

#price and list of discount options
original_price = 1000
discount_options = [0, 5, 10, 15, 20, 25]

#pick a random discount from the options
discount = random.choice(discount_options)

#calculate the final discounted price
final_price = original_price - (original_price * (discount / 100))
print(final_price)

#display message if no discount was chosen
if discount == 0:
    print("Better luck next time.")

#display message if max discount was chosen

elif discount == 25:
    print("Congratulations! You got the maximum discount.")

else:
    print("You got a discount.")
