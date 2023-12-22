import pytest

from fuel import get_fuel_percentage


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert get_fuel_percentage("1/4") == "25%"
    assert get_fuel_percentage("1/2") == "50%"
    assert get_fuel_percentage("3/4") == "75%"
    assert get_fuel_percentage("1/1") == "100%"


def test_2():
    with pytest.raises(ValueError):
        get_fuel_percentage(1 / 2)
        get_fuel_percentage(3 / 4)


def test_3():
    with pytest.raises(ZeroDivisionError):
        get_fuel_percentage("3/0")
        get_fuel_percentage("5/0")


main()
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError

# If Y is 0, then convert should raise a ZeroDivisionError.
