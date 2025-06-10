import pandas as pd
import re

def clean_tweet(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    
    # Remove punctuation and symbols
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove extra whitespace
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)

    return text

def main():
    # Load the dataset
    df = pd.read_csv("svenv/data/tweets.csv")

    # Drop rows with missing data
    df.dropna(subset=["tweet"], inplace=True)

    # Apply cleaning
    df["cleaned_tweet"] = df["tweet"].apply(clean_tweet)

    # Save cleaned data
    df[["cleaned_tweet"]].to_csv("svenv/data/elon_tweets_cleaned.csv", index=False)
    print("✅ Cleaned tweets saved to 'elon_tweets_cleaned.csv'")

if __name__ == "__main__":
    main()
