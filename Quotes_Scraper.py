from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def quotes_from_1_page(page_link):
    """
    :param page_link (string): A link to a page of quotes of an author on azquotes.com
    :return: A dataframe with 2 columns: all quotes from a given page and the heart count for each quote
    """

    html = urlopen(f"{page_link}")
    res = BeautifulSoup(html.read(), "html5lib")

    # Find all the <a> tags that have the class "title". These correspond to quotes.
    quotes = res.find_all("a", {"class": "title"})
    # Store the quotes in a list.
    quotes_list = []
    for quote in quotes:
        quotes_list.append(quote.get_text())

    # Find all the <a> tags that have the class "heart24 heart24-off". These correspond to the heart counts (i.e. number of likes) for each quote.
    hearts = res.find_all("a", {"class": "heart24 heart24-off"})
    # Store the heart counts in a list.
    heart_count_list = []
    for tag in hearts:
        heart_count = int(tag.string)
        heart_count_list.append(heart_count)

    # Store the quotes and their heart counts in a dataframe
    df = pd.DataFrame({'heart_count': heart_count_list, 'quote': quotes_list})

    return df

# print(quotes_from_1_page("https://www.azquotes.com/author/4399-Albert_Einstein"))
# print(quotes_from_1_page("https://www.azquotes.com/author/4399-Albert_Einstein?p=200000000"))

def quotes_first_30_pages(first_page_link):
    """
    :param first_page_link (string): The link to the first page of quotes of an author on azquotes.com
    :return: A dataframe with 2 columns: all quotes from the first 30 pages of the author and the heart count for each quote
    """

    # Extract the quotes and heart count from the author's first page
    df = quotes_from_1_page(first_page_link)

    # Extract the quotes and heart counts from the next 29 pages.
    # If there are less than 29 additional pages, then the last page will be retrieved multiple times until 29 iterations are complete.
    for i in range(2,31):
        page_link = first_page_link + f"?p={i}"
        df = pd.concat([df, quotes_from_1_page(page_link)])

    # Eliminate any possible duplicate quotes that may have occurred due to possibly retrieving the last page more than once.
    df = df.drop_duplicates()

    return df

# Create Excel sheet for first 30 pages of author's quotes
df = quotes_first_30_pages("https://www.azquotes.com/author/13382-William_Shakespeare")
df.to_csv("William_Shakespeare_Quotes.csv", index=False)
