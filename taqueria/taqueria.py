def main():
    taqueria_cal()

def taqueria_cal():
    total = 0
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while True:
        try:
            item = input('Item: ').lower().title()
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
            
        except EOFError:
            break

        except KeyError:
            break

if __name__ == "__main__":
    main()