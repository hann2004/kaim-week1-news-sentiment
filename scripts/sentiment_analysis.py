import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(df):
    """
    Perform sentiment analysis on news headlines
    Returns DataFrame with sentiment scores
    """
    vader = SentimentIntensityAnalyzer()
    
    def textblob_sentiment(text):
        try:
            return TextBlob(str(text)).sentiment.polarity
        except:
            return 0
    
    def vader_sentiment(text):
        try:
            return vader.polarity_scores(str(text))['compound']
        except:
            return 0
    
    # Calculate both sentiment scores
    df['textblob_sentiment'] = df['headline'].apply(textblob_sentiment)
    df['vader_sentiment'] = df['headline'].apply(vader_sentiment)
    
    return df