def main():
    greeting = input("Greeting: ")
    print(f"${greet_wisely(greeting)}")


def greet_wisely(greeting):
    greeting = greeting.strip().lower()

    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
