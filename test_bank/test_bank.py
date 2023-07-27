import bank
from bank import value

def test_greet():
    assert value("hello, CS50") == 0
    assert value("What's up!") == 100
    assert value("Hi, there!") == 20
    assert value("HI, THERE!") == 20