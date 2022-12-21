def main():

    print("exemple 08 list 06 add")

    list_01 = [3, 2, 8]

    print("Exemple de list : ", list_01)

    list_01.extend([11,5])
    print("List avec l'extension du tableau [11,5] :", list_01)

    list_01.insert(2,13)
    print("List insertion en 2 de 13", list_01)

    list_01 = list_01 + [99,-2]
    print("List add 99 et -2", list_01)

    list_01 += [33]
    print("List add 33", list_01)


if __name__ == "__main__":
    main()
