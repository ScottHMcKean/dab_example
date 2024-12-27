import pytest
import pandas as pd
import numpy as np
from src.transform import prepare_stock_data

@pytest.fixture
def sample_stock_data():
    """Create sample stock data for testing"""
    dates = pd.date_range(start='2023-01-01', end='2023-01-25')
    df = pd.DataFrame({
        'date': dates,
        'close': [100 + i * 0.5 for i in range(len(dates))],
        'open': [100 + i * 0.3 for i in range(len(dates))],
        'high': [100 + i * 0.7 for i in range(len(dates))],
        'low': [100 + i * 0.1 for i in range(len(dates))],
        'volume': [1000000] * len(dates)
    })
    return df

def test_prepare_stock_data_columns(sample_stock_data):
    """Test that all expected columns are present after transformation"""
    df = prepare_stock_data(sample_stock_data)
    
    expected_columns = {
        'date', 'close', 'open', 'high', 'low', 'volume',
        'returns', 'moving_avg_5d', 'moving_avg_20d'
    }
    assert set(df.columns) == expected_columns

def test_prepare_stock_data_returns_calculation(sample_stock_data):
    """Test that returns are calculated correctly"""
    df = prepare_stock_data(sample_stock_data)
    
    # Calculate expected returns manually
    expected_returns = sample_stock_data['close'].pct_change()
    pd.testing.assert_series_equal(
        df['returns'],
        expected_returns.dropna(),
        check_names=False
    )

def test_prepare_stock_data_moving_averages(sample_stock_data):
    """Test that moving averages are calculated correctly"""
    df = prepare_stock_data(sample_stock_data)
    
    # Calculate expected moving averages manually
    expected_ma5 = sample_stock_data['close'].rolling(window=5).mean()
    expected_ma20 = sample_stock_data['close'].rolling(window=20).mean()
    
    pd.testing.assert_series_equal(
        df['moving_avg_5d'],
        expected_ma5.dropna(),
        check_names=False
    )
    pd.testing.assert_series_equal(
        df['moving_avg_20d'],
        expected_ma20.dropna(),
        check_names=False
    )

def test_prepare_stock_data_no_nulls(sample_stock_data):
    """Test that the final DataFrame contains no null values"""
    df = prepare_stock_data(sample_stock_data)
    assert not df.isnull().any().any() 