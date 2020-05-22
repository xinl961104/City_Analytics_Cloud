# -*- coding: utf-8 -*-

import tweepy
from tweepy.auth import OAuthHandler
import json
import time
import couchdb
import TwitterCredentials


def load_api():

    auth = OAuthHandler(TwitterCredentials.CONSUMER_KEY,
                                TwitterCredentials.CONSUMER_SECRET)
    auth.set_access_token(TwitterCredentials.ACCESS_TOKEN,
                                  TwitterCredentials.ACCESS_TOKEN_SECRET)
    # load the twitter API via tweepy
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

api = load_api()

def get_tweet_by_screenname(screen_name):
    api = load_api()

    # COUCHDB_SERVER = 'http://admin:password@115.146.92.188:5984/' #My Own Database
    COUCHDB_SERVER = 'http://admin:password@172.26.129.40:5984/' #Group DB 
    couch = couchdb.Server(COUCHDB_SERVER)
    DBNAME = 'historical_data'
    try:
        db = couch.create(DBNAME)
    except:
        db = couch[DBNAME]

    while True:
        try:
            for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name,
                                       tweet_mode='extended', exclude_replies=False).items():
                
                if tweet.lang == 'en':
                    
                    temp_json = tweet._json
                    temp_json['_id'] = tweet.id_str
                    
                    full_text_retweeted = tweet._json.get('retweeted_status')
                    
                    if full_text_retweeted != None:
                        temp_json['text'] = full_text_retweeted.get('full_text')
                    else:
                        temp_json['text'] = tweet.full_text
                        
#                     del temp_json['full_text']
                    try:
                        db.save(temp_json)
           
                    except:
                        pass;
                    

        except tweepy.TweepError:
            print('Tweepy error. The system is gonna sleep for 1 min. ')
            time.sleep(60)

        except StopIteration:
            pass;
        break;
        
