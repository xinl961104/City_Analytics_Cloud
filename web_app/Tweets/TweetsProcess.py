import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

CONSUMER_KEY = "3Y38E0OHKTlAL9YbqG3mE5iE2"
CONSUMER_SECRET = "hMwzyhvEVAQbebvkY36pWB3FrDZXpFv7bNx9kYJdA7yUnVNSyB"
ACCESS_TOKEN = "1239723135848439808-fj1PDzvwSAmT5kaY9UXLr5LVSvgNNt"
ACCESS_SECRET = "RmX57K1xyXDZQsvBIwodYnNMxd1uCrBrEagpljoUwVgDt"


class StdOutListener(StreamListener):
    """
    This is a basic listener class that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:
            with open("result_tweets.json", 'a') as tf:
                tf.write(data)
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


hash_tag_list = ["vegan", "vegetarian"]
listener = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
stream = Stream(auth, listener)
stream.filter(track=hash_tag_list)
