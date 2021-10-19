import requests

# Sample of how to get all the articles from url api

# "qInTitle" it can be also just "q"

url = 'https://newsapi.org/v2/everything?' \
       'qInTitle=polkadot&'\
       'from=2021-10-01&'\
       'sortBy=publishedAt&'\
       'language=en&'\
       'apiKey=d962211689dd462081a53787d32d44fa'

response = requests.get(url)
content = response.json()
articles = content['articles']
x =content['articles'][3]['url']
print(content)
print('-' * 10)
print(x)

y = 0
for article in articles:
    y = int(y)
    y = y + 1
    print(str(y) + '\n' + article['title'] + '\n' + article['url'] + '\n')