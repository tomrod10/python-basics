def main():
    shorten()


def shorten():
    user_input = input("Input: ")
    for char in user_input:
        if char in ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]:
            user_input = user_input.replace(char, "")
    print(user_input)


if __name__ == "__main__":
    main()
