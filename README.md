# Quotes_Extraction_With_API

I wanted a list of quotes that could be used to create a YouTube channel. This project uses the API from [ZenQuotes.io](https://zenquotes.io/) to extract quotes from various authors into a .csv file. In [Extraction-of-All-Quotes.py](https://github.com/nateofspades/Quotes_Extraction_With_API/blob/master/Extraction-of-All-Quotes.py) the quotes across all authors are extracted into a Pandas dataframe. Each row in the dataframe corresponds to 1 quote, and also contains the name and an image of the quote's author. This dataframe is then stored in ['Quotes.csv'](   ).

The file [Random-Quotes.py](  ) also shows how to use the API to generate random quotes using the API. This can be used, for example, to generate a quote of the day.

