def main():
    greeting = []
    w = (input("Greeting: ").lower().strip())
    greeting.append(w)
    print(f"${value(greeting)}")


def value(greet):
    if greet[0][0:5] == "hello":
        return 0
    elif greet[0][0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

