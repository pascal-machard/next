def main():

    print("exemple 08 list 02 sort")

    list_01 = [3, 2, 8, 5]

    print("Exemple de list : ", list_01)

    list_01.sort()
    print("List triée ", list_01)

    list_01.sort(reverse=True)
    print("List triée inverse", list_01)

if __name__ == "__main__":
    main()
