# File: tests/test_grammar_stats.py

from lib.grammar_stats import *

def test_grammar_stats_check_correct():
    gstats = GrammarStats()
    assert gstats.check("Hello everynyan!") == True

def test_grammar_stats_check_incorrect1():
    gstats = GrammarStats()
    assert gstats.check("hello everynyan!") == False

def test_grammar_stats_check_incorrect2():
    gstats = GrammarStats()
    assert gstats.check("Hello everynyan") == False

def test_grammar_stats_check_incorrect3():
    gstats = GrammarStats()
    assert gstats.check("hello everynyan") == False

def test_grammar_stats_percentage_good():
    gstats = GrammarStats()
    gstats.check("Hello everynyan!")
    gstats.check("hello everynyan!")
    gstats.check("Hello everynyan")
    gstats.check("hello everynyan")
    assert gstats.percentage_good() == 25