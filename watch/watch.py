import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{link.group(2)}"
    elif link := re.search(r"<iframe width=\"([0-9]+)\" height=\"([0-9]+)\" src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\" title=\"([a-zA-Z0-9 ]+)\" frameborder=\"([0-9]+)\" allow=\"([a-zA-Z0-9\;\- ]+)\" allowfullscreen></iframe>", s):
        return f"https://youtu.be/{link.group(4)}"
    else:
        return None

if __name__ == "__main__":
    main()