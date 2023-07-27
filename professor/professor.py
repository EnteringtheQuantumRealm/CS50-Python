import random


def main():
    eqnum = 10
    score = 0
    chances = 3
    level = get_level()
    while eqnum != 0:
        if chances == 3:
            x, y = generate_integer(level)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            right_answer = x + y
            if user_answer == right_answer:
                eqnum = eqnum - 1
                score = score + 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {right_answer}"))
            chances = 3
            eqnum = eqnum - 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()