# File: tests/test_design_recipe3.py

from lib.design_recipe3 import *

def test_isToDo_True():
    result = isToDo("Check for bugs #TODO")
    assert result == True

def test_isToDo_False1():
    result = isToDo("Check for bugs")
    assert result == False

def test_isToDo_False2():
    result = isToDo("Check for bugs #todo")
    assert result == False