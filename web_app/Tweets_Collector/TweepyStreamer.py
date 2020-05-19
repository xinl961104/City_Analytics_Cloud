#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import TwitterCredentials
import couchdb
import json


class TwitterStreamer():
    """
    Streaming and processing live tweets
    """
    def __init__(self):
        pass

    def stream_tweets(self, location_list):
        listener = StdOutListener()
        auth = OAuthHandler(TwitterCredentials.CONSUMER_KEY,\
                                TwitterCredentials.CONSUMER_SECRET)

        auth.set_access_token(TwitterCredentials.ACCESS_TOKEN,
                                  TwitterCredentials.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        stream.filter(locations =location_list, stall_warnings=True)


class StdOutListener(StreamListener):

    """
    Print the received tweets to StdOut and save/upload
    """

    def __init__(self):
        # COUCHDB_SERVER = 'http://admin:password@115.146.92.188:5984/'
        COUCHDB_SERVER = 'http://admin:password@172.26.132.199:5984/' #Group DB
        couch = couchdb.Server(COUCHDB_SERVER)
        DBNAME = 'historical_data'
        try:
            self.db = couch.create(DBNAME)
        except:
            self.db = couch[DBNAME]

    def on_data(self, data):

        while True:

            try:
                tweet = json.loads(data)
                tweet['_id'] = tweet['id_str']
                try:
                    self.db.save(tweet)
                except:
                    pass;
                    
                print(str(tweet) + '\n\n\n\n')

                return True
            
                except tweepy.TweepError:
                    print('Tweepy error. The system is gonna sleep for 1 min. ')
                    time.sleep(60)

            except BaseException as e:

                print('Error on_data: %s' % str(e))

            except StopIteration:
                pass
            
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
    
    location = [113.0822098723,-43.5934083376, 153.7755692473,-11.1098013981]

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(location)
