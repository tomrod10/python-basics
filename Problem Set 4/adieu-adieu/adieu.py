import inflect


def main():
    adieu()

def adieu():
    names = []
    p = inflect.engine()
    while True:
        try:
            msg = 'Adieu, adieu, to'
            name = input('Input: ')
            names.append(name)
            print(msg, p.join(names))
        except EOFError:
            print()
            break
main()
