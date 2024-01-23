import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(
        r"^(25[0-5]|2[0-4]4[0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4]4[0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4]4[0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4]4[0-9]|[0-1]?[0-9][0-9]?)$",
        ip,
    )
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
