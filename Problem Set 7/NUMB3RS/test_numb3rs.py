from numb3rs import validate


def main():
    test_ip_true()
    test_ip_false()


def test_ip_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.24.5.10") == True
    assert validate("10.20.30.40") == True


def test_ip_false():
    assert validate("cat") == False
    assert validate("1.275.275.275") == False
    assert validate("275.123.123.123") == False
    assert validate("275.275.275.275") == False


main()
