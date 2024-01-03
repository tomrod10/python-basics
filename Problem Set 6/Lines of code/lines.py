import sys


def main():
    count_code_lines()


def count_code_lines():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")

        lines = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip() != "":
                    lines += 1
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
