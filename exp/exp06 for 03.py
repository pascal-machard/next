def main():

    print("exemple 05 for 02")

    print("Saisi d'une valeur entiere :")
    value = input()

    value_int = int(value)

    for i in range(0, value_int, 2):
        print("coucou ", i)


if __name__ == "__main__":
    main()
