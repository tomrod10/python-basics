import re


def main():
    print(parse(input("HTML: ")))


# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
def parse(html):
    src_attr = re.search(r"(\bsrc=)(.+\")", html)
    # print(src_attr)
    url = src_attr.group(2)
    # From: ---> "https://www.youtube.com/embed/xvFZjo5PgG0"
    # To: ---> https://youtu.be/xvFZjo5PgG0

    # grab to the right of embed/{video_id}
    video_id = re.search(r"(?:embed/)(.+[a-zA-Z0-9])", url).group(1)
    shortened_url = "https://youtu.be/" + video_id
    return shortened_url


if __name__ == "__main__":
    main()
