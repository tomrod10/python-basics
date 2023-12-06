import sys
import random
from pyfiglet import Figlet


def main():
    print_ascii()


def print_ascii():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
    elif (
        len(sys.argv) == 3
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and (sys.argv[2] in fonts)
    ):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    message = input("Input: ")

    print("Output:")
    print(figlet.renderText(message))


main()
