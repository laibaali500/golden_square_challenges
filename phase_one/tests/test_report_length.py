from lib.report_length import *

def test_report_length_with_five_characters():
    result = report_length("Hello")
    assert result == "This string was 5 characters long."

def test_report_length_with_sixteen_characters():
    result = report_length("Hi! How are you?")
    assert result == "This string was 16 characters long."