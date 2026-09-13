# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


# Requesting the bookstoscrape website for book titles and their prices

def scrape_books():
    url = 'https://books.toscrape.com/' # website we intend on scraping
    try:
         response = requests.get(url)
    except requests.RequestException:
         print("Error fetching website") # handle any connection or request-related error
         return None

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser") # parse the received html response for book information and price

        # finding HTML elements containing book prices and titles
        elements = soup.find_all('h3')
        prices = soup.find_all(class_='price_color')
        # Creating an empty list that will contain all book data
        items = [] 
        # Using a for loop to loop through the first ten elements keeping track of their position
        for index,element in enumerate(elements[:10]):
            title = element.find('a')['title'] # Grabs the full book title 
            price = prices[index].text
            cleaned_price = float(price.replace('Â', '').replace('£', '')) # Cleaning price by removing symbols and converting price to a float
            items.append({"title":title, "price":cleaned_price})

        return items

    else:
        return "Failed to retrieve website"



from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_KEY = os.getenv("ACCESS_KEY")
# Creating a function fo get the currency exchange rate
def get_exchange_rate():
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={ACCESS_KEY}&symbols=GBP,KES"
    try:
         response = requests.get(url)
    except requests.RequestException:
         print("Error getting exchange rate data")
         return None

    if response.status_code == 200:
        exchange_rate_data = response.json()
        rates = exchange_rate_data["rates"]
        gbp_to_kes =(rates["KES"])/(rates["GBP"])
        return gbp_to_kes
 # Calling both functions and storing returned data   
items = scrape_books()
gbp_to_kes = get_exchange_rate()

# Looping through every dictionary in items list 
for item in items:
            item["price_kes"] = round(item["price"] * gbp_to_kes, 2) # Creates a new dictionary key to store the converted price in kes
            print(item)
# Creating a json file to store all book data including the converted prices
with open("books.json", "w") as file:
     json.dump(items, file, indent=4)

df = pd.DataFrame(items)
df.columns = ["Product", "GBP Price", "KES Price"]
print(df)
