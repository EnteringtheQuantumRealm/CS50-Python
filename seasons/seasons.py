from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():
    try:
        bday = input("Date of Birth: ")
        subtract = operator.__sub__(date.today(), date.fromisoformat(bday))
        print(day_to_min(subtract.days))
    except ValueError:
        sys.exit("Invalid date")


def day_to_min(d):
    minutes = d * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()