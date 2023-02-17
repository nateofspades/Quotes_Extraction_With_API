import requests
import time
import pprint

quote_list = []
for i in range(1, 21):
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    quote_list.append(f'{quote} - {author}')
    if i%5 == 0:
        time.sleep(35)

quote_list = list(set(quote_list))

print(quote_list)