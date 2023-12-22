import pytest

from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("1/100") == 1

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ZeroDivisionError):
        convert("0/0")
        convert("3/0")
        convert("5/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

    with pytest.raises(TypeError):
        gauge("3")
        gauge({})


main()
