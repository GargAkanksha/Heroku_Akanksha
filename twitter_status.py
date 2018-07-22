import tweepy
from config import consumer_key,consumer_secret,access_token, access_token_secret   
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

quotes_list = ["This is tweet 1","This is tweet 2", "This is tweet 3"]

def tweet_func(tweet_number):
    api.update_status(quotes_list[tweet_number])
    print(f' Tweet #{tweet_number} tweeted successfully')

counter = 0

while(True):
    tweet_func(counter)
    time.sleep(10)
    counter+=1
    if counter>2:
        break
