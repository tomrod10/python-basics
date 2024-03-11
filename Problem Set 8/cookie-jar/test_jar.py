import pytest
from jar import Jar

jar = Jar()

def test_init():
    assert str(jar) == ""
    assert jar.capacity == 12
    assert jar.size == 0

def test_deposit():
    assert jar.size == 0
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"
    assert jar.size == 3

def test_withdraw():
    jar.withdraw(2)
    assert str(jar) == "🍪"
    assert jar.size == 1
    jar.withdraw(1)
    assert str(jar) == ""
    assert jar.size == 0

def test_exceptions():
    with pytest.raises(ValueError):
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar.withdraw(20)
    with pytest.raises(ValueError):
        Jar(-3)

