import pandas as pd
import numpy as np

def calculate_pynance_metrics(df):
    """
    Calculate additional financial metrics that PyNance would provide
    """
    # Volatility metrics
    df['daily_volatility'] = df['Close'].pct_change().rolling(window=20).std() * np.sqrt(252)
    
    # Price momentum
    df['price_momentum'] = (df['Close'] / df['Close'].shift(20) - 1) * 100
    
    # Volume indicators
    df['volume_sma'] = df['Volume'].rolling(window=20).mean()
    df['volume_ratio'] = df['Volume'] / df['volume_sma']
    
    # Support and resistance levels
    df['resistance'] = df['High'].rolling(window=50).max()
    df['support'] = df['Low'].rolling(window=50).min()
    
    return df