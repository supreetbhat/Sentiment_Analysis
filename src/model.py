from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Test on a sample Elon tweet
sample = "Fuck you"
result = sentiment_pipeline(sample)
print(result)
