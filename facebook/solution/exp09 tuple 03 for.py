import numpy as np

def main():

    print("exemple 09 tuple 03 for")

    tuple_a = ("blue", "red", "green", "purple")

    print ("for")
    for color in tuple_a:
        print("color : ", color)

    print ("-----------------------------")
    print ("for")

    for i in range(0,len(tuple_a)):
        print("color : ",tuple_a[i])

    print ("-----------------------------")
    print ("While")
    index = 0
    length = len(tuple_a)

    while index < length:
        print("color : ",tuple_a[index])
        index += 1

if __name__ == "__main__":
    main()
