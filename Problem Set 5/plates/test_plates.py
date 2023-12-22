import pytest
from plates import is_valid


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert is_valid("Hello") == True
    assert is_valid("CS50") == True
    assert is_valid("CS5012") == True
    assert is_valid("ThisIsTooLong") == False
    assert is_valid("Hello ") == False
    assert is_valid("Hello,") == False
    assert is_valid("ABC5D") == False
    assert is_valid("CS054") == False


def test_2():
    assert is_valid("C") == False
    assert is_valid("24") == False
    assert is_valid(",./%") == False
    assert is_valid("CS  50") == False


def test_3():
    with pytest.raises(TypeError):
        assert is_valid(54)
        assert is_valid({})


main()
