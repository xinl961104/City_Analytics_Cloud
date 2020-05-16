#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import TwitterCredentials
import couchdb
import json


class TwitterStreamer():
    """
    Streaming and processing live tweets
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_file_name, location_list):

            listener = StdOutListener(fetched_tweets_file_name)

            auth = OAuthHandler(TwitterCredentials.CONSUMER_KEY,
                                TwitterCredentials.CONSUMER_SECRET)

            auth.set_access_token(TwitterCredentials.ACCESS_TOKEN,
                                  TwitterCredentials.ACCESS_TOKEN_SECRET)

            stream = Stream(auth, listener)
            #stream.filter(track=track_list)
            stream.filter(locations =location_list)


class StdOutListener(StreamListener):

    """
    Print the received tweets to StdOut and save/upload
    """

    def __init__(self, fetched_tweets_file_name):
        COUCHDB_SERVER = 'http://admin:password@115.146.92.188:5984/'
        # COUCHDB_SERVER = 'http://admin:password@172.26.132.199:5984/'
        couch = couchdb.Server(COUCHDB_SERVER)
        DBNAME = 'stream_test_05_16s'
        self.db = couch.create(DBNAME)
        # self.db = couch[DBNAME]
        self.fetched_tweets_file_name = fetched_tweets_file_name


    def on_data(self, data):

        while True:

            try:
                with open(self.fetched_tweets_file_name, 'a') as tf:

                    tweet = json.loads(data)
                    self.db.save(tweet)

                    tf.write(str(tweet))
                    print(str(tweet) + '\n\n\n\n')

                return True

            except BaseException as e:

                print('Error on_data: %s' % str(e))

            except StopIteration:
                pass
         #Handle the timeout exception!
        return True


    def on_status(self, status):
        try:
            text = status.extended_tweet["full_text"]
        except AttributeError:
            text = status.text


    def on_error(self, status):
        print(status)
        if status == 420:
            # returning False in on_error disconnects the stream
            return True


if __name__ == '__main__':
    fetched_tweets_file_name = 'stream.txt'
    location = [113.0822098723,-43.5934083376, 153.7755692473,-11.1098013981]

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_file_name, location)
