from fractions import Fraction


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            numerator = int(x)
            denominator = int(y)
            f = numerator / denominator
            if f <= 1:
                percentage = int(100 * f)
                return percentage
        except (ZeroDivisionError, ValueError):
            raise
        else:
            fraction = input("Fraction: ")
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
