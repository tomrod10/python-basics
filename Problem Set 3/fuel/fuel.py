from fractions import Fraction


def main():
    percentage = convert()
    gauge(percentage)


def convert():
    while True:
        fuel = input("Fraction: ")
        try:
            x, y = fuel.split("/")
            numerator = int(x)
            denominator = int(y)
            fraction = numerator / denominator
            if fraction <= 1:
                break
        except (ZeroDivisionError, ValueError):
            pass
    return int(fraction * 100)


def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


main()
