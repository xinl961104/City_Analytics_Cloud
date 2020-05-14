# -*- coding: utf-8 -*-

import tweepy
from tweepy import OAuthHandler
import datetime as dt
import time
import json
import TwitterCredentials

def load_api():

    auth = OAuthHandler(TwitterCredentials.CONSUMER_KEY, 
                                TwitterCredentials.CONSUMER_SECRET)
    auth.set_access_token(TwitterCredentials.ACCESS_TOKEN, 
                                  TwitterCredentials.ACCESS_TOKEN_SECRET)
    # load the twitter API via tweepy
    return tweepy.API(auth, wait_on_rate_limit=True)

def main():
    search_list = ['vegan OR #vegan', 'veggie OR #veggie', 'vegie OR #vegie', 'vegetarian OR #vegetarian']
#                  # 'veganism', 'plant-eating', 'herbivorous', 'plant-based', 'vegetarianism']
#    search_list = ['covid OR #covid']
    geocode="-23.8136,133.9631,2500km"
    time_limit = 9 # time limit in hours
    start = dt.datetime.now()
    end = start + dt.timedelta(hours=time_limit)
    api = load_api()
#    while dt.datetime.now() < end:
#        for word in search_list:
#            tweets = tweet_search(api, 'covid OR #covid', 1500, "2020-05-05", "2020-05-06", geocode)
#            with open('covid_hugeAU_sample_0505.json', 'a') as f:
#                for tweet in tweets:
#                    json.dump(tweet._json, f)
#                    f.write('\n')    
#    api.search(q=query, count=remaining_tweets,since=since, until=until, geocode=geocode)
    latest_max_id = [] 
    iteration = 0
    for q in search_list:
        new_tweets = api.search(q=q, geocode=geocode)
        maxid = new_tweets[0]._json.get('id')
        latest_max_id.append(maxid)
    for query, mid in zip(search_list,latest_max_id):
        maxid = mid
        while dt.datetime.now() < end:
            try:
                iteration += 1    
                new_tweets = api.search(q=query, geocode=geocode, max_id = maxid)
                with open('raw.json', 'w') as f:
                    for tweet in new_tweets:
                        
                        if tweet._json['place']['country_code'] == 'AU':
                            print(tweet._json)
                            print('\n\n\n\n')
                            json.dump(tweet._json, f)
                            f.write('\n\n')    
                maxid = new_tweets[-1]._json.get('id')
#            except tweepy.TweepError:
#                print('exception raised, waiting 16 minutes')
#                print('(until:', dt.datetime.now()+dt.timedelta(minutes=16), ')')
#                time.sleep(15*60 + 3)
#                break # stop the loop
            
            except:
                pass

        

###########################################    
#    hsg_list = ['vegan']# 'veggie', 'vegan', 'vegetarian']#, '#veggie', '#veganfood', '#veganlife', '#vegetarian']
#    api = load_api()
#    n = 0
#    place = api.geo_search(query="Melbourne", granularity = "city")
#    place_id = place[0].id
#    for hst in hsg_list:
#        q="place:%s %s"%(place_id, hst)
#        tweets = tweepy.Cursor(api.search, q=q, since="2020-04-25", until="2020-05-05", tweet_mode="extended").items()
#        while True:
#            try:
#                n += 1
#                tweet = tweets.next()
#                with open('melb_vegan_sample.json', 'a') as f:
#                    for tweet in tweets:
#                        json.dump(tweet._json, f)
#                        f.write('\n')
#            except StopIteration:               
#                print('Loop is over.')
#                break;
#    print('-'*30)
#    print(n, 'relevant tweest found')
if __name__ == "__main__":
    main()