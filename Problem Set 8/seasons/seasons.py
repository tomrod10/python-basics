import sys
import inflect
from datetime import date

p = inflect.engine()


def main():
    try:
        s = input("Date of Birth: ")
        date.fromisoformat(s)
    except ValueError:
        sys.exit()
    print(minutes_lived(s))


def minutes_lived(date_str):
    try:
        dob = date.fromisoformat(date_str)
        year = dob.year
        month = dob.month
        day = dob.day
    except ValueError:
        return "Invalid date"

    dt = date(year, month, day)
    today = date.today()
    diff = today - dt
    minutes = int(
        (diff.total_seconds() + 86_400) / 60
    )  # adding 86,400 (seconds in 1 day) because the diff is 364 days. Answers are based on 365 days

    msg = p.number_to_words(minutes, andword="") + " minutes"
    return msg.capitalize()


if __name__ == "__main__":
    main()
