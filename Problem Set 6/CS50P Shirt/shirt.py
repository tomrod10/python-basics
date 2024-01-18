import sys
import os
from PIL import Image, ImageOps


def main():
    overlay_shirt()


def overlay_shirt():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        try:
            muppet = Image.open(sys.argv[1], mode="r", formats=None)
        except FileNotFoundError:
            sys.exit("File does not exist")

        extensions = [".png", ".jpg", ".jpeg"]
        extension1 = os.path.splitext(sys.argv[1])[1]
        extension2 = os.path.splitext(sys.argv[2])[1]

        if extension1 == extension2 and extension1 in extensions:
            shirt = Image.open("./shirt/shirt.png", mode="r", formats=None)
            shirt_size = shirt.size
            muppet = ImageOps.fit(muppet, shirt_size)

            muppet.paste(shirt, shirt)
            muppet.save(sys.argv[2])
            return
        elif extension1 != extension2:
            sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid inputs")


main()
