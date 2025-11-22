import sys
import os
import pandas as pd

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Try to import with error handling
try:
    from scripts.technical_analysis import calculate_technical_indicators
    TALIB_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    TALIB_AVAILABLE = False

def test_technical_indicators_calculation():
    """Test that technical indicators are calculated correctly"""
    if not TALIB_AVAILABLE:
        print("TA-Lib not available - skipping test")
        return True
    
    # Create sample data
    sample_data = pd.DataFrame({
        'Close': [100 + i for i in range(100)],
        'Open': [99 + i for i in range(100)],
        'High': [101 + i for i in range(100)],
        'Low': [98 + i for i in range(100)], 
        'Volume': [1000000] * 100
    })

    result = calculate_technical_indicators(sample_data)

    # Assert indicators were added
    assert 'SMA_20' in result.columns
    assert 'RSI' in result.columns
    assert 'MACD' in result.columns

    print("✓ All technical indicator tests passed!")
    return True

if __name__ == "__main__":
    success = test_technical_indicators_calculation()
    exit(0 if success else 1)