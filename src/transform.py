import pandas as pd
import numpy as np

def prepare_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare stock data for storage
    
    Args:
        df: Raw stock price DataFrame
    
    Returns:
        Processed DataFrame
    """
    # Make a copy to avoid modifying the input DataFrame
    df = df.copy()
    
    # Ensure all required columns exist
    required_columns = {'date', 'close', 'open', 'high', 'low', 'volume'}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Calculate returns
    df['returns'] = df['close'].pct_change()
    
    # Calculate moving averages
    df['moving_avg_5d'] = df['close'].rolling(window=5).mean()
    df['moving_avg_20d'] = df['close'].rolling(window=20).mean()
    
    # Drop any NaN values
    df = df.dropna()
    
    # Ensure all columns are present in the expected order
    expected_columns = [
        'date', 'close', 'open', 'high', 'low', 'volume',
        'returns', 'moving_avg_5d', 'moving_avg_20d'
    ]
    
    # Reorder columns
    df = df[expected_columns]
    
    return df
