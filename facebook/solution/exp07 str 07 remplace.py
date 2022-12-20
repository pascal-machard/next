def main():

    print("exemple 07 str 07")

    print("Saisi de la chaine de caractère :")
    buffer = input()

    print("Remplace :")
    buffer_remplace = input()

    print("Remplacer par :")
    buffer_remplace_by = input()

    print("La chaine en majuscule :", buffer.replace(buffer_remplace,buffer_remplace_by))


if __name__ == "__main__":
    main()
