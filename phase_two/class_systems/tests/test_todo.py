# File: test_todo.py

from lib.todo import *

def test_todo():
    todo1 = Todo("play amogus")
    todo2 = Todo("play minecraft parkour")
    todo3 = Todo("play subway surfers")
    todolist = TodoList()
    todolist.add(todo1)
    assert todolist.incomplete() == ["play amogus"]
    todo1.mark_complete()
    assert todolist.complete() == ["play amogus"]
    todolist.add(todo2)
    todolist.add(todo3)
    todolist.give_up()
    assert todolist.complete() == ["play amogus", "play minecraft parkour", "play subway surfers"]