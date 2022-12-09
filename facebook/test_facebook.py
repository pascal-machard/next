import unittest

from facebook.facebook import user


class UnitestPoint3D(unittest.TestCase):

    @staticmethod
    def test_user():
        u = user(name="Toto",mail="toto@gmail.com",birsday="03/07/1972")
        assert u.name == "Toto"
        assert u.mail == "toto@gmail.com"
        assert u.birhday == "03/07/1972"

