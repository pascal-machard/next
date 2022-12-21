def main():

    print("exemple 04 if")

    print("Saisi d'une valeur :")
    value = input()

    if value == "polo":
        print("Oui c'est bien polo")
    elif value == "toto":
        print("Oui c'est bien l'ami de polo, c'est toto")
    else:
        print("valeur saisie = ", value)

    print("fin du test")

if __name__ == "__main__":
    main()
