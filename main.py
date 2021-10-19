import os 
import yagmail 
from dotenv import load_dotenv
from news import NewsFeed
import datetime
from time import sleep


while True:

    if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 00:
        print('Executing!')    


        load_dotenv('credentials.env')


        def get_sender_credentials():
            email = os.environ.get('EMAIL')
            psw = os.environ.get('PSW')
            return email, psw

        def get_receivers():
            receivers = os.environ.get('RECEIVERS')
            receivers = receivers.split(', ')
            return receivers

        def get_interests():
            interests = os.environ.get('INTERESTS')
            interests = interests.split(', ')
            return interests

        def send_news_feed():
            email, psw = get_sender_credentials()    
            email = yagmail.SMTP(user=email, password=psw)
            receivers = get_receivers()
            interests = get_interests()
            for (receiver, interest) in zip(receivers, interests):
                today = datetime.datetime.now().strftime('%Y-%m-%d')
                yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                news_feed = NewsFeed(interest=interest, 
                                    from_date=yesterday, 
                                    to_date=today, 
                                    language='en') 
                email.send(to=receiver, 
                            subject=f'NEWS ABOUT {interest}', 
                            contents=f'Hi, this is me news bot!\n I have recent news about {interest} for you!\n{news_feed.get()}\n\n Sincerely, \n News Bot')

                #print(f'NEWS ABOUT {interests[0]}')
                #print(f'Hi, this is me news bot!\n I have recent news about {interests[0]} for you!\n{news_feed.get()}\n News Bot')
        
        send_news_feed()

    sleep(60)