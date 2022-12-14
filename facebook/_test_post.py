import unittest

from facebook.post import post
from facebook.user import user


class UnitestFaceBookUser(unittest.TestCase):
    def setUp(self):
        self.u_toto = user(name="Toto", mail="toto@gmail.com", birthday="03/07/1972")
        self.u_tata = user(name="Tata", mail="tata@gmail.com", birthday="12/09/1989")
        self.u_titi = user(name="Titi", mail="titi@gmail.com", birthday="03/03/2000")

    def test_post_create(self):
        post_new = post(title="post exp", content="abcdefghijklmnopqrstuvwxyz")
        assert self.u_toto.number_of_post() == 0
        self.u_toto.add_post(post_new)
        assert self.u_toto.number_of_post() == 1

    def test_post_like(self):
        post_new = post(title="post exp", content="abcdefghijklmnopqrstuvwxyz")
        post_new.add_like(":(", self.u_toto, "21/11/22 09:12:30")
        post_new.add_like(":)", self.u_tata, "23/11/22 10:45:12")
        post_new.add_like(":)", self.u_titi, "23/11/22 17:23:10")
        assert post_new.number_of_like() == 3
        assert len(post_new.get_like(":)")) == 2
        assert len(post_new.get_like_date("23/11/22")) == 2
