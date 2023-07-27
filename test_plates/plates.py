def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check for length (2-6)
    if len(s)>6 or len(s)<2:
        return False

    # check alphanumeric (No periods, spaces, or punctuation marks are allowed)
    elif not s.isalnum():
        return False

    # check first 2 elements are alphabets
    elif not s[0:2].isalpha():
        return False

    # if all elements are not alphabets, submit50 cs50/problems/2022/python/platesfind first number is not "0" and check if there is no alphabet after first num
    for i in range(len(s)):
        if s[i::].isalpha():
            return True
        elif s[i].isalpha():
            continue
        elif s[i].isdigit():
            if int(s[i]) == 0:
                return False
            elif s[i+1::].isdigit() == False:
                return False
            else:
                return True    # all conditions satisfied!


if __name__ == "__main__":
    main()