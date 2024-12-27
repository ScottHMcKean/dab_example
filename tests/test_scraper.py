import pytest
from datetime import datetime, timedelta
import pandas as pd
from src.scraper import fetch_stock_data

@pytest.fixture
def mock_yfinance(mocker):
    """Mock yfinance to avoid actual API calls during tests"""
    mock_ticker = mocker.patch('yfinance.Ticker')
    
    # Create sample data
    dates = pd.date_range(start='2023-01-01', end='2023-01-10')
    sample_data = pd.DataFrame({
        'Date': dates,
        'Open': [150.0] * len(dates),
        'High': [155.0] * len(dates),
        'Low': [145.0] * len(dates),
        'Close': [152.0] * len(dates),
        'Volume': [1000000] * len(dates)
    })
    sample_data.set_index('Date', inplace=True)
    
    # Configure the mock to return our sample data
    mock_ticker.return_value.history.return_value = sample_data
    return mock_ticker

def test_fetch_stock_data_default_dates(mock_yfinance):
    """Test fetching stock data with default dates"""
    df = fetch_stock_data('AAPL')
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'date' in df.columns
    assert all(col in df.columns for col in ['open', 'high', 'low', 'close', 'volume'])

def test_fetch_stock_data_custom_dates(mock_yfinance):
    """Test fetching stock data with custom date range"""
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    
    df = fetch_stock_data('AAPL', start_date, end_date)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df) == 10  # Should have 10 days of data

def test_fetch_stock_data_column_names(mock_yfinance):
    """Test that column names are properly formatted"""
    df = fetch_stock_data('AAPL')
    
    expected_columns = {'date', 'open', 'high', 'low', 'close', 'volume'}
    assert all(col.islower() for col in df.columns)
    assert all(col.replace('_', '').isalnum() for col in df.columns)
    assert set(df.columns) >= expected_columns 