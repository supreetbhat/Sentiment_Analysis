# Elon Musk Tweet Sentiment Analysis

This project performs sentiment analysis on a dataset of Elon Musk tweets using a pretrained Hugging Face model.

## Features

- Static sample of 100 Elon tweets
- Regex-based text cleaning
- Sentiment prediction using Hugging Face Transformers
- Output includes tweet, sentiment label, and confidence score

## Files

- `tweets.csv`: Raw tweets
- `clean.py`: Cleans tweet text (lowercase, removes URLs, mentions, etc.)
- `elon_tweets_cleaned.csv`: Cleaned tweet output
- `model.py`: Applies sentiment model and predicts labels
- `tweet_streamer.py`: To fetch the targeted tweets using twitter api

## Model Used

- `distilbert-base-uncased-finetuned-sst-2-english`
- Returns `POSITIVE` or `NEGATIVE` sentiment
