"""
implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file,
excluding comments and blank lines.

If the user does not specify exactly one command-line argument, or
if the specified file's name does not end in .py, or
if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods,
including lstrip and startswith.
# Note that open can raise a FileNotFoundError, per
docs.python.org/3/library/exceptions.html#FileNotFoundError.
"""


import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(count_lines(sys.argv[1]))


def count_lines(file):
    try:
        number_of_lines = 0
        with open(file, "r") as f:  # with문을 사용하면 파일을 열고 닫는 것을 자동적으로 처리가능.
            for line in f:     # 파일객체(f)는 기본적으로 for 문과 함께 사용하여 파일을 줄단위로 읽기 가능.
                if not (line.lstrip().startswith("#") or line.strip() == ""):
                    number_of_lines = number_of_lines + 1
            return number_of_lines
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()