import re


def main():
    print(parse(input("HTML: ")))


# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
def parse(html):
    url = re.search(r"(?:\bsrc=)(.+\")", html).group(1)
    video_id = re.search(r"(?:embed/)(.+[a-zA-Z0-9])", url).group(1)
    shortened_url = "https://youtu.be/" + video_id
    return shortened_url


if __name__ == "__main__":
    main()
