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


count = 0
api = load_api()


def get_tweet_by_screenname(screen_name, fetched_tweets_file_name):
    temp_json = {}
    count = 0
    api = load_api()
    
    
    
    COUCHDB_SERVER = 'http://admin:pass@115.146.92.188:5984/' #My Own Database
#    COUCHDB_SERVER = 'http://admin:password@172.26.132.199:5984/' #Group DB
    couch = couchdb.Server(COUCHDB_SERVER)
    DBNAME = 'rest_api_test_05_15'
    db = couch.create(DBNAME)
#    db = couch[DBNAME]
    
    
    while True:
        while count < 3201:
            try:  
                for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, 
                                           exclude_replies=True).items(): 
                                 
                    tweet_id_str = tweet.id_str
                    tweet_text = tweet.text  
                    create_time = tweet.created_at 
                    screen_name = tweet.user.screen_name 
                    place = tweet.place
                    coordinates = tweet.coordinates
                    entities = tweet.entities
                    lang = tweet.lang
                    
                    temp_json['tweet_id'] = tweet_id_str
                    temp_json['tweet_text'] = str(tweet_text)
                    temp_json['timestamp'] = str(create_time)
                    temp_json['screen_name'] = str(screen_name)
                    temp_json['place'] = str(place)
                    temp_json['coordinates'] = str(coordinates)
                    temp_json['entities'] = str(entities)
                    temp_json['lang'] = str(lang)
                    
                    print(temp_json)
                    print(str(count), '\n\n\n\n\n')
                    
                    count += 1
                    jsonFile = json.dumps(temp_json)
                    
                    if fetched_tweets_file_name is not None:
                        with open(fetched_tweets_file_name, 'a') as tf:
                            tf.write(str(jsonFile) + '\n')
                    
                    db.save(temp_json)        
                    temp_json = {}
                    
                    
            except tweepy.TweepError:  
                time.sleep(60)
                
            except StopIteration:
                pass;
        break;
    
get_tweet_by_screenname('theresa_may', 'Tweepy_rest_api.json')
    
#    for tweet in tweepy.Cursor(api.user_timeline, screen_name = name,
#                               tweet_mode='extended').items(20):
##        api.user_timeline(screen_name=name):
#        print(tweet.text)
#        count += 1
#        print(str(count), '\n\n\n\n\n')

#    tweets = tweepy.Cursor(api.user_timeline, screen_name=name,
##                               tweet_mode='extended', include_rt=True,
##                               exclude_replies=True).items()
#    
#    alltweets.extend(tweets)
#    
#    oldest = alltweets[-1].id - 1
#    while len(tweets) > 0:
##        print("getting tweets before %s" % (oldest))
#        #tweets = api.user_timeline(screen_name = name, count=200, max_id=oldest)
#            tweets = tweepy.Cursor(api.user_timeline, screen_name=name,
#                               tweet_mode='extended', include_rt=True,
#                               exclude_replies=True).items()
#        alltweets.extend(tweets)
#        oldest = alltweets[-1].id - 1
##        print("...%s tweets downloaded so far" % (len(alltweets)))
#        outtweets = [[tweet.id, tweet.created_at, tweet.place, tweet.coordinates, 
#                      #tweet.text, 
#                      tweet.entities, tweet.retweet_count, tweet.favorite_count,
#                      tweet.lang, tweet.user] for tweet in alltweets]
#        for tweet in outtweets:
#            print(tweet)
#            break;
#        break;
            
    
#    alltweets = tweepy.Cursor(api.user_timeline, screen_name=name,
#                               tweet_mode='extended', include_rt=True,
#                               exclude_replies=True).items()
        
#        alltweets.extend(tweets)
#    for tweet in alltweets: 
#            
#        try:
#            count += 1
#
#            outtweets = [[tweet.id_str, tweet.created_at, tweet.place, 
#                            tweet.coordinates, #tweet.text, 
#                            tweet.entities, 
#                            tweet.lang, tweet.user] for tweet in alltweets]
         
#            for tweet in outtweets:
#                temp_json['id'] = tweet[0]
#                temp_json['created_at'] = str(tweet[1])
#                temp_json['place'] = str([tweet[2]])
#                temp_json['coordinates'] = str(tweet[3])
#                temp_json['text'] = str(tweet[4])
#                temp_json['entities'] = str(tweet[5])
#                temp_json['lang'] = tweet[6]
#                temp_json['user'] = str(tweet[7])
#        
#        
#            with open('trial.json', 'w') as f:
#                json.dump(temp_json, f)
#                f.write('\n')
                    
                    #            with open('covid_hugeAU_sample_0505.json', 'a') as f:
#                for tweet in tweets:
#                    json.dump(tweet._json, f)
#                    f.write('\n')  
#        pass
                #db.save(temp_json)
#        temp_json = {}
                
#        except tweepy.TweepError:  
#            time.sleep(60)
#            pass
    
    
    
#get_tweet('realDonaldTrump')
#def get_tweets(screen_name):
#    alltweets = []
#    
#    new_tweets = load_api().user_timeline(screen_name = screen_name,count=200)
#    alltweets.extend(new_tweets)
#    oldest = alltweets[-1].id - 1
#    
#    while len(new_tweets) > 0:
#        #print("getting tweets before %s" % (oldest))
#    
#        new_tweets = load_api().user_timeline(screen_name = screen_name,
#                                   count=200, max_id=oldest)
#        
#        alltweets.extend(new_tweets)
#        oldest = alltweets[-1].id - 1
#        #print("...%s tweets downloaded so far" % (len(alltweets)))   
#
#            
#        outtweets = [[tweet.id_str, tweet.created_at, tweet.place, 
#                      tweet.coordinates, tweet.text, tweet.lang]
#                     for tweet in alltweets]
#        
#        print(outtweets)
    
    
#        with open('%s_tweets.csv' % screen_name, 'w') as f:
#            writer = csv.writer(f)
#            writer.writerow(["id","place", "created_at","text"])
#            writer.writerows(outtweets)
#        pass




'''
def main():
    #search_list = ['vegan OR #vegan', 'veggie OR #veggie', 'vegie OR #vegie', 'vegetarian OR #vegetarian']
#                  # 'veganism', 'plant-eating', 'herbivorous', 'plant-based', 'vegetarianism']
    search_list = ['covid OR #covid']
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
                with open('raw.json', 'a') as f:
                    for tweet in new_tweets:
                        json.dump(tweet._json, f)
                        f.write('\n')    
                maxid = new_tweets[-1]._json.get('id')
            except tweepy.TweepError:
                print('exception raised, waiting 16 minutes')
                print('(until:', dt.datetime.now()+dt.timedelta(minutes=16), ')')
                time.sleep(15*60 + 3)
                break # stop the loop

''' 
    