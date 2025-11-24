import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def calculate_stock_returns(df):
    """
    Calculate daily stock returns
    """
    df['daily_return'] = df['Close'].pct_change() * 100
    return df

def align_sentiment_with_returns(news_df, stock_df, stock_symbol):
    """
    Align news sentiment with stock returns by date
    """
    # Filter news for specific stock
    stock_news = news_df[news_df['stock'] == stock_symbol].copy()
    
    # Extract date from news (assuming 'date_clean' column exists)
    stock_news['date_only'] = pd.to_datetime(stock_news['date_clean']).dt.date
    
    # Group sentiment by date
    daily_sentiment = stock_news.groupby('date_only').agg({
        'vader_sentiment': 'mean',
        'textblob_sentiment': 'mean'
    }).reset_index()
    
    # Prepare stock data
    stock_data = stock_df.copy()
    stock_data['date_only'] = pd.to_datetime(stock_data['Date']).dt.date
    stock_data = calculate_stock_returns(stock_data)
    
    # Merge sentiment with stock returns
    merged_data = pd.merge(daily_sentiment, stock_data, on='date_only', how='inner')
    
    return merged_data

def calculate_correlations(merged_data):
    """
    Calculate correlation between sentiment and stock returns
    """
    correlations = {}
    
    # VADER sentiment correlation
    if len(merged_data) > 1:
        corr_vader, pval_vader = pearsonr(merged_data['vader_sentiment'], merged_data['daily_return'])
        correlations['vader'] = {'correlation': corr_vader, 'p_value': pval_vader}
    
    # TextBlob sentiment correlation
    if len(merged_data) > 1:
        corr_textblob, pval_textblob = pearsonr(merged_data['textblob_sentiment'], merged_data['daily_return'])
        correlations['textblob'] = {'correlation': corr_textblob, 'p_value': pval_textblob}
    
    return correlations