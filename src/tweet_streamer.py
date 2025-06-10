import tweepy
import os
import pandas as pd
from dotenv import load_dotenv

# Load API key
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Initialize Tweepy client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Get Elon Musk's user ID
user = client.get_user(username="elonmusk")
elon_id = user.data.id

# Fetch up to 100 recent tweets from Elon
tweets = client.get_users_tweets(
    id=elon_id,
    max_results=100,
    tweet_fields=["text"]
)

# Extract only the text content
tweet_texts = [tweet.text for tweet in tweets.data]

# Save to CSV
df = pd.DataFrame(tweet_texts, columns=["tweet"])
df.to_csv("svenv/data/elon_tweets.csv", index=False)
