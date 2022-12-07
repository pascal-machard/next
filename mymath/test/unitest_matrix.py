import math
import unittest

from mymath.matrix import matrix
from mymath.point3d import Point3D


class UnitestMatrix(unittest.TestCase):

    @staticmethod
    def test_simple_matrix_constructor():
        m = matrix(2, 3)
        assert m.nl == 2
        assert m.nc == 3
        return 0

    @staticmethod
    def test_simple_matrix_load():
        m = matrix(2, 3)
        m.load([[1.0, 0.0, 2.0], [0.0, 2.0, 1.0]])
        assert m[0][0] == 1.0
        assert m[0][1] == 0.0
        assert m[0][2] == 2.0
        assert m[1][0] == 0.0
        assert m[1][1] == 2.0
        assert m[1][2] == 1.0
        return 0

    @staticmethod
    def test_simple_matrix_load():
        m = matrix(2, 3)
        m.load([[1.0, 0.0, 2.0], [0.0, 2.0, 1.0]])
        m.zeros()
        assert m[0][0] == 0.0
        assert m[0][1] == 0.0
        assert m[0][2] == 0.0
        assert m[1][0] == 0.0
        assert m[1][1] == 0.0
        assert m[1][2] == 0.0
        return 0

    @staticmethod
    def test_simple_matrix_load():
        m = matrix(2, 3)
        m.load([[1.0, 0.0, 2.0], [0.0, 2.0, 1.0]])
        n = matrix(2, 3)
        n.load([[1.0, 0.0, 2.0], [0.0, 2.0, 1.0]])
        assert m == n
        return 0

    @staticmethod
    def test_simple_matrix_add():
        m = matrix(2, 3)
        m.load([[1.0, 0.0, 2.0], [0.0, 2.0, 1.0]])
        n = matrix(2, 3)
        n.load([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
        l = m + n
        assert l.matrix[0][0] == 2.0
        assert l.matrix[0][1] == 1.0
        assert l.matrix[0][2] == 3.0
        assert l.matrix[1][0] == 1.0
        assert l.matrix[1][1] == 3.0
        assert l.matrix[1][2] == 2.0
        return 0

    @staticmethod
    def test_simple_matrix_subb():
        m = matrix(2, 3)
        m.load([[1.0, 0.0, 2.0], [0.0, 2.0, 1.0]])
        n = matrix(2, 3)
        n.load([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
        l = m - n
        assert l.matrix[0][0] == 0.0
        assert l.matrix[0][1] == -1.0
        assert l.matrix[0][2] == 1.0
        assert l.matrix[1][0] == -1.0
        assert l.matrix[1][1] == 1.0
        assert l.matrix[1][2] == 0.0
        return 0

    @staticmethod
    def test_simple_matrix_subb():
        m = matrix(3, 3)
        m.identity()
        assert m.matrix[0][0] == 1.0
        assert m.matrix[0][1] == 0.0
        assert m.matrix[0][2] == 0.0
        assert m.matrix[1][0] == 0.0
        assert m.matrix[1][1] == 1.0
        assert m.matrix[1][2] == 0.0
        assert m.matrix[2][0] == 0.0
        assert m.matrix[2][1] == 0.0
        assert m.matrix[2][2] == 1.0
        return 0

    @staticmethod
    def test_simple_matrix_lign():
        m = matrix(3, 3)
        m.identity()
        n = m.lign(0)
        assert n.matrix[0][0] == 1.0
        assert n.matrix[0][1] == 0.0
        assert n.matrix[0][2] == 0.0
        return 0

    @staticmethod
    def test_simple_matrix_column():
        m = matrix(3, 3)
        m.identity()
        n = m.column(1)
        assert n.matrix[0][0] == 0.0
        assert n.matrix[1][0] == 1.0
        assert n.matrix[2][0] == 0.0
        return 0

    @staticmethod
    def test_simple_transpos():
        m = matrix(3, 3)
        m.load([[1.0, 0.0, 2.0],
                [0.0, 2.0, 1.0],
                [1.0, 0.0, 2.0]])
        t = matrix(3, 3)
        t.load([[1.0, 0.0, 1.0],
                [0.0, 2.0, 0.0],
                [2.0, 1.0, 2.0]])
        n = m.transpose()
        assert n == t
        return 0

    @staticmethod
    def test_simple_multiplication_double():
        m = matrix(3, 3)
        m.load([[1.0, 0.0, 2.0],
                [0.0, 2.0, 1.0],
                [1.0, 0.0, 2.0]])
        r = matrix(3, 3)
        r.load([[2.0, 0.0, 4.0],
                [0.0, 4.0, 2.0],
                [2.0, 0.0, 4.0]])
        n = m * 2
        assert n == r
        return 0

    @staticmethod
    def test_simple_multiplication_matrice():
        m = matrix(3, 2)
        m.load([[5.0, 1.0],
                [2.0, 3.0],
                [3.0, 4.0]])
        n = matrix(2, 3)
        n.load([[1.0, 2.0, 0.0],
                [4.0, 3.0, -1.0]])
        o = m * n
        r = matrix(3, 3)
        r.load([[9.0, 13.0, -1.0],
                [14.0, 13.0, -3.0],
                [19.0, 18.0, -4.0]])
        assert o == r
        return 0