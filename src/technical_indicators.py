# src/technical_indicators.py

import pandas as pd
import talib

def add_sma(df, windows=[5, 10, 20, 50, 100, 200]):
    """Add Simple Moving Averages"""
    for window in windows:
        df[f'SMA_{window}'] = talib.SMA(df['Close'], timeperiod=window)
    return df

def add_ema(df, windows=[5, 10, 20, 50, 100, 200]):
    """Add Exponential Moving Averages"""
    for window in windows:
        df[f'EMA_{window}'] = talib.EMA(df['Close'], timeperiod=window)
    return df

def add_rsi(df, period=14):
    """Add Relative Strength Index"""
    df['RSI'] = talib.RSI(df['Close'], timeperiod=period)
    return df

def add_macd(df, fastperiod=12, slowperiod=26, signalperiod=9):
    """Add MACD and its components"""
    macd, macd_signal, macd_hist = talib.MACD(df['Close'], fastperiod=fastperiod,
                                              slowperiod=slowperiod, signalperiod=signalperiod)
    df['MACD'] = macd
    df['MACD_Signal'] = macd_signal
    df['MACD_Hist'] = macd_hist
    return df

def add_bollinger_bands(df, timeperiod=20, nbdevup=2, nbdevdn=2):
    """Add Bollinger Bands"""
    upper, middle, lower = talib.BBANDS(df['Close'], timeperiod=timeperiod,
                                        nbdevup=nbdevup, nbdevdn=nbdevdn, matype=0)
    df['BB_Upper'] = upper
    df['BB_Middle'] = middle
    df['BB_Lower'] = lower
    return df

# Map function names to actual functions for dynamic use
INDICATOR_FUNCTIONS = {
    "sma": add_sma,
    "ema": add_ema,
    "rsi": add_rsi,
    "macd": add_macd,
    "bollinger": add_bollinger_bands
}

def add_indicators(df, indicators=None, **kwargs):
    """
    Add selected indicators dynamically.
    :param df: DataFrame
    :param indicators: list of indicator names as strings, e.g. ["sma", "rsi"]
    :param kwargs: optional keyword args passed to each indicator function
    """
    if indicators is None:
        indicators = INDICATOR_FUNCTIONS.keys()  # add all by default

    for ind in indicators:
        func = INDICATOR_FUNCTIONS.get(ind.lower())
        if func:
            df = func(df, **kwargs)
    return df
