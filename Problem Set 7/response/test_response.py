from response import validate_email


def main():
    test_validate_email1()


def test_validate_email1():
    assert validate_email("tom@harvard.edu") == "Valid"
    assert validate_email("example@gmail.com") == "Valid"
    assert validate_email("tom@@harvard.edu") == "Invalid"
    assert validate_email("tom@harvard..edu") == "Invalid"


main()
