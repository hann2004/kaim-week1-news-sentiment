import pandas as pd
import talib
import matplotlib.pyplot as plt
import sys
import os

# Add the parent directory to Python path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_prep import load_stock_data

def calculate_technical_indicators(df):
    """
    Calculate technical indicators using TA-Lib
    """
    # Moving Averages
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    
    # RSI
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    
    # MACD
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'])
    
    # Bollinger Bands
    df['BB_upper'], df['BB_middle'], df['BB_lower'] = talib.BBANDS(df['Close'], timeperiod=20)
    
    return df

def main():
    # Load the data
    files = ["AAPL.csv", "GOOG.csv", "MSFT.csv", "AMZN.csv", "NVDA.csv", "META.csv"]
    stocks = load_stock_data(files)
    
    # Calculate indicators for each stock
    for symbol, df in stocks.items():
        print(f"Calculating indicators for {symbol}...")
        df_with_indicators = calculate_technical_indicators(df)
        stocks[symbol] = df_with_indicators
    
    return stocks

if __name__ == "__main__":
    stocks = main()
    # Show results for one stock
    symbol = "AAPL"
    print(f"\nTechnical indicators for {symbol}:")
    print(stocks[symbol][['Date', 'Close', 'SMA_20', 'RSI', 'MACD']].tail())