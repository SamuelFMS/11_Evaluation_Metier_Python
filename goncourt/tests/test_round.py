import unittest

from business.business import Business
from business.round_business import RoundBusiness

Business.set_connection("goncourt_test", "goncourt_test")


class TestRound(unittest.TestCase):
    def setUp(self):
        """Préparé avant chaque test"""
        self.round_business = RoundBusiness()

    def test_get_round_for_year(self):
        results = self.round_business.get_round_for_year(2026)
        assert len(results) == 3

    def test_get_number(self):
        assert self.round_business.get_number(3) == 3

    def test_get_round_by_id(self):
        assert self.round_business.get_round_by_id(3).id_round == 3