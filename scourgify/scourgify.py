"""
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input,
whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order,
first, last, and house.

Converts that input to that output, splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or
if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clear_charm(sys.argv[1], sys.argv[2])


def clear_charm(input, output):
    try:
        with open(input) as input:
            rows = csv.DictReader(input)
            with open(output, "w") as output:
                    fieldnames = ["first", "last", "house"]
                    writer = csv.DictWriter(output, fieldnames = fieldnames)
                    writer.writeheader()
                    for student in rows:
                            last, first = student["name"].strip().split(", ")
                            house = student["house"].strip()
                            writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
     main()



