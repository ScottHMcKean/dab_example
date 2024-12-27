import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def fetch_stock_data(
    symbol: str, start_date: datetime = None, end_date: datetime = None
) -> pd.DataFrame:
    """
    Fetch stock data from Yahoo Finance

    Args:
        symbol: Stock symbol (e.g., 'AAPL')
        start_date: Start date for data collection
        end_date: End date for data collection

    Returns:
        DataFrame with stock price data
    """
    if not start_date:
        start_date = datetime.now() - timedelta(days=365)
    if not end_date:
        end_date = datetime.now()

    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start_date, end=end_date)

    # Reset index to make date a column
    df = df.reset_index()

    # Ensure column names are lowercase and consistent
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Ensure 'date' column exists (it might be 'Date' or 'datetime')
    if 'date' not in df.columns and 'datetime' in df.columns:
        df = df.rename(columns={'datetime': 'date'})

    # Ensure required columns exist
    required_columns = {'date', 'open', 'high', 'low', 'close', 'volume'}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return df
