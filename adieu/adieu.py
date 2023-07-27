import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ").strip().title()
        name_list.append(name)

    except EOFError:
        break

    else:
        continue

print("\nAdieu, adieu, to", p.join(name_list))