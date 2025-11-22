import pandas as pd
import os

DATA_DIR = "data"  # path to your CSV files

def load_stock_data(filenames):
    """
    Load multiple stock CSV files into a dictionary of DataFrames.
    filenames: list of CSV filenames
    Returns: dict {symbol: DataFrame}
    """
    stock_data = {}
    for file in filenames:
        # Use the file name (without .csv) as the stock symbol
        symbol = os.path.splitext(file)[0]
        df = pd.read_csv(os.path.join(DATA_DIR, file), parse_dates=['Date'])
        df.sort_values('Date', inplace=True)
        df.reset_index(drop=True, inplace=True)
        stock_data[symbol] = df
    return stock_data

if __name__ == "__main__":
    # Example usage
    files = ["AAPL.csv", "GOOG.csv", "MSFT.csv", "AMZN.csv", "NVDA.csv", "META.csv"]
    stocks = load_stock_data(files)
    for symbol, df in stocks.items():
        print(f"{symbol} data shape:", df.shape)
        print(df.head())
