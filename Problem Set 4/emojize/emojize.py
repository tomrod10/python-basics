import emoji


def main():
    turn_to_emoji()


def turn_to_emoji():
    user_input = input("Input: ")
    emojized = emoji.emojize(user_input, language="alias")
    print("Output:", emojized)


main()
