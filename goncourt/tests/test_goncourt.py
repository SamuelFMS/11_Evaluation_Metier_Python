import unittest

from business.business import Business
from business.goncourt_business import GoncourtBusiness

Business.set_connection("goncourt_test", "goncourt_test")


class TestRound(unittest.TestCase):
    def setUp(self):
        """Préparé avant chaque test"""
        self.goncourt_business = GoncourtBusiness()

    def test_get_round_for_year(self):
        results = self.goncourt_business.get_all()
        assert len(results) == 1
        assert results[0].year == 2026
