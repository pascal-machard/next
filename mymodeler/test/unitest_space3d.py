import unittest

from mymath.point3d import Point3D
from mymodeler.landmark3d import Space3D


class UnitestSpace3D(unittest.TestCase):

    @staticmethod
    def test_simple_space_constructor():
        o = Point3D(x=1.0, y=2.0, z=3.0)
        s = Space3D(o, 0.0, 0.0, 0.0)
        assert s.o == o

        return 0
