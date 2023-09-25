# File tests/test_diary.py

import pytest
from lib.diary import *

def test_diary_title():
    diary = DiaryEntry("My day", "Today I ate some bread.")
    assert diary.title == "My day"

def test_diary_contents():
    diary = DiaryEntry("My day", "Today I ate some bread.")
    assert diary.contents == "Today I ate some bread."

def test_diary_format():
    diary = DiaryEntry("My day", "Today I ate some bread.")
    assert diary.format() == "My day: Today I ate some bread."

def test_diary_count_words():
    diary = DiaryEntry("My day", "Today I ate some bread.")
    assert diary.count_words() == 5

def test_diary_reading_time():
    diary = DiaryEntry("Avatar: The Last Airbender",
                       """Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
                       Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, 
                       but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, 
                       an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
                       But I believe Aang can save the world.""") # 85 words
    assert diary.reading_time(5) == 17

def test_diary_reading_chunk():
    diary = DiaryEntry("Avatar: The Last Airbender",
                       """Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
                       Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, 
                       but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, 
                       an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
                       But I believe Aang can save the world.""") # 85 words
    assert diary.reading_chunk(5, 2) == "Water. Earth. Fire. Air. Long ago, the four nations lived"

def test_diary_reading_serveral_chunks():
    diary = DiaryEntry("Avatar: The Last Airbender",
                       """Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
                       Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, 
                       but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, 
                       an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
                       But I believe Aang can save the world.""") # 85 words
    diary.reading_chunk(5, 2)
    assert diary.reading_chunk(5, 2) == "together in harmony. Then, everything changed when the Fire Nation"

def test_diary_reading_chunk_restart():
    diary = DiaryEntry("Avatar: The Last Airbender",
                       """Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
                       Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, 
                       but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, 
                       an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
                       But I believe Aang can save the world.""") # 85 words
    diary.reading_chunk(5, 2)
    assert diary.reading_chunk(5, 2) == "Water. Earth. Fire. Air. Long ago, the four nations lived"