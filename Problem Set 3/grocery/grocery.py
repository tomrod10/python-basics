def main():
    grocery_list()


def grocery_list():
    items = {}
    while True:
        try:
            item = input()
            if item not in items:
                items[item] = 1
            else:
                items[item] = items[item] + 1
        except EOFError:
            sorted_items = sorted(items.keys())
            for item in sorted_items:
                print(f"{items[item]} {item.upper()}")
            break


main()
