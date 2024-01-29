from um import count


def main():
    test_count1()
    test_count2()
    test_count3()


def test_count1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count(" um ") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album") == 1


def test_count2():
    assert count("UM") == 1
    assert count("u m") == 0
    assert count("yum") == 0
    assert count("u um") == 1


def test_count3():
    assert count(" um") == 1
    assert count("um ") == 1
    assert count("um. um") == 2
    assert count("ummmm") == 0
    assert count("uuuuum") == 0


main()
