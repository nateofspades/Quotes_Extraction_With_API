import requests
import pandas as pd

# Load the API key from the .env file
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("api_key")

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

author_list = ['Albert-Einstein', 'Abraham-Lincoln', 'Alan-Watts']

# Create the quotes dataframe consisting of all the authors in author_list.
quotes_df = pd.DataFrame({'author': [], 'image': [], 'quote': []})
for author in author_list:
    quotes_df = pd.concat([quotes_df, quotes_extraction_function(author)])

print(quotes_df)


### NEXT STEPS
# Start by making video with Einstein quotes:
#   i) find text-to-speech software which allows music in the background
#  ii) choose a voice + background music
# iii) make the video; don't worry about the visual aspect of the video for now
#  iv) create a mock YouTube channel. Don't worry about name / logo / branding; I will delete the channel afterwards
#   v) load the video to YouTube channel
# Possible: Make a single dataset of all of the appropriate authors (e.g. excluding living authors)
#    The reason this might make sense is because many authors have only a few quotes and therefore not enough for their
#    own videos. We might therefore need to group them.
#    (If I do this then I need to use time module to make sure we are not making too many requests per 30 seconds)