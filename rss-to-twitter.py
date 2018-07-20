import feedparser
import datetime
import twitter
#You should have python-twitter installed to run this scripts. Run "pip install python-twitter" in your concole.
#Docs here: https://python-twitter.readthedocs.io/en/latest

api = twitter.Api(consumer_key='Your consumer key',
                 consumer_secret='Your consumer secret', access_token_key='Your access token key',
                 access_token_secret='Your access token secret')

today_date = str(datetime.datetime.today().strftime("%a, %d %b %Y"))#you can use another time format if this doesn't suit you
feed = feedparser.parse('Your rss feed URL')
i = 0
text = ['Phrase 1: ', 'Phrase 2: ', 'Phrase 3: '] #There can be many entries a day, in that case use different Tweet statuses for different links
for entry in feed.entries[:4]:#iterate through first n entries, in this case — 4; you can change this number or remove it completely
    published_date = entry.published
    my_status = text[i]
    if published_date.find(today_date) != -1:
        article_link = entry.link
        new_status = api.PostUpdate(my_status + article_link)
        i = i+1
        print('Task completed\n') #For you to know that everything works just fine
