def main():

    print("exemple 07 str 01")

    print("Saisi d'une chaine de caractères (>5 caractère):")
    buffer = input()

    print("Premier caractère : ", buffer[0])
    print("Premier caractère : ", buffer[0:1])

    print("Dernier caractère : ", buffer[-1])

    print("5 premiers caractères", buffer[0:5])
    print("5 derniers caractères", buffer[-5:])


if __name__ == "__main__":
    main()
