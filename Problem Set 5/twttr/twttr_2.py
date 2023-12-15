def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(string):
    for char in string:
        if char in ["a", "i", "e", "o", "u", "A", "I", "E", "O", "U"]:
            string = string.replace(char, "")
    return string


if __name__ == "__main__":
    main()
