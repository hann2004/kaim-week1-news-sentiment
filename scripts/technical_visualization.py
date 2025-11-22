import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.technical_analysis import calculate_technical_indicators
from src.data_prep import load_stock_data

def plot_technical_indicators(stocks, symbol="AAPL"):
    """
    Create visualization for technical indicators
    """
    df = stocks[symbol]
    
    # Create subplots
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle(f'Technical Analysis for {symbol}', fontsize=16)
    
    # Plot 1: Price and Moving Averages
    axes[0].plot(df['Date'], df['Close'], label='Close Price', linewidth=1)
    axes[0].plot(df['Date'], df['SMA_20'], label='20-day SMA', linewidth=1)
    axes[0].plot(df['Date'], df['SMA_50'], label='50-day SMA', linewidth=1)
    axes[0].set_title('Price and Moving Averages')
    axes[0].legend()
    axes[0].grid(True)
    
    # Plot 2: RSI
    axes[1].plot(df['Date'], df['RSI'], label='RSI', color='orange', linewidth=1)
    axes[1].axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
    axes[1].axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
    axes[1].set_title('RSI (14-day)')
    axes[1].legend()
    axes[1].grid(True)
    
    # Plot 3: MACD
    axes[2].plot(df['Date'], df['MACD'], label='MACD', linewidth=1)
    axes[2].plot(df['Date'], df['MACD_signal'], label='Signal Line', linewidth=1)
    axes[2].set_title('MACD')
    axes[2].legend()
    axes[2].grid(True)
    
    plt.tight_layout()
    plt.savefig(f'outputs/{symbol}_technical_analysis.png')
    plt.show()

def main():
    # Load data and calculate indicators
    files = ["AAPL.csv", "GOOG.csv", "MSFT.csv", "AMZN.csv", "NVDA.csv", "META.csv"]
    stocks = load_stock_data(files)
    
    # Calculate indicators for each stock
    for symbol, df in stocks.items():
        print(f"Calculating indicators for {symbol}...")
        df_with_indicators = calculate_technical_indicators(df)
        stocks[symbol] = df_with_indicators
    
    # Plot for each stock
    for symbol in stocks.keys():
        print(f"Creating visualization for {symbol}...")
        plot_technical_indicators(stocks, symbol)
    
    return stocks

if __name__ == "__main__":
    # Create outputs directory
    os.makedirs('outputs', exist_ok=True)
    stocks = main()