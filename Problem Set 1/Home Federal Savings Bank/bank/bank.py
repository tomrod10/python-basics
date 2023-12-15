def main():
    greet_wisely()


def greet_wisely():
    greeting = (input("Greeting: ")).strip().lower()

    if "hello" in greeting:
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
