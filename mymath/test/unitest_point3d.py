import math
import unittest

from mymath.point3d import Point3D


class UnitestPoint3D(unittest.TestCase):

    @staticmethod
    def test_simple_3D_constructor():
        p = Point3D(x=0.0, y=0.0, z=0.0)
        assert p.x == 0.0
        assert p.y == 0.0
        assert p.z == 0.0
        return 0

    @staticmethod
    def test_simple_3D_add():
        a = Point3D(x=1.0, y=2.0, z=3.0)
        b = Point3D(x=4.0, y=5.0, z=6.0)
        c = a + b
        assert c.x == 5.0
        assert c.y == 7.0
        assert c.z == 9.0
        return 0

    @staticmethod
    def test_simple_3D_mul():
        a = Point3D(x=1.0, y=2.0, z=3.0)
        c = a * 2.0
        assert c.x == 2.0
        assert c.y == 4.0
        assert c.z == 6.0
        return 0

    @staticmethod
    def test_simple_3D_pow():
        a = Point3D(x=1.0, y=2.0, z=3.0)
        c = a ** 2.0
        assert c.x == 1.0
        assert c.y == 4.0
        assert c.z == 9.0
        return 0

    @staticmethod
    def test_simple_3D_inv():
        a = Point3D(x=2.0, y=4.0, z=10.0)
        c = a.__invert__()
        assert c.x == 0.5
        assert c.y == 0.25
        assert c.z == 0.10
        return 0

    @staticmethod
    def test_simple_3D_distance():
        a = Point3D(x=1.0, y=1.0, z=1.0)
        b = Point3D(x=2.0, y=3.0, z=4.0)

        assert abs(a.dist(b) - math.sqrt(1 + 4 + 9)) < 0.001
        return 0

    @staticmethod
    def test_simple_3D_middle():
        a = Point3D(x=2.0, y=1.0, z=6.0)
        b = Point3D(x=2.0, y=3.0, z=4.0)
        c = a.middle(b)

        assert c.x == 2
        assert c.y == 2
        assert c.z == 5
        return 0

    @staticmethod
    def test_simple_3D_translation():
        a = Point3D(x=2.0, y=1.0, z=6.0)
        c = a.translation(1.0, 2.0, 3.0)

        assert c.x == 3
        assert c.y == 3
        assert c.z == 9
        return 0

    @staticmethod
    def test_simple_3D_coord():
        a = Point3D(x=2.0, y=1.0, z=6.0)
        assert a.coord() == [2.0, 1.0, 6.0]

    @staticmethod
    def test_simple_3D_coord_homogen():
        a = Point3D(x=2.0, y=1.0, z=6.0)
        assert a.coord_homogen() == [2.0, 1.0, 6.0, 1.0]

