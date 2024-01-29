import re


def main():
    print(count(input("String: ")))


def count(str):
    matches = re.findall(r"(?: |\b)um(?:\b| )", str, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
