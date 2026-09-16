from business.business import Business
from dao.goncourt_dao import GoncourtDao


class GoncourtBusiness(Business):
    goncourt_dao = GoncourtDao()

    def get_all(self):
        """
        Retrieves all years from the database. that have a goncourt
        :return: list of years of each goncourt
        """
        list_year = self.goncourt_dao.get_all(self.get_connection().cursor())
        return list_year
