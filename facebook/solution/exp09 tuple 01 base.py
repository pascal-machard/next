import numpy as np

def main():

    print("exemple 09 tuple 01 base")

    # Tuple de str
    tuple_a = ("blue", "red", "green", "purple", "yellow")
    # Tuple de données mixte
    tuple_b = ("blue", 123, "red", -99)

    print("Tuple vide :", ())
    print(" --------------------------- ")
    print("Tuple une valeur :", (33,))
    print(" --------------------------- ")
    print("Tuple color :", tuple_a)
    print(" --------------------------- ")
    print("Other Tuple : ", tuple_b)


if __name__ == "__main__":
    main()
