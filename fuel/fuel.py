from fractions import Fraction

def main():
    get_fuel_percentage()

def get_fuel_percentage():
    while True:
        fuel = input("Fraction: ")
        try:
            x, y = fuel.split('/')
            numerator = int(x)
            denominator = int(y)
            fraction = numerator / denominator
            if (fraction <= 1):
                break
        except (ZeroDivisionError, ValueError):
            pass
    percentage = int(fraction * 100)
    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{percentage}%')

main()
