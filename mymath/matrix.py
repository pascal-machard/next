class matrix:
    def __init__(self, l, c):
        self.nl = l
        self.nc = c
        mat = []
        for i in range(l):
            ligne = []
            for j in range(c):
                ligne.append(0)
            mat.append(ligne)
        self.matrix = mat

    def load(self, tableau):  # permet de convertir un 2d-array en matrice
        if len(tableau) != self.nl or len(tableau[0]) != self.nc:
            return ("error : Bad dimensions")
        for i in range(self.nl):
            for j in range(self.nc):
                self.matrix[i][j] = tableau[i][j]

    def __add__(self, other):
        if not isinstance(other, matrix):
            return ("error : You must add matrix with matrix")
        if (self.nl != other.nl or self.nc != other.nc):
            return ("error : You must add same dimension matrix")
        mat = matrix(self.nl, self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                mat.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return mat

    def __iadd__(self, other):
        if (self.nl != other.nl or self.nc != other.nc):
            return ("error : bad dimensions")
        matreturn = self + other
        return matreturn

    def __isub__(self, other):
        if (self.nl != other.nl or self.nc != other.nc):
            return ("error : bad dimensions")
        matreturn = self - other
        return matreturn

    def __sub__(self, other):
        if not isinstance(other, matrix):
            return ("error : You must add matrix with matrix")
        if (self.nl != other.nl or self.nc != other.nc):
            return ("error : You must add same dimension matrix")
        matreturn = matrix(self.nl, self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                matreturn.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return matreturn

    def __mul__(self, other):
        if isinstance(other,matrix):

            if (self.nc != other.nl):
                return ("error: bad dimension")

            result = matrix(other.nc, self.nl)

            for l in range(result.nl):
                for c in range(result.nc):
                    x = 0
                    for ind in range(self.nc):
                        x = x + self.matrix[l][ind] * other.matrix[ind][c]
                    result.matrix[l][c] = x
        else:
            result = matrix(self.nl, self.nc)
            for i in range(self.nl):
                for j in range(self.nc):
                    result.matrix[i][j] = other * self.matrix[i][j]

        return result

    def __eq__(self, other):
        if isinstance(other, matrix):
            return self.matrix == other.matrix

    def __pow__(self, exposant):  # la puissance est définie pour les exposants entiers relatifs
        if not isinstance(exposant, int):
            return ("error : parameter must be integer")
        if self.nl != self.nc:
            return ("error : you must use a square matrix")
        if exposant == 0:
            matreturn = matrix(self.nl, self.nc)
            matreturn.identity()
            return matreturn
        if exposant > 0:
            matreturn = matrix(self.nl, self.nc)
            matreturn.identity()
            for i in range(exposant):
                matreturn = matreturn * self
            return matreturn
        if exposant == -1:
            if self.nl != self.nc:
                return ("error : you must inverse a square matrix")
            ident = matrix(self.nl, self.nc)
            ident.identity()
            matinter = self.augment_c(ident)
            mat1 = matinter.gauss_jordan()
            matreturn = mat1.slice_c(self.nc, mat1.nc + 1)
            return matreturn

        if exposant < -1:
            return (self ** (-1)) ** (-exposant)

    def identity(self):  # charge l'identité dans la matrice si elle est carrée
        if self.nl != self.nc:
            return ("error : identity is square matrix")
        for i in range(self.nl):
            for j in range(self.nc):
                if i == j:
                    self.matrix[i][j] = 1
                else:
                    self.matrix[i][j] = 0

    def zeros(self):
        for i in range(self.nl):
            for j in range(self.nc):
                self[i][j] = 0

    def __len__(self):
        return self.nl * self.nc

    def augment_c(self, other):  # augmente la matrice avec une autre à droite
        if not isinstance(other, matrix) or self.nl != other.nl:
            return "error : you must augment a matrix with a matrix"
        matreturn = matrix(self.nl, (self.nc + other.nc))
        for i in range(self.nl):
            for j in range(self.nc):
                matreturn[i][j] = self[i][j]
            for j in range(other.nc):
                matreturn[i][self.nc + j] = other[i][j]
        return matreturn

    def augment_l(self, other):  # augmente la matrice avec une autre en dessous
        if not isinstance(other, matrix) or self.nc != other.nc:
            return "error : you must augment a matrix with a matrix"
        matreturn = matrix(self.nl + other.nl, self.nc)
        for i in range(self.nl):
            matreturn[i] = self[i]
        for i in range(other.nl):
            matreturn[i + self.nl - 1]
        return matreturn

    def permutation_l(self, ligne1, ligne2):  # permutation de deux lignes entre elles
        if not isinstance(ligne1, int) or not isinstance(ligne2, int):
            return ("error : You must input two int arguments")
        matreturn = matrix(self.nl, self.nc)
        for i in range(self.nl):
            if i == ligne1:
                matreturn[i] = self[ligne2]
            elif i == ligne2:
                matreturn[i] = self[ligne1]
            else:
                matreturn[i] = self[i]
        return matreturn

    def permutation_c(self, colonne1, colonne2):  # permutation de deux colonnes entre elles
        if not isinstance(colonne1, int) or not isinstance(colonne2, int):
            return ("error : you must imput two int arguments")
        matreturn = matrix(self.nl, self.nc)
        for i in range(self.nl):
            for j in range(self.nc):
                if j == colonne1:
                    matreturn[i][j] = self.matrix[i][colonne2]
                elif j == colonne2:
                    matreturn[i][j] = self.matrix[i][colonne1]
                else:
                    matreturn[i][j] = self.matrix[i][j]
        return matreturn

    def transpose(self):  # renvoie la matrice transposée
        matreturn = matrix(self.nc, self.nl)
        for i in range(self.nc):
            for j in range(self.nl):
                matreturn.matrix[i][j] = self.matrix[j][i]
        return matreturn

    def column(self, ind):  # renvoie le ind^ème vecteur colonne
        matreturn = matrix(self.nl, 1)
        for i in range(self.nl):
            matreturn.matrix[i][0] = self.matrix[i][ind]
        return matreturn

    def lign(self, ind):  # revoie le ind^ème vecteur ligne
        matreturn = matrix(1, self.nc)
        for i in range(self.nc):
            matreturn.matrix[0][i] = self.matrix[ind][i]
        return matreturn