import requests
import pandas as pd

# Load the api_key from the .env file
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("api_key")

author = "Albert-Einstein"

# Extract the quotes.
response = requests.get(f"https://zenquotes.io/api/quotes/author/{author}/{api_key}")
if response.status_code == 200:
    quotes = response.json()
    author_list = []    # All values in author_list will be the same
    image_list = []     # All values in image_list will be the same
    quote_list = []     # These values will not be the same
    image = ''
    for quote in quotes:
        author_list.append(quote['a'])    # Retrieves the author
        image_list.append(quote['i'])     # Retrieves the image of the author
        quote_list.append(quote['q'])     # Retrieves the quote
else:
    print(f"Request failed with status code {response.status_code}")

# Store the quotes in a dataframe.
df = pd.DataFrame({'author': author_list, 'image': image_list, 'quote': quote_list})
df = df.drop_duplicates()

# Store the quotes in an Excel sheet.
df.to_csv(f"{author}-Quotes.csv", index=False)