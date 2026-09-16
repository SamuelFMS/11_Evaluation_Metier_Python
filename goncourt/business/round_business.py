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

    def get_number(self, id_round: int) -> int:
        result = self.round_dao.get_number(self.get_connection().cursor(), id_round)
        assert result is not None
        return result

    def get_round_by_id(self, id_round: int) -> Round:
        result = self.round_dao.get_by_id(self.get_connection().cursor(), id_round)
        assert result
        return result
