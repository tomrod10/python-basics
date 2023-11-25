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
        except EOFError:
            print(msg, p.join(names))
            break
main()
