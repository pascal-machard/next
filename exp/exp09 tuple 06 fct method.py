import numpy as np

def main():

    print("exemple 09 tuple 06 fct method")

    tuple_a = (99, 12, -75, 5, 12)
    print("tuple_a : ", tuple_a)

    print("----------------------------------")

    print("len(tuple_a) : ", len(tuple_a))
    print("max(tuple_a) : ", max(tuple_a))
    print("min(tuple_a) : ", min(tuple_a))
    print("sum(tuple_a) : ", sum(tuple_a))

    print("----------------------------------")

    list_b = ["red", "green", "blue"]
    print("list_b :", list_b)
    tuple_b = tuple(list_b)
    print("tuple_b : ", tuple_b)

    print("----------------------------------")

    print("tuple_a :", tuple_a)
    print("tuple_a.count(5)",tuple_a.count(5))
    print("tuple_a.count(12)", tuple_a.count(12))
    print("tuple_a.count(7)", tuple_a.count(7))

    print("tuple_a.index(5)",tuple_a.index(5))
    print("tuple_a.index(12)", tuple_a.index(12))
    print("tuple_a.index(12,3)", tuple_a.index(12,3))

if __name__ == "__main__":
    main()
