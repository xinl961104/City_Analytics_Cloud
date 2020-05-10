#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 02:30:39 2020

@author: ds1989
"""
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import couchdb


access_token = "3197784877-xI9f00daEbkgPLXW7RTcJxRnH64mRjslInwbc5A"
access_token_secret = "LF39cQmBwUqOgeTj6IrGqpmsLKipSjxLrUEiflkZ5famV"
consumer_key = "FbrngwngBIXxELqzf7nL43kht"
consumer_secret = "30qgR1cqgILlzEACV4tU2DPatgxdxsx9UkEEHIdDaG8u3QKQy9"


COUCHDB_SERVER = 'http://admin:password@172.26.130.140:5984/'
couch = couchdb.Server(COUCHDB_SERVER)
db = couch.create('stream_test_05_11')


# Initialize Global variable
tweet_count = 0

#location = [143.896746, -37.483931, 146.280313, -38.565583]
location = [144.852311, -37.808891, 151.212274 , -33.850515]
# Input number of tweets to be downloaded
#n_tweets = 10

def filterLocation(tweet):
    if tweet['geo'] and tweet["coordinates"]:
        return tweet

class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        
        
        #if tweet_count < n_tweets:
            #print(data)
        try:
            with open("result_tweets.json", 'a') as tf:
                
                tweet = json.loads(data)
                #tweet_count += 1
                print(data + '\n\n\n\n')
                tweet = filterLocation(json.loads(data))
                tf.write(str(tweet))
                
                db.save(tweet)
                
                return True
        
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True        
            
#        else:
#            stream.disconnect()
        
    def on_status(self, status):
        print(status.text)
        #if 'manchester united' in status.text.lower():
            #print(status.coordinates)

    def on_error(self, status):
        print(status)
        if status == 420:
            # returning False in on_error disconnects the stream
            return True


 
# Handle Twitter authetification and the connection to Twitter Streaming API
track_list = ["vegan", "vegetarian", "veggie", "#vegan", "#vegetarian", "#veggie"]#keywords
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
#stream.filter(track=track_list)
stream.filter(locations =location)