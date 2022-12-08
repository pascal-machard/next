
import unittest

class UnitestDico(unittest.TestCase):

    @staticmethod
    def test_dico_base_a():
        dico = {"A":1,"B":5,"C":10}
        assert dico["A"] == 1
        assert dico["B"] == 5
        assert dico["C"] == 10

    @staticmethod
    def test_dico_base_b():
        dico = {}
        dico["C"] = 10
        assert dico["C"] == 10

    @staticmethod
    def test_dico_base_clear():
        dico = {"A":1,"B":5,"C":10}
        dico.clear()
        assert len(dico) == 0

    @staticmethod
    def test_dico_base_copy():
        dico = {"A":1,"B":5,"C":10}
        dico_bis = dico.copy()
        dico.clear()
        assert len(dico_bis) == 3

    @staticmethod
    def test_dico_base_get():
        dico = {"A":1,"B":5,"C":10}
        assert dico.get("B") == 5

    @staticmethod
    def test_dico_base_keys():
        dico = {"A": 1, "B": 5, "C": 10}
        d = dico.keys()
        assert dico.items()[1] == "B"

