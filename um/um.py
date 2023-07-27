import re


def main():
    print(count(input("Input: ")))


def count(s):
    format = "(^|[^a-zA-Z0-9])um($|[^a-zA-Z0-9])"
    match = re.findall(format, s, re.IGNORECASE)
    if match:
        return(len(match))


if __name__ == "__main__":
    main()