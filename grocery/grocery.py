list = {}

while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        else:
            if item in list:
                list[item] += 1
            else:
                list[item] = 1

for k, v in sorted(list.items()):
                print(v, k)