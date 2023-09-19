import pytest
from lib.password_checker import *

def test_password_checker_works():
    checker = PasswordChecker()
    result = checker.check("12345678")
    assert result == True

def test_password_checker_error():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        result = checker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."