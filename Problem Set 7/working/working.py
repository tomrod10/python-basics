import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(
        r"([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)",
        s,
    )

    if matches:
        hour1, minute1, meridien1, hour2, minute2, meridien2 = matches.groups()

        hour1 = int(hour1)
        if meridien1 == "PM" and hour1 != 12:
            hour1 += 12
        elif meridien1 == "AM" and hour1 == 12:
            hour1 -= 12
        hour1 = "0" + str(hour1) if hour1 < 10 else hour1

        hour2 = int(hour2)
        if meridien2 == "PM" and hour2 != 12:
            hour2 += 12
        elif meridien2 == "AM" and hour2 == 12:
            hour2 -= 12
        hour2 = "0" + str(hour2) if hour2 < 10 else hour2

        minute1 = int(minute1) if minute1 != None else 0
        if minute1 >= 60:
            raise ValueError
        elif minute1 < 10:
            minute1 = "0" + str(minute1)

        minute2 = int(minute2) if minute2 != None else 0
        if minute2 >= 60:
            raise ValueError
        elif minute2 < 10:
            minute2 = "0" + str(minute2)

        return f"{hour1}:{minute1} to {hour2}:{minute2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
