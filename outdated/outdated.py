import re

month = [
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
    "December"
]

def main():
    formattedDate = validate_date()
    print(formattedDate)

def validate_date():
    t = re.split(r"-|/|, | ", input('Date: ').strip())

    while True:
        try:
            # Month DD, YYYY -> YYYY-MM-DD
            if t[0].isalpha() and t[0] in month:
                dd = t[1].zfill(2)
                mm = month.index(t[0]) + 1
                yyyy = t[2]

                if int(dd) > 31:
                    t = re.split(r"-|/|, | ", input('Date: ').strip())

                formattedDate = f"{yyyy}-{mm:02}-{dd:02}"
                return formattedDate

            # MM/DD/YYYY -> YYYY-MM-DD
            elif t[0].isalnum() and len(t[0]) == 1 or 2:
                dd = t[1].zfill(2)
                mm = t[0].zfill(2)
                yyyy = t[2]

                if int(dd) > 31 or int(mm) > 12:
                    t = re.split(r"-|/|, | ", input('Date: ').strip())

                formattedDate = f"{yyyy}-{mm:02}-{dd:02}"
                return formattedDate

        except ValueError:
            t = re.split(r"-|/|, | ", input('Date: ').strip())

        else:
            continue

main()