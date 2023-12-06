def main():
    format_to_ISO()


def format_to_ISO():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        try:
            date = input("Date: ").replace("/", " ").replace(",", "")
            month, day, year = date.split(" ")

            if (int(month) >= 1 and int(month) <= 12) and (
                int(day) >= 1 and int(day) <= 31
            ):
                break
        except:
            try:
                if month in months:
                    month = str(months.index(month) + 1)
                if (int(month) >= 1 and int(month) <= 12) and (
                    int(day) >= 1 and int(day) <= 31
                ):
                    break
            except:
                print()
                pass
    print(f"{year}-{int(month):02}-{int(day):02}")


main()
