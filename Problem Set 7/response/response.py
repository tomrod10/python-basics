import validators


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(str):
    if validators.email(str) or len(str) == 0:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
