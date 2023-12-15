import pytest
from bank_2 import greet_wisely


def main():
    test_default()
    test_casings()


def test_default():
    assert greet_wisely("Hello") == 0
    assert greet_wisely("Hello, Newman") == 0
    assert greet_wisely("   hi  ") == 20
    assert greet_wisely("How you doing?") == 20
    assert greet_wisely("What's happening?") == 100


def test_casings():
    assert greet_wisely("HELLO") == 0
    assert greet_wisely("hello, newman") == 0
    assert greet_wisely("HoW yOu DoInG?") == 20
    assert greet_wisely("What's happening?") == 100


if __name__ == "__main__":
    main()
