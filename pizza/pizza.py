"""
In a file called pizza.py, implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio's format, and
outputs a table formatted as ASCII art using tabulate,
a package on PyPI at [pypi.org/project/tabulate].
Format the table using the library's [grid format].

If the user does not specify exactly one command-line argument, or
if the specified file’s name does not end in .csv, or
if the specified file does not exist,
the program should instead exit via sys.exit.

# Recall that the csv module comes with quite a few methods, per [docs.python.org/3/library/csv.html],
among which are reader, per [docs.python.org/3/library/csv.html#csv.reader],
and DictReader, per [docs.python.org/3/library/csv.html#csv.DictReader].
# can raise a FileNotFoundError, per [docs.python.org/3/library/exceptions.html#FileNotFoundError].
# tabulate package comes with just one function, per [pypi.org/project/tabulate].
"""

import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            print(tabulize(sys.argv[1]))

def tabulize(file):
    try:
        with open(file) as f:
            rows = csv.reader(f)  # csv.reader로 헹데이터를 리스트로 반환
            table = tabulate(rows, headers="firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()