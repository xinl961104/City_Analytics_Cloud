#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:32:28 2020

@author: danny
"""
import tweepy
from tweepy import OAuthHandler
import datetime as dt
import time
#ctn = 0
#with open('result_tweets.json','r') as lines:
#    for line in lines:
#        data = json.loads(line)
#        if data.get('geo') != None:
#            print(data['geo'])
#            ctn += 1
#        if data.get('place') != None:
#            print(data['place'])
#            ctn += 1
#    print(ctn, 'tweets have geo tag')
    
    
#Access token : 1131912292054863872-3Q10teYItIyGpk4eKPFvXEB26VbW6H
#Access token secret : Owsl6iSNrDyaHHuiFRiAyQpoGB1H7PhQrfBnP6bVbveXG
def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = 'ORz2DIXszIiSTBPvtl3QIJ2R7'
    consumer_secret = 'Ol4PHsLWtW25J0IdhTHydLFlSeoGtuEChhavufqZZ8ncWAZWl8'
    access_token = '1131912292054863872-3Q10teYItIyGpk4eKPFvXEB26VbW6H'
    access_secret = 'Owsl6iSNrDyaHHuiFRiAyQpoGB1H7PhQrfBnP6bVbveXG'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

def tweet_search(api, query, max_tweets, since, until, geocode):
    ''' Function that takes in a search string 'query', the maximum
        number of tweets 'max_tweets', and the minimum (i.e., starting)
        tweet id. It returns a list of tweepy.models.Status objects. '''

    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=remaining_tweets,since=since, until=until, geocode=geocode)
            print('found',len(new_tweets),'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
        except tweepy.TweepError:
            print('exception raised, waiting 15 minutes')
            print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
            time.sleep(15*60)
            break # stop the loop
    return searched_tweets

def main():
    api = load_api()
    n = 0
    place = api.geo_search(query="AU", granularity = "country")
    place_id = place[0].id
    print(place_id)
    q="place:%s %s"%(place_id, '#vegan')
    tweets = tweepy.Cursor(api.search, q=q, since="2020-04-27", until="2020-05-01", tweet_mode="extended").items()
    while True:
        try:
            n += 1
            tweet = tweets.next()
            tweetJson = tweet._json
            print(tweetJson)
        except StopIteration:
            print('Loop is over.')
            break;
    print('-'*30)
    print(n, 'relevant tweest found')
if __name__ == "__main__":
    main()