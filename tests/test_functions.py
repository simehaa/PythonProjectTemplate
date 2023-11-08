from datetime import datetime

from src.functions import get_todays_date


def test_get_todays_date():
    assert (
        get_todays_date() == datetime.now().date()
    ), "get_todays_date() should return today's date"
