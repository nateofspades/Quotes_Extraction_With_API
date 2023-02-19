import requests
import time

# Generates a list of 20 random quotes, along with the author of each quote.
quote_list = []
for i in range(1, 21):
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    quote_list.append(f'{quote} - {author}')
    if i%5 == 0:
        time.sleep(35)

# Eliminate any duplicate quotes that might have occurred.
quote_list = list(set(quote_list))