from lib.gratitudes import *

def test_gratitudes_with_one_name():
    grats = Gratitudes()
    grats.add("Bob")
    result = grats.format()
    assert result == "Be grateful for: Bob"

def test_gratitudes_with_more_names():
    grats = Gratitudes()
    grats.add("Bob")
    grats.add("Ana")
    grats.add("Sammy")
    result = grats.format()
    assert result == "Be grateful for: Bob, Ana, Sammy"