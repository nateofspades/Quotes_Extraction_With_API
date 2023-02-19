import requests
import pandas as pd
import time

# Load the API key from the .env file
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("api_key")

# Acquire the list of all authors on ZenQuotes.
response = requests.get(f"https://zenquotes.io/api/authors/{api_key}")
author_dicts = response.json()
author_list = []
for dict in author_dicts:
    author_list.append(dict['a'].replace(' ', '-')) # Spaces between names need to be replaced with hyphens for the API for quote extraction to work

# Create the function which extracts all quotes from an input author.
def quotes_extraction_function(author):
    """
    :param author: One of the authors from ZenQuotes.io https://zenquotes.io/authors. Author names are separated by hyphens.
    :return: A dataframe where each row corresponds to 1 quote of the author. Each row also has the author name and image.
    """
    author_list = []  # All values in author_list will be the same
    image_list = []  # All values in image_list will be the same
    quote_list = []  # These values will not be the same
    response = requests.get(f"https://zenquotes.io/api/quotes/author/{author}/{api_key}")
    if response.status_code == 200:
        quotes = response.json()
        for quote in quotes:
            author_list.append(quote['a'])  # Retrieves the author
            image_list.append(quote['i'])   # Retrieves the image of the author
            quote_list.append(quote['q'])   # Retrieves the quote

    # Create the dataframe.
    df = pd.DataFrame({'author': author_list, 'image': image_list, 'quote': quote_list})
    df = df.drop_duplicates()

    return df

# Create the quotes dataframe consisting of all the authors in author_list (except for the ones which cause issues with the above function).
quotes_df = pd.DataFrame({'author': [], 'image': [], 'quote': []})
for author in author_list:
    try:
        quotes_df = pd.concat([quotes_df, quotes_extraction_function(author)])
    except:
        continue
    time.sleep(6.1) # Wait 6.1 seconds before the next iteration; ZenQuotes only allows 5 API calls per 30 seconds.

# Create the Excel file from the quotes dataframe.
quotes_df.to_csv('Quotes.csv', index=False)


