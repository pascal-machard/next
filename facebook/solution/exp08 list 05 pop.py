def main():

    print("exemple 08 list 05 pop")

    list_01 = [3, 2, 8, 5]

    print("Exemple de list : ", list_01)

    list_01.pop()
    print("List sans le dernier élément :", list_01)


    list_01.pop(1)
    print("List sans l'avant dernier élément :", list_01)

if __name__ == "__main__":
    main()
