import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + time + " to " + time + "$", s)
    if match:
        begin_time = conversion(match.group(1), match.group(2), match.group(3))
        finish_time = conversion(match.group(4), match.group(5), match.group(6))
        return f"{begin_time} to {finish_time}"
    else:
        raise ValueError


def conversion(HH, MM, XM):
    if HH == "12":
        if XM == "AM":
            HH = "00"
        else:
            HH = "12"
    else:
        if XM == "AM":
            HH = f"{int(HH):02}"
        else:
            HH = f"{int(HH)+12}"
    if MM == None:
        MM = "00"
    else:
        MM = f"{int(MM):02}"
    return f"{HH}:{MM}"


if __name__ == "__main__":
    main()