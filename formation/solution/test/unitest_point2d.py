import math
import unittest

from formation.solution.lib.point2d import Point2D


class UnitestPoint2D(unittest.TestCase):

    @staticmethod
    def test_simple_2D_constructor():
        p = Point2D(x=0.0, y=0.0)
        assert p.x == 0.0
        assert p.y == 0.0
        return 0

    @staticmethod
    def test_simple_2D_add():
        a = Point2D(x=1.0, y=2.0)
        b = Point2D(x=4.0, y=5.0)
        c = a + b
        assert c.x == 5.0
        assert c.y == 7.0
        return 0

    @staticmethod
    def test_simple_2D_mul():
        a = Point2D(x=1.0, y=2.0)
        c = a * 2.0
        assert c.x == 2.0
        assert c.y == 4.0
        return 0

    @staticmethod
    def test_simple_2D_pow():
        a = Point2D(x=1.0, y=2.0)
        c = a ** 2.0
        assert c.x == 1.0
        assert c.y == 4.0
        return 0

    @staticmethod
    def test_simple_2D_inv():
        a = Point2D(x=2.0, y=4.0)
        c = a.__invert__()
        assert c.x == 0.5
        assert c.y == 0.25
        return 0

    @staticmethod
    def test_simple_2D_distance():
        a = Point2D(x=1.0, y=1.0)
        b = Point2D(x=2.0, y=3.0)

        assert abs(a.dist(b) - math.sqrt(1 + 4)) < 0.001
        return 0

    @staticmethod
    def test_simple_2D_middle():
        a = Point2D(x=2.0, y=1.0)
        b = Point2D(x=2.0, y=3.0)
        c = a.middle(b)

        assert c.x == 2
        assert c.y == 2
        return 0

    @staticmethod
    def test_simple_2D_translation():
        a = Point2D(x=2.0, y=1.0)
        c = a.translation(1.0, 2.0)

        assert c.x == 3
        assert c.y == 3
        return 0

    @staticmethod
    def test_simple_2D_coord():
        a = Point2D(x=2.0, y=1.0)
        assert a.coord() == [2.0, 1.0]

    @staticmethod
    def test_simple_2D_coord_homogen():
        a = Point2D(x=2.0, y=1.0)
        assert a.coord_homogen() == [2.0, 1.0, 1.0]

