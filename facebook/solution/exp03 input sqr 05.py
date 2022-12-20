def main():

    print("exemple 03 input sqr 05")

    value=""

    while not value.isnumeric():
        print("Saisi d'une valeur :")
        value = input()

    print("valeur saisie = ", value)
    value_int = int(value)
    print("Valeur au carré = ", value_int * value_int)


if __name__ == "__main__":
    main()
