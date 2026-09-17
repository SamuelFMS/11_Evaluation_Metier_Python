import unittest
from random import Random

from business.business import Business
from business.vote_business import VoteBusiness
from models.vote import Vote


Business.set_connection("goncourt_test", "goncourt_test")

class TestVote(unittest.TestCase):
    def setUp(self):
        """Préparé avant chaque test"""
        self.vote_business = VoteBusiness()

    def test_get_vote_for_year(self):
        list_vote: list[Vote] = self.vote_business.get_vote_for_year(2026)
        assert len(list_vote) > 0
        for vote in list_vote:
            assert vote.id_vote

    def test_set_vote_for_year(self):
        random:Random = Random()
        list_vote = self.vote_business.get_vote_for_year(2026)
        random_int = random.randint(1, 1000)
        list_vote[0].number_of_votes = random_int
        self.vote_business.set_note(list_vote[0])
        new_list_vote = self.vote_business.get_vote_for_year(2026)
        assert new_list_vote[0].number_of_votes == random_int