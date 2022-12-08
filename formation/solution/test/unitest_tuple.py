
import unittest

class UnitestTuple(unittest.TestCase):

    @staticmethod
    def test_tuple_base_A():
        a = (1, 2, 5)
        assert a[0] == 1
        assert a[1] == 2
        assert a[2] == 5

    @staticmethod
    def test_tuple_base_B():
        a = (1,)
        assert a[0] == 1

    @staticmethod
    def test_tuple_base_C():
        a = ("A","B","C")
        assert a[0] == "A"
        assert a[1] == "B"
        assert a[2] == "C"
