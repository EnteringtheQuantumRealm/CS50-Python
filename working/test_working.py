import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 6 PM") == "09:00 to 18:00"
    assert convert("9:00 AM to 6:00 PM") == "09:00 to 18:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 7:50 AM") == "22:30 to 07:50"

def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 19:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 35:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 15:100 PM")