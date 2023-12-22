from fractions import Fraction


def main():
    percentage = get_fuel_percentage()
    print(percentage)


def get_fuel_percentage():
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
    percentage = int(fraction * 100)
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


main()
