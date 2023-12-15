import pytest
from twttr_2 import shorten


def main():
    test_default()
    test_numbers()
    test_objects()


def test_default():
    assert shorten("Twitter") == "Twttr"
    assert shorten("hello") == "hll"
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_numbers():
    with pytest.raises(TypeError):
        shorten(1)
        shorten(0)


def test_objects():
    val_1 = shorten([])
    val_2 = shorten({})
    assert val_1 != isinstance(val_1, str)
    assert val_2 != isinstance(val_2, str)


if __name__ == "__main__":
    main()
