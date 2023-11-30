import json

# Read tweets from JSON file
with open('tweets.json', 'r') as file:
    tweets = json.load(file)

# Print each tweet
for tweet in tweets:
    print(tweet)
    print()
