import sys
import csv

from tabulate import tabulate


def main():
    tabulate_pizza_menu()


def tabulate_pizza_menu():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a csv file")

        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for line in reader:
                menu.append(line)

        print(tabulate(menu, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
