def main():

    print("exemple 03 input sqr 03")

    print("Saisi d'une valeur :")
    value = input()

    print("valeur saisie = ", value)

    if value.isnumeric():
        value_int = int(value)
        print("valeur au carré = ", value_int * value_int)


if __name__ == "__main__":
    main()
