from lib.greet import *

def test_greet_with_Bob():
    result = greet("Bob")
    assert result == "Hello, Bob!"