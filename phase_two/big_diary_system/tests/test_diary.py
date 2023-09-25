# File: tests/diary.py

from lib.diary import *

def test_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry("Best Video Games", """League of Legends, Valorant, OSU, Minecraft""", "07500 000000")
    entry2 = DiaryEntry("Your Mum", """gfhdjgkhfdjkghdfkjvnbfdjkbgdkjfgjdgbjs""", "07999 999999")
    entry3 = DiaryEntry("Avatar Aang", """Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
                       Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, 
                       but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, 
                       an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
                       But I believe Aang can save the world.""", "07000 000000") #85 words
    diary.write(entry1)
    diary.write(entry2)
    diary.write(entry3)
    bestEntry = diary.selectEntry(2,5) #10 words
    assert bestEntry == entry1.contents


def test_diary_contacts():
    diary = Diary()
    entry1 = DiaryEntry("Best Video Games", """League of Legends, Valorant, OSU, Minecraft""", "07500 000000")
    entry2 = DiaryEntry("Your Mum", """gfhdjgkhfdjkghdfkjvnbfdjkbgdkjfgjdgbjs""", "07999 999999")
    entry3 = DiaryEntry("Avatar Aang", """Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. 
                       Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, 
                       but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, 
                       an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. 
                       But I believe Aang can save the world.""", "07000 000000") #85 words
    diary.write(entry1)
    diary.write(entry2)
    diary.write(entry3)
    contacts = diary.listContacts()
    assert contacts == ["Best Video Games : 07500 000000", "Your Mum : 07999 999999", "Avatar Aang : 07000 000000"]

def test_todolist():
    todo1 = Todo("play amogus")
    todo2 = Todo("play minecraft parkour")
    todo3 = Todo("play subway surfers")
    todolist = TodoList()
    todolist.add_todo(todo1)
    assert todolist.incompleted() == ["play amogus"]
    todo1.markComplete()
    assert todolist.completed() == ["play amogus"]