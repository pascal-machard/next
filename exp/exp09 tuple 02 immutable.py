import numpy as np

def main():

    print("exemple 09 tuple 02 immutable")

    list_a = ["blue", "red", "green", "purple"]

    print("list_a: ", list_a)
    print("Addresse de list_a: ", hex(id(list_a)))

    list_a.append("yellow")
    print("Ajout de 'yellow' dans la liste")
    print("list_a: ", list_a)
    print("Address de list_a: ", hex(id(list_a)))
    print("L'adresse de la liste n'a pas changé.")

    print("--------------------------------------------")

    tuple_a = ("blue", "red", "green", "purple")
    print("tuple_a: ", tuple_a)
    print("Addresse de tuple_a: ", hex(id(tuple_a)))

    tuple_a = tuple_a + ("yellow",)
    print("Ajout de 'yellow' dans le tuple")
    print("tuple_a: ", tuple_a)
    print("Address de tuple_a: ", hex(id(tuple_a)))
    print("L'adresse du tuple a changé.")

if __name__ == "__main__":
    main()
