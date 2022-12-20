import re

def main():

    print("exemple 03 input sqr 06")

    value=""

    while re.match('^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$', value) is None:
        print("Saisi d'une valeur :")
        value = input()

    print("valeur saisie = ", value)
    value_int = float(value)
    print("Valeur au carré = ", value_int * value_int)


if __name__ == "__main__":
    main()
