import os
import requests
from dotenv import load_dotenv


class NewsFeed:

    """ 
    Representing multiple news titles and links as a single string.
    Example:
    Hi John,
    Here are the news in which you are interested.
    1.) Bitcoin raises above $65000! <link>
    ... 
    """

    load_dotenv('credentials.env')
    api_key = os.environ.get('API_KEY')
    base_url = 'https://newsapi.org/v2/everything?'
    

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language


    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)
        y = 0
        email_body = ''
        for article in articles:
            y = int(y)
            y = y + 1
            email_body = email_body + str(y) + '\n' + article['title'] + '\n' + article['url'] + '\n' + '\n'
        return email_body


    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles


    def _build_url(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&'\
              f'from={self.from_date}&'\
              f'to={self.to_date}&'\
              f'language={self.language}&'\
              f'apiKey={self.api_key}'             
        return url


if __name__ == "__main__":
    new_feed = NewsFeed(interest='stock', from_date='2021-10-18', to_date='2021-10-18', language='en')
    print(new_feed.get())