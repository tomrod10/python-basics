from seasons import minutes_lived


def main():
    test1()
    test2()


def test1():
    assert (
        minutes_lived("2023-01-31")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        minutes_lived("2022-01-31")
        == "One million, fifty-one thousand, two hundred minutes"
    )
    assert (
        minutes_lived("1999-01-01")
        == "Thirteen million, one hundred ninety-one thousand, eight hundred forty minutes"
    )


def test2():
    assert minutes_lived("cat") == "Invalid date"
    assert minutes_lived("2022-31-50") == "Invalid date"
    assert minutes_lived("1-12-2023") == "Invalid date"
    assert minutes_lived("2022-1-31") == "Invalid date"


main()
