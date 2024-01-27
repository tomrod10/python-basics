import pytest
from working import convert


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_2():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("10 AM to 12:09 AM") == "10:00 to 00:09"
    assert convert("10 AM to 12:11 AM") == "10:00 to 00:11"


def test_3():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:70 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM to 5")


if __name__ == "__main__":
    main()
