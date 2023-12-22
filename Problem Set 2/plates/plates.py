def main():
    plate = is_valid(input("Plate: "))
    if plate:
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    if len(p) < 2 or len(p) > 6 or p[0:2].isalpha() == False or p.isalnum() == False:
        return False

    # check that no digits are in the middle of the plate
    for i in range(len(p) - 1):
        if p[i].isdigit() and p[i + 1].isalpha():
            return False

    # check that first digit is not a zero 0
    for i in p:
        if i.isdigit():
            return i != "0"
    else:
        return True


if __name__ == "__main__":
    main()
