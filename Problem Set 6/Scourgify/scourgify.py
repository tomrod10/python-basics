import sys
import csv


def main():
    scourgify()


def scourgify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1]) as file1:
                reader = csv.DictReader(file1)
                with open(sys.argv[2], "w") as file2:
                    writer = csv.DictWriter(
                        file2, fieldnames=["first", "last", "house"]
                    )
                    writer.writeheader()

                    for row in reader:
                        row["first"] = row.pop("name")
                        last_name, first_name = row["first"].split(", ")
                        row["first"] = first_name
                        row["last"] = last_name
                        writer.writerow(row)
        else:
            sys.exit("Not a csv file")

    except FileNotFoundError:
        sys.exit("File does not exist")


main()
