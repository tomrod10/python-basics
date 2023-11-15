# ask for fraction input in the form of X/Y
# anything entered in the wrong format reprompts user to enter a fraction
# return fraction in percentage
# if percentage is <= 1% return E for empty
# if percentage is >= 99% return F for full

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