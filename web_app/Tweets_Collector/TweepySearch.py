import tweepy
from tweepy import OAuthHandler
import datetime
import time
import TwitterCredentials
from TweepyREST import get_tweet_by_screenname

def load_api():

    auth = OAuthHandler(TwitterCredentials.CONSUMER_KEY,
                                TwitterCredentials.CONSUMER_SECRET)
    auth.set_access_token(TwitterCredentials.ACCESS_TOKEN,
                                  TwitterCredentials.ACCESS_TOKEN_SECRET)
    # load the twitter API via tweepy
    return tweepy.API(auth, wait_on_rate_limit=True)
#    return tweepy.API(auth)


def get_targetDate(today):
    targetDate = today - datetime.timedelta(days = 7)
    targetDate = targetDate.strftime('%Y-%m-%d')
    return targetDate

api = load_api()
today = datetime.date.today()

geocode= '-37.2803,145.2201,150km'
screen_name_list = []

count = 0
stop_iter_count = 50000

place =  api.geo_search(query="AU", granularity = "country")
place_id = place[0].id
tweets = tweepy.Cursor(api.search, q = "place:%s"%place_id, tweet_mode='extended', 
                       since = get_targetDate(today), end = today).items()
sinceid = tweets[0]._json.get('id')

while True:
    try:
        for tweet in tweets:
            if tweet.place is not None and tweet.lang == 'en':

                count += 1
                print('Screen_name:', tweet.user.screen_name)
                print('Text:', tweet.full_text)
                print('Place:', tweet.place)
                print('Coordinates:', tweet.coordinates)
                print('language:', tweet.lang)
                print('\n\n')
                print('Tweets count:', str(count))
                print('This tweet was created at: ', tweet.created_at)
                print('Time right now:', datetime.datetime.now())
                print('\n\n')
                screen_name_list.append(str(tweet.user.screen_name))

            if count > stop_iter_count:
                break;

    except tweepy.TweepError:
        print('Tweepy error. The system is gonna sleep for 15 min. ')
        time.sleep(15*60+1)
        pass;

    except StopIteration:
        pass;

    break;

screen_name_set = set(screen_name_list)
print(len(screen_name_set), '\n\n\n\n')
for name in screen_name_set:
    get_tweet_by_screenname(name, None)
##    get_tweet_by_screenname(name, 'Tweepy_rest_api.txt')
