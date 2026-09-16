from typing import List

from business.business import Business
from business.novel_business import NovelBusiness
from dao.goncourt_dao import GoncourtDao
from dao.vote_dao import VoteDao
from models.vote import Vote


class VoteBusiness(Business):
    vote_dao = VoteDao()
    goncourt_dao: GoncourtDao = GoncourtDao()
    novel_business: NovelBusiness = NovelBusiness()

    def get_vote_for_year(self, year: int) -> list[Vote]:
        """
        Get all votes for a given year/goncourt
        :param year:
        :return:
        """
        cursor = self.get_connection().cursor()
        list_votes: List[Vote] = self.vote_dao.get_all_by_related_id(cursor, self.goncourt_dao, year)
        for vote in list_votes:
            vote.novel = self.novel_business.get_by_id(vote.novel_id)
        return list_votes

    def set_note(self, vote: Vote) -> bool:
        """
        Update a note to the vote
        :param vote:
        :return:
        """
        if (self.vote_dao.update_note(self.get_connection().cursor(), vote)):
            self.get_connection().commit()
            return True
        else:
            return False
