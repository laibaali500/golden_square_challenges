import pytest
from lib.old_diary_functions import *

def test_make_snippet_long():
    result = make_snippet("Hello, everynyan! How are you? Fine thank you.")
    assert result == "Hello, everynyan! How are you? ..."

def test_make_snippet_short():
    result = make_snippet("Hi there!")
    assert result == "Hi there!"

def test_count_words():
    result = count_words("I like chicken nuggets!")
    assert result == 4