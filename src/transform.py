import pandas as pd


def prepare_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare stock data for storage

    Args:
        df: Raw stock price DataFrame

    Returns:
        Processed DataFrame
    """
    # Add some basic technical indicators
    df["returns"] = df["close"].pct_change()
    df["moving_avg_5d"] = df["close"].rolling(window=5).mean()
    df["moving_avg_20d"] = df["close"].rolling(window=20).mean()

    # Drop any NaN values
    df = df.dropna()

    return df
