#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import datetime
import xlsxwriter

from importlib._bootstrap_external import SourceFileLoader


dictPath = 'twitter_credentials.py'
secret = SourceFileLoader("twitter_credentials", dictPath).load_module()

CONSUMER_KEY = secret.secretTwitter.get("CONSUMER_KEY")
CONSUMER_SECRET = secret.secretTwitter.get("CONSUMER_SECRET")
ACCESS_TOKEN = secret.secretTwitter.get("ACCESS_TOKEN")
ACCESS_SECRET = secret.secretTwitter.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

username = "Huawei"
startDate = datetime.datetime(2014, 6, 1, 0, 0, 0)
endDate =   datetime.datetime(2015, 1, 1, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1], " - fetching some more")
    print()
    print()
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")