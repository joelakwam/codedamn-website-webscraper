import requests # <-- Import library for making HTTP requests.
from bs4 import BeautifulSoup # <-- For extracting data from the webpage.
import csv


response = requests.get('https://flipkart.com') # <-- Making request to 'https://codedamn.com' and storing the response.
beautifulsoup = BeautifulSoup(response.content, 'html.parser') # <-- Initializing the BeautifulSoup class.


top_items = [] # <-- Empty list for storing top items from the website.

products = beautifulsoup.select('div.thumbnail') # <-- Selecting the HTML tag that contains all items.

for element in products:
    title = element.select('h4 > a.title')[0].text # <-- Extracting the title of an item.
    review = element.select('div.ratings')[0].text # <-- Extracting the HTML tag that contains the review of an item.

    info = {
        "title": title.strip(),
        "review": review.strip()
    }

    top_items.append(info) # <-- Add item information to the 'top_items' array.


"""
    - Generate a new CSV file with the following titles:
        1. Product Name
        2. Price
        3. Description
        4. Reviews
        5. Product Image
"""

all_products = [] # <-- Empty array for storing all products from the website.

# <-- Iterate over the products array --> #
for product in products:
    product_name = product.select('')[0].text # <-- Extracting product's name.
    price = product.select('')[0].text # <-- Extracting product's price.
    description = product.select('')[0].text # <-- Extracting product's description.
    reviews = product.select('')[0].text # <-- Extracting product's reviews.
    image_url = product.select('')[0].text # <-- Extracting product's image url.

    product_info = {
        "product_name": product_name.strip(),
        "price": price.strip(),
        "description": description.strip(),
        "reviews": reviews.strip(),
        "image_url": image_url.strip()
    }

    """
        - NOTE: the 'strip()' method is used for removing whitespaces that might be present.
    """

    all_products.append(product_info) # <-- Add 'product_info' dictionary to the 'all_products' array.

keys = all_products[0].keys()

with open('products.csv', 'w', newline = '') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)


print(top_items) # <-- Print all top items in the 'top_items' array to the console.
