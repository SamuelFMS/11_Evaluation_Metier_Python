import unittest

from business.business import Business
from business.novel_business import NovelBusiness
from models.novel import Novel

Business.set_connection("goncourt_test", "goncourt_test")


class TestNovel(unittest.TestCase):
    def setUp(self):
        """Préparé avant chaque test"""
        self.novel_business = NovelBusiness()

    def test_novel_get_all(self):
        results = self.novel_business.get_all()
        assert len(results) > 0
        for result in results:
            assert type(result) == Novel
            assert result.id_novel is not None

    def test_novel_get_all_from_round(self):
        results = self.novel_business.get_all_from_round(1)
        assert len(results) > 0
        for result in results:
            assert type(result) == Novel
            assert result.id_novel is not None

    def test_novel_add_novel_to_round(self):
        results = self.novel_business.add_novel_to_round(1, 1, 2026)
        assert results

    def test_novel_remove_novel_from_round(self):
        results = self.novel_business.remove_novel_from_round(1, 1, 2026)
        assert results
