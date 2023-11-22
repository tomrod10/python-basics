import sys
import random
from pyfiglet import Figlet

def main():
    print_ascii()

def print_ascii():
    figlet = Figlet()
    message = input('Input: ')
    try:
        font_flag = sys.argv[1]
        f = sys.argv[2]
        if font_flag in ('-f', '--font'):
            figlet.setFont(font=f)
            print(figlet.renderText(message))
        else:
            raise ValueError("Invalid font flag")
    except IndexError:
        fonts = figlet.getFonts()
        random_font = fonts[random.randrange(0, len(fonts))]
        figlet.setFont(font=random_font)
        print(figlet.renderText(message))

main()
