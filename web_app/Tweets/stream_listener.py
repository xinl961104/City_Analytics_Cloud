import json

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from importlib._bootstrap_external import SourceFileLoader


dictPath = 'twitter_credentials.py'
secret = SourceFileLoader("twitter_credentials", dictPath).load_module()

CONSUMER_KEY = secret.secretTwitter.get("CONSUMER_KEY")
CONSUMER_SECRET = secret.secretTwitter.get("CONSUMER_SECRET")
ACCESS_TOKEN = secret.secretTwitter.get("ACCESS_TOKEN")
ACCESS_SECRET = secret.secretTwitter.get("ACCESS_SECRET")


def filterLocation(tweet):
    if tweet['geo'] and tweet["coordinates"]:
        return tweet


class StdOutListener(StreamListener):
    """
    This is a basic listener class that just prints received tweets to stdout.
    """

    def on_data(self, data):
        try:
            with open("result_tweets.json", 'a') as tf:
                print(data)
                #data.decode("utf-8").strip()
                tweet = filterLocation(json.loads(data))
                tf.write(str(tweet))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


hash_tag_list = ["vegan", "vegetarian", "veggie"]
listener = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
stream = Stream(auth, listener)
stream.filter(track=hash_tag_list)
