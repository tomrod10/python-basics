from watch import parse


def main():
    test_valid_html()
    test_invalid_html()


def test_valid_html():
    assert (
        parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )


def test_invalid_html():
    assert (parse("dog")) == None
    assert (
        parse('<iframe width="560" src="https://cs50.harvard.edu/python"></iframe>')
        == None
    )


main()
