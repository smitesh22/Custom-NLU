import tweepy
import os 

auth = tweepy.OAuth1UserHandler(
    os.environ.get("TWITTER_API_KEY"),
    os.environ.get("TWITTER_API_KEY_SECRET")
)
auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), 
    os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
)

api = tweepy.API(auth)

query = 'located at'
tweet_count = 1  # Number of tweets to fetch

print(os.environ.get("TWITTER_API_KEY"))
tweets = api.search_tweets(q=query, lang='en', count=tweet_count)

# Display fetched tweets
for tweet in tweets:
    if "located at" in tweet.full_text.lower():
        print(tweet.full_text)

"""
export TWITTER_API_KEY='N43AwQd7n0NDKJ6IVQKxqKAsB'
export TWITTER_API_KEY_SECRET='X1atvfTEgCBfguHuK7Qa4ct3cCtsFbUcoV0YSiozQ0KqkY2clI'
export TWITTER_ACCESS_TOKEN='739863771946979329-3pC66AXNLcPeNyMc8LJa2ONORltRKjm'
export TWITTER_ACCESS_TOKEN_SECRET='FX7CNYaed10N0MtWIurhVkYkbCOQtYXifzgMoTtuUmyuT'
export CLIENT_ID='UXc0OHJxTzVQQU9oTTIyY2Z3Q1Y6MTpjaQ'
export CLIENT_SECRET='kxiecLMn1UPKHyRs--m0-kJH-Qn6p0jm9phq3ykfK2jEsK6FWU'
 """
 