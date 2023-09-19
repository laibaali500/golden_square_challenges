import pytest
from lib.present import *

def test_present_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present_already_contents():
    present = Present()
    present.wrap("Bicycle")
    with pytest.raises(Exception) as e:
        present.wrap("LEGO")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."