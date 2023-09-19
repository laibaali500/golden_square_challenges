# File: tests/test_grammar_check.py

from lib.grammar_check import *

def test_grammar_check_correct():
    result = grammar_check("Hello everynyan!")
    assert result == True

def test_grammar_check_partially_correct1():
    result = grammar_check("hello guys!")
    assert result == False

def test_grammar_check_partially_correct2():
    result = grammar_check("Hello guys")
    assert result == False

def test_grammar_check_incorrect():
    result = grammar_check("hey guys")
    assert result == False