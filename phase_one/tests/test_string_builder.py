from lib.string_builder import *

def test_string_builder_add_a_string():
    string_builder = StringBuilder()
    string_builder.add("abcde")
    result = string_builder.output()
    assert result == "abcde"

def test_string_builder_add_strings():
    string_builder = StringBuilder()
    string_builder.add("abcde")
    string_builder.add("fghij")
    result = string_builder.output()
    assert result == "abcdefghij"

def test_string_builder_check_size():
    string_builder = StringBuilder()
    string_builder.add("abcdefghij")
    result = string_builder.size()
    assert result == 10