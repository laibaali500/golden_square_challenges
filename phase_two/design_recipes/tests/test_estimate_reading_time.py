# File: tests/test_estimate_reading_time.py
from lib.estimate_reading_time import *

def test_estimate_reading_time_200_words():
    result = estimate_reading_time(200)
    assert result == 1

def test_estimate_reading_time_450_words():
    result = estimate_reading_time(450)
    assert result == 2.25