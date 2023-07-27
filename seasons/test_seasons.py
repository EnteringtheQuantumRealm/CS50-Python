from seasons import day_to_min

def test_date():
    assert day_to_min(730) == "One million, fifty-one thousand, two hundred minutes"
    assert day_to_min(365) == "Five hundred twenty-five thousand, six hundred minutes"