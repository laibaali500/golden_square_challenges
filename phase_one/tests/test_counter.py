from lib.counter import *

def test_counter_to_one():
    counter = Counter()
    counter.add(1)
    result = counter.report()
    assert result == "Counted to 1 so far."


def test_counter_to_ten():
    counter = Counter()
    counter.add(1)
    counter.add(9)
    result = counter.report()
    assert result == "Counted to 10 so far."