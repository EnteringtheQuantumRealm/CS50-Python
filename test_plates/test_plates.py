import plates
from plates import is_valid

def test_begintwoletters():
    assert is_valid("CS50") == True
    assert is_valid("50") == False
    assert is_valid("500CS") == False

def test_numnzero():
    assert is_valid("CS05") == False
    assert is_valid("CS05A") == False
    assert is_valid("ABC110") == True

def test_length():
    assert is_valid("ABCHHH1") == False
    assert is_valid("MONEYBAG") == False

def test_punct():
    assert is_valid("ABC0!!") == False