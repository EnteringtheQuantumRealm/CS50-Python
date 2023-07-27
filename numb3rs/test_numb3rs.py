from numb3rs import validate


def test_validate():
    assert validate("125.1.0.1") == True
    assert validate("254.255.254.255") == True
    assert validate("522.53.532.0") == False
    assert validate("1.2.3.1000") == False
    assert validate("butter") == False
    assert validate("1.0.0.1") == True
    assert validate("11.22.100.88") == True
    assert validate("200.300.400.500") == False
    assert validate("250.225.225.225") == True