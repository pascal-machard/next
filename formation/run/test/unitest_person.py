import math
import unittest

from formation.run.lib.client import Client
from formation.run.lib.person import Person


def who_is_it(p):
    return p.who_is_it()


class UnitestPerson(unittest.TestCase):

    @staticmethod
    def test_simple_person_constructor_base():
        p = Person()
        assert p.first_name == ""
        assert p.last_name == ""
        assert p.age == 0
        return 0

    @staticmethod
    def test_simple_person_constructor_one():
        p = Person("Brown")
        assert p.first_name == "Brown"
        assert p.last_name == ""
        assert p.age == 0
        return 0

    @staticmethod
    def test_simple_person_constructor_two():
        p = Person("Brown", "John")
        assert p.first_name == "Brown"
        assert p.last_name == "John"
        assert p.age == 0
        return 0

    @staticmethod
    def test_simple_person_constructor_three():
        p = Person("Brown", "John", 45)
        assert p.first_name == "Brown"
        assert p.last_name == "John"
        assert p.age == 45
        return 0

    @staticmethod
    def test_simple_person_str():
        p = Person("Brown", "John", 45)
        s = str(p)
        assert s == "Brown John 45 years"

    @staticmethod
    def test_simple_person_fct():
        p = Person("Brown", "John", 45)
        p.inc_age()
        assert str(p) == "Brown John 46 years"

    @staticmethod
    def test_simple_person_who_is_it():
        p = Person()
        assert p.who_is_it() == "I'm a person"

    @staticmethod
    def test_simple_client_constructor_three():
        c = Client("Brown", "John", 45)
        assert c.first_name == "Brown"
        assert c.last_name == "John"
        assert c.age == 45
        assert issubclass(Client, Person)
        assert isinstance(c, Person)

    @staticmethod
    def test_simple_client_who_is_it():
        p = Client()
        assert p.who_is_it() == "I'm a client"

    @staticmethod
    def test_simple_polymorphism_fct():
        p = Person()
        c = Client()

        assert who_is_it(p) == "I'm a person"
        assert who_is_it(c) == "I'm a client"