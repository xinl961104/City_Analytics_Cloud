import tweepy
from importlib._bootstrap_external import SourceFileLoader


dictPath = 'twitter_credentials.py'
secret = SourceFileLoader("twitter_credentials", dictPath).load_module()

CONSUMER_KEY = secret.secretTwitter.get("CONSUMER_KEY")
CONSUMER_SECRET = secret.secretTwitter.get("CONSUMER_SECRET")
ACCESS_TOKEN = secret.secretTwitter.get("ACCESS_TOKEN")
ACCESS_SECRET = secret.secretTwitter.get("ACCESS_SECRET")
# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# geocode="37.781157 -122.3987201mi", until="2015-07-19"
searched_tweets = api.search(q="vegan")
with open("result_tweets_search.json", 'a') as tf:
    print(type(searched_tweets))
    tf.write(str(searched_tweets))
