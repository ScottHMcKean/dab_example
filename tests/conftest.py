import pytest
import pandas as pd
from datetime import datetime, timedelta

@pytest.fixture
def sample_dates():
    """Provide sample dates for testing"""
    return {
        'start': datetime(2023, 1, 1),
        'end': datetime(2023, 1, 31)
    } 