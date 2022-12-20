def main():

    print("exemple 03 input sqr 04")

    print("Saisi d'une valeur :")
    value = input()

    print("valeur saisie = ", value)

    if value.isnumeric():
        value_int = int(value)
        print("Valeur au carré = ", value_int * value_int)
    else:
        print("La valeur n'est pas un entier")


if __name__ == "__main__":
    main()
