import unittest

from facebook.post import post
from facebook.user import user


class UnitestPointFaceBook(unittest.TestCase):
    def setUp(self):
        self.u = user(name="Toto", mail="toto@gmail.com", birthday="03/07/1972")

    def test_user(self):
        assert self.u.name == "Toto"
        assert self.u.mail == "toto@gmail.com"
        assert self.u.birthday == "03/07/1972"

    def test_user_active(self):
        assert self.u.active

    def test_user_zero_friends(self):
        assert self.u.number_of_friend() == 0

    def test_user_one_friends(self):
        u_friend = user(name="Polo", mail="polo@gmail.com", birthday="21/06/1990")
        self.u.add_friend(u_friend)
        assert self.u.number_of_friend() == 1

    def test_user_find_friend(self):
        u_friend = user(name="Polo", mail="polo@gmail.com", birthday="21/06/1990")
        self.u.add_friend(u_friend)
        assert self.u.search_friend("Polo") == u_friend
