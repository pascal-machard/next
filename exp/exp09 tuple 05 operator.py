import numpy as np

def main():

    print("exemple 09 tuple 05 operator")

    tuple_a = ("blue", "red", "green", "purple")
    print("tuple_a : ", tuple_a)

    tuple_b = (1, 33)
    print("tuple_b : ", tuple_a)

    tuple_c = tuple_a + tuple_b
    print("tuple_a + tuple_b: ", tuple_c)

    print("----------------------------------")

    tuple_d = tuple_b * 3
    print("tuple_b * 3 : ", tuple_d)

    print("----------------------------------")

    has_red = "red" in tuple_a
    print("tuple_a has red color : ", has_red)

    has_no_yellow = "yellow" not in tuple_a
    print("tuple_a has no yellow color : ", has_no_yellow)

if __name__ == "__main__":
    main()
