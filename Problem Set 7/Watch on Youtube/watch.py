import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    try:
        url = re.search(r"(?:\bsrc=)(.+?\")", html).group(1)
        video_id = re.search(r"(?:embed/)(.+[a-zA-Z0-9])", url).group(1)
        return "https://youtu.be/" + video_id
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
