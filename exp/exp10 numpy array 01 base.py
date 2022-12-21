import numpy as np

def main():

    print("exemple 09 numpy array 01 base")

    a = np.array([4, 7, 9])
    print("Tableau :", a)
    print("Nombre d'éléments : ", np.size(a))

    b = np.array([[4, 7, 9], [12, -2, 7]])
    print("Tableau :", b)
    print("Nombre d'éléments : ", np.size(b))
    print("Dimension : ", np.shape(b))


if __name__ == "__main__":
    main()
