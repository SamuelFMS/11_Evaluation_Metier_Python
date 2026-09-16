from business.business import Business
from dao.goncourt_dao import GoncourtDao
from dao.round_dao import RoundDao
from models.round import Round


class RoundBusiness(Business):
    round_dao: RoundDao = RoundDao()
    goncourt_dao: GoncourtDao = GoncourtDao()

    def get_round_for_year(self, year: int) -> list[Round]:
        """
        Get a round from the database
        :param year:
        :return:
        """
        return self.round_dao.get_all_by_related_id(self.get_connection().cursor(), self.goncourt_dao, year)
