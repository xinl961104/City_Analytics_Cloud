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
    return tweepy.API(auth, wait_on_rate_limit=True)


api = load_api()


def get_tweet_by_screenname(screen_name, fetched_tweets_file_name):
    count = 0
    api = load_api()

    # COUCHDB_SERVER = 'http://admin:password@115.146.92.188:5984/' #My Own Database
    COUCHDB_SERVER = 'http://admin:password@172.26.129.40:5984/'  #Group DB
    couch = couchdb.Server(COUCHDB_SERVER)
    DBNAME = 'historical_data'
    try:
        db = couch.create(DBNAME)
    except:
        db = couch[DBNAME]

    while True:
        try:
            for tweet in tweepy.Cursor(api.user_timeline,
                                       screen_name=screen_name,
                                       exclude_replies=False).items():

                if tweet.lang == 'en':

                    # temp_json = {}
                    # temp_json['_id'] = tweet.id_str
                    # temp_json['tweet_text'] = str(tweet.text)
                    # temp_json['timestamp'] = str(tweet.created_at)
                    # temp_json['screen_name'] = str(tweet.user.screen_name)
                    # temp_json['place'] = str(tweet.place)
                    # temp_json['coordinates'] = str(tweet.coordinates)
                    # temp_json['entities'] = str(tweet.entities)
                    # temp_json['lang'] = str(tweet.lang)
                    # print(temp_json)
                    # print(str(count), '\n\n\n\n\n')

                    count += 1
                    # jsonFile = json.dumps(temp_json)
                    temp_json = tweet._json
                    temp_json['_id'] = tweet.id_str
                    try:
                        db.save(temp_json)
                    except:
                        pass
                    # if fetched_tweets_file_name is not None:
                    #     with open(fetched_tweets_file_name, 'a') as tf:
                    #         tf.write(str(jsonFile) + '\n\n')

                    if count > 3500:
                        break

        except tweepy.TweepError:
            print('Tweepy error. The system is gonna sleep for 1 min. ')
            time.sleep(60)

        except StopIteration:
            pass
        break


#get_tweet_by_screenname('realDonaldTrump', None)
